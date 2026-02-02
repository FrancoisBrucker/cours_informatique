---
layout: layout/post.njk

title: "Exercices : calcul de complexité"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Quelques exercices non corrigé de calculs de complexité.


## Polynômes

En complément de :

{% prerequis %}

[Algorithmes de polynômes](../exercices-itératif-récursif/#polynômes){.interne}

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
algorithme valeur_naif(P: [entier], x: réel) → réel:
    (v := réel) ← 0
    pour chaque (i := entier) de [0 .. P.longueur[:
        m := P[i]
        pour chaque (i := entier) de [0 .. i[:
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
- le nombre de multiplication utilisée par l'algorithme `valeur_naif`{.language-}
- le nombre d'additions utilisée par l'algorithme `valeur_naif`{.language-}

{% endfaire %}

### Algorithme puissances itérées

```pseudocode
algorithme valeur_itéré(P: [entier], x: réel) → réel:
    (v := réel) ← P[0]
    xi ← x
    pour chaque (i := entier) de [1 .. P.longueur[:
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
- le nombre de multiplication utilisée par l'algorithme `valeur_itéré`{.language-}
- le nombre d'additions utilisée par l'algorithme `valeur_itéré`{.language-}

{% endfaire %}


### Algorithme de Horner

{% lien %}
[Méthode de Horner](https://fr.wikipedia.org/wiki/M%C3%A9thode_de_Ruffini-Horner)
{% endlien %}

```pseudocode
algorithme valeur_horner(P: [entier], x: entier) → entier:
    i := P.longueur -1
    (v := réel) ← P[i]
    tant que i > 0:
        v ← v * x
        i ← i - 1
        v ← v + P[i]
    
    rendre v
```

{% faire %}

Prouver que l'algorithme `valeur_itéré`{.language-} est une solution au problème algorithmique valeur.

{% endfaire %}
{% faire %}

Donnez, en utilisant la notation $\mathcal{O}$ avec comme paramètre la longueur du polynôme :

- la complexité de l'algorithme `valeur_itéré`{.language-}
- le nombre de multiplication utilisée par l'algorithme `valeur_itéré`{.language-}
- le nombre d'additions utilisée par l'algorithme `valeur_itéré`{.language-}

{% endfaire %}


## $k$-ème plus petit élément

On considère le pseudo-code suivant :

```pseudocode
fonction copie(T: [entier]) → [entier]:

    T' := [entier]{longueur: T.longueur}
    T' ← T[:]

    rendre T'


fonction maximum(T: [entier]) → entier:
    m := 0
    pour chaque (i := entier) de [0 .. T.longueur[:
        if T[m] < T[i]:
            m ← i
    rendre m


fonction minimum(T):
    m := 0
    pour chaque (i := entier) de [0 .. T.longueur[:
        if T[m] > T[i]:
            m ← i
    rendre m


algorithme recherche(T: [entier], k: entier) → entier:
    max_value := T[maximum(T)]
    min := 0

    T_copie := copie(T)
    pour chaque (i := entier) de [0 .. k - 1[:
        min ← minimum(T_copie)
        T_copie[min] := max_value + 1

    rendre minimum(T_copie)
```

### 1

{% faire %}

Donnez la complexité de l'algorithme `recherche(T, k)`{.language-}

{% endfaire %}
{% info %}
Pour calculer la complexité de l'algorithme, il vous faudra également calculer les complexités des fonctions utilisées par celui-ci.
{% endinfo %}

### 2

{% faire %}

Quel est l'intérêt de la fonction `copie(T)`{.language-} ?

{% endfaire %}

### 3

{% faire %}

Démontrez que l'algorithme `recherche(T, k)`{.language-} rend l'indice du $k$ème plus petit élément de $T$.

{% endfaire %}
{% info %}
Pour démontrer ce que fait recherche, il vous faudra également trouver et démontrer ce que font les fonctions utilisées par celui-ci.
{% endinfo %}

### 4

{% faire %}

Utilisez `recherche(T, k)`{.language-} pour créer un algorithme déterminant l'indice de [la médiane d'un tableau](https://fr.wikipedia.org/wiki/M%C3%A9diane_(statistiques)). Quelle est sa complexité ?

{% endfaire %}


## <span id="triangle-de-pascal"></span>Triangle de Pascal

Formule du coefficient binomial dit du [triangle de Pascal](https://fr.wikipedia.org/wiki/Triangle_de_Pascal), avec $1\leq k \leq n$ :

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
algorithme binom(n: entier, k: entier) → entier:
    si (n == k) ou (k == 0):
        rendre 1
    sinon:
        rendre binom(n-1, k-1) + binom(n - 1, k)
```

{% faire %}

Démontrez que l'algorithme `binom(n: entier, k: entier) → entier`{.language-} calcule bien la binomiale.
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
Que pensez vous de cette complexité ?
{% endfaire %}

### Algorithme v2

{% faire %}
Montrez en utilisant l'équation de récursion que :

<div>
$$
\binom{n}{k} = \frac{n!}{k!(n-k)!} = \frac{n}{k} \binom{n-1}{k-1}
$$
</div>

{% endfaire %}
{% faire %}
Utilisez le résultat précédent pour créer un algorithme récursif de complexité $\mathcal{O}(n)$ pour calculer $\binom{n}{k}$.
{% endfaire %}
{% faire %}
En utilisant le fait que $\binom{n}{k} = \binom{n}{n-k}$, donnez une borne exacte au nombre de récursion.
{% endfaire %}

{% faire %}
En examinant la signature de cet algorithme, pourquoi ne peut-on pas vraiment l'utiliser en pratique ?
{% endfaire %}

