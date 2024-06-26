---
layout: layout/post.njk

title: Théorie des graphes
tags: ["cours", "graphes"]
authors:
  - "François Brucker"

eleventyNavigation:
  prerequis:
    - /cours/algorithmie/complexité-calculs/
    - /cours/coder-et-développer/

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Cette introduction a pour but d'exposer quelques définitions, concepts et méthodes de résolution de problèmes propre aux graphes.

Il a pour principal objectif d'allumer la petite flamme de l'intérêt pour cette structure, à la fois riche en problèmes intéressants et en solutions élégantes ; à la fois théorique — à l'intersection des mathématiques discrètes et de l'informatique théorique — et au cœur de nombre d'applications de tous les jours.

Le cours va être séparé en petites entités qui se suivent pour former un tout que l'on espère cohérent.

## <span id="structure"></span> Structure d'un graphe

1. [Structure d'un graphe](structure){.interne}
2. [Encodage de graphes](encodage){.interne}
3. [Chemins, cycle et connexité](chemins-cycles-connexite){.interne}

## Parcours

Un parcours d'un graphe est une suite de sommets ou d'arêtes ayant un propriété donné. On en verra plusieurs types ayant chacun leur propre intérêt.

### Types de parcours

1. [Largeur et profondeur](parcours-largeur-profondeur){.interne}
2. [Eulérien](parcours-eulériens){.interne}
3. [Hamiltonien](parcours-hamiltoniens){.interne}

### Projets

1. [Mots de Bruijn](projet-mots-bruijn){.interne}
2. [Problème du postier chinois](projet-postier-chinois){.interne}

## Chemins de longueur/poids minimum

### <span id="chemin-problèmes"></span> Problème et algorithmes

1. [Chemin de poids minimum](chemin-poids-min-problème){.interne}
2. [Algorithme de Dijkstra et $A^\star$](chemin-poids-min-positif){.interne}
3. [Algorithmes généraux](chemin-poids-min-cas-général){.interne}

### <span id="projet-chemin-poids-min"></span> Projets

1. [Projet chemins de poids minimum](projet-chemins-min){.interne}
2. [Projet graphe géographique](projet-graphe-géographique){.interne}
3. [Projet chemins avec hubs](projet-chemins-hub){.interne}

## Problèmes de flots

Problèmes de flots. Définition, algorithmes et applications

### Principes et algorithmes

1. [Les problèmes de flots](flots){.interne}
2. [connectivité](connectivité){.interne}

### <span id="projet-flots"></span> Projets

1. [exercices de modélisation](projet-flots-modélisation){.interne}
2. [bataille de la marne](projet-bataille-de-la-marne){.interne}

## Arbres

> TBD : mettre chemin au-dessus

> exo : <https://www.youtube.com/watch?v=OTfp2_SwxHk>
>
Un cas particulier d'intérêt : l'arbre et les chemins.

> Sous la forme d'exercices.

1. arbre planté algorithmique arborescence du parcours en largeur/profondeur + propriétés ?
2. [arbre et graphe]({{ "/cours/graphes/arbres"  }})
3. [arbres binaires de recherche]({{ "/cours/graphes/arbre-de-recherche"  }})
4. [chemins et arborescences]({{ "/cours/graphes/chemins"  }})

> TBD
> combien d'arbre ? Encodage prüfer et application à un arbre aléatoire (!= différent de la structure).
> {.note}
