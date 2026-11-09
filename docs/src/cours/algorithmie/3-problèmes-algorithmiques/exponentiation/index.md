---
layout: layout/post.njk

title: "Problèmes liés à l'exponentiation"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Calculer l'exponentiation $x^n$ de deux entiers $x$ et $n$ est un problème qui semble simple mathématiquement. Nous allons étudier ce calcul sous l'angle algorithmique et monter qu'on peut en dire bien des choses.

## Problème de l'exponentiation

{% aller %}
1. [Étude algorithmique](./étude-algorithmique)
2. [Projet : implémentation des algorithmes](./implémentation-code)
{% endaller %}

## Suites additives

{% aller %}
[Les suites additives](./projet-suite-additive)
{% endaller %}