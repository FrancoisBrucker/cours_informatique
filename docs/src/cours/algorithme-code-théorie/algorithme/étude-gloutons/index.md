---
layout: layout/post.njk 
title: "étude : algorithmes gloutons"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

prerequis:
    - "..//algorithmes-gloutons/"
---

<!-- début résumé -->

Deux cas d'utilisation des algorithmes gloutons pour résoudre de façon simple et approchée deux problèmes compliqués.

<!-- end résumé -->

TD : base et algos
TP : coder les optimisations

1. liste de pays coordonnées de la capitale
2. comment tracer des routes entre tous
3. juste plus proche ou k-plus proche marche pas forcement. il faut ajouter au plus proche de ceux qu'on a déjà
4. si route unique alors soucis si manif ou tremblement de terre
5. enveloppe convexe
6. triangulation part d'un triangle et on ajoute des points un a un. ne marche pas, pas convexe
7. enveloppe convexe + 1 point et glouton
8. glouton => triangulation de delaunay : https://mpechaud.fr/scripts/delaunay/delaunay.html
9. coloration en ne parlant pas de graphe, juste de voisins
10. algo glouton
11. nb face si face = triangle
12. => sommet <5
13. voyageur de commerce (glouton puis deux opt)

