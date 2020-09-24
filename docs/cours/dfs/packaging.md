---
layout: page
title: "Packaing"
category: cours
tags: packing web front
author: Adèle Bourgeix & Maxime Vivier
---
# Problèmes actuels:

## Problèmes de support web : 

Les navigateurs supportent mal les modules JavaScript et particulièrement la syntaxe CommonJS utilisée par les développeurs pour résoudre les problèmes d’import/export sur NodeJS.  Cela montre la nécessité d’avoir un outil qui permet l’écriture et le support des modules JS sur le web. 

## Problèmes de gestion des ressources: 

Charger un script JavaScript peut se faire de deux manières :
- via plusieurs scripts importés dans un seul fichier principal (mais les imports successifs peuvent être chronophages)
- via un seul même fichier JS qui contient tout le script nécessaire (mais cela induit des problèmes de portée des variables, de lisibilité...)

De même la gestion des ressources (css, images..) peut être compliquée. 

# Solution ? Le packaging 

Les modules bundlers sont des outils utilisés par les développeurs pour empaqueter leurs modules JS dans un seul fichier JavaScript qui peut être exécuté dans le navigateur. 

Un des avantages est que le packaging permet de charger à la fois les modules mais aussi les ressources dans leur ordre de dépendance défini dans le code. 


# Pourquoi et comment Webpack?

Webpack permet aux développeurs de :
- écrire et charger des modules JS 
- charger les ressources (JS inclus) d’une manière plus simple
