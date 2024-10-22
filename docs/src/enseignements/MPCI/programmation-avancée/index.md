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

> TBD année prochaine faire préparer le cours avant et au tableau aller plus loin ?

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

{% lien %}
Le but de cette partie est d'avoir assez de bases en C pour s'amuser.

N'hésitez pas à suivre et à faire également les exercices du cours suivant :

<https://www.0de5.net/stimuli/a-reintroduction-to-programming/essentials/just-enough-c-to-have-fun>
{% endlien %}

1. Cours 1 : Système et consequences pour le code
   1. [architecture générale](/cours/système-et-réseau/architecture-ordinateur/#général){.interne}
   2. Mémoire :
      1. [organisation système de la mémoire](/cours/système-et-réseau/système-exploitation/process/#forme-finale){.interne}
      2. différence entre pile et tas
   3. [cours de C](/cours/système-et-réseau/langage-c/){.interne} : survole tout jusqu'aux exercices. A préparer chez vous
2. Cours 2 : [exercices en C](/cours/système-et-réseau/langage-c/exercices){.interne}

{% faire "**DM**" %}
Faire en C le [projet sac à dos](/cours/algorithmie/problème-sac-à-dos/projet){.interne}

A rendre pour le 18 octobre.
{% endfaire %}

> TBD année prochaine :
>
> 1. les faire préparer le cours :
>    1. lire le cours : (pseudo-assembleur si pas préparé avant), von Neumann et C avant
>    2. faire le premier exercice
> 2. pendant le cours faire le système avec [radare2](https://book.rada.re/intro/overview.html) qui décompile à la volée comme dans <https://www.youtube.com/watch?v=76acHVJfziw.

### Bases de la théorie des graphes

#### Cours 1

1. [Graphes bases](/cours/graphes/structure){.interne} :
   1. rappel des définitions
   2. quelques propriétés sur les degrés, les chemins et les cycles
   3. NP complétude du problème clique
2. [exercice sur les tournois](/cours/graphes/parcours-hamiltoniens/#tournoi-exercice){.interne}

#### Cours 2

1. [Parcours eulériens](/cours/graphes/parcours-eulériens/){.interne}
2. [Parcours hamiltoniens](/cours/graphes/parcours-hamiltoniens/){.interne}
3. idée du problème du postier chinois

#### Cours 3

1. rappels sur les chemins les plus courts :
   1. [Poids positifs](/cours/graphes/chemin-poids-min-problème/){.interne}
   2. Noms des [algorithmes pour poids quelconques](/cours/graphes/chemin-poids-min-cas-général/){.interne}
2. Arbres :
   1. [version théorie des graphes des arbres](/cours/graphes/arbres/){.interne}
      - définitions
      - propriétés fondamentales
      - Cayley et Prüfer
   2. [Arbres couvrants](/cours/graphes/arbres-couvrants/){.interne}

### Problèmes de flots

#### Cours 1 : problèmes

[Problème et résolutions flots](/cours/graphes/flots/){.interne}

#### Cours 2 : applications

Exercices sur les flots :

1. [applications directs](/cours/graphes/flots-exercices/){.interne}
2. [Problèmes de transport](/cours/graphes/projet-flots-modélisation/){.interne}
3. [Bataille de la Marne](/cours/graphes/projet-bataille-de-la-marne/){.interne}

### Graphes biparti

1. [graphes bi-parti](/cours/graphes/graphe-biparti/){.interne} bases
2. [parcours de graphes classiques](/cours/graphes/parcours-largeur-profondeur/){.interne}

### DS

Temporellement placé juste après le cours 6.

[sujet](./DS/ds.pdf)

### Couplages dans les graphes

Cours 1 et 2

1. [graphes bi-parti](/cours/graphes/graphe-biparti/){.interne} (fin) :
   1. théorème de Graham-Pollack
   2. NP-complétude de la reconnaissance triparti
2. [couplage](/cours/graphes/couplage/){.interne}
3. Application : algorithme de Chritofides
4. [$k$-connectivité d'un graphe](/cours/graphes/connectivité/){.interne}

### Cryptographie

Cours 1, 2 et 3

{% aller %}
[Cryptographie](/cours/sécurité/){.interne}
{% endaller %}

### Coloriabilité

> TBD

### Planarité

> TBD

### Graphes aléatoires et infini

> TBD

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
- une présentation d'une jolie démonstration du proof from the book.
- un ds de théorie des graphes/informatique théorique
