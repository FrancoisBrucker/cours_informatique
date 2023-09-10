---
layout: layout/post.njk 
templateEngineOverride: njk, md

title: Gestion des source et site do-it
tags: ['enseignement', 'ECM']

eleventyNavigation:
    order: 1
    prerequis:
        - "/tutoriels/ordinateur-développement/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



Ce cours introductif ne présuppose aucune connaissance informatique spécifique (à part les acquis du tronc commun).

Le but de ce cours est que vous puissiez :

- comprendre la problématique de la gestion des sources
- gérer efficacement un projet à plusieurs
- contribuer au [parcours Do_It](https://github.com/FrancoisBrucker/do-it)

## Plan

1. introduction à la gestion des sources
   1. pourquoi ? Pour ne plus avoir peur d'avancer et de tester ; et pour le travail en groupe
   2. pour qui ? Tout le monde ! C'es un cadeau fait par les informaticiens aux monde. Ne le salopez pas comme la gestion de projet agile...
   3. histoire :
      - <https://www.atikteam.com/fr/blog/page/Gestion-de-sources-centralisee-vs-decentralisee>
      - <https://blog.tarynmcmillan.com/a-history-of-version-control>
2. [création d'un compte github]({{ "/cours/gestion-des-sources" }}#compte-github)
3. inscription au [projet do-it](https://github.com/FrancoisBrucker/do-it)
4. [tuto github]({{ "/cours/gestion-des-sources" }})
5. faire fonctionner le projet Do_It chez soit
6. en utilisant l'[application desktop]({{ "/cours/gestion-des-sources" }}#utilisation-desktop-github), [contribuez au projet do-it](https://francoisbrucker.github.io/do-it/ct/contribuer-au-site/), en ajoutant une page pour vos pok&mon du temps 1.

## Ressources

Tiré essentiellement du cours :

{% aller %}
[Le cours de gestion des sources avec github]({{ "/cours/gestion-des-sources" }})
{% endaller %}

Qui ajoute une description de `git` en lui-même et de comment l'utiliser.

> TBD :
>
> * histoire de la gestion des sources.
> * résumé des différentes action qu'il faut faire pour que tout se passe bien
