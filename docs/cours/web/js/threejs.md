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

Maintenant que toutes les librairies nécessaires ont été implémentées, on va pouvoir s'intéresser à la structure du code pour un projet three.js.
Dans un premier temps, comme on a vu juste au desssus et comme dans tout projet js, on importe les différents éléments dont on aura besoin pour développer notre projet.
Ensuite on initialise les variables importantes du projet ( en particulier la scène, la caméra et le renderer que l'on va voir juste après). Ces variables sont utilisées dans l'entiereté du projet et il est donc utile de les définir dès le début.
```javascript
let scene, renderer, camera;
```
On utilise ensuite une fonction d'initialisation pour donner des propriétés à ces variables et établir toutes les actions que l'on veut faire faire à notre environnement 3D.
```javascript
init();

function init() {
    camera = ...;
    scene = ...;
    renderer = ...;
    const light = ...;
    const mesh = ...;
}
``` 
On remarque que l'appel à la fonction init() a lieu avant la déclaration de celle-ci. Ce n'est pas une particularité de three.js mais directement de js. Le fait d'utiliser la déclaration *function* permet de définir la fonction avant qu'elle ne soit utilisée ailleurs, même si cet ailleurs est avant dans le code. 

### Scene, Camera et Renderer

Donc on a vu que three.js utilise des outils afin de faciliter le travail de l'utilisateur. Les outils les plus importants sont les scènes, les caméras et les renderer (moteurs de rendu). Ces trois éléments sont essentiels à tout projet three.js, sans eux impossible d'afficher quoi que ce soit. Concrètement on va utiliser la caméra pour faire un rendu de la scène.

- La scène correspond donc à notre environnement de travail, ce qui va etre rendu visible par le renderer. Elle permet de localiser avec des coordonnées 3D les différents objets que l'on va ensuite créer. L'object scene ayant déjà été créé avant le fonction init(), on peut se contenter ici de le modifier sans l'initialiser.
```javascript
scene = new THREE.Scene();
```

- Les caméras sont aussi un point essentiel de three.js car elles définissent comment la scène va etre vu par l'utilisateur final. Il existe plusieurs types de caméras avec des possibilités et des effets différents. Une des caméra les plus utilisé est la PerspectiveCamera qui mimique la vision humaine. 
```javascript
camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );
camera.position.set(0, 0, 5);
camera.lookAt( 0, 0, 0 );
```
Ici on définit une caméra avec différentes propriétés : le **FOV** (Field of view), l'**aspect** qu'on définit ici comme le rapport entre la largeur et la hauteur de l'écran, et enfin on définit les valeurs pour **near** et **far**. Ces deux valeurs déterminent à quelle distance se trouve les plans limites de la caméra. Tout ce qui se trouve avant le plan near et après le plan far ne seront pas vu par la caméra et ils ne seront donc pas rendu par le renderer.

On peut aussi définir une position ainsi que la direction dans laquelle la caméra regarde de manière relative à la scène que l'on a créée avant. 

![une camera]({{ "/assets/cours/web/threejs/camera.jpg" | relative_url }}){:style="margin: auto;display: block;"}

- Enfin le moteur de rendu ou renderer. Il s'agit du travail final qui va venir faire un rendu 3D de la scène vu au travers de la caméra. L'objet final sera une image 2D de la scène 3D que l'on peut intégrer dans un canvas pour etre utiliser directement en html. Comme dit précedement, classiquement on utilise le moteur de rendu WebGLRenderer mais il est possible d'en utiliser d'autres (notamment au cas ou des utilisateurs sont sur des vieux navigateurs qui ne supportent pas WebGL ce qui est rare).
De la même manière que pour la caméra, il est possible de définir l'**aspect** du rendu, par exemple relatif à la taille de l'écran sur lequel on va ensuite afficher l'image. La dernière ligne ajoute le renderer dans le body du fichier HTML pour qu'il puisse afficher quelque chose.
```javascript
renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild(renderer.domElement);
```

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

Ensuite on crée notre matériau avec `MeshStandardMaterial`. On spécifie sa couleur 
en hexadécimal (par exemple ici c'est du rouge). 
```javascript
const plane_material = new THREE.MeshStandardMaterial( color:0xff0000 );
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
la liste de toutes les formes possibles.

Il existe aussi de nombreux matériaux avec des propriétés différentes. Par 
exemple `MeshBasicMaterial()` ne gère pas les effets de lumière et d'ombres, 
alors que d'autres matériaux comme `MeshStandardMaterial()` ou `MeshPhongMaterial()` qui les supporte. 
[A voir ici](https://threejs.org/docs/index.html?q=material#api/en/materials/MeshBasicMaterial) 
tous les matériaux disponibles.


## Go rendre ça plus joli

### Lumière
On peut améliorer notre rendu notament en ajoutant des lumières. Pour ajouter une lumière, c'est très simple, il suffit d'ajouter
<br>

```javascript
const light = new THREE.DirectionalLight(0xffffff, 1);
```

Le premier argument est le code couleur en hexadécimal de la lumière et le deuxième est son intensité.
<br>
Il suffit ensuite de choisir sa position et de l'ajouter à la scène :

```javascript
light.position.set(0,2,2);
scene.add(light);
```
On a alors un plan qui est éclairé par le dessus.
### Ombres
Un autre aspect pour augmenter la beauté de notre projet sont les ombres ! On peut en effet rajouter des ombres dans Three.js. Pour se faire, rien de plus simple :

On ajoute en premier un cube pour pouvoir voir les ombres :

```javascript
const cube_geometry = new THREE.BoxGeometry(1,1)
const cube_material = new THREE.MeshStandardMaterial(0xffffff);
const cube = new THREE.Mesh( cube_geometry, cube_material);
cube.position.set(0,0,1);

```
Il faut maintenant lui autoriser à diffuser des ombres :
```javascript
cube.castShadow= true;
scene.add(cube);
```

De même pour la lumière, il faut aussi lui autoriser (on ajuste sa position pour avoir un bon rendu au passage):

```javascript
light.position.set(-2,-2,5);
light.castShadow = true;
```

Jusque la vous ne devez rien voir. Il faut aussi activer la résolution pour les ombres : 

```javascript
renderer.shadowMap.enabled= true
```
On a la lumière qui envoie des ombres, le cube qui envoie des ombres, mais qui doit les recevoir ? C'est le plan, ! Donc faisons en sorte qu'il le recoive :

```javascript
plane.receiveShadow= true
```

On remarque cependant que l'ombre est pixelisée : c'est parce que d'origine la `shadowMap` est de taille `512x512`, on peut l'augmenter par la commande :
```javascript
light.shadowMapWidth = 512*8;
light.shadowMapHeight = 1024*8;
```
On va aussi rajouter un léger effet de flou sur les bords de l'ombre:
```javascript
light.shadow.radius = 4;
```

Enfin, on aimerait ajouter une lumière ambiante partout dans notre scène, pour y voir un peu plus clair. 
On rajoute donc :

```javascript
const ambientLight = new THREE.AmbientLight( 0xcccccc, 0.3 );
scene.add( ambientLight );
```

### Textures
On a vu que pour tous les objets, nous avons besoin d'un `MeshMaterial` et d'une `Geometry`. Au début du projet, nous 
avons utilisé `MeshStandardMaterial`. C'est ici que nous devons mettre notre texture. 

Elle sera divisée en plusieurs sous couches qui permettront un rendu plus que quali !

Pour ce projet, on choisit cette [texture](https://drive.google.com/drive/folders/1r2R96PnfH85xlv11MWRV8zSIT73Id3C9) qui plus est gratuite. On les mets dans un dossier `img` dans le projet. 

On doit alors charger toutes les images dans notre projet :

```javascript
const textureloader = new THREE.TextureLoader()
const textureBasecolor = textureloader.load('img/Concrete_Blocks_011_basecolor.jpg')
const textureAmbientOcclussion = textureloader.load('img/Concrete_Blocks_011_ambientOcclusion.jpg')
const textureheight = textureloader.load('img/Concrete_Blocks_011_height.jpg')
const texturenormal = textureloader.load('img/Concrete_Blocks_011_normal.jpg')
const textureroughness = textureloader.load('img/Concrete_Blocks_011_roughness.jpg')
```
Maintenant on peut ajouter les couches à notre cube :
```javascript
const cube_material = new THREE.MeshStandardMaterial(    
    {
    map : textureBasecolor,
    normalMap: texturenormal,
    bumpMap: textureheight,
    roughnessMap: textureroughness,
    roughness:0.05
}
);
```
Le problème est que la texture a besoin d'être rendu en boucle, donc on ne la voit pas si l'on ne rend pas en boucle, il faut alors rajouter la fonction suivante à la fin

```javascript
function rend(){
    renderer.render(scene,camera);
    requestAnimationFrame(rend)
}
rend()
```
## Déplacement de la caméra

Il est desfois plus agréable de pouvoir déplacer la caméra comme on le souhaite pour pouvoir bien visualiser ce que l'on est en train de modéliser. En conception 3D, il est important de pouvoir observer son travail sous plusieurs angles afin de s'assurer que tout correspond bien à ce que l'on souhaite. En effet on peut faire le cube le plus joli qu'on souhaite, si la caméra est toujours pointée dans la même direction , on ne verra jamais l'arrière de ce cube et il ne correspond peut etre pas du tout à ce que l'on veut.

On a vu qu'il est possible de changer l'emplacement et vers où la caméra regarde dans le code ce n'est pas forcement le plus intéressant pour pouvoir déplacer la caméra "à la volée" autours d'un objet pour en vérifier les propriétés pendant les phases de développment.

On va donc essayer de mettre en place une méthode de déplacement de la caméra qui soit controlée par l'utilisateur au niveau de l'affichage dans le navigateur web. Et traditionnellement, pour permettre à un utilisateur d'interagir avec un programme, qu'est ce qu'on utilise ? Un clavier et/ou une souris !

### Déplacement avec ZQSD

### Rotation avec la Souris

Une des méthodes les plus simples de déplacement de caméra consiste à autoriser une rotation de la caméraà l'aide de la souris. Ce type de controle s'appelle OrbitControl dans three.js. C'est un controle très simple à mettre en place et à utiliser. Juste en maintenant le clic gauche de la souris et en bougeant la souris, on change l'axe de visualisation de la caméra. Combiné à un déplacement grâce au touches ZQSD, on peut obtenir un controle sur la caméra similaire à un jeu fps.

```javascript
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';

const controls = new OrbitControls( camera, renderer.domElement );
controls.target.set( 0, 1, 0 );
controls.update();
```

## Génération du monde

### Plus de cubes

Maintenant qu'on peut sauter partout, rajoutons de quoi faire du ***parkour*** !

Par exemple plein de cubes. Pour ça, on va d'abord créer une liste d'objets en 
dehors de notre fonction init():

```javascript
const objects = [];
```

Ensuite on va créer dans notre fonction init() plein de cubes, qu'on va placer 
aléatoirement dans une zone donnée :

```javascript
for ( let i = 0; i < 20; i ++ ) {

        const cube = new THREE.Mesh( cube_geometry, cube_material );
        cube.position.x = Math.floor( Math.random() * 10 - 5 ) * 5;
        cube.position.y = Math.floor( Math.random() * 4 ) * 5 + 2.5;
        cube.position.z = Math.floor( Math.random() * 10 - 5 ) * 5;
        cube.castShadow = true;
        cube.receiveShadow = true;

        scene.add( cube );
        objects.push( cube );

    }
```
## CONCLUSION

Et voila enfin à la fin de ce tuto ! Maintenant nous avons un environnement capable de faire tourner notre code js en utilisant la librairie three.js pour générer un monde en 3D et y déplacer une caméra à l'intérieur à l'aide du clavier et de la souris ! Voici le lien vers notre répo github pour trouver notre code :
https://github.com/LeoLaurent/three-js-project