---
layout: layout/post.njk

title: "Projet numérologie : partie 5 / tests unitaires : routes"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Tests de routes.

<!-- fin résumé -->

On a déjà un peu regardé les route avec [postman](../../3-postman){.interne}, mais ce n'est pas un test unitaire proprement dit, car il faut tout tester à la main. Pour automatiser tout ça nous allons utiliser la bibliothèque [supertest](https://github.com/visionmedia/supertest#readme) pour gérer le serveur. Supertest va créer une instance de notre serveur pour chaque test, cela nous permettra de faire plein de test en même temps (il va lancer chaque serveur sur un autre port).

## Installation

```
npm install --save-dev supertest
```

## Utilisation

{% lien %}
[Un tutoriel](https://dev.to/nedsoft/testing-nodejs-express-api-with-jest-and-supertest-1km6)
{% endlien %}

On teste toutes les routes du serveur pour être sur de ne pas avoir de 404. Ce n'est pas la peine de tester l'algorithmie des routes s'il y en a, puisque ceci est fait avec des tests unitaires.

### Séparer routes et serveur

Pour que supertest fonctionne, il faut pouvoir lancer le serveur à la volée ce qui est impossible actuellement puisque `index.js`{.fichier} crée les routes et lance le serveur tout seul. On sépare donc tout ça en deux fichiers.

`app.js`{.fichier} qui crée les routes :

```js
import { fileURLToPath } from 'url';
import path from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);


import express from 'express';
const app = express()

import {router as routes} from "./routes/index.js";

import { logger } from './logger.js';

app.use(function (req, res, next) {
    logger.http(req.url)
    next(); // sans cette ligne on ne pourra pas poursuivre.
})

app.use("/static", express.static(path.join(__dirname, '/static')))

app.get('/', (req, res) => {
    res.redirect(301, '/static/index.html')
})

app.use('/', routes)

app.use(function (req, res) {
    logger.info("et c'est le 404 : " + req.url);

    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/html');

    res.end("<html><head><title>le quatre cent quatre</title></head><body><h1>Et c'est le 404.</h1></body></html>");

})

export { app };

```

Et `index.js`{.fichier} qui ne fait que lancer le serveur :

```js
import { app } from "./app.js"

import { logger } from './logger.js';

const hostname = '127.0.0.1';
const port = 3000;


app.listen(port, hostname);
logger.info(`Start server at http://${hostname}:${port}/`)

```

### Tests

Créons notre fichier de tests de routes `__tests__/routes.js`{.fichier} qui teste qu'il y a une redirection vers `/static/index/html` et que les 404 sont mis en œuvre :

```js
import request from 'supertest';

import { app } from '../app.js';

let user;
let server;

beforeAll(async () => {
    user = await request.agent(app);
    server = await app.listen(3000);
});

afterAll(async () => {
    await server.close();
});


test('GET index.html', (done) => {
    user
        .get('/')
        .expect(301)
        .expect(function(res) {
            expect(res.headers.location).toBe('/static/index.html')
        })
        .end((err, res) => {
            if (err) {
                return done(err);
            }
            done()
        })
})

test('GET 404', (done) => {
    user
        .get('/not here')
        .expect(404)
        .end((err) => {
            done(err)
        })
})

```

On utilise les méthodes `beforeAll`{.language-} et `afterAll`{.language-} pour gérer la création (avant tous les tests) et la suppression du serveur (après tous les tests).

Gestion des promesses :

* on a passé un paramètre (`done`) dans la fonction de test. Ce paramètre est exécuté en fin de test pour montrer que le test est fini. C'est la façon qu'à jest de traiter les [tests de fonctions asynchrones](https://jestjs.io/docs/asynchronous), sinon il n'a aucun moyen de savoir si un test est fini ou pas.
* on passe l'application à supertest (`request.agent(app)`) pour créer un serveur qu'on interroge ensuite.
* n'oubliez pas de finir par `.end` pour récupérer les erreurs s'il y en a et exécuter `done` pour la fin de test.

### Environnement de tests

On voit qu'il y a un soucis, les logs sont activés et écrivent des choses dans les fichiers de logs alors que c'est des tests.

Il faut créer des environnement différents pour la production et les tests.

{% lien %}

* <https://rafaelalmeidatk.com/blog/why-you-should-not-use-a-custom-value-with-node-env>
* <https://nodejs.dev/fr/learn/how-to-read-environment-variables-from-nodejs/>

{% endlien %}

Commençons par changer le logger si on est en mode de test. Modifions le fichier `logger.js`{.fichier} :

```js
import winston from 'winston';

let env = process.env.NODE_ENV || 'development';

let logger_choice;

if (env === "test") {
  logger_choice = winston.createLogger({
    silent: true,
  })
} else {
  logger_choice = winston.createLogger({
    level: 'verbose',
    format: winston.format.combine(
      winston.format.timestamp(),
      winston.format.json()),
    transports: [
      new winston.transports.Console(),
      new winston.transports.File({ filename: 'error.log', level: 'error' }),
      new winston.transports.File({ filename: 'http.log', level: 'http' }),
    ],
  });
}

export const logger = logger_choice;
```

Regardez comment l'environnement est géré dans ce fichier : on utilise la bibliothèque [process](https://nodejs.org/api/process.html#process) qui contient — entre autre — les variables d'environnement. Par défaut jest exécute les tests en mode `"test"`{.language-}, donc en appelant nos tests, il ne devrait plus y avoir de logs affiché.

Changeons le mode d'exécution des tests pour le développement sous mac et Linux :

```
NODE_ENV=development NODE_OPTIONS=--experimental-vm-modules npx jest
```

Sous powershell  :

```
$env:NODE_ENV='development' ; NODE_OPTIONS=--experimental-vm-modules npx jest
```

Vous devriez revoir les logs.

> TBD : qu'ajouter dans le `package.json`{.fichier} pour que a marche sous powershell ?
