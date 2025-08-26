---
layout: layout/post.njk

title: Interagir avec le système

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

> TBD un système sert à stocker des données et exécuter des programmes.

## Un ordinateur pour le développement

> tout doit être propre.

## Système 


### Fichiers

> TBD de façon système, une donnée ou un programme est stocké de la même manière, sous la forme de fichiers

Savoir comment est organisé le disque dur de votre ordinateur

{% aller %}
[Naviguer dans un système de fichiers](fichiers-navigation){.interne}
{% endaller %}

### Programmes 

> TBD Fichiers exécutables
> TBD programme, path
> TBD lien vers vscode et on le recherche sous windows, linux avec l'explorateur et mac.
>

### Le terminal

Le terminal permet d'exécuter rapidement des commandes.

{% aller %}
[Terminal](terminal){.interne}
{% endaller %}

## Réseau

> TBD reprendre la partie réseau et ne garder que :
> - transport
> - url et ressource