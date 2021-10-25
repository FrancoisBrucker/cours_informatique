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

### three.js et vite

## Les bases

### Structure du projet

### Scene, Camera et Renderer

### Créer un plan: Geometry et Material

## Go rendre ça plus joli

### Lumière ambiante

### Ombres

### Textures

## Déplacement de la caméra

### Déplacement avec ZQSD

### Rotation avec la Souris

## Génération du monde
