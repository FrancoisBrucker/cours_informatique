---
layout: layout/post.njk 
title: "S5 : Algorithmie avancée"

eleventyNavigation:
  order: 3

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

---

## Plan

1. 24/25 et 25/26 : Turing vers pseudo-assembleur
2. Assembleur, mémoire et C
3. graphes, arbre (nb) et k-connexité (Menger)
4. Graphes eulérien -> Christofides et idée du couplage sur graphe complet valué
5. 24/25 : flots (idée de la programmation linéaire) + plut de poids min/max
6. coupe min/max et couplage max graphe bi-parti
7. couplage min/max sur graphe bi-parti (parler de la méthode hongroise ?)
8. Graphes aléatoires et infinis
9. Cryptographie
10. Coloriabilité de graphes
11. graphes planaires

> TBD si on a le temps ou qu'ils ont envie

1. Couplage :
    1. valué : Lovaz dans Matching theory
    2. donner algo couplage Edmonds fleur + autre.
2. aléatoire, algorithme randomisé et approximation
    1. Commencez par les considération probabilistes sous-jacentes et exemples direct pour chaque
    2. exemples classiques
3. retour sur le couplage et algo randomisé
