---
layout: layout/post.njk

title:  "DS 1 : mines-ponts 2017"
---

{% note "**Sujet**" %}

Le sujet du DS 1 est [L'épreuve commune d'informatique mines/ponts 2017](../mines-info-2017-sujet.pdf){.fichier} (sans la partie VI).

Durée du contrôle : 3h.

{% endnote %}

La durée du contrôle était de 3h, le double de celui normalement alloué à l'épreuve. Le but était de se concentrer sur la justesse de vos raisonnement et de vos justifications avant de travailler la rapidité. On reprend ainsi la célèbre maxime de Kent Beck sur l'ordre de développement d'un bon code (un bon code doit avoir les 3, mis en œuvre dans cet ordre) :

1. make if work
2. make it right
3. make it fast

Si vous avez bien compris et réussi le sujet, il vous faut travailler la rapidité en L2 et L3.

## Barème

* Questions Q1 à Q20 : 1 point par question
* Questions Q21 à Q25 : 1/2 point par question
* Total : Noté sur 22.5 points

Statistiques descriptives du contrôle :

* moyenne : 13,68
* écart-type : 4,41
* min : 0,00
* max : 20,00

La moyenne d'un examen devrait être de 12 avec un écart type de 2. Ici elle est bien trop élevée (13.7) et l'écart-type est également bien trop important (4.5). Ceci signifie que : 1 - l'examen était trop facile (*ie.* vous aviez trop de temps pour faire un examen de 1h30) et 2 - la population est hétérogène (*ie.* il y a trop de personnes ayant plus de 18).

Ventilation des notes :

* $N < 10$ : 10 personnes
* $10 \leq N < 14$ : 12 personnes
* $14 \leq N < 18$ : 13 personnes
* $18 \leq N$ : 7 personnes

Si vous avez moins de 12, vous ne pouvez vous contenter de votre note, il faut encore progresser pour avoir un niveau acceptable en informatique et si vous avez moins de 14 vous êtes dans la deuxième moitié de la promo.

A votre niveau, progresser signifie principalement :

* **se relire** pour supprimer les erreurs bêtes qui font perdre des quart de points
* **relire la question** avant de répondre pour vérifier que l'on ne va pas répondre à côté
* et surtout **tester ses algorithmes** sur une feuille de brouillon avec de petits exemples pour vérifier qu'ils font bien ce que l'on pense qu'ils font

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
A = [False for i in range(11)]

for i in (0, 2, 3, 10):
    A[i] = True
```

La complexité de l'algorithme précédent est en $\mathcal{O}(1)$ car il ne fonctionne **que** pour $A$ qui est de taille $11$.

#### Remarques suite à la correction des copies

* `1 != True`{.language-} les booléens prennent 2 valeurs `True`{.language-} et `False`{.language-} pas 0 ou 1 qui sont des entiers. On peut interpréter des entiers comme des booléens (0 est faux et tous les autres entiers sont vrais) mais ce n'est pas la même chose.
* Comme la liste `A`{.language-} que l'on vous demande de construire est une constante, la complexité de son calcul est en $\mathcal{O}(1)$. puisqu'il ne fonctionne que pour `A`{.language-} par pour une autre liste.

### Q3

```python
def occupe(L, i):
    return L[i]
```

La complexité de fonction `occupe(L, i)` est $\mathcal{O}(1)$ puisque'il suffit accéder à un élément d'une liste. Elle donne bien le résultat attendu si $L$ est conforme à Q1.

#### Remarque suite à la correction des copies

On ne teste pas la véracité des booléens, on l'utilise. On remplace donc tous les `if L[i] == true return True else return False`{.language-} par `return L[i]`{.language-} qui est équivalent.

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

Les deux fonctions vérifient que les longueurs des deux listes sont égales et que leurs éléments coïncident.

#### <span id="rq-q5"></span> Remarque suite à la correction des copies

Attention aux tailles des listes.

```python
def compare(L1, L2):
    for i in range(len(L1)):
        if L1[i] != L2[i]:
        return False
    return True
```

Produit une erreur si `len((L2)) < len(L1)`{.language-} et est faux si `len((L2)) > len(L1)`{.language-} (par exemple `L1= [1, 2]`{.language-} et `L2 = [1]`{.language-}).

### Q6

A part la boucle `for`{.language-} toutes les autres opérations de la méthode `égal`{.language-} sont en $\mathcal{O}(1)$. Si les deux listes à comparer sont égales, il faut parcourir tous les éléments de la liste : la complexité est donc en $\mathcal{O}(n)$ où $n$ est la longueur de la liste `L1`{.language-}.

{% attention %}
Les complexités des deux fonctions **sont les mêmes**. La comparaison de deux listes en python avec l'opérateur `==` est de complexité égal à la taille de la plus petite des listes.
{% endattention %}

### Q7

Le retour de la fonction `égal`{.language-} est un booléen.

#### <span id="rq-q7"></span> Remarque suite à la correction des copies

Le terme demandé est ***booléen***. Dire juste `True`{.language-} ou `False`{.language-} n'est pas suffisant.

### Q8

Procédons par étape. Position initiale `A = [True, False, True, True, False, False, False, False, False, False, True]`{.language-} :

```
A  : ⇨▢⇨⇨▢▢▢▢▢▢⇨
```

L'instruction `P2 = avancer(avancer(A, False), True)`{.language-} revient à exécuter `avancer(P1, True)` où `P1=avancer(A, False)`{.language-}. Il faut donc commencer par déterminer `P1` avant de calculer `avancer(P1, P2)`.

On a que `P1 = avancer(A, False)`{.language-} vaut `[False, True, False, True, True, False, False, False, False, False, False]`{.language-}.

```
A  : ⇨▢⇨⇨▢▢▢▢▢▢⇨
P1 : ▢⇨▢⇨⇨▢▢▢▢▢▢
```

De là, `avancer(P1, True)`{.language-} vaut alors : `[True, False, True, False, True, True, False, False, False, False, False]`{.language-}

```
A  : ⇨▢⇨⇨▢▢▢▢▢▢⇨
P1 : ▢⇨▢⇨⇨▢▢▢▢▢▢
P2 : ⇨▢⇨▢⇨⇨▢▢▢▢▢
```

### Q9

En python :

* $L[:m]$ correspond aux $m$ premiers éléments de la liste, donc ceux allant de l'indice 0 à l'indice $m-1$
* $L[m:]$ correspond aux derniers éléments de la liste en commençant par celui d'indice $m$.

Il faut faire avancer les dernier éléments de la liste (avec `avancer`{.language-}) sans toucher au  premiers éléments :

```python
def avancer_fin(L, m):
    return L[:m] + avancer(L[m:], False)
```

La complexité de la fonction précédente est en $\mathcal{O}(n)$ où $n$ est la taille de la liste. Car la créations
 des listes partielles et la fonction avancer sont toutes de complexités égales à la longueur des listes qu'elles manipulent.

#### <span id="rq-q9"></span> Remarques suite à la correction des copies

* Le sujet donne des fonctions à coder, il faut les utiliser. Ne recodez pas tout à chaque fois. En plus, les algorithmes deviennent plus simple.
* Attention aux complexité : la concaténation crée une nouvelle liste, sa complexité est égale à la somme des tailles des 2 listes.

### Q10

La case $L[m]$ étant inoccupée, faire avancer le début de la liste ne va pas faire *déborder*de voiture. On peut alors procéder exactement de la même manière que pour la question précédente (en faisant attention à l'indice de fin du découpage), ce qui donne une complexité égale à $\mathcal{O}(n)$.

```python
def avancer_debut(L, b, m):
    return avancer(L[:m + 1], b) + L[m + 1:]
```

#### <span id="rq-q10"></span> Remarques suite à la correction des copies

Idem que pour la question précédente :

* Le sujet donne des fonctions à coder, il **faut** les utiliser. Ne recodez pas tout à chaque fois. En plus, les algorithmes deviennent plus simple.
* Attention aux complexité : la concaténation crée une nouvelle liste, sa complexité est égale à la somme des tailles des 2 listes.

### Q11

On remonte la liste de l'indice $i=m-1$ à $i=0$ jusqu'à trouver une case non occupée. Une fois celle ci trouvée on utilise `avancer_debut`{.language-} de la question précédente.

Si aucune case n'est libre (on arrive à la fin de la boucle `for`{.language-}),une telle case n'existe pas on rend uniquement une copie de la liste puisque rien ne peut bouger.

La remontée de l'indice $i$ prenant au maximum $\mathcal{O}(m)$ opérations et comme `avancer_debut`{.language-} est de complexité proportionnelle à la taille de sa liste en entrée, la complexité totale est en $\mathcal{O}(m)$.

```python
def avance_debut_bloque(L, b, m):
    for i in range(m - 1, -1, -1):
        if not occupe(L, i):
            return avancer_debut(L, b, i)
    return list(L) # copie de la liste
```

Il y a aussi la version récursive qui se rappelle s'il n'est pas possible de résoudre le problème directement :

```python
def avance_debut_bloque(L, b, m):
    if m == 0:
        return list(L) # copie de la liste    
    elif not occupe(L, m - 1):
        return avancer_debut(L, b, m - 1)
    else:
        return avance_debut_bloque(L, b, m - 1)
```

{% attention %}
Le sujet demande de rendre une **copie** de la liste.
{% endattention %}

#### <span id="rq-q11"></span> Remarque suite à la correction des copies

Pour cette question en particulier, utiliser les questions et les algorithmes précédents rend le code bien plus clair et facile à lire.

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

#### <span id="rq-q12"></span> Remarque suite à la correction des copies

La liste étant de longueur impaire, l'indice du milieu est au choix :

* `m = (len(L) - 1) / 2`{.language-}
* `len(L) // 2`{.language-}

Mais aucune autre formule. Si vous aviez fait un test de votre formule avec un petit exemple, ne nombreuses fautes auraient pu être évitées.

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

La file $L1$ étant prioritaire, les voitures de la file $L2$ ne peuvent avancer pendant les 4 premières étapes.  Puis il faut les déplacer, donc encore au moins 5 étapes. Le nombre minimal d'opérations est ainsi d'au moins 4 + 5 = 9 opérations.

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

```python/
def élimine_double(L):
    L2 = [L[0]]
    
    for i in range(1, len(L)):
        if L[i-1] < L[i]:
            L2.append(x)
    return L2
```

Comme la complexité de la méthode de liste `append`{.language-} est en $\mathcal{O}(1)$, la complexité du corps de la boucle for (lignes 5-6) est en $\mathcal{O}(1)$. Le nombre d'itération de cette boucle est en $\mathcal{O}(n)$, avec $n$ la taille de la liste, donc la complexité totale de l'algorithme est en $\mathcal{O}(n)$.

#### <span id="rq-q17"></span> Remarques suite à la correction des copies

* `del L[i]`{.language-} n'est **pas** en $\mathcal{O}(1)$, il faut décaler tout ce qui est à droite de l'indice $i$ d'une case vers la gauche. Sa complexité est donc en taille de la liste.
* `L + [a]`{.language-} n'est **pas** en $\mathcal{O}(1)$, il faut créer une nouvelle liste contenant tous les éléments. Sa complexité est donc en taille de la liste.

Une erreur récurrente qui fait des bug difficile à trouver : on ne modifie pas ce sur quoi on itère. Donc les choses du style :

```python
for i in range(len(L)):
    if truc:
        del L[i]
```

Vont rater car $i$ va à un moment aller plus loin que la liste actuelle. Si vous voulez faire ce genre de chose il faut utiliser un `while`{.language-} :


```python
i = 0
while i < len(L):
    if truc:
        del L[i]
    else:
        i += 1
```

Enfin, on ne modifie par l'itérateur, ça ne sert à rien :

```python
for i in range(len(L)):
    if truc:
        i += 1
```

Est inutile, lorsque l'on va recommencer la boucle $i$ reprendra son court normal, car il va prendre la valeur suivante du range. Pour incrémenter plusieurs fois l'itérateur il faut utiliser un `while`{.language-} :

```python
i = 0
while i < len(L):
    if truc:
        i += 1
    else:
        i += 1
```

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

#### Pour aller plus loin

La fonction `doublons(L)`{.language-} est affreuse !

Déjà, sa complexité est de l'ordre de$\mathcal{O}(n^2)$ si la liste passée en entrée est triée et sans doublons.

Mais de façon bien plus affreuse, elle n'est pas cohérente sur son retour. Parfois elle rend la liste passée en paramètre (si $n \leq 1$), parfois elle rend une copie (si $L[0] < L[1]$) et parfois elle rend une copie **et** modifie la liste passée en paramètre (si $L[0] == L[1]$). Bref, c'est du très mauvais code. Il faut **toujours** être consistant. Soit on modifie les paramètre en entrée et dans ce cas là on ne rend rien, **soit** on rend quelque chose et dans ce cas là on ne modifie pas les paramètres d'entrée.

### Q20

* la fonction `recherche`{.language-} rend un booléen
* `but`{.language-} est une liste de deux éléments formant le croisement. Il correspond à l'état qe l'on cherche à atteindre
* `espace`{.language-} est une liste de croisements (qui sont des listes à deux éléments). Cette liste correspond à tous les états que l'on peut atteindre à partir de init(qui est une liste de 2 liste formant un croisement)
* `successeurs`{.language-} rend une liste de croisements (qui sont des listes à deux éléments).

### Q21

`in2`{.language-} correspond à une recherche dichotomique, dont la complexité est de l'ordre de $\mathcal{O}(log_2(n))$, alors que `in1`{.language-} est une recherche linéaire dont la complexité est de l'ordre de $\mathcal{O}(n)$.

Il est donc **beaucoup** plus judicieux de d'utiliser `in2`{.language-} plutôt que `in1`{.language-}.

### Q22

un entier $x$ se représente de façon binaire par l'équation :

$$
x = \sum_{i=0}^{i = \log_2(x)} x_i 2^i
$$

Où les $x_i$ valent soit $1$ soit $0$. L'entier $x$ est représenté par $\log_2(x)$ bits valant chacun $x_i$.

On peut alors associer à une liste $L$ de $n$ booléens les $x^L_i$ valant $1$ si `L[n-1-i] == True`{.language-} et 0 si `L[i] == False`{.language-}. La représentation binaire de $L$ est alors représentée par le nombre :

$$
N(l) = \sum_{i=0}^n x^L_i 2^i
$$

Pour $L = [True, False, False]$ on a $0 \cdot 2^0 + 0 \cdot 2^1 + 1 \cdot 2^2$, ce qui correspond au nombre binaire $100$ qui vaut 4.

L'algorithme ci-après en est un calcul. Sa complexité est en $\mathcal{O}(n)$

```python
def versEntier(L):
    entier = 0
    puissance_2 = 1
    
    for i in range(len(L) - 1, -1, -1):
        if L[i]:
            entier += puissance_2 

        puissance_2 *= 2
    
    return entier  
```

Ou dans l'autre sens (vu dans une copie) :

```python
def versEntier(L):
    entier = 0
    
    for i in range(len(L)):
        entier *= 2

        if L[i]:
            entier += 1
    
    return entier  
```

#### <span id="rq-q22"></span> Remarques suite à la correction des copies

Le calcul de $2^i$ ne compte pas pour $\mathcal{O}(1)$. On a vu en cours qu'il faut toujours au minimum $\log_2(i)$ opérations pour cela. La complexité de la fonction suivante est donc en $\mathcal{O}(n\log(n))$ et **pas** en $\mathcal{O}(n)$ :

```python
def f(n):
    s = 0
    for i in range(n):
        s += 2 ** i
    
    return s
```

### Q23

Il faut que la taille de `L`{.language-} soit au minimum égal à la valeur entière du $\log_2(n)$.
Il faut que `i >= 0`{.language-} pour que la boucle de fasse pas d'erreur lors de l'affectation à `res[i]`{.language-}.

### Q24

Comme on supprime les doublons et que l'on s'arrête si l'espace de solutions n'a pas grossi, au pire, l'algorithme s'arrêtera lorsque tous les croisements possibles seront vus, comme il y en a un nombre fini (borné par $2 * 2^n$ listes de 2 files au maximum) l'algorithme va s'arrêter.

### Q25

A chaque étape, les nouvelles solutions sont trouvées à partir d'éléments obtenus à l'étape précédente, sinon elles seraient déjà présent dans l'ensemble des solutions.

Le nombre minimum d'étape pour trouver une solution est donc le nombre de fois où l'on a bouclé sur le `while`{.language-} de la fonction recherche.
