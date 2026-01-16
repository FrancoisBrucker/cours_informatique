---
layout: layout/post.njk
title: Design d'algorithmes

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD donner des exemples du discours de la méthode (cf. poly PP)
> TBD : diviser pour régner et programmation dynamique c'est la même idée mais on résout différemment. Diviser pour régner on descend et programmation dynamique on remonte (on part du petit et on généralise)

## Diviser pour régner

{% aller %}
[Diviser pour régner](./diviser-régner){.interne}
{% endaller %}

## Programmation dynamique

{% aller %}
[Programmation dynamique](./programmation-dynamique){.interne}
{% endaller %}

## Algorithmes gloutons

{% aller %}
[Algorithmes gloutons](./algorithmes-gloutons){.interne}
{% endaller %}

## Recherche exhaustive

{% aller %}
[Énumération de toutes les solutions](./algorithmes-énumération){.interne}
{% endaller %}

## Programmation par contraintes

> TBD parler d'optimisation combinatoire. Résolution par solveur de SAT. sujet de recherche très fécond
> p47 <https://members.femto-st.fr/pierre-cyrille-heam/sites/femto-st.fr.pierre-cyrille-heam/files/content/Enseignement/cours-satsolveurs.pdf>
> TBD : <https://people.csail.mit.edu/virgi/6.s078/lecture3and4.pdf>

> On ne continue que si ça vaut le coup.
> sudoku : encore possible ?
> programmation linéaire et branch and bound pour contrainte non linéaire typiquement en nombre entier 0/1 pour SAT.
> 
> branch and bound Pour la programmation linéaire.
> <http://sirdeyre.free.fr/Papiers_etc/2007_Sudokus_et_programmation_lineaire_2.pdf>
> TBD brute force et on stope l'énumération si on a déjà mieux

> sudoku sous la forme d'un sat. <https://www.researchgate.net/publication/339822516_Software_Design_Completion_of_Sudoku_Game_with_Branch_and_Bound_Algorithm/fulltext/5e678a05299bf1744f6f1ad4/Software-Design-Completion-of-Sudoku-Game-with-Branch-and-Bound-Algorithm.pdf>
> <https://www.reddit.com/r/optimization/comments/rycl1g/how_to_solve_a_sudoku_puzzle_with_simplex_or/>

> TBD backtracking amélioré : on ne parcourt pas tout l'espace

> branch and bound exemple : <https://www.baeldung.com/cs/branch-and-bound>
> <https://www.youtube.com/watch?v=2zKCQ03JzOY>
> reprendre des choses du sac à dos pour les mettre ici.

branch and bound : <https://www.youtube.com/watch?v=E7hJXsywOdA>

## Méta-heuristiques

> TBD partie approximation et performances garanties

Méthode générale de création d'algorithmes heuristiques sans garantie de performance mais souvent efficace en pratique. Un peu oublié de part la prépondérance des méthodes à base de réseau de neurones, mais peut-être utile si on ne peut pas entraîner un réseau et certaines méthodes sont très efficaces.

> <https://fr.wikipedia.org/wiki/M%C3%A9taheuristique>
> <https://www.techno-science.net/glossaire-definition/Probleme-du-sac-a-dos-page-4.html>
> <https://fr.wikipedia.org/wiki/M%C3%A9taheuristique>

- recuit simulé
- tabou
- algorithme génétiques
- fourmi

> TBD remplir [une grille aléatoire de sudoku](https://www.youtube.com/watch?v=2SuvO4Gi7uY) en utilisant [la réduction de paquet d'onde](https://fr.wikipedia.org/wiki/R%C3%A9duction_du_paquet_d'onde) (si si. Voir [ici](https://robertheaton.com/2018/12/17/wavefunction-collapse-algorithm/) pour une explication et un autre exemple). Attention, parfois cette méthode va rater et il faudra faire du [backtracking](https://fr.wikipedia.org/wiki/Retour_sur_trace).