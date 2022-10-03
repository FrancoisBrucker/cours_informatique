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

## Découverte d'html

1. Introduction avec les [outils de développement](./outils-de-développement/)
2. [Introduction à html](./html-introduction) chez soit dans un seul fichier
3. Différence entre exécuter un fichier soit et sur un serveur : [Qu'est qu'une url ?](./anatomie-url)
4. [Projet html](./projet-html)

## Découverte de css

1. [Introduction à css](./css-introduction)
2. [Unités et couleurs](./unités-couleurs)
3. [Sélecteurs css](./sélecteurs-css)

> TBD :
>
> * animations
> * fonts (à refaire avec la nouvelle api)

## Gestion des fichiers

<https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/Dealing_with_files>

Ayez :

1. un dossier spécifique où vous rangez tout votre site
2. à l'intérieur de ce dossier, le fichier `index.html`{.fichier} est l'entrée de votre site
3. ayez des dossiers spécifiques pour ranger les différents types de fichiers que vous utiliserez

{% note %}
Utilisez **toujours** des chemins relatifs lorsque vous référencez vos fichiers.
{% endnote %}

## Boîtes et positionnement

1. [modèle de boîtes](./modèle-boites)
2. [balise anonymes](./balises-anonymes) div et span (class)
3. [positionnement](./positionnement)

exercice :

* flex + grid
* design de page

## Bibliothèques css

* exercice

exercices : bibliothèque css. Utilisation avec un cdn.

* bootstrap
* lib à la mode en 2022
* ...

Comment :

* cdn
* téléchargement des fichiers (on verra plus tard comment faire mieux avec npm)

## Javascript

1. [Bases de javascript](./javascript-bases)
2. [Manipuler l'arbre DOM en javascript](./javascript-dom)
3. [gestion des événements](./javascript-événements)
5. lien entre les 3 (tuto cours)

projet numérologie partie 1

> TBD :
>
> * exercices : bibliothèques css
> * à faire pour tous : installation node

### Serveur web

1. node install
2. console node
3. serveur web
4. échanger des données avec json. Problèmes de cors/htaccess
5. npm pour gérer des paquets et utilisation de npm sans node pour le front

projet numérologie partie 2

## Projets

### Numérologie

* numérologie

### Commentaires

> TBD