---
layout: layout/post.njk
title: Couplages

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le problème de couplage théorique avec de grandes portées pratiques

## Problème

{% aller %}
[Problème du couplage](./problème/){.interne}
{% endaller %}

## Algorithme optimaux

Le problème a l'air ardu mais il n'est pas NP-complet comme on pourrait s'y attendre, il est même facile à résoudre algorithmiquement. On peut noter que l'article présentant l'algorithme de résolution de ce problèmes nommé ["paths trees and flowers" (Edmonds, 1965)](https://math.nist.gov/~JBernal/p_t_f.pdf) est à l'origine même de la notion de problème polynomial (même si on trouve [des références plus anciennes](https://blog.computationalcomplexity.org/2022/11/who-first-thought-of-notion-of.html)).

Bref. C'est un joli problème avec de jolis algorithme et utile en pratique ce qui ne gâche rien.

### Chemins augmentant

Le principal outil utilisé pour résoudre le problème est le chemin augmentant. C'est le pendant graphe [des chaines augmentantes des flots](../flots/définitions/#chaîne-augmentante){.interne}.

{% aller %}
[Chemins augmentant](./chemins-augmentant/){.interne}
{% endaller %}

### Graphes bi-parti

{% aller %}
[Cas bi-parti](./couplage-bi-parti){.interne}
{% endaller %}

### Cas général

{% aller %}
[Cas général](./couplage-cas-général){.interne}
{% endaller %}

## Couplage de poids maximal

### Couplage max pour des graphes bi-parti

{% aller %}
[Cas bi-parti](./couplage-max-bi-parti){.interne}
{% endaller %}

### Couplage max cas général

{% aller %}
[Cas général](./couplage-max-cas-général){.interne}
{% endaller %}

## Variante

> TBD couplage par listes : proofs from the book problem de Dinitz (en faire un dm/exos)
> TD est-ce que ça exite dans le cas général ?

## Implémentations

- [NetworkX](https://networkx.org/) : <https://stackoverflow.com/questions/27132313/maximum-weighted-pairing-algorithm-for-complete-graph>
- <https://cs.stackexchange.com/questions/109021/perfect-matching-in-complete-weighted-graph>
