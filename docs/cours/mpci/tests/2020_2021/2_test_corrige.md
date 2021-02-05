---
layout: page
title:  "corrigé Test 2 : complexité"
category: cours
tags: informatique cours 
---

## barême

* 4pt : 1pt par question

## erreurs fréquemment rencontrées

### récursion

Attention la ligne `return n* factorielle(n-1)` n'est **PAS** en $\mathcal{O}(K * C(n-1))$ (avec $C(n)$ la complexité de l'algorithme), c'est en \mathcal{O}(K + C(n-1))$. En effet cette ligne est :

* une multiplication : $\mathcal{O}(1)$
* un appel de fonction en $C(n-1)$ opérations.

On ne multiplie que lorsque l'on effectue plusieurs fois un bloc d'instruction (donc pour une boucle `for` ou un `while`) là on ne fait qu'appeler une fonction.

### la complexité dépend des entrées

Pour l'exercice 3 en particulier, $\mathcal{O}(compteur)$ n'est pas correct car compteur est une variable de l'algorithme et n'est pas une entrée de celui ci (qui sont nombre et exposant). Comme compteur vaut initialement exposant, c'est $\mathcal{O}(exposant)$ qui est une bonne réponse.

### Que vaut n ?

Pour les exercices 3 et 4 en particulier, $\mathcal{O}(n)$ ne veut rien dire si $n$ n'est pas défini.

## 1. itératif

```python
def factorielle( n ):   # O(1)
    f = 1               # O(1)
    while n > 1:        # boucle O(n)
        f = f * n       # O(1)
        n = n - 1       # O(1)
    return f            # O(1)
```

* A chaque étape du bloc `while`, n est décrémenté de 1 : on rentre $\mathcal{O}(n)$ fois dans la boucle.
* Les autres lignes de l'algorithmes sont en $\mathcal{O}(1)$ (affectation, multiplication et soustraction).

La complexité de l'algorihtme est en : $\mathcal{O}(1) + \mathcal{O}(1) +  \mathcal{O}(n) * (\mathcal{O}(1) + \mathcal{O}(1)) + \mathcal{O}(1)$

Ce qui se fimplifie en $\mathcal{O}(n)$

## 2. récursif

```python
def factorielle( n ):                # O(1)
    if n <= 1:                       # O(1)
        return 1                     # O(1)
    return n * factorielle(n-1)      # O(1) + C(n-1)
```

En notant $C(n)$ la complexité de l'algorithme, on obtient l'équation de récurrence : $C(n) = 3 * \mathcal{O}(1) + C(n-1) = \mathcal{O}(1) + C(n-1)$ 

Cette équation a été résolue dans le cours et donne : $C(n) = \mathcal{O}(n)$

## 3. puissance

```python
def puissance(nombre, exposant):     # O(1)
    resultat = 1                     # O(1)
    compteur = exposant              # O(1)
    while compteur > 0:              #  boucle O(exposant)
        resultat *= nombre           # O(1)
        compteur -= 1                # O(1)
    return resultat                  # O(1)
```

Initialement `compteur` vaut `exposant` et à chque itération de la boucle sa valeur est décfrémentée de 1. On rentre donc $\mathcal{O}(exposant)$ fois dans la boucle.

Comme toutes les autres lignes sont en $\mathcal{O}(1)$, la complexité totale de l'algorithme est en $\mathcal{O}(n)$.

## 4. tris

```python
def selection(tab):                                           # O(1)
    for i in range(len(tab) - 1):                             # O(len(tab))
        min_index = i                                         # O(1)
        for j in range(i + 1, len(tab)):                      # O(len(tab) - i) boucle i allant de 0 à len(tab) -2 
            if tab[j] < tab[min_index]:                       # O(1)
                min_index = j                                 # O(1)
        tab[i], tab[min_index] = tab[min_index], tab[i]       # O(1)
```

Deux boucles imbriquées. La seconde boucle est en $\mathcal{O}(len(tab)- i)$ itérations, $i$ étant strictement croissant de $i=0$ à $i = len(tab) - 2$, on peut utiliser l'astuce du cours et dire que cette boucle est exécutée $\mathcal{O}(len(tab))$ fois à chaque fois.

On en conclut que la complexité est en $\mathcal{O}(len(tab) ^2)$