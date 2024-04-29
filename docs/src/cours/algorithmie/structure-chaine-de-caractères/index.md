---
layout: layout/post.njk
title: "Structure chaine de caractères"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD : pas implémentation (voir partie code pour utf8 et python). ici juste suite finie de caractère = mot = chaine de caractère
> ordre entre les caractères. facile pour nous mais peut etre un soucis pour les chinois
> implique ordre entre les mots

Différent d'une liste car on ne peut avoir qu'un nombre fini d'éléments à chaque case (un alphabet)
## Structure algorithmique

> monoide

## Encodage

>TBD : pas juste 1 nombre de taille fixe. On module la taille selon l'usage. Plus c'est utilisé plus c'est court. Comment faire ? C'est le principe de unicode

{% aller %}
[encodage](./encodage){.interne}
{% endaller %}

## Recherche de sous-chaines

{% aller %}
[Problème de la recherche de sous-chaines](./recherche-sous-chaines){.interne}
{% endaller %}




