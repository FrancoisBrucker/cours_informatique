---
layout: layout/post.njk

title: Les 8 reines

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Ce problème initial consiste à placer 8 reines sur un échiquier (possédant 8 lignes et 8 colonnes) sans qu'aucune reine ne puisse en prendre une autre.
Une reine peut prendre toute pièce qui est sur sa ligne, sa colonne ou sur ses diagonales.

Nous verrons ici un cas un peu plus général consistant à placer $n$ reines sur un échiquier à $n$ lignes et $n$ colonnes. On vous demande de donner la complexité de vos algorithmes en fonction de cette taille $n$.

## Modélisation

On modélise l'échiquier par une matrice `E` à $n$ lignes et $n$ colonnes ($n=8$ pour un échiquier traditionnel): `E[i][j]` correspond à la case à l'intersection de la ligne `i` et de la colonne `j`. Cette case est vraie si une reine y est placée et fausse sinon.

{% faire %}
Créez un algorithme permettant de créer un échiquier $n \times n$ vide.
{% endfaire %}

{% faire %}
Écrivez une fonction permettant de savoir si on peut placer une reine à la ligne `i`{.language-} et la colonne `j`{.language-} pour un échiquier donné (de taille quelconque). Elle rendra `Vrai`{.language-} si la reine peut être placée et `Faux`{.language-} sinon.
{% endfaire %}

{% faire %}
En déduire Éun algorithme qui, à partir d'un échiquier de taille quelconque $n$, rend `Vrai`{.language-} si l'échiquier résout le problème des 8 reines et `Faux`{.language-} sinon.
{% endfaire %}

## Résolution par énumération

> TBD rec (faire comme DS 1 2025 ENS)
> TBD iteratif

## Résolution par permutation

On peut cependant faire mieux que juste créer tous les échiquiers possibles.

{% faire %}
Montrez que l'on peut représenter le problème des $n$ reines par une permutation du tableau `[0, ..., n-1]`{.language-}.
{% endfaire %}

Vous pourrez utiliser dans cette parties [les différents algorithmes de permutation que l'on a vu](../permutations){.interne}

### Permutations

{% faire %}
Écrivez un algorithme prenant en paramètre une permutation de `[0, ..., n-1]`{.language-} et rendant `Vrai`{.language-} si la permutation est une solution du problème des 8 reines et `Faux`{.language-} sinon.
{% endfaire %}

### Résolution

On utilise les parties précédentes pour résoudre le problème des $n$ reines.

{% faire %}

Déduisez des questions précédentes un algorithme permettant de résoudre le problème des $n$ reines en examinant toutes les permutations.
{% endfaire %}

{% faire %}

Montrez qu'il est inutile d'examiner toutes les permutations et qu'il suffit souvent de connaître le début d'une permutation pour l'invalider. En déduire une méthode de résolution du problème n'examinant pas toutes les permutations.
{% endfaire %}

{% faire %}
Que pouvez-vous dire des différences de complexité entre les deux méthodes de résolution ?
{% endfaire %}

## Généralisation

{% lien %}
<https://interstices.info/le-probleme-des-8-reines-et-au-dela/>
{% endlien %}
