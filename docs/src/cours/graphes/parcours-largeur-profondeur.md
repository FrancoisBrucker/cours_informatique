---
layout: layout/post.njk

title: Parcours
authors: 
    - François Brucker

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Deux parcours classiques d'un graphe : largeur et profondeur.

<!-- fin résumé -->

> TBD compléter en utilisant des pile et des files pour les algos.

## Largeur

[Parcours en largeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_largeur)

tous les sommets une fois de plus en plus loin et chemin longs

## Profondeur

[Parcours en profondeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_profondeur)

parler de trouver cycles en temps linéaire avec.
