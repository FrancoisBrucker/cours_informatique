---
layout: layout/post.njk
title: Couplages

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD on a déjà vu dans le problème du postier chinois.
> greedy algo : <https://people.cs.uchicago.edu/~laci/HANDOUTS/greedymatching.pdf>. On avait montré qu'il était au pire 1/2 moins bon.
> approximation 1/2 : <https://www.sciencedirect.com/science/article/abs/pii/S0020019002003939?via%3Dihub>

Le problème de couplage peut être défini ainsi :

{% note "**Définition**" %}
Soit $G=(V, E)$ un graphe. Un **_couplage_** est un ensemble $M \subseteq E$ tel que si $xy, x'y' \in E$ alors $xy \cap x'y' = \varnothing$ (le degré de tout sommet du graphe $G'=(V, M)$ est strictement inférieur à 2).
{% endnote %}

Dans un couplage tout extrémité d'une arête n'apparaît qu'une seule fois. Par exemple, les arêtes rouges du graphe ci-dessous :

![couplage exemple](couplage-exemple.png)

On définit plusieurs types de couplages selon le graphe :

{% note "**Définition**" %}
Soit $G=(V, E)$ un graphe. Un **_couplage_** $M$ est dit :

- **_maximal_** s'il n'existe pas de couplage $M'$ l'incluant (toute arête de $G$ possède une extrémité co;;une avec une arête de $M$)
- **_maximum_** s'il n'existe pas de couplage $M'$ tels que $\vert M'\vert > \vert M\vert$
- **_parfait_** si pour tout sommet de $V$ il existe une arête de $M$ l'ayant comme extrémité. Un couplage parfait ne peut exister que s'il y a un nombre pair de sommet et à forcément $\vert V \vert/2$ arêtes.
{% endnote %}

Le couplage du graphe précédent par exemple était maximal mais pas maximum. Il possède en effet un couplage parfait :

![couplage exemple parfait](couplage-exemple-parfait-1.png)

{% exercice %}
Montrez que le graphe précédent admet un autre couplage parfait.
{% endexercice %}
{% details "solution" %}
![couplage exemple parfait 2](couplage-exemple-parfait-2.png)
{% enddetails %}

> TBD perfect matching :
>
> - tutte 47 graph with perfect matching dans NP cap co-NP
> - <https://www.dimap.ufrn.br/~mfsiqueira/Marcelo_Siqueiras_Web_Spot/Talks_files/matching-1.pdf> 
> - <http://users.cms.caltech.edu/~schulman/Courses/18cs150/lec11.pdf>
> Tutte, c'est déterminent et c'est idem que multiplication de matrice. - <https://www.cs.mcgill.ca/~amehra13/Presentations/max_matching.pdf>


> TBD taille du couplage MAX : <https://fr.wikipedia.org/wiki/Formule_de_Tutte-Berge>

## Chemin augmentant

> TBD chemin augmentant, comme mariage

### Chemin augmentant et couplage maximum

> TBD caractérisation de Berge
>
### Trouver un chemin augmentant ?

> TBD pb de trouver un chemin augmentant : marche pas si cycle de longueur impaire.

> TBD général, histoire de la résolution : <https://ti.inf.ethz.ch/ew/lehre/GA07/lec-matching-alg.pdf>

## Graphe biparti

1. graphe biparti
   1. propriétés
   2. résolution
   3. couplage et couverture pour les graphes biparti
   4. biparti valué (min couverture = max couplage) :
      1. on peut toujours se ramener à un couplage parfait de $K_{n,n}$ en mettant des 0 sur les arˆ´tes qui n'existent pas
      2. <https://webia.lip6.fr/~bampise/kuhn-munkres.pdf>

> TBD : méthode hongroise <https://www.youtube.com/watch?v=fMAmtE0UyzI>

## Graphe quelconque

1. général
   1. les fleurs d'Edmonds $\mathcal{O}(n^4)$: <https://fr.wikipedia.org/wiki/Algorithme_d%27Edmonds_pour_les_couplages>, <https://math.nist.gov/~JBernal/p_t_f.pdf>
   2. couplage d'un graphe valué : <https://en.wikipedia.org/wiki/Maximum_weight_matching>
      1. on peut toujours se ramener à un couplage parfait en doublant le graphe et en mettant des 0 sur les arêtes qui relient les 2 copies du graphe
      2. on cherche des chaînes augmentantes dans des graphes particuliers. <https://theory.stanford.edu/~jvondrak/MATH233B-2017/lec6.pdf>. [Framework primal/dual](https://math.mit.edu/~goemans/PAPERS/book-ch4.pdf) : ceci dépasse le cadre de ce cours mais généralise ce qu'on a vu pour les graphes bipartis

{% lien %}

- [programmation linéaire et couplage](https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15850-f20/www/notes/lec7.pdf)
- [primal dual et problèmes combinatoires](https://www.youtube.com/watch?v=Z0eSQapcE6A&list=PLXsmhnDvpjORcTRFMVF3aUgyYlHsxfhNL&index=42)

{% endlien %}

## Implémentation

- networkx : <https://stackoverflow.com/questions/27132313/maximum-weighted-pairing-algorithm-for-complete-graph>
- <https://cs.stackexchange.com/questions/109021/perfect-matching-in-complete-weighted-graph>