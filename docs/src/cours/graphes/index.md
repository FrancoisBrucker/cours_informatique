---
layout: layout/post.njk
title: Introduction à la théorie des graphes
tags: ['cours', 'graphes']

authors:
    - "François Brucker"


eleventyNavigation:
  key: "Graphes"
  parent: "Cours"
---

<!-- début résumé -->

Cette introduction a pour but d'exposer quelques définitions, concepts et méthodes de résolution de problèmes propre aux graphes.

Il a pour principal objectif d'allumer la petite flamme de l'intérêt pour cette structure, à la fois riche en problèmes intéressants et en solutions élégantes ; à la fois théorique — à l'intersection des mathématiques discrètes et de l'informatique théorique — et au cœur de nombre d'applications de tous les jours.

Le cours va être séparé en petites entités qui se suivent pour former un tout que l'on espère cohérent.

<!-- fin résumé -->

## Plan

> TBD : reprendre le cours papier.

### première partie

Où l'on découvre les graphes et l'on résout notre premier problème concret grâce à eux.

1. [Structure d'un graphe](structure)
2. [Chemins, cycle et connexité](chemins-cycles-connexite)
3. [Encodage de graphes](encodage)

Applications : 

1. [Parcours eulériens]({{ "/cours/graphes/parcours-euleriens" | url }}) : première application. Et on en profite pour montrer quelques algorithmes et propriétés
2. [Mots de Brujin]({{ "/cours/graphes/mots-brujin" | url }}) : on se rend compte qu'on peut modéliser un problème concret sous la forme d'un problème de graphe.

[Et si l'on codait tout ça ?]({{ "/cours/graphes/circuits-euleriens" | url }})

### deuxième partie

> TBD : mettre chemin au-dessus

Un cas particulier d'intérêt : l'arbre et les chemins.

> Sous la forme d'exercices.

1. [l'arbre]({{ "/cours/graphes/arbres" | url }})
2. [arbres binaires de recherche]({{ "/cours/graphes/arbre-de-recherche" | url }})
3. [chemins et arborescences]({{ "/cours/graphes/chemins" | url }})

> TBD
> combien d'arbre ? Encodage prüfer et application à un arbre aléatoire (!= différent de la structure).
{.note}

### troisième partie

chemins de longueur minimum.

### quatrième partie

Problèmes de flots. Définition, algorithmes et applications

1. [problèmes de flots]({{ "/cours/graphes/flots" | url }})
2. [applications]({{ "/cours/graphes/flots-applications" | url }})
