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

Three.js est une librairie 3D qui permet de créer du contenu 3D sur un navigateur très facilement. L'interet de la librairie est que la plupart des navigateurs internet supportent three.js et qu'il est donc possible de diffuser son code sans avoir à recourir à des plugins pour le faire fonctionner.
Three.js utilise presque systématiquement WebGL comme moteur de rendu (renderer en anglais) qui est un système de bas niveau qui ne permet de ne dessiner que des points, des lignes et des triangles. L'utilisatoion direct de WebGL pour générer du contenu 3D est long et demande une grande quantité de code car il va tout falloir créer "à la main", et c'est là qu'intervient three.js: la librairie sert d'intermédiaire entre l'utilisateur et WebGL afin de traduire facilement le travail de l'utilisateur pour WebGL. Three.js utilise notamment des scènes, lumière, materiaux, caméras, textures, filet (mesh), etc, commme outils pour accélerer le travail.

### à quoi sert ce tuto?

Le but de ce tuto est d'apprendre les bases de three.js afin de mener à bien un projet simple. Le projet que nous avons choisi pour travailler sur la librairie est de créer un petit environnement 3D dans lequel on pourra déplacer une caméra à l'aide de la souris et du clavier.

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

Pour l'instant notre scène est complètement vide. On va donc rajouter des objets !
Commençons par ajouter un plan.

Un objet est défini par deux attributs: Sa géométrie et son matériau.

La géométrie du plan est créée avec *PlaneGeometry* qui prend en paramètres 
les longueur et largeur du plan 
(l'unité de mesure est abstraite, elle est propre à three.js).
```javascript
const plane_geometry = new THREE.PlaneGeometry( 20, 20 );
```

Ensuite on crée notre matériau avec `MeshBasicMaterial`. On spécifie sa couleur 
en hexadécimal (par exemple ici c'est du rouge). 
```javascript
const plane_material = new THREE.MeshBasicMaterial( color:0xff0000 );
```

Puis on crée notre objet avec `Mesh` qui prend en paramètres la géométrie et le 
matériau.
```javascript
const plane = new THREE.Mesh( plane_geometry, plane_material );
```

Et enfin, on l'ajoute à la scène:
```javascript
scene.add( plane );
```

On peut créer n'importe quel type d'objet de cette manière. 
Une géométrie peut être créée point par point avec `ShapeGeometry()`, ou 
générée avec des fonctions prévues pour, comme `PlaneGeometry()`, 
`BoxGeometry()`... [A voir ici](https://threejs.org/docs/index.html?q=geometry#api/en/geometries/BoxGeometry) 
la liste de tous les possibles.

Il existe aussi de nombreux matériaux avec des propriétés différentes. Par 
exemple `BasicMeshMaterial()` ne gère pas les effets de lumière et d'ombres, 
donc par la suite on va utiliser `PhongMeshMaterial()` qui les supporte. 
[A voir ici](https://threejs.org/docs/index.html?q=material#api/en/materials/MeshBasicMaterial) 
tous les matériaux disponibles.


## Go rendre ça plus joli

### Lumière ambiante

### Ombres

### Textures

## Déplacement de la caméra

### Déplacement avec ZQSD

### Rotation avec la Souris

## Génération du monde
