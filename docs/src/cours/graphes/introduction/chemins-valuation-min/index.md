---
layout: layout/post.njk

title: Trouver des chemins dans un graphe

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Pour cette partie, nous n'allons considérer **que des graphes orientés** car les notions et théorèmes présentés s'y prêtent mieux. Cela n'entraîne pas une grande perte de généralité : un graphe non orienté (valué) pouvant être considéré comme un graphe orienté avec 2 arcs opposés de même valuation.

Commençons par définir le problème :

{% note "**Définition**" %}
Soit $G = (V, E)$ un graphe orienté et $a, b$ deux sommets. Un **chemin de longueur minimum entre $a$ et $b$** est un chemin $v_0 \dots v_{k}$ tel que :

- $a = v_0$ et $b=v_{k}$
- il n'existe pas de chemin entre $a$ et $b$ de [longueur](../chemins-cycles-connexite#definition-longueur){.interne} strictement plus petite que $k$ (il y a $k+1$ sommets, donc $k$ arêtes).
  {% endnote %}

Que l'on généralise souvent aux **graphes (orientés) valués** :


{% note "**Définition**" %}
Soit $(G, f)$ un graphe valué et $a, b$ deux sommets de $G$. Un **chemin de poids minimum entre $a$ et $b$** est un chemin $c=v_0 \dots v_{k}$ tel que :

- $a = v_0$ et $b=v_{k}$
- il n'existe pas de chemin $w_0\dots w_{k'}$ de poids plus petit que celui de $c$.
  {% endnote %}

Il est clair qu'un chemin de longueur minimum d'un graphe est un chemin de poids minimum où toutes les valuations sont égales à 1.

Attention cependant :

{% note "**Proposition**" %}
Il peut exister **plusieurs chemins** de poids minimum entre $a$ et $b$ dans un graphe orienté valué $(G,f)$.
{% endnote %}
{% details "preuve", "open" %}
Le graphe orienté $G = (\\{a, b, c, d\\}, \\{ab, bc, ad, dc\\})$ admet deux chemins de longueur minimum entre $a$ et $c$.
{% enddetails %}

Le problème du chemin de poids minimum fait partie de ces problèmes où l'on cherche à minimiser une fonction mais où ce qui nous intéresse c'est l'élément qui réalise le minimum. Ce genre de problème admet souvent un minimum (unique) réalisable par plusieurs éléments.

## Graphe à valuation positive

Commençons par restreindre le problème au cas intuitif où **la valuation $f$ des arcs correspond à un coût**. Pensez par exemple à google maps où les arcs sont des tronçons de route. Les valuations peuvent alors être la distance du tronçon, les péages ou encore le temps min (en respectant les limitations de vitesse) pour le parcourir.

{% aller %}

[Graphe avec valuations positives](valuation-positive){.interne}

{% endaller %}

## Graphe à valuation quelconque

La définition que l'on s'est donné de chemin de poids minimum est intuitive : on cherche à aller d'un sommet $a$ à un sommet $b$ de la façon la plus rapide possible (pensez à un google maps par exemple). Mais cette notion est plus fine que l'on pourrait le croire lorsque l'on permet aux valuations d'être négatives. 

{% aller %}
 
[Algorithmes généraux (Bellman-Ford et Roy-Floyd-Warshall)](cas-général){.interne}

{% endaller %}

## On s'entraîne

Un projet de code pour expérimenter :

{% aller %}

[Projet chemins de poids minimum](projet-chemins-min){.interne}

{% endaller %}
