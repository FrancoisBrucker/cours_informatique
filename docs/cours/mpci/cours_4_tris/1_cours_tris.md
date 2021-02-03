---
layout: page
title:  "Méthodes de tris"
category: cours
tags: informatique cours 
---

## Introduction

On verra quelques algorithmes de tris et cela nous permettra de parler de complexité min/ max et en moyenne.

En plus, les tris c'est chouette parce qu'il y a [plein de façon de trier](https://fr.wikipedia.org/wiki/Algorithme_de_tri)

## différentes complexités

Les méthodes des tri vont nous permettre d'introduire différentes notions de complexité.

On va prendre l'exemple de la recherche d'un élément dans une liste :

```python
def recherche(element, liste):
    for x in liste:
        if element == x:
            return True
    return False
```

La fonction `recherche` va rendre `True` si l'entrée `element` est dans la liste en entrée nommée `liste`.

On voit que le nombre d'opérations va varier selon la taille de `liste` et si `element` est dans la liste ou non.

### complexité ou complexité maximale

Lorsque l'on parle de *complexité* sans rien ajouter c'est **toujours** de la *complexité maximale* dont on parle. C'est à dire le nombre d'opérations maximale mesurée en $\mathcal{O}$ qu'effectue la fonction pour une taille d'entrée donnée. On donnera également une entrée particulière réalisant cette complexité.

Pour la fonction `recherche` la **complexité maximale** est atteinte lorsque tous les éléments de `liste` sont parcourus sans trouver `element`.

Donc : la complexité de recherche est $\mathcal{O}(n)$  où $n$ est la longueur de `liste` et elle est atteinte pour une `liste` ne contenant pas `element`.

On voit qu'on a :

* donné la complexité de la fonction en fonction de la taille des entrées (ici la taille de la liste)
* on a donné un exemple d'entrée réalisant cette complexité : une `liste` de taille quelconque ne contenant pas `element`.

> On ne peut pas juste donner une taille de liste particulière come exemple. Il faut que tous les paramètres de la complexité (ici uniquement la taille), puisse varier jusqu'à l'infini.

### complexité minimale

La *complexité minimale*  nombre d'opérations minimale mesurée en $\mathcal{O}$ qu'effectue la fonction pour une taille d'entrée donnée.

C'est à dire que l'on cherche une entrée particulière qui va produire le moins d'opérations possible.

Pour la fonction `recherche` la **complexité minimale** est atteinte lorsque `element` est le premier élément de `liste`.

Donc : la **complexité minimale** de recherche est $\mathcal{O}(1)$   et elle est atteinte pour une `liste` de taille quelconque dont le premier élément est `element`.

### complexité en moyenne

La complexité en moyenne est calculée en considérant le nombre d'opérations moyenne pris pour toutes les entrées d'une taille fixée.

Pour pouvoir la calculer, il faut se donner un modèle aléatoire de données et calculer l'espérance (la moyenne) du nombre d'opérations pour ce modèle.

POur recherche, regardons combien d'opérations va prendre notre algorithme selon la position de `element` dans `liste`. On voit rapidement que si `element` est à la $i$ème position de `liste` le nombre d'opérations va être proportionnelle à $i$, disons $K * i$ opérations.

Le nombre d'opérations moyen est alors :

$$\sum_{i=0}^{i < n} (p_i * K * i)$$

Où $p_i$ est la probabilité qu'`element` soit à la $i$ème position de `liste`. Comme on a aucune raison de privilégier une position par rapport à une autre, on considère que notre modèle de donnée est équi-probable et donc que $p_i = \frac{1}{n}$  pour tout $i$. La complexité en moyenne vaut alors :

$$\sum_{i=0}^{i < n}() \frac{1}{n} * K * i )= \frac{K}{n}\sum_{i=0}^{i < n} i = \frac{K * (n-1)}{2} = \mathcal{O}(n)$$

La complexité en moyenne est égale à la complexité : il y a beaucoup plus de cas où la complexité effective est proche de la complexité maximale que de la complexité minimale.

> **Remaque** : pour aller plus vite, on aurait pu dire que si notre modèle est équiprobable, `element` va se trouver en moyenne au milieu de notre tableau, et donc qu'il faut parcourir de l'ordre de $\frac{n}{2}$ éléments de `liste`, la complexité en moyenne est de $\mathcal{O}(n/2) = \mathcal{O}(n)$. Attention cependant, c'est un raccourci...Faites très attention à ne pas vous tromper. Si vous avez un doute, faites le calcul effectif.
Par exemple, pour un modèle de données où nos données sont toujours tries ou juste quelques inversions : la complexité en moyenne va être $\mathcal{O}(n)$.

La complexité en moyenne est très importante en pratique puisque c'est celle là que vous allez la plupart du temps avoir lorsque vous exécuterez votre fonction.

De plus, lorsque vous mesurez le temps d'exécution d'une fonction avec des paramètres aléatoires, c'est cette complexité là que vous mesurez, **pas** la complexité maximale.

## tris simple

### tri par sélection

En entrée, un tableau `tab` remplit de nombre et de taille $n$ :

```python
def selection(tab):
    for i in range(len(tab) - 1):
        min_index = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[min_index]:
                min_index = j
        tab[i], tab[min_index] = tab[min_index], tab[i]

```

#### preuve que sélection trie

Il y a 2 boucles imbriquées. La raison d'être de la boucle faisant varier j est de faire en sorte que `min_index` soit l'indice de de la plus petite valeur du tableau pour les indices plus grand que $i$.

Ensuite on échange cette valeur avec celle initialement à l'indice $i$.

Notre invariant de boucle peut donc être : _"à la fin de chaque étape $i$ de l'algorithme les $i$ plus petites valeurs du tableaux sont triées aux $i$ premiers indices du tableau"_

#### complexités du tri par sélection

deux boucles imbriquées :

* la boucle extérieure est en $\mathcal{O}(n)$
* la boucle intérieure est d'itérations variables mais décroissantes de $n$ à 1 itérations : on utilise la règle qui dit que globalement, sa complexité est donc en nombre d'itérations max : $\mathcal{O}(n)$.

L'échange étant en $\mathcal{O}(1)$ la complexité totales est en $\mathcal{O}(n) * \mathcal{O}(n) = \mathcal{O}(^2)$.

Le nombre d'itérations n'est pas dépendant du tableau.

### tri par insertion

en entrée, un tableau `tab` remplit de nombre et de taille $n$.

```python
def insertion(tab):
    for i in range(1, len(tab)):
        actu = tab[i]
        j = i
        while j > 0 and tab[j - 1] > actu:
            tab[j] = tab[j - 1]
            j -= 1
        tab[j] = actu
```

#### preuve qu'insertion trie

A chaque itération $i$ l'algorithme remonte la valeur initialement en position $i$ à la première position pour laquelle il est plus grand que le précédent. Remarquez bien que nous n'avons jamais changé les différentes valeurs du tableau.

Notre invariant de boucle peut donc être : _"à la fin de l'itération i, les i premiers éléments du tableau sont triés"_

#### complexités du tri par insertions

La complexité va changer selon la nature du tableau :

* si le tableau est déjà trié : je ne rentre jamais dans la boucle du *tant que* : la complexité est en $\mathcal{O}(n)$
* si le tableau est trié à l'envers : on effectue à chaque itération $i$, $i$ étapes dans la boucle du *tant que* : la complexité est en $\mathcal{O}(n^2)$

Ceci est problématique. La complexité (le cas le pire) arrive-t-elle souvent ou pas pour des données "normales" ?

Pour le savoir, on calcule la complexité en moyenne de notre algorithme. La complexité en moyenne dépend d'un modèle de donnée.

Par exemple, pour un modèle de données où nos données sont toujours tries ou juste quelques inversions : la complexité en moyenne va être $\mathcal{O}(n)$.

Souvent, pour la complexité en moyenne on considère des données aléatoires. C'est à dire que tout peut se passer de façon équiprobable : dans notre cas, au doigt mouillé, ça veut dire que notre boucle tant que va tout le temps remonter de la moitié de ce qui est possible (donc $i /2$ opérations) : pour un élément donné (aléatoire) il y a autant de nombre plus petit que lui que de nombre plus grand.

En moyenne, la boucle *tant que* effectue donc un nombre d'itérations égal à $i /2$ : ça croit de 1 à $n/2$ : elle est donc de complexité $\mathcal{O}(n)$. Au final, la complexité moyenne de l'algorithme est donc en $\mathcal{O}(n^2)$

Pour notre algorithme cela veut dire que le cas le meilleur arrive très rarement par rapport au cas le pire (parmi les $n!$ ordres possible, il y en a très peut qui sont presque triés).

> **Remarque** : Vous allez le prouver expérimentalement pendant la session de code.

### différence de traitement des données ?

Chaque tri a une façon bien à lui de trier les objets. C'est pour ça qu'un informaticien aime les tris : il a plein de façon différente de faire.

On va le *voir*.

On dessine le tableau à chaque modification de celui-ci. On voit la différence de traitement des algorithmes de tris.

Exemple pour le tri par insertion/sélection. On a tout mis dans un unique fichier *"main.py"* :

```python
import random

import matplotlib.pyplot as plt


def draw_tab(tab):
    plt.cla()  # on efface le dessin 
    plt.plot(tab, 'ro')
    plt.pause(0.1) # on pause le dessin
    


def selection(tab):
    for i in range(len(tab) - 1):
        min_index = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[min_index]:
                min_index = j
        tab[i], tab[min_index] = tab[min_index], tab[i]
        draw_tab(tab)


def insertion(tab):
    for i in range(1, len(tab)):
        actu = tab[i]
        j = i
        while j > 0 and tab[j - 1] > actu:
            tab[j] = tab[j - 1]
            draw_tab(tab)
            j -= 1
        tab[j] = actu
        draw_tab(tab)


tab = list(range(30))
random.shuffle(tab)

print(tab)
plt.plot(tab, 'ro')
# selection(tab)
insertion(tab)
plt.show()

print(tab)
```

## complexité du tri ?

Mais au final, parmi tous les algorithmes de tris, c'est les quels qui vont le plus vite ? Et est-ce le minimum possible ?

nombre de cas différents que peut traiter un algorithme : Dépend du nombre de tests que fait l'algorithme pour pouvoir les différentier :

* 0 test -> 1 cas (l'algorithme répond toujours la même chose)
* 1 test -> 2 cas
* 2 tests -> $4 = 2^2$ cas
* p tests -> $2^p$ cas

Si on veut distinguer $n$ cas il faut ainsi au moins $\ln_2(n)$ tests. Donc un algorithme qui doit traiter $n$ cas différents aura au moins une complexité de $\mathcal{O}(\ln_2(n))$ opérations (les tests).

Nombre de cas différents pour trier tri une liste de $n$ éléments ? Toutes les permutations possibles donc $n!$ façons de ranger $n$ éléments. 

comme $n! = n * (n-1) * (n-2) * \dots * 2 * 1$, on arrive à obtenir l'encadrement suivant :

* comme $n$ est plus grand que tous les éléments du produit on à $n! \leq n^n$
* comme $n! \geq n * (n-1) * ... * (n/2 + 1) * (n/2)$ et que  $n/2$ est plus petit que les éléments du produit, on a $n! > (n/2)^{(n/2)}$

donc : 

* $(n/2)^{(n/2)} \leq n! \leq n^n$
* en passant au log : $\ln_2 ((n/2)^{(n/2)}) <= \ln_2(n!) <= \ln_2 (n^n)$
* donc $n/2 * \ln_2 (n/2) <= \ln_2(n!) <= n \ln_2(n)$

Comme $\ln_2 (n/2) = \ln_2 (n) + \ln_2(1/2) = \ln_2 (n) - \ln_2(2) = \ln_2 (n) - 1$, on a que :

$$\frac{1}{2} n\ln(n) - \frac{n}{2} \leq \ln(n!) \leq n\ln_2(n)$$

Ce qui donne :

$$\frac{1}{2} - \frac{1}{\ln_2(n)} \leq \frac{\ln(n!)}{n\ln_2(n)} \leq 1$$

Et puisque pour tout $n > 4$  on a que $\ln_2(n) > 2$, on a pour $n > 4$ :

$$\frac{1}{4} \leq \frac{\ln(n!)}{n\ln_2(n)} \leq 1$$

Cette inégalité nous permet facilement de montrer qu'une fonction en $\mathcal{O}(\ln_2(n!))$ sera aussi en $\mathcal{O}(n \ln_2(n))$ et donc qu'il faut au moins $\mathcal{O}(n \ln_2(n))$ tests pour distinguer parmi $n!$ possibilités.

**Conclusion** : Tout algorithme de tri aura une complexité de au moins $\mathcal{O}(n \ln_2(n))$  opérations.

Pour finir, notez qu'il existe des algorithmes de tri en $\mathcal{O}(n \ln_2(n))$  opérations comme le [tri fusion par exemple](https://fr.wikipedia.org/wiki/Tri_fusion) par exemple.

> **Remarque** : le tri est le cas heureux d'un problème dont on connaît la complexité (c'est à dire que l'on a un algorithme de cmplexité (maximale) minimale). Ce n'est pas le cas pour tous les problèmes. Genre la [multiplication de matrices](https://fr.wikipedia.org/wiki/Produit_matriciel), ou une borne min est de $\mathcal{O}(n^2)$ (avec $n$ le nombre de lignes de la matrice), mais on ne sait pas s'il existe des algorithme pour le faire. Le mieux que l'on sait faire pour l'instant c'est en $\mathcal{O}(n^{2.376})$.

## tri rapide

Le tri rapide est une méthode de tri d'une liste à $n$ éléments dont :

* la complexité (maximale) est $\mathcal{O}(n^2)$,
* la complexité en moyenne est $\mathcal{O}(n\ln_2 (n))$,
* la complexité minimale est $\mathcal{O}(n\ln_2 (n))$,

```python
def rapide(tab):
    if len(tab) <= 1:
        return tab

    pivot = tab[0]

    tab_gauche = [tab[i] for i in range(1, len(tab)) if tab[i] <= pivot]
    tab_droite = [tab[i] for i in range(1, len(tab)) if tab[i] > pivot]

    return rapide(tab_gauche) + [pivot] + rapide(tab_droite)
```

On utilise les [list comprehension](https://python.doctor/page-comprehension-list-listes-python-cours-debutants) de python. C'est un moyen clair et efficace de générer des listes.

### preuve du tri rapide

* `tab_gauche` contient tous les élements du tableau d'indice `> 0` et plus petit ou égal à `pivot` qui est égal à `tab[0]`
* `tab_droite` contient tous les élements du tableau d'indice `> 0` et plus plus grand strictement à `pivot`
 
Si rapide fonctionne pour des tableaux de longeurs strictement plus petit que $n$, il fonctionne également pour des tableaux de longueur $n$ : le tableau rendu est le tableau des valeurs plus petite que `pivot` triées (ce tableau est de longueur `< n`, donc c'est trié par hypothèse de récurence) + `[pivot]` + le tableau des valeurs plus grande que `pivot` triées (ce tableau est de longueur `< n`, donc c'est trié par hypothèse de récurence)

On il fonctionne pour des tableau de longueur 0 ou 1, donc par récurrence, c'est ok.

### complexités du tri rapide

Nous n'allons pas faire ici de calcul rigoureux. Si ça vous intéresse, reportez vous là : <http://perso.eleves.ens-rennes.fr/~mruffini/Files/Other/rapide.pdf>

En notant $n$ la taille de la liste on a comme équation de récurrence pour la complexité $C(n)$ :

$$C(n) = \mathcal{O}(n) + C(n_1) + C(n_2)$$

Où $n_1$ est la taille du tableau de gauche et $n_2$ celle de droite ($n_1 + n_2 = n$)

On voit que la complexité du tri rapide tient dans le nombre de récursions qui est fait.

#### complexité (maximale) du tri rapide

Un tableau de n-1 case et l'autre tout petit. Ca arrive pour des tableaux déjà triés. La complexité est alors de :

$$C(n) = \mathcal{O}(n) + C(n-1)$$

Donc $C(n) = \mathcal{O}(n) + \dots + \mathcal{O}(n)$ où l'on additionne $n$ fois $\mathcal{O}(n)$ : la complexité est de $C(n) = \mathcal{O}(n^2)$.

**Attention** : on additionne $n$ fois $\mathcal{O}(n)$. Comme $n$ n'est pas une constante, il **FAUT** le rentrer dans le $\mathcal{O}$.

#### complexité en moyenne du tri rapide

On coupe toujours le tableau en 2 parties égales. Si les nombres sont répartiés aléatoirement, il n'y a en effet aucune raison que notre pivot sot le plus petit ou le plus grand. Intuitivement, la plus grande probabilité est qu'il soit environ plus grand que la moitié des valeurs restantes et plus petit que l'autre moitié.

Si l'on coupe toujours au milieu on a alors : 

$$C(n) = \mathcal{O}(n) + 2 * C(\frac{n}{2})$$

Ce qui donne :

$$C(n) = \mathcal{O}(n) + 2 * (\mathcal{O}(\frac{n}{2}) + 2 * C(\frac{n}{4})) = 2 * \mathcal{O}(n) + 4 * C(\frac{n}{4})$$

>**Attention** : Comme on est entrain de tout calculer, il ne faut pas simplifier les $2 * \mathcal{O}(n)$. Si vous avez du mal, remplacez tous les $\mathcal{O}(n)$ par une constante $K$ et poursuivez le calcul jusqu'au baut, c'est à dire jusqu'à éliminer les $C(n)$.

Une rapide récurrence nous donne alors : 

$$C(n) = i * \mathcal{O}(n) + 2^{i} * C(\frac{n}{2^{i}})$$

Au maximum $i = \ln_2(n)$ (après, $\frac{n}{2^{i}} < 1$) et dans ce cas là :

$$C(n) = \ln_2(n) * \mathcal{O}(n) + 2^{\ln_2(n)} * C(\frac{n}{2^{\ln_2(n)}})$$

$$C(n) = \ln_2(n) * \mathcal{O}(n) + n * C(1)$$

On en conclut que la complexité vaut : $$C(n) = \mathcal{O}(\ln_2(n) * n)$$

#### complexité minimale du tri rapide

Si l'on découpe notre tableau de façon  non équilibrée, une branche de la récursion va faire plus d'opérations que $C(n/2)$. La complexité minimale est ainsi atteinte lorsque l'on coupe notre tableau exactement en 2.

#### conclusion

Le tri rapide est donc rigolo :

* il a une complexité moyenne qui vaut sa complexité minimale et qui est $\mathcal{O}(n * \ln(n))$, donc la meilleur possible
* il est très rapide pour les tableaux en désordre et très lent pour les tableaux déjà triés.

En pratique, on commence donc par mélanger le tableau pour le trier ensuite, c'est plus rapide que le trier tout court.
