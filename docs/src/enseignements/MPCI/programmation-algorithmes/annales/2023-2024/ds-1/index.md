---
layout: layout/post.njk
title: "DS 1"
---

{% note "**Sujet**" %}

[Étude de l'élément majoritaire](./ds1_2023_2024.pdf){.fichier}

Durée du contrôle : 3h.

{% endnote %}

## Barème

> TBD

## Corrigé

### Exercice 1 : encadrement du problême

#### 1.1

Il ne peut y avoir qu'un seul élément majoritaire car il contient strictement plus de la moitié des éléments.

#### 1.2.1

Pour tout $n > 2$ on a $\frac{n}{2} + 1 < n$, on peut donc créer un tableau de taille $n$ ayant un deux valeurs distinctes et un élément majoritaire. On peut alors toujour s'arranger pour que $T[i]$ ne soit pas l'élément majoritaire.

#### 1.2.2

Le tableau avec une unique valeur répond trivialement à la question.

#### 1.2.3

La question 1.2.1 nous montre que l'on peut créer un tableau possédant un élément majoritaire et tel que $T[i]$ ne soit pas cet élément. On peut de plus s'arranger pour que cet élément majoritaire soit exactement présent la partie entière de $\frac{n}{2}$ plus 1 fois (on remplace si nécessaire les éléments surnuméraires par $T[i]$).

Le tableau $T'$ tel que :

- $T[j] = T'[j]$ pour tout $j \neq i$
- $T'[i]$ vaut l'élément majoritaire de $T$

Répond à la question.

#### 1.2.4

On procède comme dans le cours pour démontrer [la complexité du problème de la recherche](/cours/algorithmie/complexité-problème/#complexité-recherche).

On suppose qu'il existe un algorithme prenant strictement moins que $n$ opérations pour trouver l'élément majoritaire de tout tableau de taille $n > N_0$. Prenons un tableau $T$ comme dans la question précédente. On a alors deux cas :

- soit l'algorithme a parcouru toutes les cases de $T$ possédant l'élément majoritaire et il a eu besoin d'au moins $\frac{n}{2} + 1 = \Omega(n)$ opérations,
- soit il n'a pas parcouru toutes les cases de $T$ possédant l'élément majoritaire, disons $T[i]$, et on crée le tableau $T'$ identique à $T$ sauf pour la case d'indice $i$ : $T'$ ne possède pas d'élément majoritaire mais l'algorithme va donner la même réponse que pour $T$. Contradiction.

#### 1.3.1

```python

def compte(T, x):

    nombre = 0
    for element in T:
        if element == x:
            nombre += 1
    return nombre
```

La complexité de la fonction est en $\mathcal{O}(n)$ où $n$ est la taille de $T$ puisque :

- toutes les lignes sont de complexité $\mathcal{O}(1)$
- la boucle `for`{.language-} est exécutée la taille de $T$ fois, c'est à dire $\mathcal{O}(n)$ fois.

L'invariant de boucle que l'on va utiliser pour prouver l'algorithme `compte`{.language-} est : au bout de la $i$ ème itération, `nombre`{.language-} vaut le nombres de fois où `x`{.language-} est présent dans les $i$ premières cases de $T$.

1. l'invariant est clairement vérifié à la fin de la première itération
2. si l'invariant est vérifié à la fin de la $i$ ème itération, , comme la $i+1$ itération vérifie si `x == T[i]`{.language-} et ajoute 1 à `nombre`{.language-} si c'est le cas, l'invariant est toujours vérifié à la fin de la $i + 1$ ème itération.
3. l'invariant est vrai en sortie de boucle, c'est à dire après avoir parcouru tous les éléments de $T$ : `nombre`{.language-} vaut bien le nombre de fois où `x`{.language-} est présent dans $T$.

#### 1.3.2

```python#

def élément_majoritaire(T):
    for x in T:
        if compte(T, x) > len(T) / 2:
            return x
    return None
```

Le test de la ligne 4 est en $\mathcal{O}(n)$ où $n$ est la taille de $T$ puisqu'il faut exécuter `compte`{.language-}. Toutes les autres lignes sont de complexité $\mathcal{O}(1)$ et comme la boucle `for`{.language-} est exécutée la taille de $T$ fois, on exécute `compte`{.language-} $n$ fois ce qui porte la complexité de l'algorithme à $\mathcal{O}(n^2)$.

L'invariant de boucle que l'on va utiliser pour prouver l'algorithme `élément_majoritaire`{.language-} est : au bout de la $i$ ème itération,aucun des $i$ premières cases de $T$ n'est un élément majoritaire.

1. l'invariant est clairement vérifié à la fin de la première itération
2. si l'invariant est vérifié à la fin de la $i$ ème itération, comme la $i+1$ itération vérifie si `T[i]`{.language-} est un élément majoritaire, l'invariant est toujours vérifié à la fin de la $i + 1$ ème itération.
3. l'invariant est vrai en sortie de boucle, c'est à dire après avoir parcouru tous les éléments de $T$ : si on arrive en ligne 6, c'est que $T$ n'a pas d'élément majoritaire. Si l'on s'arrête à la fin de la $i$ ème itération c'est que `T[i-1]`{.language-} est l'élément majoritaire de $T$.

#### 1.3.3

En utilisant le premier tableau, la fonction va parcourir tous les éléments de $T$ et pour chacun effectuer la fonction `compte`{.language-} sans trouver d'élément présent 5 fois ou plus.

En utilisant le premier tableau, la fonction sortir au bout de la première itération puisque 2 est l'élément majoritaire de $T$.

#### 1.3.4

L'algorithme de la question 1.3.2 résoud le problème de la recherche d'un élément majoritaire, sa complexité est donc un majorant de la complexité du problème.

### Exercice 2 : Tris

### Exercice 3 : Diviser pour régner

### Exercice 4 : Piles
