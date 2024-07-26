---
layout: layout/post.njk 
title:  "Problème SAT"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons intensivement utiliser la réduction pour classer les problèmes algorithmiques, et en particulier les réduction depuis [le problème SAT](https://fr.wikipedia.org/wiki/Probl%C3%A8me_SAT).

Nous avons entraperçu le problème lorsque nous avons parlé de [pseudo-assembleur](../exécuter-code/pseudo-assembleur#clauses) et que tout les fonctions de $\\{0, 1\\}^n$ dans $\\{0, 1\\}$ peuvent s'écrire comme conjonction de clauses :

{% note "**Définition**" %}

```text
nom: SAT
entrée : f une conjonction de clauses sur les variables x[1] à x[n]
Question: existe-t-il une assignation de x[1] à x[n] tel que f soit égale à 1 ?
```

{% endnote %}

Le problème `SAT` cherche à savoir s'il existe des valeurs pour lesquelles $f$ est vraie.

> TBD exemple sudoku.

> TBD subsetsum 3-sat : <https://ics.uci.edu/~goodrich/teach/cs162/notes/pnp3.pdf>
> 
## TBD

> en faire des exos.

> TBD "gadget" pour la transformation
> exemples.

selon ce que l'on cherche à faire.
passer d'un problème à un autre pour le résoudre.

> parler de 2-sat ≤ 3-sat = k-sat = sat
résoudre 2-sat.

> TBD
>
> TBD : Dire, mais laisser la démo pour plus tard, que SAT est supérieur à tout et donner exemple de réduction ≤ SAT et aussi ≥ SAT mais pas le sac à dos.

> exemple réduction :
>
> résolution 3-sat par backtracking
> tbd support cours s1 mpci 