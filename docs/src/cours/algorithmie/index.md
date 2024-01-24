---
layout: layout/post.njk

title: Algorithmie
tags: ['cours', 'algorithmie']
authors:
    - François Brucker

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Cours d'algorithmie.

{% info %}
*L'informatique n'est pas plus la science des ordinateurs que l'astronomie n'est celle des télescopes* [E. Dijkstra](https://fr.wikipedia.org/wiki/Edsger_Dijkstra)
{% endinfo %}

Il est conseillé pour ce cours d'avoir des bases de programmation en python. Pour apprendre vous pouvez vous reporter au cours [coder et développer](/cours/coder-et-développer).

## Algorithmes et programmes

### <span id="bases-théoriques"></span>Bases théoriques

{% aller %}
[Bases théoriques](./bases-théoriques){.interne}
{% endaller %}

### <span id="écrire-algorithmes"></span>Écrire des algorithmes pour résoudre des problèmes

{% aller %}
[Écrire des algorithmes](./écrire-algorithmes){.interne}
{% endaller %}

### Machines de Turing

Cette partie est là pour vous montrer que pseudo-code et machines de Turing sont deux notions équivalentes. On aura également besoin des machines de Turing bien plus tard, lorsque nous rencontrerons les classes de problèmes.

{% aller %}
[Machines de Turing](./machine-turing){.interne}
{% endaller %}

## Complexités

{% aller %}
[Calcul de complexité d'un algorithme](./calcul-complexités){.interne}
{% endaller %}
{% aller %}
[Complexité d'un problème algorithmique](./problème-complexités){.interne}
{% endaller %}

## On s'entraîne : problèmes liés à l'exponentiation

{% aller %}
[Calculer $x^y$](./projet-exponentiation){.interne}
{% endaller %}
{% aller %}
[Les suites additives](./projet-suite-additive){.interne}
{% endaller %}

## On s'entraîne : problèmes de tris

- ordre et désordre

## Classes de Problèmes Algorithmiques

> TBD on a vu avec exponentiation que l'on ne sait pas à priori la meilleurs complexité d'un algorithme résolvant un problème.
> TBD définition de problème, complexité et classes de problèmes.
> TBD : problème de décision, si structure finie on fait tous les cas et hop on a le résultat... Mais en beaucoup de temps
