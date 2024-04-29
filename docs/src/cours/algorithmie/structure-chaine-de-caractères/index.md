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

## Autre problèmes

- Recherche de sous-mots
- recherche de motifs 
- ...

## Vers les expressions régulières

La recherche de sous-chaine n'est presque jamais utilisée en tant que tel en informatique car il faut trouver l'expression exacte :

- on ne cherche pas les formes proches (ce qui est possible en utilisant l'alignement de séquences)
- on ne cherche pas de motifs (on appelle cela des [expression régulières](https://fr.wikipedia.org/wiki/Expression_r%C3%A9guli%C3%A8re))

Les expressions régulières dépassent de loin le cadre de ce cours mais c'est un sujet à la fois marrant, utile et intéressant. Si vous voulez vous initier en douceur, lisez [le tuto python](https://docs.python.org/fr/3/howto/regex.html) qui y est consacré, ou passez directement à [O'reilly](https://www.oreilly.com/library/view/introducing-regular-expressions/9781449338879/).
