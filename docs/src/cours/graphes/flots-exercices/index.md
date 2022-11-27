---
layout: layout/post.njk
title: "Flots : exercices"

authors: 
    - François Brucker

eleventyNavigation:
  key: "Flots : exercices"
  parent: "Graphes"
---

<!-- début résumé -->

Une série d'exercices pour s'entraîner à la modélisation par les flots.

<!-- end résumé -->

## Application directe du cours

On commence par voir si on se rappelle le cours. On considère le réseau suivant (en gras les capacités, en italique les flux) :

![flot application](flot-app-1.png)

### Graphe d'écart

{% exercice %}
Tracer le graphe d'écart associé à ce réseau.
{% endexercice %}
{% details "solution" %}
![flot application](flot-app-2.png)

Les arcs plein sont les arcs directs, les arcs en pointillés, les arcs retours.
{% enddetails %}

### Résolution

{% exercice %}
Cherchez à améliorer le flot avec une chaîne augmentante en utilisant le graphe d'écart, puis  augmentez le jusqu'à son maximum avec l'algorithme de Ford et Fulkerson en exhibant une coupe minimum.
{% endexercice %}
{% details "solution" %}
Une chaîne augmentante et l'augmentation de flot associée dans la foulée :

![flot application](flot-app-3.png)

La coupe min :

![flot application](flot-app-4.png)
{% enddetails %}

## Problème du transport de marchandise

Un problème de transport est une variation sur les flots.

On considère que l'on a un graphe orienté $G = (V, E)$ et que l'on a dans ce graphe deux sous ensembles :

* un ensemble $S \subsetneq V$ de sources qui ont une marchandise en excès
* un ensemble $P \subsetneq V$ de puits qui demandent cette marchandise

Les sommets qui ne sont ni dans $S$ ni dans $P$ sont dit sommets intermédiaires.

On a de plus une valuation $v(u)$ pour chaque arc de $G$ qui détermine le coût de transport d'une unité sur cet arc.

Le problème est alors de transporter les ressources des sommets de $S$ aux sommets de $P$ à coût minimum.

{% exercice %}
Montrer que l'on peut modéliser ce problème comme un problème de flot maximum à coût minimum.
{% endexercice %}
{% details "solution" %}
On ajoute au graphe :

* un sommet $s$ et des arcs $sx$ pour $x \in S$ de coût 0 et de capacité l'excédent en $x$
* un sommet $p$ et des arcs $xp$ pour $x \in P$ de coût 0 et de capacité la demande en $x$

On considère que les capacités des autres arcs du graphe sont égales à $+\infty$.

Le problème du transport de marchandise revient à trouver le flot maximum à coût minimum.
{% enddetails %}

Le graphe suivant est un problème de transport :

![flot application](flot-app-5.png)

Le coût de transport est sur les arcs et les demandes (nombres négatifs)/excès (nombres positifs) de marchandises sont en gras à côté des nœuds.

{% exercice %}
Résoudre le problème de transport du graphe précédent.
{% endexercice %}
{% details "solution" %}
Le graphe exemple transformé en problème de flot est :

![flot transport](flot-app-6.png)

Les capacités sont en gras (les arcs sans capacités sont considérés comme étant de capacité infini) et les coûts sont sur les arcs (les arcs sans coûts sont considérés comme étant de coût nul).

On peut redessiner le réseau sous cette forme :

![flot transport graphe d'écart](flot-app-transport-1.png)

Le flot étant nul au départ, le graphe d'écart pondéré est égal à :

![flot transport graphe d'écart](flot-app-transport-2.png)

Un chemin de poids min entre $s$ et $p$ pourra alors être : $scap$ de poids 0 et qui permet d'augmenter le flot de 2 :

![flot transport augmentation 1](flot-app-transport-3.png)

On a de là le graphe d'écart :

![flot transport augmentation 1](flot-app-transport-4.png)

Un chemin de poids min entre $s$ et $p$ pourra alors être : $sebp$ de poids 2 et qui permet d'augmenter le flot de 1 :

![flot transport flot max](flot-app-transport-5.png)

Le flot est maximum, l'algorithme de Ford et Fulkerson nous donnant une coupe min valant 3 :

![flot transport coupe min](flot-app-transport-6.png)
{% enddetails %}

## Problème du transport amoureux

Des héros littéraires ont décidé de se marier. On considère pour simplifier qu'ils sont tous hétérosexuels et qu'ils ont préétablis une matrice d'affinité : un cœur dans la case signifie que la ligne et la colonne sont intéressées l'une par l'autre.

|         |Cléopâtre|Iphigénie|Juliette|Fanny|Chimène|
|  :-:    |   :-:   |   :-:   |   :-:  |:-:  |  :-:  |
|Achille  |     ♥   |    ♥    |        |     |       |
|César    |     ♥   |         |        |  ♥  |       |
|Rodrigue |         |         |    ♥   |     |   ♥   |
|Roméo    |         |         |    ♥   |     |   ♥   |
|Marius   |         |         |    ♥   |  ♥  |       |

Pour un graphe simple $G = (V, E)$ un couplage $M$ est un un ensemble d'arêtes deux à deux disjointes (pour tout sommet $x$, il existe au plus 1 arête de $M$ telle que $x$ soit une de ses extrémités).

{% exercice %}
Montrez que ce problème peut s'écrire comme un problème de couplage maximum dans un graphe
{% endexercice %}
{% details "solution" %}
On peut écrire le graphe suivant, en liant les affinités par une arête. Le graphe est bi-parti car les mariages sont ici hétérosexuels :

![graphe bi-parti](flot-app-mariage-1.png)

Comme on ne peut marier une personne qu'une seule fois, c'est bien un problème de couplage (l'arête choisie est le mariage).

{% enddetails %}

Un graphe simple $G = (V, E)$ est biparti s'il existe $V_1$ et $V_2$ tels que $V = V_1 \cup V_2$, $V_1 \cap V_2 = \emptyset$ et tel que toute arête de $E$ a une extrémité dans $V_1$ et l'autre dans $V_2$.

{% exercice %}
Montrer que comme ce graphe est bi-parti, on peut modéliser le problème de couplage comme un problème de flot maximum.
{% endexercice %}
{% details "solution" %}
Pour le transformer en problème de flot on peut créer le réseau suivant, avec des capacités de 1 partout :

![graphe bi-parti](flot-app-mariage-2.png)

Cela fonctionne car pour chaque chaîne augmentante, on va la saturer par un entier (donc 1) : on est assuré que le flot maximum sera entier, on ne va pas marier à moitié une personne.
{% enddetails %}

Une fois le problème modélisé, résolvez le.

{% exercice %}
Il existe deux solutions où tout le monde est marié à la fin. Lesquelles ?
{% endexercice %}
{% details "solution" %}
En résolvant le problème on trouve :

* Iphigénie - Achille
* Cléopâtre - César
* Juliette - Rodrigue
* Fanny - Marius
* Chimène - Roméo

Il y a aussi la solution classique où vous échangez les maris de Juliette et Chimène.

{% enddetails %}

Notez que si l'on ne se restreint pas aux mariages hétérosexuels, le graphe n'est plus biparti. Le problème du couplage dans un graphe ne peut plus se résoudre comme un problème de flot, il faut utiliser [l'algorithme d'Edmonds](https://fr.wikipedia.org/wiki/Algorithme_d%27Edmonds_pour_les_couplages) pour le résoudre.

{% info %}
Si l'on veut rajouter des amants (chaque personne peut avoir un conjoint et/ou un amant), le problème devient NP-difficile.
{% endinfo %}

Ce problème est un exemple pratique du fait que si les capacités sont entières, le flot sera lui aussi entier.

## $k$-connectivité dans un graphe

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
