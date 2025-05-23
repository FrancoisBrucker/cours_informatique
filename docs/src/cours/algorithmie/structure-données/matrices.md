---
layout: layout/post.njk 
title:  "Matrices"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On peut facilement créer des matrices uniquement avec des tableaux (on l'a déjà un peu expérimenté avec [le tri par base](../../projet-algorithmes-classiques//tris-spéciaux/#tri-base){.interne} où les données était des tableaux et surtout [le problème des 8 reines](../../projet-algorithmes-classiques/8-reines){.interne} Ce type est tellement utilisé en algorithme qu'on le considérera souvent comme un type de base.

Pour cela on utilisera le paradigme suivant :

{% note "**Définition**" %}

Une matrice de dimension $k$ est constitué d'un tableau de matrices de dimensions $k-1$
{% endnote %}

Une matrice entière $M$ de $n$ lignes et $p$ colonnes sera constitué d'un tableau de $n$ lignes (un tableau de $p$ entiers).

## Matrice 2D

Une matrice d'entiers en deux dimensions sera ainsi un tableau de tableaux, donc de type :

```pseudocode
M: [[entier]]
```

### Création

La création d'une matrice $M$ se fait ligne à ligne :

```pseudocode
algorithme creation_matrice(nb_lignes: entier, nb_colonnes:entier) → [[entier]]:
    M ← un nouveau tableau de n tableaux d'entiers

    pour chaque i de [0, nb_lignes[:
        L ← un nouveau tableau de nb_colonnes entiers
        M[i] ← L
    rendre M
```

La création et l'affectation initiale d'une matrice est linéaire en sa taille.

Comme lors de la création de tableaux les valeurs sont indéterminées, on a coutume d'initialiser les valeurs de la matrice lors de sa création :

```pseudocode
algorithme creation_matrice(nb_lignes: entier, nb_colonnes:entier, valeur: entier) → [[entier]]:
    M ← un nouveau tableau de l tableaux d'entiers

    pour chaque i de [0, nb_lignes[:
        L ← un nouveau tableau de nb_colonnes entiers
        pour chaque j de [0, nb_colonnes[:
            L[j] ← valeur
        M[i] ← L
    rendre M
```

Le nombre d'opération élémentaires pour initialiser la matrice sera alors proportionnelle à sa taille, le nombre de lignes fois le nombre de colonnes.

### Utilisation

Une fois la matrice créée, il est facile de lire et écrire un élément. Par exemple pour affecter puis afficher à l'écran l'élément de ligne $i$ et de colonne $j$ de la matrice $M$ :

```pseudocode
x ← un entier entré par l'utilisateur
M[i][j] ← x
Affiche à l'écran M[i][j]
```

### _Abus_ de notations

Cette utilisation nous permettra d'étendre aux matrice les _abus_ classique des tranches de tableaux.

Comme la création directe qui prend $\mathcal{O}(n)$ opérations. :

```pseudocode
M ← une nouvelle matrice à n ligne et m colonnes
```

Ou encore parler de la matrice `M[a:b][c:d]` qui correspond à une sous matrice de $M$ allant des colonnes d'indice `c`{.language-} à `d-1`{.language-} pour les lignes allant de l'indice `a`{.language-} à `b-1`{.language-}.:

## Généralisation

Cette méthode se généralise aisément à des matrices de dimensions supérieures.

Pour créer une matrice de dimension 3 (d1, d2 et d3) :

```pseudocode
M3 ← un nouveau tableau de n tableaux de tableaux

pour chaque i de [0, d1[:
    M2 ← un nouveau tableau de d2 tableaux
    M3[i] ← M2
    pour chaque j de [0, d2[:
        L ← un nouveau tableau de d3 entiers
        M2[j] ← L
```

Une fois la matrice créée, son utilisation est identique à une matrice en deux dimensions :

```pseudocode
x ← un entier entré par l'utilisateur
M[i][j][k] ← x
Affiche à l'écran M[i][j][k]
```

Son type sera un un tableau de tableaux de tableaux d'entiers :

```pseudocode
M: [[[entier]]]
```

Et tout ceci se généralise à la dimension $k$ bien sur...

## Nombre d'opérations élémentaires

La méthode de création présenté nécessite une boucle, ce n'est donc pas une opération élémentaire.

Il faut par exemple $n$ opérations pour créer une matrice de $n$ lignes et $p$ colonnes.
Ceci n'est souvent pas gênant algorithmiquement car si on utilise une matrice c'est pour utiliser toutes ses lignes et colonnes, ne serait-ce que pour les initialiser (rappelez vous que lorsque l'on crée un tableau ses valeurs sont indéterminées).

Mais si l'on veut pouvoir créer des matrices en 1 unique opération on peut le faire comme le montre la série d'exercice suivant. On utilise cependant peu cette méthode algorithmiquement car son utilisation complexifie l'algorithme sans réel gain car s'il faut initialiser la matrice on ne gagne rien (algorithmiquement) à la créer en $\mathcal{O}(1)$ opération.

Son réel gain est au niveau de l'implémentation car elle permet de stocker la matrice dans des cases mémoires contiguës ce qui permet une gestion [de la mémoire cache](https://fr.wikipedia.org/wiki/M%C3%A9moire_cache) plus optimale. Ceci dépasse cependant le cadre de ce cours d'algorithmie (rendez vous dans le cours système !)

{% exercice %}
Montrez qu'il existe une bijection entre l'ensemble de tous les couples $(i, j)$ pour $1\leq i \leq n$ et $1\leq j \leq p$ et l'intervalle $[0, p\cdot q[$
{% endexercice %}
{% details "corrigé" %}

<div>
$$
f(i, j) = (i-1) \cdot n + (j-1)
$$
</div>

C'est une bijection puisque :

<div>
$$
f^{-1}(k) = ((k \\\;\mbox{ div } n) + 1, (k\mathbin{\small\\%} n) + 1)
$$
</div>

{% enddetails %}

{% exercice %}
Déduire de la question précédente un moyen de créer une matrice de $n$ lignes et $p$ colonnes d'entier en 1 opérations.

Comment accéder à l'élément de ligne $i$ et de colonne $j$ ?
{% endexercice %}
{% details "corrigé" %}

On crée un tableau de $n\cdot p$ entiers en 1 opération puis on y accède via la bijection $f$ définie précédemment.
{% enddetails %}
{% exercice %}
Comment généraliser ceci à une matrice de dimension supérieure ?
{% endexercice %}
{% details "corrigé" %}

<div>
$$
f(c_1, \dots, c_k) = \sum_{1\leq i < k} (c_i - 1) \prod_{i < j}d_j + (c_k-1)
$$
</div>

Est une bijection de l'ensemble des $k$-uplets $(c_1, \dots, c_k)$ avec $1\leq c_i \leq d_i$ dans l'intervalle $[0, \Pi_{i}d_i[$. Prouvons le.

Comme :

<div>
$$
\begin{array}{lcl}
\sum_{2\leq i < k} (c_i - 1) \prod_{i < j}d_j + (c_k-1) &\leq & \sum_{2\leq i < k} (d_i - 1) \prod_{i < j}d_j + (d_k-1)\\
&\leq & \sum_{2\leq i \leq k} \prod_{i \leq j}d_j - \sum_{2\leq i < k} \prod_{i < j}d_j -1\\
&\leq &  \sum_{2\leq i \leq k} \prod_{i \leq j}d_j - \sum_{3\leq i \leq k} \prod_{i \leq j}d_j -1\\
&\leq&  \prod_{2 \leq j}d_j -1\\
&<&  \prod_{2 \leq j}d_j
\end{array}
$$
</div>

On a que $c_1 - 1 = f(c_1, \dots, c_k) \\\;\mbox{ div } \prod_{1 < j}d_j$ et on peut itérer le processus pour obtenir les autres composantes.

En posant :

- $K_1 = f(c_1, \dots, c_k)$
- $K_{i+1} = K_i \mathbin{\small\\%} \prod_{i < j}d_j$

On a $c_i = K_i \\\;\mbox{ div } \prod_{i < j}d_j$

{% enddetails %}
