---
layout: layout/post.njk

title: Plusieurs Core

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Pendant longtemps les processeurs n'avaient qu'un core (les deux termes étaient même synonyme), l'intérêt d'avoir plusieurs cores est que plusieurs process peuvent être exécutés en parallèle, chacun sur son core.

Pour que tout ceci se passe au mieux, il faut faire attention à la mémoire qui elle est partagée par tous les cores. Il ne faut en effet pas qu'un core modifie la mémoire utilisée par un autre core. 

> TBD : L3 slice et propagation