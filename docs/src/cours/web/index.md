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

1. Introduction avec les [outils de développement](./outils-de-développement/)
2. [introduction à html/css](./html-css-introduction) chez soit dans un seul fichier
3. [Qu'est qu'une url ?](./anatomie-url)

Mettre son site sur l'école avec [cyberduck](https://cyberduck.io/).

index.html = fichier par défaut.

puis ajouter une image. chemin relatif

puis séparer html et css en 2.

1. js
   1. console
   2. dans le html
   3. fichier séparé (à la fin)
2. allons pls loin :
   1. balises structurelles
   2. balises anonymes et classes css
   3. id et js
