---
layout: layout/post.njk

title: Théorie des graphes
tags: ["cours", "graphes"]
authors:
  - "François Brucker"
resume: "Cette introduction a pour but d'exposer quelques définitions, concepts et méthodes de résolution de problèmes propre aux graphes."

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
3. [Parcours en largeur et en profondeur](parcours-largeur-profondeur){.interne}

{% endaller %}

## Cliques et stables

{% aller %}

[Cliques et stables d'un graphe](cliques-stables){.interne}

{% endaller %}

## Parcours

Un parcours d'un graphe est une suite de sommets ou d'arêtes ayant un propriété donné. On en verra plusieurs types ayant chacun leur propre intérêt.

### Chemins et cycles

{% aller %}

[Chemins, cycle et connexité](chemins-cycles-connexite){.interne}

{% endaller %}

Projet :

{% aller %}

[Chemins de Taxis](projet-chemin-de-taxi){.interne}

{% endaller %}

### Chemins le plus long

{% aller %}

1. [Chemins et cycles Eulérien](parcours-eulériens){.interne}
2. [Chemins et cycles Hamiltonien](parcours-hamiltoniens){.interne}
3. [Ordonnancement de tâches](parcours-ordonnancement){.interne}

{% endaller %}

Projets :

{% aller %}

1. [Mots de Bruijn](projet-mots-bruijn){.interne}
2. [cycle-chemin](./projet-chemins-cycles){.interne}

{% endaller %}

### Chemins de longueur/poids minimum

#### <span id="chemin-problèmes"></span> Problème et algorithmes

{% aller %}

1. [Chemin de poids minimum](chemin-poids-min-problème){.interne}
2. [Algorithme avec poids positifs (Dijkstra et $A^\star$)](chemin-poids-min-positif){.interne}
3. [Algorithmes généraux (Bellman-Ford et Roy-Floyd-Warshall)](chemin-poids-min-cas-général){.interne}

{% endaller %}

#### <span id="projet-chemin-poids-min"></span> Projets

{% aller %}

1. [Projet chemins de poids minimum](projet-chemins-min){.interne}
2. [Projet graphe géographique](projet-graphe-géographique){.interne}
3. [Projet chemins avec hubs](projet-chemins-hub){.interne}

{% endaller %}

## Arbres

{% aller %}

[Arbres](arbres){.interne}

{% endaller %}

> TBD projets/applications
> Buneman ET MPCI 24-25
> TBD X-arbre et représentation combinatoire des arbres par bi-partition.
> TBD c'est l'ET 2024-2025
> TBD évolution arborée et distance d'évolution. Condition des 4-points.

## Problèmes de flots

Problèmes de flots. Définition, algorithmes et applications

### Principes et algorithmes

{% aller %}

1. [Les problèmes de flots](flots){.interne}
2. [Exercices d'application](flots-exercices){.interne}

{% endaller %}

### <span id="projet-flots"></span> Modélisation

{% aller %}

1. [Deux problèmes de transports](projet-flots-modélisation){.interne}
2. [bataille de la marne](projet-bataille-de-la-marne){.interne}
3. [connectivité](connectivité){.interne}

{% endaller %}

<!-- > TBD en DM [Théorème de Baranyai](https://en.wikipedia.org/wiki/Baranyai%27s_theorem). C'est des flots. <https://math.stackexchange.com/questions/1827816/proof-of-baranyais-theorem> et p20 <http://discretemath.imp.fu-berlin.de/DMII-2018-19/connectivity-flows-baranyai.pdf> -->

## Graphe biparti

Une classe particulières de graphes cruciale :

{% aller %}
[Graphe bi-parti](graphe-biparti){.interne}
{% endaller %}

## Couplages

Problèmes de couplage dans un graphe. On passera un peu de temps sur le cas des graphes bi-parti avant d'aborder le cas général.

{% aller %}
[Couplages](./couplages/){.interne}
{% endaller %}

<!-- carré latin. Avec preuve et code. -->

<!-- Un projet qui utilise (presque) tout ce qu'on a vu jusqu'à présent, et en particulier les couplages :

{% aller %}

[Problème du postier chinois](projet-postier-chinois){.interne}

{% endaller %} -->

## Colorabilité d'un graphe

{% aller %}

[Colorabilité](./colorabilité){.interne}

{% endaller %}

<!-- Passer d'une coloration des arêtes aux sommets via le line graph :

{% aller %}

[projet _line graph_](./projet-line-graph){.interne}

{% endaller %} -->

## Graphes Planaires

{% aller %}

[Graphes planaires](./graphes-planaires){.interne}

{% endaller %}

<!-- 
## Graphes cordés

> TBD conf de knuth <https://www.youtube.com/watch?v=txaGsawljjA>

## Graphes parfaits

{% aller %}

[Graphes parfaits](./graphes-parfaits){.interne}

{% endaller %}

## Graphes aléatoires et infinis

> TBD erdos-rado
> graphe infini unique
> grosse partie connexe
> pas connexe puis tout d'un coup connexe
> mes amis ont plus d'amis que moi
> Beaucoup de graphes ne sont pas parfait en prenant H = C5 : <https://math.stackexchange.com/questions/4729419/let-h-be-a-graph-prove-that-almost-every-graph-g-in-mathcalg-n-p-has>

>probabilistic method : hamiltonian path <https://www.youtube.com/watch?v=feEXMWBQGZk&list=PLUl4u3cNGP61cYB5ymvFiEbIb-wWHfaqO&index=5> et lire <https://www-sop.inria.fr/members/Frederic.Havet/Cours/proba-notes.pdf>

## Algorithmes randomisés

> TBD Partie 3, après algo random et hasard en algorithmie.

> TBD <https://www.cse.iitd.ac.in/~ssen/chapters/randgraph.pdf>
> probabilistic method in graph theory : <https://www.youtube.com/watch?v=crMyNv2fdkc&list=PLUl4u3cNGP61cYB5ymvFiEbIb-wWHfaqO>

### couplage

> Algo randomisés :
>
> - <https://www.epfl.ch/labs/disopt/wp-content/uploads/2018/09/pset3.pdf>
> - <https://madars.org/projects/6854/AlgMatching.pdf>
> - <https://www.cs.cmu.edu/~15850/notes/lec8.pdf>
> - <https://www.math.uwaterloo.ca/~harvey/W11/Matching.pptx>
>
> TBD : <https://web.eecs.umich.edu/~pettie/matching/Rabin-Vazirani-randomized-maximum-matching.pdf> -> peut être amélioré.
> Micali-Vazirani : <https://arxiv.org/pdf/2012.03582>
>
> TBD : Harvey 2006, le mieux, Las Vegas :
>
> - <https://www.math.uwaterloo.ca/~harvey/Publications/AlgebraicMatching/AlgebraicMatching.pdf>
> - Thèse (MIT) : <https://www.math.uwaterloo.ca/~harvey/PhDThesis.pdf>
> - <https://web.eecs.umich.edu/~pettie/matching/Harvey-maximum-matching-j-version.pdf>
> -->