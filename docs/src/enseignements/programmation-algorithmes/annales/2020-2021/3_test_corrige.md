---
layout: layout/post.njk

title:  "corrigé Test 3 : preuve"
authors:
    - François Brucker
---

## barème

* 1pt pour la complexité et 1pt pour la preuve par algorithme

## 1. suppression de valeur

### complexité algorithme 1

On considère que la création d'une liste et l'ajout d'un élément en fin de liste sont des opérations en $\mathcal{O}(1)$ opérations. De là, notre algorithme est en $\mathcal{O}(n)$ opérations où $n$ st la taille de la liste `L`{.language-}.

### preuve algorithme 1

L'algorithme va parcourir la liste et ajouter un à un à L2 tous les éléments de `L`{.language-} différents de `val`{.language-}. Notre invariant de boucle pourrait donc être : à la fin de l'itération $i$ L2 est la restriction de `L[:i]`{.language-} aux valeurs différentes de `val`{.language-}.

* **initialisation** : à la fin de la première itération ($i=1$), `L2`{.language-} est vide si `x = L[0]`{.language-} vaut `val`{.language-} et vaut `[x]`{.language-} sinon. Ok.
* **récurrence** : On suppose la propriété vraie à la fin de l'itération $i$. L'itération $i+1$ a considéré $x = L[i]$. Notons `L2'`{.language-} la valeur de `L2`{.language-} à la fin de l'itération $i+1$. Au début de l'itération $i+1$, par hypothèse de récurrence, `L2`{.language-} est la restriction de `L[:i]`{.language-} aux valeurs différentes de `val`{.language-}. La restriction de  `L[:i+1]`{.language-} aux valeurs différentes de `val`{.language-} est alors soit égal à `L2`{.language-} si `L[i] = val`{.language-} soit `L2 + L[i]`{.language-} sinon. C'est exactement ce que vaut `L2'`{.language-}.

A la fin de la dernière itération, `L2`{.language-} vaut donc la restriction de `L[:n]`{.language-} (avec `n = len(L)`{.language-}) aux valeurs différentes de val.

## 2. suppression de doublon

### complexité algorithme 2

Commençons par compter le nombre de fois où la boucle `tant que`{.language-} sera exécutée. `L`{.language-} est modifiée à chaque fin de boucle `L = algorithme-1(L, x)`{.language-} avec `x = L[0]`{.language-}.  Comme l'algorithme de la question 1 rend la restriction de de `L`{.language-} aux valeurs différentes de `x`{.language-}, elle va forcément être strictement plus petite (puisque `x=L[0]`{.language-} il est forcément dans la liste)  : la longueur de la liste diminue strictement à chaque itération, on ne peut y rentrer que la longueur de `L`{.language-} initiale fois.

La seule ligne de l'algorithme qui n'est pas de complexité $\mathcal{O}(1)$ est : `L = algorithme-1(L, x)`{.language-}. Sa complexité est égale à une affectation ($\mathcal{O}(1)$) plus la complexité de l'algorithme de la question 1, qui vaut de l'ordre de la taille de la liste passée en entrée.

Cette taille diminue strictement à chaque itération : on peut utiliser l'astuce du cours pour ne garder que la complexité la plus importante, c'est à dire $\mathcal{O}(len(L))$ avec `L`{.language-} la liste initiale.

Notre complexité est donc de l'ordre : $\mathcal{O}(1) + A * (\mathcal{O}(1) + B)$ où :

* A est le nombre de fois où l'on rentre dans la boucle tant que : $\mathcal{O}(len(L))$
* B est la complexité maximale de l'algorithme de la question 1 : $\mathcal{O}(len(L))$

Notre algorithme est de complexité : $\mathcal{O}(len(L)^2)$

### preuve algorithme 2

La liste `L`{.language-} contient $k$ valeurs différentes que l'on note $v_1, \dots v_k$ dans l'ordre de la liste (le 1er indice où l'on rencontre $v_i$ est strictement plus petit que le 1er indice où l'on rencontre $v_j$ si $i < j$).

Notre invariant de boucle sera : au bout de la $i$ème itération :

* $L2 = [v_1, \dots, v_i]$.
* `L`{.language-} vaut la restriction de `L`{.language-} initiale aux valeurs différentes de $v_1$ jusqu'à $v_i$.

* **initialisation** : comme $v_1= L[0]$ notre invariant est vrai puisque l'algorithme 1 rendra la restriction de `L`{.language-} initiale aux éléments différents de $v_1$.
* **récurrence** : On suppose la propriété vraie à la fin de l'itération $i$. Au début de l'itération $i+1$, on a par hypothèse de récurrence que $L2 = [v_1, \dots, v_i]$ et que `L`{.language-} vaut la restriction de la liste `L`{.language-} initiale aux valeurs différentes de $v_1$ jusqu'à $v_i$. Donc $L[0] = v_{i+1}$ et tout se passe comme à la 1ère itération.

A la fin de l'algorithme, notre invariant est toujours juste : $L2 = [v_1, \dots, v_k]$
