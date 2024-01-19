---
layout: layout/post.njk 
title: Calculabilité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On vient de le voir : il y a plus de nombres réels que d'algorithmes. Il existe donc forcément des choses que ne peut pas calculer un algorithme.

Mais avant de voir ce que ne peut pas faire un algorithme, voyons des choses que l'on peut faire avec.

## Algorithmes et fonctions

On a vu qu'un algorithme et tout ce qu'il manipulait pouvait être considéré comme une suite finie de 0 et de 1. On en déduit immédiatement la proposition suivante :

{% note "**Proposition**" %}
Un algorithme est une fonction :

$$f: \\{0, 1\\}^\star \rightarrow \\{0, 1\\}^\star$$

Où $\\{0, 1\\}^\star$ est l'ensemble des suites finies de $0$ et de $1$.
{% endnote %}

Remarquez que ceci fonctionne même si un algorithme possède plusieurs entrées. Il suffit de les écrire sous la forme d'une chaîne de caractère où chaque paramètre est séparé par une virgule par exemple et de transcrire cette chaîne en suite de 0 et de 1.

Comme une suite finie de 0 et de 1 est une écriture binaire d'un entier positif on en déduit immédiatement que :

