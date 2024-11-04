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

> TBD lien sur vertex/edge et planar : <https://www-sop.inria.fr/members/Frederic.Havet/Cours/coloration.pdf>

## Coloration des sommets

Certainement la plus populaires des colorations de graphe.

{% note "**Définition**" %}
Soit $G=(V, E)$ un graphe. Une **_$k$-coloration_** de $G$ est une fonction $c: V \to \\{1,\dots, k\\}$ telle que pour toute arête $xy \in E$, $c(x) \neq c(y)$.
{% endnote %}

> TBD exemples :
>
> - discret
> - arbre
> - cycle pair
> - cycle impair C5
> - clique K6
>

Les exemples précédent le montre, il existe une borne minimum pour tout graphe :

<span id="definition-notation-coloration-minimum"></span>
{% note "**Définition**" %}

Soit $G=(V, E)$ un graphe. On note $\chi(G)$ le nombre minimum de couleurs qu'il faut pour colorier ses sommets et on l'appelle **_nombre chromatique de $G$_**.

{% endnote %}

Entraînons-nous à trouver $\chi$ pour des classes de graphes connus :

{% exercice %}
Montrer que :

- $\chi(G) = 2$ si $G$ est un chemin ou un cycle de longueur pair,
- $\chi(G) = 3$ si $G$ est un chemin ou un cycle de longueur impair,
{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}

{% exercice %}
Montrer que :

- $\chi(K_n) = n$
{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}

Le lecteur attentif aura remarqué que la notion de colorabilité est équivalente à la notion [de graphes $k$-parti](../graphe-biparti/#k-parti){.interne} :

{% note "**Proposition**" %}
Un graphe $G$ est $\chi(G)$-parti si et n'est pas $(\chi(G)-1)$-parti.
{% endnote %}

On en déduit donc immédiatement :

{% note "**Proposition**" %}
Le problème de savoir si un graphe est $k$-colorable, avec $k\geq 3$ est NP-complet.
{% endnote %}
{% details "preuve", "open" %}
Clair puisque c'est exactement [le problème `Rec-3-parti`](../graphe-biparti/#Rec-3-parti-NPC){.interne} qui est NP-complet et que `Rec-k-parti ≤ Rec-(k+1)-parti`
{% enddetails %}

### Coloration et composition de graphes

La coloration de graphe peut se faire _plus ou moins_ par parties en  utilisant la [composition de graphes](../structure/#composition-graphes){.interne} :

{% note "**Proposition**" %}
Pour deux graphes $G_1=(V_1, E_1)$ et $G_2=(V_2, E_2)$ on a :

- $\chi(G_1 + G_2) = \max(\\{\chi(G_1), \chi(G_2) \\})$
- $\chi(G_1 \lor G_2) = \chi(G_1) + \chi(G_2)$
- $\chi(G_1 \square G_2) = \max(\\{\chi(G_1), \chi(G_2) \\})$
{% endnote %}
{% details "preuve", "open" %}
Les deux premières propositions sont triviales.

Pour montrer la troisième, soient $c_1$ et $c_2$ des colorations de $G_1$ et $G_2$ respectivement et on pose $m = \max(\\{\chi(G_1), \chi(G_2) \\})$.

La fonction $c: V_1 \times V_2 \to \\{0, \dots, m-1\\}$ telle que $c((x, y)) = c_1(x) + c_2(y) \mod m$ est une coloration de $G_1 \square G_2$. En effet si $\\{(x_1, y_1), (x_2, y_2)\\}$ est une arête de $G_1 \square G_2$ on a soit :

- $x_1 = y_1$ et $\vert c((x_1, y_1)) - c((x_2, y_2)) \vert = \vert c_2(x_2) - c_2(y_2) \vert > 0$ puisque $x_2y_2$ est une arête de $G_2$
- $x_2 = y_2$ et $\vert c((x_1, y_1)) - c((x_2, y_2)) \vert = \vert c_1(x_1) - c_1(y_1) \vert > 0 $ puisque $x_1y_1$ est une arête de $G_1$

{% enddetails %}

> TBD exemples du cours papier.

### Heuristique gloutonne

{% lien %}
[Algorithme glouton en action](https://www.youtube.com/watch?v=L2csXWQMsNg)
{% endlien %}

> tbd glouton + améliorations en classant par ordre décroissant et en utilisant [dsatur](https://en.wikipedia.org/wiki/DSatur)
>

### Majorations de la colorabilité

tbd permet de déduire des bornes !

> tbd glouton amélioré. Pas fait en pratique car compliqué alors glouton doit être simple.
>
> TBD entre clique et degré. Montrer que pas égal.

### Colorabilité et isomorphisme de graphe

> test heuristique d'isomorphisme de graphe <https://en.wikipedia.org/wiki/Colour_refinement_algorithm> et <https://en.wikipedia.org/wiki/Weisfeiler_Leman_graph_isomorphism_test>

## Coloration des arêtes

{% note "**Définition**" %}
Soit $G=(V, E)$ un graphe. Une **_$k$-coloration des arêtes_** $G$ est une fonction $c: E \to \\{1,\dots, k\\}$ telle que pour triplet de sommets $x \neq y \nea z \in E$ si $xy, xz \in E$ alors $c(xy) \neq c(xz)$.
{% endnote %}

> TBD exemples :
>
> - discret
> - arbre
> - cycle pair
> - cycle impair C5
> - clique K6
>

Les exemples précédent le montre, il existe une borne minimum pour tout graphe :

<span id="definition-notation-coloration-arête-minimum"></span>
{% note "**Définition**" %}

Soit $G=(V, E)$ un graphe. On note $\chi'(G)$ le nombre minimum de couleurs qu'il faut pour colorier ses arêtes et on l'appelle **_nombre chromatique des arêtes de $G$_**.

{% endnote %}

Le lecteur attentif aura remarqué que la notion de colorabilité des arêtes se rapproche de la notion [de couplage](../couplages) : la $k$ colorabilité des arêtes correspond à une partition en couplages de $G$.

> TBD : Pour nous ok. Au moins n-1 et la construction du début fonctionne.

> - cas particulier du Théorème de Baranyai: <https://math.stackexchange.com/questions/1827816/proof-of-baranyais-theorem> et p20 <http://discretemath.imp.fu-berlin.de/DMII-2018-19/connectivity-flows-baranyai.pdf>


> NP-complet. Sketch of proof là : <<https://www.lirmm.fr/~bessy/GraphesStructM1/DM3/Papers/LevenGalil.pdf>>

### Lien avec la colorabilité des sommets

Via le [line graph](https://en.wikipedia.org/wiki/Line_graph).

- line graph edge veterx coloring <=>  edge coloring. Mais tout n'est pas un line graph (demo par comfiguration exclue) <https://www.labri.fr/perso/mbonamy/917U/3-Edge-Colouring.pdf>
> preuve par sous graphe exclus : <https://core.ac.uk/download/pdf/82132835.pdf>
> <https://en.wikipedia.org/wiki/Line_graph>
> on peut peut utiliser l'algo glouton pour résoudre le problème
> TBD : Harary theorem 8.3 unique line graph et thm 1.7.4 de <https://faculty.etsu.edu/gardnerr/5340/notes-Godsil-Royle/Algebraic-GT-GR-1-7.pdf> pour démontrer les graphes interdits.

> TBD line graph exercices : <https://faculty.etsu.edu/gardnerr/5340/notes-Godsil-Royle/Algebraic-GT-GR-1-7.pdf>
>
> - line graph de graphes réguliers sont eulériens lemma 1.7.1
> - line graph d'un graph eulérien est eulérien et hamiltonien
> - <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/96BA451CF0099F38C1B3FA867EC1A835/S0008439500054989a.pdf/div-class-title-on-eulerian-and-hamiltonian-graphs-and-line-graphs-div.pdf>

### Bornes la colorabilité des arêtes

> TBD preuve théorème de Vizings plus d'autres trucs : <https://math.uchicago.edu/~may/REU2015/REUPapers/Green.pdf>

[Vizing's Theorem](https://www.youtube.com/watch?v=OZWZpQmGp0g)

> TBD la preuve donne un algo pour edge colorier avec delta+1 couleurs.

C'est NP-complet de savoir si le graphe est de classe 1 ou 2. On le verra plus tard (graphe aléatoires) qu'un graphe est presque sûrement de type 1.

> TBD c'est une illustration de ce qu'est NP-complet. Presque tout le temps facile, sauf quelques exemples qui sont inextricables.

> TBD exo graphe biparti type 1. TBD preuve générale sur edge coloring.

<https://mathweb.ucsd.edu/~gptesler/154/slides/154_graphcoloring_20-handout.pdf>

> TBD fun fact. Graphes réguliers avec un nombre impair de sommet sont de classe 2.
> TBD la NP-complétude se niche donc uniquement sur les graphes 3-réguliers avec un nombre pair de sommets
