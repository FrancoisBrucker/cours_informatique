---
layout: page
title:  "projet / alignement de séquences"
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [algorithmie]({% link cours/algorithme-code-theorie/algorithme/index.md %}) / [projet : alignement de sequences]({% link cours/algorithme-code-theorie/code/projet-alignement-sequences.md %})
>
> prérequis :
>
>* [projet : fichiers]({% link cours/algorithme-code-theorie/code/projet-fichiers.md %})
>* [étude : alignement de séquences]({% link cours/algorithme-code-theorie/algorithme/etude-alignement-sequences.md %})
>
{: .chemin}


On peut aussi généraliser en supposant que 
> * dot plot : classes qui vont avec
> * coder l'algo (+ test) plus classes qui vont avec
> * comparer les batonnet couleurs
> * méthode de parcimonie entre 2 et généralisation
{: .tbd}



## algorithme

Nous allons créer l'algorithme en plusieurs parties :

1. rendre une fonction de coût élémentaire
2. rendre la matrice d'édition
3. utiliser la matrice d'édition pour connaitre la distance d'édition
4. utiliser la matrice d'édition pour connaitre un alignement optimal

### distance élémentaire

La distance élémentaire doit associer un réel positif à :

* un couple de caractère pour une substitution
* un caractère pour une insertion ou une suppression

Ces informations peuvent être stockées dans un dictionnaire `dist` avec comme clés :

* $(x, y)$ avec $x$ et $y$ deux caractères. On peut de plus supposer que $x \leq y$
* $x$ avec $x$ un caractère

En supposant que l'on ait un dictionnaire `dist` de ce type, il sera plus aisé de d'avoir une fonction de signature `f(x, y=None)` telle que :

* si $x$ et $y$ sont donné, rend `dist[(x, y)]` si $x < y$ et `dist[(y, x)]` sinon.
* si uniquement $x$ est renseigné ($y$ vaut `None`), la fonction devrait rendre $d[x]$.

On peut alors créer une fonction qui prend en paramètre ce dictionnaire et rend une fonction de calcul. Ceci est facile à faire en python, et savoir créer une fonction qui rend une fonction est une compétence qui peut se révéler utile :

```python
def crer_fonction(dist):
    def f(x, y=None):
        if y is None:
            return dist[x]
        elif x < y:
            return dist[(x, y)]
        else:
            return dist[(y, x)]
    return f
```

### matrice d'édition

Maintenant qu'on a la fonction d'édition élémentaire, on peut écrire l'algorithme qui crée la matrice d'édition

```python
def calcul_matrice(a, b, f):
    M = [[0] * len(a) for i in len(b)]
    M[0][0] = 0
    for j in range(len(a)):
        M[0][j] = M[0][j + 1] + f(a[j])
    for i in range(len(b)):
        M[i][0] = M[j + 1][0] + f(b[i])
    
    for i in range(len(b)):
        for j in range(len(a)):
            M[i + 1][j + 1] = min(M[i][j] + f(a[j], b[i]),
                                  M[i + 1][j] + f(b[i]), 
                                  M[i][j + 1] + f(a[j]))

    return M
```

La distance d'édition entre $a$ et $b$ est alors `M[-1][-1]`.

### alignement à partir de la matrice d'édition

La matrice d'édition nous permet de retrouver l'alignement, en *remontant* la matrice.


Ecrivez l'algorithme qui, à partir de deux séquences $a$ et $b$ et d'une distance élémentaire écrite sous forme d'une fonction rend la matrice d'édition.


 permet de rendre la matrice
> écrire l'algorithme + complexité
{: .tbd}


> chemin = alignement
{: .tbd}

