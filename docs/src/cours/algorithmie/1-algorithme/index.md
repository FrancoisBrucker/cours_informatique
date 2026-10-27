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

On peut maintenant définir une grammaire permettant de décrire des algorithmes sous la forme de pseudo-code et s'en servir pour résoudre des problèmes :

{% aller %}
1. [Écrire les algorithmes en pseudo code](./pseudo-code)
2. [Pseudo-code = algorithme](./thèse-church-turing)
{% endaller %}

### Prouver des algorithmes

{% aller %}
[Problème algorithmique et preuve d'algorithmes](./problème-preuve)
{% endaller %}


### <span id="entraînement-preuve"></span>On s’entraîne : création d'algorithmes itératifs et récursifs

Une série de problèmes algorithmiques à résoudre par des algorithmes simples et clairs. Le but d'un algorithme papier est d'être compris.

{% aller %}
[Projet : Écrire et prouver des algorithmes itératifs et récursifs](./projet)
{% endaller %}


On vérifie qu'on sait faire :

{% aller %}
[exercices non corrigés](./exercices-non-corrigés)
{% endaller %}
