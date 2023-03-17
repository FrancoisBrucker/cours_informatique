---
layout: layout/post.njk 
title:  "Projet commentaires : partie 1 / architecture"
category: cours
author: "François Brucker"
---

> [commentaires]({% link cours/web/projets/commentaires/index.md %}) / [partie 1]({% link cours/web/projets/commentaires/partie-1-site/index.md %}) / [architecture]({% link cours/web/projets/commentaires/partie-1-site/1-architecture.md %})
{.chemin}

## plan du site

Commençons par créer un dossier qui contiendra notre serveur et nommons le *"commentaires"*.

Nous allons avoir une partie front et une partie back. Nous laisserons la partie back à la racine de notre projet et placerons nos fichiers front dans un dossier nommé *"static"*.

Nous ajouterons petit à petit des dossiers pour garder le tout cohérent. Vous pouvez voir [ici](https://blog.logrocket.com/the-perfect-architecture-flow-for-your-next-node-js-project/) ce que peut donner un projet complet (nous n'aurons ici pas besoin de tous les dossiers).

### partie front

Dans *"commentaires/static"* on va juste placer un fichier *"index.html"* minimal :

```html
<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Numérologie</title>
    </head>
    <body>
        <form>
            <label>Prénom :</label>
            <input type="text"/>

            <button type="submit">Envoi</button>
        </form>
        <p>7</p>
    </body>
</html>
```

Nous allons gérer toutes nos dépendances front en utilisant `npm`. On commence donc tout de suite par initialiser le projet par la commande `npm init` dans ce dossier. Le *"package.json"* final est :

```json
{
  "name": "static",
  "version": "1.0.0",
  "description": "partie statique du site",
  "main": "index.html",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}
```

> Nous aurons 2 projets `npm` : l'un pour gérer les dépendances front (celui que nous venons de créer) et l'un pour gérer les dépendances back. Attention à ne pas se mélanger les pinceaux.

### partie back

Initialisons notre projet avec la commande `npm init` dans le dossier *"commentaires"*. Le *"package.json"* final est :

```json
{
  "name": "commentaires",
  "version": "1.0.0",
  "description": "donnez votre avis",
  "main": "server.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}
```

On ajoute le module express : `npm add --save express` et on crée notre serveur dans le fichier *"server.js"*. Il est pour l'instant juste là pour gérer les fichiers statiques :

```js
const path = require('path')

const express = require('express')
const app = express()

const hostname = '127.0.0.1';
const port = 3000;

app.use("/static", express.static(path.join(__dirname, '/static')))

app.get('/', (req, res) => {
    res.redirect(301, '/static/index.html')
})


app.use(function (req, res) {
    console.log("et c'est le 404 : " + req.url);

    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/html');

    res.end("<html><head><title>404</title></head><body><h1>Et c'est le 404.</h1><p> ressource non trouvée</p></body></html>");

})

app.listen(port, hostname);
console.log(`Server running at http://${hostname}:${port}/`);
```

### on teste

La commande classique `node server.js` lance le serveur.

On va tout de suite ajouter un script de lancement de notre site dans le fichier *"package.json"*, pour utiliser la commande `npm start`, qui est la commande de démarrage du serveur par convention.

La partie `"scripts"` de *"package.json"* devient alors :

```json
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "node server.js"
  },
```

> En json, il faut être très pointilleux sur l'écriture des objets : chaque attribut est séparé par une `,`, **sauf** le dernier. Si vous vous trompez le programme ne se lancera pas.
{.attention}

A partir de maintenant, on exécutera notre serveur avec la commande : `npm start` qui doit rendre, pour l'instant, quelque chose comme ça :

```text

> commentaires@1.0.0 start
> node server.js

Server running at http://127.0.0.1:3000/

```

## structure

On a donc pour l'instant l'instant l'architecture suivante :

```text
.
├── ./node_modules
├── ./package-lock.json
├── ./package.json
├── ./server.js
└── ./static
    ├── ./static/index.html
    └── ./static/package.json
```

> On a utilisé la commande unix [tree](https://linux.die.net/man/1/tree) (`tree -f | grep -v "node_modules/.*"`) pour réaliser le dessin ci-dessus.
