---
layout: layout/post.njk

title:  "sujet Test 3 : complexité"
---

{% attention %}
Vous avez 15min pour faire le test.
{% endattention %}

## Rendu

### Type de rendu

Rendu sur feuille.

### Éléments de notation

1. Écriture sous la forme d'un pseudo-code correct
2. Lorsque l'on vous demande de donner un algorithme il faudra toujours, en plus de son pseudo-code, prouver :
   - sa finitude
   - son exactitude

Ne tartinez pas des pages et des pages de démonstration. Allez directement au fait et si c'est évident, dites le.

## Sujet

### 1 un algorithme de multiplication

```pseudocode
programme mul(x: entier, y: entier) → entier:
    r ← 0
    tant que x ≠ 0:
        si x est impair:
            x ← x - 1
            r ← r + y
        x ← x / 2
        y ← y * 2
    
    rendre r
```

#### 1.1

Montrer que le programme `mul`{.language-} est un algorithme.

#### 1.2

Donnez la complexité de l'algorithme `mul`{.language-} en fonction de `x`{.language-}.

#### 1.3

Démontrez que `mul(x, y) = x * y`{.language-}.

### 2 représentation binaire des nombres

Dans le calcul de la complexité précédent on a considéré, comme toujours, que la multiplication de deux entiers est effectuée en une opération et que le stockage d'un entier ne prend qu'une case mémoire. C'est le cas lorsque les entiers considérés sont bornés ce qui est habituellement le cas (ils sont codés sur 64 bits et permettent de stocker des entiers de 0 à $2^{64}-1$) mais supposons ici que nous pouvons avoir des entiers aussi grand que l'on veut.

Pour cela on code un entier $n$ par un tableau $T$ de bits (0 ou 1) tel que :

<div>
$$
n = \sum_{0\leq i < T.\mbox{\tiny longueur}}2^i\cdot T[i]
$$
</div>

#### 2.1

Comment savoir si l'entier $n$ représenté par un tableau de bits $T_n$ est pair ?

#### 2.2

```pseudocode
algorithme mul2(T: [bit]):
    pour chaque i de [1, T.longueur - 1]:
        T[i] ← T[i-1]
    T[0] ← 0
```

##### 2.2.1

Quel est la complexité de l'algorithme `mul2(T: [bit])`{.language-} ?

##### 2.2.2

Montrez en quelques mots que l'algorithme `mul2(T: [bit])`{.language-} permet de multiplier par deux **en place** (en modifiant le tableau) un entier représenté par $T$ si $T[-1] = 0$.

##### 2.3

Donnez un algorithme `div2(T: [bit])`{.language-} ainsi que sa complexité permettant de diviser par deux **en place** (en modifiant le tableau) un entier représenté par $T$ si $T[0] = 0$.

#### 2.4

Si les tableaux $T_x$ et $T_y$ représentant respectivement deux entiers `x`{.language-} et `y`{.language-} sont tels que $T_x[-1] = T_y[-1] = 1$, quelle est la taille du tableau représentant l'entier $x\cdot y$ ?

### 3 adaptation de l'algorithme

#### 3.1

Modifiez l'algorithme `mul(x: entier, y: entier) → entier`{.language-} de la question 1 pour qu'il soit de signature : `mul(Tx: [bit], Ty: [bit]) → [bit]`{.language-}

#### 3.2

Déduire des questions précédentes la complexité de ce nouvel algorithme par rapport à `Tx.longueur`{.language-} et `Ty.longueur`{.language-}.

<!--

> TBD faire addition et soustraction binaire in place avant ça.

### 4 Pour aller plus loin un autre algorithme

> TBD add en log n
> TBD soustraction et division : <https://leria-info.univ-angers.fr/~jeanmichel.richer/ensl1i_base_de_l_info_1_sub_div.php>
> TBD mul plus long c;est pour ça qu'on considère plus gros.
> TBD si taille fixe ok.
>
> TBD avons nous eu raison de choisir 1 et 1 pour mul et 1

### 5 Pour aller plus loin un autre algorithme

> TBD Kolmogorov et Karatsuba.
>
> TBD pour aller plus loin et en faire un long exo
> TBD <https://en.wikipedia.org/wiki/Karatsuba_algorithm>
>
> TBD pour ne pas conclure on ne sais pas jusqu'ou on peut aller. 

-->
