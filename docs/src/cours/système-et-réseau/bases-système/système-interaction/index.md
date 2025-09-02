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

## Fichiers

Quel que soit le système d'exploitation que vous utilisez, les données (ainsi que les applications) sont stockées sous la forme de **_fichiers_** organisé en arbre. Il est crucial de savoir y naviguer.

{% aller %}
[Naviguer dans un système de fichiers](fichiers-navigation){.interne}
{% endaller %}


Le système d'exploitation a besoin de ses pro
{% aller %}
[Organisation des fichiers](fichiers-système){.interne}
{% endaller %}

> TBD fichiers système (/system32 pour windows, fichiers systèmes unix (on y reviendra) et spécificités macos library)

## Programmes 

> TBD exécutables et bibliothèque (dll)
> TBD exemple de vscode <https://code.visualstudio.com/> : ou il est (windows, linux, mac), ses paramètres (système, utilisateur).

{% info %}
Pour utiliser vscode en développement, vous pouvez aller :

[éditeur vscode](/cours/coder-et-développer/bases-programmation/éditeur-vscode/){.interne}
{% endinfo %}
