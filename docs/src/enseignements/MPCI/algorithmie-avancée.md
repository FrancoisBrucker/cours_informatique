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

## Programme

En quatre parties.

### Modèles de calculs et classes de problèmes "utiles"

1. cours 1 : [Modèle de calcul](/cours/algorithmie/#modèle-calculs){.interne}
   1. [pseudo-assembleur](/cours/algorithmie/exécuter-code/pseudo-assembleur/){.interne}
   2. [Architecture de Von Neumann](/cours/algorithmie/exécuter-code/von-neumann/){.interne}
   3. Modèle de la [Machine de Turing](/cours/algorithmie/machine-turing/){.interne}
2. Cours 2 : Turing et NP
   1. [Machines de Turing](/cours/algorithmie/machine-turing/){.interne}
      1. définition alternatives
         - 2 curseurs
         - 2 rubans
         - alphabets
      2. Modèle `01#`
      3. coder avec Turing
         1. doublement de batons
         2. [autres exemples](https://courses.cs.washington.edu/courses/cse431/14sp/scribes/lec3.pdf)
   2. [réduction de problèmes](/cours/algorithmie/problème-réduction/){.interne}
   3. Classes de problèmes :
      1. [P, NP et NPC : avec vérifieurs](/cours/algorithmie/problèmes-NP/){.interne}
      2. [Recherche universelle](/cours/algorithmie/recherche-universelle/){.interne}
3. Cours 3 : NP et Turing, NPC
   1. [SAT, 3-SAT et 2-SAT](/cours/algorithmie/problème-SAT/){.interne}
   2. P, NP et NPC
      1. [de vérifieur à décideur](/cours/algorithmie/décision-problèmes/){.interne}
      2. [SAT est NPC](/cours/algorithmie/décision-problèmes/SAT-NPC/){.interne}
4. Cours 4 : [problème du sac à dos](/cours/algorithmie/problème-sac-à-dos/){.interne}
   1. [SAC à dos est NPC](/cours/algorithmie/exemples-problèmes-NPC/){.interne}
   2. [résolutions](/cours/algorithmie/problème-sac-à-dos/étude){.interne} :
      1. fractionnel
      2. énumération (juste donner le principe)
      3. programmation dynamique

### C

1. Système :
   1. [architecture générale](/cours/système/architecture-ordinateur/#général){.interne}
   2. Mémoire :
      1. [organisation système de la mémoire](/cours/système/système-exploitation/process/#forme-finale){.interne}
      2. différence entre pile et tas
2. [cours de C](/cours/système/langage-c/){.interne}
3. Faire en C le [projet sac à dos](/cours/algorithmie/problème-sac-à-dos/projet){.interne}

### Graphes

> TBD : voir ce qu'ils connaissent déjà

{% aller %}
[cours de Graphes](/cours/graphes/){.interne}
{% endaller %}

1. Graphes 1 :
   1. rappels
   2. quelques propriétés degrés/chemins
   3. connectivités : arbres
   4. parcours en largeur/profondeur
2. Arbres :
   1. arbres preuves Prufer effeuillage ...
   2. parcours en profondeur et arborescence
3. graphes, arbre (nb) et k-connexité (Menger)
4. Graphes eulérien -> Christofides et idée du couplage sur graphe complet valué
5. flots (idée de la programmation linéaire) + flot de poids min/max
6. coupe min/max et couplage max graphe bi-parti
7. Graphes aléatoires et infinis (intro)
8. Coloriabilité de graphes
9. graphes planaires

### Cryptographie

{% aller %}
[Cryptographie](/cours/système/cryptographie/){.interne}
{% endaller %}

## Modalités de contrôle

### Note

La note de cette UE résulte de cette formule :

$$
\max (\frac{DM+ DS + ET}{3}, ET)
$$

Avec :

- $DM$ devoir(s) maison ou exposé(s)
- $DS$ la note du devoir surveillé
- $ET$ est l'examen terminal

### Rendus

- deux dm de code
- un ds de théorie des graphes/informatique théorique
