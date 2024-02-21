---
layout: layout/post.njk

title: Cols

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[Corrigé](./corrigé){.interne}
{% endlien %}

Le but de cet exercice est d'étudier les **_cols_** d'un tableau.

{% note "**Définition**" %}
Un **_col_** d'un tableau d'entiers $T$ de taille $n > 1$ est un indice $0 \leq i < n$ tel que :

- soit $i = 0$ et $T[i] \leq T[1]$
- soit $i = n-1$ et $T[i] \leq T[n-2]$
- soit $0 < i < n-1$ et $T[i] \leq \min(T[i-1], T[i+1])$
  {% endnote %}

## Existence

Montrer que tout tableau d'entiers $T$ de taille $n > 1$ contient au moins 1 col.

## Découverte

Donnez un algorithme nommé `trouve(T)`{.language-} permettant de trouver un col d'un tableau d'entiers $T$ de taille $n > 1$ passé en paramètre en $\mathcal{O}(n)$ opérations.

Vous expliciterez :

- que la complexité de votre algorithme est bien celle demandée,
- qu'il trouve bien un col.

## Rapidité

Démontrez que l'algorithme suivant permet de trouver un col d'un tableau d'entiers $T$ de taille $n > 1$ passé en paramètre.

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

On a utilisé dans le code précédent le fait que :

- `T[-1]`{.language-} soit le dernier élément du tableau et `T[-2]`{.language-} l'avant dernier.
- `a // b`{.language-} rende la division entière de `a`{.language-} par `b`{.language-}

## Complexité

Donnez la complexité de l'algorithme `trouve_vite(T)`{.language-}.

## complexité du problème

Après avoir formalisé le problème de la recherche d'un col dans un tableau, vous démontrerez que sa complexité est égale à la complexité de l'algorithme `trouve_vite(T)`{.language-} de la question 3.

## Généralisation

On appelle col d'une matrice un élément minimum local de sa ligne et maximum local de sa colonne.

1. montrez qu'il n'existe pas forcément de col à une matrice
2. donnez un algorithme linéaire en la taille de la matrice pour trouver un col s'il existe
3. montrer que l'optimisation utilisée sur la ligne ne fonctionne pas sur les matrices.
