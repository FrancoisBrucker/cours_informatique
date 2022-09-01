---
layout: layout/post.njk 
title: Gestion des sources

tags: ['cours', 'projet']

authors:
    - François Brucker

eleventyNavigation:
  key: "Gestion des sources"
  parent: Cours
---

<!-- début résumé -->

Comment gérer les sources d'un projet avec git et github.

<!-- fin résumé -->

## Gestion des sources

https://www.youtube.com/watch?v=w3jLJU7DT5E

Marche aussi avec du texte. Comme un rapport écrit en markdown (ou en latex par exemple).

On doit pouvoir :

* travailler à plusieurs sur un projet et toujours avoir la dernière version
* travailler sur le même document
* avoir accès à toutes les versions du projet, quite à revenir en arrière si besoin

{% attention %}
Dire que l'on connaît git ou github parce qu'on se sert de github comme d'un drive est un mensonge et vous fera passer pour un rigolo...
{% endattention %}

## Github

<https://github.com/> est une interface au logiciel de gestion de sources [git](https://fr.wikipedia.org/wiki/Git). Il en existe d'autres, comme <https://gitlab.com/> par exemple.

{% info %}
L'[aide de github](https://docs.github.com/en/get-started) est très bien faite, n'hésitez pas à y jeter un coup d'œil.
{% endinfo %}

### Création du compte github

1. créez votre compte avec github
   * On crée ici votre compte github *pro*, ne mettez pas de bêtises
   * Utilisez une adresse mail pérenne (genre votre adresse pro gmail ou votre adresse ecm)
2. modifier son profile :
   1. Allez dans la modification du profile :
      * en haut à droite de la fenêtre puis *"Your profile"*
      * ou `https://github.com/<votre login>` en remplaçant `<votre login>` par votre login.
   2. Il **faut** mettre de bonnes info car lorsque vous modifiez le code vous êtes responsable de ce que vous modifiez. Il faut donc :
       * savoir qui a modifier le code et pourvoir le retrouver
       * votre compte github est aussi votre book. Il permet de savoir ce que vous avez fait.
       * Mettez donc au moins :
         * un vrai nom
         * une vrai photo (rechargez la page pour avoir la nouvelle photo)

### Utilisation de github

{% chemin %}
[Un projet uniquement avec github](projet-github)
{% endchemin %}

Vous avez vu les principales qualités d'un logiciel de gestion de sources :

* faire des commit
* gérer des branches
* fusionner des branches en résolvant des conflits
* voir l'historique du projet
* comment ajouter des membres à un projet

## Github desktop

Travailler depuis le site uniquement est très limitant. Github est le lieu où est stocké du projet, l'outil qui fait tout fonctionner est [git](https://fr.wikipedia.org/wiki/Git). Avant d'utiliser la ligne de commande qui peut être intimidante, utilisant une application développée par github qui permet d'en utiliser les fonctions les plus courantes.

### Installation

Il suffit d'aller sur cette page : <https://desktop.github.com/> pour télécharger puis installer l'application.

### Projet avec desktop

{% chemin %}
[Un projet avec l'application desktop](projet-github-desktop)
{% endchemin %}

Vous avez vu les principales qualités d'un logiciel de gestion de sources :

* faire un clone
* notion de gestion distribuée
* le stage
* faire un rebase

## Bonnes pratiques

{% chemin %}
[Bonnes pratiques](bonnes-pratiques)
{% endchemin %}

Pour participer à un repo github/gitlab il y a quelques us et coutumes à respecter afin de permettre au mieux la relecture, l'ajout de fonctionnalités et la compréhension de chacun.

## Git

Les notions que l'on a vu précédemment suffisent pour un usage courant de la gestion des sources avec github. Si vous voulez :

* utiliser git avec votre éditeur de texte comme vscode
* ou si vous voulez utiliser git en ligne de commande pour contrôler toutes vos opérations

Il vous faudra installer le programme `git` en ligne de commande.

{% info %}
L'installation et la configuration de git n'est pas très technique. Cela vaut le coup de de le faire ne serait-ce que pour pouvoir utiliser les magnifiques plugins de vscode.
{% endinfo %}

### Installation et configuration

{% chemin %}
[Configuration et initialisation de projets avec git](git-init)
{% endchemin %}

### Utilisation de git avec vscode

{% chemin "**Documentation :**" %}
<https://code.visualstudio.com/docs/editor/versioncontrol#_git-support>
{% endchemin %}

vscode permet d'utiliser directement les commandes git et possède de nombreux plugins permettant, par exemples :

* d'utiliser github avec l'[extension github](https://code.visualstudio.com/docs/editor/github)
* de voir le graphe de dépendances avec l'extension [git-graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) (commande `git-graph.view` pour voir le graphe)
* de voir l'historique de modification d'un fichier avec l'extension [git-history](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory) (cliquer droit sur un fichier puis `Git: view file history`)
* ...

### Dans les détails

{% chemin %}
[Git dans les détails](./git)
{% endchemin %}

Cette partie du cours s'adresse plus particulièrement aux informaticiens voulant utiliser git en ligne de commande et/ou à ceux voulant comprendre le fonctionnement précis de git.
