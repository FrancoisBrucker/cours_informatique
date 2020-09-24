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

## Et comment on utilise Webpack ? 
