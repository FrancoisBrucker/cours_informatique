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

Pour faire simple, Webpack réalise une concaténation "intelligente" des fichiers: chaque fichier indique ses dépendances, qui sont incluses dans un graphe global. 
Pour cela, Webpack fonctionne alors en deux étapes. 

# Une étape de détermination des dépendances

Webpack part du fichier "entrée" spécifié dans la configuration, puis parcourt le fichier à la recherche de modules dépendant de cette entrée. Il parcourt ensuite chacun de ses modules à la recherche de modules qui en dépendent, construisant alors un graphe de dépendance. Ainsi de suite, jusqu'à ce que toute l'arborescence des dépendances soit épuisée.  

# Une étape d'empaquetage

Webpack empaquete alors les fichiers dans un seul même fichier n'utilisant que le nécesaire à chaque module. Par exemple, si une seule fonction d'un module est utilisée, seule cette fonction sera compilée dans le fichier de sortie.


## Et comment on utilise Webpack ?

# Tutoriel 

Webpack propose un tutoriel simple pour pouvoir comprendre le fonctionnement du bundling. L'idée de ce tutoriel est d'abord d'importer le module lodash directement dans le fichier de départ index.html. Avec Webpack, on importe le module dans le fichier entrée script et au moment de compiler, webpack introduit un fichier bundle.js en sortie qui compile le script source avec les fonctions du module lodash qui sont utilisées.

 
Ici, le tutoriel

#  Paramétrer le fichier de configurations 
