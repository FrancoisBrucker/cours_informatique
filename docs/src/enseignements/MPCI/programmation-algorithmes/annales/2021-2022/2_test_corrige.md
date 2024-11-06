---
layout: layout/post.njk

title:  "corrigé Test 2 : complexité et preuve"
authors:
    - François Brucker
---

## Barème

La note est sur 4.

1. complexité recherche + complexité autres fonctions : 3pt
2. 1pt
3. preuve recherche + preuve autres fonctions : 1pt (bonus)
4. 1pt (bonus)

Les questions 3 et 4 n'ont pratiquement jamais été traitées, alors que la question 4 était facile.

La ventilation des notes est :

|note  | 1  | 1.5 | 2.5 | 2.75| 3   |3.25 | 3.5 |3.75 | 4 |
-------|----|-----|-----|-----|-----|-----|-----|-----|---|
|nombre|1   |2    |2    |1    |6    |1    |  2  |  17 |14 |
|rang  |46  | 44  | 42  | 41  | 35  |34   |32   | 15  | 1 |

Pour une moyenne de 3.5 et un écart-type de 0.7.

## Erreurs fréquemment rencontrées

Attention, $k$ fait partie des données de l'algorithme. Pour une taille de tableau de $n$, Donner une complexité de $\mathcal{O}(kn)$ dans la question 1 est donc plus précis qu'une complexité de $\mathcal{O}(n^2)$, $k$ pouvant varier de $1$ à $n$.

## 1

### Complexité maximum et minimum

Les deux algorithmes ne varient que de 1 test, les deux complexités sont donc égales. On ne calculera que la complexité de `maximum`{.language-} :

```python/
def maximum(T):
    m = 0
    for i in range(len(T)):
        if T[m] < T[i]:
            m = i
    return m

```

On note $n$ la longueur du tableau.

Ligne à ligne :

1. affectation des paramètres : $\mathcal{O}(1)$
2. affectation d'une variable : $\mathcal{O}(1)$
3. boucle de $n$ itérations
4. un test et une comparaison : $\mathcal{O}(1)$
5. une affectation : $\mathcal{O}(1)$
6. retour de fonction : $\mathcal{O}(1)$

<div>
$$
\begin{array}{lcl}
C(n) &=& \mathcal{O}(1) + \\
&& \mathcal{O}(1) + \\
&& n \cdot(\\
&& \mathcal{O}(1) + \\
&& \mathcal{O}(1)) + \\
&& \mathcal{O}(1) \\
&=& 3\cdot\mathcal{O}(1) + n\cdot (2\cdot\mathcal{O}(1)) \\
&=& \mathcal{O}(n)\\
\end{array}
$$
</div>

On en conclut que la complexité des algorithmes `maximum`{.language-} et `minimum`{.language-} ne dépendent que de la taille de `T`{.language-} et vaut $\mathcal{O}(n)$

### Complexité de `copie`{.language-}

```python/
def copie(T):
    nouveau = []
    for x in T:
        nouveau.append(x)

    return nouveau
```

On note $n$ la longueur du tableau.

Ligne à ligne :

1. affectation des paramètres : $\mathcal{O}(1)$
2. affectation d'une variable : $\mathcal{O}(1)$
3. boucle de $n$ itérations
4. on ajoute un élément en fin de tableau : $\mathcal{O}(1)$
5. retour de fonction : $\mathcal{O}(1)$

<div>
$$
\begin{array}{lcl}
C(n) &=& \mathcal{O}(1) + \\
&& \mathcal{O}(1) + \\
&& n \cdot(\\
&& \mathcal{O}(1)) + \\
&& \mathcal{O}(1) \\
&=& 3\cdot\mathcal{O}(1) + n \cdot(\mathcal{O}(1)) \\
&=& \mathcal{O}(n)\\
\end{array}
$$
</div>

On en conclut que la complexité des algorithmes `copie`{.language-} ne dépend que de la taille de `T`{.language-} et vaut $\mathcal{O}(n)$

### Complexité de `recherche`{.language-}

```python/
def recherche(T, k):
    max_value = T[maximum(T)]

    T_copie = copie(T)
    for i in range(k - 1):
        min = minimum(T_copie)
        T_copie[min] = max_value + 1

    return minimum(T_copie)
```

Ligne à ligne :

1. affectation des paramètres : $\mathcal{O}(1)$
2. en deux temps :
   1. exécution de la fonction `maximum(T)`{.language-} : $C_\mbox{maximum}(T)$
   2. affectation d'une variable à un élément d'un tableau : $\mathcal{O}(1)$
3. —
4. affection d'une variable au résultat de la fonction `copie(T)`{.language-} : $\mathcal{O}(1) + C_\mbox{copie}(T)$
5. boucle for de $k-1$ itérations
6. affection d'une variable au résultat de la fonction `minimum(T_copie)`{.language-} : $\mathcal{O}(1) + C_{\mbox{minimum}}(T_\mbox{copie})$
7. affectation d'un élément d'un tableau : $\mathcal{O}(1)$
8. —
9. en deux temps :
   1. exécution de la fonction `minimum(T_copie)`{.language-} : $C_{\mbox{minimum}}(T_\mbox{copie})$
   2. retour de la fonction $\mathcal{O}(1)$

La complexité de l'algorithme est alors, avec $n$ la taille du tableau `T`{.language-} :

<div>
$$
\begin{array}{lcl}
C(n) &=& \mathcal{O}(1) + \\
&& C_\mbox{maximum}(T) + \mathcal{O}(1) +\\
&& \mathcal{O}(1) + C_\mbox{copie}(T) +\\
&& (k - 1)\cdot (\\
&& \mathcal{O}(1) + C_\mbox{minimum}(T_\mbox{copie}) +\\
&& \mathcal{O}(1)) +\\
&& \mathcal{O}(1) + C_\mbox{minimum}(T_\mbox{copie})\\
&=& 4 \cdot \mathcal{O}(1) + \\
&& C_\mbox{maximum}(T) + C_\mbox{copie}(T) + C_\mbox{minimum}(T_\mbox{copie}) + \\
&& (k-1) \cdot(2 \mathcal{O}(1) + C_\mbox{minimum}(T_\mbox{copie}))\\
&=& \mathcal{O}(k) + \\
&& C_\mbox{maximum}(T) + C_\mbox{copie}(T) + \\
&& k \cdot C_\mbox{minimum}(T_\mbox{copie}) \\
\end{array}
$$
</div>

En reprenant les complexités des algorithmes `minimum`{.language-}, `maximum`{.language-} et `copie`{.language-}, et en notant $n$ la taille du tableau `T`{.language-}, on a :

<div>
$$
\begin{array}{lcl}
C(n) &=& \mathcal{O}(k) + \\
&& C_\mbox{maximum}(T) + C_\mbox{copie}(T) + \\
&& k \cdot C_\mbox{minimum}(T\mbox{copie}) \\
&=& \mathcal{O}(k) + \mathcal{O}(n) + \mathcal{O}(n) + k\cdot\mathcal{O}(n)\\
&=&  \mathcal{O}(k\cdot n)\\
\end{array}
$$
</div>

## 2

On utilise l'algorithme `copie`{.language-} pour ne pas modifier les données initiales (on change les valeurs du tableau en ligne 70)

## 3

### copie

On peut utiliser l'invariant de boucle : *au bout de la $k$ème itération, `nouveau`{.language-} contient les $i$ premiers éléments de `T`* pour démontrer que `nouveau`{.language-} continent tous les éléments du tableau passé en paramètre.

### maximum et minimum

On peut utiliser l'invariant de boucle : *au bout de chaque itération `m`{.language-} contient l'**indice** de l'élément maximum (respectivement minimum) des $i$ premières cases de `T`{.language-}* pour démontrer que `maximum`{.language-} (respectivement `minimum`{.language-}) rendra l'indice du plus grand (respectivement plus petit) élément de `T`{.language-}.

### recherche

L'invariant suivant peut être démontré :

Au bout de chaque itération :

* les cases des $i+1$ plus petits éléments de `T`{.language-} contiennent la valeur `max_value + 1`{.language-} pour `T_copie`{.language-},
* les valeurs des autres cases de `T_copie`{.language-} sont identiques à celles de `T`{.language-}

## 4

La médiane d'un tableau revient à chercher le $\frac{n}{2}$ ème plus petit élément d'un tableau de taille $n$ : c'est le résultat de `recherche(T, len(T)//2)`{.language-} et est de complexité : $\mathcal{O}(n^2)$
