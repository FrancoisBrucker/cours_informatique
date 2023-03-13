---
layout: layout/post.njk

title: "Projet numérologie : partie 4 / routes"

eleventyNavigation:
  key: "Projet numérologie : partie 4 / routes"
  parent: "Projet numérologie / partie 4 jardinage"
---

<!-- début résumé -->

Rationalisation des différentes routes du serveur.

<!-- fin résumé -->

Si l'on continue comme ça, notre fichier `numérologie/index.js`{.fichier} va devenir énorme et contenir toutes les routes de notre projet. Il faut rationaliser tout ça en organisant les routes par *thème*.

## Routeur

Pour cela, commençons par créer un fichier `numérologie/routes/index.js`{.fichier} où on va déporter toutes nos routes non statiques :

```js
import express from 'express';

import numérologie from '../back/numérologie.js';
import db from "../db.js"

let router = express.Router();

router.get(encodeURI('/prénom'), (req, res) => {
    console.log(req.query)
    let prénom = req.query["valeur"]
    let chiffre = numérologie.chiffre(prénom)
    db.model.Prénoms.findOne({
        where: {
            prénom: prénom
        }
    }).then((data) => {
        if (data === null) {
            db.model.Prénoms.create({
                prénom: prénom
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
            prénom: prénom,
            chiffre: chiffre,
            message: data.message
        })
    })
})

router.get(encodeURI('/api/prénoms/read'), (req, res) => {
    db.model.Prénoms.findAll()
        .then((data) => {
            var liste = []
            for (let element of data) {
                liste.push({
                    prénom: element.prénom,
                    chiffre: numérologie.chiffre(element.prénom)
                })
            }
            res.json(liste)
        })
})


export {
    router
}
```

{% note %}
Remarquez que nous avons utilisé ici une nouvelle façon d'exporter des noms : on le fait directement.
{% endnote %}

Ce fichier contient toutes les routes non statique et non `/` de notre serveur. Elles sont rangées dans un [router](http://expressjs.com/fr/guide/routing.html#express-router).


{% attention %}
Les imports de nos fichiers sont dans le dossier parent, il faut donc mettre `../` devant pour les retrouver
{% endattention %}

On utilise ce fichier dans `numérologie/index.js`{.fichier} :

```js
import { fileURLToPath } from 'url';
import path from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);


import express from 'express';
const app = express()

import {router as routes} from "./routes/index.js";

const hostname = '127.0.0.1';
const port = 3000;

app.use(function (req, res, next) {
    const date = new Date(Date.now())
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

On importe le router avec la ligne `import {router as routes} from "./routes/index.js";`{.language-}. Ceci a de plus permi de renommer notre `router`{.language-} `routes`{.language-} ici.

Notre serveur est bien plus petit !

## API

Finissons cette partie en ajoutant une indirection à nos routes. On va créer un nouveau dossier `numérologie/routes/api/`{.fichier} qui va contenir toutes les routes de l'api CRUD (pour l'instant embryonnaire puisqu'il n'y a qu'une route).

Comme avant, on crée aussi un fichier `numérologie/routes/api/index.js`{.fichier} qui va contenir nos routes :

```js
import express from 'express';

import numérologie from '../../back/numérologie.js'
import db from "../../db.js"

let router = express.Router();

router.get(encodeURI('/prénoms/read'), (req, res) => {
    db.model.Prénoms.findAll()
        .then((data) => {
            var liste = []
            for (let element of data) {
                liste.push({
                    prénom: element.prénom,
                    chiffre: numérologie.chiffre(element.prénom)
                })
            }
            res.json(liste)
        })
})


export {router};

export {
    router
}
```

On va utiliser ce fichier dans notre notre gestionnaire de route — le fichier `numérologie/routes/index.js`{.fichier} — que l'on modifie en:

```js
import express from 'express';

import numérologie from '../back/numérologie.js'
import db from "../db.js"

import {router as apiRoutes} from './api/index.js'

let router = express.Router();

router.get(encodeURI('/prénom'), (req, res) => {
    console.log(req.query)
    let prénom = req.query["valeur"]
    let chiffre = numérologie.chiffre(prénom)
    db.model.Prénoms.findOne({
        where: {
            prénom: prénom
        }
    }).then((data) => {
        if (data === null) {
            db.model.Prénoms.create({
                prénom: prénom
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
            prénom: prénom,
            chiffre: chiffre,
            message: data.message
        })
    })
})

router.use('/api', apiRoutes)


export {
    router
}
```

Toutes les routes de `apiRoutes` commencerons par `/api`. Un tel procédé rend très simple la concaténation de routes (ce n'est pas la peine d'éditer plein de fichier lors d'un changement d'architecture des routes) et permet de bien séparer les groupes de routes en dossier séparés.

## Routes

Les routes non statiques que possèdent maintenant notre serveur sont :

* <http://127.0.0.1:3000/prénom> (GET) définie dans `route/index.js`{.fichier}
* <http://127.0.0.1:3000/api/prénoms/read> (GET) définie dans `route/api/index.js`{.fichier}
