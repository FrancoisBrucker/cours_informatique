---
layout: layout/post.njk
title: Algorithme de Busacker et Gowen

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[Algorithme de Busacker et Gowen](https://fr.wikipedia.org/wiki/Algorithme_de_Busacker_et_Gowen)
{% endlien %}

{% attention %}
On considérera par la suite que le graphe $G$ est antisymétrique puisque l'on utilise des graphes d´écart. On a vu que ce n'était pas restrictif puisque l'on peut associer un graphe antisymétrique à tout graphe en ne changeant pas les valeurs de flots
{% endattention %}

Si on doit payer un coût pour faire transiter un flot par un arc, il est naturel de rechercher un flot maximum à coût minimum.

{% note "**Définition**" %}
Si $\gamma : E \rightarrow \mathbb{R}^+$ est une fonction de coût sur les arc de $G$ et $f$ un de ses flot, le coût du flot est :

<div>
$$
\sum_{xy \in G} f(xy) \cdot \gamma(xy)
$$
</div>
{% endnote %}

Le problème est alors :

{% note %}
Parmi tous les flot maximum, un choisir un de coût minimum.
{% endnote %}

Ce qui est surprenant, c'est que ceci peut se faire aisément en modifiant l'algorithme de Edmonds et Karp : plutôt que de chercher un chemin de longueur minimum dans le graphe d'écart, on cherche un chemin de coût minimum en utilisant la fonction de coût suivante :

- si $xy$ est un arc de $G$ on le coût de l'arc dans le graphe d'écart est le même que pour le graphe d'origine puisque si cet arc est choisi on va augmenter le flot passant par lui
- si $xy$ est un arc de $G$ on le coût de l'arc dans le graphe d'écart est l'opposé du coût dans le graphe d'origine puisque si cet arc est choisi on va diminuer le flot passant par lui

{% attention %}
Comme les poids peuvent être négatifs, il faut utiliser [l'algorithme de Belman-ford](../../chemin-poids-min-cas-général/){.interne} de complexité $\mathcal{O}(e(G) \cdot v(G))$ pour trouver un chemin de longueur minimum entre $s$ et $t$.
{% endattention %}

Enfin, il faut partir du flot nul pour que l'optimalité soit garantie.

{% note %}
Cet algorithme est appelé **_algorithme de Busacker-Gowen_**.
{% endnote %}

Cela semble une amélioration naturelle mais la justification de sa véracité ne l'est pas vraiment.

## Véracité

> TBD voir le charon-Hudry p251 (partie 11.5)

## Complexité

La recherche d'un chemin de coût min n'est plus en $\mathcal{O}(e(G))$ mais en $\mathcal{O}(e(G) \cdot v(G))$. Une recherche de chemin puis une augmentation du flot est donc en $\mathcal{O}(e(G) \cdot v(G))$ opérations.

La complexité totale est donc bornée, comme pour celui de Ford et Fulkerson en $\mathcal{O}(c(S, \overline{S}) \cdot e(G) \cdot v(G))$ opérations.

> TBD est-ce polymomial ? Wikipedia dit n^4 mais sans preuve. Est-ce que la longueur des chemins augmente ?
