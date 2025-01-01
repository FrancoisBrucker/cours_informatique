---
layout: layout/post.njk

title: Connaissances système minimales

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On suppose ici que vous savez minimalement interagir avec votre système d'exploitation en exécutant des applications via un menu ou l'explorateur de fichiers.

Nous allons voir ici deux choses fondamentales :

1. l'organisation du système en dossiers et fichiers
2. comment interagir avec le système via le terminal

## Système de Fichiers

Savoir comment est organisé le disque dur de votre ordinateur

{% aller %}
[Naviguer dans un système de fichiers](fichiers-navigation){.interne}
{% endaller %}

## Utilisation du Terminal

Le terminal permet d'exécuter rapidement des commandes.

{% aller %}
[Terminal](terminal){.interne}
{% endaller %}
