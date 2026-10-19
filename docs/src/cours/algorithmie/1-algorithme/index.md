---
layout: layout/post.njk

title: "Partie I : Écrire des algorithmes"
eleventyNavigation:
  prerequis: 
    - "/cours/coder-et-développer/apprendre-programmation/concepts/"

eleventyComputed:  
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Ce que devrait connaître tout ingénieur en algorithmie.

## Algorithmes et programmes

Commençons par définir ce qu'est un algorithme et ce qu'il peut ou ne peut pas faire :

{% aller %}
[Bases théoriques](./bases-théoriques)
{% endaller %}

### Pseudo code

On peut maintenant définir une grammaire permettant décrire des algorithmes sous la forme de pseudo-code et s'en servir pour résoudre des problèmes :

{% aller %}
1. [Écrire les algorithmes en pseudo code](./pseudo-code)
2. [Pseudo-code = algorithme](./thèse-church-turing)
{% endaller %}

### Problème algorithmique

{% aller %}
[Problème algorithmique et preuve d'algorithmes](./problème-preuve)
{% endaller %}


### <span id="entraînement-preuve"></span>On s’entraîne : création d'algorithmes itératifs et récursifs

> TBD à regrouper en seul gros truc.

Une série de problème algorithmique à résoudre par des algorithmes simples et clairs. Le but d'un algorithme papier est d'être compris.

{% aller %}
1. [Projet : Écrire et prouver des algorithmes itératifs et récursifs](./projet-itératif-récursif)
2. [Projet : techniques de récursion](./projet-techniques-de-récursion)
{% endaller %}



On vérifie qu'on sait faire :

{% aller %}
[exercices non corrigés](./exercices-itératif-récursif)
{% endaller %}

## Complexité

> TBD : une fois qu'on a un algorithme qui fait ce qu'on veut on essaie de le faire le plus vite possible (en moins d'instruction possible)