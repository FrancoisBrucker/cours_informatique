---
layout: page
title:  "Projet numérologie : partie 5 / tests unitaires"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %}) / [partie 5]({% link cours/web/projets/numerologie/partie-5-tests/index.md %}) / [tests unitaires]({% link cours/web/projets/numerologie/partie-5-tests/1-tests-unitaires.md %})
{: .chemin}


> TBD
> jest
> mock ?

## bibliothèque de test

Il existe plusieurs bibliothèques permettant de faire des tests unitaires. Nous allons utiliser [jest](https://jestjs.io/)

Commençons par l'installer :

```shell
npm install --save-dev jest
```

Remarquez qu'on a pas utilisé le classique `--save` mais le nouveau `--save-dev`. Ceci à changer le fichier *"package.json"* :

```json
{
  "name": "numerologie",
  "version": "1.0.0",
  "description": "de la numérologie",
  "main": "index.js",
  "scripts": {
    "init": "node db-init.js",
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "node index.js"
  },
  "author": "François Brucker",
  "license": "WTFPL",
  "dependencies": {
    "express": "^4.17.1",
    "sequelize": "^6.7.0",
    "sqlite3": "^5.0.2"
  },
  "devDependencies": {
    "jest": "^27.3.1"
  }
}
```

Une valeur a été ajoutée : `"devDependencies"` pour distinguer les dépendances utiles en production (`"dependencies"`) et celles utiles en développement. En tapant :

* `npm install` : toutes les dépendances (`"dependencies"` et `"devDependencies"`) seront installées
* `npm install --production` : uniquement les dépendances `"dependencies"`  seront installées

Voir [la documentation](https://docs.npmjs.com/cli/v7/commands/npm-install) pour de plus amples informations.

## usage

