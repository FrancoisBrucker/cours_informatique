---
layout: layout/post.njk

title:  "DS 1 : mines-ponts 2017"
---

{% note "**Sujet**" %}

Le sujet du DS 1 est [L'épreuve commune d'informatique mines/ponts 2017](mines-info-2017-sujet.pdf) (sans la partie VI).

La durée du contrôle était de 3h, c'est à dire le double de celui normalement alloué à l'épreuve.

{% endnote %}

## Barème

> TBD

## Remarques

Comme en code (maxime de Kent Beck) :

1. make if work
2. make it right
3. make it fast

Pour l'instant, on se concentre sur le 1 et 2, vous aviez ainsi 3h pour un sujet de 1h30. Si vous avez bien compris et réussi le sujet, il vous faut travailler la rapidité en L2 et L3.

### Erreurs communes

* le sujet donne des fonction, il faut les utiliser.

## Correction

### Q1

Une suite de $n$ cases successives se modélise par une liste de longueur $n$. Comme les voitures sont indifférenciées et qu'il n' peut y avoir qu'une voiture au maximum par case, on peut modéliser une file de voiture par une liste $A$ :

* de longueur $n$
* s'il y a une voiture dans la case $i$ de la file on note `A[i] = True`{.language-}
* s'il n'y a pas de voiture dans la case $i$ de la file on note `A[i] = False`{.language-}

### Q2

```python
A = [True, False, True, True, False, False, False, False, False, False, True]
```

Ou si on veut la créer :

```python
n = 11
A = [False for i in range(n)]

for i in (0, 2, 3, 10):
    A[i] = True
```

### Q3

```python
def occupe(L, i):
    return L[i]
```

### Q4

Chaque case pouvant être occupée ou non, il y a deux possibilités pour chacune des $n$ cases d'une liste : il y a $2^n$ possibilités.

### Q5

Les deux solutions suivantes sont équivalentes :

```python
def égal(L1, L2):
    if len(L1) != len(L2):
        return False
    for i in range(L1):
        if L1[i] != L2[i]:
            return False
    return True
```

et

```python
def égal(L1, L2):
    return L1 == L2
```

### Q6

A part la boucle `for`{.language-} toutes les autres opérations de la méthode `égal`{.language-} sont en $\mathcal{O}(1)$. Si les deux listes à comparer sont égales, il faut parcourir tous les éléments de la liste : la complexité est donc en $\mathcal{O}(n)$ où $n$ est la longueur de la liste `L1`{.language-}.

{% attention %}
Les complexités des **deux** fonctions les mêmes. La comparaison de deux listes en python avec l'opérateur `==` est de complexité égal à la taille de la plus petite des listes.
{% endattention %}

### Q7

Le retour de la fonction `égal`{.language-} est un booléen.

### Q8

Procédons par étape. L'instruction `avancer(avancer(A, False), True)`{.language-} revient à exécuter `avancer(P1, True)` où `P1=avancer(A, False)`{.language-}. Il faut donc commencer par déterminer `P1` avant de calculer `avancer(P1, P2)`.

Comme `A = [True, False, True, True, False, False, False, False, False, False, True]`{.language-}, on a que `P1 = avancer(A, False)`{.language-} vaut `[False, True, False, True, True, False, False, False, False, False, False]`{.language-}.

De là, `avancer(P1, True)`{.language-} vaut alors : `[True, False, True, False, True, True, False, False, False, False, False]`{.language-}

### Q9

En python :

* $L[:m]$ correspond aux $m$ premiers éléments de la liste, donc ceux allant de l'indice 0 à l'indice $m-1$
* $L[m:]$ correspond aux derniers éléments de la liste en commençant par celui d'indice $m$.

Il faut faire avancer les dernier éléments de la liste (avec `avancer`{.language-}) sans toucher au  prmeirs éléments :

```python
def avancer_fin(L, m):
    return L[:m] + avancer(L[m:], False)
```

La complexité de la fonction précédente est en $\mathcal{O}(n)$ où $n$ est la taille de la liste. Car la créations
 des listes partielles et la fonction avancer sont toutes de complexités égales à la longueur des listes qu'elles manipulent.

### Q10

La case $L[m]$ étant inoccupée, faire avancer le début de la liste ne va pas faire *déborder*de voiture. On peut alors procéder exactement de la même manière que pour la question précédente (en faisant attention à l'indice de fin du découpage), ce qui donne une complexité égale à $\mathcal{O}(n)$.

```python
def avancer_debut(L, b, m):
    return avancer(L[:m + 1], b) + L[m + 1:]
```

### Q11

On remonte la liste de l'indice $i=m-1 à $i=0$ jusqu'à trouver une case non occupée. Une fois celle ci trouvée on utilise `avancer_debut`{.language-} de la question précédente.

Si aucune case n'est libre (on arrive à la fin de la boucle `for`{.language-}),une telle case n'existe pas on rend uniquement une copie de la liste puisque rien ne peut bouger.

La remontée de l'indice $i$ prenant au maximum $\mathcal{O}(m)$ opérations et comme `avancer_debut`{.language-} est de complexité proportionnelle à la taille de sa liste en entrée, la complexité totale est en $\mathcal{O}(m)$.

```python
def avance_debut_bloque(L, b, m):
    for i in range(m - 1, -1, -1):
        if not occupe(L, i):
            return avancer_debut(L, b, i)
    return list(L) # copie de la liste
```

### Q12

On procède comme indiqué dans le sujet :

1. on avance la file $L1$ et la file $L$2 à partir du croisement, aucun blocage ne peut arriver
2. la case du croisement est forcément libre pour $L1$ et $L2$ après la première étape, on peut donc avancer le début de la file $L1$
3. si le croisement est libre (la case m n'est pas occupée pour $L1$) on peut avancer le début de $L2$, sinon on effectue un avancement avec le début bloqué.

Comme il y a un nombre constant de fonction dépendant de la taille des listes en entrée, on en déduit que la complexité totale est en $\mathcal{O}(n)$ où $n$ est la taille des listes.

```python
def avancer_files(L1, b1, L2, b2):
    m = (len(L1) - 1) / 2
    
    R1 = avancer_fin(L1, m)
    R2 = avancer_fin(L2, m)
    
    R1 = avance_debut(R1, b1, m)

    if occupe(R1, m):
        R2 = avance_debut_bloque(R2, b2, m)
    else:
        R2 = avance_debut(R2, b2, m)
    
    return [R1, R2]
```

### Q13

Position initiale :

```
    E
    ▢
    ⇩ 
D ▢⇨⇩⇨▢
    ▢
    ▢
```

Après utilisation de la fonction `avancer-files(D, False, E, False)`{.language-} on obtient :

```
    E
    ▢
    ⇩ 
D ▢▢⇨▢⇨
    ⇩
    ▢
```

Ce qui donne comme listes :

* `D = [False, False, True, False, True]`{.language-}
* `E = [False, True, False, True, False]`{.language-}

### Q14

Si la file $L1$ est pleine et qu'à chaque étape on ajoute une voiture, le croisement (d'indice $m$) sera toujours occupé par une voiture de $L1$ : aucun voiture de la file $L2$ ne pourra dépasser le croisement. Si la file $L2$ est pleine jusqu'à l'indice précédent le croisement, aucune ce ces voitures ne pourra se déplacer.

```
     L2
     ⇩
     ⇩ 
L1 ⇨⇨⇨⇨⇨
     ▢
     ▢
```

### Q15

Position initiale :

```
      L2
       ⇩
       ⇩
       ⇩
       ⇩ 
L1 ⇨⇨⇨⇨▢▢▢▢▢
       ▢
       ▢
       ▢
       ▢
```

La file $L1$ étant prioritaire, les voitures de la file $L2$ ne peuvent avancer pendant les 4 premières étapes.  Puis il faut les déplacer, donc encore au moins 5 étapes. Le nombre minimal d'opérations est aisni d'au moins 4 + 5 = 9 opérations.

Ceci est suffisant :

On commence par faire 5 fois `avancer_files(L1, False, L2, False)`{.language-}. Les 4 voitures de $L1$ ont dépassé le croisement et la première voiture de $L2$ est sur le croisement :

```
      L2
       ▢
       ⇩
       ⇩
       ⇩ 
L1 ▢▢▢▢⇩⇨⇨⇨⇨
       ▢
       ▢
       ▢
       ▢
```

Puis on ajoute les nouvelles voitures de $L1$ en faisant 4 fois `avancer_files(L1, True, L2, False)`{.language-} :

```
      L2
       ▢
       ▢
       ▢
       ▢
L1 ⇨⇨⇨⇨▢▢▢▢▢
       ⇩
       ⇩
       ⇩
       ⇩ 
```

### Q16

Cette étape finale est impossible à obtenir car la file $L1$ est prioritaire. A l'étape précédente il y a forcément une voiture de la file $L1$ sur le croisement, ce qui laisse un *trou* au croisement sur la file $L2$ :

```
      L2
       ▢
       ▢
       ▢
       ⇩
L1 ▢▢▢▢⇨⇨⇨⇨?
       ⇩
       ⇩
       ⇩
       ? 
```

Ce *trou* ne peut être comblé en une étape : la position de l'étape (c) est impossible à obtenir.

### Q17

La liste étant triée, un doublon est tel que $L[i] = L[i+1]$. On peut alors supprimer les doublons en parcourant la liste $L$ et en ne considérant que les éléments tels que $L[i] > L[i-1]$. Ceci donne l'algorithme suivant :

```python#
def élimine_double(L):
    L2 = [L[0]]
    
    for i in range(1, len(L)):
        if L[i-1] < L[i]:
            L2.append(x)
    return L2
```

{% info %}
Pour une liste $L$, `L[-1]`{.language-} renvoie son dernier élément. C'est équivalent à `L[len(L) - 1]`{.language-}.
{% endinfo %}

Comme la complexité de la méthode de liste `append`{.language} est en $\mathcal{O}(1)$, la complexité du corps de la boucle for (lignes 5-6) est en $\mathcal{O}(1)$. Le nombre d'itération de cette boucle est en $\mathcal{O}(n)$, avec $n$ la taille de la liste, donc la complexité totale de l'algorithme est en $\mathcal{O}(n)$.

### Q18

La fonction `doublons`{.language-} rend une liste triée sans doublons de la liste triée passée en paramètre. Cette fonction étant récursive, nous allons le prover par récurrence sur la taille $n$ de la liste.

Si $n \leq 1$ on rend la liste en entrée, Ok. On suppose la propriété pour $n \geq 1$. A $n+1$. 

Si $L[0] \neq L[1]$, $L[0]$ est le 1er élément de la liste triée sans doublons issue de $L$ et comme :

* tous les éléments de $L[1:]$ sont strictement plus grand que $L[0]$
* par hypothèse de récurrence, `doublons(L[1:])`{.language-} rendra la liste sans doublons de la liste triée $L[1:]$

La liste triée sans doublons issue de $L$ est bien égale à $[L[0]] + doublons(L[1:]).

Si $L[0] \neq L[1]$ la liste triée sans doublons de $L$ est égale à la liste triée sans doublons de la liste $L$ privée de son élément $L[1]$. Ok

On a démontrée que `doublons`{.language-} est une fonction qui rend une liste triée sans doublons de la liste triée passée en argument. Donc elle rendra `[1, 2, 3, 5]`{.language-} pour la liste triée `[1, 1, 2, 2, 3, 3, 3, 5]`{.language-} passée en paramètre.

### Q19

Non, car elle rendrait $[1, 2, 1]$ pour la même liste en entrée.

{% note "**pour aller plus loin**" %}
La fonction `doublons(L)`{.language-} est affreuse !

Déjà, sa complexité est de l'ordre de$\mathcal{O}(n^2)$ si la liste passée en entrée est triée et sans doublons.

Mais de façon bien plus affreuse, elle n'est pas cohérente sur son retour. Parfois elle rend la liste passée en paramètre (si $n \leq 1$), parfois elle rend une copie (si $L[0] < L[1]$) et parfois elle rend une copie **et** modifie la liste passée en paramètre (si $L[0] == L[1]$). Bref, c'est du très mauvais code. Il faut **toujours** être consistant. Soit on modifie les paramètre en entrée et dans ce cas là on ne rend rien, **soit** on rend quelque chose et dans ce cas là on ne modifie pas les paramètres d'entrée.

{% endnote %}

### Q20

* la fonction `recherche`{.language-} rend un booléen
* `but`{.language-} est une liste à deux éléments, les deux listes formants le croisement.
* `espace`{.language-} est une liste de croisements (qui sont des listes à deux éléments).
* `successeurs`{.language-} rend une liste de croisements (qui sont des listes à deux éléments).

### Q21

`in2` correspond à une recherche dichotomique, dont la complexité est de l'ordre de $\mathcal{O}(log_2(n))$, alors que `in1` est une recherche linéaire dont la complexité est de l'ordre de $\mathcal{O}(n)$.

Il est donc **beaucoup** plus judicieux de d'utiliser `in2` plutôt que `in1`.

### Q22

```python
def versEntier(L):
    entier = 0
    
    puissance_2 = 1
    
    for x in reversed(L):
        if x == True:
            entier += puissance_2 
        puissance_2 *= 2
    
    return entier  
```

### Q23

Il faut que la taille de `L` soit au minimum égal à la valeur entière du $\log_2$.
Il faut que `i >= 0` pour que la boucle de fasse pas d'erreur lors de l'affectation à `res[i]`.

### Q24

Comme on supprime les doublons et que l'on s'arrête si l'espace de solutions n'a pas grossi, au pire, l'algorithme s'arrêtera lorsque tous les croisements possibles seront vus, comme il y en a un nombre fini (borné par $2 * 2^n$ listes de 2 files au maximum) l'algorithme va s'arrêter.

### Q25

A chaque étape, les nouvelles solutions sont trouvées à partir d'éléments obtenus à l'étape précédente, sinon elles seraient déjà présent dans l'ensemble des solutions.

Le nombre minimum d'étape pour trouver une solution est donc le nombre de fois où l'on a bouclé sur le `while` de la fonction recherche.
