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

Comme `A = [True, False, True, True, False, False, False, False, False, False, True]`{.language-}, on a que `P1 = avancer(A, False)`{.language-} vaut `[False, True, False, True, True, False, False, False, False, False, False]`{.language-}. De là, `avancer(P1, True)` vaut alors : `[True, False, True, False, True, True, False, False, False, False, False]`

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

On remonte la liste de l'indice $i=m-2 à $i=0 et on déplace la voiture de $i$ à $i+1$ si la case en $i+1$ est libre.

Ceci prend $\mathcal{O}(m)$ opérations.

```python
def avance_debut_bloque(L, b, m):
    L = list(L)  # copie de la liste

    for i in range(m - 2, -1, -1):
        if not occupe(L, i + 1):
            L[i+1] = L[i]
            L[i] = False

    if not occupe(L, 0) and b:
        debut[0] = True
    return L
```

### Q12

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

* `D = [False, False, True, False, True]`
* `E = [False, True, False, True, False]`

### Q14

Si la file `L1` est pleine, la file `L2` est pleine jusqu'à l'indice `m-1` et qu'à chaque étape on ajoute une voiture, le croisement sera occupé par une voiture de la file `L1` à  chaque étape : les voiture de la fie `L2` ne pourront jamais dépasser le croisement.

### Q15

Le nombre minimal d'opérations est au moins 4 + 5 = 9 opérations. En effet, la file `L1` étant prioritaire, les voitures de la file `L2` ne peuvent avancer pendant les 4 premières étapes.  Puis il faut les déplacer, donc encore au moins 5 étapes.

Ceci est suffisant :

* 5 fois `avancer_files(L1, False, L2, False)` : les 4 voitures de `L1` ont dépassé le croisement et la première voiture de `L2` est sur le croisement.
* 4 fois `avancer_files(L1, True, L2, False)` : on ajoute les voitures à `L1`

### Q16

Cette étape finale est impossible à obtenir car la file `L1` est prioritaire. La seule position précédente de l'étape (c) possible  est :

* pour `L1` : `[False, False, False, False, True, True, True, True, False]]`
* donc pour `L2` : `[False, False, False, True, False, True, True, True, False]]`

Comme cette étape ne mène pas à l'étape (c), la position est impossible à obtenir.

### Q17

```python
def élimine_double(L):
    L2 = [L[0]]
    
    for x in L:
        if x != L2[-1]:
            L2.append(x)
    return L2
```

*Nota Bene* : Pour une liste, `L[-1]` renvoie le dernier élément d'une liste. C'est équivalent à `L[len(L) - 1]`.

### Q18

C'est une fonction qui supprime les doublons d'une liste triée. Elle rend `[1, 2, 3, 5]`.

### Q19

Non, car elle rendrait `[1, 2, 1]` pour la même liste en entrée.

### Q20

* la fonction `recherche` rend un booléen
* `but` est une liste à deux éléments, les deux listes formants le croisement.
* `espace` est une liste de croisements (qui sont des listes à deux éléments).
* `successeurs` rend une liste de croisements (qui sont des listes à deux éléments).

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
