---
layout: layout/post.njk
title: "Connectivité"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Utilisation des flots pour démontrer les résultats de Menger sur la $k$-connectivité d'un graphe

<!-- end résumé -->

> TBD : ajouter dessins et transformer exercice en propositions

Nous allons démontrer ici un des [théorème de Menger](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Menger) sur les connectivité d'un graphe.

On veut répondre à la question suivante : Soient deux sommets $s$ et $p$  d'un graphe orienté $G = (V, E)$, combien de chemins deux à deux disjoints relient $s$ et $p$ ?

On note :

* $P(s, p)$ le nombre de chemins deux à deux disjoints entre $s$ et $p$ dans $G$
* $N(s, p)$ le nombre d'arc qu'il faut supprimer dans $G$ pour qu'il n'existe plus de chemins entre $s$ et $p$

{% exercice %}
Montrez que $P(s, p) \leq N(s, p)$
{% endexercice %}
{% details "solution" %}
Comme les chemins sont disjoints, il faut au moins supprimer $P(s, p)$ arcs pour les déconnecter.
{% enddetails %}

On considère le réseau formé de $G$, de la source $s$ et du puits $p$ et dont toutes les capacités valent $1$.

{% exercice %}
Montrez que $\mbox{val}(f) \leq P(s, p)$.
{% endexercice %}
{% details "solution" %}
Soit $f$ un flot maximum pour le réseau.

Comme les capacités valent toutes 1, chaque flux est soit 0 soit 1. De là tous les arcs sortant de $s$ de flux 1 vont créer des chemins disjoints vers $p$.

{% enddetails %}

En utilisant une coupe min du flot max :

{% exercice %}
Montrez que $N(s, p) \leq \mbox{val}(f)$
{% endexercice %}
{% details "solution" %}
Sur une coupe minimum $(S, \overline{S})$, toutes les arêtes allant de $S$ vers $\overline{S}$ sont à 1 et sont au nombre de $\mbox{val}(f)$. Or si on supprime toutes ces arcs, on déconnecte $s$ de $p$ : $N(s, p) \leq \mbox{val}(f)$.
{% enddetails %}

En déduire que :

{% exercice %}
$P(s, p) = N(s, p) = \mbox{val}(f)$
{% endexercice %}
{% details "solution" %}
On a les 3 inégalités :

* $P(s, p) \leq N(s, p)$
* $\mbox{val}(f) \leq P(s, p)$
* $N(s, p) \leq \mbox{val}(f)$

Donc : $P(s, p) = N(s, p) = \mbox{val}(f)$
{% enddetails %}

On peut maintenant chercher à trouver la forte arc-connectivité de $G$, c'est à dire le nombre minimum d'arcs à supprimer de $G$ pour le rendre non fortement connexe (il existe alors deux sommet $a$ et $b$ tel qu'il n'existe pas de chemin entre $a$ et $b$).

{% exercice %}
Proposez un algorithme (naïf) basé sur le résultat précédent pour connaître $k$ pour un graphe donné
{% endexercice %}
{% details "solution" %}

> TBD

{% enddetails %}

On peut aller plus rapidement en prouvant le *lemme de Zorn* : En supposant une numérotation de $0$ à $n-1$ de $V$ ($V = \\{x_0, \dots, x_{n-1}\\}$), la forte arc-connectivité de $G$ est le minimum de $N(x_i, x_{i+1})$ lorsque $i$ varie de $0$ à $n-1$ et avec $x_n = x_0$.

{% exercice %}
Démontrer par l'absurde le lemme de Zorn.
{% endexercice %}
{% details "solution" %}
On suppose par l'absurde que le minimum de $N(x_i, x_{i+1})$ soit strictement plus grand que la forte arc connectivité de $G$ que l'on note $k$. En supprimant $k$ arcs je déconnecte $x_i$ de $x_j$. On a deux cas :

* si $i < j$ alors comme on peut toujours aller de $x_k$ à $x_{k+1}$ pour tous $i \leq k < j$, il existe un chemin entre $x_i$ et $x_j$ ce qui est impossible.
* si $j < i$ alors comme on peut toujours aller de $x_k$ à $x_{k+1}$ pour tous $j \leq k < n - 1$ il existe un chemin entre $x_i$ et $x_0$, puis un raisonnement identique nous indique qu'on peut aller de $x_0$ à $x_j$. Il existe donc un chemin entre $x_i$ et $x_j$ ce qui est impossible.

Trouver la forte arc connectivité d'un graphe orienté se fait donc en procédant à $\vert V \vert$ calcul de flot maximum.
{% enddetails %}

Lorsque le graphe $G = (V, E)$ est non orienté, on considère le graphe orienté $G^\star = (V, E')$ avec $xy$ et $yx$ comme arcs de $G'$ si $xy$ est une arête de $G$.
On assigne de plus une capacité de 1 à tous les arcs de $G^\star$ et on note $f$ un de ses flot maximum.

En notant :

* $P(s, p)$ le nombre de chemins deux à deux disjoints entre $s$ et $p$ dans $G$
* $N(s, p)$ le nombre d'arêtes qu'il faut supprimer dans $G$ pour qu'il n'existe plus de chemins entre $s$ et $p$
* $P^\star(s, p)$ le nombre de chemins deux à deux disjoints entre $s$ et $p$ dans $G^\star$
* $N^\star(s, p)$ le nombre d'arcs qu'il faut supprimer dans $G^\star$ pour qu'il n'existe plus de chemins entre $s$ et $p$

{% exercice %}
Montrez que : $N(s, P) = N^\star(s, P) = P(s, p) = P^\star(s, p) = \mbox{val}(f)$
{% endexercice %}
{% details "solution" %}

{% enddetails %}

On considère le graphe ci-après :

![flot Menger](flot-menger-2.png)

{% exercice %}
Quel est son arc connectivité ?
{% endexercice %}
{% details "solution" %}
Ce graphe s'appelle le [graphe de Petersen](https://fr.wikipedia.org/wiki/Graphe_de_Petersen)) graphe est 3 et 2 pour le second (il suffit de supprimer les arêtes rouges)
{% enddetails %}

Et lui ?

{% exercice %}
![flot menger](flot-menger-3.png)
{% endexercice %}
{% details "solution" %}
![flot menger](flot-menger-4.png)
{% enddetails %}

On voit de ces exemples que le degré minimum n'est que majorant de l'arc connectivité d'un graphe.

{% exercice %}
Montrez que pour tout graphe : $N(s, P) = N^\star(s, P) = P(s, p) = P^\star(s, p) = \mbox{val}(f)$

{% endexercice %}
{% details "solution" %}

1. On a clairement que $N(s, p) \geq P(s, p)$.
2. $P(s, p) \geq P^\star(s, p)$
    De plus, $P(a, b) \geq P^\star(s, p)$. Si les $P^\star(s, p)$ chemins ne partagent pas d'arcs issus du dédoublement des arêtes en arcs, on peut créer $P^\star(s, p)$ chemins disjoints entre $s$ et $p$ dans $G$.

    Si 2 chemins partagent une arête $xy$ l'un l'$xy$ et l'autre l'arc $yx$, on peut procéder comme dans la figure ci-dessous pour créer 2 chemins partageant strictement moins d'arêtes.

    ![flot Menger](flot-menger-1.png)

    On peut alors itérativement construire $P^\star(s, p)$ chemins ne partageant pas d'arcs issus du dédoublement des arêtes en arcs.
3. $N(s, P) \geq N^\star(s, P)$
    En supprimant $N^\star(s, p)$ arcs de $G^\star$ on déconnecte $s$ de $p$. Si on supprime les arêtes de $G$ qui ont donné naissance à ces arcs, on déconnecte $s$ de $p$ dans $G$. En effet, s'il restait un chemin entre $s$ et $p$ dans $G$, il en resterait également un dans $G^\star$.

    On a donc $N^\star(s, p) \geq N(s, p)$.

On a les inégalités suivantes : $N^\star(s, p) \geq N(s, p) \geq P(s, p) \geq P^\star(s, p)$

Or $P^\star(s, p) = N^\star(s, p) = \mbox{val}(f)$ ce qui conclut la preuve d'égalité.
{% enddetails %}
