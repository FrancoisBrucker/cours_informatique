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
   3. Modèle de la [Machine de Turing](/cours/algorithmie/machine-turing/)
2. Cours 2 : Turing et NP
   1. [Machines de Turing](/cours/algorithmie/machine-turing/)
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
3. Cours 3 : NP et Turing, NPC
   1. [SAT, 3-SAT et 2-SAT](/cours/algorithmie/problème-SAT/)
   2. P, NP et NPC
      1. [de vérifieur à décideur](/cours/algorithmie/décision-problèmes/)
      2. [SAT est NPC](/cours/algorithmie/décision-problèmes/SAT-NPC/)
4. Cours 4 : [problème du sac à dos](/cours/algorithmie/problème-sac-à-dos/)
   1. SAC à dos est NPC
   2. résolutions

### C

1. Système :
   1. [architecture générale](/cours/système/architecture-ordinateur/#général)
   2. Mémoire :
      1. [organisation système de la mémoire](/cours/système/système-exploitation/process/#forme-finale)
      2. différence entre pile et tas
2. [cours de C](/cours/système/langage-c/)

### Graphes

> TBD : voir ce qu'ils connaissent déjà

{% aller %}
[cours de Graphes](/cours/graphes/)
{% endaller %}

5. Graphes 1 :
   1. rappels
   2. quelques propriétés degrés/chemins
   3. connectivités : arbres
   4. parcours en largeur/profondeur
6. Graphes :
   1. arbres preuves Prufer effeuillage ...
   2. parcours en profondeur et arborescence

## Est tombé aux concours de cette partie

- variations et calcul sur 3-SUM
- sac à dos en programmation dynamique
- graphes bi-parti

## TBD

> TBD : fortement connexe et
> 

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
