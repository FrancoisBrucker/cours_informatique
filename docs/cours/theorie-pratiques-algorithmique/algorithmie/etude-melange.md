---
layout: page
title:  "étude / mélanger un tableau"
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [algorithmie]({% link cours/theorie-pratiques-algorithmique/algorithmie/index.md %}) / [étude :  mélanger un tableau]({% link cours/theorie-pratiques-algorithmique/algorithmie/etude-melange.md %})
>
> prérequis :
>
>* [étude : l'exponentiation]({% link cours/theorie-pratiques-algorithmique/algorithmie/etude-exponentiation.md %})
>
{: .chemin}

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

Attention, l'algorithme suivant :

```text
soit T un tableau à n cases
de i = 0 à n-1:
    T[i] = randint(0, n-1)
rendre T
```

Ne résout pas le problème "permutation" puisqu'il peut y avoir des répétitions.

## borne min du problème

Comme il faut rendre un tableau de longueur $n$, une borne minimum du problème "permutation" est de $\mathcal{O}(n)$. Mais rien ne dit qu'un tel algorithme existe.

## existence d'un algorithme

Avant de chercher plus loin commençons par montrer qu'il existe un algorithme pour résoudre le problème. Si l'on possède une liste de toutes les permutations possible, l'algorithme suivant fonctionne :

```text
soit P un tableau contenant une fois chaque permutation de T
i = randint(0, n! - 1)
rendre P[i]
```

Il nous reste à créer toutes les permutations possibles d'un tableau. C'est ce que fait l'algorithme suivant, récursif et en python.

## toutes les permutations

<style>
    table, td, tr, th, pre {
        padding:0;
        margin:0;
        border:none
    }
</style>
{% highlight python linenos %}

def permutations(elements):
    if len(elements) == 0:
        return [[]]

    les_permutations = []
    for i in range(len(elements)):
        premier = elements[i]
        elements_sans_premier = elements[:i] + elements[i+1:]
        permutations_sans_premier = permutations(elements_sans_premier)
        for une_fin_de_permutation in permutations_sans_premier:
            permutation = [premier] + une_fin_de_permutation
            les_permutations.append(permutation)
    return les_permutations

{% endhighlight %}

Pour placer dans la liste de listes `P` toutes les permutations de `[0, 1, 2, 3, 4, 5]`, on lance l'algorithme comme ça : `P = permutations([0, 1, 2, 3, 4, 5])`.

> Testez cet algorithme.
{: .a-faire}

Analysons cet algorithme pour vérifier qu'il fait bien ce qu'on pense qu'il fait (bien).

### finitude {#finitude-permutations}

A chaque récursion, le tableau `elements` est strictement plus petit. En effet le tableau `elements_sans_premier` sur lequel porte la récursion est la restriction du tableau `elements` en supprimant l'élément d'indice `i` (`elements_sans_premier = elements[:i] + elements[i+1:]`).

Il arrivera donc une récursion où `elements` sera vide : le test de la ligne 2 stoppera la récursion.

### preuve {#preuve-permutations}

on prouve par récurrence sur la taille du tableau `elements` que `permutations_rec(elements)` donne un tableau contenant toutes les permutations de `elements`.

   1. pour `len(elements) == 0` c'est clair.
   2. on suppose la propriété vrai pour `len(elements) == p`. Pour `len(elements) == p + 1`, par hypothèse de récurrence, le retour de la récursion `permutations_rec(elements_sans_premier)` sera l'ensemble des permutations de `elements[:i] + elements[i+1:]` pour une position `i` de `elements`. Pour un `i`  donné on obtient alors  toutes les permutations de `elements` ayant `elements[i]` en première position (on ajoute `elements[i]` à toutes les permutations de `elements[:i] + elements[i+1:]`). Comme `i` prend tous les indice de `elements`, on on obtient aufinal toutes les permutations du tableau `elements`.

### complexité {#complexite-permutations}

La complexité de l'algorithme va dépendre de la taille $n$ du tableau `elements`. : on note sa complexité $C(n)$. Comme il est récursif, on va chercher une équation de récurrence que satisfait $C(n)$ à résoudre.

Complexité de chaque ligne :

1. $\mathcal{O}(1)$ définition de la fonction
2. $\mathcal{O}(1)$ un test
3. $\mathcal{O}(1)$ retour d'une constante
4.
5. $\mathcal{O}(1)$ affectation d'une constante
6. une boucle de $n$ itérations
7. $\mathcal{O}(1)$ une affectation d'un élément d'un tableau
8. $\mathcal{O}(n)$ car on crée un **nouveau** tableau de taille $n-1$
9. $C(n-1)$, c'est notre récursion.
10. une boucle de $\mathcal{O}((n-1)!)$ itérations (toutes les permutations d'un tableau à n-1 éléments)
11. $\mathcal{O}(n)$ car on crée un **nouveau** tableau de taille $n$
12. $\mathcal{O}(1)$, on ajoute un élément à la fin d'une liste (les tableau en pthon sont des listes, l'ajout d'un élément à la fin d'une liste est en temps constant)
13. $\mathcal{O}(1)$ retour d'une fonction

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

```python
from random import randint

def melange(elements):
    P = permutations(elements)
    i = randint(0, len(P) - 1)
    return P[i]

```

Comme la fonction [randint](https://docs.python.org/fr/3/library/random.html#random.randint) du module [random](https://docs.python.org/fr/3/library/random.html) de python rend un nombre aléatoire, `melange` est bien une solution au problème puisque chaque permutation sera équiprobable.

Sa complexité est cependant prohibitive. Comme on a considéré que la complexité de `randint` est de $\mathcal{O}(1)$, la complexité de `melange` est de l'ordre de la complexité de `permutations` donc : $\mathcal{O}((n+2)!)$ avec $n$ la taille du tableau `element`. L'algorithme `melange` n'est pas utilisable en pratique car [n! est trop gros]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-max-min.md %}#n_factoriel)

> L'intérêt de `mélange` est théorique. Il montre qu'il existe un algorithme pour résoudre le problème (et en donne par là également une borne max).
{: .note}

## algorithme de fisher-yates ou de Knuth

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

> Testez cet algorithme pour voir s'il rend bien des permutation du tableau en entrée.
{: .a-faire}

> Notez que la boucle for pourrait aussi s'écrire `for i in range(len(copie_elements) - 1, 0, -1):` sans perte de généralité.

### finitude {#finitude-knuth}

Une unique boucle for sur la longueur du tableau : l'algorithme fini toujours.

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
{: .a-faire}

{% details  une solution possible %}

Il faut que [matplotlib](https://matplotlib.org/) soit installé pour que le code fonctionne.

* On a utilisé quelques trucs de matplotlib pour que la figue soit jolie :
  * [des legendes](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html), que l'on a placé en dehors de la figure
  * [un axe horizontal](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axhline.html)
* on a mis un [break](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops) dans la recherche de la permutation, pour éviter de faire des recherches inutiles.

On a également a mis les constantes en majuscule, [conformément au style](https://www.python.org/dev/peps/pep-0008/#constants)

```python
from random import randint
import matplotlib.pyplot as plt

def permutations(elements):
    if len(elements) == 0:
        return [[]]
    
    les_permutations = []
    for i in range(len(elements)):
        premier = elements[i]
        elements_sans_premier = elements[:i] + elements[i+1:]
        permutations_sans_premier = permutations(elements_sans_premier)
        for une_fin_de_permutation in permutations_sans_premier:
            permutation = [premier] + une_fin_de_permutation
            les_permutations.append(permutation)
    return les_permutations
    

def melange_knuth(elements):
    copie_elements = list(elements)
    for i in range(len(copie_elements) - 1, -1, -1):
        j = randint(0, i)
        copie_elements[i], copie_elements[j] = copie_elements[j], copie_elements[i]
    return copie_elements


NOMBRE_ITERATION = 100000
TABLEAU = [1, 2, 3, 4, 5, 6]
PERMUTATIONS = [x for x in permutations(TABLEAU)]

compte = [0] * len(PERMUTATIONS)

for k in range(NOMBRE_ITERATION):
    res = melange_knuth(TABLEAU)
    
    for i in range(len(PERMUTATIONS)):
        if  PERMUTATIONS[i] == res:
            compte[i] += 1
            break

fig, ax = plt.subplots(figsize=(20, 5))

ax.set_xlim(-1, len(PERMUTATIONS) - 1)

ax.plot(compte, label="knuth")
ax.axhline(y=NOMBRE_ITERATION / len(PERMUTATIONS), color="red", label="théorique")

ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
ax.set_title("nombre de permutations")

plt.show()

```

> Une version avancée du code précédent aurait utilisé un [compteur](https://docs.python.org/fr/3/library/collections.html#counter-objects) du module [collections](https://docs.python.org/fr/3/library/collections.html) pour accélérer le comptage, mais cela aurait nécessiter de changer nos listes en tuples.

{% enddetails %}

J'obtiens le résultat suivant :

![mélange de Knuth]({{ "/assets/cours/algorithmie/melange_knuth.png" | relative_url }}){:style="margin: auto;display: block"}

Le nombre de permutations trouvé oscille bien autour de la valeur théorique.

> Pour vérifier que notre résultat est bien conforme à un tirage aléatoire, on devrait [fair un test du chi2 d'indépendance](https://fr.wikipedia.org/wiki/Test_du_%CF%87%C2%B2#Test_du_%CF%872_d'ind%C3%A9pendance), mais cela nous éloignerait de trop d'un cours d'algorithmie.

### preuve de programme

On suppose que le tableau d'entrée possède $n$ éléments.

On va montrer que les probabilités de sortie de chaque permutation sont bien équiprobables de trois façons différentes. Toutes les démonstrations reposent sur le fait :

* qu'une fois un élément choisi, il n'est plus jamais déplacé
* tous les éléments seront choisis une fois dans l'algorithme (il y a $n$ itérations et on choisi un élément à chaque itération)

#### preuve par probabilités

On va calculer la probabilité que l'élément originellement en position $i$ se retrouve en position $n-j$ à la fin de l'algorithme. Si notre tirage est équiprobable, cette probabilité doit être égal à $\frac{1}{n}$ quelquesoient $i$ et $j$.

Pour que cela arrive, il faut que :

* l'élément n'ait pas été pris pendants la première itération : il y a $\frac{n-1}{n}$ chances que ça arrive (on ne choisit pas notre élément parmi $n$ possibles : $1-\frac{1}{n} = \frac{n-1}{n}$)
* l'élément n'ait pas été pris pendants la deuxième itération : il y a $\frac{n-2}{n-1}$ chances que ça arrive (on ne choisit pas notre élément parmi $n - 1$ possibles : $1-\frac{1}{n-1} = \frac{n-2}{n-1}$)
* ...
* l'élément n'ait pas été pris pendants la $j-1$ ème itération : il y a $\frac{n-j+1}{n-j+2}$ chances que ça arrive (on ne choisit pas notre élément parmi $n-(j-1) +1$ possibles : $1-\frac{1}{n-j+2} = \frac{n-j+1}{n-j+2}$)
* l'élément ait été pris pendants la $j$ ème itération : il y a $\frac{1}{n-j+1}$ chances que ça arrive

De là, la probabilité que l'élément originellement en position $i$ se retrouve en position $n-j$ à la fin de l'algorithme est :

$$\frac{n-1}{n} \cdot \frac{n-2}{n-1} \cdot ... \cdot \frac{n-j+1}{n-j+2} \cdot \frac{1}{n-j+1} == \frac{1}{n}$$

C'est bien équiprobable !

#### preuve par dénombrement

A la $i$ème itération on choisit un élément parmi $n-i+1$, et comme $i$ croit de $1$ à $n-1$, on a $n!$ parcours différents de l'algorithme.

L'algorithme choisit donc bien 1 permutation parmi $n!$, toutes différentes : il y a bien équiprobabilité des choix.

#### preuve par récurrence

1. lors de la première itération, on choisit un entier $k$ entre $0$ et $n-1$ et on échange l'élément d'indice $k$ avec celui d'indice $n-1$. Cet élément ne sera **plus jamais changé** dans la suite de l'algorithme. On en conclut que chaque élément du tableau d'entrée à la même chance d'être en dernière place de la permutation de sortie.
2. une fois la première itération terminée, tout se passe comme si on exécutait l'algorithme avec un tableau de taille $n-1$ contenant tous les éléments du tableau de départ sauf celui placé lors de la 1ère itération.
3. donc si l'algorithme fonctionne pour des tableau de longueur $n-1$, il fonctionne aussi pour des tableau de longueur $n$.
4. on peut terminer la preuve en remarquant que si le tableau a une longueur de 1, on a bien en sorite l'unique permutation du tableau en entrée.

> Cette preuve permet aussi de montrer que l'algorithme ne peux pas boucler et retrouver deux fois la même permutation avec 2 exécutions différentes.

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

```python
def melange_transposition(elements):
    copie_elements = list(elements)
    for k in range(len(copie_elements) - 1):
        i = randint(0, len(copie_elements) - 1)
        j = randint(0, len(copie_elements) - 1)
        
        copie_elements[i], copie_elements[j] = copie_elements[j], copie_elements[i]
    return copie_elements
```

> Refaites l'expérience de la [vérification expérimentale](#verif-expe) pour cet algorithme.
{: .a-faire}

J'obtiens quelque chose du type :

![mélange de transpositions]({{ "/assets/cours/algorithmie/melange_transposition.png" | relative_url }}){:style="margin: auto;display: block"}

On remarque que les premières permutations sont surreprésentées par rapport à ce qu'on devrait avoir. On remarque aussi qui'l y a des piques réguliers que l'on observe pas avec le mélange de Knuth. Ceci est du au fait que l'on peut produire une même permutation de plusieurs manière avec cet algorihtme : on produit plus facilement certaines permutations que d'autres, ce qui rend l'algorithme non equiprobable.

> lisez et comprenez l'article : <https://datagenetics.com/blog/november42014/index.html>. Il explique pourquoi cette méthode n'est pas efficace.
{: .a-faire}

Nous allons ici juste montrer que les permutations ne sorties ne sont pas équiprobables. On calcule la probabilité que l'élément $i$ reste en position $i$ à la fin d la permutation. 

> plusieurs chois jamais choisi ou choisi une fois puis replacé au bonendroit, etc. ; donc cette proba est > que jamais choisi.
{: .tbd}

### randint doit être puissant

> pseudo-aléatoire : def
> on y reviendra plus tard dans le cours
{: tbd}

pour un deck de 52 cartes trop de permutations par rapport au nombre aléatoire

il faut un randint vraiment puissant. (on verra ça plus tard.)

<https://www.i-programmer.info/programming/theory/2744-how-not-to-shuffle-the-kunth-fisher-yates-algorithm.html>

### attention aux humains

<https://draftsim.com/mtg-arena-shuffler/> ce que les maths disent de l'aléatoire vs ce que les humains disent de l'aléatoire

## autres références

Quelques autres articles sur le sujet :

* <https://possiblywrong.wordpress.com/2014/12/01/card-shuffling-algorithms-good-and-bad/>
* <https://blog.codinghorror.com/the-danger-of-naivete/>
* <https://www.stashofcode.fr/tri-aleatoire-des-elements-dun-tableau/>
