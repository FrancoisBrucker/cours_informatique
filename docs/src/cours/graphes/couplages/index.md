---
layout: layout/post.njk
title: Couplages

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> Problème

> Graphe biparti.
> algo problème général
> random ?

- tutte 47 graph with perfect matching dans NP cap co-NP

{% note "**Définition**" %}
Soit $G = (V, E)$ un graphe. Un sous-ensemble $M\subseteq E$ est un **_couplage_** si quelque soient $xy \neq x'y' \in M$, $xy \cap x'y' =\varnothing$ (le degré de tout sommet du graphe $G'=(V, M)$ est strictement inférieur à 2).

{% endnote  %}

> TBD cas simple : graphe bi-parti.
>
> TBD cas compliqué. graphe général.
> 
> TBD deux type d'algo pour le maximum :
>
> 1. exact Edmonds -> peut être amélioré
> 2. randomisé <https://web.eecs.umich.edu/~pettie/matching/Rabin-Vazirani-randomized-maximum-matching.pdf> -> peut être amélioré.
> 
> 
>  simple qui peut être amélioré.
> 
> TBD <https://www.dimap.ufrn.br/~mfsiqueira/Marcelo_Siqueiras_Web_Spot/Talks_files/matching-1.pdf> 
> TBD Couplage maximum, maximal et parfait.
>
> TBD pas de chaîne augmentante = maximum (Berge. 1957)
> TBD Perfect Matching (Tutte. 1947)
> TBD taille du couplage MAX : <https://fr.wikipedia.org/wiki/Formule_de_Tutte-Berge>
>
> approximation 1/2 : <https://www.sciencedirect.com/science/article/abs/pii/S0020019002003939?via%3Dihub>
> peut être randomisé.
> TBD Harvey 2006 : <https://www.math.uwaterloo.ca/~harvey/Publications/AlgebraicMatching/AlgebraicMatching.pdf>. Thèse (MIT) : <https://www.math.uwaterloo.ca/~harvey/PhDThesis.pdf>
> 
> TBD <http://users.cms.caltech.edu/~schulman/Courses/18cs150/lec11.pdf>
>
> TBD algo fleur de Edmonds O(n^4)
> 
> - <https://www.cs.mcgill.ca/~amehra13/Presentations/max_matching.pdf>
> <https://ti.inf.ethz.ch/ew/lehre/GA07/lec-matching-alg.pdf>
> <https://www.epfl.ch/labs/disopt/wp-content/uploads/2018/09/pset3.pdf>
>  <https://madars.org/projects/6854/AlgMatching.pdf>
>  <https://www.cs.cmu.edu/~15850/notes/lec8.pdf>
>  <https://www.math.uwaterloo.ca/~harvey/W11/Matching.pptx>
> 
  - Micali-Vazirani : <https://arxiv.org/pdf/2012.03582>
  - Harvey le mieux, las-vegas : <https://web.eecs.umich.edu/~pettie/matching/Harvey-maximum-matching-j-version.pdf>

- networkx : <https://stackoverflow.com/questions/27132313/maximum-weighted-pairing-algorithm-for-complete-graph>
- <https://cs.stackexchange.com/questions/109021/perfect-matching-in-complete-weighted-graph>
- <https://en.wikipedia.org/wiki/Maximum_weight_matching>