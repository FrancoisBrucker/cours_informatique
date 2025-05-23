---
layout: layout/post.njk

title: Triangle de Pascal

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Formule du coefficient binomial dit du [triangle de Pascal](https://fr.wikipedia.org/wiki/Triangle_de_Pascal), avec $1\leq k \leq n$ :

<div>
$$
\binom{n}{k} = \binom{n-1}{k-1} \mathrel{+} \binom{n-1}{k}
$$
</div>

et :

<div>
$$
\binom{n}{0} = \binom{n}{n} = 1
$$
</div>

## Algorithme récursif

{% faire %}

Après avoir examiné les conditions d'arrêt, donner un algorithme récursif permettant de calculer le coefficient binomial.

{% endfaire %}

## Algorithme itératif

Pas de récursion terminale garantie si double récursion. Mais on peut tout de même ici en donner une version itérative. Avant de résoudre l'exercice suivant, regardez comment vous faisiez au lycée en remplissant petit à petit chaque ligne d'une matrice. La ligne $n$ correspond aux coefficients $\binom{n}{k}$ pour tout $0\leq k \leq n$, et vous la remplissiez en utilisant les lignes précédentes avec l'équation. Mais si, rappelez-vous :

{% lien %}
[Calculer un coefficient binomial : triangle de Pascal - Terminale](https://www.youtube.com/watch?v=6JGrHD5nAoc)
{% endlien %}

Pour ces algorithme on utilisera un tableau de tableau comme un type matrice (on étudiera plus précisément défini lorsque l'on a parlé de pseudo-code. Une matrice $M$ est un tableau de (tableaux d'entiers)de telle sorte que :

- $M$ est de type `[[entier]]`{.language-}
- $M[i]$ est la (i+1) ème ligne de la matrice
- $M[i][j]$ est le (j+1) ème élément de la (i+1) ème ligne de la matrice.

Le code suivant crée une matrice triangulaire inférieure à $n$ lignes valant 1 à toutes les cases du tableau :

```pseudocode
algorithme crée_matrice(n: entier) → [[entier]]
matrice ← un tableau de [entier] de taille n

pour chaque i de [1, n]:
    ligne ← un tableau d'entiers de taille i

    matrice[i-1] ← ligne
    pour chaque j de [1, i]:
        ligne[j-1] ← 1 
```

Utiliser le code précédent pour résoudre l'exercice suivant :

{% exercice %}
En créant itérativement la matrice triangulaire inférieure, donner une version itérative de l'algorithme calculant le triangle de Pascal. Sa signature devra être :

```pseudocode
algorithme binom_matrice(n: entier) → [[entier]]:
```

{% endexercice %}
{% details "corrigé" %}

Première version qui calcule toute la matrice triangulaire inférieure :

```pseudocode/
algorithme binom_matrice(n: entier) → [[entier]]:
    matrice ← un tableau de [entier] de taille n+1

    pour chaque i de [0, n]:
        ligne ← un tableau d'entiers de taille i+1

        matrice[i] ← ligne
        pour chaque j de [0, i]:
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

{% enddetails %}



L'algorithme suivant est le dernier algorithme que nous avons créé pour calculer $\binom{n}{k}$.

On va créer un algorithme qui rend uniquement la dernière ligne de la matrice :

```pseudocode/
algorithme binom_ligne(n: entier, k: entier) → [[entier]]:
    courante ← un tableau d'entiers de taille k+1
    précédente ← un tableau d'entiers de taille k+1

    pour chaque i de [0, n]:
        pour chaque j de [0, min(i, k)]:
            précédente[j] ← courante[j]

        pour chaque j allant de 0 à min(i, k):
            si (j == i) ou (j == 0):
                courante[j] ← 1
            sinon:
                courante[j] ← précédent[j-1] + précédent[j]

    rendre courante[k]
```

Sa complexité temporelle est $\mathcal{O}(nk)$ et il nécessite deux tableaux de taille $k$ pour fonctionner.

{% exercice %}
En remplissant la ligne courante de droite à gauche montrez que l'on peut se passer de la ligne `précédente`{.language-} et n'utiliser qu'un seul tableau  de taille $k$.

{% endexercice %}
{% details "corrigé" %}

```pseudocode/
algorithme binom_ligne(n: entier, k: entier) → [[entier]]:
    courante ← un tableau d'entiers de taille k+1

    pour chaque i de [0, n]:
        de j=min(i, k) à j=0 par pas de -1:
            si (j == i) ou (j == 0):
                courante[j] ← 1
            sinon:
                courante[j] ← courante[j-1] + courante[j]

    rendre courante[k]
```

L'algorithme devient _joli_, avec une seule boucle et un seul tableau.

{% enddetails %}




Le calcul du coefficient binomial se fait en utilisant [le triangle de Pascal](https://fr.wikipedia.org/wiki/Triangle_de_Pascal).

Pour $n > p > 0$ :

<div>
$$
\binom{n}{k} = \binom{n-1}{k-1} \mathrel{+} \binom{n-1}{k}
$$
</div>

et :

<div>
$$
\binom{n}{0} = \binom{n}{n} = 1
$$
</div>

## Récursif

```pseudocode
algorithme binom_rec(n: entier, k: entier) → entier:
    si (n == k) ou (k == 0):
        rendre 1
    sinon:
        rendre binom_rec(n-1, k-1) + binom_rec(n - 1, k)
```

{% exercice %}
Montrez que la complexité de l'algorithme `binom_rec`{.language-} est en $\Omega(\binom{n}{k})$.
{% endexercice %}
{% details "corrigé" %}

L'équation de récursion donne, en fonction de n et k :

<div>
$$
\begin{array}{lcl}
C(n, k) & = & \mathcal{O}(1) + C(n-1, k-1) + C(n-1, k) \\
&\geq&C(n-1, k-1) + C(n-1, k)\\
\end{array}
$$
</div>

Or comme $C(n, n) = C(n, 0) = \mathcal{O}(1) \geq 1$

que $C(n, k) \geq \binom{n}{k}$

{% enddetails %}

Nous allons montrer que cette complexité est rédhibitoire pour la plupart des calculs.

{% exercice %}
Montrez que pour $n \geq 1$:

<div>
$$
\begin{array}{lcl}
\binom{2n}{n} & \geq & 2^{n}\\
\end{array}
$$
</div>

{% endexercice %}
{% details "corrigé" %}

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

{% enddetails %}

{% exercice %}
En déduire que cette complexité est rédhibitoire dans le cas le pire.
{% endexercice %}
{% details "corrigé" %}

Comme la complexité du calcul récursif de $\binom{n}{k}$ est en $\Omega(\binom{n}{k})$, le calcul de $\binom{2n}{n}$ va prendre un temps de calcul $\Omega(2^n)$, ce qui est exponentiel.
{% enddetails %}

## Itératif v1

```pseudocode/
algorithme binom_matrice(n: entier) → [[entier]]:
    matrice ← un tableau de [entier] de taille n+1

    pour chaque i de [0, n]:
        ligne ← un tableau d'entiers de taille i+1

        matrice[i] ← ligne
        pour chaque j allant de 0 à i:
            si (j == i) ou (j == 0):
                ligne[j] ← 1
            sinon:
                précédent ← matrice[i-1]
                ligne[j] ← précédent[j-1] + précédent[j]

    rendre matrice
```

{% exercice %}
Utilisez la fonction `binom_matrice(n: entier) → [[entier]]`{.language-} pour créer l'algorithme itératif de signature :

```pseudocode
algorithme binom(n: entier, k:entier) → entier
```

calculant $\binom{n}{k}$.

Donnez-en sa complexité.

{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme binom(n: entier, k:entier) → entier:
    matrice ← binom_matrice(n)

    rendre matrice[n-1][k]
```

La complexité est en $\mathcal{O}(1)$ plus la complexité de la fonction `binom_matrice(n: entier) → [[entier]]`{.language-}.

En utilisant [la règle de calcul de complexité sur les boucles dépendantes mais croissantes](../../complexité-calculs/complexité-algorithmes/#règle-croissance){.interne}, cette complexité est en $\mathcal{O}(n^2)$.

On en déduit que la complexité de l'algorithme `binom`{.language-} est en $\mathcal{O}(n^2)$
{% enddetails %}

## Itératif v2

{% exercice %}
Modifier l'algorithme précédent pour donner un algorithme itératif de complexité $\mathcal{O}(nk)$ pour calculer $\binom{n}{k}$.
{% endexercice %}
{% details "corrigé" %}

On a pas besoin de toute la matrice triangulaire inférieure, on peut se restreindre à ne calculer que les k première colonnes :

```pseudocode/
algorithme binom_matrice2(n: entier, k: entier) → [[entier]]:
    matrice ← un tableau de [entier] de taille n+1

    pour chaque i de [0, n]:
        ligne ← un tableau d'entiers de taille i+1

        matrice[i] ← ligne
        pour chaque j allant de 0 à min(i, k):
            si (j == i) ou (j == 0):
                ligne[j] ← 1
            sinon:
                précédent ← matrice[i-1]
                ligne[j] ← précédent[j-1] + précédent[j]

    rendre matrice
```

La complexité de la fonction `binom_matrice2`{.language-} est clairement en $\mathcal{O}(nk)$ puisque la boucle intérieure ne fera jamais plus de $k$ itérations.

de là, l'algorithme suivant est aussi de complexité $\mathcal{O}(nk)$ :

```pseudocode
algorithme binom(n: entier, k:entier) → entier:
    matrice ← binom_matrice2(n, k)

    rendre matrice[n-1][k]
```

{% enddetails %}

La complexité est maintenant maîtrisée, mais la complexité spatiale est aussi en $\mathcal{O}(nk)$. On peut faire mieux car pour calculer la $i$ème ligne de la matrice triangulaire inférieure de Pascal on a uniquement besoin de la ligne précédente.

{% exercice %}
Modifier l'algorithme précédent pour donner un algorithme itératif de complexité $\mathcal{O}(nk)$ pour calculer $\binom{n}{k}$ et de complexité spatiale $\mathcal{O}(k)$
{% endexercice %}
{% details "corrigé" %}

On va créer un algorithme qui rend uniquement la dernière ligne de la matrice :

```pseudocode/
algorithme binom_ligne(n: entier, k: entier) → [[entier]]:
    courante ← un tableau d'entiers de taille k+1
    précédente ← un tableau d'entiers de taille k+1

    pour chaque i de [0, n]:
        pour chaque j allant de 0 à min(i, k):
            précédente[j] ← courante[j]

        pour chaque j allant de 0 à min(i, k):
            si (j == i) ou (j == 0):
                courante[j] ← 1
            sinon:
                courante[j] ← précédent[j-1] + précédent[j]

    rendre courante[k]
```

> Spoiler : on verra que l'on peut faire encore mieux...
{% enddetails %}
