---
layout: page
title:  "Introduction aux graphes"
category: cours
author: "François Brucker"
---

> [graphes]({% link cours/graphes/index.md %})
{: .chemin}

## Introduction

Ce cours, introductif, à pour but d'exposer quelques définitions, concepts et méthodes de résolution de problèmes propre aux graphes.

Il a pour principal objectif d'allumer la petite flamme de l'intérêt pour cette structure à la fois riche en problèmes intéressants et en solutions élégantes ; à la fois théorique — à l'intersection des mathématiques discrètes et de l'informatique théorique — et au cœur de nombre d'applications de tous les jours.

Le cours va être séparé en petites entités qui se suivent pour former un tout qu'on espère cohérent.

## Plan du cours

### première partie

Où l'on découvre les graphes et l'on résout notre premier problème concret grâce à eux.

1. [bases]({% link cours/graphes/bases.md %}) : principales définitions
2. [encodage de graphes]({% link cours/graphes/encodage.md %}) : comment coder un graphe
3. [parcours eulériens]({% link cours/graphes/parcours-euleriens.md %}) : première application. Et on en profite pour montrer quelques algorithmes et propriétés
4. [mots de Brujin]({% link cours/graphes/mots-brujin.md %}) : on se rend compte qu'on peut modéliser un problème concret sous la forme d'un problème de graphe.

[Et si l'on codait tout ça ?]({% link cours/graphes/circuits-euleriens.md %})

### deuxième partie

Un cas particulier d'intérêt : l'arbre et les chemins.

> Sous la forme d'exercices.

1. [l'arbre]({% link cours/graphes/arbres.md %})
2. [arbres binaires de recherche]({% link cours/graphes/arbre-de-recherche.md %})
3. [chemins et arborescences]({% link cours/graphes/chemins.md %})

> TBD
> combien d'arbre ? Encodage prüfer et application à un arbre aléatoire (!= différent de la structure).
{: .note}

### troisième partie

Problèmes de flots. Définition, algorithmes et applications

1. [problèmes de flots]({% link cours/graphes/flots.md %})
2. [applications]({% link cours/graphes/flots-applications.md %})