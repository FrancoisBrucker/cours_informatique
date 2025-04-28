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

<span id="algorithme-tri-sélection"></span>

```pseudocode
algorithme sélection(T: [entier]) → ∅:
    pour chaque i de [0, T.longueur[:  # boucle principale
        min_index ← i
        pour chaque j de [i + 1, T.longueur[:  # boucle intérieure
            si T[j] < T[min_index]:
                min_index ← j
        T[i], T[min_index] ← T[min_index], T[i]
```

{% details "code python" %}

```python
def sélection(T):
    for i in range(len(T) - 1):
        min_index = i
        for j in range(i + 1, len(T)):
            if T[j] < T[min_index]:
                min_index = j
        T[i], T[min_index] = T[min_index], T[i]
```

{% enddetails  %}

L'algorithme `sélection`{.language-} **modifie** le tableau passé en paramètre.

<span id="définition-in-place"></span>

{% note "**Définition**" %}
Les algorithmes qui modifient leurs entrées sont appelés [**_in place_**](https://en.wikipedia.org/wiki/In-place_algorithm)
{% endnote %}

## <span id="fonctionnement-sélection"></span> Fonctionnement

{% faire %}
Vérifiez que l'algorithme fonctionne pour :

- un petit tableau trié : `[1, 2, 3]`{.language-}
- un petit tableau non trié où le plus petit est en dernière place : `[3, 2, 1]`{.language-}

{% endfaire %}

## <span id="preuve-sélection"></span> Preuve

Le principe de fonctionnement est clair :

1. la boucle `pour chaque`{.language-} de la ligne 4 trouve l'indice du plus petit élément du tableau `T[i:]`{.language-}.
2. la ligne 7 échange le minimum du tableau `T[i:]`{.language-} avec `T[i]`{.language-}
3. la boucle principale fait recommencer cette procédure pour chaque indice de $T$.

On a alors clairement l'invariant de boucle :

> **Invariant de boucle :** À la fin de chaque étape $i$ de l'algorithme les $i$ plus petites valeurs du tableau sont triées aux $i$ premiers indices du tableau.

Qui permet de prouver qu'la fin de la boucle principale, le tableau est trié.

## <span id="complexités-sélection"></span> Complexités

On suppose que la taille du tableau est $n$.

Allons plus vite pour la complexité :

- toutes les instructions sont en $\mathcal{O}(1)$
- la boucle principale effectue $\mathcal{O}(n)$ itérations ($n-1$ exactement mais ce n'est pas important)
- la boucle intérieure fait $n-i-1$ itérations

Le nombre d'itérations de la boucle intérieure n'est pas constant, mais il décroît puisque $i$ augmente à chaque itération de la boucle `pour chaque`{.language-} de la ligne 2. On peut alors utiliser [la règle de croissance](../../complexité-calculs/complexité-algorithmes#règle-croissance){.interne} pour utiliser le maximum, $n-1$, pour le calcul de la complexité.

Ce qui donne une complexité de :

<div>
$$
\begin{array}{lcl}
C & = & \mathcal{O}(1) + \mathcal{O}(n) \cdot (\mathcal{O}(1) + \mathcal{O}(n) \cdot \mathcal{O}(1))\\
& = & \mathcal{O}(1) + \mathcal{O}(n) \cdot \mathcal{O}(n)\\
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
