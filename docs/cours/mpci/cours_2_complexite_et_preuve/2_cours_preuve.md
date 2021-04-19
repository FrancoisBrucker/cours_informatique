---
layout: page
title:  "preuve"
category: cours
tags: informatique cours 
author: "François Brucker"
---

# Introduction

Pour prouver qu'un algorithme fonctionne il faut :

* prouver qu'il s'arrête
* avoir une idée de sa complexité (est-ce que je vais le voir s'arrêter de mon vivant ?)
* prouver qu'il fait bien ce que l'on attend de lui

Prouver qu'un algorithme s'arrête fait partie des problèmes théoriques difficiles en informatique. Rassurez-vous, pour vos algorithmes, ce sera facile de le savoir ou de le voir. 

La preuve de l'algorithme est parfois plus délicate : le problème étant souvent (toujours ?) concentré dans les boucles ou les récursions. On cherche à trouver des propriétés qui sont conservées avant et après une itération : 

* soit une équation de récurrence plus une condition d'arrêt de récurrence.
* soit [un invariant de boucle](https://fr.wikipedia.org/wiki/Invariant_de_boucle). Ces invariants vont alors être conservés jusqu'à la fin de l'algorithme et nous permettre de prouver son résultat.


## factorielle récursive

```python
def factorielle(n):
	if n <= 1:
		return 1
	return n * factorielle(n-1)
```

* finitude : $n$ doit être un réel. Comme $n$ décroît strictement à chaque appelle récursif et on stoppe si $n \leq 1$.
* complexité dépend de $n$, le nombre pas sa taille.
* preuve : 
    * entrée : des entiers positifs
    * fonction de récurrence. En $n=0$ et $n=1$ ça marche. Si ça marche en n-1, ça marche en n car $n! = n * (n-1)!$


## max d'un tableau

### itératif

```python
def maximum(t):
    m = t[0]
    for x in t:
        if m < x:
            m = x
    return m
```

* finitude : clair car une unique boucle for.
* complexité : une boucle en $\mathcal{O}(len(t))$ et des choses en $\mathcal{O}(1)$ : $\mathcal{O}(len(t))$
* preuve : par invariant.

Pour les preuves par invariant de boucle, le schéma de preuve est le suivant : 

1. on écrit l'invariant et on vérifie qu'il est vrai avant ou après la première boucle.
2. on écrit l'invariant avec les variable après la boucle. On les notes avec le nom de la variable suivi d'un `'` (prim). Il faut prouver que cette égalité est vraie.
3. pour prouver l'invariant après la boucle, on écrit les variable après la boucle d'itération $i$ en fonction des variable juste avant la boucle d'itération $i$ 
4. on vérifie que l'on retombe bien sur l'invariant.

Ici notre invariant est : *"Après l'étape $i$ de la boucle, $m$ vaut le maximum des $i$ premiers élément du tableau."*

Après la première itération de la boucle, comme $m$ vaut initialement le premier élément du tableau, on a que $m=t[0]$ qui est bien le maximum des 1 premier éléments du tableau. 

On suppose l'invariant vrai au début de la boucle $i$. A la fin de la boucle, $m'$ (la valeur de $m$ à l'issue de la boucle d'itération $i$) vaut soit $m$ (la valeur de $m$ au début de la boucle d'itération $i$) soit $x$ la $i$ ème valeur du tableau.

Comme l'invariant est vrai au début de la boucle d'itération $i$, $m$ vaut le maximum du tableau sur les $i-1$ premiers éléments. Or $m' = max(m, x)$, donc $m'$ vaut bien le maximum du tableau sur les $i$ premiers éléments.

### récursif

```python
def maximum_tableau(tab, debut=0):
    if debut == len(tableau) - 1:
        return tab[debut]
    return max(tab[debut], maximum_tableau(tab, debut + 1))
```

* finitude : début augment strictement et s'arrête lorsqu'il vaut `len(tableau) - 1`
* complexité : de l'ordre $\mathcal{O}(len(t))$ récursion d'un algorithme en $\mathcal{O}(1)$ : $\mathcal{O}(len(t))$
* preuve : récurrence sur la longueur d 'un tableau. On vérifie que l'algorithme fonctionne pour une longueur de tableau de 1, puis on effectue preuve par récurrence.


## division euclidienne


```python
def euclide(a, b):
	r = a
	q = 0
	while r >= b:
		r -= b
		q += 1
	return (q, r)
```


>**Remarque** : 
>
>* on utilise les raccourci python pour -b et +1. 
>* on rend bien un unique objet [tuple](https://docs.python.org/fr/3/tutorial/datastructures.html#tuples-and-sequences ) (une liste où on ne peut pas bouger les éléments).

### finitude

le programme s'arrête ? : Oui si a et b sont des entiers positifs. Car 

* `r` est un entier 
* `r` après une itération est **strictement plus petit** que le `r` avant itération 
* on s'arête si `r` est plus petit que `b`. 

### complexité

De l'ordre du nombre de fois où l'on rentre dans la boucle. Comme $r$ ne fait que décroître strictement et vaut $a$ au départ : $\mathcal{O}(a)$. 
Comme on décrémente de $b$ à chaque fois on a aussi :  $\mathcal{O}(a / b)$

Retour : 1 objet liste. 

### preuve

invariant : `a = r + q * b`

En suivant les étapes de la preuve par invariant : 

1. l'invariant est bien vrai avant la première boucle puisque $q=0$ et $r=a$ à ce moment là.
2. on doit prouver que `a' = r' + q' * b'`
3. si l'on est passé dans la boucle on a `a'=a`, `r' = r - b`, `b' = b` et `q' = q + 1`
4. donc `r' + q' * b' = r-b + (q+1) * b = r + q * b = a = a'`. On a bien `a' = r' + q' * b'`, l'invariant est démontré.

L'invariant étant juste tout le temps, il l'est en particulier à l'issue de la dernière boucle. A ce moment là on a `a = r + q * b` avec `r < b` ce qui est bien la définition de la division euclidienne.


## Ackermann

Souvent, savoir si un algorithme va finir est trivial. Mais qu'en est-il de la [fonction d'Ackermann](https://fr.wikipedia.org/wiki/Fonction_d%27Ackermann), très importante en informatique théorique ?

En gros, c'est une fonction qui ne peut être décrite que par un algorithme. Il n'existe pas de fonction qui la calcule. Elle se définit de la manière suivante, pour tous entiers m et n positifs :

* A(m, n) = n + 1 si m = 0 
* A(m - 1, 1) si n = 0
* A(m - 1, A(m, n - 1)) sinon.

Cette fonction s'arrête bien un jour.



Pour chaque appel récursif de la fonction d'ackerman, soit m, soit $n$ est strictement plus petit dans la fonction appelée que dans la fonction appelante. On arrivera donc toujours à $m = 0$ qui stoppera la récursion ou $n = 0$ qui fera baisser la valeur de $m$.
 

Pour calculer Ack(2, 3) par exemple, on a les récurrences suivantes :

* Ack(2, 3) = Ack(1, Ack(2, 2))
* Ack(2, 2) = Ack(1, Ack(2, 1))
* Ack(2, 1) = Ack(1, Ack(2, 0))
* Ack(2, 0) = Ack(1, 1)
* Ack(1, 1) = Ack(0, Ack(1, 0))
* Ack(1, 0) = Ack(0, 1) = 2
* puis on remonte d'un cran et les récursions recommencent...


Au final on trouve Ack(2, 3) = 9. La fonction croît très très vite. Par exemple Ack(5, 0) = Ack (4, 1) = 65533 et Ack(4, 2) = $2^{65536} - 3$.

Complexité : nombre d'opération au moins supérieure à son résultat puisque que l'on ne fait qu'ajouter 1 à n comme calcul et les valeurs de n sont modifiées de +1 ou -1.


