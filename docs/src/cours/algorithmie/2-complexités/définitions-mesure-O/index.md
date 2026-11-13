---
layout: layout/post.njk

title: Mesures de complexités

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le calcul de la complexité d'un algorithme est une part importante de l'algorithmie. Elle met en œuvre des outils puissants et peut nécessiter des analyses et des raisonnements fins.

## Complexité algorithmique

{% aller %}
1. [Définitions](./définitions)
2. [Importance](./importance)
{% endaller %}

## Outil de mesure de la complexité : les $\mathcal{O}$

{% aller %}
1. [Problème du comptage exhaustif](./problème-comptage-exhaustif)
2. [Les $\mathcal{O}$ pour l'algorithmie](./O-pour-l-algorithmie)
{% endaller %}

> TBD suite = formulaire ; merge le 2eme

{% aller %}
1. [Comparaisons asymptotiques](./comparaisons-asymptotiques)
2. [regle pour les algorithmea](complexité-algorithmes-O)
{% endaller %}
