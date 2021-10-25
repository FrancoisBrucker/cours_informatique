---
layout: page
title:  "Création d'environnements 3D avec three.js"
category: cours
authors:
- "Rose Simon"
- "Laurent Léo"
- "Pépin Anthony"
---


## Introduction

### three.js c'est quoi?

### à quoi sert ce tuto?

## Installation

### Prérequis

On va utiliser three.js et vite.js, que l'on intallera avec node packet manager.
Il faut donc avoir installé [node.js](https://nodejs.org/en/download/) 
au préalable.

Pour plus de confort, on vous conseille également d'utiliser un IDE pour 
coder, par exemple [VSCode](https://code.visualstudio.com/download).

### three.js et vite.js

On crée un dossier `three-js-project/` qui sera la racine de notre projet.

On installe dedans three.js avec la commande `npm install --save three`.

Pour utiliser three.js, on va créer une app web qu'on va faire tourner 
avec [vite.js](https://vitejs.dev/).

vite.js permet d'actualiser en direct notre projet web lorsqu'on modifie notre 
code, le rendant très utile pendant la phase de développement, surtout pour faire 
du three.js.

Dans le dossier `three-js-project/`, on entre la commande `npm init vite@latest` 
pour installer vite.js.

Il nous demande ensuite d'entrer le nom de notre app (on va l'appeler `app-vite`) 
puis quel type de projet on veut créer: on choisit ici vanilla pour partir 
de rien.

On suit ensuite ses instructions: On va dans le dossier `app-vite` qu'il vient 
de générer et on installe les packages nécessaires avec `npm install`.

On peut ensuite faire un `npm run dev` pour lancer notre application en local. 
En allant sur http://localhost:3000/ on peut voir notre appli !

Allons voir dans `app-vite/` la structure de notre code: La page qui s'affiche est 
notre `index.html`, dans lequel on trouve un appel à notre fichier `main.js`: 
```html
<body>
    <div id="app"></div>
    <script type="module" src="/main.js"></script>
  </body>
```
Dans notre main.js on a ce qui s'affiche pour l'instant sur la page `index.html`: 
```javascript
document.querySelector('#app').innerHTML = `
  <h1>Hello Vite!</h1>
  <a href="https://vitejs.dev/guide/features.html" target="_blank">Documentation</a>
`
```

C'est ici qu'on va coder l'intégralité de notre code pendant ce tutoriel. 
Pour le moment enlevons ces lignes et remplaçons ça par l'import de three.js :
```javascript
import * as THREE from 'three';
```

C'est tout bon, on peut passer au vif du sujet !


## Les bases

### Structure du projet

### Scene, Camera et Renderer

### Créer un plan: Geometry et Material

## Go rendre ça plus joli

### Lumière ambiante

### Ombres

### Textures

## Déplacement de la caméra

### Déplacement avec ZQSD

### Rotation avec la Souris

## Génération du monde
