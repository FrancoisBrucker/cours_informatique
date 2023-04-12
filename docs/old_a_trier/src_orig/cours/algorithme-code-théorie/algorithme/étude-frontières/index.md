---
layout: layout/post.njk 
title: "étude : Frontières"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

prerequis:
    - "..//algorithmes-gloutons/"
---

<!-- début résumé -->

Problèmes de tracé de frontières et de colorations de cartes de géographies.
<!-- end résumé -->

1. enveloppe convexe
2. triangulation part d'un triangle et on ajoute des points un a un. ne marche pas, pas convexe
3. enveloppe convexe + 1 point et glouton
4. glouton => triangulation de delaunay : https://mpechaud.fr/scripts/delaunay/delaunay.html
5.  coloration en ne parlant pas de graphe, juste de voisins
6.  algo glouton
7.  nb face si face = triangle
8.  => sommet <5
9.  voyageur de commerce (glouton puis deux opt)

