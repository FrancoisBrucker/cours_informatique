---
layout: page
title:  "DS"
category: cours
tags: informatique cours 
authors: "François Brucker"
---

>
> 1. cours où on ne connait pas la complexité max la plus faible. La borne est gigantesque, alors que la moyenne est toute simple.
>
{: .tbd}

* optimisez votre temps. Si vous bloquez passez à un autre exercice.
* les sujets de concours ne sont pas fait pour être fini.

## Introduction

Erreurs communes :

1. question 1
   * 1.1 rahhhh. C'est les 3 qui sont tout aussi importants. Seuls 2 personnes ont eu juste.
   * 1.2.2 : peut de bonne solution. Borne min puis borne atteinte
2. question 2
   * votre algorithme de retournement fait identité. Il faut s'arrêter à la moitié.

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

```python
def retournement(T, r):
    T2 = []
    for i in range(r, -1, -1):
        T2.append(T[i])

    for i in range(r+1, len(T)):
        T2.append(T[i])

    return T2
```

L'algorithme est constitué de deux boucles for, la première de $r+1$ itérations et la seconde de $\mid T \mid - r-1$ opérations. Toutes les autres opérationÒ sont en $\mathcal{O}(1)$, l'algorithme s'arrête bien et est de complexité $\mathcal{O}(\mid T \mid)$.

La première boucle for effectue le retournement du tableau $T[:r+1]$, c'est à dire des $r+1$ premières crêpes de la pile (de l'indice 0 à $r$ inclus), la seconde ajoute dans le même ordre la fin de la pile. 

### 2.3

#### 2.3.1

Pour un tableau $T$, `retournement(T, r)` retourne les $r+1$ premiers éléments du tableau, et donc $T[r]$  avant l'opération de retournement se retrouve en $T[0]$ après le retournement. On peut donc placer n'importe quel élément de la pile en 1ère position.

De même l'élément en $T[0]$ avant retournement se retrouve en position $T[r]$ après le retournement `retournement(T, r)` : on peut placer l'élément d'indice 0 du tableau en n'importe quelle position en 1 opération de retournement.

#### 2.3.2

```python
def tri(T):
    n = len(T)
    for t in range(n-1, -1, -1):
        trouver l'indice i de l'élément de taille t
        T = retournement(T, i)
        T = retournement(T, t)

    return T
```

Invariant de boucle : **à la fin d'une itération de la boucle, $T[i] = i$ pour tout $i \geq t$.**

##### 2.3.3

L'opération de retournement est en $\mathcal{O}(\mid T \mid)$ opérations. Donc notre algorithme de tri est en $\mathcal{O}(\mid T \mid ^2)$ opérations, ce i est plus grand que la complexité du problème du tri. C'est cohérent.

### 2.4

#### 2.4.1

Notre algorithme est en $\mathcal{O}(\mid T \mid)$ retournement, c'est don cune borne maximum du problème du retournement de crêpes.

#### 2.4.2

1. une adjacence étant un un couple $(i, i+1)$ tel que $\mid T[i] - T[i+1] \mid > 1$,il faut que $0 \leq i < \mid T \mid -1 = n -1$
2. Si $(i-1, i)$ et $(i, i+1)$ sont deux adjacences, alors :
   * soit $T[i-1] < T[i]$ et donc $T[i] = T[i-1] - 1$. De là on ne peut avoir $T[i] > T[i+1]$ car sinon $T[i+1] = T[i-1]$ ce qui est impossible. On a donc $T[i-1] < T[i] < T[i+1]$
   * soit $T[i-1] > T[i]$ et un raisonnement similaire au précédent nous permet de montrer que $T[i-1] > T[i] > T[i+1]$.

   Donc s'il y a $n-1$ adjacences, soit $T$ est trié par ordre croissant, soit par ordre décroissant.
3. un retournement `retournement(T, r)` ne peut changer les adjacences pour $i < r - 1$ (si (i, i+1) est une adjacence avant retournement, alors $(r-i-1, r-i)$  est une adjacence après retournement), et pour $i \geq r$. La seule adjacence qui peut être modifiée est $(r-1, r)$.
4. L'ordre $[n-2, n-4, \dots, (1\mbox{ ou }0\mbox{ selon la parité de }n), n-1, n-3, \dots, 0\mbox{ ou }1\mbox{ selon la parité de }n]$ a bien 0 adjacences et si $n \geq 4$.

Pour trier la pile il faut au moins autant de retournements que de paires non adjacentes plus 1 pour mettre l'élément $n-1$ en fin de liste qui est une opération qui ne change pas le nombre d'adjacences.
