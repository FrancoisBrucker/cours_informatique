---
layout: layout/post.njk
title: "Projet numérologie : partie 2 / mise en place front"

authors:
    - "François Brucker"


eleventyNavigation:
  key: "Projet numérologie : partie 2 / mise en place front"
  parent: "Projet numérologie / partie 2 serveur"
---

<!-- début résumé -->

Mise en place du serveur express pour le site.

<!-- fin résumé -->

## Préparation

Pour l'instant, notre projet ressemble à ça :

```
.
├── index.html
├── main.css
├── mes_tests.js
└── numerologie.js
```

Qui correspond peu ou prou à la partie front de notre serveur. Rendons ceci explicite en déplaçant nos fichier dans un dossier `static`{.fichier}.

### Fichiers static

{% faire %}

* supprimer le fichier `mes_tests.js`{.fichier} qui ne nous sers plus
* déplacer les fichiers `index.html`{.fichier}, `main.css`{.fichier} et `numerologie.js`{.fichier} dans un dossier `static`{.fichier}
* créer un fichier vide `index.js`{.fichier} à la racine du projet pour simuler notre serveur.
{% endfaire %}

On obtient la structure classique d'un serveur web en node :

```text
.
├── index.js
└── static
    ├── index.html
    ├── main.css
    └── numerologie.js
```

{% faire %}

On vérifie que le front n'est pas cassé en ouvrant le fichier `index.html`{.fichier} avec notre navigateur.

{% endfaire %}

### packages Express

Il nous reste à préparer la partie serveur en mettant en place node et express.

{% faire %}

Dans le dossier `numerologie`{.fichier} :

1. initialisation du projet en tapant la commande : `npm init`
2. ajout du package express et sauvegarde dans le fichier de configuration `package.json`{.fichier} : `npm add --save express`
{% endfaire %}

## Routes

On reprend le code de la partie [server express](../../serveur-web/express) pour notre site, uniquement en front pour l'instant :

```javascript
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

    res.end("");

})

app.listen(port, hostname);
console.log(`Server running at http://${hostname}:${port}/`);

```

## mise en place des fichiers

Le projet ressemble maintenant à ça :

```text
.
├── index.js
├── node_modules
|   └── ...
├── package-lock.json
├── package.json
└── static
    ├── index.html
    ├── main.css
    └── numerologie.js
```
