---
layout: layout/post.njk
title: Pseudo-code

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

[La définition générale d'un algorithme](../bases-théoriques/définition){.interne} ne spécifie rien sur les instructions à utiliser, juste qu'elles doivent être décrites en un nombre fini de mots. Un **_pseudo-code_** est une proposition d'instructions possibles pour décrire un algorithme, compréhensibles par un humain.

Ce n'est cependant pas une langue car il n'y a pas de place pour l'ambiguïté ni l'invention : tout doit y être rigoureusement défini, et chaque étape élémentaire doit être réalisable en un temps fini par un humain :

{% info %}

Rappelez-vous les trois premières règles de la [définition d'un algorithme](../bases-théoriques/définition/#règles-générales){.interne} qui sont faciles à respecter.

{% endinfo %}

Ce n'est pas non plus un langage informatique dont le but est d'être compris par un ordinateur. Il est communément admis que tout algorithme peut être écrit en **_pseudo-code_** :

<span id="règles"></span>
{% note "**Définition**" %}
Un pseudo-code est une succession de lignes qui seront exécutées **_en séquence_** les unes à la suite des autres. Chaque ligne est composée d'une instruction qu'il faut réaliser avant de passer à la ligne suivante.
{% endnote %}

Avant de définir précisément le pseudo-code, notez la thèse (hypothèse) fondamentale de l'informatique :

{% note "**Thèse de Church-Turing**" %}

Tout programme (et donc algorithme) peut s'écrire sous la forme d'un pseudo-code (et réciproquement).

{% endnote %}
{% lien %}
[Thèse de Church-Turing](https://fr.wikipedia.org/wiki/Th%C3%A8se_de_Church).
{% endlien %}

La thèse de Church-Turing a été initialement formulée pour les Machines de Turing mais (nous le verrons bien plus tard) pseudo-code et machines de Turing sont deux notions équivalentes. Notez que cette affirmation n'est pas démontrée mais que toutes les tentatives (et il y en a eu) pour infirmer cette affirmation ont été des échecs.

## Pseudo-code et langages de programmation

Les langages de programmation classiques comme [python](https://www.python.org/), [java](https://www.java.com/fr/) ou encore [rust](https://www.rust-lang.org/fr) se transcrivent aisément en pseudo-code et réciproquement. Ce sont deux notions équivalentes :

- on utilisera le pseudo-code pour l'étude théorique des algorithmes
- on codera ces algorithme dans un langage dédié à être exécuté lorsque l'on voudra les tester. Dans le cadre de ce cours on utilisera le python.

## Éléments de pseudo-code

### Briques de base

Commençons par décrire la _grammaire de base_ du pseudo-code :

{% aller %}
[Briques de base](briques-de-base){.interne}
{% endaller %}

### Algorithmes en pseudo-code

Un programme et un algorithme doivent posséder des paramètres d'entrées
En pseudo-code, un algorithme est une suite d'instructions qui, a partir de paramètres d'entrée, rend une sortie. Considérons par exemple la description de  l'algorithme de recherche d'un élément dans une liste :

```text
Nom : recherche
Entrées :
    t : un tableau d'entiers
    x : un entier
Programme :
    parcourir chaque élément de t jusqu'à trouver un élément dont la valeur est égale à la valeur de x.
    Si on trouve un tel élément, rendre "Vrai"
    Sinon rendre "Faux"
```

En pseudo-code, cela va donner ça :

<div id="problème-recherche"></div>

```pseudocode
algorithme recherche(t: [entier],
                     x: entier     # entier recherché dans t
                    ) → booléen:   # Vrai si x est dans t

    pour chaque e de t:
        si e == x:
            rendre Vrai
    rendre Faux
```

Le programme est un bloc. La definition du bloc (jusqu'aux `:`{.language-}) est constitué :

1. du mot-clé `algorithme`{.language-} qui détermine la nature du bloc
2. suit le du nom du programme
3. puis ses paramètres d'entrées entre parenthèses. Chaque paramètre est décrit par son nom suivit de son type
4. enfin, le type de sortie de l'algorithme qu'on fait précéder d'une flèche.

Si on a besoin d'information supplémentaire pour qu'un lecteur puisse mieux comprendre le pseudo-code on peut ajouter des commentaires en les faisant commencer par un `#`{.languages-}.  Ne mettez pas trop de commentaires, normalement le pseudo-code et le nom des variables doit suffire. On a ici juste décrit ce que fait l'algorithme avec ses paramètres d'entrées.

{% lien %}
La description des types de paramètres est reprise du format python : <https://docs.python.org/fr/3.13/library/typing.html>
{% endlien %}

Terminons par un petit exercice :

<span id="algorithme-nombre-occurrences"></span>

{% exercice %}
Adaptez le pseudo code de l'algorithme `recherche((t: [entier], x: entier) → booléen)`{.language-} précédent pour créer l'algorithme :

```pseudocode
nombre((t: [entier], x: entier) → entier)
```

Cet algorithme  rend le nombre de fois où `x`{.language-} est présent dans `t`{.language-}
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme nombre(t: [entier], x: entier) → entier:
    nombre ← 0
    pour chaque e de t:
        si e == x:
            nombre ← nombre + 1
    rendre nombre
```

{% enddetails %}

### Fonctions

Un algorithme est constitué uniquement d'instructions de base. Mais rien n'empêche de réutiliser des algorithmes déjà écrit en les appelant par leur nom. Ces algorithmes intermédiaires sont appelées **_fonctions_**.

{% aller %}
[Fonctions](fonctions){.interne}
{% endaller %}

### <span id="type-matrice"></span>Matrice

Terminons cette partie en montrant que l'on peut facilement créer des matrices uniquement avec des tableaux. Ce type est tellement utilisé en algorithme qu'on le considérera souvent comme un type de base.

{% note "**À retenir**" %}

Une matrice de dimension $k$ est constitué d'un tableau de matrices de dimensions $k-1$
{% endnote %}

Une matrice entière $M$ de $n$ lignes et $p$ colonnes sera constitué d'un tableau de $n$ lignes (un tableau de $p$ entiers).

#### Type

Une matrice d'entiers en deux dimensions sera ainsi un tableau de tableaux, donc de type :

```pseudocode
M: [[entier]]
```

#### Création

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

#### Utilisation

Une fois la matrice créée, il est facile de lire et écrire un élément. Par exemple pour affecter puis afficher à l'écran l'élément de ligne $i$ et de colonne $j$ de la matrice $M$ :

```pseudocode
x ← un entier entré par l'utilisateur
M[i][j] ← x
Affiche à l'écran M[i][j]
```

Cette utilisation nous permettra d'étendre aux matrice les _abus_ classique des tranches de tableaux. Ainsi `M[a:b][c:d]` correspondra à une sous matrice de $M$ allant des colonnes d'indice `c`{.language-} à `d-1`{.language-} pour les lignes allant de l'indice `a`{.language-} à `b-1`{.language-}.

#### Généralisation

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

#### Nombre d'opérations élémentaires

La méthode de création présenté nécessite une boucle, ce n'est donc pas une opération élémentaire.

Il faut par exemple $n$ opérations pour créer une matrice de $n$ lignes et $p$ colonnes.
Ceci n'est souvent pas gênant algorithmiquement car si on utilise une matrice c'est pour utiliser toutes ses lignes et colonnes, ne serait-ce que pour les initialiser (rappelez vous que lorsque l'on crée un tableau ses valeurs sont indéterminées).

Mais si l'on veut pouvoir créer des matrices en 1 unique opération on peut le faire comme le montre la série d'exercice suivant. On utilise cependant peu cette méthode algorithmiquement car son utilisation complexifie (souvent inutilement) l'algorithme.

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
f^{-1}(k) = ((k \div n) + 1, (k \mod n) + 1)
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

On a que $c_1 - 1 = f(c_1, \dots, c_k) \div \prod_{1 < j}d_j$ et on peut itérer le processus pour obtenir les autres composantes.

En posant :

- $K_1 = f(c_1, \dots, c_k)$
- $K_{i+1} = K_i \mod \prod_{i < j}d_j$

On a $c_i = K_i \div \prod_{i < j}d_j$

{% enddetails %}

## Écrire du bon pseudo-code

Un bon pseudo-code doit être compréhensible en tant que tel, sans commentaires.

Pour cela il faut :

- expliciter la signature de vos algorithme
- utiliser des noms de variables ou de fonctions explicites et utile à la compréhension
- séparer les différentes parties d'un algorithmes en fonctions au nom explicite.

Leurs noms importent peu, seuls leurs fonctions sont importantes. Vous pouvez donc utiliser les mots qui vous plaisent, du moment qu'ils sont compréhensible pour vous et — surtout — pour votre lecteur. Le plus souvent, on utilisera un mix de python et de français, ou d'anglais.
