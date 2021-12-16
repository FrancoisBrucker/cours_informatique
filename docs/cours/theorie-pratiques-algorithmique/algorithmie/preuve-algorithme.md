---
layout: page
title:  "preuve d'algorithme"
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [algorithmie]({% link cours/theorie-pratiques-algorithmique/algorithmie/index.md %}) / [preuve d'algorithme]({% link cours/theorie-pratiques-algorithmique/algorithmie/preuve-algorithme.md %})
>
> prérequis :
>
>* [algorithmie/pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %})
{: .chemin}

Ua algorithme **toujours** un but, quelque chose pour quoi il est fait. Dans notre cas, un algorithme calculera la solution d'un problème.

Pour chaque algorithme que vous créerez ou que l'on demandera d'étudier il faudra :

1. caractériser le problème que l'algorithme es sensé résoudre
2. démontrer que l'algorithme fonctionne, c'est à dire qu'il le résout le problème en temps fini.

Prouver qu'un algorithme s'arrête fait partie des problèmes théoriques difficiles en informatique. En algorithmie, les algorithmes résolvent des problèmes et donc ils sont sensé s'arrêter et il sera (normalement) de le voir. En revanche, la preuve de l'algorithme est parfois plus délicate. Le problème étant souvent (toujours ?) concentré dans les boucles ou les récursions de l'algorithme, on cherchera à trouver des propriétés qui sont conservées avant et après une itération ou une récursion :

> Pour prouver un algorithme on cherchera à établir :
>
> * une équation de récurrence plus une condition d'arrêt pour prouver un algorithme récursif.
> * [un invariant de boucle](https://fr.wikipedia.org/wiki/Invariant_de_boucle) pour des algorithme itératifs. Ces invariants vont alors être conservés jusqu'à la fin de l'algorithme et nous permettre de prouver son résultat.
>
{: .code}

Notez que bien souvent prouver un algorithme et le créer est la même chose. Comprendre comment on peut résoudre un problème donné nous donnera l'algorithme et récproquement.

A part la recommendation ci-dessus, il n'existe pas vraiment de règles à appliquer pour prouver un algorithme. Seule l'expérience et l'étude des algorithmes classique vous permettra de trouver facilement comment prouver un algorithme.

> dans la suite, les algorithmes seront tous donnés en python

## factorielle récursive

```python
def factorielle(n):
    if n <= 1:
        return 1
    return n * factorielle(n-1)
```

* finitude : Si $n$ est un réel, l'algorithme va s'arrêter : $n$ décroît strictement à chaque appelle récursif et on stoppe si $n \leq 1$.
* complexité : dépend de $n$, le nombre pas sa taille.
* preuve : Pra récurrence sur $n$, avec $n$ entier positif.
  * entrée : des entiers positifs
  * fonction de récurrence. Si $n=0$ ça marche. Si ça marche pour l'entrée n-1, ça marche pour $n$ car la fonction rend $n \cdot factorielle(n-1)$ qui vaut $n \cdot (n-1)!$ par hypothèse de récurence.

## maximum d'un tableau

On va voir 2 algorithmes pour caluler la valeure maximum d'un tableau de réels.

### algorithme itératif

```python
def maximum(t):
    m = t[0]
    for x in t:
        if m < x:
            m = x
    return m
```

* finitude : clair car une unique boucle for.
* complexité : une boucle en $\mathcal{O}(len(t))$ et des choses en $\mathcal{O}(1)$. Sa complexité est en $\mathcal{O}(len(t))$
* preuve : par invariant de boucle.

> Pour les preuves par invariant de boucle, le schéma de preuve est le suivant :
>
> 1. on vérifie que l'invariant est vrai juste avant la première itération de la boucle
> 2. on suppose l'invariant vrai au début de l'itération $i$ de la boucle et on vérifie qu'il est toujours vérifié à la fin de l'itération $i$.
>
> Pour simplifier l'écriture, on note avec un `'` (prim) les variables à la fin de la boucle d'itération $i$.
{: .note}

Ici notre invariant est : *"Au début l'itération $i + 1 > 1$ de la boucle, $m$ vaut le maximum des $i$ premiers élément du tableau."*

Après la première itération de la boucle, comme $m$ vaut initialement le premier élément du tableau, on a que $m=t[0]$ qui est bien le maximum des 1 premier éléments du tableau. L'invariant est vérifié au début de l'itération $2$.

On suppose l'invariant vrai au début de l'itération $i + 1 >1$. A la fin de l'itération, $m'$ (la valeur de $m$ à l'issue de la boucle d'itération $i + 1$) vaut soit $m$ (la valeur de $m$ au début de la boucle d'itération $i +1 $) soit $x'$ (la variable $x$ affectée lors de) qui vaut la $i + 1$ème valeur du tableau.

Comme l'invariant est vrai au début de la boucle d'itération $i + 1$, $m$ vaut le maximum du tableau sur les $i$ premiers éléments. Or $m' = \max(m, x)$, donc $m'$ vaut bien le maximum du tableau sur les $i + 1$ premiers éléments.

### algorithme récursif

```python
def maximum(tab, debut=0):
    if debut == len(tableau) - 1:
        return tab[debut]
    x = maximum_tableau(tab, debut + 1)
    if tab[debut] < x
        return tab[debut]
    else:
        return x
```

> On a utilisé la possibilité d'avoir des [arguments par défaut](https://docs.python.org/fr/3.9/tutorial/controlflow.html#default-argument-values) en python. Ceci nous permet d'exécuter la fonction maximum comme si elle n'avait qu'un seul paramètre.

* finitude : début augmente strictement et s'arrête lorsqu'il vaut `len(tableau) - 1`
* complexité : de l'ordre $\mathcal{O}(len(t))$ puisque l'on effectue au maximum `len(tableau)` récursions d'un algorithme en $\mathcal{O}(1)$.
* preuve : par récurrence sur la longueur d'un tableau. On vérifie que l'algorithme fonctionne pour une longueur de tableau valant 1, puis on effectue preuve par récurrence sur la longueur du tableau.

## division euclidienne

Prouvons l'algorithme de la division euclidienne ci-après :

```python
def euclide(a, b):
    r = a
    q = 0
    while r >= b:
        r -= b
        q += 1
    return (q, r)
```

> On utilise la possibilité que donne python d'écrire `x += y` (*resp.* `x -= y`) à la place de `x = x + y` (*resp.* `x = x + y`).

Notez que le retour de la fonction est un [tuple](https://docs.python.org/fr/3/tutorial/datastructures.html#tuples-and-sequences) à 2 éléments (c'est à dire un tableau à 2 éléments que l'on ne peut pas modifer)

### finitude

le programme s'arrête ? : Oui si a et b sont des entiers positifs. Car

* `r` est un entier
* `r` après une itération est **strictement plus petit** que le `r` avant itération
* on s'arête si `r` est strictement plus petit que `b`.

### complexité

De l'ordre du nombre de fois où l'on rentre dans la boucle. Comme $r$ ne fait que décroître strictement et vaut $a$ au départ, on estime la complexité de l'algorithme en $\mathcal{O}(a)$.

> Comme on décrémente de $b$ à chaque fois on a aurait pu aussi dire que la complexité est en $\mathcal{O}(\frac{a}{b})$

### preuve

On veut montrer que l'on obtient bien une division euclidienne de $a$ par $b$. C'est à dire que $a = bq + r$ avec $r < b$. Pour cela on va s'aider de l'invariant de boucle : `a = r + q * b`

Prouvons l'invariant :

1. l'invariant est bien vrai avant la première boucle puisque $q=0$ et $r=a$ à ce moment là.
2. on doit prouver que `a' = r' + q' * b'`
3. si l'on est passé dans la boucle on a `a'=a`, `r' = r - b`, `b' = b` et `q' = q + 1`
4. donc `r' + q' * b' = r-b + (q+1) * b = r + q * b = a = a'`. On a bien `a' = r' + q' * b'`, l'invariant est démontré.

L'invariant étant juste tout le temps, il l'est en particulier à l'issue de la dernière boucle. A ce moment là on a `a = r + qb` avec `r < b` ce qui est bien ce qu'il fallait démontrer.
