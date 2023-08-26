---
layout: layout/post.njk

title: "Projet numérologie : partie 5 / tests unitaires : base de données"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Tests des appels à la base de données.

<!-- fin résumé -->

Tester les appels en base ne peut se faire avec la base de production ou de développement. Deux solution sont possible pour effectuer les tests :

1. avoir une base de test qui sera réinitialisée entre chaque test pour isoler les testes des uns des autres.
2. on simule une base de donnée ([mock](https://fr.wikipedia.org/wiki/Mock_(programmation_orient%C3%A9e_objet)))

## Environnement de test

Créons une base de donnée en mémoire pour notre environnement de tests.

Dans le fichier `db.js`{.fichier}, on remplace la création de la constante sequelize par :

```js
// ...

let env = process.env.NODE_ENV || 'development';

let storage;

if (env === "test") {
  storage = ":memory:"
} else {
  storage = path.join(__dirname, 'db.sqlite')
}

const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: storage,
  logging: (msg) => logger.info(msg),
});

// ...

```

## Tests

On peut maintenant créer nos tests.

1. avant tous les tests : crée une base
2. avant chaque test : on vide la base des données testées et on crée ce dont on a besoin dans chaque test
3. utilisation de supertest pour tester l'accès à la base via les routes
  
Fichier `__tests__/db.js`{.fichier} :

```js
import request from 'supertest';


import { app } from '../app.js';
import db from "../db.js"

let user;
let server;

beforeAll(async () => {
    user = await request.agent(app);
    server = await app.listen(3001); // test en parallèle et parfois 3000 et 3001

    await db.sequelize.sync({ force: true })
});


afterAll(async () => {
    await server.close();
});


describe('prénoms', () => {
    beforeEach(async () => {
        await db.model.Prénoms.sync({ force: true })
        await db.model.Signification.sync({ force: true })
    });


    test('Prénom read', async () => {
        await db.model.Prénoms.create({
            prénom: "Carole"
        })

        await db.model.Signification.create({
            message: "Quatre",
            nombre: 4,
        })    
        await user
            .get(encodeURI('/prénom?valeur=Carole'))
            .expect(200)
            .expect('Content-Type', /json/)
            .expect(function (res) {
                expect(res.body).toEqual({"chiffre": 4, "message": "Quatre", "prénom": "Carole"})
            })
    })

})
```

Quelques subtilités :

* on a changé le port du serveur en 3001. Comme les tests s'effectuent en parallèle, il est parfois possible que les 2 tests supertests soient exécutées ensembles
* nos tests sont passés en asynchrones
* on test le résultat de la requête. C'est à priori inutile si on ne teste que la route. Comme ici, le test fait office de test de route et de fonctionnalité, on le laisse.

## Mock

> TBD : en commonJS.
> à refaire en ES6 <https://jestjs.io/fr/docs/es6-class-mocks>

La seconde solution est de ne pas toucher la base de donnée et de remplacer un appel de la base de donnée par notre propre code.

Pour cela on utilise le fait qu'en javascript, une fois un module importé une fois, il n'est plus lu ensuite, on ne fait que rendre les objets exportés. De là, on [mock](https://fr.wikipedia.org/wiki/Mock_(programmation_orient%C3%A9e_objet)) le module ou une partie de celui ci en l'important une première fois avant tout le monde. Lorsque les autres fichiers importeront le module, c'est notre mock qu'ils vont importer.

On a utilisé cette technique pour tester la route `/api/prenoms/read'`en mockant la partie `model` du module db. Fichier `__test__/donnees.mock.js`{.fichier} :

```js
const request = require('supertest');



jest.mock("../db", () => {
    const originalModule = jest.requireActual('../db');
    return {
        __esModule: true,
        ...originalModule,
        model: {
            Prenoms: {
                findAll: () => {
                    return new Promise((resolve, reject) => {
                        resolve([{ prenom: "toto" }])
                    })
                }
            }
        },
    };
});

const numérologie = require("../back/numérologie")
const app = require('../app')

test('GET /api/prenoms/read', (done) => {

    request(app)
        .get("/api/prenoms/read")
        // .expect("Content-Type", "application/json; charset=utf-8")
        .expect((res) => {
            expect(res.body).toEqual([{
                prenom: "toto",
                chiffre: numérologie.chiffre("toto")
            }])
        })
        .end((err, res) => {
            if (err) {
                return done(err)
            }
            return done()
        })

})
```

On a dans le code ci-dessus remplacé la partie model du retour du `require("db")` par une [promesse](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Promise) qui rend toujours `[{ prenom: "toto" }]`. IL n'y a alors plus d'appel à la base de donnée dans la route et le code se poursuit jusqu'à renvoyer la liste qui est notre test.

> La technique de mock est très puissante ! Elle permet de tester presque tout ce qu'on veut sans soucis. Lisez [la documentation de jest](https://jestjs.io/docs/mock-functions) pour plus de renseignements sur ce qu'on peut faire avec.
