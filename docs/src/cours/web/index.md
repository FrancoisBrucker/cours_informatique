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
* background
* police de caractères

## Troisième partie : Boîtes et positionnement

1. [modèle de boîtes](./modele-boites)
2. positionnement fixed, static, relative, absolute (plus flottant car moins pratique que flex) <https://developer.mozilla.org/fr/docs/Learn/CSS/CSS_layout/Positioning>. z-index. Utile avec les balise de comportement header, footer, aside, etc.

exercice : flex + grid
exercice : faire une interface à un jeu ?

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
