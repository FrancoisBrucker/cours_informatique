---
layout: layout/post.njk 
title: "Algorithme de tri fusion"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Le [tri fusion](https://fr.wikipedia.org/wiki/Tri_fusion) est un tri de complexité optimale : $\mathcal{O}(n\ln(n))$ opérations où $n$ est la taille de la liste en entrée. Il fonctionne selon principe algorithme de [diviser pour régner](https://fr.wikipedia.org/wiki/Diviser_pour_r%C3%A9gner_(informatique)) :

<span id="diviser-pour-régner"></span>
{% note "**À retenir**"%}
Un algorithme de la forme ***diviser pour régner*** fonctionne en deux parties :

1. **résoudre** $k$ sous-problèmes du problème initial
2. **combiner** les $k$ solutions des sous-problèmes en une solution du problème initial

Puisqu'il suffit de s'utiliser lui pour résoudre les sous-problèmes sa forme générale est :

```text
def algorithme(données):
    A partir de données créer k données_partielles_i (1 ≤ i ≤ k)
    pour chaque i allant de 1 à k:
        solution_i = algorithme(données_partielles_i)
    
    solution = combiner(solution_1, ..., solution_k)

    rendre solution
```

{% endnote %}

L'intérêt de ces programme est que si la complexité de la fonction `combiner`{.language-} est faible, la complexité de l'`algorithme`{.language-} également.

## Combiner

Pour un tri, si on scinde le tableau le tableau en tableau plus petit que l'on tri, le but de la fonction `combiner`{.language-} est de créer un tableau trié à partir de tableaux **triés**.

L'algorithme ci-après le fait de façon optimale, en $\mathcal{O}(\vert T1 \vert + \vert T2 \vert)$ :

```python#
def combiner(T1, T2):
    i1 = i2 = 0
    T = []
    while i1 < len(T1) or i2 < len(T2):
        if i2 == len(T2):
            T.append(T1[i1])
            i1 += 1
        elif i1 == len(T1):
            T.append(T2[i2])
            i2 += 1
        elif T1[i1] < T2[i2]:
            T.append(T1[i1])
            i1 += 1
        else:
            T.append(T2[i2])
            i2 += 1
    return T
```

### <span id="fonctionnement-colle"></span> Fonctionnement

On vérifie pour deux petits tableaux **triés**. Par exemple pour `T1=[1, 4, 7]`{.language-} et `T2=[0, 2, 3, 98]`{.language-}. `T`{.language-} vaudra :

1. `[0]`{.language-} après la 1ère itération (`i1=0`{.language-} et `i2=1`{.language-})
2. `[0, 1]`{.language-} après la 2nde itération (`i1=1`{.language-} et `i2=1`{.language-})
3. `[0, 1, 2]`{.language-} après la 3ème itération (`i1=1`{.language-} et `i2=2`{.language-})
4. `[0, 1, 2, 3]`{.language-} après la 4ème itération (`i1=1`{.language-} et `i2=3`{.language-})
5. `[0, 1, 2, 3, 4]`{.language-} après la 5ème itération (`i1=2`{.language-} et `i2=3`{.language-})
6. `[0, 1, 2, 3, 4, 7]`{.language-} après la 6ème itération (`i1=3`{.language-} et `i2=3`{.language-})
7. `[0, 1, 2, 3, 4, 7, 98]`{.language-} après la 7ème itération (`i1=3`{.language-} et `i2=4`{.language-})

### <span id="preuve-colle"></span> Preuve

L'algorithme se finit bien puisqu'à chaque itération de la boucle while soit `i1`{.language-} soit `i2`{.language-} augmente. Au bout de `len(T1) + len(T2)`{.language-} itération on aura `i1`{.language-} = `len(T1)`{.language-} et `i2`{.language-} = `len(T1)`{.language-}, donc la condition `i1 < len(T1) or i2 < len(T2)`{.language-} ne sera plus vérifiée.

L'invariant de boucle que l'on peut facilement prouver est :

{% note "**Invariant de boucle**" %}
À la fin de chaque itération, `T[:i1 +i2]`{.language-} est trié et contient les `i1`{.language-} premiers éléments de `T1`{.language-} et les `i2`{.language-} premiers éléments de `T2`{.language-}
{% endnote %}

### <span id="complexités-colle"></span> Complexités

Allons un peu plus vite :

- on a une boucle `while`{.language-} de `len(T1) + len(T2)`{.language-} itérations
- chaque ligne de l'algorithme est en $\mathcal{O}(1)$

{% note "**Proposition**" %}
La complexité max et min de `colle`{.language-} est $\mathcal{O}(n_1 + n_2)$ avec $n_1$ et $n_2$ les tailles des tableaux `T1`{.language-} et `T2`{.language-} respectivement.
{% endnote %}

## Pseudo-code

Avec notre fonction `combiner(T1, T2)`{.language-} le pseudo code de l'algorithme fusion est :

```python

def fusion(T):
    if len(T) < 2:
        return T
    else:
        milieu = len(T) // 2
        T1 = T[:milieu]
        T2 = T[milieu:]

        T1_trié = fusion(T1)
        T2_trié = fusion(T2)
        T_trié = combiner(T1_trié, T2_trié)
    
        return T_trié 

```

## <span id="preuve-fusion"></span> Preuve

Comme  `milieu < len(T)`{.language-} si `len(T) > 1`{.language-}, l'algorithme va bien converger et s'arrêter. De plus, comme l'algorithme `combiner`{.language-} est démontré, `fusion`{.language-} est bien un algorithme de tri.

## <span id="complexités-fusion"></span> Complexités

La complexité de l'algorithme `fusion`{.language-} est (avec $n$ la taille du tableau passé en entrée) :

$$C(n) = 2 \cdot C(\frac{n}{2}) + D(n)$$

Où :

- $C(n)$ est la complexité de l'algorithme fusion pour une liste à $n$ éléments (algorithme `fusion`{.language-})
- $D(n)$ est la complexité de fusionner deux listes triées en une unique liste triées (algorithme `combiner`{.language-}).

Comme l'algorithme `combiner`{.language-} est en $\mathcal{O}(n)$, l'équation de récurrence de la complexité est :

$$C(n) = 2 \cdot C(\frac{n}{2}) + \mathcal{O}(n)$$

Pour connaître la valeur de la complexité on utilise [le master theorem](https://fr.wikipedia.org/wiki/Master_theorem) qui est **LE** théorème des complexités pour les algorithmes récursifs. Son énoncé nous permet de déterminer aisément la complexité de nombreux algorithmes récursifs :

<span id="master-theorem"></span>
{% note "**Forme O [du master theorem](https://fr.wikipedia.org/wiki/Master_theorem)**" %}

Une complexité de la forme :

<div>
$$
C(n) = a \cdot C(\frac{n}{b}) + \mathcal{O}(n^d)
$$
</div>

Est en :

- $C(n)  = \mathcal{O}(n^d \cdot \ln(n))$ si $a=b^d$ (équivalent à $d = \log_b(a)$)
- $C(n)  = \mathcal{O}(n^{\log_b(a)})$ si $a>b^d$
- $C(n)  = \mathcal{O}(n^d)$ si si $a<b^d$

{% endnote %}
{% details "preuve", "open" %}
Comme $C(n) = a \cdot C(\frac{n}{b}) + \mathcal{O}(n^d)$, il existe $N_0$ tel que pour tout $n \geq N_0$, on a :

<div>
$$
C(n) \leq a \cdot C(\frac{n}{b}) + n^d
$$
</div>

On en conclut que si $C'(n) = a \cdot C'(\frac{n}{b}) + n^d$ alors $C(n) \leq C'(n)$ pour tout $n$ et donc si $C'(n)$ est en $\mathcal{O}(g(n))$, alors $C(n)$ le sera aussi.

<div>
$$
\begin{array}{lcl}
C'(n) &=&a \cdot C'(\frac{n}{b}) + n^d \\
&=& a\cdot (a \cdot C'(\frac{n}{b^2}) + (\frac{n}{b})^d) + n^d\\
&=& a^2 \cdot C'(\frac{n}{b^2}) + n^d \cdot (1 + \frac{a}{b^d})\\
&=& a^2 \cdot (a \cdot C'(\frac{n}{b^3}) + (\frac{n}{b^2})^d) + n^d \cdot (1 + \frac{a}{b^d})\\
&=& a^3 \cdot C'(\frac{n}{b^3}) + n^d \cdot (1 + \frac{a}{b^d} + (\frac{a}{b^d})^2)\\
&=& \dots \\
&=& a^{\log_b(n)}C'(1) + n^d \cdot (\sum_{i=0}^{\log_b(n)}(\frac{a}{b^d})^i)\\
\end{array}
$$
</div>

Comme $a^{\log_b(n)} = \exp(\ln(a) \cdot \frac{\ln(n)}{\ln(b)} ) = \exp(\ln(n) \cdot \frac{\ln(a)}{\ln(b)} ) = n^{\log_b(a)}$ on en conclut, en posant $C'(1) = K$, que :

<div>
$$
C'(n) = K \cdot n^{\log_b(a)} + n^d \cdot \sum_{i=0}^{\log_b(n)}(\frac{a}{b^d})^i
$$
</div>

Il y a alors plusieurs cas. Commençons par étudier le cas où $\frac{a}{b^d} = 1$ (équivalent à $d = \log_b(a)$). Dans ce cas, on a :

<div>
$$
C'(n) = K \cdot n^d + n^d \cdot \sum_{i=0}^{\log_b(n)}1 = n^d(\log_b(n) + K) = \mathcal{O}(n^d \cdot \ln(n))
$$
</div>

Si $\frac{a}{b^d} \neq 1$, on peut utiliser le fait que $\sum_{i=0}^kx^k = \frac{x^{k+1} -1}{x-1}$ (cette formule  se démontre aisément par récurrence  sur $k$ et est super utile dans plein de calculs de complexité, il est bon de la connaître) pour obtenir :

<div>
$$
\begin{array}{lcl}
C'(n) &=& K \cdot n^{\log_b(a)} + n^d \cdot \frac{(\frac{a}{b^d})^{\log_b(n) +1} -1}{\frac{a}{b^d}-1}\\
& = & K \cdot n^{\log_b(a)} + n^d \cdot \frac{\frac{a}{b^d}\cdot\frac{n^{\log_b(a)}}{n^d} -1}{\frac{a}{b^d}-1}\\
& =& K \cdot n^{\log_b(a)} + \frac{\frac{a}{b^d}\cdot n^{\log_b(a)} - n^d}{\frac{a}{b^d}-1} \\
& = & (K + \frac{\frac{a}{b^d}}{\frac{a}{b^d} - 1}) \cdot n^{\log_b(a)} - \frac{1}{\frac{a}{b^d} - 1} \cdot n^d
\end{array}
$$
</div>

On en déduit facilement que :

- $\frac{a}{b^d} < 1$ (équivalent à $\log_b(a) < d$) implique $C'(n) = \mathcal{O}(n^d)$
- $\frac{a}{b^d} > 1$ (équivalent à $\log_b(a) > d$) implique $C'(n) = \mathcal{O}(n^{\log_b(a)})$

{% enddetails %}
{% info %}
Le master theorem est la raison pour laquelle vous verrez parfois des complexités avec des exposants non entiers
{% endinfo %}
Dans notre cas on a $a = 2$, $b = 2$  et $d = 1$ donc $a=b^d$ :

{% note "**Proposition**" %}
La complexité de l'algorithme `fusion`{.language-} est $\mathcal{O}(n\ln(n))$ où $n$ est la taille de la liste en entrée
{% endnote %}
{% details "Calcul de la complexité sans utiliser le master theorem", "open" %}

<div>
$$
\begin{array}{lcl}
C(n) &=& 2 \cdot C(\frac{n}{2}) + \mathcal{O}(n)\\
&=& 2 \cdot (2 \cdot (C(\frac{n}{4}) + \mathcal{O}(\frac{n}{2})) + \mathcal{O}(n)\\
&=& 2^2 \cdot C(\frac{n}{2^2}) + 2 \cdot \mathcal{O}(\frac{n}{2}) + \mathcal{O}(n)\\
&=& 2^2 \cdot C(\frac{n}{2^2}) + 2 \cdot \mathcal{O}(n)\\
&=& ...\\
&=& 2^i \cdot C(\frac{n}{2^i}) + k \cdot \mathcal{O}(n)\\
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

Tout comme le tri par sélection, le tri fusion a la particularité d'avoir toujours le même nombre d'opérations quelque soit la liste en entrée.
