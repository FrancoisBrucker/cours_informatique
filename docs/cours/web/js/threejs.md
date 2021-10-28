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

### Three.js c'est quoi?

Three.js est une librairie qui permet de créer du contenu 3D sur un navigateur très facilement. L'intérêt de la librairie est que la plupart des navigateurs internet supportent three.js, et qu'il est donc possible de diffuser son code sans avoir à recourir à des plugins pour le faire fonctionner.
Three.js utilise presque systématiquement WebGL comme moteur de rendu (renderer en anglais) qui est un système de bas niveau qui ne permet de ne dessiner que des points, des lignes et des triangles. L'utilisation directe de WebGL pour générer du contenu 3D est longue et demande une grande quantité de code car il va tout falloir créer "à la main". C'est là qu'intervient three.js: la librairie sert d'intermédiaire entre l'utilisateur et WebGL afin de traduire facilement le travail de l'utilisateur pour WebGL. Three.js utilise notamment des scènes, lumière, matériaux, caméras, textures, filet (mesh), etc, commme outils pour accélérer le travail.

### À quoi sert ce tuto?
Il est possible de faire plein de choses en Threejs comme des animations, jeux, navigations de page ... En voilà un exemple :

![une planete]({{ "/assets/cours/web/threejs/planete.gif" | relative_url }}){:style="margin: auto;display: block;"}

Vous pouvez trouver une liste beaucoup plus détaillée sur le [site officiel](https://threejs.org/examples/).

Le but de ce tuto est d'apprendre les bases de three.js afin de mener à bien un projet simple. Le projet que nous avons choisi pour travailler sur la librairie est de créer un petit environnement 3D dans lequel on pourra déplacer une caméra à l'aide de la souris et du clavier.

## Installation

### Prérequis

On va utiliser three.js et vite.js, que l'on intallera avec node packet manager.
Il faut donc avoir installé [node.js](https://nodejs.org/en/download/) 
au préalable.

Pour plus de confort, on vous conseille également d'utiliser un IDE pour 
coder, par exemple [VSCode](https://code.visualstudio.com/download).

### Three.js et vite.js

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
Dans un premier temps, comme on a vu juste au dessus et comme dans tout projet en js, on importe les différents éléments dont on aura besoin pour développer notre projet.
Ensuite on initialise les variables importantes du projet ( en particulier la scène, la caméra et le renderer que l'on va voir juste après). Ces variables sont les variables globales qu'on va modifier dans nos fonctions.
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

- La scène correspond donc à notre environnement de travail, ce qui va être rendu visible par le renderer. Elle permet de localiser avec des coordonnées 3D les différents objets que l'on va ensuite créer. L'object scene ayant déjà été créé avant le fonction init(), on peut se contenter ici de le modifier sans l'initialiser.
```javascript
scene = new THREE.Scene();
```

- Les caméras sont aussi un point essentiel de three.js car elles définissent comment la scène va etre vu par l'utilisateur final. Il existe plusieurs types de caméras avec des possibilités et des effets différents. Une des caméras les plus utilisées est la PerspectiveCamera qui mimique la vision humaine. 
```javascript
camera = new THREE.PerspectiveCamera( 110, window.innerWidth / window.innerHeight, 0.1, 1000 );
camera.position.set(0, 10, 0);
camera.lookAt( 0, 0, 0 );
```
Ici on définit une caméra avec différentes propriétés : le **FOV** (Field of view), l'**aspect** qu'on définit ici comme le rapport entre la largeur et la hauteur de l'écran, et enfin les valeurs pour **near** et **far**. Ces deux valeurs déterminent à quelle distance se trouvent les plans limite de la caméra. Tout ce qui se trouve avant le plan near et après le plan far ne sera pas vu par la caméra et ne sera donc pas rendu par le renderer.

On peut aussi définir la position ainsi que la direction dans laquelle la caméra regarde de manière relative à la scène que l'on a créée avant. 

![une camera]({{ "/assets/cours/web/threejs/camera.jpg" | relative_url }}){:style="margin: auto;display: block;"}

- Enfin le moteur de rendu ou renderer. Il s'agit du travail final qui va venir faire un rendu 3D de la scène vu au travers de la caméra. L'objet final sera une image 2D de la scène 3D que l'on peut intégrer dans un canvas pour être utilisé directement en html. Comme dit précédemment, classiquement on utilise le moteur de rendu WebGLRenderer mais il est possible d'en utiliser d'autres (notamment au cas où des utilisateurs sont sur des vieux navigateurs qui ne supportent pas WebGL ce qui est rare).
De la même manière que pour la caméra, il est possible de définir l'**aspect** du rendu, par exemple relatif à la taille de l'écran sur lequel on va ensuite afficher l'image. La dernière ligne ajoute le renderer dans le body du fichier HTML pour qu'il puisse afficher quelque chose.
```javascript
renderer = new THREE.WebGLRenderer({antialias: true});
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild(renderer.domElement);
```

### Créer un plan: Geometry et Material

Pour l'instant notre scène est complètement vide. On va donc rajouter des objets !
Commençons par ajouter un plan.

Un objet est défini par deux attributs: Sa géométrie et son matériau.

La géométrie du plan est créée avec `PlaneGeometry` qui prend en paramètres 
les longueur et largeur du plan 
(l'unité de mesure est abstraite, elle est propre à three.js).
```javascript
const plane_geometry = new THREE.PlaneGeometry( 400, 400 );
```

Ensuite on crée notre matériau avec `MeshStandardMaterial`. On spécifie sa couleur 
en hexadécimal (par exemple ici c'est du blanc). 
```javascript
const plane_material = new THREE.MeshStandardMaterial( color:0xffffff );
```

Puis on crée notre objet avec `Mesh` qui prend en paramètres la géométrie et le 
matériau. Tournons aussi notre plan pour faire un sol.
```javascript
const plane = new THREE.Mesh( plane_geometry, plane_material );
plane.rotateX( - Math.PI / 2 );
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

### Adapter l'app à la fenêtre du navigateur

Notre renderer apparait bien, mais n'occupe pas toute la fenêtre. En plus, il ne 
s'adapte pas à la taille de la fenêtre lorsqu'on la modifie.

Rajoutons cette fonction dans le main.js (en dehors de la fonction`init()`) pour 
permettre au renderer d'adapter sa taille en temps réel :

```javascript
function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();

    renderer.setSize( window.innerWidth, window.innerHeight );
}
```

On voit ici qu'on modifie à la fois le champ de la caméra et la taille du renderer. 
On doit ensuite ajouter un listener à la fin de notre fonction `init()`, 
qui vérifie si la taille de la fenêtre est 
modifiée, et appelle la fonction `onWindowResize()`quand c'est le cas :

```javascript
window.addEventListener( 'resize', onWindowResize );  
```

C'est mieux, mais on a toujours des marges blanches autour de notre renderer. 
Allons dans notre fichier `style.css`. On peut pour l'instant enlever ce qui y 
était et modifier la marge du body :

```css
body {
    margin: 0;
}
```

Parfait, maintenant améliorons le rendu de nos objets.

### Lumière
On peut améliorer notre rendu en ajoutant des lumières. Pour ajouter une lumière, c'est très simple, il suffit d'ajouter:


```javascript
const light = new THREE.DirectionalLight(0xffffff, 1);
```

Le premier argument est le code couleur en hexadécimal de la lumière et le deuxième est son intensité.

Il suffit ensuite de choisir sa position et de l'ajouter à la scène :

```javascript
light.position.set(20, 400, 200);
scene.add(light);
```
On a alors un plan qui est éclairé par le dessus.

### Ombres
Un autre aspect pour augmenter la beauté de notre projet sont les ombres ! On peut en effet rajouter des ombres dans Three.js. Pour se faire, rien de plus simple :

On ajoute en premier un cube pour pouvoir voir les ombres :

```javascript
const cube_geometry = new THREE.BoxGeometry(10,10)
const cube_material = new THREE.MeshStandardMaterial(0xffffff);
const cube = new THREE.Mesh( cube_geometry, cube_material);
cube.position.set(0,10,0);

```
Il faut maintenant lui autoriser à diffuser des ombres :
```javascript
cube.castShadow= true;
scene.add(cube);
```

De même pour la lumière, il faut aussi lui autoriser :

```javascript
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

### Fond et Brouillard

Pour l'instant le fond est complètement noir, c'est un peu triste. Rajoutons un 
fond bleu ciel et un effet de brouillard avec la distance.

Pour cela, rien de plus simple, ces deux lignes suffisent (à rajouter quand on crée 
notre scène):
```javascript
scene.background = new THREE.Color(0x87CEFA);
scene.fog = new THREE.Fog(0x87CEFA, 1, 200);
```
En choisissant la même couleur pour les deux, on a l'impression de ne plus distinguer 
le sol au loin (il se fond avec le fond). Les deux autres paramètres de `Fog()` 
sont near et far, c'est le même principe que lorsqu'on a créé la caméra.

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
Le problème est que la texture a besoin d'être rendue en boucle (on ne la voit pas sinon). Il faut donc rajouter la fonction suivante à la fin:

```javascript
function animate(){
    renderer.render(scene,camera);
    requestAnimationFrame(animate)
}
animate()
```

animate() est exécutée à chaque frame: Dès qu'on veut modifier quelque chose en temps réel, on utilise cette fonction.

### Pour un beau parquet

Maintenant qu'on a fait la texture du cube, on peut aller plus loin en faisant la texture du sol. On va alors utiliser cette [texture](https://drive.google.com/drive/folders/1_muKfn_cQXV6VTWbxuJpywb0tMq51SD8).
On refait le même travail :

```javascript
    const textureloaderWood = new THREE.TextureLoader()
    const textureBasecolorWood = textureloaderWood.load('img/Wood_Floor_009_basecolor.jpg')
    const textureAmbientOcclussionWood = textureloaderWood.load('img/Wood_Floor_009_ambientOcclusion.jpg')
    const textureheightWood = textureloaderWood.load('img/Wood_Floor_009_height.png')
    const texturenormalWood = textureloaderWood.load('img/Wood_Floor_009_normal.jpg')
    const textureroughnessWood = textureloaderWood.load('img/Wood_Floor_009_roughness.jpg')
```
A l'exception qu'ici notre texture est trop petite pour recouvrir tout notre sol. On doit alors répéter la texture : 
```javascript
    textureBasecolorWood.wrapS = textureBasecolorWood.wrapT =THREE.RepeatWrapping
    textureBasecolorWood.repeat.set(15,15)
    textureAmbientOcclussionWood.wrapS = textureAmbientOcclussionWood.wrapT=THREE.RepeatWrapping
    textureAmbientOcclussionWood.repeat.set(15,15)
    textureheightWood.wrapS = textureheightWood.wrapT=THREE.RepeatWrapping
    textureheightWood.repeat.set(15,15)
    texturenormalWood.wrapS = texturenormalWood.wrapT=THREE.RepeatWrapping
    texturenormalWood.repeat.set(15,15)
    textureroughnessWood.wrapS = textureroughnessWood.wrapT=THREE.RepeatWrapping
    textureroughnessWood.repeat.set(15,15 )
```

S et T sont les dimensions 2D de recouvrement de texture, on leur dit de wrap en S et en T suivant un schéma de repeat qui est set à 15 répétitions suivant chaque coordonnée.

## Déplacement de la caméra

Il est des fois plus agréable de pouvoir déplacer la caméra comme on le souhaite pour pouvoir bien visualiser ce que l'on est en train de modéliser. En conception 3D, il est important de pouvoir observer son travail sous plusieurs angles afin de s'assurer que tout correspond bien à ce que l'on souhaite. En effet on peut faire le cube le plus joli qu'on souhaite, si la caméra est toujours pointée dans la même direction , on ne verra jamais l'arrière de ce cube et il ne correspond peut etre pas du tout à ce que l'on veut.

On a vu qu'il est possible de changer la position et vers où la caméra regarde dans le code. Ce n'est pas forcement le plus intéressant pour pouvoir déplacer la caméra "à la volée" autour d'un objet pour en vérifier les propriétés pendant les phases de développment.

On va donc essayer de mettre en place une méthode de déplacement de la caméra qui soit contrôlée par l'utilisateur au niveau de l'affichage dans le navigateur web. Et traditionnellement, pour permettre à un utilisateur d'interagir avec un programme, qu'est ce qu'on utilise ? Un clavier et/ou une souris !

Pour cette partie, on va s'inspirer de [cet exemple](https://threejs.org/examples/misc_controls_pointerlock.html) de la librairie Three.js.
### Déplacement en mode fps
    
Il existe plusieurs controleurs de caméra déjà intégrés
dans Three.js et ici on va utiliser `PointerLockControls`. Tout 
d'abord il faut l'importer :

```javascript
import { PointerLockControls } from 'three/examples/jsm/controls/PointerLockControls';
```

Une fois importé, on peut déjà déclarer une variable `controls` au même endroit de que l'on a déclaré `camera, renderer, scene`

Ensuite, dans notre fonction `init`, on peut directement ajouter les lignes : 
```javascript
    controls = new PointerLockControls( camera ,  document.body );

    document.body.addEventListener( 'click', function () {
        
        controls.lock();
        
    }, false );
    
    scene.add( controls.getObject() );
```

On crée d'abord un objet `PointerLockControls` et on va demander au `body` de notre document d'attendre que l'utilisateur clique
sur la fenêtre pour lock sa souris et il pourra contrôler la vue.

Maintenant il s'agit de lier les touches du clavier au code.

On va d'abord créer en début de script plusieurs constantes que nous pourrons utiliser par la suite :

```javascript
let moveForward = false;
let moveBackward = false;
let moveLeft = false;
let moveRight = false;
let canJump = false;
```
Ces variables vont nous aider à choisir la direction de notre personne.

On va ensuite créer deux constantes qui modifieront ces variables : 

```javascript
const onKeyDown = function ( event ) {

        switch ( event.code ) {

            case 'ArrowUp':
            case 'KeyW':
                moveForward = true;
                break;

            case 'ArrowLeft':
            case 'KeyA':
                moveLeft = true;
                break;

            case 'ArrowDown':
            case 'KeyS':
                moveBackward = true;
                break;

            case 'ArrowRight':
            case 'KeyD':
                moveRight = true;
                break;

            case 'Space':
                if ( canJump === true ) velocity.y +=250;
                canJump = false;
                break;

        }
    };

    const onKeyUp = function ( event ) {
        switch ( event.code ) {

            case 'ArrowUp':
            case 'KeyW':
                moveForward = false;
                break;

            case 'ArrowLeft':
            case 'KeyA':
                moveLeft = false;
                break;

            case 'ArrowDown':
            case 'KeyS':
                moveBackward = false;
                break;

            case 'ArrowRight':
            case 'KeyD':
                moveRight = false;
                break;

        }
    };
```

Par la suite on va faire en sorte que notre jeu écoute ce que l'on tape :

```javascript
document.addEventListener( 'keydown', onKeyDown );
document.addEventListener( 'keyup', onKeyUp );
```

Maintenant nous avons notre code qui écoute notre clavier et des variables dont les valeurs varient en fonction de nos touches
pressées. Il faut maintenant pouvoir bouger. Pour cela on va créer en variable globale deux vecteurs `direction` et `velocity` :

```javascript
const velocity = new THREE.Vector3();
const direction = new THREE.Vector3();
```

Et on va ajouter une variable temps :

```javascript
let prevTime = performance.now();
```

Une fois fait, on peut aller dans notre fonction `animate` pour faire bouger notre petit personnage.

On va commencer par créer une nouvelle constante temps :
```javascript
const time = performance.now();
```

Puis, après vérification que les contrôles sont locked :

```javascript
if ( controls.isLocked === true ) {
    
    
            const delta = ( time - prevTime ) / 1000;
    
            velocity.x -= velocity.x * 10.0 * delta;
            velocity.z -= velocity.z * 10.0 * delta;
    
            velocity.y -= 6* 100.0 * delta; // 100.0 = masse
    
            direction.z = Number( moveForward ) - Number( moveBackward );
            direction.x = Number( moveRight ) - Number( moveLeft );
            direction.normalize(); 
    
            if ( moveForward || moveBackward ) velocity.z -= direction.z * 400.0 * delta;
            if ( moveLeft || moveRight ) velocity.x -= direction.x * 400.0 * delta;
            
    
            controls.moveRight( - velocity.x * delta );
            controls.moveForward( - velocity.z * delta );
    
            controls.getObject().position.y += ( velocity.y * delta ); 
    
            if ( controls.getObject().position.y < 10 ) {
    
                velocity.y = 0;
                controls.getObject().position.y = 10;
    
                canJump = true;
    
            }
    
        }
```

Expliquons ces lignes :

* On va créer un intervalle de temps entre la dernière fois qu'on a rendu le monde et maitenant
* Ensuite on setup l'inertie : plus le chiffre est grand, plus la vitesse reviendra à 0 vite (.js mdr)
* Ici on simule la gravité : on a pris 6 comme valeur pour un meilleur gameplay
* Ici on gère le vecteur pour savoir où on se dirige en transformant les booléens en nombres
* On augmente la vitesse suivant la direction avec comme valeur 400 ( modifiable pour plus de fun )
* On applique la vitesse à notre controller (en y aussi si on saute)
* On reset la vitesse en y si on est au sol

A la fin de ce `if`, il ne faut pas oublier de :
```javascript
        prevTime = time;
        renderer.render( scene, camera );
```
### Bonus: Rotation autour d'un point fixe

Une autre méthode souvent utilisée consiste à autoriser une rotation de la caméra à l'aide de la souris. Ce type de contrôle s'appelle OrbitControl dans three.js. C'est un contrôle très simple à mettre en place et à utiliser. Juste en maintenant le clic gauche de la souris et en bougeant la souris, on change l'axe de visualisation de la caméra.

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
for ( let i = 0; i < 100; i ++ ) {

        const cube = new THREE.Mesh( cube_geometry, cube_material );
        cube.position.x = Math.floor( Math.random() * 20 - 5 ) * 10;
        cube.position.y = Math.floor( Math.random() * 20 ) * 5 + 5;
        cube.position.z = Math.floor( Math.random() * 20 - 5 ) * 10;
        cube.castShadow = true;
        cube.receiveShadow = true;

        scene.add( cube );
        objects.push( cube );

    }
```

### Détection de sol

On doit aussi rajouter des contrôles pour pouvoir s'amuser avec ces cubes et sauter dessus. On va d'abord créer une variable globale 
```javascript
let raycaster;
```

A la fin de la fonction `init`, on va ajouter la ligne :
```javascript
raycaster = new THREE.Raycaster( new THREE.Vector3(), new THREE.Vector3( 0, - 1, 0 ), 0, 10 );
```
pour initialiser la valeur du raycaster, qui sera en fait nos pieds.

On va donc ensuite aller dans la fonction `animate`, dans le `if`:
```javascript
raycaster.ray.origin.copy( controls.getObject().position );
raycaster.ray.origin.y -= 10;
```
On récupère la position de la camera et on y soustrait la taille qui est de 10 ici.

Ensuite on crée ceci :

```javascript
            const intersections = raycaster.intersectObjects( objects, false );
    
            const onObject = intersections.length > 0;
```

On regarde si nos pieds sont en intersection avec un objet de la liste `objects`.

Et si on est sur un objet, c'est qu'on était en saut donc on ne pouvait plus sauter :

```javascript
            if ( onObject === true ) {
    
                velocity.y = Math.max( 0, velocity.y );
                canJump = true;
    
            }
```

## Conclusion

Pour décortiquer un peu plus ou juste si vous êtes perdu, voici le [repo git du projet final](https://github.com/LeoLaurent/three-js-project)

# Références

[La documentation Three js](https://threejs.org/docs/index.html)

[Plein d'exemples de projets en Three js](https://threejs.org/examples/#webgl_animation_cloth)

[Tutoriel des bases de Three js](https://www.youtube.com/watch?v=YK1Sw_hnm58)

Shadow et light : 

* [Gérer la caméra responsable des ombres](https://stackoverflow.com/questions/48355479/three-js-directionallight-and-shadow-cut-off)
* [Faire des ombres plus sympas](https://stackoverflow.com/questions/41212156/create-very-soft-shadows-in-three-js)

Textures :

* [Site de textures 3D open source](https://3dtextures.me/)
* [Tuto texture](https://www.youtube.com/watch?v=thVl4UOQSEM)