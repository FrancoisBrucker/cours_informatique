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

date: 2026-01-05

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Cette introduction a pour but d'exposer quelques définitions, concepts et méthodes de résolution de problèmes propre aux graphes.

Il a pour principal objectif d'allumer la petite flamme de l'intérêt pour cette structure, à la fois riche en problèmes intéressants et en solutions élégantes ; à la fois théorique — à l'intersection des mathématiques discrètes et de l'informatique théorique — et au cœur de nombre d'applications de tous les jours.

Le cours va être séparé en petites entités qui se suivent pour former un tout que l'on espère cohérent.

## Introduction générale

{% aller %}

[Introduction](./introduction/){.interne}

{% endaller %}

## Cliques et stables maximum

{% aller %}

[cliques et stables](/cours/graphes/cliques-stables/){.interne}

{% endaller %}

## Colorabilité d'un graphe

{% aller %}

[Colorabilité](./colorabilité){.interne}

{% endaller %}

## Graphes Planaires

{% aller %}

[Graphes planaires](./graphes-planaires){.interne}

{% endaller %}


> TBD le reste est en chantier.

## générer des graphes

- à sommets fixé

- Markov sur graphes : 2 cas : graphe de sommets ou structure
  - puis Markov sur euler
  - toutes les arborescence avec Markov 
  
### Euler et hamilton 

> TBD degrés : euler clair pair / ham et degré. Prop de Chvatal.



> TBD générer des graphes avec degrés fixe pour essayer nos algorithmes
> TBD on random des nombres dans une borne et on continue
le montre avec des matrices, nous juste avec un graphe.

> postier chinois et chritofides après couplage.
> TBD voir comment faire pour aller mieux -> pb du couplage.
> TBD à la fin du couplage. Se poser la question de résolution exacte ? NP-complet. et on y va.


### Projet graphes d'intervalles

1. meurtre
2. caractérisation Gilmore–Hoffman, forme "ordre des sommets"

Il existe n ordre linéaire entre les sommets te que x < y < z si xz est une arête alors xy aussi

, l'ensemble de ses voisins situés après lui dans l'ordre forme un bloc consécutif d'indices.

### Chemins de longueur/poids minimum

#### <span id="chemin-problèmes"></span> Problème et algorithmes


{% aller %}

1. [Parcours en largeur et en profondeur](parcours-largeur-profondeur){.interne}
2. [Odds and ends](./odds-and-ends/){.interne}
> TBD un écart sur combien de graphes différents ? A sommets fixés, et si on réordonne les sommets ?

{% endaller %}

## Cliques et stables

{% aller %}

[Cliques et stables d'un graphe](cliques-stables){.interne}

{% endaller %}

## Parcours

Un parcours d'un graphe est une suite de sommets ou d'arêtes ayant un propriété donné. On en verra plusieurs types ayant chacun leur propre intérêt.

### Chemins et cycles

Projet :

{% aller %}

1. [Chemins de Taxis](projet-chemin-de-taxi){.interne}
2. [cycle-chemin](projet-chemins-cycles){.interne}
{% endaller %}


## Graphe à degré fixé

- [formule de Erdos-Gallai](https://www.sciencedirect.com/science/article/pii/S0012365X09004683?fr=RR-2&ref=pdf_download&rr=a3de998bcd180c79)
- existence de graphes réguliers
- connexités des graphes à sommets fixé preuve de Ryker sur les matrices 0/1

> tous les graphes à suite de degré fixé Bender–Canfield 1978, affiné par McKay et McKay–Wormald
> TBD connexité <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4BE766CCFDF1704C196AA182C0C5EC88/S0008414X00044734a.pdf/combinatorial_properties_of_matrices_of_zeros_and_ones.pdf> 
> 
## Markov sur graphes
> TBD MCMC : <https://www.youtube.com/watch?v=nndtTssgtZE>

> TBD deux convergences possible si bi-parti ou pas.

> TBD markov sur graphe 2 critères de convergence :
>   1. P^n > 0
>   2. 1./p P^n pour graphe bi parti (ex arbre)

> Utilisation pour tirer :
>   - un graphe à sommet fixé aléatoire
>   - trouverr une arborescence aléatoire : Aldous-Broder

> TBD compter arbres couvrant markov simple
> TBD  Amélioration sur arbre avec Kirchoff sur graphe valué.

> application : créer un labyrinthe : <https://weblog.jamisbuck.org/2011/1/17/maze-generation-aldous-broder-algorithm> <https://epubs.siam.org/doi/10.1137/0403039>
> 


## Chemins le plus long

graphes-hamiltoniens

> TBD à transformer en voyageur de commerce

> Hamilton :
> [hamiltonian ciruits in random graph](https://www.sciencedirect.com/science/article/pii/0012365X76900686?ref=pdf_download&fr=RR-2&rr=a3dea0291f060c79) (posa) et [Fast probabilistic algorithms for hamiltonian circuits and matchings](https://www.sciencedirect.com/science/article/pii/002200007990045X?ref=pdf_download&fr=RR-2&rr=a3dea07c28a50c79)



Projets chemin (mettre de l'ordre)

{% aller %}

1. [Projet graphe géographique](projet-graphe-géographique){.interne}
2. [Projet chemins avec hubs](projet-chemins-hub){.interne}
3. [Projet chemin le plus long](chemin-le-plus-long){.interne}

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


<!-- Passer d'une coloration des arêtes aux sommets via le line graph :

{% aller %}

[projet _line graph_](./projet-line-graph){.interne}

{% endaller %} -->

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