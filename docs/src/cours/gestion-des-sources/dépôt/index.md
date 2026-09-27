---
layout: layout/post.njk

title: Dépôt du code source

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD pas le pytest ni le pycache.

Nous allons voir les besoins minimum pour stocker et distribuer un code source. Pour cela il nous fout un lieu sur internet où l'on pourra déposer son code, nous avons chois d'utiliser  la plateforme [github](https://github.com/), donc commençons par nous y créer un compte :

{% aller %}
[Création d'un compte github](./github-compte){.interne}
{% endaller %}

Après avoir examiné les besoins qui impliquent l'utilisation d'un SCM, on en verra une implémentation possible sur une structure distribuée et l'usage qu'on peut en faire au quotidien.

## Besoins pour un dépôt

{% aller %}
[Besoins](./besoins-dépôt/){.interne}
{% endaller %}

## Projet : dépôt github

Nous allons utiliser <https://github.com/> comme dépôt commun de nos projet. Le site fonctionne avec logiciel de gestion de sources [git](https://fr.wikipedia.org/wiki/Git). Il en existe d'autres, comme <https://gitlab.com/> par exemple.



## Projet 

> TBD un projet

1. nouveau projet
2. upload
3. download zip
4. versions :
   1. mettre un tag : une release
   2. mettre une nouvelle version avec upload (est-ce que ça marche ?)
   3. faire une branche
   4. voir les évolutions

Ayez un `readme.md`{.fichier} comme page d'accueil

> TBD attention à ne pas mettre dans le projet :
>
> - les fichiers de vscode
> - l'environnement virtuel
> - les fichiers qui ne sont pas des sources (test, pyc, etc)