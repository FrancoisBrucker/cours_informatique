---
layout: page
title: "Packaging"
category: cours
tags: packaging web front
authors:
	- "Adèle Bourgeix"
	- "Maxime Vivier"
---
## Problèmes actuels:

### Problème de support web : 

Les navigateurs supportent mal les modules des applications JavaScript et particulièrement la syntaxe CommonJS utilisée par les développeurs pour résoudre les problèmes d’import/export sur NodeJS. 

> **Nota Bene**: Les modules sont des morceaux de code réutilisables créés à partir du JavaScript, des node_modules, des images et des styles CSS de votre application, conçus pour être facilement utilisés dans votre site Web.


Cela montre la nécessité d’avoir un outil qui permet l’écriture et le support des modules sur le web. 

### Et d'ailleurs c'est quoi ces import/export ?
Les import/exports ont été introduits en Javascript pour permettre la programmation modulaire déjà présente dans d'autres langages de programmation. 
Un module est un bloc de code cohérent et indépendant. Selon les bonnes pratiques, il est préférable qu'un fichier soit une et une seule fonctionnalité.
Les modules permettent :
- une meilleure maintenabilité du code : un bon module doit être autonome et on doit pouvoir le modifier sans avoir à modifier d'autres scripts.
- éviter de polluer : les modules possèdent leur propre espace de portée globale et les autres scripts n'y ont pas accès par défaut.
- Une meilleure réutilisation du code : comme le disait un saint homme, appliquez la méthode DRY (Don't Repeat Yourself).

Pour réaliser cette structure on exporte une variable, une fonction ou même une classe d'un fichier JS pour pouvoir l'importer dans d'autres fichiers où on aurai besoin de la fonctionnalité en uestion. On choisit donc les éléments d'un module que l'on veut exposer en les précédant d'une déclaration `export`. Ces éléments pourront être importés avec la syntaxe `import` dans d'autres modules.
Les détails de toutes les différentes syntaxes d'[import](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Instructions/import)/[export](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Instructions/export) sont très bien expliqués sur le site developer mozilla.

Ce qu'il faut savoir c'est que JS, quand il voit un `export` il va exposer aux autres fichiers ce qu'il exporte sous la forme d'un objet. De l'autre côté quand JS voit un `import` dans un fichier il va importer l'objet qui était exposé dans l'autre fichier.

### Problème de gestion des ressources: 

Par exemple, charger un script JavaScript peut se faire de deux manières :
- via plusieurs scripts importés dans un seul fichier principal (mais les imports successifs peuvent être chronophages)
- via un seul même fichier JS qui contient tout le script nécessaire (mais cela induit des problèmes de portée des variables, de lisibilité...)

De même la gestion des ressources (css, images..) peut être compliquée.
Cet exemple montre la necessité d'optimiser la gestion des modules. 

## Solution ? Le packaging 

Les modules bundlers sont des outils utilisés par les développeurs pour empaqueter leurs modules JS dans un seul fichier JavaScript qui peut être exécuté dans le navigateur. 

Le packaging a trois buts principaux dans la compilation de votre JS :
* L'optimisation de rendu du code
	* charger tous les modules différents, même ce qui n'est pas utilisé. Le principal problème est avec les nodes_modules qui est un dossier très lourd. Ainsi le principe de "tree-shaking" vient palier à ce problème ne gardant que les objets utilisés dans les librairies et modules.
	* En plus d'être lourd, le node_modules prend du temps à être scanné entièrement pour chercher les dépendances. De même, si le nombre de module devient grand, cela peut prendre un peu plus de temps pour tous les charger. En regroupant tout dans un seul et même fichier (ou parfois plusieurs si c'est nécessaire), le packager réunit déjà dans le script tout ce qui est nécessaire pour fonctionner. 
* Il facilite la gestion des ressources statiques (CSS, images, fontes) en les considérant égalament comme module au même titre que les autres vrais modules.
* Il gomme les problèmes d'ordre d'imports de scripts interdépendants qui peut faire crasher la page.

Un des avantages est que le packaging permet de charger à la fois les modules mais aussi les ressources dans leur ordre de dépendance défini dans le code.
