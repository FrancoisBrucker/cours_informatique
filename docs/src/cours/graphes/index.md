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

[Chemins de Taxis](projet-mots-bruijn){.interne}

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

> TBD : exemple de chemins de taxi. Voir <https://archipel.uqam.ca/8784/1/M14397.pdf> et <https://www.youtube.com/watch?v=C0sJycGTLTc>

## Arbres

{% aller %}

[Arbres](arbres){.interne}

{% endaller %}

## Exercices

> TBD
>
> - Chritofides <https://en.wikipedia.org/wiki/Christofides_algorithm> (en gardant l'algorithme heuristique, 1/2 approximation donc 2 approximation. On verra plus tard que 3/2 approximation)
> - Théorie de Buneman et X-arbres

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

## Graphe biparti

Un exemple particulier de graphes, les graphes bipartis :

{% aller %}
[Graphe bi-parti](graphe-biparti){.interne}
{% endaller %}

## Couplages

Problèmes de couplage dans un graphe. On passera un peu de temps sur le cas des graphes bi-parti avant d'aborder le cas général.

> TBD couper en bi-parti et quelconque et ajouter des exercices

{% aller %}
[Couplages](./couplages/){.interne}
{% endaller %}

### Graphe bi-parti

> TBD

### Graphe quelconque

> TBD

### Projet

> TBD revenir sur le problème du voyage de commerce avec

{% aller %}

[Problème du postier chinois](projet-postier-chinois){.interne}

{% endaller %}

## Colorabilité d'un graphe

{% aller %}

[Colorabilité](./colorabilité){.interne}

{% endaller %}

## Graphes parfaits

{% aller %}

[Graphes parfaits](./graphes-parfaits){.interne}

{% endaller %}

## Graphes Planaires

{% aller %}

[Graphes planaires](./graphes-planaires){.interne}

{% endaller %}

## Projets Autres

> TBD [DM line graph](./line-graph){.interne}

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
>