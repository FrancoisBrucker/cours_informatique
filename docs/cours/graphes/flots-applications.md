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

>Cherchez à améliorer le flot avec une chaine augmentante, puis  augmentez le jusqu'à son maximum avec l'algorithme de Ford et Fulkerson en exhibant une coupe minimum.
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

## stockage dans les noeuds

## k-connectivité dans un graphe

## bataille de la marne
