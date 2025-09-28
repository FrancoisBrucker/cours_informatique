---
layout: layout/post.njk

title: Colorabilité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Il existe deux notion de colorabilité dans les graphes : la coloration de sommets et la coloration d'arêtes. Dans les deux cas, on veut colorier avec deux couleurs différentes des éléments (sommets ou arêtes respectivement) qui se touches (via une arête ou un sommet, respectivement).

Bien que ces deux façons de colorer des graphes soient liées, elles possèdent chacune des propriétés et théorèmes intéressants, nous en verront quelques uns.

Enfin, ces deux types de colorations ont des applications pratiques nombreuses et différentes. Par exemple :

- comment organiser un plan de table ou résoudre un sudoku pour la coloration des sommets (voir par exemple [cette video](https://www.youtube.com/watch?v=y4RAYQjKb5Y))
- comment organiser un tournoi sportif pour la coloration des arêtes (via l'algorithme de [round robin scheduling](https://nrich.maths.org/articles/tournament-scheduling). On verra plus tard que c'est optimal)

{% lien %}

[cours sur la coloration](https://www-sop.inria.fr/members/Frederic.Havet/Cours/coloration.pdf)

{% endlien %}

## Coloration des sommets

{% aller %}
[Coloration des sommets d'un graphe](coloration-sommets){.interne}
{% endaller %}

## Coloration des arêtes

{% aller %}
[Coloration des arêtes d'un graphe](coloration-arêtes){.interne}
{% endaller %}

## Lien entre les deux

> TBD à faire

Via le [line graph](https://en.wikipedia.org/wiki/Line_graph).

> TBD définition line graph
> TBD passage de l'un à l'autre et équivalence du nombre de couleurs. On peut peut utiliser l'algo glouton pour résoudre le problème

> TBD ici juste dire que l'on peut le faire et renvoyer à un DM sur le line graphe. C'est des jolis preuve d'isomorphisme qui fonctionnent.

- line graph edge veterx coloring <=>  edge coloring. Mais tout n'est pas un line graph (demo par comfiguration exclue) <https://www.labri.fr/perso/mbonamy/917U/3-Edge-Colouring.pdf>
> preuve par sous graphe exclus : <https://core.ac.uk/download/pdf/82132835.pdf>
> <https://en.wikipedia.org/wiki/Line_graph>

> TBD : Harary theorem 8.3 unique line graph et thm 1.7.4 de <https://faculty.etsu.edu/gardnerr/5340/notes-Godsil-Royle/Algebraic-GT-GR-1-7.pdf> pour démontrer les graphes interdits.

> TBD line graph exercices : <https://faculty.etsu.edu/gardnerr/5340/notes-Godsil-Royle/Algebraic-GT-GR-1-7.pdf>
>
> - line graph de graphes réguliers sont eulériens lemma 1.7.1
> - line graph d'un graph eulérien est eulérien et hamiltonien
> - <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/96BA451CF0099F38C1B3FA867EC1A835/S0008439500054989a.pdf/div-class-title-on-eulerian-and-hamiltonian-graphs-and-line-graphs-div.pdf>