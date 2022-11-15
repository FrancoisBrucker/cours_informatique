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

## <span id="trinité"><span>  Trinité html/css/js

### Découverte d'html

1. Introduction avec les [outils de développement](./outils-de-développement/)
2. [Introduction à html](./html-introduction) chez soit dans un seul fichier
3. Différence entre exécuter un fichier soit et sur un serveur : [Qu'est qu'une url ?](./anatomie-url)
4. [Projet html](./projet-html)

### Découverte de css

1. [Introduction à css](./css-introduction)
2. [Unités et couleurs](./unités-couleurs)
3. [Sélecteurs css](./sélecteurs-css)

> TBD :
>
> * animations
> * fontes (à refaire avec la nouvelle api)

### Gestion des fichiers

{% chemin %}
<https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/Dealing_with_files>
{% endchemin %}

Ayez :

1. un dossier spécifique où vous rangez tout votre site
2. à l'intérieur de ce dossier, le fichier `index.html`{.fichier} est l'entrée de votre site
3. ayez des dossiers spécifiques pour ranger les différents types de fichiers que vous utiliserez

{% note %}
Utilisez **toujours** des chemins relatifs lorsque vous référencez vos fichiers.
{% endnote %}

### Boîtes et positionnement

1. [modèle de boîtes](./modèle-boites)
2. [balise anonymes](./balises-anonymes)
3. [positionnement](./positionnement)

> TBD :
>
> * à présenter : flex + grid
> * exercice à présenter : design de page

### Bibliothèques css

* exercice à présenter

exercices : bibliothèque css. Utilisation avec un cdn.

* bootstrap
* lib à la mode en 2022
* ...

Comment :

* cdn
* téléchargement des fichiers (on verra plus tard comment faire mieux avec npm)
* node_modules (npm pour gérer des paquets et utilisation de npm sans node pour le front)

### Javascript

1. [Bases de javascript](./javascript-bases)
2. [Manipuler l'arbre DOM en javascript](./javascript-dom)
3. [gestion des événements](./javascript-événements)

{% faire %}
[Projet Numérologie](projet-numerologie) partie 1.
{% endfaire %}

## <span id="serveur"><span> Serveur web

Comprendre numérologie 1

1. [Lire des données](lire-données)
2. [Serveur web](serveur-web)

{% faire %}
[Projet Numérologie](projet-numerologie) partie 2.
{% endfaire %}

à faire : décathlon, faire un client/serveur : tous

exercice : ??

## <span id="données"><span> Gestion de données

1. [côté serveur](./gestion-données-serveur)
2. [utiliser des bases de données](bases-de-données)
3. [côté client](./gestion-données-client)
4. [cookies](./gestion-données-cookies)

## Projets

### A vous : Décathlon

* règles :
  * sur le site du créateur : <https://www.knizia.de/wp-content/uploads/reiner/freebies/Website-Decathlon.pdf>
  * en français : <http://www.jeuxprintandplay.fr/Fiches%20jeux/Fiche%20jeu%20Decathlon.html>
* supports pour y jouer en vrai : <http://juegosrollandwrite.com/remake-reiner-knizias-decathlon/>

Choisissez un sport et faite toute la partie jet de dés côté serveur pour éviter la triche.
Ne stockez as de données côté serveur.

Certains présenteront la fois d'après.

### Numérologie

{% chemin %}
[Projet Numérologie](projet-numerologie)
{% endchemin %}

### Commentaires

> TBD

## Stocker des données

> TBD :
>
> * cookies
> * localstorage