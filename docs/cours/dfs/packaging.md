---
layout: page
title: "Packaging"
category: cours
tags: packaging web front
author: Adèle Bourgeix & Maxime Vivier
---
## Problèmes actuels:

### Problème de support web : 

Les navigateurs supportent mal les modules des applications JavaScript et particulièrement la syntaxe CommonJS utilisée par les développeurs pour résoudre les problèmes d’import/export sur NodeJS. 

> **Nota Bene**: Les modules sont des morceaux de code réutilisables créés à partir du JavaScript, des node_modules, des images et des styles CSS de votre application, conçus pour être facilement utilisés dans votre site Web.


Cela montre la nécessité d’avoir un outil qui permet l’écriture et le support des modules sur le web. 

#### Et d'ailleurs c'est quoi ces import/export ?


### Problème de gestion des ressources: 

Par exemple, charger un script JavaScript peut se faire de deux manières :
- via plusieurs scripts importés dans un seul fichier principal (mais les imports successifs peuvent être chronophages)
- via un seul même fichier JS qui contient tout le script nécessaire (mais cela induit des problèmes de portée des variables, de lisibilité...)

De même la gestion des ressources (css, images..) peut être compliquée.
Cet exemple montre la necessité d'optimiser la gestion des modules. 

## Solution ? Le packaging 

Les modules bundlers sont des outils utilisés par les développeurs pour empaqueter leurs modules JS dans un seul fichier JavaScript qui peut être exécuté dans le navigateur. 

Un des avantages est que le packaging permet de charger à la fois les modules mais aussi les ressources dans leur ordre de dépendance défini dans le code. 

