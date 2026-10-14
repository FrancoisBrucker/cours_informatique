---
layout: layout/post.njk

title: Introduction à la théorie des graphes

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

À partir des définitions générales sur de leur utilité algorithmique et pratique, nous allons raconter une histoire à priori simple dont les ramifications vont nous montrer de nombreuses facettes de la théorie des graphes.

## <span id="structure"></span> Structure d'un graphe

{% aller %}

1. [Structure d'un graphe](structure)
2. [Encodage de graphes](encodage)

{% endaller %}

Connexités :

{% aller %}

[Chemins, cycle et connexité](chemins-cycles-connexite)

{% endaller %}

Les plus simples des graphes connexes :

{% aller %}

[Les Arbres](arbres)

{% endaller %}

## Aller d'un sommet à un autre

{% aller %}

[Chemin de valuation minimale dans un graphe](chemins-valuation-min)

{% endaller %}

## Parcourir tout le graphe

### Graphes Eulérien

L'origine de la théorie des graphe :

{% aller %}

[Chemins et cycles Eulérien](graphes-eulériens)

{% endaller %}

Et une conséquence inattendue (exercice de modélisation) :

{% aller %}

[Mots de Bruijn](mots-bruijn)

{% endaller %}

{% aller %}

[Compter et piocher les graphes eulériens](compter-piocher-eulerien)

{% endaller %}

<!-- TBD

Codons tout ça :

{% aller %}

[Projet : Graphes eulérien](projet-graphes-eulerien)

{% endaller %}
 -->

### Graphes Hamiltoniens

{% aller %}

[Chemins et cycles Hamiltonien](graphes-hamiltoniens)

{% endaller %}

## Problèmes universels en théorie des graphes

{% prerequis %}
[Problèmes NP](/cours/algorithmie/problèmes-NP/)
{% endprerequis %}

{% aller %}

1. [Cliques et stables](cliques-stables)
2. [Chemin le plus long](./chemin-le-plus-long/)
3. [Coloration de sommets](./coloration-sommets/)

{% endaller %}
 
## Graphes planaires

Finissons cette introduction par une classe intéressantes de graphes, ceux qu'on peut dessiner.

{% aller %}

[Graphes planaires](./graphes-planaires/)

{% endaller %}
