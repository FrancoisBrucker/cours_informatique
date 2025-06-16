---
layout: layout/post.njk 
templateEngineOverride: njk, md

title: Gestion des source et site do-it
tags: ['enseignement', 'ECM']

eleventyNavigation:
    order: 1
    prerequis:
        - "/cours/coder-et-développer/ordinateur-développement/"
        - "/tutoriels/format-markdown/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



Ce cours introductif ne présuppose aucune connaissance informatique spécifique (à part les acquis du tronc commun, c'est à dire vraiment pas grand chose).

Le but de ce cours est que vous puissiez :

- comprendre la problématique de la gestion des sources
- gérer efficacement un projet à plusieurs
- contribuer [au parcours Do_It](https://francoisbrucker.github.io/do-it/)

### Comment

On utilise git et github pour montrer comment tout ça fonctionne. On fera ça sur un projet existant : [le projet do-it](https://github.com/FrancoisBrucker/do-it).

1. [création d'un compte github](/cours/gestion-des-sources#compte-github){.interne}
2. Ajout en tant que collaborateur
3. utilisation de l'[application desktop](/cours/gestion-des-sources/projet-github-desktop/){.interne} pour [télécharger le projet](/cours/gestion-des-sources/projet-github-desktop/#récupérer-projet){.interne}.
4. Analyse du projet :
   1. fichiers
   2. compilation
   3. visualisation en local
5. contribuer

## Le site Do_It

### Faire des modifications en local

> TBD : prendre un cobaye et utiliser son ordi pour le montrer à tous.

1. fait son home et vérifie en local que c'est ok.
2. voir les ajouts en local et continuer jusqu'à ce que tout se compile bien.
3. commit

### Envoyer ses modifications sur le serveur

> TBD faire en sorte que ce soit bien un rebase

1. pull
2. push

> TBD simuler un merge

## À faire chez soit

1. suivre le cours desktop pour [faire un nouveau projet](/cours/gestion-des-sources/projet-github-desktop/#nouveau-projet){.interne} ce qui vous apprendra les principales actions de la gestion des sources.
2. ajouter ses pok et mon du temps 1.

{% info %}
[Aide markdown du site Do_It](https://francoisbrucker.github.io/do-it/cs/contribuer-au-site/)
{% endinfo %}

## Pour aller plus loin

Continuez le cours suivant, au moins la partie où l'on crée et gère des projets uniquement avec le site github :

{% aller %}
[Cours Gestion des sources](/cours/gestion-des-sources/){.interne}
{% endaller %}

Et si vous voulez faire de l'informatique, faites la suite du cours et faite toute la gestion de projet git au terminal. Vous aurez plus de contrôle sur ce que vous faites.
