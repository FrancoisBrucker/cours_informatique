---
layout: layout/post.njk

title: Architecture des ordinateurs

eleventyNavigation:
    order: 1
    prerequis:
        - "../fonctions/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## OS

Vision utilisateur débutant

> TBD screenshot avec un écran (windows/max) et une appli steam/word

3 OS : doz/mac/Linux/Ubuntu

Exécutions d'applications en cliquant et via le terminal (bases).

Installation d'applications :

* windows : store et install, lisez les paramètres !
* brew : applications Linux sous mac
* snap/apt : Linux/Ubuntu

## Fichiers

Vision utilisateur éclairé

> TBD : système de fichier pour structurer son travail et retrouver des données (exemple de MyApp)

path des applications et modifications de celles-ci

## Développeur

> TBD terminal + vscode + python

## Archi

### Carte mère

<https://fr.wikipedia.org/wiki/UEFI>

> TBD attention plein de vieux trucs sur internet :
>
> * bios (plus depuis 2006)
> * architecture northbridge/southbridge