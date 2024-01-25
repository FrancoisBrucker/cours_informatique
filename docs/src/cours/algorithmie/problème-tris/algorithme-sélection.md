---
layout: layout/post.njk 
title: "Algorithme du tri par sélection"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le tri par sélection est un algorithme simple qui fonctionne de la même manière quelque-soit le tableau en entrée. L'algorithme procède ainsi : à chaque itération de l'algorithme, on place à l'indice $i$ du tableau son $i$-ème plus petit élément.

On en déduit l'algorithme en pseudo-code suivant :

```python#
def sélection(T):
    for i in range(len(T) - 1):
        min_index = i
        for j in range(i + 1, len(T)):
            if T[j] < T[min_index]:
                min_index = j
        T[i], T[min_index] = T[min_index], T[i]
```

L'algorithme `sélection`{.language-} **modifie** le tableau passé en paramètre. On appelle ces algorithmes [in place](https://en.wikipedia.org/wiki/In-place_algorithm) car ils ne rendent rien, mais modifient les données en entrées.

## <span id="fonctionnement-sélection"></span> Fonctionnement

On vérifie que l'algorithme fonctionne pour :

- un petit tableau trié : `[1, 2, 3]`{.language-}
- un petit tableau non trié où le plus petit est en dernière place : `[3, 2, 1]`{.language-}

## <span id="preuve-sélection"></span> Preuve

Le principe de fonctionnement est clair. Il reste à prouver que c'est bien ce que l'algorithme `sélection`{.language-} fait.

1. la boucle `for`{.language-} de la ligne 4 trouve l'indice du plus petit élément du tableau `T[i:]`{.language-}.
2. la ligne 7 échange le minimum du tableau `T[i:]`{.language-} avec `T[i]`{.language-}
3. comme la boucle `for`{.language-} de la ligne 2 incrémente $i$, on a l'invariant de boucle :

{% note "**Invariant de boucle**" %}
À la fin de chaque étape $i$ de l'algorithme les $i$ plus petites valeurs du tableau sont triées aux $i$ premiers indices du tableau.
{% endnote %}

## <span id="complexités-sélection"></span> Complexités

On suppose que la taille du tableau est $n$.

Ligne à ligne :

1. début de fonction : $\mathcal{O}(1)$
2. une boucle de $n-1$ itérations
3. une affectation $\mathcal{O}(1)$
4. une boucle de $n-i-1$ itérations ($i$ est la variable définie ligne 2)
5. un test et deux valeurs d'un tableau : $\mathcal{O}(1)$
6. une affectation : $\mathcal{O}(1)$
7. deux affectation et quatre valeurs d'un tableau : $\mathcal{O}(1)$

Le nombre d'itérations de la boucle for de la ligne 4 n'est pas constant, mais il décroît puisque $i$ augmente à chaque itération de la boucle `for`{.language-} de la ligne 2. On peut alors utiliser [la règle de croissance](../../complexité-calculs/règles-de-calcul#règle-croissance){.interne} pour utiliser le maximum, $n-1$, pour le calcul de la complexité.

Ce qui donne une complexité de :

<div>
$$
\begin{array}{lcl}
C & = & \mathcal{O}(1) + \\
&& (n-1) \cdot (\\
&& \mathcal{O}(1) + \\
&& (n-1) \cdot ( \\
&& \mathcal{O}(1) + \\
&& \mathcal{O}(1)) + \\
&& \mathcal{O}(1)) \\
& = & \mathcal{O}(1) + (n-1) \cdot (\mathcal{O}(1) + (n-1) \cdot (\mathcal{O}(1))\\
& = & \mathcal{O}(n^2) \\
\end{array}
$$
</div>

Le nombre d'itérations est constant quelque soit le tableau, on a donc :

{% note "**Proposition**" %}
La complexité de l'algorithme `sélection`{.language-} est ($n$ est la taille du tableau passé en entrée) :

- la **complexité min** vaut $\mathcal{O}(n^2)$
- la **complexité (max)** vaut $\mathcal{O}(n^2)$
- la **complexité en moyenne** vaut également $\mathcal{O}(n^2)$ (car les complexités min et max sont égales)

{% endnote %}
