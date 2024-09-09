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

### Modèles de calculs et classes de problèmes "utiles"

1. cours 1 : [Modèle de calcul](/cours/algorithmie/#modèle-calculs)
   1. [pseudo-assembleur](/cours/algorithmie/exécuter-code/pseudo-assembleur/)
   2. [Architecture de Von Neumann](/cours/algorithmie/exécuter-code/von-neumann/)
   3. [Machines de Turing](/cours/algorithmie/machine-turing/)
2. Cours 2 : Turing et NP
   1. Machine de Turing
      1. définition alternatives
         - 2 curseurs
         - 2 rubans
         - alphabets
      2. Modèle `01#`
      3. coder avec Turing
         1. doublement de batons
         2. [autres exemples](https://courses.cs.washington.edu/courses/cse431/14sp/scribes/lec3.pdf)
   2. [réduction de problèmes](/cours/algorithmie/problème-réduction/)
   3. Classes de problèmes :
      1. [P, NP et NPC : avec vérifieurs](/cours/algorithmie/problèmes-NP/)
      2. [Recherche universelle](/cours/algorithmie/recherche-universelle/)
3. Cours 3
   1. Machines de Turing
      1. MTU
      2. Castors affairées
      3. [Rappels sur le problème de l'arrêt](/cours/algorithmie/bases-théoriques/arrêt-rice/). Avec le code de la machine (comme MTU) en entrée.
   2. P, NP et NPC
      1. [décision](/cours/algorithmie/décision-problèmes/)
      2. co-NP
   3. SAT, 3-SAT et 2-SAT
4. Cours 4 : [problème du sac à dos](/cours/algorithmie/problème-sac-à-dos/) et pseudo-polynomial.

### C

{% aller %}
[cours de C](/cours/système/langage-c/)
{% endaller %}

### Graphes

> TBD : voir ce qu'ils connaissent déjà

{% aller %}
[cours de Graphes](/cours/graphes/)
{% endaller %}

5. Graphes 1 :
   1. rappels
   2. quelques propriétés degrés/chemins
   3. connectivités
   4. parcours en largeur/profondeur
6. Graphes : 
   1. arbres def et preuves
   2. prufer
   3. parcours en profondeur et arborescence


## TBD

6.  Assembleur, mémoire et C
7.  graphes, arbre (nb) et k-connexité (Menger)
8.  Graphes eulérien -> Christofides et idée du couplage sur graphe complet valué
9.  24/25 : flots (idée de la programmation linéaire) + plut de poids min/max
10. coupe min/max et couplage max graphe bi-parti
11. couplage min/max sur graphe bi-parti (parler de la méthode hongroise ?)
12. Graphes aléatoires et infinis
13. Cryptographie
14. Coloriabilité de graphes
15. graphes planaires

> TBD si on a le temps ou qu'ils ont envie

1. Couplage :
    1. valué : Lovaz dans Matching theory
    2. donner algo couplage Edmonds fleur + autre.
2. aléatoire, algorithme randomisé et approximation
    1. Commencez par les considération probabilistes sous-jacentes et exemples direct pour chaque
    2. exemples classiques
3. retour sur le couplage et algo randomisé
