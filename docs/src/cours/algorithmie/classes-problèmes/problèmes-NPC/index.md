---
layout: layout/post.njk
title: "Problèmes NP complets"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD 

## Réduction de problème

### Définitions

A ≤ B si on peut passer de A à B pour poser le problème puis passer d'une solution de B à A, le tout efficacement (polynomialement).

Ceci permet de résoudre A en utilisant un algorithme permettant de résoudre B.

Prenons un exemple un peu idiot mais qui permettra de se fixer les idées

> TBD max tableau ≤ sort
> TBD recherche doublon et tri (trié = O(n) et sans tri O(n2))
> TBD <https://courses.engr.illinois.edu/cs473/fa2011/lec/21_notes.pdf>
<https://en.wikipedia.org/wiki/Polynomial-time_reduction>
<https://www.youtube.com/watch?v=eHZifpgyH_4>

### Problèmes de décision

> pas de solution. A priori plus simple

## Bornes ?

> TBD : existe-t-il des éléments maximaux ? 
> TBD : existe-t-il une borne sup ? 

oui, c'est les problèmes NP complet.

NP-difficile c'est les éléments maximaux pour les décidables.

1. réduction de problèmes : faire un ou deux exemples simples
2. le cas du problème SAT : très général.
3. 3-SAT ≥ SAT et 3-SAT ≤ SAT et c'est le cas de plein d'autres problèmes
4. tous les problèmes sont plus simple que SAT : c'est le problème le plus dur de NP. 
5. la classe NPC des problèmes universels, sans structure.

<https://www.cs.princeton.edu/courses/archive/fall05/cos226/lectures/reductions.pdf>
