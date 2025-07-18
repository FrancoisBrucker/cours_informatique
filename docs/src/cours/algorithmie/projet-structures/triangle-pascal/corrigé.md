---
layout: layout/post.njk

title: Corrigé

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Algorithme récursif

La formule de récursion s'arrête dans deux cas possibles soit $k = 1$ (première récursion) soit $n - 1 = k$ deuxième récursion. On a alors deux conditions d'arrêts à regarder pour $1\leq k \leq n$ :

- soit $k = 0$ et $\binom{n}{0} = 1$
- soit $k = n$ et $\binom{n}{n} = 1$

Ce qui donne le code :

<span id="algorithme-binom-rec"></span>

```pseudocode
algorithme binom(n: entier, k: entier) → entier:
    si (n == k) ou (k == 0):
        rendre 1
    sinon:
        rendre binom(n-1, k-1) + binom(n - 1, k)
```

Comme $n$ diminue strictement et $1\leq k \leq n$ on se rapproche strictement de la condition d'arrêt, le programme s'arrête à chaque fois : c'est un algorithme.

L'équation de récursion donne, en fonction de n et k :

<div>
$$
\begin{array}{lcl}
C(n, k) & = & \mathcal{O}(1) + C(n-1, k-1) + C(n-1, k) \\
&\geq&C(n-1, k-1) + C(n-1, k)\\
\end{array}
$$
</div>

Or comme $C(n, n) = C(n, 0) = \mathcal{O}(1) \geq 1$, on a $C(n, k) \geq \binom{n}{k}$

Or :

<div>
$$
\begin{array}{lcl}
\binom{2n}{n} & = & \binom{2n-1}{n-1} + \binom{2n-1}{n}\\
              &&  \binom{2n-2}{n-2} + \binom{2n-2}{n-1} + \binom{2n-1}{n}\\
              &\geq  & \binom{2n-2}{n-1} + \binom{2n-1}{n}\\
              &\geq & \binom{2n-2}{n-1} + \binom{2n-2}{n-1} + \binom{2n-2}{n}\\
              &\geq & 2\cdot\binom{2n-2}{n-1}\\
              &\geq & \dots \\
              &\geq & 2^k\cdot\binom{2(n-k)}{n-k}\\
              &\geq & 2^{n}\cdot\binom{n}{0}
\end{array}
$$
</div>

Comme la complexité du calcul récursif de $\binom{n}{k}$ est en $\Omega(\binom{n}{k})$, le calcul de $\binom{2n}{n}$ va prendre un temps de calcul exponentiel $\Omega(2^n)$.

## Algorithme itératif

### v1

Première version qui calcule toute la matrice triangulaire inférieure :

<span id="algorithme-binom-matrice"></span>

```pseudocode/
algorithme binom_matrice(n: entier) → [[entier]]:
    matrice ← un tableau de [entier] de taille n+1

    pour chaque i de [0 .. n]:
        ligne ← un tableau d'entiers de taille i+1

        matrice[i] ← ligne
        pour chaque j de [0 .. i]:
            si (j == i) ou (j == 0):
                ligne[j] ← 1
            sinon:
                précédent ← matrice[i-1]
                ligne[j] ← précédent[j-1] + précédent[j]

    rendre matrice
```

Il y a deux boucles imbriquées, donc deux invariants à trouver !

L'invariant de la boucle 4-13 peut être :

> **Invariant de la boucle 4-13** : `matrice[i-1]`{.language-} contient la $i$ème ligne de la matrice triangulaire inférieure de Pascal.

Pour le prouver, il faut trouver un invariant à la boucle 8-13. Par exemple :

> **Invariant de la boucle 8-13** : si `matrice[i-2]`{.language-} contient la $i-1$ème ligne de la matrice triangulaire inférieure de Pascal, alors `ligne`{.language-} contient la $i$ème ligne de la matrice triangulaire inférieure de Pascal.

Ce dernier invariant est évidemment vrai par construction de la boucle (c'est la relation de récurrence). Une fois la boucle 8-13 prouvée, cela prouve l'invariant de la boucle 4-13.

On utilise alors l'algorithme précédent pour déterminer la binomiale :

<span id="algorithme-binom-1"></span>

```pseudocode
algorithme binom(n: entier, k:entier) → entier:
    matrice ← binom_matrice(n)

    rendre matrice[n][k]
```

La complexité est en $\mathcal{O}(1)$ plus la complexité de la fonction `binom_matrice(n: entier) → [[entier]]`{.language-}.

En utilisant [la règle de calcul de complexité sur les boucles dépendantes mais croissantes](../../complexité-calculs/complexité-algorithmes/#règle-croissance){.interne}, cette complexité est en $\mathcal{O}(n^2)$.

On en déduit que la complexité de l'algorithme `binom`{.language-} est en $\mathcal{O}(nk)$. Comme il faut de plus stocker toute la matrice triangulaire inférieure, sa complexité spatiale est en $\mathcal{O}(nk)$

### v2

On va créer un algorithme qui rend uniquement la dernière ligne de la matrice :

```pseudocode
algorithme ligne_suivante(l: [entier]) → [entier]:
    l2 ← un tableau d'entiers de taille l.longueur +1

    l2[0] ← 1
    l2[-1] ← 1

    pour chaque i de [1 .. l2.longueur - 1[:
        l2[1] ← l[i] + l[i-1]

    rendre l2
```

L'algorithme `ligne_suivante(l: [entier]) → [entier]`{.language-} est correct si $l= [\binom{n}{0}, \dots, \binom{n}{n}]$ puisque on applique directement l'équation de récursion. Sa complexité spatiale et temporelle est en $\mathcal{O}(l.\text{\small longueur})$.

On a alors la version améliorée de `binom(n: entier, k:entier) → entier`{.language-} :

<span id="algorithme-binom-2"></span>

```pseudocode
algorithme binom(n: entier, k:entier) → entier:
    l ← [0]
    répéter n fois:
       l ← ligne_suivante(l)

    rendre l[k]
```

Si la complexité temporelle ne change pas, la complexité spatiale est maintenant de $\mathcal{O}(l.\text{\small longueur})$.

On peut faire mieux en ne calculant que les $k+1$ premiers éléments de chaque ligne. Il faut pour cela modifier l'algorithme en créant une version alternative de `ligne_suivante`{.language-} : `ligne_suivante(l: [entier]) → [entier]`{.language-}

<span id="algorithme-binom-3"></span>

```pseudocode
fonction ligne_suivante(l: [entier], k: entier) → [entier]:
    m ← min(k, l.longueur + 1)
    l2 ← un tableau d'entiers de taille m + 1

    l2[0] ← 1
    l2[-1] ← 1

    pour chaque i de [1 .. m]:
        l2[1] ← l[i] + l[i-1]

    rendre l2

algorithme binom(n: entier, k:entier) → entier:
    l ← [0]
    répéter n fois:
       l ← ligne_suivante(l, k)

    rendre l[k]

```

## Algorithme liste

<span id="algorithme-binom"></span>

```pseudocode
fonction ligne_suivante(l: Liste<entier>, k: entier) → ∅:
    si l.longueur + 1 < k:
        l.append(1)
    l[0] ← 1
    l[-1] ← 1

    de j=min(l.longueur -1, k)-1 à j=1 par pas de -1:
        l[j] ← l[j] + l[j-1]

algorithme binom(n: entier, k:entier) → entier:
    l ← Liste<entier> 
    l[0] ← 1
    répéter n fois:
       ligne_suivante(l, k)

    rendre l[k]

```

L'algorithme devient _joli_, avec une seule boucle et un seul tableau.
