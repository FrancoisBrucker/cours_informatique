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

{% faire %}
Montrer que tout tableau d'entiers $T$ de taille $n > 1$ contient au moins 1 col.
{% endfaire %}

## Découverte

{% faire %}
Donnez un algorithme nommé `trouve(T)`{.language-} permettant de trouver un col d'un tableau d'entiers $T$ de taille $n > 1$ passé en paramètre en $\mathcal{O}(n)$ opérations.

Vous expliciterez :

- que la complexité de votre algorithme est bien celle demandée,
- qu'il trouve bien un col.
{% endfaire %}

## Rapidité

{% faire %}
Démontrez que l'algorithme suivant permet de trouver un col d'un tableau d'entiers $T$ de taille $n > 1$ passé en paramètre.
{% endfaire %}

```pseudocode
algorithme trouve_vite(T: [entier]) → entier:
    si T[0] <= T[1]:
        rendre 0

    si T[-1] <= T[-2]:
        rendre T.longueur - 1

    début ← 0
    fin ← T.longueur - 1

    tant que Vrai:
        milieu ← (fin + début) // 2
        si T[milieu] <= min(T[milieu - 1], T[milieu + 1]):
            rendre milieu

        si T[milieu] > T[milieu - 1]:
            fin ← milieu
        sinon:
            début ← milieu
```

{% details "code python" %}

```python/
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

{% enddetails %}

## Complexité

{% faire %}
Donnez la complexité de l'algorithme `trouve_vite(T)`{.language-}.
{% endfaire %}

## complexité du problème

{% faire %}
Après avoir formalisé le problème de la recherche d'un col dans un tableau, vous démontrerez que sa complexité est égale à la complexité de l'algorithme `trouve_vite(T)`{.language-}.
{% endfaire %}

## Généralisation

{% note "**Définition**" %}
On appelle **_col d'une matrice_** un élément minimum **global** de sa ligne et maximum **global** de sa colonne.

{% endnote %}

{% faire %}

1. montrez qu'il n'existe pas forcément de col à une matrice
2. donnez un algorithme linéaire en la taille de la matrice pour trouver un col s'il existe
3. montrer que l'optimisation utilisée sur la ligne ne fonctionne pas sur les matrices.

{% endfaire %}
