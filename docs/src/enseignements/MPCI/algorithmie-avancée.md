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

1. exécuter du code
   1. pseudo-assembleur
   2. modèle de Von Neumann
   3. la pile : structure de donnée et usage
2. penser l'informatique
   1. Machine de Turing
   2. définitions alternatives
   3. Machine de Turing Universelle
3. Réduction de problèmes
   1. problèmes P et NP
   2. 
4. 24/25 et 25/26 : Turing vers pseudo-assembleur
5. Assembleur, mémoire et C
6. graphes, arbre (nb) et k-connexité (Menger)
7. Graphes eulérien -> Christofides et idée du couplage sur graphe complet valué
8. 24/25 : flots (idée de la programmation linéaire) + plut de poids min/max
9.  coupe min/max et couplage max graphe bi-parti
10. couplage min/max sur graphe bi-parti (parler de la méthode hongroise ?)
11. Graphes aléatoires et infinis
12. Cryptographie
13. Coloriabilité de graphes
14. graphes planaires

> TBD si on a le temps ou qu'ils ont envie

1. Couplage :
    1. valué : Lovaz dans Matching theory
    2. donner algo couplage Edmonds fleur + autre.
2. aléatoire, algorithme randomisé et approximation
    1. Commencez par les considération probabilistes sous-jacentes et exemples direct pour chaque
    2. exemples classiques
3. retour sur le couplage et algo randomisé
