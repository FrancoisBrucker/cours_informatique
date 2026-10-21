---
layout: layout/post.njk

title: Mesures de complexités

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Cette partie s'intéresse à la notion de complexités pour un algorithme qui permet de mesurer ses performances.

{% lien %}
[une intro très bien faite sur la complexité des problèmes algorithmiques](https://www.youtube.com/watch?v=n8Z7v09zrl0&list=PLF0b3ThojznQJ6u4FUcpyzi0it5EpR3dh&index=12){.externe}
{% endlien %}

## Complexité d'un algorithme

Cette partie s'intéresse à la notion de complexité d'un algorithme et donne les moyens de la calculer.

{% aller %}
1. [Définition et outil de mesure](./définition-complexité)
2. [Calcul de complexités avec des $\mathcal{O}$](./complexité-algorithmes)
3. [Complexité en moyenne]()
{% endaller %}

Utilisation pour calculer théoriquement et en pratique la complexité d'algorithmes :

{% aller %}
1. [Calcul de complexités avec des $\mathcal{O}$](./complexité-algorithmes)
2. [Complexité en moyenne](./complexité-moyenne)
{% endaller %}

## On s'entraîne

### Projet 

> TBD code
> voir qu'il y a une légère variation à chaque appel même avec les même données. DOnc faire une moyenne.
> pyperf

### Calculs

> TBD exo recherche : min/max/moyenne. Un autre ou moyenne proche du min
Maintenant que l'on peut calculer les complexités, on peut reprendre les algorithmes itératifs et récursifs que [nous avons crées précédemment](./projet-itératif-récursif) :

{% aller %}
[Projet : calculer des complexités d'algorithmes itératifs et récursifs](./projet-calcul-complexite)
{% endaller %}

On vérifie qu'on sait faire :

{% aller %}
[exercices non corrigés](./exercices-calculs-compexités)
{% endaller %}

> TBD : une fois qu'on a un algorithme qui fait ce qu'on veut on essaie de le faire le plus vite possible (en moins d'instruction possible)

<!-- TBD

- ajouter un projet de de code. avec tableaux numpy, split de valeurs, enlever le ramasse=miette etc pour bien calculer en moyenne en code
- tbd ajouter voir si for est pareil que while en pratique.
- tbd gagner un peu est non optimal par rapport à ganger un ordre de grandeur.
- tbd coder les calcul des boucles du cours et voir que effectivement les sommes sont proches.

- ajouter des exercices avec l'ordi avec plusieurs algos pour un même problème puis amélioration de la constantes multiplicative.

-->