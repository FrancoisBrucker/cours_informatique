---
layout: layout/post.njk

title: "Exercices : calcul de complexité"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Quelques exercices non corrigés de calcul de complexité.

## Polynômes

En complément de :

{% prerequis %}

[Algorithmes de polynômes](../../1-algorithme/exercices-non-corrigés/#polynômes)

{% endprerequis %}

Le but de cette partie est d'estimer le nombre (en $\mathcal{O}$) de multiplications et d'additions du calcul d'une valeur d'un polynôme.

{% note "**Problème algorithmique**" %}
- **NOM** : valeur

- **ENTRÉES** :
  - une liste de $n+1$ réels $[a_0, \dots, a_n]$ $n \geq 0$
  - un réel $x$
- **SORTIE** : $\sum_{i=0}^na_i x^i$
{% endnote %}

**Contraintes** : on suppose que l'on ne possède pas de fonction puissance, uniquement la multiplication et l'addition.

### Algorithme naïf

```pseudocode
algorithme valeur_naif(P: []int, x: float) → float:
    ref v ← 0
    ref m int
    pour chaque i de [0 .. P.longueur[:
        m ← P[i]
        pour chaque _ de [0 .. i[:
            m ← m * x
        v ← v + m
    
    rendre v
```

{% faire %}

Prouver que l'algorithme `valeur_naif`{.language-} est une solution au problème algorithmique valeur.

{% endfaire %}
{% faire %}

Donnez, en utilisant la notation $\mathcal{O}$ avec comme paramètre la longueur du polynôme :

- la complexité de l'algorithme `valeur_naif`{.language-}
- le nombre de multiplications utilisées par l'algorithme `valeur_naif`{.language-}
- le nombre d'additions utilisées par l'algorithme `valeur_naif`{.language-}

{% endfaire %}

### Algorithme puissances itérées

```pseudocode
algorithme valeur_itéré(P: []int, x: float) → float:
    ref v, xi ← P[0], x

    pour chaque i de [1 .. P.longueur[:
        v ← v + P[i] * xi
        xi ← xi * x
    
    rendre v
```

{% faire %}

Prouver que l'algorithme `valeur_itéré`{.language-} est une solution au problème algorithmique valeur.

{% endfaire %}
{% faire %}

Donnez, en utilisant la notation $\mathcal{O}$ avec comme paramètre la longueur du polynôme :

- la complexité de l'algorithme `valeur_itéré`{.language-}
- le nombre de multiplications utilisées par l'algorithme `valeur_itéré`{.language-}
- le nombre d'additions utilisées par l'algorithme `valeur_itéré`{.language-}

{% endfaire %}


### Algorithme de Horner

{% lien %}
[Méthode de Horner](https://fr.wikipedia.org/wiki/M%C3%A9thode_de_Ruffini-Horner){.externe}
{% endlien %}

```pseudocode
algorithme valeur_horner(P: []int, x: int) → int:
    ref i ← P.longueur - 1
    ref v ← P[i]
    tant que i > 0:
        v ← v * x
        i ← i - 1
        v ← v + P[i]
    
    rendre v
```

{% faire %}

Prouver que l'algorithme `valeur_horner`{.language-} est une solution au problème algorithmique valeur.

{% endfaire %}
{% faire %}

Donnez, en utilisant la notation $\mathcal{O}$ avec comme paramètre la longueur du polynôme :

- la complexité de l'algorithme `valeur_horner`{.language-}
- le nombre de multiplications utilisées par l'algorithme `valeur_horner`{.language-}
- le nombre d'additions utilisées par l'algorithme `valeur_horner`{.language-}

{% endfaire %}

## <span id="triangle-de-pascal"></span>Triangle de Pascal

Formule du coefficient binomial dit du [triangle de Pascal](https://fr.wikipedia.org/wiki/Triangle_de_Pascal){.externe}, avec $1\leq k \leq n$ :

<div>
$$
\binom{n}{k} = \binom{n-1}{k-1} \mathrel{+} \binom{n-1}{k}
$$
</div>

et :

<div>
$$
\binom{n}{0} = \binom{n}{n} = 1 \text{ pour tout } n\geq 0
$$
</div>

### Algorithme v1

<span id="algorithme-binom-rec"></span>

```pseudocode
algorithme binom(n: int, k: int) → int:
    si (n == k) ou (k == 0):
        rendre 1
    sinon:
        rendre binom(n-1, k-1) + binom(n - 1, k)
```

{% faire %}

Démontrez que l'algorithme `binom(n: int, k: int) → int`{.language-} calcule bien la binomiale.
{% endfaire %}

{% faire %}
Montrez que la complexité de l'algorithme `binom`{.language-} est en $\Omega(\binom{n}{k})$.
{% endfaire %}

Nous allons montrer que cette complexité est rédhibitoire pour la plupart des calculs.

{% faire %}

Montrez que :
<div>
$$
\begin{array}{lcl}
\binom{2n}{n} &\geq & 2\cdot\binom{2n-2}{n-1}\\
\end{array}
$$
</div>
{% endfaire %}

{% faire %}
En déduire que :

<div>
$$
\begin{array}{lcl}
\binom{2n}{n} & \geq & 2^{n}\\
\end{array}
$$
</div>

{% endfaire %}
{% faire %}
Que pensez-vous de cette complexité ?
{% endfaire %}

### Algorithme v2

{% faire %}
Montrez en utilisant l'équation de récursion que :

<div>
$$
\binom{n}{k} = \frac{n!}{k!(n-k)!} = \frac{n}{k} \cdot \binom{n-1}{k-1}
$$
</div>

{% endfaire %}
{% faire %}
Utilisez le résultat précédent pour créer un algorithme récursif de complexité $\mathcal{O}(n)$ pour calculer $\binom{n}{k}$.
{% endfaire %}
{% faire %}
En utilisant le fait que $\binom{n}{k} = \binom{n}{n-k}$, donnez une borne exacte au nombre de récursions.
{% endfaire %}

{% faire %}
La division $\frac{n}{k}$ ne rendant pas forcément un entier, pourquoi ne peut-on pas vraiment utiliser directement la formule de récurrence en pratique ?

{% endfaire %}
{% faire %}
Modifier l'algorithme pour qu'il utilise tout le temps des entiers.
{% endfaire %}
{% info %}
Vous pourrez remarquer que si $\frac{n}{k}$ n'est pas entier, une autre division l'est forcément. 
{% endinfo %}

## Multiplication d'entiers

{% attention %}
On supposera dans tout cet exercice que nos entiers sont positifs.
{% endattention %}

### Multiplication naïve

```pseudocode
algorithme mul(x: int, y: int) → int:
    ref r ← 0
    tant que x ≠ 0:
        x ← x - 1
        r ← r + y
    
    rendre r
```

{% faire %}
Donnez la complexité de l'algorithme `mul`{.language-} en fonction de `x`{.language-}.
{% endfaire %}
{% faire %}
Démontrez que `mul(x, y) = x * y`{.language-}.
{% endfaire %}

### Multiplication russe

Une petite variation (astucieuse) de l'algorithme naïf :

```pseudocode
programme mul_russe(x: int, y: int) → int:
    ref r ← 0
    tant que x ≠ 0:
        si x est impair:
            x ← x - 1
            r ← r + y
        x ← x / 2
        y ← y * 2
    
    rendre r
```

{% faire %}
Donnez la complexité de l'algorithme `mul_russe`{.language-} en fonction de `x`{.language-}.
{% endfaire %}
{% info %}
Vous pourrez utiliser le fait que $x = \sum_{0\leq i \leq p} x_i 2^i$ avec $x_i \in \\{0, 1\\}$, et $p = \lfloor \log_2(x)\rfloor$
{% endinfo %}
{% faire %}
Démontrez que `mul(x, y) = x * y`{.language-}.
{% endfaire %}
{% info %}
Vous pourrez utiliser l'invariant : `X * Y = r + x * y`{.language-} avec `X`{.language-} et `Y`{.language-} les paramètres initiaux.
{% endinfo %}

### Multiplication binaire

Dans le calcul de la complexité précédent on a considéré, comme toujours, que la multiplication de deux entiers est effectuée en une opération et que le stockage d'un entier ne prend qu'une case mémoire. En réalité nos entiers sont codés sous la forme de tableaux $T$ de bits (0 ou 1) tels que :

<div>
$$
x = \sum_{0\leq i < T.\mbox{\tiny longueur}}2^i\cdot T[i]
$$
</div>

```pseudocode
algorithme mul2(T: []bit):
    pour chaque i de [1 .. T.longueur - 1]:
        T[i] ← T[i-1]
    T[0] ← 0
```

{% faire %}
Quelle est la complexité de l'algorithme `mul2(T: []bit)`{.language-} ?
{% endfaire %}
{% faire %}
Montrez que l'algorithme `mul2(T: []bit)`{.language-} multiplie par deux l'entier représenté par $T$ si $T[-1] = 0$.
{% endfaire %}
{% faire %}
Donnez un algorithme `div2(T: []bit)`{.language-} ainsi que sa complexité permettant de diviser par deux **en place** (en modifiant le tableau) un entier représenté par $T$ si $T[0] = 0$.
{% endfaire %}
{% faire %}
Si les tableaux $T_x$ et $T_y$ représentant respectivement deux entiers `x`{.language-} et `y`{.language-} sont tels que $T_x[-1] = T_y[-1] = 1$, quelle est la taille du tableau représentant l'entier $x\cdot y$ ?
{% endfaire %}
{% faire %}
Modifiez l'algorithme `mul(x: int, y: int) → int`{.language-} de la question 1 pour qu'il soit de signature : `mul(Tx: []bit, Ty: []bit) → []bit`{.language-}
{% endfaire %}
{% faire %}
Donnez la complexité de ce nouvel algorithme par rapport à `Tx.longueur`{.language-} et `Ty.longueur`{.language-}.

{% endfaire %}
