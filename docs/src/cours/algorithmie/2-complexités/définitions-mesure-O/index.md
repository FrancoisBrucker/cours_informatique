---
layout: layout/post.njk

title: Mesures de complexités

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le calcul de la complexité d'un algorithme est une part importante de l'algorithmie. Elle met en oeuvre des outils puissant et peut nécessiter des des analyses et des raisonnements fins.

## Complexité algorithmique

{% aller %}
1. [Définitions](./définitions)
2. [Importance](./importance)
{% endaller %}

## Outil de mesure de la complexité : les $\mathcal{O}$

{% aller %}
[Problème du comptage exhaustif](./problème-comptage-exhaustif)
{% endaller %}

Comme il est impossible de connaître le nombre exact d’instructions et qu'au final on s'en fiche puisque seule la forme générale et asymptotique est importante, on utilise des [comparaisons asymptotiques](https://fr.wikipedia.org/wiki/Comparaison_asymptotique){.externe}.

{% aller %}
1. [Comparaisons asymptotiques](./comparaisons-asymptotiques)
2. [Les $\mathcal{O}$ pour l'algorithmie](./O-pour-l-algorithmie)
{% endaller %}
