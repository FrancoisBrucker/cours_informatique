---
layout: page
title:  "cdn_yarn"
category: tutorial
tags: web
author: Tina ALAEI
---


# Imports de modules

En pratique, un développeur ne code pas lui même toutes ses pages à partir de rien. Souvent, il utilise des 
"paquets", ou modules, qui sont des codes déjà existants qui permettent d'implémenter différentes fonctionnalités sans 
avoir à les coder de zéro. 

Nous allons ici illustrer notre cours à l'aide de [purecss](https://purecss.io/), qui est un template très simpliste 
offrant des styles prédéfinis en css.

## Télécharger les fichiers

Il est parfois possible, depuis la documentation des modules, de télécharger directement les fichiers sources 
nécessaires. Cependant, c'est assez peu recommendé dans le cadre d'un projet à plusieurs. En effet, ce cas 
d'utilisation force le partage de tous les fichiers du module, ce qui est assez lourd au final.

## CDN

Il est aussi possible d'inclure les fichiers à l'aide d'un **CDN (content delivery network)**, ou réseau de 
diffusion de 
contenu en français. Un CDN est un réseau de serveurs qui coopèrent afin de mettre du contenu à disposition sur 
l'internet mondial.

L'ajout par CDN se présente toujours par une balise `<link />` à ajouter dans la balise `<head>` quand il s'agit de 
css, et par une balise `<script>` dans le cas de javascript. Les balises en questions sont disponibles sur la 
documentation des modules.

En l'occurence, ici, pour Purecss, la balise à ajouter dans le `<head>` est :
~~~ html
<link rel="stylesheet" href="https://unpkg.com/purecss@2.0.3/build/pure-min.css" integrity="sha384-cg6SkqEOCV1NbJoCu11+bm0NvBRc8IYLRGXkmNrqUBfTjmMYwNKPWBTIKyw9mHNJ" crossorigin="anonymous">
~~~

Cette ligne de code va importer tout le style compris dans Purecss, ce qui nous permettra d'utiliser les élements 
compris dans le template.

## NPM/YARN


Npm et Yarn sont tous deux des gestionnaires de paquets de Node.js. Ils permettent à l'utilisateur d'installer 
facilement des packets sur des projet. Là où cette solution diffère du simple téléchargement des fichiers en local, 
c'est que ces gestionnaires de paquets gèrent eux même les dépendances utiles au projet, mais aussi qu'il est 
possible de réinstaller tous les packets à partir d'un seul fichier. Il n'y aura donc pas à téléverser chaque module 
téléchargé à chaque fois.

### Installation

Avant toute chose, il faut [**installer Node.js**](https://nodejs.org/en/download/package-manager/). Il est plus propre 
d'installer ça vient un 
gestionnaires de packets.

- Windows : ``scoop install nodejs``
- Mac : ``brew install nodejs``

_Verifiez toutefois que Node.js ne soit pas déjà installé sur votre machine avec_ ``node -v``.


En théorie, **npm est installé avec Node.js** donc vous l'aurez déjà sur votre machine.

_Vous pouvez là encore vérifier via la commande_ ``npm -v``.


Une alternative, parfois plus stable, de npm existe : [**yarn**](https://classic.yarnpkg.com/en/docs/install). 

- Windows : ``scoop install yarn``
- Mac : ``brew install yarn``

### Utilité

Yarn ou Npm vont générer un fichier ``package.json``. Ce fichier peut être vu comme un répertoire des informations 
relatives à notre projet, et en particulier la liste de packages présents/utiles au projet.


### Initialisation

> **_Remarque :_**  Nous illustrons ici l'initialisation avec yarn, mais je préciserais à chaque fois l'équivalent npm 
des commandes.

On initialise le projet via la commande ``yarn init`` (ou ``npm init`` si vous utilisez npm) que l'on exécute - en 
général - dans le dossier racine du projet. Yarn vous posera 
plusieurs questions - relatives aux métadonnées du projet, i.e. nom du projet, description ... - à 
l'issue desquelles il créera un fichier ``package.json``.

### Ajouter des modules

Pour ajouter des packets au projet, il faut executer la commande ``yarn add <nom du packet>`` (ou ``npm install <nom 
du packet>``). Cela va installer le nouveau packet dans un dossier ``node_module``, et ajouter le nom du packet 
ainsi que sa version dans une section ``dependencies`` dans le ``package.json``.

> **_Remarque :_**  Il y a ici cependant une petite subtilité. En effet, il est aussi possible d'installer un package
 en ``devDependencies``.
 On peut installer ainsi les modules qui doivent toujours être inclus avec le projet pour son
  bon fonctionnement avec les ``dependencies``, et ceux qui ne sont utiles que pendant le développement avec les
  ``devDependencies``.

On peut ainsi ajouter purecss à notre projet via la commande :
- Si on veut l'installer avec les ``dependencies`` :
~~~ console
yarn add purecss
~~~
- Si on veut l'installer avec les ``devDependencies`` :
~~~ console
yarn add --dev purecss
~~~
_ou_ ``npm install purecss --save-dev`` _pour la version npm._

### Génerer l'installation des modules

Lorsque l'on execute les commandes ci-dessus, le gestionnaire de packet que l'on utilise installe dans la version du 
projet en local. Cependant, lorsque l'on développe à plusieurs, on ne transmettra jamais le dossier ``node_module``. 
On ne transmettra que le fichier ``package.json`` grace auquel nous allons pouvoir re-génerer en local le dossier 
``node_module``.

Ainsi, pour réinstaller tous les modules, on utilise la commande :
~~~ console
yarn
~~~
_Il est aussi possible d'utiliser_ ``yarn install``. _Pour npm, on utilisera_ ``npm install``.

Si l'on souhaite ignorer les dépendances de développement dans l'installation, notamment dans le cas où l'on veut 
générer les dépendances pour la version en production, il suffit d'ajouter ``--production`` à la commande ci-dessus.


> **_Remarque :_**  Selon le gestionnaire utilisé, nous avons un fichier ``yarn.lock`` ou ``package-lock.json``. Ce 
fichier décrit le contenu véritable du ``node_module`` : l'integralités des packages installés, leur version, et 
les dépendances qui viennent avec. Ce fichier ne doit pas être transféré.

### Comment utiliser les modules installés

En général, il faudra "build" le package via npm build.

Cependant, dans le cas ici présent, avec purecss, les fichier sont déjà buildés, et donc le template est utilisable 
dès son installation. Il suffit d'ajouter le fichier de la même façon qu'on ajoute un css local.

> **_Remarque :_**  En pratique, on ne fera jamais ça. En effet, rares sont les bibliothèques déjà compilées, mais 
c'est aussi pas commun de faire référence au dossier ``node_module`` dans le code. En général on va passer par 
**webpack**, qui va nous permettre de packager tous les modules que l'on utilise dans des fichiers js 
compréhensibles et optimisés pour le navigateur.


### Variables du package.json

Voici un exemple de ce à quoi votre fichier ``package.json`` peut ressembler à présent :
~~~ json
{
  "name": "test",
  "version": "1.0.0",
  "license": "MIT",
  "dependencies": {
    "purecss": "^2.0.3"
  }
}
~~~

Les variables ``name``, ``version``, ``license`` sont des métadonnées liés au projet. On peut aussi parfois voir des 
métadonnées sous des variables telles que ``description``, ``author``, ``repository`` (si le projet a un git) ...

Les variables ``dependencies`` et ``devDependencies`` listent les packets que l'on a voulu installer via npm.

D'autres variables peuvent néanmoins être très utilisées lorsque l'on parle d'un projet.

#### scripts
La variable script au sein du package.json permet de faire des "raccourcis" pour des commandes que l'on va souvent 
utiliser.

Synthaxe de la variable ``scripts`` :
~~~ json
"scripts": {
    "build": "<commande à exécuter>",
    "watch": "<commande à exécuter>",
  }
~~~
_Nous illustrons ici avec "build" et "watch" mises comme commandes raccourcies mais leurs noms et nombre sont le choix du
 développeur qui les met en place._

Une fois que nous avons mis en place ces "raccourcis", il suffit de lancer la commande ``npm run <nom du raccourci>``
 afin d'executer la commande à laquelle le raccourci correspond.

#### config - ou autres -
Cette variable n'est pas "officielle". Elle est seulement créé selon le bon vouloir de la personne qui veut 
l'utiliser. Cependant, quelle que soit son nom, il est parfois utile de créer des variables pour ne pas avoir à 
réecrire pusieurs fois la même chose.

Cet article explique assez bien l'utilité que cela peut avoir : [Variables in package.json](https://brianchildress.co/variables-in-package-json/)

## References

