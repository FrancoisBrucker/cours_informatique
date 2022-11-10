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

{% prerequis "**Prérequis** :" %}

* [notion de complexité algorithmique]({{"/cours/algorithme-code-théorie/algorithme/complexité-max-min/" | url}})
* [bases de python]({{"/cours/base-code/" | url}}) (également la partie [pour aller plus loin]({{"/cours/base-code/" | url}}#pour-aller-plus-loin) car nous aurons à installer des packages et à utiliser le terminal) et [list comprehension en python](https://docs.python.org/fr/3/howto/functional.html#generator-expressions-and-list-comprehensions)

{% endprerequis %}

## Structure d'un graphe

1. [Structure d'un graphe](structure)
2. [Encodage de graphes](encodage)
3. [Chemins, cycle et connexité](chemins-cycles-connexite)

## Parcours

Un parcours d'un graphe est une suite de sommets ou d'arêtes ayant un propriété donné. On en verra plusieurs types ayant chacun leur propre intérêt.

### Types de parcours

1. [Largeur et profondeur](parcours-largeur-profondeur)
2. [Eulérien](parcours-euleriens)
3. [Hamiltonien](parcours-hamiltoniens)

### Projets

1. [Mots de Bruijn](projet-mots-bruijn)
2. [Problème du postier chinois](projet-postier-chinois)

## Chemins de longueur minimum

1. [chemin de poids minimum](chemin-poids-min)
2. [Projet chemins de longueur minimum](projet-chemins-min)
3. projet OSM

## Problèmes de flots

Problèmes de flots. Définition, algorithmes et applications

1. [problèmes de flots]({{ "/cours/graphes/flots" | url }})
2. [applications]({{ "/cours/graphes/flots-applications" | url }})

## arbres

> TBD : mettre chemin au-dessus

Un cas particulier d'intérêt : l'arbre et les chemins.

> Sous la forme d'exercices.

1. arbre planté algorithmique arborescence du parcours en largeur/profondeur + propriétés ?
2. [arbre et graphe]({{ "/cours/graphes/arbres" | url }})
3. [arbres binaires de recherche]({{ "/cours/graphes/arbre-de-recherche" | url }})
4. [chemins et arborescences]({{ "/cours/graphes/chemins" | url }})

> TBD
> combien d'arbre ? Encodage prüfer et application à un arbre aléatoire (!= différent de la structure).
{.note}

$k$-connectivité ? Menger ?
