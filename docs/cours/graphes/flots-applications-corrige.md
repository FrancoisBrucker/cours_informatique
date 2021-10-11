---
layout: page
title:  "Théorie des graphes : flots - appication (corrigé)"
category: cours
tags: informatique graphes
author: "François Brucker"
---

> [graphes]({% link cours/graphes/index.md %}) / [flots : applications]({% link cours/graphes/flots-applications.md %})
{: .chemin}

Element de corrigé des applications des flots.

[les exercices]({% link cours/graphes/flots-applications.md %})

## application simple

### graphe d'écart

Le graphe d'écart associé à ce réseau :

![flot application]({{ "/assets/cours/graphes/flot-app-2.png" | relative_url }}){:style="margin: auto;display: block;"}

### résolution

Une chaine augmentante et l'augmentation de flot associée dans la foulée :

![flot application]({{ "/assets/cours/graphes/flot-app-3.png" | relative_url }}){:style="margin: auto;display: block;"}

La coupe min :

![flot application]({{ "/assets/cours/graphes/flot-app-4.png" | relative_url }}){:style="margin: auto;display: block;"}

## problème du transport de marchandise

On considère que l'on a un graphe orienté $G = (V, E)$ et que l'on a dans ce graphe deux sous ensembles :

* un ensemble $S \subsetneq V$ de sources qui ont une marchandise en excès
* un ensemble $P \subsetneq V$ de puits qui demandent la marchandises

Les sommets qui ne sont ni dans $S$ ni dans $P$ sont dit sommets intermédiaires.

On a de plus une valuation $v(u)$ pour chaque arc de $G$ qui détermine le coût de transport d'une unité sur cet arc.

Le problème est alors de transporter les ressources des sommets de $S$ au sommet de $P$ à coût minimum.

On ajoute au graphe :

* un sommet $s$ et des arcs $sx$ pour $x \in S$ de coût 0 et de capacité l'excédent en $x$
* un sommet $p$ et des arcs $xp$ pour $x \in P$ de coût 0 et de capacité la demande en $x$

On considère que les capacités des autres arcs du graphe sont égales à $+\infty$.

Le problème du transport de marchandise revient à trouver le flot maximum à coût minimum.

Le graphe exemple transformé en problème de flot est :

![flot transport]({{ "/assets/cours/graphes/flot-app-6.png" | relative_url }}){:style="margin: auto;display: block;"}

Les capacités sont en gras (les arcs sans capacités sont considérés comme étant de capacité infini) et les coûts sont sur les arcs (les arcs sans coûts sont considérés comme étant de coût nul).

Le graphe d'écart pondéré est alors :


## problème du transport amoureux

## stockage dans les noeuds

## k-connectivité dans un graphe

## bataille de la marne
