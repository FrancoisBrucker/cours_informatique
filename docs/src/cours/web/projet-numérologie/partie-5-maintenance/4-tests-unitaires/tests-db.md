---
layout: layout/post.njk

title: "Projet numérologie : partie 5 / tests unitaires : base de données"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Tester les appels en base ne peut se faire avec la base de production ou de développement. Deux solution sont possible pour effectuer les tests :

1. avoir une base de test qui sera réinitialisée entre chaque test pour isoler les testes des uns des autres.
2. on simule une base de donnée ([mock](<https://fr.wikipedia.org/wiki/Mock_(programmation_orient%C3%A9e_objet)>))

## Environnement de test

Créons une base de donnée en mémoire pour notre environnement de tests.

Dans le fichier `db.js`{.fichier}, on remplace la création de la constante sequelize par :

```js
// ...

let env = process.env.NODE_ENV || "development";

let storage;

if (env === "test") {
  storage = ":memory:";
} else {
  storage = path.join(__dirname, "db.sqlite");
}

const sequelize = new Sequelize({
  dialect: "sqlite",
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
import request from "supertest";

import { app } from "../app.js";
import db from "../db.js";

let user;
let server;

beforeAll(async () => {
  user = await request.agent(app);
  server = await app.listen(3001); // test en parallèle et parfois 3000 et 3001

  await db.sequelize.sync({ force: true });
});

afterAll(async () => {
  await server.close();
});

describe("prénoms", () => {
  beforeEach(async () => {
    await db.model.Prénoms.sync({ force: true });
    await db.model.Signification.sync({ force: true });
  });

  test("Prénom read", async () => {
    await db.model.Prénoms.create({
      prénom: "Carole",
    });

    await db.model.Signification.create({
      message: "Quatre",
      nombre: 4,
    });
    await user
      .get(encodeURI("/prénom?valeur=Carole"))
      .expect(200)
      .expect("Content-Type", /json/)
      .expect(function (res) {
        expect(res.body).toEqual({
          chiffre: 4,
          message: "Quatre",
          prénom: "Carole",
        });
      });
  });
});
```

Quelques subtilités :

- on a changé le port du serveur en 3001. Comme les tests s'effectuent en parallèle, il est parfois possible que les 2 tests supertests soient exécutées ensembles
- nos tests sont passés en asynchrones
- on test le résultat de la requête. C'est à priori inutile si on ne teste que la route. Comme ici, le test fait office de test de route et de fonctionnalité, on le laisse.
