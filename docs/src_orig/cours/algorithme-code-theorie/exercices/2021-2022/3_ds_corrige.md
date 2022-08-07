---
layout: page
title:  "DS"
category: cours
tags: informatique cours 
authors: "François Brucker"
---

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [exercices]({% link cours/algorithme-code-theorie/exercices/index.md %}) / [2021-2022]({% link cours/algorithme-code-theorie/exercices/2021-2022/index.md %}) / [sucorrigéjet DS]({% link cours/algorithme-code-theorie/exercices/2021-2022/3_ds_corrige.md %})
{.chemin}

## Introduction

> ventilation des notes
>
{.tbd}

### remarques

* les 3 exercices doivent être faisable en 2h.
* optimisez votre temps. Si vous bloquez passez à un autre exercice. Les premières questions sont souvent plus faisables que les dernières (Si vous prenez une copie par exercice cela permet de revenir à une exercice plus tard sans perdre le correcteur)

### erreurs communes

1. question 1
   * 1.1 rogntujdu ! Les 3 qui sont tout aussi importants l'un que l'autre. Seuls 2 personnes ont eu juste.
   * 1.2.2 : peu de bonnes solutions. On démontre en >2 temps :
     1. on prouve une borne minium
     2. on montre qu'elle est atteinte pour un algorithme qu'on exhibe.
2. question 2
   * votre algorithme de retournement fait souvent identité (il retourne 2 fois et fait donc un virage à 360 degrés). Il faut s'arrêter à la moitié.
   * il y a 2 paramètres à l'algorithme de retournement : la liste et la position de la spatule
3. question 3
   * `T[T[0]], T[0] = T[0], T[T[0]]` et pas le contraire. C'est une erreur subtile que je n'ai pas compté. C'est que l'écriture ne se fais pas en même temps. n commence par celui de gauche.

## Question 1

### 1.1

Les **trois** parties sont tout aussi importantes les unes que les autres !

1. sans programme principal, ça ne sert à rien de coder. En revanche, un programme principal ne fait rien sans les fonctions
2. sans fonctions, le programme ne fait rien. En revanche, on ne sait pas si les fonctions sont sans erreurs sans les tests
3. un test n'a d'intérêt que si la fonction est utilisée pour autre chose. En revanche on ne sait pas si le code est sans erreur sans les tests

### 1.2

#### 1.2.1

* la complexité maximale d'un algorithme est le nombre maximum d'opérations dont aura besoin l'algorithme pour se terminer pour une entrée de taille donnée
* la complexité minimale d'un algorithme est le nombre minimum d'opérations dont aura besoin l'algorithme pour se terminer pour une entrée de taille donnée
* la complexité en moyenne d'un algorithme est le nombre moyenne d'opérations dont aura besoin l'algorithme pour se terminer pour toutes les entrées d'une taille donnée
* la complexité d'un problème est le minimum de la complexité maximale pour tous les algorithmes le résolvant

#### 1.2.2

Pour connaitre la complexité du problème du tri, on procède en 2 temps :

1. on cherche une borne minimum de complexité (maximale) pour tout algorithme résolvant le problème du tri
2. on exhibe un algorithme ayant cette borne min comme complexité.

Un algorithme de tri devra, pour un tableau de taille $n$, distinguer parmi $n!$ cas (toutes les permutations possibles du tableau) pour rendre le tableau triée. Sa complexité sera donc au minimum de $\mathcal{O}(\ln(n!)) = \mathcal{O}(n\ln(n))$.

Comme le tri fusion vu en cours est de cette complexité on en déduit que la complexité du problème du tri d'un tableau de taille $n$ est en $\mathcal{O}(n\ln(n))$.

## Questions 2

Le [tri de crêpes](https://fr.wikipedia.org/wiki/Tri_de_cr%C3%AApes) est un problème originellement étudié par Bill Gates (oui, lui même) et Chritos Papadimitriou (un grand nom de l'informatique théorique) dans [un papier de decrete mathematics](https://www.sciencedirect.com/science/article/pii/0012365X79900682?via%3Dihub). Il y démontre une borne supérieure bien meilleure que celle que l'on vous fait calculer. Mais lisez ce papier, il est facile à comprendre.

### 2.1

Pour les $n$ crêpes, on peut les ordonner par taille de la plus petite à la plus grande. On peut donc associer à chaque crêpe son ordre - 1 dans cet ordre : les crêpes peuvent être vues comme un nombre entre 0 et $n-1$.

La pile de crêpes est alors un tableau $T$ de taille $n$, la plus haute en première position, chaque crêpe étant représenté par sa position moins 1 dans l'ordre des tailles. Ce tableau est une permutation de $[0 \mathrel{ {.}\,{.} } n-1]$

Ordonner les crêpes par taille est alors équivalent à ordonner le tableau $T$ par ordre croissant.

L'opération de retournement revient à retourner le début du tableau T.

### 2.2

Il faut 2 paramètres pour l'algorithme de retournement : la liste et la position de la spatule

```python
def retournement(T, spatule):
    T2 = []
    for i in range(spatule, -1, -1):
        T2.append(T[i])

    for i in range(spatule + 1, len(T)):
        T2.append(T[i])

    return T2
```

L'algorithme est constitué de deux boucles for, la première de $\mbox{spatule}+1$ itérations et la seconde de $\mid T \mid - \mbox{spatule}-1$ opérations. Toutes les autres opérations sont en $\mathcal{O}(1)$, l'algorithme s'arrête bien et est de complexité $\mathcal{O}(\mid T \mid)$.

La première boucle for effectue le retournement du tableau $T[:r+1]$, c'est à dire des $r+1$ premières crêpes de la pile (de l'indice 0 à $r$ inclus), la seconde ajoute dans le même ordre la fin de la pile. 

### 2.3

#### 2.3.1

Pour un tableau $T$, `retournement(T, r)` retourne les $r+1$ premiers éléments du tableau, et donc $T[r]$  avant l'opération de retournement se retrouve en $T[0]$ après le retournement. On peut donc placer n'importe quel élément de la pile en 1ère position.

De même l'élément en $T[0]$ avant retournement se retrouve en position $T[r]$ après le retournement `retournement(T, r)` : on peut placer l'élément d'indice 0 du tableau en n'importe quelle position en 1 opération de retournement.

#### 2.3.2

Comme les tailles sont des entiers de 0 à $n-1$, on connait le maximum du tableau. On a écrit le code de l'algorithme en python mais on aurait tout aussi bien pu l'écrire en pseudo-code

```python
def tri(T):
    n = len(T)
    for t in range(n-1, -1, -1):  #  de t=n-1 à t=0
        i = 0                     # trouve l'indice i tel que T[i] == t
        while T[i] != t:
            i += 1

        T = retournement(T, i)
        T = retournement(T, t)

    return T
```

1. complexité en nombre de retournements : $\mathcal{O}(n)$ itérations dans la boucle for, et deux retournements par itérations.
2. preuve de l'algorithme par invariant de boucle : *à la fin d'une itération de la boucle for, $T[i] = i$ pour tout $i \geq t$.*. Sa preuve est immédiate car elle découle de la question 2.3.1

##### 2.3.3

On note $n$ la taille de la liste.

On pourrait croire que notre algorithme de tri en $\mathcal{O}(n)$ retournement est inférieur à la complexité du tri qui est de $\mathcal{O}(n\ln(n))$ ($n < n \ln(n)$ si $n > e$).

Mais l'opération de retournement est en $\mathcal{O}(n)$ opérations. Donc notre algorithme de tri est en réalité en $\mathcal{O}(n^2)$ opérations, ce i est plus grand que la complexité du problème du tri. C'est cohérent.

### 2.4

#### 2.4.1

Notre algorithme est en $\mathcal{O}(\mid T \mid)$ retournement, c'est donc une borne maximum du problème du retournement de crêpes.

#### 2.4.2

1. une adjacence étant un un couple $(i, i+1)$ tel que $\mid T[i] - T[i+1] \mid > 1$,il faut que $0 \leq i < \mid T \mid -1 = n -1$
2. Si $(i-1, i)$ et $(i, i+1)$ sont deux adjacences, alors :
   1. prouvons $n-1$ adjacences implique trié.
      * soit $T[i-1] < T[i]$ et donc $T[i] = T[i-1] - 1$. De là on ne peut avoir $T[i] > T[i+1]$ car sinon $T[i+1] = T[i-1]$ ce qui est impossible. On a donc $T[i-1] < T[i] < T[i+1]$
      * soit $T[i-1] > T[i]$ et un raisonnement similaire au précédent nous permet de montrer que $T[i-1] > T[i] > T[i+1]$.

      Donc s'il y a $n-1$ adjacences, $T$ est trié par ordre croissant ou par ordre décroissant.
   2. réciproquement, si la liste est triée avec le plus grand élément à la fin, il y a bien $n-1$ adjacences.
3. un retournement `retournement(T, r)` ne peut changer les adjacences pour $i < r - 1$ (si (i, i+1) est une adjacence avant retournement, alors $(r-i-1, r-i)$  est une adjacence après retournement), et pour $i \geq r$. La seule adjacence qui peut être modifiée est $(r-1, r)$.
4. L'ordre $[n-2, n-4, \dots, (1\mbox{ ou }0\mbox{ selon la parité de }n), n-1, n-3, \dots, 0\mbox{ ou }1\mbox{ selon la parité de }n]$ a bien 0 adjacences et si $n \geq 4$.

Pour trier la pile il faut au moins autant de retournements que de paires non adjacentes plus 1 pour mettre l'élément $n-1$ en fin de liste qui est une opération qui ne change pas le nombre d'adjacences.

## Question 3

### 3.1

#### 3.1.1

```python
def echange(T):
    while T[0] != 0:
        a = T[0]
        T[a], T[0] = a, T[a]
```

#### 3.1.2

```python
[2, 1, 6, 7, 0, 4, 5, 3]
[6, 1, 2, 7, 0, 4, 5, 3]
[5, 1, 2, 7, 0, 4, 6, 3]
[4, 1, 2, 7, 0, 5, 6, 3]
[0, 1, 2, 7, 4, 5, 6, 3]
```

### 3.2

A la fin d'une itération de l'algorithme on a $a = T[a]$ avec $a \neq 0$. L'indice $a$ ne changera plus jamais tout au long de l'algorithme, donc $L(T)$ a un 1 de plus si $0 \neq T[0]$ à la fin de l'itération.

Lors de la dernière itération, comme $a= T[a]$ et $0 = T[0]$, $L(T)$ augmente de deux 1.

#### 3.3

Comme le nombre de 1 de $L(T)$ augmente strictement à chaque étape et qu'il ne peut y a voir que $n$ 1 à la fin : l'algorithme s'arrête bien au bout d'au pire $n$ itérations.

#### 3.4

```python
def tri(T):
    for i in range(len(T)):
        while T[i] != i:
            a = T[i]
            T[a], T[i] = a, T[a]
```

On ajoute une boucle qui parcours tous les éléments et qui fait les permutations si $T[i] \neq i$.

La complexité est bien en $\mathcal{O}(n)$ car à chaque itération de la boucle while $L(T)$ augmente strictement : on ne peut rentrer dans la boucle while qu'au pire $n$ fois.

#### 3.5

Ici on doit trier une permutation des n premiers entiers. C'est bien plus restrictif que le problème du tri où les éléments à trier peuvent avoir des égalités, et des éléments non consécutifs.

En fait, l'algorithme le plus simple qui trie les $n$ premiers entiers est :

```python

def tri(T):
    return list(range(len(T)))
```

Qui est bien en $\mathcal{O}(n)$...

Notre problème est un **sous-problème** du problème du tri et pas le problème général du tri : il peut admettre une complexité plus faible.
