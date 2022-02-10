---
layout: page
title:  "corrigé Test 2 : complexité et preuve"
category: cours
tags: code python
---


Toute tentative d'enfumage sera sanctionnée avec des points en moins :

* soyez précis et correct
* justifiez toutes vos réponses

On considère le code suivant :

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


def maximum(T):
    m = 0
    for i in range(len(T)):
        if T[m] < T[i]:
            m = i
    return m


def minimum(T):
    m = 0
    for i in range(len(T)):
        if T[m] > T[i]:
            m = i
    return m


def recherche(T, k):
    max_value = T[maximum(T)]

    T_copie = copie(T)
    for i in range(k - 1):
        min = minimum(T_copie)
        T_copie[min] = max_value + 1

    return minimum(T_copie)

{% endhighlight %}

## 1

Donnez la complexité de la fonction `recherche(T, k)`

> Pour calculer la complexité de la fonction recherche, il vous faudra également calculer les complexités des fonctions utilisées par celle-ci.
{: .attention}

## 2

Quel est l'intérêt de la fonction `copie(T)` ?

## 3

Démontrez que la fonction `recherche(T, k)` rend l'indice du $k$ème plus petit élément de $T$.

> Pour démontrer ce que fait recherche, il vous faudra également trouver et démontrer ce que font les fonctions utilisées par celle-ci.
{: .attention}

## 4

Utilisez `recherche(T, k)` pour créer un algorithme déterminant l'indice de la médiane d'un tableau. Quelle est sa complexité ?
