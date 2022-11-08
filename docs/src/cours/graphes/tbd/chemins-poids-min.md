---
layout: layout/post.njk
title: Chemins

authors: 
    - François Brucker

eleventyNavigation:
  key: "Chemins"
  parent: "Graphes"
---

{% prerequis "**Prérequis** :" %}

* [Chemins, cycles et connexité](../chemins-cycles-connexite)

{% endprerequis %}

<!-- début résumé -->

Chemins entre deux sommets.

<!-- fin résumé -->


### Prim vs Dijkstra

{% exercice %}
* Quelle est la différence entre Prim et Dijsktra ?
* Montrez que les problèmes qu'ils résolvent sont différents et en déduire que l'arborescence obtenue par l'algorithme de Dijsktra pour un graphe non orienté peut être différente de l'arbre de poids minimum obtenu par Prim
{% endexercice %}
{% details "solution" %}
Le graphe suivant montre que l'arborescence de Disjkstra sera différente de l'arbre de poids minimum donné par Prim.

![Prim vs Dijkstra](../assets/img/chemin_prim_vs_dijkstra.png)

{% attention %}
Ne confondez pas les 2 problèmes !
{% endattention %}
{% enddetails %}


