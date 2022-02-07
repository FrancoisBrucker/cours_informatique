---
layout: page
title:  "étude / mélanger un tableau"
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [algorithmie]({% link cours/theorie-pratiques-algorithmique/algorithmie/index.md %}) / [étude : mélanger un tableau]({% link cours/theorie-pratiques-algorithmique/algorithmie/etude-melange.md %})
>
> prérequis :
>
> * [étude : l'exponentiation]({% link cours/theorie-pratiques-algorithmique/algorithmie/etude-exponentiation.md %})
>
{: .chemin}

Avant toute chose :

> Creéz un projet vscode pour implémenter, tester et utiliser les différents algorithmes.
{: .a-faire}

Nous allons étudier ici deux algorithmes permettant de mélanger un tableau. Commençons par identifier le problème. Nous allons utiliser le problème suivant, qui consiste à rendre une permutation des $n$ premiers entiers :

* **nom** : permutation
* **entrée** : un tableau d'entiers
* **sortie** : une permutation aléatoire du tableau en entrée

> une permutation d'un tableau $T$ de taille $n$ est un tableau $T'$ de taille $n$ où $T'[i] = T[\sigma(i)]$ avec $\sigma$ une bijection de $[0 .. n-1]$.

L'algorithme que nous allons montrer ici nécessite que l'on puisse obtenir un entier aléatoire plus petit qu'un nombre donné $n$. On va donc considérer que l'on a une fonction `randint` de complexité $\mathcal{O}(1)$ qui résout le problème "randint" suivant :

* **nom** : randint
* **entrées** : deux entiers $a$ et $b$
* **sortie** : un entier aléatoire $c$ tel que $a \leq c \leq b$.

On ne va pas définir plus que ça la notion d'aléatoire en informatique. On va ici prendre la définition mathématique : rend un nombre entre $a$ et $b$ de façon équiprobable, et considérer que c'est ok.

> Il n'existe pas d'aléatoire au sens mathématique en informatique. On ne peut atteindre que des nombre [pseudo-aléatoires](https://fr.wikipedia.org/wiki/Pseudo-al%C3%A9atoire), mais c'est une autre histoire.

## remarques préliminaires

> Lalgorithme suivant ne résout pas le problème "permutation". Pourquoi ?
{: .a-faire}

```text
soit T un tableau à n cases
de i = 0 à n-1:
    T[i] = T[randint(0, n-1)]
rendre T
```

{% details solution %}

Il peut y avoir des répétitions.

{% enddetails %}

> Codez cette méthode (en utilisant la fonction [randint](https://docs.python.org/fr/3/library/random.html#random.randint) du module [random](https://docs.python.org/fr/3/library/random.html)) pour vous rendre compte par vous-même qu'elle ne résout pas le problème.
{: .a-faire}

## borne min du problème

> Donnez la borne min du problème "permuation", même si on se sait pas si un tel algorithme
{: .a-faire}
{% details solution %}
Comme il faut rendre un tableau de longueur $n$, une borne minimum du problème "permutation" est de $\mathcal{O}(n)$. Mais rien ne dit qu'un tel algorithme existe.

{% enddetails %}

## existence d'un algorithme

Avant de chercher plus loin commençons par montrer qu'il existe un algorithme pour résoudre le problème. Si l'on possède une liste de toutes les permutations possible, l'algorithme suivant fonctionne :

```text
soit P un tableau contenant une fois chaque permutation de T
i = randint(0, n! - 1)
rendre P[i]
```

Il nous reste à créer toutes les permutations possibles d'un tableau. C'est ce que fait l'algorithme suivant, récursif et en python qui implémente la récurence de [la partie étude des tris]({% link cours/theorie-pratiques-algorithmique/algorithmie/etude-tris.md %}#borne-max).

## toutes les permutations {#algo-toutes-permutations}

Une permutation de $T$ peut être vu comme la [concaténation](https://fr.wikipedia.org/wiki/Concat%C3%A9nation#Programmation) de la liste à un élément $[T[i]]$ ($0 \leq i < n$)  et d'une permutation de $T'$ qui contient tous les éléments de $T$ sauf $T[i]$.

La remarque précédente nous donne la forme générale d'un algorithme récursif permettant de résoudre le problème. Le pseudo-code ci-après décrit une fonction `permutations` rend une liste contenant toutes les permutations de $T$ (chaque élément de `L` est un tableau) :

<style>
    table, td, tr, th, pre {
        padding:0;
        margin:0;
        border:none
    }
</style>
{% highlight text linenos %}
permutations(T):
    si T est vide:
        rendre [T] # la liste contenant toutes les permutation de de T, c'est à dire T
    L = []  # va contenir les permutations de T
    pour chaque i allant de 0 à len(T) - 1:
        soit a = T[i]
        soit T' la liste contenant tous les él&ments de T sauf T[i]
        soit L' = permutations(T')
        pour chaque P' de L':
            P = concaténation de [a] et de P'
            ajoute P à la fin de L
    rendre L
{% endhighlight %}

> Codez cet algorithme et mettez en places des tests pour vérifier qu'il fonctionne.
{: .a-faire}
{% details aide à la programmation %}

Vous pourrez utiliser le fait que :

* en python, la concaténation de deux tableaux `T1` et `T2` s'écrit `T1 + T2` (sa complexité est la somme de la taille des 2 tableaux puisqu'il faut créer un nouveau tableau)
* le [slycing de listes](https://zestedesavoir.com/tutoriels/582/les-slices-en-python/) en python est très puissant. Par exemple :
  * `T[:i]` contient les `i`prémiers éléments de la liste (de 0 à `i-1` inclut. Elle **ne continet donc pas** `T[i]`)
  * `T[i:]` contient la fin de la liste à partir de l'élément `i`.
  * `T[:i] + T[:i+1]` contient donc toute la liste sauf l'élément `T[i]`

{% enddetails %}

Pour placer dans la liste de listes `P` toutes les permutations de `[0, 1, 2, 3, 4, 5]`, on lance l'algorithme comme ça : `P = permutations([0, 1, 2, 3, 4, 5])`.

Analysons cet algorithme pour vérifier qu'il fait bien ce qu'on pense qu'il fait (bien).

### finitude {#finitude-permutations}

A chaque récursion, le tableau `T` est strictement plus petit. En effet le tableau `T'` sur lequel porte la récursion est la restriction du tableau `T` en supprimant l'élément d'indice `i`.

Il arrivera donc une récursion où `T` sera vide : le test de la ligne 2 stoppera la récursion.

### preuve {#preuve-permutations}

on prouve par récurrence sur la taille du tableau `T` que `permutations(T)` donne un tableau contenant toutes les permutations de `T`.

   1. pour `len(T) == 0` c'est clair.
   2. on suppose la propriété vrai pour `len(T) == p`. Pour `len(T) == p + 1`, par hypothèse de récurrence, le retour de la récursion `permutations(T')` sera l'ensemble des permutations `T'`. Pour un `i`  donné on obtient alors toutes les permutations de `T` ayant `T[i]` en première position (on ajoute `T[i]` à toutes les permutations de `T'`). Comme `i` prend tous les indice de `T`, on obtient au final toutes les permutations du tableau `T`.

### complexité {#complexite-permutations}

La complexité de l'algorithme va dépendre de la taille $n$ du tableau `T` : on note sa complexité $C(n)$. Comme il est récursif, on va chercher une équation de récurrence que satisfait $C(n)$ à résoudre.

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

En simplifiant les $\mathcal{O}(1)$, on obtient l'équation de récurrence suivante :

$$
\begin{array}{lcl}
C(n) & = & \mathcal{O}(1) + n \cdot (\mathcal{O}(n) + C(n-1) + (n-1)! \cdot (\mathcal{O}(n)))\\
     & = & \mathcal{O}(1) + \mathcal{O}(n^2) + n \cdot C(n-1) + n! \cdot \mathcal{O}(n)\\
     & = & \mathcal{O}(n^2) + n \cdot C(n-1) + \mathcal{O}(n\cdot n!)\\
     & = & n \cdot C(n-1) + \mathcal{O}(n\cdot n!)\\
\end{array}
$$

On peut maintenant étendre la récurrence

$$
\begin{array}{lcl}
C(n) & = & n \cdot C(n-1) + \mathcal{O}(n\cdot n!)\\
     & = & n \cdot (n-1) \cdot C(n-2) + n \mathcal{O}(n-1)\cdot (n-1)!)) + \mathcal{O}(n\cdot n!)\\
     & = & n \cdot (n-1) \cdot C(n-2) + \mathcal{O}(n-1)\cdot (n)!)) + \mathcal{O}(n\cdot n!)\\
     & = & n \cdot (n-1) \cdot C(n-2) + \mathcal{O}((n + (n-1))n!)\\
     & = & ...\\
     & = & \Pi_{i=0}^p (n -i)\cdot C(n-i-1) + \mathcal{O}(\sum_{i=0}^p (n -i))n!)\\
     & = & n! \cdot C(0) + \mathcal{O}(\sum_{i=0}^{n-1} (n - i))n!)\\
\end{array}
$$

Comme $C(0) = \mathcal{O}(1)$ et que $\sum_{i=0}^{n-1}(n-i) = \mathcal{O}(n^2)$ On en déduit que :

$$C(n) = \mathcal{O}(n^2n!) = \mathcal{O}((n+2)!)$$

### utilisation

L'algorithme `permutations` rend un tableau contenant toutes les permutations du tableau passé en entrée. La taille de la sortie est donc très grande.

Par exemple pour `permutations([1, 2, 3, 4])` va rendre :

```text
[[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]
```

On remarque que :

* le premier élément du tableau de sortie est le tableau initial
* le dernier élément du tableau de sortie est l'inverse du tableau initial
* que sont placés en premier les permutations ne changeant pas le 1er élément, puis celle où le 2nd élément est le premier, et ainsi de suite jusqu'à placer toutes les permutations où le dernier élément est le premier.

## un algorithme inefficace

Un algorithme de mélange utilisant `permutations` est alors de choisir 1 permutation parmi toutes les permutations d'un tableau en entrée.

> Codez un algorithme `melange(T)` qui commence par utiliser `permutations(T)` pour créer toutes les permutations possible, puis en choisi un au hasard (en utilisant la fonction [randint](https://docs.python.org/fr/3/library/random.html#random.randint) du module [random](https://docs.python.org/fr/3/library/random.html)) pour la rendre.
{: .a-faire}

```python
from random import randint

def melange(elements):
    P = permutations(elements)
    i = randint(0, len(P) - 1)
    return P[i]

```

Tester un algorithme avec du hasard est une technique avancée. Nous ne la traiterons pas ici, en revanche, on peut vérifier expérimentalement que c'est cohérent.

> Obtient-on bien toutes les permutations du tableau `[1, 2, 3]` si on exécute `melange` un grand nombre de fois ?
> Toutes les permutaions apparaissent-elles *à peu prêt$ le même nombre de fois ?
>
> Vérifiez-le expérimentalement
{: .a-faire}

A priori, oui, tout doit bien se passer si la la fonction [randint](https://docs.python.org/fr/3/library/random.html#random.randint) de python rend un nombre aléatoire : `melange` doit bien rendre qcache permutation de façon équiprobable.

C'est bien une solution au problème, mais sa complexité est cependant prohibitive.

Comme on a considéré que la complexité de `randint` est de $\mathcal{O}(1)$, la complexité de `melange` est de l'ordre de la complexité de `permutations` donc : $\mathcal{O}((n+2)!)$ avec $n$ la taille du tableau `element`. L'algorithme `melange` n'est pas utilisable en pratique car [n! est trop gros]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-max-min.md %}#n_factoriel)

> L'intérêt de `mélange` est théorique. Il montre qu'il existe un algorithme pour résoudre le problème (et en donne par là également une borne max).
{: .note}

## algorithme de Fisher-Yates ou de Knuth {#algorithme-fisher-yates}

L'algorithme que l'on va montrer maintenant, dit de [fisher-yates ou encore de Knuth](https://fr.wikipedia.org/wiki/M%C3%A9lange_de_Fisher-Yates), va également résoudre le problème "permutation", mais de façon bien plus élégante.

> Comme Fisher et Yates étaient des mathématiciens et Knuth un (grand) informaticien, les informaticiens préfèrent appeler cet algorithme *algorithme de Knuth* plutôt qu'*algorithme de Fisher-Yates*. Cependant comme Knuth a créé de très nombreux algorithmes, googler "algorithme de fisher-yates" donne directement le résultat attendu alors que googler "algorithme de knuth" donne plein de résultats différents (mais tous sont de superbes algorithmes !).

<style>
    table, td, tr, th, pre {
        padding:0;
        margin:0;
        border:none
    }
</style>
{% highlight python linenos %}
from random import randint

def melange_knuth(elements):
    copie_elements = list(elements)
    for i in range(len(copie_elements) - 1, -1, -1):
        j = randint(0, i)
        copie_elements[i], copie_elements[j] = copie_elements[j], copie_elements[i]
    return copie_elements

{% endhighlight %}

> Testez cet algorithme pour voir s'il rend bien des permutations du tableau en entrée.
{: .a-faire}

> Notez que la boucle for pourrait aussi s'écrire `for i in range(len(copie_elements) - 1, 0, -1):` sans perte de généralité.

### finitude {#finitude-knuth}

Une unique boucle for sur la longueur du tableau : l'algorithme finit toujours.

### complexité {#complexité-knuth}

Comme `randint` est considérée en $\mathcal{O}(1)$, la complexité totale de l'algorithme est (ligne à ligne) :

4. $\mathcal{O}(n)$ puisque l'on copie un tableau
5. une boucle for de $\mathcal{O}(n)$ itérations
6. utilisation de `randint` en $\mathcal{O}(1)$
7. 2 affectations et 2 recherches dans un tableau : $\mathcal{O}(1)$
8. retour de fonction : $\mathcal{O}(1)$

Ce qui donne une complexité de :

$$
\begin{array}{lcl}
C(n) & = & \mathcal{O}(n) + \mathcal{O}(n) \cdot (\mathcal{O}(1) + \mathcal{O}(1)) + \mathcal{O}(1)\\
& = & \mathcal{O}(n) + \mathcal{O}(n) + \mathcal{O}(1)\\
& = & \mathcal{O}(n) \\
\end{array}
$$

### vérification expérimentale {#verif-expe}

Si, en exécutant l'algorithme on se rend bien compte qu'il *mélange* le tableau en entrée, ce n'est pas très clair à première vue que toutes les permutations sont équiprobables.

On va le vérifier expérimentalement en regardant les permutations du tableau `[1, 2, 3, 4, 5, 6]`. On va compter combien de fois apparait chaque permutation (il y en a $6! = 720$) pour un grand nombre de tirage. Pour cela :

1. on utilise l'algorithme `permutations` pour calculer toutes les permutations. On les stocke dans un tableau `PERMUTATIONS`. Elles sont rendues dans un tableau de longueur $6!$
2. on initialise un tableau de longueur $6!$, que l'on nomme `compte`, avec des 0.
3. on exécute un grand nombre de fois l'algorithme `melange_knuth` (100000 fois) et à chaque résultat on ajoute 1 à `compte[i]` où $i$ est l'indice de la permutation rendue par l'algorithme dans le tableau `PERMUTATIONS`.
4. on affiche le résultat en le comparant au résultat théorique (s'il y a équiprobabilité, on devrait retrouver $100000 / 720 \simeq 139$ fois chaque permutation)

> Codez cette expérience.
> Pour rendre le résultat graphiquem, vous pourrez représenter la courbe $(i, compte[i])$.
{: .a-faire}

Pour la partie graphique, il faut que [matplotlib](https://matplotlib.org/) soit installé pour que le code fonctionne.  On a utilisé quelques trucs de matplotlib pour que la figue soit jolie :

* [des legendes](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html), que l'on a placé en dehors de la figure
* [un axe horizontal](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axhline.html)

Eléments du code :

```python

NOMBRE_ITERATION = 100000
TABLEAU = [1, 2, 3, 4, 5, 6]
PERMUTATIONS = permutations(TABLEAU)

compte = [0] * len(PERMUTATIONS)

#  ICI : on remplit le talbeau compte.

fig, ax = plt.subplots(figsize=(20, 5))

ax.set_xlim(-1, len(PERMUTATIONS) - 1)

ax.plot(compte, label="knuth")
ax.axhline(y=NOMBRE_ITERATION / len(PERMUTATIONS), color="red", label="théorique")

ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
ax.set_title("nombre de permutations")

plt.show()
```

Vous devriez obtenir le résultat suivant :

![mélange de Knuth]({{ "/assets/cours/algorithmie/melange_knuth.png" | relative_url }}){:style="margin: auto;display: block"}

Le nombre de permutations trouvé oscille bien autour de la valeur théorique.

> Pour vérifier que notre résultat est bien conforme à un tirage aléatoire, on devrait [fair un test du chi2 d'indépendance](https://fr.wikipedia.org/wiki/Test_du_%CF%87%C2%B2#Test_du_%CF%872_d'ind%C3%A9pendance), mais cela nous éloignerait de trop d'un cours d'algorithmie.

### preuve de programme

On suppose que le tableau d'entrée possède $n$ éléments.

On va montrer que les probabilités de sortie de chaque permutation sont bien équiprobables de trois façons différentes. Toutes les démonstrations reposent sur le fait :

* qu'une fois un élément choisi, il n'est plus jamais déplacé
* tous les éléments seront choisis une fois dans l'algorithme (il y a $n$ itérations et on choisit un élément à chaque itération)

#### preuve par probabilités

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

#### preuve par dénombrement

A la $i$ème itération on choisit un élément parmi $n-i+1$, et comme $i$ croit de $1$ à $n-1$, on a $n!$ parcours différents de l'algorithme.

L'algorithme choisit donc bien 1 permutation parmi $n!$, toutes différentes : il y a bien équiprobabilité des choix.

#### preuve par récurrence

1. lors de la première itération, on choisit un entier $k$ entre $0$ et $n-1$ et on échange l'élément d'indice $k$ avec celui d'indice $n-1$. Cet élément ne sera **plus jamais changé** dans la suite de l'algorithme. On en conclut que chaque élément du tableau d'entrée à la même chance d'être en dernière place de la permutation de sortie.
2. une fois la première itération terminée, tout se passe comme si on exécutait l'algorithme avec un tableau de taille $n-1$ contenant tous les éléments du tableau de départ sauf celui placé lors de la 1ère itération.
3. donc si l'algorithme fonctionne pour des tableau de longueur $n-1$, il fonctionne aussi pour des tableau de longueur $n$.
4. on peut terminer la preuve en remarquant que si le tableau a une longueur de 1, on a bien en sortie l'unique permutation du tableau en entrée.

> Cette preuve permet aussi de montrer que l'algorithme ne peut pas boucler et retrouver deux fois la même permutation avec 2 exécutions différentes.

## méthodes de python

Python utilise la méthode [shuffle](https://docs.python.org/fr/3/library/random.html#random.shuffle) du module random pour mélanger une liste.

**Attention**, La méthode shuffle ne rend pas une nouvelle liste, elle mélange la liste en entrée. Si l'on veut créer une nouvelle liste il faut utiliser la méthode [sample](https://docs.python.org/fr/3/library/random.html#random.sample) avec les paramètres suivants : `sample(x, k=len(x))`

> La méthode utilisée par shuffle est l'algorithme de Knuth / Fisher-Yates.

> Regardez les 4 différentes méthodes pour mélanger en python de cet article : <https://www.geeksforgeeks.org/python-ways-to-shuffle-a-list/>. La 4ème méthode n'est pas optimale en complexité. Pourquoi ?
{: .a-faire}

{% details  solution %}

La ligne `element=arr.pop(j)` supprime l'élément $j$ de la liste `arr`. Sa complexité est $\mathcal{O}(n)$ avec $n$ la taille de la liste `arr` car ce n'est pas formément le dernier élément qui est supprimé. La complexité totale de leur mélangeage est alors $\mathcal{O}(n^2)$ et pas $\mathcal{O}(n)$.

{% enddetails %}

## attention

### à trop mélanger on ne mélange pas bien

Si vous implémentez un algorithme de mélange mais qu'il peut obtenir plusieurs fois la même permutation avec des opérations différentes, alors vous risquez fort de ne pas être équiprobable. Illustrons ceci par un exemple.

On sait que toute permutation d'un tableau peut être atteinte en échangeant itérativement une paire d'éléments (on appelle ça une [décomposition en produit de transpositions](https://fr.wikipedia.org/wiki/Permutation#D%C3%A9composition_en_produit_de_transpositions)). On peut même montrer qu'il suffit d'en faire au plus la taille du tableau moins 1.

On en déduit l'algorithme de mélange suivant :

1. soit $T$ un tableau à $n$ éléments
2. répétez $n-1$ fois
   1. soit i un nombre aléatoire entre 0 et $n-1$
   2. soit j un nombre aléatoire entre 0 et $n-1$
   3. échanger $T[i]$ et $T[j]$

> Codez cet algorithme et refaites l'expérience de la [vérification expérimentale](#verif-expe) pour cet algorithme.
{: .a-faire}

Vous devirez obtenir quelque chose du type :

![mélange de transpositions]({{ "/assets/cours/algorithmie/melange_transposition.png" | relative_url }}){:style="margin: auto;display: block"}

On remarque que les premières permutations sont surreprésentées par rapport à ce qu'on devrait avoir. On remarque aussi qui'l y a des pics réguliers que l'on n'observe pas avec le mélange de Knuth. Ceci est du au fait que l'on peut produire une même permutation de plusieurs manière avec cet algorithme : on produit plus facilement certaines permutations que d'autres, ce qui rend l'algorithme non équiprobable.

> lisez et comprenez l'article : <https://datagenetics.com/blog/november42014/index.html>. Il explique pourquoi cette méthode n'est pas efficace.
{: .a-faire}

Nous allons ici juste montrer que les permutations en sorties ne sont pas équiprobables. La probabilité que l'élément d'indice $l$ ne soit jamais choisi pendant l'algorithme est :

$$P_n = (\frac{n-1}{n} \cdot \frac{n-1}{n})^n$$

Puisque l'algorithme a choisi pour chacune des $n$ étapes de la boucle for un élément différent de $l$ pour les lignes 4 et 5.

Or :

$$
P_n = ((1 - \frac{1}{n})^n)^2 \xrightarrow[n\to\infty]{} (\frac{1}{e})^2 > 0
$$

> $(1 - \frac{1}{n})^n = e^{n \ln (1-\frac{1}{n})} \sim e^{n \cdot (-\frac{1}{n})}$ lorsque $n$ tend vers l'infini puisque $\ln(1+u) \sim u$ lorsque $u$ tend vers $0$.

Ceci est incompatible avec l'équiprobabilité puisque :

* $P_n$ est plus petit que la probabilité que l'élément d'indice $l$ soit en position $l$ à la fin de l'algorithme (c'est même strictement plus petit puisqu'il peut n'avoir jamais bougé ou être revenu à sa place)
* s'il y a équiprobabilité, la probabilité que l'élément d'indice $l$ soit en position $l$ à la fin de l'algorithme doit être de $\frac{1}{n}$
* il existe $N_0$ tel que pour tout $n \geq N_0$, on a  $\frac{1}{n} < (\frac{1}{e})^2$

> Les remarques ci-dessus montrent que pour $n$ assez grand, la probabilité que l'élément $l$ soit en position $l$ à la fin de l'algorithme est strictement plus grande que l'équiprobabilité.
{: .note}

C'est bien ce qu'on remarque sur la figure avec la surreprésentation de la première permutation qui est la permutation où rien n'a bougé.

### randint doit être puissant

En informatique, il est impossible de tirer un nombre au hasard. On est obligé d'utiliser des suites périodiques qui se comportent comme des nombre aléatoires. On appelle ces suites [pseudo-aléatoires](https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9rateur_de_nombres_pseudo-al%C3%A9atoires).

La période de cette suite doit être très grande pour pouvoir générer toutes les permutations : la période doit être plus grande que $n!$. Sinon, certaines permutations seront sur-représentées.

Par exemple, pour pouvoir mélanger un paquet de 52 cartes de façon équiprobable en utilisant une suite pseudo-aléatoire, il faut que sa période soit plus que grande que $52! = 80658175170943878571660636856403766975289505440883277824000000000000 \sim 2^{226}$

> Une suite pseudo-aléatoire simple a souvent une période de $2^{64}$, ce qui n'est vraiment pas assez grand pour pouvoir mélanger équiprobablement un jeu de carte.

> Regardez la partie *A Shortage Of Random Numbers!* du lien suivant <https://www.i-programmer.info/programming/theory/2744-how-not-to-shuffle-the-kunth-fisher-yates-algorithm.html> qui explique celà.
{: .a-faire}

### attention aux humains

La perception de ce qu'est l'aléatoire n'est pas aisée. Lorsque l'on joue à un jeu de cartes par exemple, le [biais de confirmation](https://fr.wikipedia.org/wiki/Biais_de_confirmation) tend à se rappeler les évènement très défavorables au détriment de ceux juste *normaux*. De plus, lorsque l'on demande à des humains de tirer des nombres aléatoires, souvent ils ne le sont pas :

* Lorsque l'on demande à des humains de choisir un nombre aléatoirement entre 1 et 10, [ils répondent le plus souvent 7](https://www.reddit.com/r/dataisbeautiful/comments/acow6y/asking_over_8500_students_to_pick_a_random_number/).
* lorsque l'on demande à des humains d'écrire une suite aléatoire de 200 nombres valant 0 ou 1, il y aura une sous-représentation des longues séquences avec le même nombre : celà ne *fait pas aléatoire* d'avoir plein de fois le même nombre à la suite (alors que statistiquement, il faut bien que ces séquences existent).

> lisez l'article de <https://draftsim.com/mtg-arena-shuffler/> qui montre cela avec le mélangeur de [MTGA](https://magic.wizards.com/fr/mtgarena).
{: .a-faire}

## autres références

Quelques autres articles sur le sujet :

* <https://possiblywrong.wordpress.com/2014/12/01/card-shuffling-algorithms-good-and-bad/>
* <https://blog.codinghorror.com/the-danger-of-naivete/>
* <https://www.stashofcode.fr/tri-aleatoire-des-elements-dun-tableau/>
