---
layout: layout/post.njk
title: Problème algorithmique

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


On a vu que toute question n'admet pas forcément un algorithme pour le résoudre et que si on possède un algorithme il n'est pas évident de savoir ce qu'il fait. Cependant, on utilise quotidiennement des algorithmes et on se repose sur eux pour résoudre des problèmes concret.

Comment faire c eci alors que l'on a vu qu'il n'existe pas de procédure automatique pour le faire (on l'a vue, c'est [le théorème de Rice](../bases-théoriques/arrêt-rice/#théorème-rice){.interne}) ? C'est ce qu'on va aborder ici, en deux temps :

1. on va commencer par formaliser ce qu'est un problème
2. se donner des outils pour prouver qu'un algorithme donné résout bien le problème posé.

{% note "**Définition**" %}
Un **_problème_** est un texte composé de 3 parties :

- **nom** : le nom du problème
- **données** : les paramètres dont on a besoin
- **question** : ce que l'on cherche

{% endnote %}

Par exemple :

{% note "**Problème**" %}

- **nom** : maximum
- **données** : un tableau d'entiers
- **question** : quel est l'entier maximum du tableau ?

{% endnote %}

On se placera dans ce cours dans un cadre algorithmique : c'est à dire des problèmes qui admettent des algorithmes qui en trouve la solution (on se posera donc uniquement des questions sérieuses comme la recherche d'un éléments dans un tableau et on laissera de côté les problèmes futiles comme ["quand est-ce qu'on mange ?"](https://www.youtube.com/watch?v=WtetsFQHD9A) ou encore ["quel est le sens de la vie ?"](https://www.youtube.com/watch?v=LAwDWZoETk4)). Définissons formellement ce type de problème :

{% note "**Définition**" %}
**_Un problème est algorithmique_** s'il existe un algorithme pour le résoudre, c'est à dire que cet algorithme :

- prend en paramètres les entrées du problème
- donne la réponse à la question.

{% endnote %}

Cette définition a un sens puisqu'[il existe des problèmes non résoluble par un algorithme](../bases-théoriques/calculabilité#non-calculable){.interne}.
