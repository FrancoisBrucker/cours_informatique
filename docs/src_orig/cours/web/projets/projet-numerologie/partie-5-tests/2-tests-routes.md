---
layout: layout/post.njk 
title:  "Projet numérologie : partie 5 / tests de routes"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numérologie/index.md %}) / [partie 5]({% link cours/web/projets/numérologie/partie-5-tests/index.md %}) / [tests fonctionnels]({% link cours/web/projets/numérologie/partie-5-tests/2-tests-routes.md %})
{.chemin}

Le tests des routes du serveur nous permet de garantir que l'api fonctionne bien. C'est différent des tests unitaires car il faut que le serveur tourne pour les faire.

## mise en place

On va utiliser la bibliothèque [supertest](https://github.com/visionmedia/supertest#readme) pour gérer le serveur. Supertest va créer une instance de notre serveur pour chaque test, cela nous permettra de faire plein de test en même temps (il va lancer chaque serveur sur un autre port).

Commençons pas l'installer :

```shell
npm install supertest --save-dev
```

Pour pouvoir l'utiliser, il faut séparer l'application (express) du serveur proprement dit. On va donc créer un fichier *"numérologie/app.js"* qui contiendra toute notre application :

```js
const path = require('path')

const express = require('express')
const app = express()

const routes = require("./routes")

app.use(function (req, res, next) {
    date = new Date(Date.now())
    console.log('Time:', date.toLocaleDateString(), date.toLocaleTimeString(), "; url :", req.url);
    next(); // sans cette ligne on ne pourra pas poursuivre.
})

app.use("/static", express.static(path.join(__dirname, '/static')))

app.get('/', (req, res) => {
    res.redirect(301, '/static/index.html')
})

app.use('/', routes)

app.use(function (req, res) {
    console.log("et c'est le 404 : " + req.url);

    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/html');

    res.end("<html><head><title>la quatre cent quatre</title></head><body><h1>Et c'est la 404.</h1><img  src=\"https://www.leblogauto.com/wp-content/uploads/2020/04/Peugeot-404-1.jpg\" /></body></html>");

})

module.exports = app
```

et ne laisser que le lancement du serveur à *"numérologie/index.js"* :

```js
const app = require("./app")

const hostname = '127.0.0.1';
const port = 3000;

app.listen(port, hostname);
console.log(`Server running at http://${hostname}:${port}/`);
```

C'est *"numérologie/app.js"* que nous importerons pour nos tests.

## tests

### premier test

On va faire un premier test pour voir si on arrive à mettre en place tout ça, dans un fichier *"\_\_test\_\_/routes.text.js"* :

```js
const request = require('supertest');

const app = require('../app')

test("GET /", (done) => {
    request(app)
        .get("/")
        .expect("Content-Type", "text/plain; charset=utf-8")
        .expect(301)
        .end((err, res) => {
            if (err) {
                return done(err)
            }
            return done()
        })
})
```

Plusieurs choses :

* on a passé un paramètre (`done`) dans la fonction de test. Ce paramètre est exécuté en fin de test pour montrer que le test est fini. C'est la façon qu'à jest de traiter les [tests de fonctions asynchrones](https://jestjs.io/docs/asynchronous), sinon il n'a aucun moyen de savoir si un test est fini ou pas.
* on passe l'application à supertest (`request(app)`) pour créer un serveur qu'on interroge ensuite.
* n'oubliez pas de finir par `.end` pour récupérer les erreurs s'il y en a et exécuter `done` pour la fin de test.

### fichiers statiques

Ajoutons les tests des autres routes statiques. On va ajouter une autre bibliothèque, [jsdom](https://github.com/jsdom/jsdom) (`npm install --save-dev jsdom`), qui nous permettra de tester le contenu du html :

```js
const request = require('supertest');
const { JSDOM } = require('jsdom')

const app = require('../app')

describe("routes statiques", () => {
    test("GET /", (done) => {
        request(app)
            .get("/")
            .expect("Content-Type", "text/plain; charset=utf-8")
            .expect(301)
            .end((err, res) => {
                if (err) {
                    return done(err)
                }
                return done()
            })
    })

    test("GET /index.html 404", (done) => {
        request(app)
            .get("/index.html")
            .expect(404)
            .end((err, res) => {
                if (err) {
                    return done(err)
                }
                return done()
            })
    })

    test("GET /static/index.html", (done) => {
        request(app)
            .get("/static/index.html")
            .expect("Content-Type", "text/html; charset=UTF-8")
            .expect(200)
            .end((err, res) => {
                if (err) {
                    return done(err)
                }
                return done()
            })
    })
    test("GET /static/prenoms.html", (done) => {
        request(app)
            .get("/static/prenoms.html")
            .expect("Content-Type", "text/html; charset=UTF-8")
            .expect(200)
            .expect((res) => {
                dom = new JSDOM(res.text)
                expect(dom.window.document.querySelector("#main > p").textContent).toBe("Chargement des prénoms...")
            })
            .end((err, res) => {
                if (err) {
                    return done(err)
                }
                return done()
            })
    })
})
```

> On aura tendance à plutôt placer en test fonctionnels les tests qui vérifient du html. On l'a fait ici pour vous introduire la bibliothèque jsdom qui est très pratique

## tests de base de données

Il nous reste deux routes à tester à faire qui concernent les bases de données. On va traiter ces deux cas différemment.

### mock

La première solution est de ne pas toucher la base de donnée et de remplacer un appel de la base de donnée par notre propre code.

Pour cela on utilise le fait qu'en javascript, une fois un module importé une fois, il n'est plus lu ensuite, on ne fait que rendre l'objet `module.exports`. De là, on [mock](https://fr.wikipedia.org/wiki/Mock_(programmation_orient%C3%A9e_objet)) le module ou une partie de celui ci en l'important une première fois avant tout le monde. Lorsque les autres fichiers importeront le module, c'est notre mock qu'ils vont importer.

On a utilisé cette technique pour tester la route `/api/prenoms/read'`en mockant la partie `model` du module db. Fichier *"numérologie/\_\_test\_\_/donnees.test.js"* :

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

### environnement/base de test

Lorsque l'on a de nombreux appel différent à la base de donnée, il est illusoire de tout mocker. On utilise alors une base de donnée spécifique aux tests. Ceci permet de plus de ne pas toucher à la base de donnée de production, ce qui est indispensable pour garantir la répétabilité des tests (et ne pas casser la production accessoirement).

#### base de test

On va commencer par différentier la base selon l'environnement d'exécution. Fichier *"numérologie/db.js"* :

```js
//...

let env = process.env.NODE_ENV || 'dev'

if (env == 'test') {
  sequelize = new Sequelize('sqlite::memory:');
} else {
  sequelize = new Sequelize({
    dialect: 'sqlite',
    storage: path.join(__dirname, 'db.sqlite')
  });
}

// ...
```

Si l'on est dans un environnement de test on crée un base en mémoire et sinon on utilise la base normale.

On place l'environnement :

* soit en assignant une valeur à la variable `process.env.NODE_ENV` ([process](https://nodejs.org/api/process.html#process) est bibliothèque globale à node et on peut mettre ce qu'on veut comme attribut à `env`)
* soit en exécutant le serveur en mettant le nom de la variable avant : `TRUC=3 npm start`. Dans le serveur, la variable `process.env.TRUC` vaudra 3.
* soit en créant une variable d'environnement dans le shell puis en exécutant le serveur (dépend du shell. En `zsh` : `export NODE_ENV="test"`)

Nous allons utiliser la première solution.

> On peut choisir ce qu'on veut comme variable d'environnement. `NODE_ENV`, est la variable usuellement utilisée, [parmi d'autres](https://www.twilio.com/blog/working-with-environment-variables-in-node-js-html)

#### tests avec une nouvelle base

Le fichier de test ci-après commence par placer l'environnement d'exécution à `"test"` puis on met en place plusieurs [fonctions spéciales de jest](https://jestjs.io/docs/setup-teardown) qui permettent d'exécuter des fonctions à des moments précis. Ici nous avons besoin d'exécuter une fonction avant chaque tests (la synchronisation et la mise à zérode la base).

Il est important de remettre à zéro la base de données à chaque test pour garantir l'indépendance des tests et leurs répétabilités.

Fichier *"numérologie/\_\_tests\_\_/prenoms.test.js"* :

```js
const request = require('supertest');

process.env.NODE_ENV = 'test'

const db = require("../db")
const app = require('../app');

beforeEach(async () => {
    await db.sequelize.sync({force: true})
    for (i=1 ; i <10 ; i +=1) {
        await db.model.Signification.create({
            message: i,
            nombre: i,
        })
    }
})

test('GET /prénom?valeur=toto pas de prénom', (done) => {
    request(app)
        .get(encodeURI("/prénom") + "?valeur=toto")
        .expect(200)
        .expect((res) => {
            expect(res.body).toEqual({"prénom":"toto","chiffre":4,"message":"4"})
        })
        .end((err, res) => {
            if (err) {
                return done(err)
            }
            return done()
        })
})
```

> On a qu'un seul test donc le `beforeEach` est théorique, mais c'est l'idée.
