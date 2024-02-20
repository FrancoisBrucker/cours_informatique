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

## Suite de Fibonacci

[La suite de Fibonacci](https://fr.wikipedia.org/wiki/Suite_de_Fibonacci) est définie par l'équation de récurence :

<div>
$$
F(n) = F(n-1) + F(n-2)
$$
</div>

Si $n > 2$ et $F(1) = F(2) = 1$

Nous allons utiliser cette suite pour donner des techniques utiles pour l'étude d'algorithmes récursifs

### Fibonacci récursif

```python
def fibonacci_rec(n):
    if n < 3:
        return 1
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)
```

Cette partie vous donne le principe général lorsque l'on calcule des complexités d'algorithmes récursifs.

1. Donnez l'équation de récurrence permettant de calculer le nombre $A(n)$ d'appels à la fonction dans l'exécution de `fibonacci_rec(n)`. Montrer que cette valeur est égale à $F(n)$.
2. Donnez l'équation de récurrence permettant de calculer la complexité $C(n)$ de l'exécution de `ma_fonction(n)`.
3. Montrez que $\mathcal{O}(1) + 2\cdot C(n-2) \leq C(n) \leq \mathcal{O}(1) + 2\cdot C(n-1)$
4. En déduire que :
   1. $C(n) \leq \mathcal{O}(1)\cdot (\sum_{i=0}^{n-3}2^i) + 2^{n-2} \cdot C(2)$
   2. $C(n) \geq  \mathcal{O}(1)\cdot (\sum_{i=0}^{(n-4)/2}2^i) + {(\sqrt{2})}^{n-2} \cdot C(2)$
5. en conclure que :
   1. $C(n) =\mathcal{O}(2^n)$
   2. $C(n) =\Omega((\sqrt{2})^n)$

{% info %}
La valeur d'[une série géométrique](https://fr.wikipedia.org/wiki/S%C3%A9rie_g%C3%A9om%C3%A9trique) est à connaitre. On en a souvent besoin en algorithmie.
{% endinfo %}

### Valeur de $F(n)$

Montrez (par récurrence) que :

<div>
$$
F(n) = \frac{1}{\sqrt{5}}(\varphi^n+\frac{1}{\varphi^n})
$$
</div>

Où $\varphi = \frac{1+\sqrt{5}}{2}$ qui est le nombre d'or et une racine du polynôme $X^2 - X - 1$ (l'autre racine étant $-\frac{1}{\varphi}$)

{% info %}
C'est hors programme, mais c'est la façon de résoudre [les suite linéaires récurrentes](https://fr.wikipedia.org/wiki/Suite_r%C3%A9currente_lin%C3%A9aire)
{% endinfo %}

En déduire que le nombre d'appels de la fonction récursive de la partie précédente vaut : $A(n) = \Theta(\varphi^n)$

### Itératif

Donnez un algorithme it´ratif de complexité $\mathcal{O}(n)$ pour calculer $F(n)$

### Récursif terminal

L'algorithme récursif est sous-optimal car il recalcule plein de fois la même chose. Pour calculer $F(n)$ il calcule deux fois $F(n-2)$, une fois dans la somme et une fois dans le calcul de $F(n-1)$.

L'algorithme itératif ne fait pas la même chose car il stocke les valeurs intermédiaires. Une technique puissante pour accéder à la même chose récursivement est de passer les variables en paramètres :

Démontrer que :

- `fibo_rec_terminal(n, 1, 1)`{.language-} calcule bien $F(n)$ :
- sa complexité est $\mathcal{O}(n)$

```python
def fibo_rec2(n, a=1, b=1):
    if n <= 1:
        return b
    elif n <= 2:
        return a
    else:
        return fibo_rec2(n - 1, a + b, a)
```

## Noob trap

On considère le code suivant :

```python#
def f(n):
    if n < 2:
        return 1
    return f(n // 2) * f(n // 4)
```

Quelle est l'équation de récurrence de la complexité :

1. $C(n) = C(n/2) * c(n/4)$
2. $C(n) = \mathcal{O}(1) + C(n/2) * c(n/4)$
3. $C(n) = \mathcal{O}(1) + C(n/2) + c(n/4)$

Déduire de la bonne réponse que la complexité de l'exécution de la fonction est linéaire.

## Tour de Hanoï

Les _tours de Hanoï_ sont un célèbre casse tête inventé par Édouard Lucas qui consiste à déplacer $n$ disques de diamètres différents d'une tour de _"départ"_ à une tour d' _"arrivée"_ en passant par une tour _"intermédiaire"_, tout en respectant les règles suivantes :

- on ne peut déplacer qu'un disque à la fois
- on ne peut placer un disque sur un disque plus petit que lui.

On suppose que cette dernière règle est également respectée dans la configuration de départ.

Donnez un algorithme récursif permettant de résoudre le problème. Quelle est sa complexité ? Peut-on faire mieux ?

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

## Triangle de Pascal

Le calcul du coefficient binomial se fait en utilisant [le triangle de Pascal](https://fr.wikipedia.org/wiki/Triangle_de_Pascal).

Pour $n > p > 0$ :

<div>
$$
C(n, p) = C(n-1, p-1) + C(n-1, p)
$$
</div>

et $C(n, 1) = C(n, n) = 1$

On vous demande de créer un algorithme :

1. récursif pour calculer $C(n, p)$, et d'en donner la complexité.
2. itératif pour calculer $C(n, p)$ en utilisant une variable matricielle $M[i][j]$ qui stoque toutes les valeurs de $C(i, j)$ intermédiaires, et d'en donner la complexité en mémoire et en nombre d'opérations.
3. itératif avec une complexité en mémoire de $\mathcal{O}(n)$ en remarquant qu'il suffit de conserver une seule ligne de a matrice.

## Compteur binaire

En entier écrit sous forme binaire peut s'écrire comme une liste $x$ composées de 0 et de 1. Par exemple l'entier 19 s'écrira $[1, 0, 0, 1, 1]$

On vous demande d'écrire la fonction `succ(n)`{.language-} qui prend en paramètre un entier écrit sous sa forme binaire et qui **le modifie** pour que sa valeur soit l'entier suivant. On supposera que l'on n'augmente pas sa taille et donc que `succ([1, 1, 1, 1])`{.language-} change la liste ne entrée en `[0, 0, 0, 0]`{.language-}.

Cette fonction permet d'écrire le code suivant :

```python
n = [1, 0, 0, 1, 1]
succ(n)
print(n)
```

Qui affichera `[1, 0, 1, 0, 0]`{.language-}

{% info %}
Les fonctions qui ne rendent rien modifient souvent leurs paramètres.
{% endinfo %}

### L'algorithme

```python#
def successeur(n):
    i = len(n) - 1

    while (i >= 0) and (n[i] == 1):
        n[i] = 0
        i -= 1

    if i >= 0:
        n[i] = 1
```

Démontrez que l'algorithme précédent répond à la question.

### Complexités min et max

Que valent les complexités min et max de cet algorithme ?

### Complexité en moyenne

Analysez selon le nombre en entrée le nombre d'itérations dans la boucle while. En déduire que le nombre moyen d'itérations de la boucle while vaut :

<div>
$$
W_\text{moy}(N) = \mathcal{O}(1) \cdot \sum_{i=0}^{N-1} i \cdot \frac{1}{2^{i+1}}
$$
</div>

Conclure en utilisant le fait que $\sum_{i=1}^N i \cdot \frac{1}{2^{i+1}}$ tent vers 1 lorsque $N$ tend vers l'infini que l'algorithme va en moyenne ne faire qu'une seule itération et donc que la complexité en moyenne de l'algorithme vaut $\mathcal{O}(1)$.

### Vérification

Que le nombre moyen d'itération vale 1 est assez contre intuitif. Vérifiez expérimentalement qu'en moyenne, si l'on appelle successeur $2^N$ fois à partir de $[0] * N$ :

- on a bien cyclé sur tous les éléments
- en moyenne le nombre d'itération dans la boucle vaut bien 1.

## Cols

Le but de cet exercice est d'étudier les **_cols_** d'un tableau.

{% note "**Définition**" %}
Un **_col_** d'un tableau d'entiers $T$ de taille $n > 1$ est un indice $0 \leq i < n$ tel que :

- soit $i = 0$ et $T[i] \leq T[1]$
- soit $i = n-1$ et $T[i] \leq T[n-2]$
- soit $0 < i < n-1$ et $T[i] \leq \min(T[i-1], T[i+1])$
  {% endnote %}

### Existence

Montrer que tout tableau d'entiers $T$ de taille $n > 1$ contient au moins 1 col.

### Découverte

Donnez un algorithme nommé `trouve(T)`{.language-} permettant de trouver un col d'un tableau d'entiers $T$ de taille $n > 1$ passé en paramètre en $\mathcal{O}(n)$ opérations.

Vous expliciterez :

- que la complexité de votre algorithme est bien celle demandée,
- qu'il trouve bien un col.

### Rapidité

Démontrez que l'algorithme suivant permet de trouver un col d'un tableau d'entiers $T$ de taille $n > 1$ passé en paramètre.

```python#
def trouve_vite(T):
    if T[0] <= T[1]:
        return 0

    if T[-1] <= T[-2]:
        return len(T) - 1

    début = 0
    fin = len(T) - 1

    while True:
        milieu = (fin + début) // 2
        if T[milieu] <= min(T[milieu - 1], T[milieu + 1]):
            return milieu

        if T[milieu] > T[milieu - 1]:
            fin = milieu
        else:
            début = milieu

```

On a utilisé dans le code précédent le fait que :

- `T[-1]`{.language-} soit le dernier élément du tableau et `T[-2]`{.language-} l'avant dernier.
- `a // b`{.language-} rende la division entière de `a`{.language-} par `b`{.language-}

### Complexité

Donnez la complexité de l'algorithme `trouve_vite(T)`{.language-}.

### complexité du problème

Après avoir formalisé le problème de la recherche d'un col dans un tableau, vous démontrerez que sa complexité est égale à la complexité de l'algorithme `trouve_vite(T)`{.language-} de la question 3.
