---
layout: layout/post.njk

title: Corrigé

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Existence

On donne trois preuves possibles

### En reprenant la définition

Si la première condition ($i=0$) est vérifiée, le tableau contient un col. On la suppose donc non vérifiée : $T[0] > T[1]$. De même, si la seconde condition ($i=n-1$) est vérifiée, le tableau contient également un col. Supposons la donc également non vérifiée : $T[n-2] < T[n-1]$.

Les deux conditions précédentes montrent qu'il existe $n-1 > i^\star > 0$ le plus petit indice tel que $T[i^\star] \leq T[i^\star +1]$. On a alors : $T[i^\star -1] > T[i^\star ] \leq T[i^\star +1]$ et $i^\star$ est un col.

### Une astuce

Un tableau d'entier possède forcément un élément minimum. Il existe donc $i^\star$ tel que $T[i^\star] \leq T[i]$ pour tout $0 \leq i < n$. De là :

- soit $i^\star = 0$ et $T[i^\star] \leq T[1]$
- soit $i^\star = n-1$ et $T[i^\star] \leq T[n-2]$
- soit $0 < i^\star < n-1$ et $T[i^\star] \leq \min(T[i^\star-1], T[i^\star+1])$

Simple et efficace, non ?

### Par récurrence

On montre par récurrence sur la taille $n$ du tableau qu'il existe toujours un col.

1. Initialisation. Si $n=2$ soit $T[0] \leq T[1]$ soit $T[0] \geq T[1]$ (ce qui est équivalent pour $n=2$ à $T[n-1] \leq T[n-2]$). Ces deux cas correspondent aux deux premières possibilités pour un col
2. on suppose la propriété vrai pour $n \geq 2$. Et on se donne un tableau $T$ de taille $n+1$.
3. l'hypothèse de récurrence stipule que le tableau $T'$ constitué des $n$ premières cases de $T$ ($T'= T[:-1]$) possède un col, disons à l'indice $i^\star$. 3 cas sont possibles :
   1. $i^\star = 0$ et $T'[0] \leq T'[1]$ ce qui implique $T[0] \leq T[1]$ : $i^\star$ est aussi un col pour $T$
   2. $0 < i^\star < n-1$ et $T'[i^\star] \leq \min(T'[i-1], T'[i+1])$ ce qui implique $T[i^\star] \leq \min(T[i^\star-1], T[i^\star+1])$ : $i^\star$ est aussi un col pour $T$
   3. $i^\star = n-1$ et $T'[n-1] \leq T'[n-2]$ ce qui implique $T[n-1] \leq T[n-2]$. On conclut en remarquant que :
      1. soit $T[n] \geq T[n-1]$ et $T[i^\star] \leq \min(T[i^\star-1], T[i^\star+1])$ : $i^\star$ est aussi un col pour $T$
      2. soit $T[n] < T[n-1]$ et $n$ est un col pour $T$.

## Découverte

La preuve de la 1ère question montrant qu'il existe forcément un col, l'algorithme suivant qui mime directement la définition (lignes 2-3 : 1ère condition, lignes 5-6 : 2ème condition et lignes 8-10 la troisième condition) trouvera forcément un col :

```python/
def trouve(T):
    if T[0] <= T[1]:
        return 0

    if T[-1] <= T[-2]:
        return len(T) - 1

    for i in range(1, len(T) - 1):
        if T[i] <= min(T[i-1], T[i + 1]):
            return i

```

Sa complexité dans le cas le pire a lieu pour les tableaux dont le premier et seul col se trouve à l'avant dernier indice (comme pour la liste $[5, 4, 3, 2, 1, 2]$ par exemple), forçant l'algorithme à :

- faire échouer le 1er test de la ligne 2 en $\mathcal{O}(1)$ opérations
- faire échouer le 2er test de la ligne 5 en $\mathcal{O}(1)$ opérations
- faire les $\mathcal{O}(n)$ itérations de la boucle for en :
  - faisant échouer tous les tests sauf le dernier $\mathcal{O}(1)$ opérations
  - réussissant le dernier test et en faisant un retour de fonction en $\mathcal{O}(1)$ opérations

La complexité totale maximale est alors :

$$
C(n) = \mathcal{O}(1) + \mathcal{O}(1) + \mathcal{O}(n) \cdot (\mathcal{O}(1) + \mathcal{O}(1)) = \mathcal{O}(n)
$$

On peut aussi utiliser la preuve précédente et _simplifier_ la boucle `for`{.language-} en gardant la même complexité :

```python
def trouve(T):
    if T[0] <= T[1]:
        return 0

    if T[-1] <= T[-2]:
        return len(T) - 1

    for i in range(1, len(T) - 1):
        if T[i] <= T[i + 1]:
            return i

```

## Rapidité

La preuve d'existence du 1 montre que pour tout $i + 1 < j$, si $T[i] > T[i+1]$ et $T[j] > T[j-1]$, alors il existe un indice $i < k < j$ tel que $k$ soit un col de la matrice.

L'invariant de boucle de la boucle `while`{.language-} est alors :

> **Invariant de boucle :** A la fin de chaque itération de la boucle `while`{.language-}, soit :
>
> - `T[milieu]`{.language-} est un col
> - `T[milieu]`{.language-} n'est pas un col et :
> - `début + 1 < fin`{.language-}
> - `T[début] > T[début+1]`{.language-} et `T[fin] > T[fin-1]`{.language-}

A la fin de la première itération, on a soit :

- `T[milieu] <= min(T[milieu - 1], T[milieu + 1])`{.language-} et `milieu`{.language-} est un col
- `fin' = milieu`{.language-} et `début' = début`{.language-} si `T[milieu] > T[milieu -1]`{.language-}. Comme initialement `0 = début + 1 < fin = len(T) - 1`{.language-} on a également `milieu - 1 > début`{.language-} puisque `T[0] > T[1]`{.language-} et l'invariant est vérifié.
- `fin' = fin`{.language-} et `début' = milieu`{.language-} si `T[milieu] <= T[milieu -1]`{.language-} et `T[milieu] > T[milieu + 1]`{.language-}. Comme `0 = début + 1 < fin = len(T) - 1`{.language-} on a également `milieu + 1 < fin`{.language-} puisque `T[-1] > T[-2]`{.language-} et l'invariant est vérifié.

La même démonstration fonctionne à l'identique à la fin de l'itération $i+1$ si l'invariant est vrai à la fin de l'itération $i$.

Comme `fin - début >= 0` et diminue strictement à chaque itération de la boucle `while`{.language-}, il arrivera **forcément** un moment où `milieu`{.language-} sera un col.

## Complexité

La procédure de la boucle `while`{.language-} est identique à la recherche dichotomique puisque l'on se place toujours au milieu de l'espace de recherche. Le cours nous indiquant que la complexité de la recherche dichotomique est $\mathcal{O}(\log_2(n)) = \mathcal{O}(\ln(n))$, on en conclut que l'algorithme `trouve_vite(T)`{.language-} est également en $\mathcal{O}(\ln(n))$ opérations.

## Complexité du problème

Il existe des tableaux ayant tous un unique col en position $i$ pour tout $0 \leq i < n$ (prenez les tableaux $[0, -1, \dots, -i, -i+1, -i +2, \dots, -i + (n - i - 1)]$). Tout algorithme trouvant les col des tableaux doit donc pouvoir distinguer parmi $n$ cas : il est au moins de complexité $\mathcal{O}(\log_2(n)) = \mathcal{O}(\ln(n))$.

Comme l'algorithme `trouve_vite(T)`{.language-} est de complexité $\mathcal{O}(\ln(n))$, c'est borne min est atteinte.

## Généralisation

### Existence

Une matrice avec ses lignes croissantes et ses colonnes décroissantes n'a pas de col.

### Algorithme

On peut stocker les maximaux des colonnes et les minimaux des lignes dans deux listes puis parcourir chaque élément de la matrice et vérifier s'il est égal au maximum de la colonne et au minimum de la ligne.

### Optimisation impossible

L'optimisation trouve un col de ligne, mais pas forcément le bon pour la matrice.

1. montrez qu'il n'existe pas forcément de col à une matrice
2. donnez un algorithme linéaire en la taille de la matrice pour trouver un col s'il existe
