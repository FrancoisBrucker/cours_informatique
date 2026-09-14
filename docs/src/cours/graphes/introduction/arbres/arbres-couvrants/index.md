---
layout: layout/post.njk

title: Arbres couvrants

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Un arbre couvrant est un sous graphe d'un graphe connexe :

{% note "**Définition**" %}
Un **_arbre couvrant d'un graphe connexe_** $G=(V, E)$  est un arbre $T=(V, E')$ tel que $E' \subseteq E$.
{% endnote %}

Commencez par montrer que cette définition fait sens :
{% exercice %}

Montrer que pour tout graphe connexe $G = (V, E)$, il existe au moins un arbre $T=(V, E')$ tel que $E' \subseteq E$.

{% endexercice %}
{% details "solution" %}
Si un graphe est connexe et n'est pas un arbre, alors il existe un cycle. En supprimant une arête de ce cycle le graphe reste connexe et a strictement moins d'arêtes. On peut alors itérativement supprimer des arêtes à un graphe connexe qui contient un cycle jusqu'à obtenir un graphe connexe à $\vert V \vert -1$ arêtes qui ne contient pas de cycles : ce sera un arbre.
{% enddetails %}

Notez que si le graphe $G$ n'est pas connexe, on peut itérer l'opération pour chaque partie connexe et trouver une **_forêt couvrante d'un graphe_**.

Les arbres couvrant d'un graphe sont beaucoup utilisés en optimisation où chaque arête à un poids, une valuation :

<span id="graphe_valué"></span>

{% note "**Définition**" %}
Un **graphe (orienté) valué** est un couple $(G, f)$ où :

- $G=(V, E)$ est un graphe (orienté)
- $f: E \rightarrow \mathbb{R}$

La **valuation** d'un graphe $G$, noté $f(G)$ est la somme des valuations de ses arcs/arêtes.
{% endnote %}


On cherche alors un arbre de valuation minimum/maximum :

{% note "**Définition**" %}
Un **_arbre couvrant de poids minimum (_resp._ maximum) d'un graphe connexe valué_** $(G, f)$  est un arbre couvrant $T=(V, E')$ tel que la somme de la valuation de ses arêtes est minimum (_resp._ maximum) parti tous les arbres couvrants de $G$.
{% endnote %}

Cette définition aussi fait sens puisqu'il y a un nombre fini d'arbres couvrants différents d'un graphe connexe. Attention cependant :

{% attention %}
Il n'y a pas unicité de l'arbre couvrant de poids minimum (_resp._ maximum) !

Si par exemple la valuation est constante, tout arbre couvrant est minimum (ils ont tous même valuation).
{% endattention %}

Le problème de la recherche d'un arbre couvrant de poids minimum est lié à bon nombre de problèmes d'optimisation. Par exemple : on suppose que vous êtes chef d'un état. Vous voulez que votre territoire soit connexe (que les gens puissent aller partout sur votre territoire), mais vous ne voulez pas payer trop cher (vous voulez être ré-élu et ça fait mauvais genre d'augmenter les impôts).

Vous demandez donc à vos conseillers de créer un graphe dont les sommets correspondant à vos villes et dont les arêtes sont valuées par le coût de construction d'une route entre ces 2 villes. Ce graphe n'a pas forcément toutes les arêtes si le coût de construction est prohibitif par exemple.

La solution la plus efficace consiste à trouver de ce graphe un arbre couvrant dont la somme des valuations est minimale parmi tous les arbres couvrant.

{% exercice %}

Pourquoi ?

{% endexercice %}
{% details "solution" %}
Un arbre est la structure minimale en nombre d'arêtes qui garantie la connexité. Parmi tous les arbres couvrants du graphe, on peut prendre un de ceux qui ont une somme des valuations de ses arêtes minimale (il y en a un nombre fini, le min existe donc mais il peut y en avoir plusieurs). Si la valuation d'une arête représente le coût, un arbre couvrant de poids minimal représente une solution de coût minimal pour rendre connexe le territoire.
{% enddetails %}

Les deux cas sont intéressant et fournissent nombre de jolis algorithmes et d'applications surprenantes,

## Cas non valué

{% aller %}
[Arbre et arborescences](./non-valué){.interne}
{% endaller %}

## Cas valué

{% aller %}
[Arbre et arborescences de poids minimal](./valué){.interne}
{% endaller %}


## On s'entraîne

{% aller %}
[Projet : débit](./projet-débit){.interne}
{% endaller %}
