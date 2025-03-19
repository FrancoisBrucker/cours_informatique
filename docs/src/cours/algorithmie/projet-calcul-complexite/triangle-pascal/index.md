---
layout: layout/post.njk

title: Triangle de Pascal

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

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

En utilisant [la règle de calcul de complexité sur les boucles dépendantes mais croissantes](../../complexité-calculs/règles-de-calcul/#règle-croissance){.interne}, cette complexité est en $\mathcal{O}(n^2)$.

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
