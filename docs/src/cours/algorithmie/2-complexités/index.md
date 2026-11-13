---
layout: layout/post.njk

title: Mesures de complexités

eleventyNavigation:
  prerequis: 
    - "/cours/coder-et-développer/apprendre-programmation/coder-projets/"


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
[Définition et outil de mesure](./définitions-mesure-O)
{% endaller %}

Utilisation pour calculer théoriquement et en pratique la complexité d'algorithmes :

{% aller %}
1. [Complexité max et min](./complexité-algorithmes)
2. [Complexité en moyenne](./complexité-moyenne)
{% endaller %}

Enfin, comment mesurer la complexité en pratique (et en python) :

{% aller %}
1. [Algorithmie et aléatoire](./algorithme-aléatoire)
2. [Mesurer la complexité d'un code](./complexité-code)
{% endaller %}

## On s'entraîne

### Vérification des acquis

Deux séries d'exercices simples pour vérifier que le cours est acquis :

{% aller %}
1. [Projet : mesurer des complexités](projet-complexité-code)
2. [Projet : calcul de complexités min et max](projet-calcul-max-min)
{% endaller %}


### Techniques de calcul

Exercices classiques de calcul de complexité (en particulier complexité en moyenne). Ils sont **à connaître** car leurs méthodes de résolution sont utiles :

{% aller %}
1. [Projet : exercices classiques de recherche d'éléments](projet-recherche-élément)
2. [Projet : vérifications expérimentales](projet-recherche-élément-code)
{% endaller %}

### On vérifie qu'on sait faire

{% aller %}
[exercices non corrigés](./exercices-non-corrigés)
{% endaller %}
