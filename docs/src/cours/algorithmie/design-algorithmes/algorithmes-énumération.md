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

## Backtracking

> <https://www.geeksforgeeks.org/difference-between-backtracking-and-branch-n-bound-technique/?ref=lbp>
> TBD brute force avec contraintes implicites

{% lien %}
[Méthode du backtrackig](https://fr.wikipedia.org/wiki/Retour_sur_trace)
{% endlien %}

## Branch and bound

> Pour la programmation linéaire.
> <http://sirdeyre.free.fr/Papiers_etc/2007_Sudokus_et_programmation_lineaire_2.pdf>
> TBD brute force et on stope l'énumération si on a déjà mieux

> <https://www.researchgate.net/publication/339822516_Software_Design_Completion_of_Sudoku_Game_with_Branch_and_Bound_Algorithm/fulltext/5e678a05299bf1744f6f1ad4/Software-Design-Completion-of-Sudoku-Game-with-Branch-and-Bound-Algorithm.pdf>
> <https://www.reddit.com/r/optimization/comments/rycl1g/how_to_solve_a_sudoku_puzzle_with_simplex_or/>

> TBD backtracking amélioré : on ne parcourt pas tout l'espace

> branch and bound exemple : <https://www.baeldung.com/cs/branch-and-bound>
> <https://www.youtube.com/watch?v=2zKCQ03JzOY>
> reprendre des choses du sac à dos pour les mettre ici.

branch and bound : <https://www.youtube.com/watch?v=E7hJXsywOdA>
