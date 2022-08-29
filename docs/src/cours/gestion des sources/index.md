---
layout: layout/post.njk 
title: Gestion des sources

tags: ['cours', 'débutant', 'code', 'python']

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
      * ou <https://github.com/[votre login]> en remplaçant `[votre login]` par votre login.
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

## github desktop

Travailler depuis le site uniquement est très limitant. Github est le lieu où est stocké du projet, l'outil qui fait tout fonctionner est [git](https://fr.wikipedia.org/wiki/Git). Avant d'utiliser la ligne de commande qui peut être intimidante, utilisant une application développée par github qui permet d'en utiliser les fonctions les plus courantes.

### Installation

Il suffit d'aller sur cette page : <https://desktop.github.com/> pour télécharger puis installer l'application.

### projet avec desktop

{% chemin %}
[Un projet avec l'application desktop](projet-github-desktop)
{% endchemin %}

Vous avez vu les principales qualités d'un logiciel de gestion de sources :

* faire un clone
* notion de gestion distribuée
* le stage
* faire un rebase

## git

Les notions que l'on a vu précédemment suffisent pour un usage courant de la gestion des sources avec github. Si vous voulez faire de l'informatique votre métier ou si vous voulez :

* savoir exactement comment tout ça fonctionne
* utiliser toutes les possibilités

Il vous faudra utiliser le programme `git` en ligne de commande.

{% chemin %}
[Configuration et fonctionnement de git](git)
{% endchemin %}

* En ligne de commande
* vscode plugin gitgraph ?

et github cli <https://docs.github.com/en/github-cli/github-cli/about-github-cli>

## S'entraîner

Projet numérologie.
