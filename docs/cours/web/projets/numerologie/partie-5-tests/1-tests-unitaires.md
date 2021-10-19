---
layout: page
title:  "Projet numérologie : partie 5 / tests unitaires"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %}) / [partie 5]({% link cours/web/projets/numerologie/partie-5-tests/index.md %}) / [tests unitaires]({% link cours/web/projets/numerologie/partie-5-tests/1-tests-unitaires.md %})
{: .chemin}


> TBD
> mock ?
> asynchrone
> before/after

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

`jest` va exécuter des tests écrit dans des fichiers. Par défaut ces fichiers sont :

* les fichiers finissant par *".test.js"* (ou *".spec.js"*) du projet ou dans ses sous dossiers
* tous les fichiers du dossier *"__tests__"* s'il existe.

### commande

On peut exécuter jest de deux façon, soit via `npm` et une configuration dans *"package.json"* ou en ligne de commande.

#### npm

On commence par associer `jest` aux tests en renseignant le champ `"test"` de l'attribut `"script"` du fichier *"package.json"* :

```json
...

  "scripts": {
    "init": "node db-init.js",
    "test": "jest",
    "start": "node index.js"
  },

...
```

Puis on exécute `jest` en tapant la commande :

```shell
npm test
```

> `npm test` est un raccourci pour `npm run test`

#### CLI

Le programme `jest` est rangé dans le dossier *"node_modules/.bin"*, on peut donc l'appeler directement par la commande :

```shell
./node_modules/.bin/jest
```

### tests

les tests seront tous de la forme (repris des [premiers pas](https://jestjs.io/fr/docs/getting-started)) :

```js
test('deux plus deux font quatre', () => {
  expect(2 + 2).toBe(4);
});
```

Chaque test aura :

* un nom. Ici : `'deux plus deux font quatre'`
* le test en lui même qui est une fonction et dont le but est de comparer une valeur théorique à une valeur réelle. Ici on cherche à vérifier que `2 + 2` vaut `4`.

L'essence même d'un test est l'utilisation de [comparateurs](https://jestjs.io/fr/docs/using-matchers)

### blocs de tests

Par défaut, on va grouper les tests similaire dans un même fichier. Si l'on a besoin de sous-groupes à l'intérieur d'un fichier, par exemple en faisant un groupe pour les tests d'une fonction, on peut utiliser un bloc [describe](https://jestjs.io/fr/docs/api#describename-fn).

## tests métiers

On va tester ici les méthodes *métiers* c'esrt à dire tout ce qui n'est pas des routes. Notre projet à un unique fichier métier : *"numerologie/back/numerologie.js"*

On doit tester toutes les méthodes de ce fichier : `nombre`, `somme` et `chiffreAssocie`.

Il n'y a jamais de bonne réponses à la question : quoi tester ? La seule réponse satisfaisante est: juste assez pour que l'on soit intimement persuadé que la fonction marche si les testent passent.

De toute façon, si l'on se rend compte (ou plutôt quand on se rendra compte) qu'il y a un bug, on écrira un test qui mettra en évidence le bug, puis on le corrigera. De cette façon ce bug ne pourra plus jamais réapparaitre, les tests étant conservés.

> Lorsqu'un programme et muni de tests, il ne peut jamais régresser : Kent Beck dit que c'est une progression par [cliquet](https://fr.wikipedia.org/wiki/Cliquet_(m%C3%A9canique))

Chaque test doit tester une seule chose, et on peut s'appuyer sur une fonction que si les tests des fonctions qui la composent sont testées. On doit donc tester `nombre` et `somme` avant de tester `chiffreAssocie`.

### module rewire

Il reste un dernier problème à résoudre avant de commencer les tests proprement dit : `nombre` et `somme` ne sont pas exportées, il est donc a priori impossible de simplement les importer pour les tester. POur faire cela, on va utiliser le module [rewire]() comme expliqué dans [ce tuto](https://javascript.plainenglish.io/how-to-test-a-non-export-function-in-javascript-a1d0bc339ac) :

```shell
npm install --save-dev rewire
```

### numerologie.test.js

