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
    - /cours/algorithmie/problèmes-NP/

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Cette introduction a pour but d'exposer quelques définitions, concepts et méthodes de résolution de problèmes propre aux graphes.

Il a pour principal objectif d'allumer la petite flamme de l'intérêt pour cette structure, à la fois riche en problèmes intéressants et en solutions élégantes ; à la fois théorique — à l'intersection des mathématiques discrètes et de l'informatique théorique — et au cœur de nombre d'applications de tous les jours.

Le cours va être séparé en petites entités qui se suivent pour former un tout que l'on espère cohérent.

## <span id="structure"></span> Structure d'un graphe

{% aller %}

1. [Structure d'un graphe](structure){.interne}
2. [Encodage de graphes](encodage){.interne}
3. [Chemins, cycle et connexité](chemins-cycles-connexite){.interne}

{% endaller %}

## Parcours

Un parcours d'un graphe est une suite de sommets ou d'arêtes ayant un propriété donné. On en verra plusieurs types ayant chacun leur propre intérêt.

### Types de parcours

{% aller %}

1. [Largeur et profondeur](parcours-largeur-profondeur){.interne}
2. [Eulérien](parcours-eulériens){.interne}
3. [Hamiltonien](parcours-hamiltoniens){.interne}
{% endaller %}

### Projets

{% aller %}

1. [Mots de Bruijn](projet-mots-bruijn){.interne}
2. [Problème du postier chinois](projet-postier-chinois){.interne}

{% endaller %}

## Arbres

{% aller %}

1. [Arbres](arbres){.interne}
2. [Arbres enracinés](arbres-enracinés){.interne}
2. [Arbres couvrant](arbres-couvrants){.interne}

{% endaller %}

> exo : <https://www.youtube.com/watch?v=OTfp2_SwxHk>
>

1. [arbres binaires de recherche]({{ "/cours/graphes/arbre-de-recherche"  }})
2. [chemins et arborescences]({{ "/cours/graphes/chemins"  }})

> TBD : DFS et arbre. Tarjan pour fortement connexe.

{% aller %}

[Structures de données arborées](structures-arborées){.interne}

{% endaller %}

## Structures de données arborées

- tas
- file de priorité
- arbre de recherche

> TBD <https://www.youtube.com/watch?v=_n7RH11-eDM&list=PLwp5OpRmcl_EukVp5ntU0gtS-_g9ntCuI>

## Chemins de longueur/poids minimum

### <span id="chemin-problèmes"></span> Problème et algorithmes

{% aller %}

1. [Chemin de poids minimum](chemin-poids-min-problème){.interne}
2. [Algorithme de Dijkstra et $A^\star$](chemin-poids-min-positif){.interne}
3. [Algorithmes généraux](chemin-poids-min-cas-général){.interne}

{% endaller %}

### <span id="projet-chemin-poids-min"></span> Projets

{% aller %}

1. [Projet chemins de poids minimum](projet-chemins-min){.interne}
2. [Projet graphe géographique](projet-graphe-géographique){.interne}
3. [Projet chemins avec hubs](projet-chemins-hub){.interne}

{% endaller %}

## Problèmes de flots

Problèmes de flots. Définition, algorithmes et applications

### Principes et algorithmes

{% aller %}

[Les problèmes de flots](flots){.interne}

{% endaller %}

### <span id="projet-flots"></span> Projets

{% aller %}

1. [exercices de modélisation](projet-flots-modélisation){.interne}
2. [bataille de la marne](projet-bataille-de-la-marne){.interne}

{% endaller %}

## Connectivité

{% aller %}

[connectivité](connectivité){.interne}

{% endaller %}

## Planarité

> TBD isomorphisme de graphe planaire

## Colorabilité

> <https://en.wikipedia.org/wiki/Weisfeiler_Leman_graph_isomorphism_test>

## Couplages

{% aller %}
[Couplages](./couplages/){.interne}
{% endaller %}
