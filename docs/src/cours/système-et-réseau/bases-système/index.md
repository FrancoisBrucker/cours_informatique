---
layout: layout/post.njk

title: Bases

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On suppose ici que vous savez minimalement interagir avec votre système d'exploitation en exécutant des applications via un menu ou l'explorateur de fichiers.

## Principes

{% aller %}
[But et principes d'un système](système-principes){.interne}
{% endaller %}

## Interactions

{% aller %}
[Interagir avec le système](système-interaction){.interne}
{% endaller %}

## Le terminal

Le terminal permet d'exécuter rapidement des commandes.

{% aller %}
[Terminal](terminal){.interne}
{% endaller %}

> TBD terminal : le programme à lancer des programmes.
> TBD path

## Installation d'un nouveau système

{% aller %}
[Nouvelle installation d'un système](système-installation){.interne}
{% endaller %}
