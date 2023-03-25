---
layout: layout/post.njk 
title: "Etude : mélanger un tableau"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

prerequis:
    - "../../code/projet-exponentiation/"
    - "../../théorie/complexité-problème/"
---

<!-- début résumé -->

Nous allons étudier deux algorithmes permettant de mélanger un tableau.

<!-- end résumé -->

{% faire %}
Créez un projet vscode pour implémenter, tester et utiliser les différents algorithmes.
{% endfaire %}

Commençons par identifier le problème. Nous allons utiliser le problème suivant, qui consiste à rendre une permutation des $n$ premiers entiers :

{% note "**Problème** :" %}

* **nom** : permutation
* **entrée** : un tableau d'entiers
* **sortie** : une permutation aléatoire du tableau en entrée

{% endnote %}

{% info %}
Une permutation d'un tableau $T$ de taille $n$ est un tableau $T'$ de taille $n$ où $T'[i] = T[\sigma(i)]$ avec $\sigma$ une bijection de $[0 .. n-1]$.
{% endinfo %}

L'algorithme que nous allons montrer ici nécessite que l'on puisse obtenir un entier aléatoire plus petit qu'un nombre donné $n$. On va donc considérer que l'on a une fonction `randint`{.language-} de complexité $\mathcal{O}(1)$ qui résout le problème *"randint"* suivant :

{% note "**Problème** :" %}

* **nom** : randint
* **entrées** : deux entiers $a$ et $b$
* **sortie** : un entier aléatoire $c$ tel que $a \leq c \leq b$.

{% endnote %}

On ne va pas définir plus que ça la notion d'aléatoire en informatique. On va ici prendre la définition mathématique : *rend un nombre entre $a$ et $b$ de façon équiprobable*, et considérer que c'est ok.

{% info %}
Il n'existe pas d'aléatoire au sens mathématique en informatique. On ne peut atteindre que des nombre [pseudo-aléatoires](https://fr.wikipedia.org/wiki/Pseudo-al%C3%A9atoire), mais c'est une autre histoire.
{% endinfo %}

## Remarques préliminaires

{% exercice %}
L'algorithme suivant ne résout pas le problème "permutation". Pourquoi ?

```python

from random import randint

def aléatoire(T):
    T_prim = []
    for i in range(len(T)):
        T_prim.append(T[randint(0, len(T) - 1)])

    return T_prim
```

{% endexercice %}
{% details "solution" %}

Il peut y avoir des répétitions dans le choix des nombre aléatoire.

{% enddetails %}
{% faire %}
Codez cette méthode (on a utilisé la fonction [randint](https://docs.python.org/fr/3/library/random.html#random.randint) du module [random](https://docs.python.org/fr/3/library/random.html)) pour vous rendre compte par vous-même qu'elle ne résout pas le problème.
{% endfaire %}

## Borne min du problème

{% exercice %}
Donnez la borne min du problème *"permutation"*, même si on se sait pas si un tel algorithme existe.
{% endexercice %}
{% details "solution" %}
Comme il faut rendre un tableau de longueur $n$, une borne minimum du problème *"permutation"* est $\mathcal{O}(n)$. Mais rien ne dit qu'un tel algorithme existe.

{% enddetails %}

## Existence d'un algorithme

Avant de chercher plus loin commençons par montrer qu'il existe un algorithme pour résoudre le problème. Si l'on possède une liste de toutes les permutations possibles, l'algorithme suivant fonctionne :

```text
soit P un tableau contenant chaque permutation de T une fois

i = randint(0, n! - 1)
rendre P[i]
```

Il nous reste à créer toutes les permutations possibles d'un tableau. C'est ce que fait l'algorithme suivant.

## Toutes les permutations { #algo-toutes-permutations }

> TBD refaire avec next :
>
```python
def next(T):
    count = 0
    i = len(T) - 2
    while T[i] > T[i + 1]:
        i -= 1
        count += 1

    I = i

    i += 1
    j = len(T) - 1
    while i < j:
        count += 1
        T[i], T[j] = T[j], T[i]
        i += 1
        j -= 1

    for i in range(I + 1, len(T)):
        count += 1
        if T[i] > T[I]:
            T[i], T[I] = T[I], T[i]
            break

    return count

T = list(range(1, 8))

T_fin = list(T)
T_fin.reverse()

print(T)
tot = 0
nb = 1
while T != T_fin:
    nb += 1
    c = next(T)
    tot += c
    # print(T, c)

from math import factorial
print(tot, nb, tot / factorial(len(T)))
```

{% note "**Définition** :" %}
Si $L = [l_1, \dots, l_n]$ et $L'= [{l'}\_1, \dots, {l'}\_{n'}]$, alors la [***concaténation***](https://fr.wikipedia.org/wiki/Concat%C3%A9nation#Programmation) de $L$ et $L'$, notée $L + L'$ est égale à la liste :

$$
L + L' = [l\_1, \dots, l\_n, l'\_1, \dots, l'\_{n'}]
$$

{% endnote %}

Une permutation de $T$ peut être vu comme la [concaténation](https://fr.wikipedia.org/wiki/Concat%C3%A9nation#Programmation) de la liste à un élément $[T[i]]$ ($0 \leq i < n$)  et d'une permutation de $T'$ qui contient tous les éléments de $T$ sauf $T[i]$. Cette remarque nous donne une formule générale de l'ensemble $\mathcal{P}(T)$ des permutations de $T$ :

<div>
$$
\mathcal{P}(T) = \cup_{i=0}^{i=n-1} \{ [T[i]] + T' \mid T' \in \mathcal{P}(T[:i] + T[i+1:]) \}
$$
</div>

{% info %}
On a utilisé [les notations de python pour les sous-listes]({{ "/cours/coder-en-python/listes" | url}}#slice)
{% endinfo %}

Le pseudo-code ci-après est une transcription de la formule précédente. La fonction `permutations`{.language-} rend une liste contenant toutes les permutations d'une liste `T`{.language-} passée en paramètre (chaque élément de `P` est un tableau) :

```python#
def permutations(T):
    if len(T) == 0:
        return [T]  # la liste contenant toutes les permutation de de T, c'est à dire T

    P = []  # va contenir les permutations de T
    
    for i in range(len(T)):  
        I = [T[i]]
        Pi = permutations(T[:i] + T[i+1:])  # récursion
        for Ti in Pi:
            P.append(I + Ti)
    return P
```

{% faire %}
Codez cet algorithme et vérifier qu'il fonctionne.

Pour placer dans la liste de listes `P` toutes les permutations de `[1, 2, 3, 4]`{.language-}, on lance l'algorithme comme ça : `P = permutations([1, 2, 3, 4])`{.language-} .
{% endfaire %}

Analysons cet algorithme pour vérifier qu'il fait bien ce qu'on pense qu'il fait (bien).

### Finitude { #finitude-permutations }

A chaque récursion, le tableau `T`{.language-} a strictement moins d'éléments. Il arrivera donc une récursion où `T`{.language-} sera vide : le test de la ligne 2 stoppera la récursion.

### Preuve { #preuve-permutations }

on prouve par récurrence sur la taille du tableau `T`{.language-} que `permutations(T)`{.language-} donne un tableau contenant toutes les permutations de `T`{.language-}.

   1. pour `len(T) == 0`{.language-} c'est clair.
   2. on suppose la propriété vrai pour `len(T) == p`{.language-}. Pour `len(T) == p + 1`{.language-}, par hypothèse de récurrence, le retour de la récursion `permutations(T[:i] + T[i+1:])`{.language-} sera l'ensemble des permutations `T[:i] + T[i+1:]`. Pour un `i`{.language-}  donné on obtient alors toutes les permutations de `T` ayant `T[i]` en première position (on concatène `[T[i]]`{.language-} à toutes les permutations de `T[:i] + T[i+1:]`{.language-}). Comme `i`{.language-} prend tous les indice de `T`{.language-}, on obtient au final toutes les permutations du tableau `T`{.language-}.

### Complexité { #complexité-permutations }

La complexité de l'algorithme va dépendre de la taille $n$ du tableau `T`{.language-} : on note sa complexité $C(n)$. Comme il est récursif, on va chercher une équation de récurrence que satisfait $C(n)$ à résoudre.

Complexité de chaque ligne :

1. $\mathcal{O}(1)$ définition de la fonction
2. $\mathcal{O}(1)$ un test
3. $\mathcal{O}(1)$ retour d'une constante
4. $\mathcal{O}(1)$ affectation d'une constante
5. une boucle de $n$ itérations
6. $\mathcal{O}(1)$ une affectation d'un élément d'un tableau
7. $\mathcal{O}(n)$ car on crée un **nouveau** tableau de taille $n-1$
8. $C(n-1)$, c'est notre récursion.
9. une boucle de $\mathcal{O}((n-1)!)$ itérations (toutes les permutations d'un tableau à n-1 éléments)
10. $\mathcal{O}(n)$ car on crée un **nouveau** tableau de taille $n$
11. $\mathcal{O}(1)$, on ajoute un élément à la fin d'une liste (les tableau en python sont des listes, l'ajout d'un élément à la fin d'une liste est en temps constant)
12. $\mathcal{O}(1)$ retour d'une fonction

Ce qui donne :

<div>
$$
\begin{array}{lcl}
    C(n) = & & \mathcal{O}(1)\\
    & + & \mathcal{O}(1)\\
    & + & \mathcal{O}(1)\\
    & + & \mathcal{O}(1)\\
    & + & n \cdot (\\
    &  & \mathcal{O}(1)\\
    & + & \mathcal{O}(n)\\
    & + & C(n-1)\\
    & + & (n-1)! \cdot (\\
    & & \mathcal{O}(n)\\
    & + & \mathcal{O}(1)\\
    & & ))\\
    & + & \mathcal{O}(1)\\
\end{array}
$$
</div>

En simplifiant les $\mathcal{O}(1)$, on obtient l'équation de récurrence suivante :

<div>
$$
\begin{array}{lcl}
C(n) & = & \mathcal{O}(1) + n \cdot (\mathcal{O}(n) + C(n-1) + (n-1)! \cdot (\mathcal{O}(n)))\\
     & = & \mathcal{O}(1) + \mathcal{O}(n^2) + n \cdot C(n-1) + n! \cdot \mathcal{O}(n)\\
     & = & \mathcal{O}(n^2) + n \cdot C(n-1) + \mathcal{O}(n\cdot n!)\\
     & = & n \cdot C(n-1) + \mathcal{O}(n\cdot n!)\\
\end{array}
$$
</div>

On peut maintenant étendre la récurrence :

<div>
$$
\begin{array}{lcl}
C(n) & = & n \cdot C(n-1) + \mathcal{O}(n\cdot n!)\\
     & = & n \cdot ((n-1) \cdot C(n-2) + \mathcal{O}((n-1)\cdot (n-1)!)) + \mathcal{O}(n\cdot n!)\\
     & = & n \cdot (n-1) \cdot C(n-2) + n \cdot \mathcal{O}((n-1)\cdot (n-1)!) + \mathcal{O}(n\cdot n!)\\
     & = & n \cdot (n-1) \cdot C(n-2) + \mathcal{O}((n-1)\cdot (n)!) + \mathcal{O}(n\cdot n!)\\
     & = & n \cdot (n-1) \cdot C(n-2) + \mathcal{O}((n + (n-1))n!)\\
     & = & \dots\\
     & = & \Pi_{i=0}^p (n -i)\cdot C(n-i-1) + \mathcal{O}(n! \cdot \sum_{i=0}^p (n -i))\\
     & = & n! \cdot C(0) + \mathcal{O}(n! \cdot \sum_{i=0}^{n-1} (n - i))\\
\end{array}
$$
</div>

Comme $C(0) = \mathcal{O}(1)$ et que $\sum_{i=0}^{n-1}(n-i) = \mathcal{O}(n^2)$ On en déduit que :

$$C(n) = \mathcal{O}(n! \cdot n^2) = \mathcal{O}((n+2)!)$$

### Utilisation

L'algorithme `permutations`{.language-} rend un tableau contenant toutes les permutations du tableau passé en entrée. La taille de la sortie est donc très grande.

Par exemple pour `permutations([1, 2, 3, 4])`{.language-} va rendre :

```python
[[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]
```

On remarque que :

* le premier élément du tableau de sortie est le tableau initial
* le dernier élément du tableau de sortie est l'inverse du tableau initial
* que sont placés en premier les permutations ne changeant pas le 1er élément, puis celle où le 2nd élément est le premier, et ainsi de suite jusqu'à placer toutes les permutations où le dernier élément est le premier.

## Un premier algorithme

Un algorithme de mélange utilisant `permutations`{.language-} est alors de choisir 1 permutation parmi toutes les permutations d'un tableau en entrée :

```python
from random import randint

def mélange(T):
    P = permutations(T)
    i = randint(0, len(P) - 1)
    return P[i]

```

Si la la fonction [randint](https://docs.python.org/fr/3/library/random.html#random.randint) de python rend un nombre aléatoire équiprobable `mélange` doit bien rendre chaque permutation de façon équiprobable.

### Expérimentations

Vérifions expérimentalement que notre algorithme rend bien une permutation équiprobable.

On va compter le nombre de fois où chaque permutation apparaît :

```python
def compte_mélange(taille_liste, nombre_lancer):
    T = list(range(taille_liste))
    P = permutations()
    N = [0] * len(P)

    for i in range(nombre_lancer):
        T2 = mélange(T)
        N[P.index(T2)] += 1
    
    return N
```

{% exercice %}
Vérifiez expérimentalement que l'on obtient bien toutes les permutations d'un tableau à 5 éléments si on exécute `melange(5, 1000)`.

Pour une liste à 5 éléments, chaque liste devrait apparaître $\frac{1000}{5!} \simeq 8$ fois. Est-ce le cas ?

{% endexercice %}
{% details "solution" %}

```python

nombre = compte_mélange(5, 1000)
print(min(nombre), sum(nombre) / len(nombre), max(nombre))
```

{% enddetails %}

Représentons graphiquement les résultats !

On a mis en abscisse les différentes permutations et en ordonnée leur nombre

```python
import matplotlib.pyplot as plt

def graphique_mélange(taille_tableau, nombre_iteration):

    nombre = compte_mélange(taille_tableau, nombre_iteration)

    fig, ax = plt.subplots(figsize=(20, 5))

    ax.set_xlim(0, len(nombre) - 1)
    ax.set_ylim(0, max(nombre) + 1)

    ax.plot(nombre, label="nombre")
    ax.axhline(y=nombre_iteration / len(nombre), color="red", label="théorique")

    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    ax.set_title(str(nombre_iteration) + " permutations d'un tableau à " + str(taille_tableau)+ " éléments")

    plt.show()

graphique_mélange(6, 10000)
```

Pour une exécution de `graphique_mélange(6, 10000)`{.language-}, j'obtiens le résultat suivant :

![mélange](mélange_1.png)

Les permutations semblent bien équiprobables.

### Complexité

Notre algorithme est bien une solution au problème, mais sa complexité est cependant prohibitive.

Comme on a considéré que la complexité de `randint`{.language-} est de $\mathcal{O}(1)$, la complexité de `mélange`{.language-} est de l'ordre de la complexité de `permutations`{.language-} donc : $\mathcal{O}((n+2)!)$ avec $n$ la taille du tableau `T`. L'algorithme `mélange`{.language-} n'est pas utilisable en pratique car [n! est trop gros](../complexité-max-min#n_factoriel)

{% note %}
L'intérêt de `mélange`{.language-} est théorique. Il montre qu'il existe un algorithme pour résoudre le problème (et en donne par là également une borne max).
{% endnote %}

## Algorithme de Fisher-Yates ou de Knuth { #algorithme-fisher-yates }

L'algorithme que l'on va montrer maintenant, dit de [fisher-yates ou encore de Knuth](https://fr.wikipedia.org/wiki/M%C3%A9lange_de_Fisher-Yates), va également résoudre le problème "permutation", mais de façon bien plus élégante.

{% info %}
Comme Fisher et Yates étaient des mathématiciens et Knuth un (grand) informaticien, les informaticiens préfèrent appeler cet algorithme *algorithme de Knuth* plutôt qu'*algorithme de Fisher-Yates*. Cependant comme Knuth a créé de très nombreux algorithmes, googler "algorithme de fisher-yates" donne directement le résultat attendu alors que googler "algorithme de Knuth" donne plein de résultats différents (mais tous sont de superbes algorithmes !).
{% endinfo %}

```python#
from random import randint

def mélange_Knuth(T):
    T2 = list(T)
    for i in range(len(T2) - 1, -1, -1):
        j = randint(0, i)
        T2[i], T2[j] = T2[j], T2[i]
    return T2
```

{% faire %}
Testez cet algorithme pour voir s'il rend bien des permutations du tableau en entrée.
{% endfaire %}

{% info %}
Notez que la boucle for pourrait aussi s'écrire `for i in range(len(T2) - 1, -1, -1)`{.language-} sans perte de généralité.
{% endinfo %}

### Finitude { #finitude-Knuth }

Une unique boucle for sur la longueur du tableau : l'algorithme finit toujours.

### complexité { #complexité-Knuth }

Comme `randint`{.language-} est considérée en $\mathcal{O}(1)$, la complexité totale de l'algorithme est (ligne à ligne) :

1. —
2. —
3. —
4. $\mathcal{O}(n)$ puisque l'on copie un tableau
5. une boucle for de $\mathcal{O}(n)$ itérations
6. utilisation de `randint`{.langage-python} en $\mathcal{O}(1)$
7. 2 affectations et 2 recherches dans un tableau : $\mathcal{O}(1)$
8. retour de fonction : $\mathcal{O}(1)$

Ce qui donne une complexité de :

<div>
$$
\begin{array}{lcl}
C(n) & = & \mathcal{O}(n) + \mathcal{O}(n) \cdot (\mathcal{O}(1) + \mathcal{O}(1)) + \mathcal{O}(1)\\
& = & \mathcal{O}(n) + \mathcal{O}(n) + \mathcal{O}(1)\\
& = & \mathcal{O}(n) \\
\end{array}
$$
</div>

### Vérification expérimentale { #vérification-expérimentale }

Si, en exécutant l'algorithme on se rend bien compte qu'il *mélange* le tableau en entrée, ce n'est pas très clair à première vue que toutes les permutations sont équiprobables.

On va le vérifier expérimentalement en regardant les permutations du tableau `[1, 2, 3, 4, 5, 6]`. On va compter combien de fois apparaît chaque permutation (il y en a $6! = 720$) pour un grand nombre de tirage.

On pourrait reprendre le code précédent et l'adapter pour notre mélange, mais il y aurait beaucoup de duplication de code. En fait seule le nom de la permutation changerait.

On préfère donc faire directement des méthodes génériques, en passant la fonction à utiliser en paramètre

<span id="fonction-en-paramètre"></span>
{% info %}
En python, une fonction à tout à fait le droit d'être un paramètre, ce qui est vraiment chouette pour écrire du code générique.
{% endinfo %}

```python
def compte_mélange_générique(fonction_mélange, taille_liste, nombre_lancer):
    T = list(range(taille_liste))
    P = permutations(T)
    N = [0] * len(P)

    for i in range(nombre_lancer):
        T2 = fonction_mélange(T)
        N[P.index(T2)] += 1
    
    return N

def graphique_mélange_générique(fonction_mélange, taille_tableau, nombre_iteration):

    nombre = compte_mélange_générique(fonction_mélange, taille_tableau, nombre_iteration)

    fig, ax = plt.subplots(figsize=(20, 5))

    ax.set_xlim(0, len(nombre) - 1)
    ax.set_ylim(0, max(nombre) + 1)

    ax.plot(nombre, label="nombre")
    ax.axhline(y=nombre_iteration / len(nombre), color="red", label="théorique")

    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    ax.set_title(str(nombre_iteration) + " permutations d'un tableau à " + str(taille_tableau)+ " éléments")

    plt.show()

```

De là, pour utiliser la fonction `mélange`{.language-} :

```python
graphique_mélange_générique(mélange, taille_tableau, nombre_iteration)
```

et pour utiliser la fonction `mélange_Knuth`{.language-} :

```python
graphique_mélange_générique(mélange_Knuth, taille_tableau, nombre_iteration)
```

{% faire %}
Testez `graphique_mélange_générique(mélange_Knuth, 6, 10000)`{.language-} et comparez la vitesse d'exécution par rapport à `graphique_mélange_générique(mélange, 6, 10000)`{.language-}
{% endfaire %}

Vous devriez obtenir le résultat suivant :

![mélange de Knuth](mélange_Knuth.png)

Le nombre de permutations trouvé oscille bien autour de la valeur théorique.

{% info %}
Pour vérifier que notre résultat est bien conforme à un tirage aléatoire, on devrait [fair un test du chi2 d'indépendance](https://fr.wikipedia.org/wiki/Test_du_%CF%87%C2%B2#Test_du_%CF%872_d'ind%C3%A9pendance), mais cela nous éloignerait trop d'un cours d'algorithmie.
{% endinfo %}

### Preuve de programme

On suppose que le tableau d'entrée possède $n$ éléments.

On va montrer que les probabilités de sortie de chaque permutation sont bien équiprobables de trois façons différentes. Toutes les démonstrations reposent sur le fait :

* qu'une fois un élément choisi, il n'est plus jamais déplacé
* tous les éléments seront choisis une fois dans l'algorithme (il y a $n$ itérations et on choisit un élément à chaque itération)

#### Preuve par probabilités

On va calculer la probabilité que l'élément originellement en position $i$ se retrouve en position $n-j$ à la fin de l'algorithme. Si notre tirage est équiprobable, cette probabilité doit être égal à $\frac{1}{n}$ quelque soient $i$ et $j$.

Pour que cela arrive, il faut que :

* l'élément n'ait pas été pris pendant la première itération : il y a $\frac{n-1}{n}$ chances que ça arrive (on ne choisit pas notre élément parmi $n$ possibles : $1-\frac{1}{n} = \frac{n-1}{n}$)
* l'élément n'ait pas été pris pendant la deuxième itération : il y a $\frac{n-2}{n-1}$ chances que ça arrive (on ne choisit pas notre élément parmi $n - 1$ possibles : $1-\frac{1}{n-1} = \frac{n-2}{n-1}$)
* ...
* l'élément n'ait pas été pris pendant la $j-1$ ème itération : il y a $\frac{n-j+1}{n-j+2}$ chances que ça arrive (on ne choisit pas notre élément parmi $n-(j-1) +1$ possibles : $1-\frac{1}{n-j+2} = \frac{n-j+1}{n-j+2}$)
* l'élément ait été pris pendant la $j$ ème itération : il y a $\frac{1}{n-j+1}$ chances que ça arrive

De là, la probabilité que l'élément originellement en position $i$ se retrouve en position $n-j$ à la fin de l'algorithme est :

$$\frac{n-1}{n} \cdot \frac{n-2}{n-1} \cdot \ ...\  \cdot \frac{n-j+1}{n-j+2} \cdot \frac{1}{n-j+1} = \frac{1}{n}$$

C'est bien équiprobable !

#### Preuve par dénombrement

A la $i$ème itération on choisit un élément parmi $n-i+1$, et comme $i$ croit de $1$ à $n-1$, on a $n!$ parcours différents de l'algorithme.

L'algorithme choisit donc bien 1 permutation parmi $n!$, toutes différentes : il y a bien équiprobabilité des choix.

#### Preuve par récurrence

1. lors de la première itération, on choisit un entier $k$ entre $0$ et $n-1$ et on échange l'élément d'indice $k$ avec celui d'indice $n-1$. Cet élément ne sera **plus jamais changé** dans la suite de l'algorithme. On en conclut que chaque élément du tableau d'entrée à la même chance d'être en dernière place de la permutation de sortie.
2. une fois la première itération terminée, tout se passe comme si on exécutait l'algorithme avec un tableau de taille $n-1$ contenant tous les éléments du tableau de départ sauf celui placé lors de la 1ère itération.
3. donc si l'algorithme fonctionne pour des tableau de longueur $n-1$, il fonctionne aussi pour des tableau de longueur $n$.
4. on peut terminer la preuve en remarquant que si le tableau a une longueur de 1, on a bien en sortie l'unique permutation du tableau en entrée.

{% info %}
Cette preuve permet aussi de montrer que l'algorithme ne peut pas boucler et retrouver deux fois la même permutation avec 2 exécutions différentes.
{% endinfo %}

## Méthodes de python

Python utilise la méthode [shuffle](https://docs.python.org/fr/3/library/random.html#random.shuffle) du module random pour mélanger une liste.

{% attention %}
La méthode shuffle ne rend pas une nouvelle liste, elle mélange la liste en entrée. Si l'on veut créer une nouvelle liste il faut utiliser la méthode [sample](https://docs.python.org/fr/3/library/random.html#random.sample) avec les paramètres suivants : `sample(x, k=len(x))`
{% endattention %}

La méthode utilisée par shuffle est l'algorithme de Knuth / Fisher-Yates.

{% exercice %}
Regardez les 4 différentes méthodes pour mélanger en python de cet article : <https://www.geeksforgeeks.org/python-ways-to-shuffle-a-list/>. La 4ème méthode n'est pas optimale en complexité. Pourquoi ?
{% endexercice %}
{% details  "solution" %}

La ligne `element=arr.pop(j)`{.language-} supprime l'élément $j$ de la liste `arr`{.language-}. Sa complexité est $\mathcal{O}(n)$ avec $n$ la taille de la liste `arr`{.language-} car ce n'est pas forcément le dernier élément qui est supprimé. La complexité totale de leur mélangeage est alors $\mathcal{O}(n^2)$ et pas $\mathcal{O}(n)$.

{% enddetails %}

## Attention

On va montrer trois écueils du mélange :

* le premier lié à un mauvais choix d'algorithme (mais pas évident à voir) : atteindre toutes les permutations n'est pas une garanti d'équiprobabilité.
* le second montre que si votre algorithme dépend d'un autre, il faut aussi analyser ses performances.
* le troisième lié aux biais cognitifs humains qui ne voient pas l'aléatoire comme ce qu'il est réellement.

### A trop mélanger on ne mélange pas bien

Si vous implémentez un algorithme de mélange mais qu'il peut obtenir plusieurs fois la même permutation avec des opérations différentes, alors vous risquez fort de ne pas être équiprobable. Illustrons ceci par un exemple.

On sait que toute permutation d'un tableau peut être atteinte en échangeant itérativement une paire d'éléments (on appelle ça une [décomposition en produit de transpositions](https://fr.wikipedia.org/wiki/Permutation#D%C3%A9composition_en_produit_de_transpositions)). On peut même montrer qu'il suffit d'en faire au plus la taille du tableau moins 1.

On en déduit l'algorithme de mélange suivant :

1. soit $T$ un tableau à $n$ éléments
2. répétez $n-1$ fois
   1. soit i un nombre aléatoire entre 0 et $n-1$
   2. soit j un nombre aléatoire entre 0 et $n-1$
   3. échanger $T[i]$ et $T[j]$

```python
def mélange_transposition(T):
    T2 = list(T)
    for k in range(len(T2) - 1):
        i = randint(0, len(T2) - 1)
        j = randint(0, len(T2) - 1)

        T2[i], T2[j] = T2[j], T2[i]
    return T2
```

{% faire %}
Codez cet algorithme et exécutez : `graphique_mélange_générique(mélange_transposition, 6, 10000)`{.language-}.
{% endfaire %}

Vous devriez obtenir quelque chose du type :

![mélange de transpositions](mélange_transposition.png)

On remarque que les premières permutations sont surreprésentées par rapport à ce qu'on devrait avoir. On remarque aussi qui'l y a des pics réguliers que l'on n'observe pas avec le mélange de Knuth. Ceci est du au fait que l'on peut produire une même permutation de plusieurs manière avec cet algorithme : on produit plus facilement certaines permutations que d'autres, ce qui rend l'algorithme non équiprobable.

{% info %}
Lisez et comprenez l'article : <https://datagenetics.com/blog/november42014/index.html>. Il explique pourquoi cette méthode n'est pas efficace.
{% endinfo %}

Nous allons ici juste montrer que les permutations en sorties ne sont pas équiprobables. La probabilité que l'élément d'indice $l$ ne soit jamais choisi pendant l'algorithme est :

$$P_n = (\frac{n-1}{n} \cdot \frac{n-1}{n})^n$$

Puisque l'algorithme a choisi pour chacune des $n$ étapes de la boucle for un élément différent de $l$ pour les lignes 4 et 5.

Or :

$$
P_n = ((1 - \frac{1}{n})^n)^2 \xrightarrow[n\to\infty]{} (\frac{1}{e})^2 > 0
$$

{% details "parce que" %}
La fonction $(1 - \frac{1}{n})^n = e^{n \ln (1-\frac{1}{n})}$ est équivalente à la fonction $e^{n \cdot (-\frac{1}{n})}$ lorsque $n$ tend vers l'infini puisque $\ln(1+u) \sim u$ lorsque $u$ tend vers $0$.
{% enddetails %}

Ceci est incompatible avec l'équiprobabilité puisque :

* $P_n$ est plus petit que la probabilité que l'élément d'indice $l$ soit en position $l$ à la fin de l'algorithme (c'est même strictement plus petit puisqu'il peut n'avoir jamais bougé ou être revenu à sa place)
* s'il y a équiprobabilité, la probabilité que l'élément d'indice $l$ soit en position $l$ à la fin de l'algorithme doit être de $\frac{1}{n}$
* il existe $N_0$ tel que pour tout $n \geq N_0$, on a  $\frac{1}{n} < (\frac{1}{e})^2$

{% note %}
Les remarques ci-dessus montrent que pour $n$ assez grand, la probabilité que l'élément $l$ soit en position $l$ à la fin de l'algorithme est strictement plus grande que l'équiprobabilité.
{% endnote %}

C'est bien ce qu'on remarque sur la figure avec la surreprésentation de la première permutation qui est la permutation où rien n'a bougé.

> TBD : dire que c'est parce que je fais exactement $\mathcal{O}(n)$ tirages. Si le nombre de tirages n'est pas borné, c'est bien équiprobable (marche aléatoire etc.)

### Randint doit être puissant

En informatique, il est impossible de tirer un nombre au hasard. On est obligé d'utiliser des suites périodiques qui se comportent comme des nombre aléatoires. On appelle ces suites [pseudo-aléatoires](https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9rateur_de_nombres_pseudo-al%C3%A9atoires).

La période de cette suite doit être très grande pour pouvoir générer toutes les permutations : la période doit être plus grande que $n!$. Sinon, certaines permutations seront sur-représentées.

Par exemple, pour pouvoir mélanger un paquet de 52 cartes de façon équiprobable en utilisant une suite pseudo-aléatoire, il faut que sa période soit plus que grande que $52! = 80658175170943878571660636856403766975289505440883277824000000000000 \sim 2^{226}$

{% info %}
Une suite pseudo-aléatoire simple a souvent une période de $2^{64}$, ce qui n'est vraiment pas assez grand pour pouvoir mélanger de façon équiprobable un jeu de carte.
{% endinfo %}

{% info %}
La partie *A Shortage Of Random Numbers!* du lien suivant <https://www.i-programmer.info/programming/theory/2744-how-not-to-shuffle-the-kunth-fisher-yates-algorithm.html> qui explique cela.
{% endinfo %}

### Attention aux humains

La perception de ce qu'est l'aléatoire n'est pas aisée. Lorsque l'on joue à un jeu de cartes par exemple, le [biais de confirmation](https://fr.wikipedia.org/wiki/Biais_de_confirmation) tend à se rappeler les évènement très défavorables au détriment de ceux juste *normaux*. De plus, lorsque l'on demande à des humains de tirer des nombres aléatoires, souvent ils ne le sont pas :

* Lorsque l'on demande à des humains de choisir un nombre aléatoirement entre 1 et 10, [ils répondent le plus souvent 7](https://www.reddit.com/r/dataisbeautiful/comments/acow6y/asking_over_8500_students_to_pick_a_random_number/).
* lorsque l'on demande à des humains d'écrire une suite aléatoire de 200 nombres valant 0 ou 1, il y aura une sous-représentation des longues séquences avec le même nombre : cela ne *fait pas aléatoire* d'avoir plein de fois le même nombre à la suite (alors que statistiquement, il faut bien que ces séquences existent).

{% info %}
Lisez l'article de <https://draftsim.com/mtg-arena-shuffler/> qui montre cela avec le mélangeur de [MTGA](https://magic.wizards.com/fr/mtgarena).
{% endinfo %}

## Autres références

Quelques autres articles sur le sujet :

* <https://possiblywrong.wordpress.com/2014/12/01/card-shuffling-algorithms-good-and-bad/>
* <https://blog.codinghorror.com/the-danger-of-naivete/>
* <https://www.stashofcode.fr/tri-aleatoire-des-elements-dun-tableau/>
