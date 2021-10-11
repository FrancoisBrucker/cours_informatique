---
layout: page
title:  "Théorie des graphes : flots - applications"
category: cours
tags: informatique graphes
author: "François Brucker"
---

> [graphes]({% link cours/graphes/index.md %}) / [flots : applications]({% link cours/graphes/flots-applications.md %})
{: .chemin}

Quelques exercices pour montrer que le problème du flot maximum permet de modéliser (et résoudre !) de nombreux problèmes concrets, très éloignées de la tuyauterie.

[éléments de corrigé]({% link cours/graphes/flots-applications-corrige.md %})

## application simple

On commence par voir si on se rappelle le cours. On considère le réseau suivant (en gras les capacités, en italique les flux) :

![flot application]({{ "/assets/cours/graphes/flot-app-1.png" | relative_url }}){:style="margin: auto;display: block;"}

### graphe d'écart

> Tracer le graphe d'écart associé à ce réseau.
{: .a-faire}

### résolution

> Cherchez à améliorer le flot avec une chaine augmentante en utilisant le graphe d'écart, puis  augmentez le jusqu'à son maximum avec l'algorithme de Ford et Fulkerson en exhibant une coupe minimum.
{:.a-faire}

## problème du transport de marchandise

Un problème de transport est une variation sur les flots.

On considère que l'on a un graphe orienté $G = (V, E)$ et que l'on a dans ce graphe deux sous ensembles :

* un ensemble $S \subsetneq V$ de sources qui ont une marchandise en excès
* un ensemble $P \subsetneq V$ de puits qui demandent la marchandises

Les sommets qui ne sont ni dans $S$ ni dans $P$ sont dit sommets intermédiaires.

On a de plus une valuation $v(u)$ pour chaque arc de $G$ qui détermine le coût de transport d'une unité sur cet arc.

Le problème est alors de transporter les ressources des sommets de $S$ au sommet de $P$ à coût minimum.

> Montrer que l'on peut modéliser ce problème comme un problème de flot maximum à coût minimum.
{: .a-faire}

Le graphe suivant est un problème de transport :

![flot application]({{ "/assets/cours/graphes/flot-app-5.png" | relative_url }}){:style="margin: auto;display: block;"}

Le coût de transport est sur les arcs et les demandes (nombres négatifs)/excès (nombres positifs) de marchandises sont en gras à côté des noeuds.

> Résoudre le problème de transport du graphe précédent.
{:.a-faire}

## problème du transport amoureux

Des héros littéraires ont décidé de se marier. On considère pour simplifier qu'ils sont tous hétérosexuels et qu'ils ont préétablis une matrice d'affinité : un cœur dans la case signifie que la ligne et la colonne sont intéressées l'une par l'autre.

|         |Cléopâtre|Iphigénie|Juliette|Fanny|Chimène|
|  :--:   |  :--:   |  :--:   |  :--:  |:--: | :--:  |
|---------|---------|---------|--------|-----|-------|
|Achille  |     ♥   |    ♥    |        |     |       |
|César    |     ♥   |         |        |  ♥  |       |
|Rodrigue |         |         |    ♥   |     |   ♥   |
|Roméo    |         |         |    ♥   |     |   ♥   |
|Marius   |         |         |    ♥   |  ♥  |       |

>Montrez que ce problème peut s'écrire comme un problème de couplage maximum dans un graphe
{: .a-faire}

Pour un graphe simple $G = (V, E)$ un couplage $M$ est un un ensemble d'arêtes deux à deux disjointes (pour tout sommet $x$, il existe au plus 1 arête de $M$ tel que $x$ soit une de ses extrémités).

> Montrer que comme ce graphe est bi-parti, on peut modéliser le problème de couplage comme un problème de flot maximum.
{: .a-faire}

Un graphe simple $G = (V, E)$ est biparti s'il existe $V_1$ et $V_2$ tels que $V = V_1 \cup V_2$, $V_1 \cap V_2 = \emptyset$ et tel que toute arête de $E$ a une extrémité dans $V_1$ et l'autre dans $V_2$.

>Une fois le problème modélisé. Résolvez le.
> Il existe deux solutions où tout le monde est marié à la fin. Lesquelles ?
{: .a-faire}

## stockage dans les noeuds

Quatre industries $x_1$, $x_2$, $x_3$ et $x_4$ rejetant des eaux
polluées doivent faire traiter ces eaux à la même station d'épuration
$x_5$.

Elles peuvent utiliser le réseau de canalisations du graphe ci-dessous :

![flot épuration]({{ "/assets/cours/graphes/flot-app-stock-1.png" | relative_url }}){:style="margin: auto;display: block;"}

Les capacités des canalisations sont données par les nombres (exprimés
en dizaines de m$^3$ par seconde) associés aux arcs du graphe. D'autre
part, les eaux rejetées des centres $x_1$, $x_2$ et $x_4$ sont
réceptionnées initialement dans des bassins de capacités finies
respectivement égales à 4, 3 et 4 dizaines de m$^3$ par seconde. Le
bassin de réception des eaux rejetées du centre $x_3$ est très grand
et peut pratiquement être considéré de capacité infinie.

>Déterminer un plan d'épuration des eaux polluées de volume (par unité
de temps) maximal.
{: .a-faire}

Des problèmes techniques vont rendre inutilisable une partie $\lambda$
de la capacité (initialement égale à 4) du bassin de réception des
eaux rejetées par le centre $x_1$.

> Quelles seront les conséquences sur
le plan d'épuration optimal ?
{: .a-faire}

## k-connectivité dans un graphe

Nous allons démontrer ici un des [théorème de Menger](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Menger) sur les connectivité d'un graphe.

On veut répondre à la question suivante : Soient deux sommets $s$ et$p$  d'un graphe orienté $G(V, E)$ et 2. Combien de chemins deux à deux disjoints relient $s$ et $p$ ?

On note :

* $P(s, p)$ le nombre de chemins deux à deux disjoints entre $s$ et $p$ dans $G$
* $N(s, p)$ le nombre d'arc qu'il faut supprimer dans $G$ pour qu'il n'existe plus de chemins entre $s$ et $p$

> Montrez que $P(s, p) \leq N(s, p)$
{: .a-faire}

On considère le réseau formé de $G$, de la source $s$ et du puis $p$ et dont toutes les capacités valent $1$.

> Montrez que $\mbox{val}(f) \leq P(s, p)$.
{: .a-faire}

En utilisant une coupe min du flot max :

> Montrez que $N(s, p) \leq \mbox{val}(f)$
{: .a-faire}

En déduire que :

> $P(s, p) = N(s, p) = \mbox{val}(f)$
{: .a-faire}

On peut maintenant chercher à trouver la forte arc-connectivité de $G$, c'est à dire le nombre minimum d'arcs à supprimer de $G$ pour le rendre non fortement connexe (il existe alors deux sommet $a$ et $b$ tel qu'il n'existe pas de chemin entre $a$ et $b$).

> Proposez un algorithme (naïf) basé sur le résultat précédent pour connaître $k$ pour un graphe donné
{: .a-faire}

On peut aller plus rapidement en prouvant le *lemme de zorn* : En supposant une numérotation de $0$ à $n-1$ de $V$ ($V = \\{x_0, \dots, x_{n-1}\\}$), la forte arc-connectivité de $G$ est le minimum de $N(x_i, x_{i+1})$ lorsque $i$ varie de $0$ à $n-1$ et avec $x_n = x_0$.

> Démontrer par l'absurde le lemme de Zorn.
{: .a-faire}

Lorsque le graphe $G = (V, E)$ est non orienté, on considère le graphe orienté $G^\star = (V, E')$ avec $xy$ et $yx$ comme arcs de $G'$ si $xy$ est une arête de $G$.
On assigne de plus une capacité de 1 à tous les arcs de $G^\star$ et on note $f$ un de ses flot maximum.

En notant :

* $P(s, p)$ le nombre de chemins deux à deux disjoints entre $s$ et $p$ dans $G$
* $N(s, p)$ le nombre d'arêtes qu'il faut supprimer dans $G$ pour qu'il n'existe plus de chemins entre $s$ et $p$
* $P^\star(s, p)$ le nombre de chemins deux à deux disjoints entre $s$ et $p$ dans $G^\star$
* $N^\star(s, p)$ le nombre d'arc qu'il faut supprimer dans $G^\star$ pour qu'il n'existe plus de chemins entre $s$ et $p$

> Montrez que : $N(s, P) = N^\star(s, P) = P(s, p) = P^\star(s, p) = \mbox{val}(f)$
{: .a-faire}

On considère le graphe ci-après :

![flot menger]({{ "/assets/cours/graphes/flot-menger-2.png" | relative_url }}){:style="margin: auto;display: block;"}

> Quel est son arc connectivité ?
{: .a-faire}

## bataille de la marne

Un dernier exemple de modélisation en utilisant les flots. Attention c'est du lourd puisque l'on va optimiser l'arrivée des [taxis à la bataille de la marne de 1914](https://fr.wikipedia.org/wiki/Taxis_de_la_Marne).

On a un ensemble $S$ de villes, et des routes reliant certaines villes entre elles (il peut exister plusieurs routes entre deux villes).

* chaque ville $i$ est caractérisée par un nombre $p_i$ de places de parking,
* chaque route $j$ est caractérisée par une longueur $l_j$ (le temps pour aller d’une extrémité à l’autre)
* chaque route $j$ a une capacité $c_j$ (nombre de véhicules qui peuvent l’emprunter par unité de temps)

Au temps $t = 0$, on a un certain nombre de véhicules stationnés dans différentes villes et il faut qu’au temps $t = K$, le plus possible de véhicules soient arrivés à une ville donnée (la Marne).

Il est possible que des véhicules arrivent avant cette date butoir, mais après la date K, c’est
trop tard.

> Modéliser ce problème par un flot maximum dans un graphe que l’on déterminera.
{: .a-faire}