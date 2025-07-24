---
layout: layout/post.njk
title: Méthodes par énumération

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


On recherche exhaustivement toutes les solutions puis on prend la meilleur.

> TBD prend du temps.
> 3 variantes selon l'information supplémentaire que l'on se donne pour résoudre. Parfois on ne gagne rien parfois on gagne beaucoup.

> TBD exemple du sudoko : <https://github.com/sandylewat/pydoku>
> <https://en.wikipedia.org/wiki/Sudoku_solving_algorithms>

## Brute Force

> TBD toute les solutions potentielles

## Branch and bound

> On ne continue que si ça vaut le coup.
> sudoku : encore possible ?
> 
> TBD brute force et on stope l'énumération si on a déjà mieux

> TBD backtracking amélioré : on ne parcourt pas tout l'espace

> branch and bound exemple : <https://www.baeldung.com/cs/branch-and-bound>
> <https://www.youtube.com/watch?v=2zKCQ03JzOY>
> reprendre des choses du sac à dos pour les mettre ici.

branch and bound : <https://www.youtube.com/watch?v=E7hJXsywOdA>

## Backtracking

> récursif, on progresse le plus possible et on revient en arrière si un soucis.
> <https://www.geeksforgeeks.org/difference-between-backtracking-and-branch-n-bound-technique/?ref=lbp>
> TBD brute force avec contraintes implicites

{% lien %}
[Méthode du Backtracking](https://fr.wikipedia.org/wiki/Retour_sur_trace)
{% endlien %}
