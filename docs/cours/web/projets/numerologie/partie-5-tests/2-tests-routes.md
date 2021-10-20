---
layout: page
title:  "Projet numérologie : partie 5 / tests de routes"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %}) / [partie 5]({% link cours/web/projets/numerologie/partie-5-tests/index.md %}) / [tests fonctionnels]({% link cours/web/projets/numerologie/partie-5-tests/2-tests-routes.md %})
{: .chemin}

Le tests des routes du serveur nous permet de garantir que l'api fonctionne bien. C'est différent des tests unitaires car il faut que le serveur tourne pour les faire.

## mise en place

On va utiliser la bibliothèque [supertest](https://github.com/visionmedia/supertest#readme) pour gérer le serveur. Supertest va créer une instance de notre serveur pour chaque test, cela nous permettra de faire plein de test en même temps (il va lancer chaque serveur sur un autre port).

Commençons pas l'installer :

```shell
npm install supertest --save-dev
```

Pour pouvoir l'utiliser, il faut séparer l'application (express) du serveur proprement dit. On va donc créer un fichier *"numerologie/app.js"* qui contiendra toute notre application :

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

et ne laisser que le lancement du serveur à *"numerologie/index.js"* :

```js
const app = require("./app")

const hostname = '127.0.0.1';
const port = 3000;

app.listen(port, hostname);
console.log(`Server running at http://${hostname}:${port}/`);
```

C'est *"numerologie/app.js"* que nous importerons pour nos tests.

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


### environnement/base de test

> TBD
> before et after pour la base
> env de test pour la base

