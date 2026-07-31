---
layout: layout/post.njk

title: Dossier et fichiers

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



> TBD termer **_Système de fichiers_**

Quel que soit le système d'exploitation que vous utilisez, les données (ainsi que les applications) sont stockées sous la forme de **_fichiers_** organisé en arbre. Il est crucial de savoir y naviguer.

## Dossiers et fichiers

{% aller %}
[Naviguer dans un système de fichiers](fichiers-navigation){.interne}
{% endaller %}

## Dossiers et fichiers système

> TBD : permet d'approfondir comment est géré l'OS (son démarrage et son fonctionnement)
> 
Le système d'exploitation a besoin de ses propres fichiers pour fonctionner correctement. Selon le système d'exploitations, ils sont rangés différemment :

{% aller %}
[Hiérarchie système](fichiers-système){.interne}
{% endaller %}
