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

## Système

{% aller %}
[Interagir avec le système](système){.interne}
{% endaller %}

## Réseau

{% aller %}
[Interagir avec le réseau](système){.interne}
{% endaller %}

## Installation


{% aller %}
[Nouvelle installation d'un système](installation){.interne}
{% endaller %}
