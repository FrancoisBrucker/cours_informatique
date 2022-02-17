---
layout: page
title:  "corrigé Test 2 : complexité et preuve"
category: cours
tags: code python
---


> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [exercices]({% link cours/algorithme-code-theorie/exercices/index.md %}) / [2021-2022]({% link cours/algorithme-code-theorie/exercices/2021-2022/index.md %}) / [corrigé Test 2 : complexité et preuve]({% link cours/algorithme-code-theorie/exercices/2021-2022/2_test_corrige.md %})
{: .chemin}

## barème

La note est sur 5.

1. complexité recherche + complexité autres fonctions : 2pt
2. .5pt
3. preuve recherche + preuve autres fonctions : 2pt
4. .5pt

## erreurs fréquemment rencontrées

> à écrire
{: .tbd}

## 1

### complexité maximum et minimum

Les deux algorithmes ne varient que de 1 test, les deux complexités sont donc égales. On ne calculera que la complexité de `maximum` :

<style>
    table, td, tr, th, pre {
        padding:0;
        margin:0;
        border:none
    }
</style>
{% highlight python linenos %}
def maximum(T):
    m = 0
    for i in range(len(T)):
        if T[m] < T[i]:
            m = i
    return m

{% endhighlight %}

On note $n$ la longueur du tableau.

Ligne à ligne :

1. affectation des paramètres : $\mathcal{O}(1)$
2. affectation d'une variable : $\mathcal{O}(1)$
3. boucle de $n$ itérations
4. un test et une comparaison : $\mathcal{O}(1)$
5. une affectation : $\mathcal{O}(1)$
6. retour de fonction : $\mathcal{O}(1)$

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

On en conclut que la complexité des algorithmes `maximum` et `minimum` ne dépendent que de la taille de `T` et vaut $\mathcal{O}(n)$

### complexité de copie

<style>
    table, td, tr, th, pre {
        padding:0;
        margin:0;
        border:none
    }
</style>
{% highlight python linenos %}
def copie(T):
    nouveau = []
    for x in T:
        nouveau.append(x)

    return nouveau

{% endhighlight %}

On note $n$ la longueur du tableau.

Ligne à ligne :

1. affectation des paramètres : $\mathcal{O}(1)$
2. affectation d'une variable : $\mathcal{O}(1)$
3. boucle de $n$ itérations
4. on ajoute un élément en fin de tableau : $\mathcal{O}(1)$
5. retour de fonction : $\mathcal{O}(1)$

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

On en conclut que la complexité des algorithmes `copie`  ne dépend que de la taille de `T` et vaut $\mathcal{O}(n)$

### complexité recherche

<style>
    table, td, tr, th, pre {
        padding:0;
        margin:0;
        border:none
    }
</style>
{% highlight python linenos %}
def recherche(T, k):
    max_value = T[maximum(T)]

    T_copie = copie(T)
    for i in range(k - 1):
        min = minimum(T_copie)
        T_copie[min] = max_value + 1

    return minimum(T_copie)

{% endhighlight %}

Ligne à ligne :

1. affectation des paramètres : $\mathcal{O}(1)$
2. en deux temps :
   1. exécution de la fonction `maximum(T)` : $C_\mbox{maximum}(T)$
   2. affectation d'une variable à un élément d'un tableau : $\mathcal{O}(1)$
3. 
4. affection d'une variable au résultat de la fonction `copie(T)` : $\mathcal{O}(1) + C_\mbox{copie}(T)$
5. boucle for de $k-1$ itérations
6. affection d'une variable au résultat de la fonction `minimum(T_copie)` : $\mathcal{O}(1) + C_\mbox{mininmum}(\mbox{T_copie})$
7. affectation d'un élément d'un tableau : $\mathcal{O}(1)$
8. 
9. en deux temps :
   1. exécution de la fonction `minimum(T_copie)` : $C_\mbox{mininmum}(\mbox{T_copie})$
   2. retour de la fonction $\mathcal{O}(1)$

La complexité de l'algorithme est alors, avec $n$ la taille du tableau `T` :

$$
\begin{array}{lcl}
C(n) &=& \mathcal{O}(1) + \\
&& C_\mbox{maximum}(T) + \mathcal{O}(1) +\\
&& \mathcal{O}(1) + C_\mbox{copie}(T) +\\
&& (k - 1)\cdot (\\
&& \mathcal{O}(1) + C_\mbox{mininmum}(\mbox{T_copie}) +\\
&& \mathcal{O}(1)) +\\
&& \mathcal{O}(1) + C_\mbox{mininmum}(\mbox{T_copie})\\
&=& 4 \cdot \mathcal{O}(1) + \\
&& C_\mbox{maximum}(T) + C_\mbox{copie}(T) + C_\mbox{mininmum}(\mbox{T_copie}) + \\
&& (k-1) \cdot(2 \mathcal{O}(1) + C_\mbox{mininmum}(\mbox{T_copie}))\\
&=& \mathcal{O}(k) + \\
&& C_\mbox{maximum}(T) + C_\mbox{copie}(T) + \\
&& k \cdot C_\mbox{mininmum}(\mbox{T_copie}) \\
\end{array}
$$

En reprenant les complexités des algorithmes `minimum`, `maximum` et `copie`, et en notant $n$ la taille du tableau `T`, on a :

$$
\begin{array}{lcl}
C(n) &=& \mathcal{O}(k) + \\
&& C_\mbox{maximum}(T) + C_\mbox{copie}(T) + \\
&& k \cdot C_\mbox{mininmum}(\mbox{T_copie}) \\
&=& \mathcal{O}(k) + \mathcal{O}(n) + \mathcal{O}(n) + k\cdot\mathcal{O}(n)\\
&=&  \mathcal{O}(k\cdot n)\\
\end{array}
$$

## 2

On utilise l'algorithme `copie` pour ne pas modifier les données initiales (on change les valeurs du tableau en ligne 70)

## 3

### copie

On peut utiliser l'invariant de boucle : *au bout de la $k$ème itération, `nouveau`contient les $i$ premiers éléments de `T`* pour démontrer que `nouveau` continent tous les éléments du tableau passé en paramètre.

### maximum et minimum

On peut utiliser l'invariant de boucle : *au bout de chaque itération `m` contient l'**indice** de l'élément maximum (respectivement minimum) des $i$ premières cases de `T`* pour démontrer que `maximum` (respectivement `minimum`) rendra l'indice du p^lus grand (respectivement plus petit) élément de `T`.

### recherche

L'invariant suivant peut être démontré :

Au bout de chaque itération :

* les cases des $i+1$ plus petits éléments de `T` contiennent la valeur `max_value + 1` pour `T_copie`,
* les valeurs des autres cases de `T_copie` sont identiques à celles de `T`

## 4

La médiane d'un tableau revient à chercher le $\frac{n}{2}$ ème plus petit élément d'un tableau de taille $n$ : c'est le résultat de `recherche(T, len(T)//2)`et est de complexité : $\mathcal{O}(n^2)$
