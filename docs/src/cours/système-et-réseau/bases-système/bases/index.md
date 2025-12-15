---
layout: layout/post.njk

title: Connaissances minimales

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On suppose ici que vous savez minimalement interagir avec votre système d'exploitation en exécutant des applications via un menu ou l'explorateur de fichiers.

## But

{% aller %}
[But et principes d'un système](but){.interne}
{% endaller %}

## Système de fichiers

Quel que soit le système d'exploitation que vous utilisez, les données (ainsi que les applications) sont stockées sous la forme de **_fichiers_** organisé en arbre. Il est crucial de savoir y naviguer.

### Dossiers et fichiers

{% aller %}
[Naviguer dans un système de fichiers](fichiers-navigation){.interne}
{% endaller %}

### Dossiers et fichiers système

Le système d'exploitation a besoin de ses propres fichiers pour fonctionner correctement. Selon le système d'exploitations, ils sont rangés différemment :

{% aller %}
[Hiérarchie système](fichiers-système){.interne}
{% endaller %}
