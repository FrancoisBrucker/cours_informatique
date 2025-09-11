---
layout: layout/post.njk

title: Interagir avec le système

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons voir ici deux choses fondamentales :

1. l'organisation du système en dossiers et fichiers
2. comment interagir avec le système via le terminal

{% info %}
Fonctionne avec les 3 systèmes Windows 11, Linux et MacOs.
{% endinfo %}

## Programmes

{% aller %}
[Programmes et bibliothèques système](fichiers-exécutable){.interne}
{% endaller %}

> TBD fichiers exécutables et bibliothèque (dll)
> TBD exemple de vscode <https://code.visualstudio.com/> : ou il est (windows, linux, mac), ses paramètres (système, utilisateur).

{% info %}
Pour utiliser vscode en développement, vous pouvez aller :

[éditeur vscode](/cours/coder-et-développer/bases-programmation/interpréteur/éditeur-vscode/){.interne}
{% endinfo %}

## Fichiers

Quel que soit le système d'exploitation que vous utilisez, les données (ainsi que les applications) sont stockées sous la forme de **_fichiers_** organisé en arbre. Il est crucial de savoir y naviguer.

{% aller %}
[Naviguer dans un système de fichiers](fichiers-navigation){.interne}
{% endaller %}

Le système d'exploitation a besoin de ses propres fichiers pour fonctionner correctement. Selon le système d'exploitations, ils sont rangés différemment :

{% aller %}
[Hiérarchie système](fichiers-système){.interne}
{% endaller %}
