---
layout: layout/post.njk

title: "Projet : calcul de complexité"

eleventyNavigation:
  prerequis:
    - /cours/algorithmie/projet-itératif-récursif/

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Quelques exemples d'algorithme pour le calcul de la complexité. Nous allons reprendre les algorithmes que nous avons crée précédemment dans la partie [calcul et preuve d'algorithmes](../projet-itératif-récursif){.interne} en utilisant ceux proposés dans la correction.

## Concaténation


## Suppression de valeurs

{% aller %}
[Suppression de valeurs](suppression-valeurs){.interne}
{% endaller %}

## Retournement d'un tableau

## Factorielle

> TBD terminale = for

## Fibonacci

{% aller %}
[Suite de Fibonacci](fibonacci){.interne}
{% endaller %}

## McCarty

## Triangle de Pascal

{% aller %}
[Triangle de Pascal](triangle-pascal){.interne}
{% endaller %}
