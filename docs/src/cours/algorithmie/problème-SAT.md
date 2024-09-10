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

> TBD dire que si on a une solution potentielle alors facile de savoir si vrai solution (donner algo) mais que trouver l'algo on ne sait pas trop à part essayer toutes les solution (donner nb de solutions).

> TBD Résolution basique énumération en $2^n$ vrai/faux pour chaque variable.

## Modélisation

Tout problème se résout via un SAT. Pas toujours facile de s'y ramener, mais parfois c'est bien

### Fonctions booléennes

> TBD clauses et conjonction de clauses. Montrer que toute fonction booléennes sont des conjonctions de clauses.
> polylog circuit et sat : <https://www.youtube.com/watch?v=6OPsH8PK7xM>

### exemple du sudoku

> TBD puissant outil de modélisation. Déjà toutes fonctions mais autres choses.
> exemple sudoku. :
>  - <https://sat.inesc-id.pt/~ines/publications/aimath06.pdf>

## 3-SAT

équivalent à SAT

> TBD <https://cse.iitkgp.ac.in/~palash/2018AlgoDesignAnalysis/SAT-3SAT.pdf>

Permet certaines réductions de façon bien plus facile :

> TBD résolution par backtracking

## 2-SAT

> Réduction ne fonctionne pas. Autre problème
> 
> Algo poly par limited backtracking : <https://en.wikipedia.org/wiki/2-satisfiability#Limited_backtracking>
> limited backatracking car chaque cas est indépendant donc si on doit rbacktracker impossible.

> 2-sat poly : <https://cp-algorithms.com/graph/2SAT.html>


> TBD faire dans la partie graphe : strongly connected component : Tarjan <https://github.com/tpn/pdfs/blob/master/Depth-First%20Search%20and%20Linear%20Graph%20Algorithms%20-%20Tarjan%20(1972).pdf>

## Réductions

> TBD bi-partition SAT : <https://people.orie.cornell.edu/dpw/orie6300/Lectures/lec25.pdf>
> TBD subsetsum 3-SAT : <https://ics.uci.edu/~goodrich/teach/cs162/notes/pnp3.pdf>

## Inversibilité du problème SAT

> revenir en arrière facile : si solution alors on a l'entrée. Les fonctions à sens unique, factorisation, etc.


> 
> TBD
>
> TBD : Dire, mais laisser la démo pour plus tard, que SAT est supérieur à tout et donner exemple de réduction ≤ SAT et aussi ≥ SAT mais pas le sac à dos.

> exemple réduction :
>
> résolution 3-sat par backtracking
>
> TBD <https://courses.engr.illinois.edu/cs473/fa2011/lec/21_notes.pdf>
>
## Résolution de SAT

> TBD : <https://people.csail.mit.edu/virgi/6.s078/lecture3and4.pdf>
