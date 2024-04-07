---
layout: layout/post.njk
title: "Structure de données linéaires"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD : structure "linéaire" permettant de contenir des données.

> plus que des tableaux

## Listes

{% aller %}
[liste](./liste/){.interne}
{% endaller %}

### Dérivés

> pile/files
> TBD : bornées
> TBD : circulaires

## Tableau associatifs

Aussi appelé dictionnaires

{% aller %}
[fonction de hachage](fonctions-hash){.interne}
{% endaller %}
{% aller %}
[dictionnaires](dictionnaire){.interne}
{% endaller %}

### Dérivés
> ensembles

