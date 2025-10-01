---
layout: layout/post.njk

title: Coloration des arêtes d'un graphe

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
<https://fr.wikipedia.org/wiki/Coloration_des_ar%C3%AAtes_d'un_graphe>
{% endlien %}

La coloration des arêtes est un sujet moins populaire que la coloration des sommets en partie parce que l'on peut résoudre le problème via [le line-graph](https://fr.wikipedia.org/wiki/Line_graph)

{% note "**Définition**" %}
Si $G=(V, E)$ est un graphe, son **_line graph_** $L(G) = (V_L, E_L)$ est défini tel que :

- $V_L = E$
- $uv \in E_L$ si les arêtes $u$ et $v$ ont une extrémité en commun

{% endnote %}

On a alors immédiatement la proposition suivante :

{% note "**Proposition**" %}

Pour tout graphe $G=(V, E)$ on a :

<div>
$$
\chi'(G) = \chi(L(G))
$$
</div>

{% endnote %}

> TBD exemple.

Cette relation permet d'utiliser les résultats de la coloration des sommets pour la colorations des arêtes, en particulier le théorème de Brook qui donne la borne :

{% note "**Proposition**" %}

Pour tout graphe $G=(V, E)$ on a :

<div>
$$
\chi'(G) \leq 2\cdot \Delta(G) -1
$$
</div>

{% endnote %}

{% details "preuve", "open" %}

On a clairement que $\Delta(G) = 2\cdot (\Delta(L(G)) - 1)$ et donc en utilisant le théorème de Brook dans sa forme allégé puisque $G$ peut-être un cycle impair, on a que $\chi(L(G)) \leq \Delta(L(G)) + 1$ ce qui conclut la preuve.
{% enddetails %}

Cependant :

- utiliser le line graph grossit fortement la taille du graphe (il  a de l'ordre du carré du nombre de sommet) ce qui agrandit très fortement le temps de calcul
- la coloration des arêtes possède des propriétés propres intéressante comme on va tenter de le voir
- on peut utiliser la coloration des arêtes pour aider à la coloration des sommets.

Déjà, on peut trouver de biens meilleurs borne !

## Bornes la colorabilité des arêtes

{% lien %}
[Vizing's Theorem](https://www.youtube.com/watch?v=OZWZpQmGp0g)
{% endlien %}

Contrairement à la coloration des sommets, il y a tres peu de choix pour le nombre de couleurs possibles pour colorer des arêtes :

{% note "**Proposition (Vizing, 1964)**" %}
Pour tout graphe $G$ on a :

<div>
$$
\Delta(G) \leq \chi'(G) \leq \Delta(G) +1
$$
</div>
{% endnote %}
{% details "preuve", "open" %}

Le théorème va se prouver en utilisant [des chaînes de Kempe](https://en.wikipedia.org/wiki/Kempe_chain) appliquées à la coloration d'arêtes.

On suppose que $G$ admet une coloration de ses arêtes $f$ et on note $F(u) = \\{f(ux) \vert x \in V, ux \in E \\}$. Une chaîne de Kempe est une suite $uv_0, \dots, uv_k$ de $k+1$ arêtes de $G$ telle que la couleur $c_i = f(uv_{i+1})$ n'est pas dans $F(v_i)$ pour tout $0 \leq i <k$

Pour toute chaîne de Kempe, il est clair que l'on peut remplacer les couleurs de $uv_{i}$ par $c_i$. Enfin, s'il existe $c$ une couleur qui n'est ni dans $F(u)$ ni dans $F(v_k)$ on peut également changer la couleur de $uv_k$ en $c$.

On va construire une coloration des arêtes de $G$ en $\Delta(G) + 1$ couleurs en commençant par le graphe discret et ajoutant une arête à la fois. Supposons que l'on ait une coloration d'un graphe partiel $G'$ de $G$ en $\Delta(G) + 1$ couleurs et on ajoute l'arête $uv_0$. Comme on a à notre disposition $\Delta(G) + 1$ couleurs, il existe forcément une couleur qui n'est pas dans
$F(u)$ et une couleur qui n'est pas dans $F(v_0)$ ce qui permet d'initialiser une chaîne de Kempe que l'on peut itérativement faire grossir construire (la couleur $c_i = f(uv_{i+1})$ n'est pas dans $F(v_i)$ pour tout $0 \leq i <k$) jusqu'à :

- soit arriver à un point où il existe $c$ une couleur qui n'est ni dans $F(u)$ ni dans $F(v_k)$ et l'on peut colorier l'arête $uv_0$ en utilisant la propriété des chaînes de Kempe
- soit arriver à un point où toutes les couleurs qui ne sont pas dans $F(v_k)$ ont déjà été utilisées.

Dans ce deuxième cas, soit $c_k$ une des couleurs qui n'est pas dans $F(v_k)$ et $l$ le plus petit indice tel que $f(uv_l) = c_k$. On peut maintenant construire une autre chaîne $w_0\dots w_p$ telle que $w_0 = u$, $w_1 = v_l$ et telle que si $f(w_iw_{i+1}) = c_k$, alors $f(w_{i+1}w_{i+2}) = c_0$. Cette chaîne ne peut revenir sur ces pas : on va arriver à un moment où la chaîne ne peut être prolongée.

On peut alors :

1. changer les couleurs de la chaîne $uv_0, \dots, uv_l$
2. échanger les couleurs sur la chaîne $w_0\dots w_p$

Ce qui donne une coloration en $\Delta(G) + 1$ couleurs de $G'$ auquel on a ajouté l'arête $uv_0$.

> TBD rendre la preuve plus clair avec des dessins

{% enddetails %}

> TBD <http://o.togni.u-bourgogne.fr/CMGraphesCh3.pdf> p21 : exemple de graphes type 1 et type 2.

> TBD Notez que la preuve donne un algo pour edge colorier avec delta+1 couleurs. Ce qui donne une super approximation si on est pas à une couleur prêt.
> 
> TBD le faire

## Exemple

Pour certains graphes, comme les graphes bi-partis, connaît l'index chromatique.

{% note "**Théorème (König)**" %}
Si $G$ est un graphe biparti, alors  $\chi'(G) = \Delta(G)$
{% endnote %}
{% details "preuve", "open" %}

> TBD p119 diestel. ou preuve avec suite de kempe pour amener vizing ? <https://www.labri.fr/perso/mbonamy/917U/3-Edge-Colouring.pdf>

{% enddetails  %}


> TBD Graphes réguliers avec un nombre impair de sommet sont de classe 2.

En revanche, dans le cas général connaître l'index chromatique est un problème NP-complet

## NP-complétude du problème

> TBD NP-complet. exercice 8.16 de <https://www-sop.inria.fr/members/Frederic.Havet/Cours/coloration.pdf>
> TBD preuve. si le graphe est de classe 1 ou 2.<https://www.lirmm.fr/~bessy/GraphesStructM1/DM3/Papers/LevenGalil.pdf>.

> TBD la NP-complétude se niche donc uniquement sur les graphes 3-réguliers avec un nombre pair de sommets

De plus, la plupart des graphes sont de type 1

> TBD Erdos. Voir si la preuve est faisable.
> - un graphe est presque sûrement de type 1 <https://www.renyi.hu/~p_erdos/1977-20.pdf> (voir <https://en.wikipedia.org/wiki/Vizing%27s_theorem>)

> TBD c'est une illustration de ce qu'est NP-complet. Presque tout le temps facile, sauf quelques exemples qui sont inextricables.

## Liens

> TBD à mettre dans le cours

> contraire : partie 4 : <https://www.labri.fr/perso/mbonamy/917U/3-Edge-Colouring.pdf>