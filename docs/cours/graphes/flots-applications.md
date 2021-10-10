---
layout: page
title:  "Théorie des graphes : flots"
category: cours
tags: informatique graphes
author: "François Brucker"
---

> [graphes]({% link cours/graphes/index.md %}) / [flots : applications]({% link cours/graphes/flots-applications.md %})
{: .chemin}

Quelques exercices pour montrer que le problème du flot maximum permet de modéliser (et résoudre !) de nombreux problèmes concrets, très éloignées de la tuyauterie.

## application simple

On commence par voir si on se rappelle le cours. On considère le réseau suivant (en gras les capacités, en italique les flux) :



### graphe d'écart

Tracer le graphe d'écart associé à ce réseau

### résolution

cherchez à améliorer le flot, puis vérifier qu'il est maximum (ou augmentez le encore) avec l'algorithme de Ford et Fulkerson.

## problème du transport de marchandise

Un problème de transport est une variation sur les flots.

On considère que l'on a un graphe orienté $G = (V, E)$ et que l'on a dans ce graphe deux sous ensembles :

* un ensemble $S \subsetneq V$ de sources qui ont une marchandise en excès
* un ensemble $P \subsetneq V$ de puits qui demandent la marchandises

Les sommets qui ne sont ni dans $S$ ni dans $P$ sont dit sommets intermédiaires.

On a de plus une valuation $v(u)$ pour chaque arc de $G$ qui dertermine le cout de transport d'une unité sur cet arc.

Le problème est alors de tranporter les ressources des sommets de $S$ au sommet de $P$ à coût minimum.

### algorithme

On peut modéliser ce problème comme un problème de flox maximum à cout minimum.

### exemple

## problème du transport amoureux

## stockage dans les noeuds

## k-connectivité dans un graphe

## bataille de la marne
