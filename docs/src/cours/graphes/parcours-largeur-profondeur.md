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

Deux parcours classiques d'un graphe : largeur et profondeur.

## Largeur

> TBD largeur et file

### Algorithme

[Parcours en largeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_largeur)

tous les sommets une fois de plus en plus loin et chemin longs

### Utilisation

- chemin le plus court en nombre de sommets non pondéré
- c'est Dijkstra avec une file de priorité et pas juste file

## Profondeur

> TBD profondeur et pile

### Algorithme

[Parcours en profondeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_profondeur)

### Utilisation

- Tarjan fortement connexe
- ordonnencement ordre en 
- parler de trouver cycles en temps linéaire avec.