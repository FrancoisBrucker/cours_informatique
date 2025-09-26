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

Le problème n'est cependant pas NP-complet comme on pourrait s'y attendre, il est même facile à résoudre algorithmiquement. Commençons par caractériser les couplages maximum.

> Outil du chemin augmentant que l'on pourra appliquer aux graphes tout d'abord bi-parti puis généraux

### Chemin augmentant

> TBD chemins augmentant est l'outil permettant de savoir s'il existe ou pas un couplage max. Comme chaine augmentante des flots.
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

## Implémentations

- [NetworkX](https://networkx.org/) : <https://stackoverflow.com/questions/27132313/maximum-weighted-pairing-algorithm-for-complete-graph>
- <https://cs.stackexchange.com/questions/109021/perfect-matching-in-complete-weighted-graph>
