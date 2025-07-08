---
layout: layout/post.njk
templateEngineOverride: njk, md

title: "J'aimerais être moins nul en python"
tags: ['enseignement', 'ECM']

eleventyNavigation:
  order: 0

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Une semaine pour comprendre le fonctionnement de python et l'utiliser pour développer ses propres programmes comme le ferait un informaticien.

Basé sur le cours :

{% aller %}
[Coder et développer en python](/cours/coder-et-développer){.interne}
{% endaller %}

Listes d'exercices en vrac :

- [les Mono-lignes](monolignes-élèves.pdf){.interne}.
- [exponentiation](/cours/algorithmie/projet-exponentiation/){.interne} :
  - prendre les algorithmes de la partie théorique (ils sont donnés) pour faire la partie pratique en python
  - puis faites la suite, plus générale sur [les suites additives](/cours_informatique/cours/algorithmie/projet-suite-additive/){.interne}
- Quelques [jeux de données du google code jam](https://github.com/lovebeckdy/google-code-jam/tree/master). Chaque dossier contient plusieurs jeux de données à résoudre. Le but est de le faire le plus rapidement possible. La première ligne de chaque jeu donne le nombre de données que contient le fichier. Il pourra être intéressant pour chaque problème, en plus de le résoudre, de faire un algorithme qui construit un jeu de donné. Deux problèmes simples si on les prend bien :
  - [Reverse word](https://github.com/lovebeckdy/google-code-jam/tree/master/reverse_words) : il faut rendre les mots dans le sens opposé (vous pourrez télécharger [ce fichier](https://raw.githubusercontent.com/hbenbel/French-Dictionary/master/dictionary/dictionary.csv) qui contient un dictionnaire. Il faudra prendre les mots qui commencent par une lettre en majuscule)
  - [store crédit](https://github.com/lovebeckdy/google-code-jam/tree/master/store_credit). Il faut trouver 2 indices différents d'une liste telle que la somme de leurs valeurs fasse une somme donnée (les deux indices existent et sont uniques pour chaque liste). Chaque donnée est constitué de 3 lignes :
    - une somme total
    - le nombre d'éléments de la troisième ligne
    - une liste de prix
- [un peu de crypto](support_eleves_cours_6.pdf)
- remplir [une grille aléatoire de sudoku](https://www.youtube.com/watch?v=2SuvO4Gi7uY) en utilisant [la réduction de paquet d'onde](https://fr.wikipedia.org/wiki/R%C3%A9duction_du_paquet_d'onde) (si si. Voir [ici](https://robertheaton.com/2018/12/17/wavefunction-collapse-algorithm/) pour une explication et un autre exemple). Attention, parfois cette méthode va rater et il faudra faire du [backtracking](https://fr.wikipedia.org/wiki/Retour_sur_trace) (ne l'implémentez pas ici, cela va au delà de cette semaine)
- Advent of code (vous pouvez vous connecter pour avec un jeu de données à vous):
  - [Popularité](https://jeroenheijmans.github.io/advent-of-code-surveys/)
  - [Advent of code 2017](https://adventofcode.com/2017) et [un jeu de donnée (et sa résolution en lisp)](https://github.com/gabrielelana/advent-of-code-2017)
  - [Advent of code 2023](https://adventofcode.com/2023) et [un jeu de donnée](https://github.com/dcastil/advent-of-code-2023/tree/main/data/examples)
  - [Advent of code 2019](https://adventofcode.com/2017) et [un jeu de donnée (et sa résolution en python)](https://github.com/jeroenheijmans/advent-of-code-2019)
- [Archives du Google code jam](https://zibada.guru/gcj/). Attention. parfois ça peut un peux piquer niveau difficulté.
