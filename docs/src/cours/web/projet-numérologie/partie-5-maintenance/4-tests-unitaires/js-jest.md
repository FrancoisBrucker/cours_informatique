---
layout: layout/post.njk

title: "Projet numérologie : partie 5 / tests unitaires : js"

eleventyNavigation:
  key: "Projet numérologie : partie 5 / tests unitaires : js"
  parent: "Projet numérologie : partie 5 / tests unitaires"
---

<!-- début résumé -->

Nous allons ajouter des tests unitaires à notre projet.

<!-- fin résumé -->

Il existe de nombreuses bibliothèques de tests en javascript. Nous allons nous focaliser sur [jest](https://jestjs.io/fr/) efficace et populaire.

## Installation

On installe la bibliothèque pour le développement (on en aura pas besoin en production) :

```
npm install --save-dev jest
```

Puis on va l'utiliser pour lancer nos tests avec la commande `npm run test`. Pour cela, modifions l'entrée test du `package.json`{.fichier}  pour :

```json
...

"scripts": {

    ...

    "test": "jest",

    ...
}

...
```
