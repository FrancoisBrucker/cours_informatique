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

Donc on a vu que three.js utilise des outils afin de faciliter le travail de l'utilisateur. Les outils les plus importants sont les scènes, les caméras et les renderer (moteurs de rendu). Ces trois éléments sont essentiels à tout projet three.js, sans eux impossible d'afficher quoi que ce soit. Concrètement on va utiliser la caméra pour faire un rendu de la scène.

- La scène correspond donc à notre environnement de travail, ce qui va etre rendu visible par le renderer. Elle permet de localiser avec des coordonnées 3D les différents objets que l'on va ensuite créer.
```javascript
const scene = new THREE.Scene();
```

- Les caméras sont aussi un point essentiel de three.js car elles définissent comment la scène va etre vu par l'utilisateur final. Il existe plusieurs types de caméras avec des possibilités et des effets différents. Une des caméra les plus utilisé est la PerspectiveCamera qui mimique la vision humaine. 
```javascript
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );
camera.position.set(0, 0, 5);
camera.lookAt( 0, 0, 0 );
```
Ici on définit une caméra avec différentes propriétés : le **FOV** (Field of view), l'**aspect** qu'on définit ici comme le rapport entre la largeur et la hauteur de l'écran, et enfin on définit les valeurs pour **near** et **far**. Ces deux valeurs déterminent à quelle distance se trouve les plans limites de la caméra. Tout ce qui se trouve avant le plan near et après le plan far ne seront pas vu par la caméra et ils ne seront donc pas rendu par le renderer.

On peut aussi définir une position ainsi que la direction dans laquelle la caméra regarde de manière relative à la scène que l'on a créée avant. 

![une camera]({{ "/assets/cours/web/threejs/camera.jpg" | relative_url }}){:style="margin: auto;display: block;"}

- Enfin le moteur de rendu ou renderer. Il s'agit du travail final qui va venir faire un rendu 3D de la scène vu au travers de la caméra. L'objet final sera une image 2D de la scène 3D que l'on peut intégrer dans un canvas pour etre utiliser directement en html. Comme dit précedement, classiquement on utilise le moteur de rendu WebGLRenderer mais il est possible d'en utiliser d'autres (notamment au cas ou des utilisateurs sont sur des vieux navigateurs qui ne supportent pas WebGL ce qui est rare).
De la même manière que pour la caméra, il est possible de définir l'**aspect** du rendu, par exemple relatif à la taille de l'écran sur lequel on va ensuite afficher l'image.
```javascript
const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
```

### Créer un plan: Geometry et Material

## Go rendre ça plus joli

### Lumière ambiante

### Ombres

### Textures

## Déplacement de la caméra

### Déplacement avec ZQSD

### Rotation avec la Souris

## Génération du monde
