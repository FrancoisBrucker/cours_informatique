---
layout: layout/post.njk

title: Parcours

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Deux parcours classiques d'un graphe : largeur et profondeur.

## Largeur

> TBD largeur et file

[Parcours en largeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_largeur)

Tous les sommets une fois de plus en plus loin et chemin long.

Utilisation :

> TBD on peut les prendre comme on veut, ce qui donne plein de parcours mais si file alors chemin plus court (en nb d'arêtes)

## Profondeur

> TBD profondeur et pile

[Parcours en profondeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_profondeur)

Utilisation :

- trouver cycles/chemin en temps linéaire
- Tarjan fortement connexe : <https://www.youtube.com/watch?v=m2mdGfxs_5E>

> TBD on va le voir partout.
