---
layout: layout/post.njk

title: Problème de l'exponentiation

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Calculer l'exponentiation $x^n$ de deux entiers $x$ et $n$ est un problème qui semble simple mathématiquement. Nous allons étudier ce calcul sous l'angle algorithmique et monter qu'on peut en dire bien des choses.

1. [Étude algorithmique](./étude-algorithmique){.interne}
2. [Implémentation des algorithmes](./implémentation-code){.interne}
