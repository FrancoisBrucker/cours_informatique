---
layout: layout/post.njk

title: "Complexité de problèmes algorithmiques"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Trouver le meilleur algorithme pour résoudre un problème donné.

## Complexité d'un problème

Cette notion est centrale en algorithmie, nous l'avons déjà abordé en creux et nous en reparlerons encore tout au log du cours.

{% aller %}
[Définitions](./définitions)
{% endaller %}

## Deux Exemples

On va illustrer la recherche de la complexité d'un problème via deux exemples paradigmatiques à connaître.

### Problèmes de l'exponentiation

{% aller %}
[Problème de l'exponentiation](./exponentiation)
{% endaller %}

### Problème du tri

{% aller %}
[Problème du tri](./tris)
{% endaller %}

## On s'entraîne

> TBD