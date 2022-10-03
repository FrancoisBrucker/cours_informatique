---
layout: page
title:  "Projet numérologie : partie 4 / routes"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %}) / [partie 4]({% link cours/web/projets/numerologie/partie-4-jardinage/index.md %}) / [routes]({% link cours/web/projets/numerologie/partie-4-jardinage/1-routes.md %})
{.chemin}

Si l'on continue comme ça, notre fichier *"numerologie/index.js"* va devenir énorme et contenir toutes les routes de notre projet. On a coutume de séparer les routes du server.

## routeur

Pour cela, commençons par créer un fichier *"numerologie/routes/index.js"* où on va déporter toutes nos routes non statiques :

```js
let express = require('express');

const numerologie = require('../back/numerologie');
const db = require("../db")

let router = express.Router();

router.get(encodeURI('/prénom'), (req, res) => {
    console.log(req.query)
    prenom = req.query["valeur"]
    chiffre = numerologie.chiffre(prenom)
    db.model.Prenoms.findOne({
        where: {
            prenom: prenom
        }
    }).then((data) => {
        if (data === null) {
            db.model.Prenoms.create({
                prenom: prenom
            })
        }
        console.log(data)
    })
    db.model.Signification.findOne({
        where: {
            nombre: chiffre
        }
    }).then((data) => {
        res.json({
            prénom: prenom,
            chiffre: chiffre,
            message: data.message
        })
    })
})

router.get('/api/prenoms/read', (req, res) => {
    db.model.Prenoms.findAll()
        .then((data) => {
            var liste = []
            for (element of data) {
                liste.push({
                    prenom: element.prenom,
                    chiffre: numerologie.chiffre(element.prenom)
                })
            }
            res.json(liste)
        })
})


module.exports = router
```

Ce fichier contient toutes les routes non statique et non `/` de notre serveur. Elles sont ranges dans un [router](http://expressjs.com/fr/guide/routing.html#express-router)

> Les imports de nos fichiers sont dans le dossier parent, il faut donc mettre `../` devant pour les retrouver
{.attention}

On utilise ce fichier dans *"numerologie/index.js"* :

```js
const path = require('path')

const express = require('express')
const app = express()

const routes = require("./routes")

const hostname = '127.0.0.1';
const port = 3000;

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

app.listen(port, hostname);
console.log(`Server running at http://${hostname}:${port}/`);
```

On importe le router avec la ligne `const routes = require("./routes")`. Lorsqe l'on importe un dossier en node, c'est comme si l'on importait le fichier *"index.js"* de ce dossier. La ligne précédente est donc équivalente à const routes = require("./routes/index.js")`

Notre serveur est bien plus petit !

## api

Finissons cette partie en ajoutant une indirection à nos routes. On va créer un nouveau dossier *"numerologie/routes/api/"* qui va contenir toutes les routes de l'api CRUD (pour l'instant embryonnaire puisqu'il n'y a qu'une route).

Comme avant, on crée aussi un fichier *"numerologie/routes/api/index.js"* qui va contenir nos routes :

```js
let express = require('express');

const numerologie = require('../../back/numerologie')
const db = require("../../db")

let router = express.Router();

router.get('/prenoms/read', (req, res) => {
    db.model.Prenoms.findAll()
        .then((data) => {
            var liste = []
            for (element of data) {
                liste.push({
                    prenom: element.prenom,
                    chiffre: numerologie.chiffre(element.prenom)
                })
            }
            res.json(liste)
        })
})


module.exports = router
```

On a pas mis comme début de route `api` car on va gérer ça dans le fichier *"numerologie/routes/index.js"* : 

```js
let express = require('express');

const numerologie = require('../back/numerologie')
const db = require("../db")

const apiRoutes = require('./api')

let router = express.Router();

router.get(encodeURI('/prénom'), (req, res) => {
    console.log(req.query)
    prenom = req.query["valeur"]
    chiffre = numerologie.chiffre(prenom)
    db.model.Prenoms.findOne({
        where: {
            prenom: prenom
        }
    }).then((data) => {
        if (data === null) {
            db.model.Prenoms.create({
                prenom: prenom
            })
        }
        console.log(data)
    })
    db.model.Signification.findOne({
        where: {
            nombre: chiffre
        }
    }).then((data) => {
        res.json({
            prénom: prenom,
            chiffre: chiffre,
            message: data.message
        })
    })
})

router.use('/api', apiRoutes)


module.exports = router
```

Toutes les routes de `apiRoutes` commencerons par `/api`. Un tel procédé rend très simple la concaténation de routes (ce n'est pas la peine d'éditer plein de fichier lors d'un changement d'architecture des routes) et permet de bien séparer les groupes de routes en dossier séparés.
