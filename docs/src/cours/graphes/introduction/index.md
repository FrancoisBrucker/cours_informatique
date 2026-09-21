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

1. [Structure d'un graphe](structure){.interne}
2. [Encodage de graphes](encodage){.interne}

{% endaller %}

Connexités :

{% aller %}

[Chemins, cycle et connexité](chemins-cycles-connexite){.interne}

{% endaller %}

Les plus simples des graphes connexes :

{% aller %}

[Les Arbres](arbres){.interne}

{% endaller %}

## Aller d'un sommet à un autre

{% aller %}

[Chemin de valuation minimale dans un graphe](chemins-valuation-min){.interne}

{% endaller %}

## Parcourir tout le graphe

### Graphes Eulérien


L'origine de la théorie des graphe :

{% aller %}

[Chemins et cycles Eulérien](graphes-eulériens){.interne}

{% endaller %}

Et une conséquence inattendue (exercice de modélisation) :

{% aller %}

[Mots de Bruijn](mots-bruijn){.interne}

{% endaller %}

{% aller %}

[Compter et piocher les graphes eulériens](compter-piocher-eulerien){.interne}

{% endaller %}


Codons tout ça :

{% aller %}

[Projet : Graphes eulérien](projet-graphes-eulerien){.interne}

{% endaller %}


### Graphes Hamiltoniens

{% aller %}

[Chemins et cycles Hamiltonien](graphes-hamiltoniens){.interne}

{% endaller %}

> TBD est-ce normal que l'on ne puisse pas trouver d'algo simple pour résoudre le pb ?
> TBD ci NP algo

## Problèmes universels en théorie des graphes

> clique/stable
> chemin le plus long
> coloration (que sommet et laisser arête à plus tard)

## Graphes planaires

Finissons cette introduction par une classe intéressantes de graphes, ceux qu'on peut dessiner.

> thm des 4 couleurs qui est le 1er théorème assisté par ordinateur (pas une IA, c'est la preuve qui est un algorithme)
> tbd 