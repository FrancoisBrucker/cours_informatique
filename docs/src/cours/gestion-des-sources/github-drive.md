---
layout: layout/post.njk

title: Github comme un drive

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

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