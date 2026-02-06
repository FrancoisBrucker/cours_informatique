---
layout: layout/post.njk
title: "Algorithme de tri fusion"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le [tri fusion](https://fr.wikipedia.org/wiki/Tri_fusion) est un tri de complexité optimale : $\mathcal{O}(n\ln(n))$ opérations où $n$ est la taille de la liste en entrée. Il fonctionne selon principe algorithme [de diviser pour régner](<https://fr.wikipedia.org/wiki/Diviser_pour_r%C3%A9gner_(informatique)>) :

Un algorithme de la forme **_diviser pour régner_** fonctionne en deux parties :

1. **résoudre** $k$ sous-problèmes du problème initial
2. **combiner** les $k$ solutions des sous-problèmes en une solution du problème initial

Puisqu'il suffit de s'utiliser lui pour résoudre les sous-problèmes sa forme générale est :

```pseudocode
algorithme résolution(données):
    A partir de données créer k données_partielles_i (1 ≤ i ≤ k)
    pour chaque i  de [1 .. k]:
        solution_i ← résolution(données_partielles_i)

    solution ← combiner(solution_1, ..., solution_k)

    rendre solution
```

L'intérêt de ces programme est que si la complexité de la fonction `combiner`{.language-} est faible, la complexité de l'algorithme l'est également.

## Combiner

Pour un tri, si on scinde le tableau le tableau en tableau plus petit que l'on tri, le but de la fonction `combiner`{.language-} est de créer un tableau trié à partir de tableaux **triés**.

L'algorithme ci-après le fait de façon optimale, en $\mathcal{O}(\vert T1 \vert + \vert T2 \vert)$ :

```pseudocode/
algorithme combiner(T1: [entier], T2: [entier]) → [entier]:
    (i1 := entier) ← 0
    (i2 := entier) ← 0
    (T := [entier]) ← [entier]{longueur: T1.longueur + T2.longueur}

    pour chaque (i := entier) de [0 .. T.longueur[:
        si i2 == T2.longueur:
            T[i] ← T1[i1]
            i1 ← i1 + 1
        sinon si i1 == T1.longueur:
            T[i] ← T2[i2]
            i2 ← i2 + 1
        sinon si T1[i1] < T2[i2]:
            T[i] ← T1[i1]
            i1 ← i1 + 1
        sinon:
            T[i] ← T2[i2]
            i2 ← i2 + 1
    rendre T
```

### <span id="fonctionnement-colle"></span> Fonctionnement

On vérifie pour deux petits tableaux **triés**. Les indices `i1`{.language-} et `i2`{.language-} marquent les positions possibles du prochain élément à ajouter dans `T`{.language-}. Par exemple pour `T1=[1, 4, 7]`{.language-} et `T2=[0, 2, 3, 98]`{.language-}. `T`{.language-} vaudra :

1. `[0]`{.language-} après la 1ère itération (`i1=0`{.language-} et `i2=1`{.language-})
2. `[0, 1]`{.language-} après la 2nde itération (`i1=1`{.language-} et `i2=1`{.language-})
3. `[0, 1, 2]`{.language-} après la 3ème itération (`i1=1`{.language-} et `i2=2`{.language-})
4. `[0, 1, 2, 3]`{.language-} après la 4ème itération (`i1=1`{.language-} et `i2=3`{.language-})
5. `[0, 1, 2, 3, 4]`{.language-} après la 5ème itération (`i1=2`{.language-} et `i2=3`{.language-})
6. `[0, 1, 2, 3, 4, 7]`{.language-} après la 6ème itération (`i1=3`{.language-} et `i2=3`{.language-})
7. `[0, 1, 2, 3, 4, 7, 98]`{.language-} après la 7ème itération (`i1=3`{.language-} et `i2=4`{.language-})

### <span id="preuve-colle"></span> Preuve

À chaque itération de la boucle, soit `i1`{.language-} soit `i2`{.language-} augmente. Au bout des `T.longueur`{.language-} itérations on aura `i1`{.language-} = `T1.longueur`{.language-} et `i2`{.language-} = `T2.longueur`{.language-}. Les indices `i1`{.language-} et `i2`{.language-} marquant les positions possibles du prochain élément à ajouter dans `T`{.language-}, l'invariant de boucle que l'on peut facilement prouver est :

> **Invariant de boucle :** À la fin de chaque itération, `T[:i]`{.language-} est trié et contient les `i1`{.language-} premiers éléments de `T1`{.language-} et les `i2`{.language-} premiers éléments de `T2`{.language-}

### <span id="complexités-colle"></span> Complexités

Allons un peu plus vite :

- on a une boucle `pour chaque`{.language-} de `T1.longueur + T2.longueur`{.language-} itérations
- chaque ligne de l'algorithme est en $\mathcal{O}(1)$

{% note "**Proposition**" %}
La complexité max et min de `combiner`{.language-} est $\mathcal{O}(n_1 + n_2)$ avec $n_1$ et $n_2$ les tailles des tableaux `T1`{.language-} et `T2`{.language-} respectivement.
{% endnote %}

### Attention

{% exercice %}
Montrer que l'algorithme combiner précédent **n'est pas équivalent** à celui-ci :

```pseudocode/
algorithme combiner_faux(T1: [entier], T2: [entier]) → [entier]:
    (i1 := entier) ← 0
    (i2 := entier) ← 0
    (T := [entier]) ← [entier]{longueur: T1.longueur + T2.longueur}

    pour chaque (i := entier) de [0 .. T.longueur[:
        si (i2 == T2.longueur) ou (T1[i1] < T2[i2]):
            T[i] ← T1[i1]
            i1 ← i1 + 1
        sinon:
            T[i] ← T2[i2]
            i2 ← i2 + 1

    rendre T
```

{% endexercice %}
{% details "corrigé" %}
Si `i2 < T2.longueur`{.language-} mais que `i1 = T1.longueur`{.language-} l'algorithme va planter car il va tenter d'accéder à `T1[i1]`{.language-} qui n'existe pas.

Faites très attention aux conditions. C'est très souvent source d'erreurs quand on va trop vite...
{% enddetails %}

## Pseudo-code

Avec notre fonction `combiner(T1, T2)`{.language-} le pseudo code de l'algorithme fusion est :

```pseudocode
algorithme fusion(T: [entier]) → [entier]:
    si T.longueur < 2:
        rendre nouveau tableau contenant T
    sinon:
        (milieu := entier) ← T.longueur // 2  # division entière
        (T1 := [entier]) ← nouveau tableau contenant T[:milieu]
        (T2 := [entier]) ← nouveau tableau contenant T[milieu:]

        (T1_trié := [entier]) ← fusion(T1)
        (T2_trié := [entier]) ← fusion(T2)
        (T_trié := [entier]) ← combiner(T1_trié, T2_trié)

        rendre T_trié

```

## <span id="preuve-fusion"></span> Preuve

Comme `milieu < T.longueur`{.language-} si `T.longueur > 1`{.language-}, l'algorithme va bien converger et s'arrêter. De plus, comme l'algorithme `combiner`{.language-} est démontré, `fusion`{.language-} est bien un algorithme de tri.

## <span id="complexités-fusion"></span> Complexités

La complexité de l'algorithme `fusion`{.language-} est (avec $n$ la taille du tableau passé en entrée) :

$$C(n) = 2 \cdot C(\frac{n}{2}) + D(n)$$

Où :

- $C(n)$ est la complexité de l'algorithme fusion pour une liste à $n$ éléments (algorithme `fusion`{.language-})
- $D(n)$ est la complexité de fusionner deux listes triées en une unique liste triées (algorithme `combiner`{.language-}).

Comme l'algorithme `combiner`{.language-} est en $\mathcal{O}(n)$, l'équation de récurrence de la complexité est :

<div>
$$
C(n) = 2 \cdot C(\frac{n}{2}) + \mathcal{O}(n)
$$
</div>

Pour connaître la valeur de la complexité on peut utiliser [le master theorem](https://fr.wikipedia.org/wiki/Master_theorem) qui est **LE** théorème des complexités pour les algorithmes récursifs (on le verra lorsque l'on étudiera en détail [les algorithmes de type diviser pour régner](../../design-algorithmes/diviser-régner/){.interne}). Mais ici pas besoin d'invoquer l'artillerie lourde, on peut aisément calculer la complexité à la main :

{% note "**Proposition**" %}
La complexité de l'algorithme `fusion`{.language-} est $\mathcal{O}(n\ln(n))$ où $n$ est la taille de la liste en entrée
{% endnote %}
{% details "preuve", "open" %}

<div>
$$
\begin{array}{lcl}
C(n) &=& 2 \cdot C(\frac{n}{2}) + \mathcal{O}(n)\\
&=& 2 \cdot (2 \cdot (C(\frac{n}{4}) + \mathcal{O}(\frac{n}{2})) + \mathcal{O}(n)\\
&=& 2^2 \cdot C(\frac{n}{2^2}) + 2 \cdot \mathcal{O}(\frac{n}{2}) + \mathcal{O}(n)\\
&=& 2^2 \cdot C(\frac{n}{2^2}) + 2 \cdot \mathcal{O}(n)\\
&=& ...\\
&=& 2^i \cdot C(\frac{n}{2^i}) + i \cdot \mathcal{O}(n)\\
&=& ...\\
&=& 2^{\log_2(n)} \cdot C(1) + \log_2(n) \cdot \mathcal{O}(n)\\
&=& n \cdot C(1) + \log_2(n) \cdot \mathcal{O}(n)\\
&=& \mathcal{O}(n) + \log_2(n) \cdot \mathcal{O}(n)\\
&=& \mathcal{O}(n\log_2(n))\\
&=& \mathcal{O}(n\ln(n))
\end{array}
$$
</div>

{% enddetails %}

Tout comme le tri par sélection, le tri fusion a la particularité d'avoir toujours le même nombre d'opérations quelque soit la liste en entrée. Attention cependant, le tri fusion n'est pas in place, il rend un nouveau tableau.
