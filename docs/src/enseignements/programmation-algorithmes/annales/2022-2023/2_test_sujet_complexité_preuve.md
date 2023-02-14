---
layout: layout/post.njk

title:  "sujet Test 2 : complexité et preuve"
authors:
    - François Brucker
---

Le but de ce test est d'étudier les ***cols*** d'un tableau.

{% note "**Définition**" %}
Un ***col*** d'un tableau d'entiers $T$ de taille $n > 1$ est un indice $0 \leq i < n$ tel que :

* soit $i = 0$ et $T[i] \leq T[1]$
* soit $i = n-1$ et $T[i] \leq T[n-2]$
* soit $0 < i < n-1$ et $T[i] \leq \min(T[i-1], T[i+1])$
{% endnote %}

## 1. Existence

{% faire %}
Montrer que tout tableau d'entiers $T$ de taille $n > 1$ contient au moins 1 col.
{% endfaire %}

## 2. Découverte

{% faire %}
Donnez un algorithme nommé `trouve(T)`{.language-} permettant de trouver un col d'un tableau d'entiers $T$ de taille $n > 1$ passé en paramètre en $\mathcal{O}(n)$ opérations.

Vous expliciterez :

* que la complexité de votre algorithme est bien celle demandée,
* qu'il trouve bien un col.
{% endfaire %}

## 3. Rapidité

{% faire %}
Démontrez que l'algorithme suivant permet de trouver un col d'un tableau d'entiers $T$ de taille $n > 1$ passé en paramètre.
{% endfaire %}

```python#
def trouve_vite(T):
    if T[0] <= T[1]:
        return 0
    
    if T[-1] <= T[-2]:
        return len(T) - 1

    début = 0
    fin = len(T) - 1

    while True:
        milieu = (fin + début) // 2
        if T[milieu] <= min(T[milieu - 1], T[milieu + 1]):
            return milieu
        
        if T[milieu] > T[milieu - 1]:
            fin = milieu
        else:
            début = milieu

```

{% info %}
On a utilisé dans le code précédent le fait que :

* `T[-1]`{.language-} soit le dernier élément du tableau et `T[-2]`{.language-} l'avant dernier.
* `a // b`{.language-} rende la division entière de `a`{.language-} par `b`{.language-}

{% endinfo %}

## 4. Complexité

{% faire %}
Donnez la complexité de l'algorithme `trouve_vite(T)`{.language-}.
{% endfaire %}

## 5. complexité du problème

{% faire %}
Après avoir formalisé le problème de la recherche d'un col dans un tableau, vous démontrerez que sa complexité est égale à la complexité de l'algorithme `trouve_vite(T)`{.language-} de la question 3.
{% endfaire %}
