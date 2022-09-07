---
layout: layout/post.njk
title: Web
tags: ['cours', 'web', 'front', 'back']

authors:
    - "François Brucker"


eleventyNavigation:
  key: "Web"
  parent: "Cours"
---

<!-- début résumé -->

Cours de développement web. On y verra la partie front, le back, la gestion d'une API.

<!-- fin résumé -->
{% prerequis %}

* [Avoir un système en état de marche]({{ '/tutoriels/installation-système' | url }})
* [Savoir naviguer dans un système de fichiers]({{ '/tutoriels/fichiers-navigation' | url }})
* [Installation et prise en main de l'éditeur de texte vsc]({{ '/tutoriels/vsc-installation-et-prise-en-main' | url }})
* Il pourra de plus être très utile de :
  * [Savoir ouvrir une fenêtre terminal]({{ '/tutoriels/terminal'  | url }})
  * [D'installez brew si vous êtes sous mac]({{ '/tutoriels/brew'  | url }})

{% endprerequis %}

## Première partie : découverte d'html

1. Introduction avec les [outils de développement](./outils-de-développement/)
2. [introduction à html/css](./html-introduction) chez soit dans un seul fichier
3. différence entre exécuter un fichier soit et sur un serveur : [Qu'est qu'une url ?](./anatomie-url)
4. [projet html](./projet-html)

## Deuxième partie : découverte de css

* sélecteur propriété
* 3 façon d'appeler du css

## Troisième partie : positionnement html

* modèle de boite
* display:
  * box model : padding, margin, border
  * display : inline, box, inline-box (pour les images)

* les boites se mettent :
  * les une en-dessous des autre pour les box
  * les unes à côté des autres pour les inline
* un box prend tout la largeur par défaut
* un inline n'a pas de width.
* Si on veut un inline avec une width : inline-box

> exemple pour centrer une image. 1. display 2. margin.

exercice : flex + grid

## Quatrième partie : javascript

1. js
   1. console
   2. dans le html
   3. fichier séparé (à la fin)
2. allons pls loin :
   1. balises structurelles
   2. balises anonymes et classes css
   3. id et js

exercice :

## projet numérologie
