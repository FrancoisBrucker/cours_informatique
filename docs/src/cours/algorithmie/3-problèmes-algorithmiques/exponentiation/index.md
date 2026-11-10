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

## Étude algorithmique

{% aller %}
[Étude algorithmique](./étude-algorithmique)
{% endaller %}

## Implémentation et mesure de complexité

{% aller %}
[Projet : implémentation des algorithmes](./implémentation-code)
{% endaller %}
