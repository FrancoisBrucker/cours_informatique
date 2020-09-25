---
layout: page
title: "Webpack"
category: cours
tags: packaging webpack front
author: Adèle Bourgeix & Maxime Vivier
---
## Pourquoi Webpack ?

Webpack permet à la fois : 
+ d'écrire et charger des modules sous n'importe quel format dans le navigateur 
+ d'optimiser l'utilisation des ressources et assets (css, images...)

## Comment ça marche ? 

Pour faire simple, Webpack réalise une concaténation "intelligente" des fichiers en un seul et même fichier: chaque fichier indique ses dépendances, qui sont incluses dans un graphe global. 
Pour cela, Webpack fonctionne alors en deux étapes. 

# Une étape de détermination des dépendances

Webpack part du fichier "entrée" spécifié dans la configuration, puis parcourt le fichier à la recherche de modules dépendant de cette entrée. Il parcourt ensuite chacun de ses modules à la recherche de modules qui en dépendent, construisant alors un graphe de dépendance. Ainsi de suite, jusqu'à ce que toute l'arborescence des dépendances soit épuisée.  

# Une étape d'empaquetage

Webpack empaquete alors les fichiers dans un seul même fichier n'utilisant que le nécesaire à chaque module. Par exemple, si une seule fonction d'un module est utilisée, seule cette fonction sera compilée dans le fichier de sortie.


## Et comment on utilise Webpack ?

# Tutoriel 

Webpack propose un tutoriel simple pour pouvoir comprendre le fonctionnement du bundling. L'idée de ce tutoriel est d'abord d'importer le module lodash directement dans le fichier de départ index.html via une balise script.

En utilisant Webpack, on importe directement le module dans le fichier script d'entrée dit "source" et au moment de compiler, Webpack créée en sortie un fichier bundle.js dit de "distribution" qui compile le script source avec les fonctions du module lodash qui sont utilisées.

 
Ici, le tutoriel

#  Paramétrer le fichier de configurations 

Depuis la version 4 de Webpack, une configuration préalable n'est pas nécessaire mais il est possible de paramétrer un fichier de configuration pour pouvoir changer les fichiers d'entrée et sortie et aussi spécifier les "loaders" pour chaque type de ressource rencontré.


> **Nota Bene**: les loaders permettent de spécifier à Webpack comment traiter la ressource en
 fonction de son type (c'est à dire la nature de son extension).


~~~
const path= require('path');

module.exports = {
	entry: './src/index.js', 
	output: { 
	filename: 'main.js',
	path: path.resolve(__dirname, 'dist'),
		},
	};
~~~

 
