---
layout: layout/post.njk

title: Trouver des chemins dans un graphe

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons étudier le problème de trouver des chemins de valuation minimale dans un graphe. 

{% aller %}

1. [Chemin de poids minimum](chemin-poids-min-problème){.interne}
2. [Algorithme avec poids positifs (Dijkstra et $A^\star$)](valuation-positive){.interne}
3. [Algorithmes généraux (Bellman-Ford et Roy-Floyd-Warshall)](cas-général){.interne}

{% endaller %}

Un projet de code pour expérimenter :

{% aller %}

[Projet chemins de poids minimum](projet-chemins-min){.interne}

{% endaller %}
