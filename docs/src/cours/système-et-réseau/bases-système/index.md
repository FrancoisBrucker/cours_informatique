---
layout: layout/post.njk

title: Bases système

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On suppose ici que vous savez minimalement interagir avec votre système d'exploitation en exécutant des applications via un menu ou l'explorateur de fichiers.

## Bases

{% aller %}
[Connaissances minimales](bases){.interne}
{% endaller %}

## Le terminal

Le terminal permet d'exécuter rapidement des commandes.

{% aller %}
[Terminal](terminal){.interne}
{% endaller %}

## Installation d'un nouveau système

{% aller %}
[Nouvelle installation d'un système](système-installation){.interne}
{% endaller %}
