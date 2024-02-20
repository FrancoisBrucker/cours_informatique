---
layout: layout/post.njk

title: Algorithmes classiques

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Algorithmes classiques dont l'intérêt est à la fois esthétique (ce sont de jolis algorithmes),
pratiques (ils mettent en oeuvre des techniques facilement réutilisables) et didactiques (trouver et prouver leurs fonctionnement vous fera progresser).

## Récursion et complexité

### Exercice 1

On considère le code suivant :

```python
def ma_fonction(n):
    if n < 5:
        return 2
    return ma_function(n-1) + ma_fonction(n-4)
```

- Quelle est la complexité de cet algorithme ? $\mathcal{O}(1)$, $\mathcal{O}(2^n)$ ou $\mathcal{O}(n)$ ? Justifiez votre réponse.
- Donnez une version itérative de l'algorithme

### Exercice 2

On considère le code suivant :

```python
def ma_fonction(n):
    if n < 3:
        return 2
    return (4 + ma_function(n // 2))) * 2 * ma_fonction(n // 4)
```

- Quelle est l'équation de complexité vérifiée par ce algorithme ?

  - $t(n)= \mathcal{O}(1) + t(n/2) + 2 \cdot t(n/4)$
  - $t(n)= \mathcal{O}(1) + t(n/2) + t(n/4)$
  - $t(n) = t(n/2) \cdot t(n/4)$

- Calculez la complexité de l'algorithme

## Tour de Hanoï

Les _tours de Hanoï_ sont un célèbre casse tête inventé par Édouard Lucas qui consiste à déplacer $n$ disques de diamètres différents d'une tour de _"départ"_ à une tour d' _"arrivée"_ en passant par une tour _"intermédiaire"_, tout en respectant les règles suivantes :

- on ne peut déplacer qu'un disque à la fois
- on ne peut placer un disque sur un disque plus petit que lui.

On suppose que cette dernière règle est également respectée dans la configuration de départ.

Donnez un algorithme récursif permettant de résoudre le problème. Quelle est sa complexité ? Peut-on faire mieux ?

## Polynômes

Un polynôme peut être vu comme une liste de ses coefficients. Le polynôme $P(x) = 1 + 3x^2$ s'écrira ainsi avec la liste $[1, 0, 3]$ et plus généralement, le polynôme $P(x) = \sum_{i=0}^n a_ix^i$ s'écrira sous la forme d'une liste $L$ à $n+1$ éléments telle que $L[i] = a_i$.

Manipulons cette structure.

### Écrivez une fonction _somme_

Écrivez une fonction permettant de rendre le polynôme $R(x) = P(x) + Q(x)$, somme des 2 polynômes $P(x)$ et $Q(x)$ passés en paramètres.

Vous pourrez utiliser la méthode `append`{.language-} des listes qui ajoute un élément en fin de liste (si `l= [1, 2]`{.language-}, l'instruction `l.append(3)`{.language-} **modifie** `l`{.language-}, pour qu'elle soit égale à `l= [1, 2, 3]`{.language-})

### Écrivez une fonction _produit_

Écrivez une fonction permettant de rendre le produit le polynôme $R(x) = P(x) \cdot Q(x)$, produit des 2 polynômes $P(x)$ et $Q(x)$ passés en paramètres.

### Écrivez une fonction _valeur_

Écrivez une fonction prenant un polynôme $P(x)$ et un réel $r$ et rendant l'évaluation $P(r)$ de $P(x)$ en $r$.

Vous pourrez utiliser le fait que `x ** i`{.language-} en python soit égal à $x^i$

L'exonentiation est une opération couteuse en multiplications. Combien en avez-vous eu besoin pour exécuter votre fonction ?

### Amélioration

Si on note :

- $A(x) = a_0$
- $X(x) = x$
- $P(x) = \sum_{i=0}^n a_ix^i$
- $Q(x) = \sum_{i=0}^{n-1} a_{i+1}x^i$

On a clairement que : $P(x) = A(x) + X(x) \cdot R(x)$.

En déduire une méthode d'évaluation de polynômes moins gourmande en multiplications.

## Suppression de valeurs

La structure de donnée utilisée ici est la **_liste_**. On considérera que :

- la création d'une liste vide se fait en $\mathcal{O}(1)$ opérations,
- l'ajout d'un élément en fin de liste se fait en $\mathcal{O}(1)$ opérations,
- lire un élément d'une liste se fait en $\mathcal{O}(1)$ opérations.

### Suppression d'une valeur

Écrire un algorithme permettant de résoudre le problème suivant :

- Données : Une liste `L`{.language-} et une valeur `val`{.language-}.
- Rendre : Une liste `L_2`{.language-}, restriction de `L`{.language-} aux valeurs différentes de `val`{.language-}.

Quel est sa complexité ?

### Suppression d'une valeur in-place

Écrire un algorithme permettant de supprimer une valeur d'une liste :

1. sans créer de liste annexe
2. de façon optimale

Pour cet exercice, on ne se préoccupe pas de l'ordre des éléments dans la liste.

## Suppression de doublons

Même structure que pour l'exercice précédent.

La structure de donnée utilisée ici est la **_liste_**. On considérera que :

- la création d'une liste vide se fait en $\mathcal{O}(1)$ opérations,
- l'ajout d'un élément en fin de liste se fait en $\mathcal{O}(1)$ opérations,
- lire un élément d'une liste se fait en $\mathcal{O}(1)$ opérations.

### Suppression de doublon en conservant l'ordre

Utilisez la question précédente pour écrire un algorithme résolvant le problème suivant :

- Données : Une liste `L`{.language-}.
- Rendre : Une liste `L_2`{.language-} ne contenant qu'une seule occurrence de chaque valeur de `L`{.language-} et en conservant le même ordre.

Quel est sa complexité ?

### Suppression de doublon d'une liste ordonnée

Même question que précédemment, mais on considère que la liste `L`{.language-} en entrée est triée. Donnez un algorithme en $\mathcal{O}(n)$ pour résoudre ce problème, où $n$ est le nombre d'éléments de `L`{.language-}.

### Suppression de doublon d'une liste sans ordre

Si l'ordre des éléments de `L_2`{.language-} n'est pas important, proposez une meilleure solution à la deuxième question.

## Min et max d'un tableau d'entiers

On compte précisément les comparaisons (comme on l'a fait en comptant les multiplications avec le problème de l'exponentiation)

- juste min
- juste max
- faire les deux ensemble

## Suite de Fibonacci

- F(n) = 1/sqrt(5)(phi^n - phi'^n) = ou` racines de x^2 = x + 1 (phi = nombre d'or, phi'=-1/phi)
- F(n+1)/F(n) -> phi
- récursif, algorithme et complexité
- itératif, algorithme et complexité
- récursif en temps linéaire (en montée)

## Triangle de Pascal

- récursif, algorithme et complexité
- itératif, algorithme et complexité
- itératif avec une complexité en mémoire de $\mathcal{O}(n)$

## Ackermann

La fonction d'Ackermann se définit de la manière suivante, pour tous entiers $m$ et $n$ positifs :

<div>
$$
A(m,n) =
\left\{
\begin{array}{lll}
 & n + 1 &\mbox{ si } m = 0\\
& A(m - 1, 1) &\mbox{ si } n = 0, m>0\\
& A(m - 1, A(m, n - 1)) &\mbox{ sinon }\\
\end{array}
\right.
$$
</div>
    
- Donnez un pseudo-code récursif et itératif de cette fonction.
- Donnez le nombres d'appels récursif du calcul de A(n, n).

> TBD calculs de A(m, n) avec les puissances itérées de Knuth.

## Méthodes de tri

### Tri par base

Ce tri s'applique uniquement aux entiers positifs, que l'on considère écrits en base 2. Notre entrée est une liste de listes composées de 0 et de 1. Par exemple : T = [[1, 0, 0, 1], [1, 1, 1, 0], [0, 0, 0, 1]] qui correspond aux nombres [9, 14, 1] On supposera également que toutes les listes ont même longueur. Le principe de ce tri est très simple :

- On considère d'abord le bit de poids le plus faible (_ie._ le plus à droite). On crée alors deux listes L0 et L1 initialement vides et on va itérativement considérer chaque élément de la liste à trier :
  - les entiers dont le bit de poids le plus faible est 0 sont ajoutés à la fin de L0
  - les entiers dont le bit de poids le plus faible est 1 sont ajoutés à la fin de L1
- On concatène les deux sous-listes T = L0 + L1
- On recommence sur le bit à gauche de celui qu'on vient de traiter.
- ...

Les parcours des liste T se font, toujours, de la gauche vers la droite.

Pour notre exemple :

1. après premiere boucle : [[1,1,1,0], [1, 0, 0, 1], [0, 0, 0, 1]]
1. après deuxième boucle : [[1, 0, 0, 1], [0, 0, 0, 1], [1,1,1,0]]
1. après troisième boucle :[[1, 0, 0, 1], [0, 0, 0, 1], [1,1,1,0]]
1. après quatrième boucle : [[0, 0, 0, 1], [1, 0, 0, 1], , [1,1,1,0]]

Donnez le pseudo-code, la preuve et la complexité de cet algorithme (on supposera que l'on dispose d'une fonction qui, étant donnés deux entiers $n$ et $i$, donne le $i^{me}$ bit de $n$).

Rappelez la complexité minimale du tri (dans le cas le pire). Commentaires.

### Tri par monotonies

Étant donné un tableau $T$, **_une monotonie_** est une suite croissante maximale d'éléments consécutifs de $T$. Par exemple :
si $T = [2,6, 1,3, 3, 5,2,6, 4,0, 1,8,9,1,3, 2,0,1,0]$, alors $[2,6]$, $[1,3,3,5]$, $[2,6]$, $[4]$, $[0, 1,8,9]$, $[1,3]$, $[2]$, $[0,1]$ et $[0]$ sont les monotonies de $T$.

Donnez un algorithme qui, étant donné un tableau $T$ construit une liste (de listes) $L$, chaque élément de $L$ étant une monotonie de $T$ (et vice versa). À partir de notre exemple, on obtient :
$L = [[2,6], [1,3,3,5],[2,6], [4], [0, 1,8,9], [1,3], [2] ,[0,1], [0]]$.

Donnez un algorithme qui fusionne deux monotonies ; par exemple, à partir de $[2,6]$ et $[1,3,3,5]$, on obtient $[1,2,3,3,5,6]$ (ceci est aussi une question de cours).

Donnez un algorithme qui, étant donnée une liste $L$ de monotonies, les fusionne deux-à-deux (en en laissant éventuellement une ``toute seule" à la fin) et met le résultat dans une liste (de listes) $L'$. Par exemple, à partir de
$L = [[2,6], [1,3,3,5],[2,6], [4], [0, 1,8,9], [1,3], [2] ,[0,1], [0]]$, on obtient $L' = [[1,2,3,3,5,6], [2,4,6],[0,1,1,3,8,9], [0,1,2], [0]]$.

En déduire un algorithme de tri. Donnez sa complexité dans le cas le meilleur et dans le cas
le pire.

Cet algorithme est en fait une variante d'un algorithme vu en cours. Lequel ?

## Compteur binaire

- suivant
- tous
- calcul de la complexité de tous
- en déduire la complexité en moyenne de suivant.

## Jets de dés

- algorithme itératif (généralisation du compteur binaire)
- algorithme récursif. Complexité en mémoire ?

On considère l'algorithme suivant:

```python
def LaFonction (L, n):
    if n == 0:
        print(L)
    else:
        for i in range(6):
            LaFonction(L + [i + 1], n -  1)

```

On rappelle que, appliqué à des listes, le $+$ est la concaténation. On supposera que l'appel initial se fait avec la liste L vide. Que fait cet algorithme ? Quelle est sa complexité ? Quelle place mémoire consomme-t-il ?

## Chaînes de caractères

### Sous-séquence

Soient deux chaînes de caractères $S_1$ et $S_2$. On dit que $S_2$ est une {\em sous-séquence} de $S_1$ si il existe une fonction strictement croissante

$$
f : \{0,\ldots, len(S_2)-1\} \longrightarrow \{0,\ldots, len(S_1)-1\}
$$

Telle que $S_1[f(j)] = S_2[ j]$ pour tout $j$ de $\{0,\ldots, len(S_2)-1\}$.

Proposez, prouvez et donnez la complexité d'un algorithme qui détermine si $S_2$ est une sous-séquence de $S_1$.

### Sous-mot

Soient deux chaînes de caractères $S_1$ et $S_2$. On dit que $S_2$ est un **_sous-mot_** de $S_1$ s'il existe un indice $i$ tel que $S_2[j] = S_1[i + j]$ pour tout $j$ de $0$ à $len(S_2) - 1$.

- Proposez, prouver et donner la complexité d'un algorithme qui détermine si $S_2$ est un sous-mot de $S_1$.
- Si toutes les lettres de $S_2$ sont deux à deux différentes, donnez un algorithme en $\mathcal{O}(len(S_1))$ pour résoudre ce problème.

## Algorithme mystère

L'algorithme suivant, à partir d'une liste d'entiers positifs, rend une autre liste. On suppose pour cet exercice que la création des deux listes tempo et sortie est en $\mathcal{O}(1)$ opérations.

```python
def mystère(tab):
    k = max(tab)
    tempo = [0] * (k + 1)
    sortie = [0] * len(tab)

    for i in range(len(tab)):
        tempo[tab[i]] += 1
    for i in range(1, k + 1):
        tempo[i] += tempo[i - 1]

    for i in range(n):
        sortie[i] = tempo[tab[i]] - 1
        tempo[tab[i]] -= 1

    return sortie

```

- Donnez la complexité de cet algorithme.
- Dites ce qu'il fait et prouvez le (_indication_: après chacune des deux premières boucles, que contient tempo ?).
- Commentaires ?

## Cols

- d'une liste (max ou min local). Trouver un algorithme en log
- d'une matrice (min ligne et max colonne) avec un algorithme linéaire en la taille de la matrice (pourquoi le log ne marche-t-il pas ?)

## Permutation circulaire

Étant donné un liste $L$ de longueur $n$ et un entier $k$, le problème est de transformer $L$ par permutation circulaire en décalant (circulairement) tous les éléments de $L$ de $k$ places. Par exemple, avec $L = \text{LongtempsJeMeSuisCouchéDeBonneHeure}$ et $k = 4$, on obtient $L' = \text{eureLongtempsJeMeSuisCouchéDeBonneH}$.

- Donnez un algorithme $\text{Permut}(L, k)$ qui, avec une liste $L$ et un entier $k$ en entrées, construit une nouvelle liste $L'$, permutation circulaire de $L$.
- Si on veut transformer $L$ en $\text{Permut}(L,k)$, montrez que la place mémoire utilisée (en plus de celle des données du problème ($L$)) par votre algorithme est $O(n)$.

On veut maintenant faire une permutation circulaire sur site, _ie._ sans utiliser plus que $O(1)$ place mémoire supplémentaire (il arrive (par exemple quand on étudie le génome) que $n$ soit très grand). Il faut pour cela
remarquer que permuter circulairement $L$ revient à prendre les $k$ dernières lettres de $L$ et à les mettre en tête. On note $L^R$ la liste $L$ **_renversée_** (par exemple, si $L =\text{Couché}$, $L^R = \text{éhcuoC}$).

- Donnez un algorithme en $O(n)$ et utilisant $O(1)$ place mémoire supplémentaire, qui transforme $L$ en $L^R$.
- Montrez que, si on note $L = AB$, où $B$ est de longueur $k$ (par exemple, avec $L = \text{LongtempsJeMeSuisCouchéDeBonneHeure}$ et $k = 4$, $A =\text{LongtempsJeMeSuisCouchéDeBonneH}$ et $B =\text{eure}), alors \text{Permut}(L, k) = (A^RB^R)^R$.
- Déduisez-en un algorithme de complexité $O(n)$ qui permute une liste (de longueur $n$), _ie._ qui transforme $L$ en $\text{Permut}(L,k)$, en utilisant $O(1)$ espace mémoire supplémentaire.

## Algorithmes arithmétique

- addition de listes de chiffres
- multiplications de listes de chiffres

(- [optimisation de Karastuba](https://fr.wikipedia.org/wiki/Algorithme_de_Karatsuba))

## Matrices

- structure
- addition
- produit par un scalaire
- produit naïf

(- [produit de Strassen](https://fr.wikipedia.org/wiki/Algorithme_de_Strassen)}
