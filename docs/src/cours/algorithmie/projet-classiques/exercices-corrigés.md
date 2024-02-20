---
layout: layout/post.njk

title: Corrigé

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Récursion et complexité

On considère le code suivant :

```python
def ma_fonction(n):
    if n < 5:
        return 2
    return ma_function(n-1) + ma_fonction(n-4)
```

### Complexité de l'algorithme

En notant $C(n)$ la complexité de la fonction, on a l'équation de récurrence suivante :

<div>
$$
C(n) = \mathcal{O}(1) + C(n-1) + C(n-4)
$$
</div>

Et la condition limite : $C(n) = \mathcal{O}(1)$ pour $n < 5$.

L'équation montre alors clairement que :

<div>
$$
\mathcal{O}(1) + C(n-4) + C(n-4) \leq C(n) \leq \mathcal{O}(1) + C(n-1) + C(n-1)= \mathcal{O}(1) + 2 \cdot C(n-1)
$$
</div>

Ce qui donne :

<div>
$$
K \cdot \mathcal{O}(1) + 2^K \cdot C(n-4\cdot K) \leq C(n) \leq K \cdot \mathcal{O}(1) + 2^K \cdot C(n-K)
$$
</div>

Et donc que $C(n) = \Omega(2^n)$.

### Version itérative

```python
def ma_fonction(n):
    C = [2, 2, 2, 2]
    for i in range(4, n):
        C = [C[0] + C[-1]] + C[:-1]

    return C[0]
```

La complexité est en $\mathcal{O}(n)$ car elle ne recalcule jamais deux fois la même chose.

## Tours de Hanoï

{% lien %}
[Tours de Hanoï sur Wikipédia](https://fr.wikipedia.org/wiki/Tours_de_Hano%C3%AF)
{% endlien %}

On suppose que l'on a les trois emplacements de tours A, B et C ; et que l'on veuille déplacer les disques de la tours A vers la tour C.

1. pour pouvoir déplacer le plus grand disque de la tour A, il faut avoir déplacé tous les disques au-dessus de lui. Comme c'est le plus grand disque, il est de plus seul sur son emplacement
2. une fois le plus grand disque seul sur sa tour, il faut le déplacer en C. Ceci n'est possible que si tous les autres disques sont en B. Il donc de plus qu'ils forment une tour
3. une fois le plus grand disque à sa place, il convient de déplacer la tour formée des autres disques, en B, sur l'emplacement C.

Donc si on possède un algorithme optimal, disons `hanoï(départ, arrivée, intermédiaire, n-1)`{.language-} pour une tour de taille $n-1$, alors l'algorithme optimal pour déplacer une tour de taille $n$ de A à C sera :

1. `hanoï(A, B, C, n-1)`{.language-}
2. déplace le disque restant en A sur l'emplacement C
3. `hanoï(B, C, A, n-1)`{.language-}

On obtient alors l'algorithme optimal suivant, en considérant que les tours sont des listes :

```python
A = list(range(5, -1, -1))
B = []
C = []

def hanoi(départ, arrivée, intermédiaire, n):
    if n == 0:
        return
    hanoi(départ, intermédiaire, arrivée, n-1)
    disque = départ.pop()
    arrivée.append(disque)
    print(A, B, C)
    hanoi(intermédiaire, arrivée, départ, n-1)

print(A, B, C)
hanoi(A, C, B, len(A))
```

On a montré que notre stratégie était optimale. Comptons le nombre d'appels récursif. Il suit l'équation de récurrence :

<div>
$$
C(n) = 2 + C(n-1) + C(n-1) = 2 + 2\cdot C(n-1)
$$
</div>

Et la terminaison : $C(0) = 0$

On obtient facilement l'expression, pour $n\geq 1$ :

<div>
$$
C(n) = \sum_{i=1}^n2^i + 2\cdot C(0) = \sum_{i=1}^n2^i
$$
</div>

La somme des $n>0$ premières puissances de 2 est à savoir facilement retrouver (c'est [une série géométrique](https://fr.wikipedia.org/wiki/S%C3%A9rie_g%C3%A9om%C3%A9trique#Terme_g%C3%A9n%C3%A9ral)) et vaut $2^{n+1}-2$.

## Polynômes

L'exercice portait sur la structure de [polynômes](https://fr.wikipedia.org/wiki/Polyn%C3%B4me).

Un polynôme est défini mathématiquement par la fonction :

$$
P(x) = \sum_{i=0}^n a_i x^i
$$

Et informatiquement par une liste à $n+1$ éléments.

$$
[a_0, \dots, a_n]
$$

### $P(x) + Q(x)$

```python
def somme(coefficients1, coefficients2):
    longueur1 = len(coefficients1)
    longueur2 = len(coefficients2)

    résultat = []
    for i in range(max(longueur1, longueur2)):
        résultat.append(0)

    for i in range(longueur1):
        résultat[i] += coefficients1[i]
    for i in range(longueur2):
        résultat[i] += coefficients2[i]

    return résultat

```

### $P(x) \cdot Q(x)$

```python
def produit(coefficients1, coefficients2):
    longueur1 = len(coefficients1)
    longueur2 = len(coefficients2)

    résultat = []

    for k in range(longueur1 + longueur2 - 1):
        i = min(longueur1 - 1, k)
        j = max(k - i, 0)

        valeur_k = 0
        while (i >= 0) and (j < longueur2):
            valeur_k += coefficients1[i] * coefficients2[j]
            i -= 1
            j += 1
        résultat.append(valeur_k)

    return résultat

```

### $P(A)$

```python
def valeur(coefficients, x):
    résultat = 0

    for i in range(len(coefficients)):
        résultat += coefficients[i] * x ** i
    return résultat

```

En utilisant l'exponentiation rapide, le calcul de $x^i$ prend $\log(i)$ multiplications. On effectue donc au total de l'ordre $n\log(n)$ multiplications pour calculer tous les $x^i$, $0 \leq i \leq n$.

### Méthode de Horner

L'optimisation proposée est dite [de Horner](https://fr.wikipedia.org/wiki/M%C3%A9thode_de_Ruffini-Horner#Valeur_d'un_polyn%C3%B4me_en_un_point). Comme beaucoup d'optimisation, elle cherche à ne pas recalculer plein de fois la même chose, ici $x^i$ dans le calcul de $x^k$ lorsque $i < j$.

En utilisant l'optimisation de Horner, on effectue au total de l'ordre $n$ multiplications pour calculer tous les $x^i$, $0 \leq i \leq n$.
i

```python
def evaluation(P, v):
    eval = P[-1]

    for i in range(len(P) - 2, -1, -1):
        eval = P[i] + v * eval

    return eval
```

## Suppression de valeurs

La structure de donnée utilisée ici est la **_liste_**. On considérera que :

- la création d'une liste vide se fait en $\mathcal{O}(1)$ opérations,
- l'ajout d'un élément en fin de liste se fait en $\mathcal{O}(1)$ opérations,
- lire un élément d'une liste se fait en $\mathcal{O}(1)$ opérations.

### Suppression d'une valeur

```text
Nom : Algorithme-1
Entrées :
    val : une valeur
    L : une liste de n valeurs
Programme :
    création d’une liste L2 vide
    pour chaque élément x de L :
        si x ≠ val :
            ajoute x à la fin de L2
    Retour L2
```

#### complexité

On considère que la création d'une liste et l'ajout d'un élément en fin de liste sont des opérations en $\mathcal{O}(1)$ opérations. De là, notre algorithme est en $\mathcal{O}(n)$ opérations où $n$ st la taille de la liste `L`{.language-}.

#### preuve

L'algorithme va parcourir la liste et ajouter un à un à L2 tous les éléments de `L`{.language-} différents de `val`{.language-}. Notre invariant de boucle pourrait donc être : à la fin de l'itération $i$ L2 est la restriction de `L[:i]`{.language-} aux valeurs différentes de `val`{.language-}.

- **initialisation** : à la fin de la première itération ($i=1$), `L2`{.language-} est vide si `x = L[0]`{.language-} vaut `val`{.language-} et vaut `[x]`{.language-} sinon. Ok.
- **récurrence** : On suppose la propriété vraie à la fin de l'itération $i$. L'itération $i+1$ a considéré $x = L[i]$. Notons `L2'`{.language-} la valeur de `L2`{.language-} à la fin de l'itération $i+1$. Au début de l'itération $i+1$, par hypothèse de récurrence, `L2`{.language-} est la restriction de `L[:i]`{.language-} aux valeurs différentes de `val`{.language-}. La restriction de `L[:i+1]`{.language-} aux valeurs différentes de `val`{.language-} est alors soit égal à `L2`{.language-} si `L[i] = val`{.language-} soit `L2 + L[i]`{.language-} sinon. C'est exactement ce que vaut `L2'`{.language-}.

A la fin de la dernière itération, `L2`{.language-} vaut donc la restriction de `L[:n]`{.language-} (avec `n = len(L)`{.language-}) aux valeurs différentes de val.

### Suppression d'une valeur in-place

> TBD

On échange l'élément à supprimer avec le dernier de la liste puis on pop.

## Suppression de doublons

Même structure que pour l'exercice précédent.

La structure de donnée utilisée ici est la **_liste_**. On considérera que :

- la création d'une liste vide se fait en $\mathcal{O}(1)$ opérations,
- l'ajout d'un élément en fin de liste se fait en $\mathcal{O}(1)$ opérations,
- lire un élément d'une liste se fait en $\mathcal{O}(1)$ opérations.

### Suppression de doublon en conservant l'ordre

```text
Nom : Algorithme-2
Entrées :
    L : une liste de n valeurs
Programme :
    création d’une liste L2 vide
    tant que L est non vide:
        x = L[0]
        ajoute x à la fin de L2
        L = algorithme-1(L, x)
    Retour L2
```

#### complexité algorithme 2

Commençons par compter le nombre de fois où la boucle `tant que`{.language-} sera exécutée. `L`{.language-} est modifiée à chaque fin de boucle `L = algorithme-1(L, x)`{.language-} avec `x = L[0]`{.language-}. Comme l'algorithme de la question 1 rend la restriction de de `L`{.language-} aux valeurs différentes de `x`{.language-}, elle va forcément être strictement plus petite (puisque `x=L[0]`{.language-} il est forcément dans la liste) : la longueur de la liste diminue strictement à chaque itération, on ne peut y rentrer que la longueur de `L`{.language-} initiale fois.

La seule ligne de l'algorithme qui n'est pas de complexité $\mathcal{O}(1)$ est : `L = algorithme-1(L, x)`{.language-}. Sa complexité est égale à une affectation ($\mathcal{O}(1)$) plus la complexité de l'algorithme de la question 1, qui vaut de l'ordre de la taille de la liste passée en entrée.

Cette taille diminue strictement à chaque itération : on peut utiliser l'astuce du cours pour ne garder que la complexité la plus importante, c'est à dire $\mathcal{O}(len(L))$ avec `L`{.language-} la liste initiale.

Notre complexité est donc de l'ordre : $\mathcal{O}(1) + A * (\mathcal{O}(1) + B)$ où :

- A est le nombre de fois où l'on rentre dans la boucle tant que : $\mathcal{O}(len(L))$
- B est la complexité maximale de l'algorithme de la question 1 : $\mathcal{O}(len(L))$

Notre algorithme est de complexité : $\mathcal{O}(len(L)^2)$

#### preuve algorithme 2

La liste `L`{.language-} contient $k$ valeurs différentes que l'on note $v_1, \dots v_k$ dans l'ordre de la liste (le 1er indice où l'on rencontre $v_i$ est strictement plus petit que le 1er indice où l'on rencontre $v_j$ si $i < j$).

Notre invariant de boucle sera : au bout de la $i$ème itération :

- $L2 = [v_1, \dots, v_i]$.
- `L`{.language-} vaut la restriction de `L`{.language-} initiale aux valeurs différentes de $v_1$ jusqu'à $v_i$.

- **initialisation** : comme $v_1= L[0]$ notre invariant est vrai puisque l'algorithme 1 rendra la restriction de `L`{.language-} initiale aux éléments différents de $v_1$.
- **récurrence** : On suppose la propriété vraie à la fin de l'itération $i$. Au début de l'itération $i+1$, on a par hypothèse de récurrence que $L2 = [v_1, \dots, v_i]$ et que `L`{.language-} vaut la restriction de la liste `L`{.language-} initiale aux valeurs différentes de $v_1$ jusqu'à $v_i$. Donc $L[0] = v_{i+1}$ et tout se passe comme à la 1ère itération.

A la fin de l'algorithme, notre invariant est toujours juste : $L2 = [v_1, \dots, v_k]$

### Suppression de doublon d'une liste ordonnée

> TBD : on ajoute l'élément que s'il est différent de celui d'avant

### Suppression de doublon d'une liste sans ordre

> TBD

On commence par trier puis on supprime

## Min et max d'un tableau d'entiers

> TBD

Si on fait les deux à la suite on a 2n comparaisons.

On commence par trier les éléments $T[i]$ et $T[i+1]$ pour tout $i$ ($n/2$ comparaisons)

Puis on cherche le min sur les $T[[2i]$ ($n/2$ comparaisons) et le max sur les $T[[2i +1]$ ($n/2$ comparaisons)

## Suite de Fibonacci

### Récursif

```python

def fibo_rec_1(n):
    if n <= 2:
        return 1
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)
```

### Itératif

```python
def fibo_iter(n):
    a = 1
    b = 1
    for i in rang(n):
        a, b = a+b, a
    return a
```

### Récursif terminal

```python
def fibo_rec2(n, a=1, b=1):
    if n <= 1:
        return a
    else:
        return fibo_rec2(n-1, a+b, a)
```

## Triangle de Pascal

Pour $n > p > 0$ :

<div>
$$
C(n, p) = C(n-1, p-1) + C(n-1, p)
$$
</div>

et $C(n, 1) = C(n, n) = 1$

### Récursif

```python
def comb_rec(n, p):

    if p <= 1 or n ==p :
        return 1
    else:
        return comb_rec(n-1, p-1) + comb_rec(n-1, k)
```

### Itératif et $\mathcal{O}(n^2)$ en mémoire

On stocke une matrice triangulaire inférieure. C

```python
def comb_iter(n, p):
    C = [[1]]

    for i in range(1, n):
        C.append([])
        for j in range(i):
            c_i_j = C[i-1][j-1] + C[i-1][j]
            C[-1].append(c_i_j)

    return C[-1][p-1]
```

### Itératif et $\mathcal{O}(n)$ en mémoire

On remarque que seule la dernière ligne est importante dans le calcul.

```python
def comb_iter2(n, p):
    C = [1]
    for i in range(1, n):
        C.append(0)
        r = C[0]
        for j in range(1, i):
            tempo = C[j]
            C[j] += r
            r = tempo

    return C[p-1]
```

> TBD : un dessin

## Ackermann

La fonction d'Ackermann se définit de la manière suivante, pour tous entiers $m$ et $n$ positifs :

<div>
$$
A(m,n) =
\left\{
\begin{array}{lll}
 & n + 1 &\mbox{ si } m = 0\\
& A(m - 1, 1) &\mbox{ si } n = 0, m>0\\
& A(m - 1, A(m, n - 1)) &\mbox{ sinon }\\
\end{array}
\right.
$$
</div>
    
- Donnez un pseudo-code récursif et itératif de cette fonction.
- Donnez le nombres d'appels récursif du calcul de A(n, n).

> TBD calculs de A(m, n) avec les puissances itérées de Knuth.

## Méthodes de tri

### Tri par base

Ce tri s'applique uniquement aux entiers positifs, que l'on considère écrits en base 2. Le principe de ce tri est très simple :

- On considère d'abord le bit de poids le plus faible (_ie._ le plus à droite) et on répartit l'ensemble à trier en deux sous ensembles :
  - les entiers dont le bit de poids le plus faible est 0
  - les entiers dont le bit de poids le plus faible est 1
- On concatène les deux sous-ensembles, en commençant par celui des bits à 0.
- On recommence sur le bit à gauche de celui qu'on vient de traiter.
- ...

Les parcours d'ensembles se font, toujours, de la gauche vers la droite.

Donnez le pseudo-code, la preuve et la complexité de cet algorithme (on supposera que l'on dispose d'une fonction qui, étant donnés deux entiers $n$ et $i$, donne le $i^{me}$ bit de $n$).

Rappelez la complexité minimale du tri (dans le cas le pire). Commentaires.

### Tri par monotonies

Étant donné un tableau $T$, **_une monotonie_** est une suite croissante maximale d'éléments consécutifs de $T$. Par exemple :
si $T = [2,6, 1,3, 3, 5,2,6, 4,0, 1,8,9,1,3, 2,0,1,0]$, alors $[2,6]$, $[1,3,3,5]$, $[2,6]$, $[4]$, $[0, 1,8,9]$, $[1,3]$, $[2]$, $[0,1]$ et $[0]$ sont les monotonies de $T$.

Donnez un algorithme qui, étant donné un tableau $T$ construit une liste (de listes) $L$, chaque élément de $L$ étant une monotonie de $T$ (et vice versa). À partir de notre exemple, on obtient :
$L = [[2,6], [1,3,3,5],[2,6], [4], [0, 1,8,9], [1,3], [2] ,[0,1], [0]]$.

Donnez un algorithme qui fusionne deux monotonies ; par exemple, à partir de $[2,6]$ et $[1,3,3,5]$, on obtient $[1,2,3,3,5,6]$ (ceci est aussi une question de cours).

Donnez un algorithme qui, étant donnée une liste $L$ de monotonies, les fusionne deux-à-deux (en en laissant éventuellement une ``toute seule" à la fin) et met le résultat dans une liste (de listes) $L'$. Par exemple, à partir de
$L = [[2,6], [1,3,3,5],[2,6], [4], [0, 1,8,9], [1,3], [2] ,[0,1], [0]]$, on obtient $L' = [[1,2,3,3,5,6], [2,4,6],[0,1,1,3,8,9], [0,1,2], [0]]$.

En déduire un algorithme de tri. Donnez sa complexité dans le cas le meilleur et dans le cas
le pire.

Cet algorithme est en fait une variante d'un algorithme vu en cours. Lequel ?

## Compteur binaire

- suivant
- tous

> TBD. Avec calcul de complexité naif et exact.

## Jets de dés

- algorithme itératif (généralisation du compteur binaire)
- algorithme récursif. Complexité en mémoire ?

On considère l'algorithme suivant:

```python
def LaFonction (L, n):
    if n == 0:
        print(L)
    else:
        for i in range(6):
            LaFonction(L + [i + 1], n -  1)

```

On rappelle que, appliqué à des listes, le $+$ est la concaténation. On supposera que l'appel initial se fait avec la liste L vide. Que fait cet algorithme ? Quelle est sa complexité ? Quelle place mémoire consomme-t-il ?

## Chaînes de caractères

### Sous-séquence

Soient deux chaînes de caractères $S_1$ et $S_2$. On dit que $S_2$ est une {\em sous-séquence} de $S_1$ si il existe une fonction strictement croissante

$$
f : \{0,\ldots, len(S_2)-1\} \longrightarrow \{0,\ldots, len(S_1)-1\}
$$

Telle que $S_1[f(j)] = S_2[ j]$ pour tout $j$ de $\{0,\ldots, len(S_2)-1\}$.

Proposez, prouvez et donnez la complexité d'un algorithme qui détermine si $S_2$ est une sous-séquence de $S_1$.

### Sous-mot

Soient deux chaînes de caractères $S_1$ et $S_2$. On dit que $S_2$ est un **_sous-mot_** de $S_1$ s'il existe un indice $i$ tel que $S_2[j] = S_1[i + j]$ pour tout $j$ de $0$ à $len(S_2) - 1$.

- Proposez, prouver et donner la complexité d'un algorithme qui détermine si $S_2$ est un sous-mot de $S_1$.
- Si toutes les lettres de $S_2$ sont deux à deux différentes, donnez un algorithme en $\mathcal{O}(len(S_1))$ pour résoudre ce problème.

## Algorithme mystère

L'algorithme suivant, à partir d'une liste d'entiers positifs, rend une autre liste. On suppose pour cet exercice que la création des deux listes tempo et sortie est en $\mathcal{O}(1)$ opérations.

```python
def mystère(tab):
    k = max(tab)
    tempo = [0] * (k + 1)
    sortie = [0] * len(tab)

    for i in range(len(tab)):
        tempo[tab[i]] += 1
    for i in range(1, k + 1):
        tempo[i] += tempo[i - 1]

    for i in range(n):
        sortie[i] = tempo[tab[i]] - 1
        tempo[tab[i]] -= 1

    return sortie

```

- Donnez la complexité de cet algorithme.
- Dites ce qu'il fait et prouvez le (_indication_: après chacune des deux premières boucles, que contient tempo ?).
- Commentaires ?

## Cols

- d'une liste (max ou min local). Trouver un algorithme en log
- d'une matrice (min ligne et max colonne) avec un algorithme linéaire en la taille de la matrice (pourquoi le log ne marche-t-il pas ?)

## Permutation circulaire

Étant donné un liste $L$ de longueur $n$ et un entier $k$, le problème est de transformer $L$ par permutation circulaire en décalant (circulairement) tous les éléments de $L$ de $k$ places. Par exemple, avec $L = \text{LongtempsJeMeSuisCouchéDeBonneHeure}$ et $k = 4$, on obtient $L' = \text{eureLongtempsJeMeSuisCouchéDeBonneH}$.

- Donnez un algorithme $\text{Permut}(L, k)$ qui, avec une liste $L$ et un entier $k$ en entrées, construit une nouvelle liste $L'$, permutation circulaire de $L$.
- Si on veut transformer $L$ en $\text{Permut}(L,k)$, montrez que la place mémoire utilisée (en plus de celle des données du problème ($L$)) par votre algorithme est $O(n)$.

On veut maintenant faire une permutation circulaire sur site, _ie._ sans utiliser plus que $O(1)$ place mémoire supplémentaire (il arrive (par exemple quand on étudie le génome) que $n$ soit très grand). Il faut pour cela
remarquer que permuter circulairement $L$ revient à prendre les $k$ dernières lettres de $L$ et à les mettre en tête. On note $L^R$ la liste $L$ **_renversée_** (par exemple, si $L =\text{Couché}$, $L^R = \text{éhcuoC}$).

- Donnez un algorithme en $O(n)$ et utilisant $O(1)$ place mémoire supplémentaire, qui transforme $L$ en $L^R$.
- Montrez que, si on note $L = AB$, où $B$ est de longueur $k$ (par exemple, avec $L = \text{LongtempsJeMeSuisCouchéDeBonneHeure}$ et $k = 4$, $A =\text{LongtempsJeMeSuisCouchéDeBonneH}$ et $B =\text{eure}), alors \text{Permut}(L, k) = (A^RB^R)^R$.
- Déduisez-en un algorithme de complexité $O(n)$ qui permute une liste (de longueur $n$), _ie._ qui transforme $L$ en $\text{Permut}(L,k)$, en utilisant $O(1)$ espace mémoire supplémentaire.

## Algorithmes arithmétique

- addition de listes de chiffres
- multiplications de listes de chiffres

(- [optimisation de Karastuba](https://fr.wikipedia.org/wiki/Algorithme_de_Karatsuba))

## Matrices

- structure
- addition
- produit par un scalaire
- produit naïf

(- [produit de Strassen](https://fr.wikipedia.org/wiki/Algorithme_de_Strassen)}
