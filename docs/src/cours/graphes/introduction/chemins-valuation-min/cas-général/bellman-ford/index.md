---
layout: layout/post.njk

title: Bellman-ford

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


## Premier exemple : chemin le plus rapide à partir d'une ville

Il existe de nombreux algorithmes permettant de trouver un chemin optimal entre deux données (le plus rapide, le moins cher, ...). Nous allons ici utiliser comme données un réseau ferré et utiliser la méthode introduite par Bellman lui-même et qui à donné le nom à l'algorithme.

Cet algorithme, appelé [_"algorithme de Bellman-Ford"_](https://fr.wikipedia.org/wiki/Algorithme_de_Bellman-Ford), est un algorithme très général de théorie des graphes. Nous allons en voir ici une version simplifiée dont le but est de vous faire sentir le principe général de la programmation dynamique et surtout comment l'utiliser comme un principe de résolution de problème.

### <span id="données"></span>Données

On va utiliser un réseau ferré comme donnée. Il est constitué d'une liste de tronçons reliant deux gares, chaque tronçon ne contenant aucune gare de passage.

{% note "**Définition**" %}

Un **_tronçon_** entre deux gares $x$ et $y$ est une ligne de rails connectant directement les deux gares, sans gare intermédiaire.

Pour un ensemble de gares $G$, on note $T$ la relation telle que :

- $T[x][y]$ est le temps pour relier la gare $x$ à la gare $y$ s'il existe un tronçon entre elles,
- $T[x][y]$ vaut $+\infty$ s'il n'existe pas de tronçon entre la gare $x$ et la gare $y$,
- $T[x][x]$ vaut 0 pour toute gare $x$
{% endnote %}

Aller d'une gare à une autre revient à suivre une suite de tronçons. Formalisons ceci :

{% note "**Définition**" %}

Un **_chemin_** entre deux gares $x$ et $y$ est soit :

- le **_tronçon_** entre $x$ et $y$
- soit une suite $g_1\dots g_{i-1}g_i\dots g_n$ telle que :
  - $g_1 = x$, $g_n = y$
  - les gares $g_{i-1}$ et $g_{i}$ sont différentes et reliées par un tronçon pour tout $1 < i \leq n$
  - pour un chemin $g_1\dots g_{i-1}g_i\dots g_n$ entre $g_1$ et $g_n$, les gares $g_2$ à $g_{n-1}$ sont dites **_gares de passage_**

{% endnote %}

### Problème à résoudre

On cherche à connaitre le temps minimal de trajet $M[x]$ entre une gare $A$ (donnée) et chaque autre gare $x$.

### Méthode de résolution

Le principe de la programmation dynamique stipule que tout chemin optimal est constitué de sous-chemins eux mêmes optimaux. La principale difficulté lorsque l'on cherche à modéliser un algorithme utilisant la programmation dynamique pour résoudre un problème est de déterminer ce que sont ces sous-problèmes.

#### Détermination des sous-problèmes

Dans le cas des chemins ferrés, on peut classer les chemins partant de $A$ par rapport à leur nombre de tronçons. De là un chemin optimal d'au plus $k$ tronçons entre la gare $A$ et une gare $x$ est constitué :

1. d'un chemin optimal d'au plus $k-1$ tronçons de la gare $A$ à une gare $y$
2. du tronçon entre la gare $y$ et la gare $x$

Si l'on connait les chemins optimaux ayant au plus $k-1$ tronçons entre $A$ et toutes les autres gares $y$ on peut créer un chemin optimal entre $A$ et $x$ d'au plus $k$ tronçons en ajontant le tronçon entre $A$ et $x$.

On a alors l'équation de récurrence suivante :

<div>
$$
M_k[x] = \min (\{ M_{k-1}[x], \min (\{M_{k-1}[y] + T[y][x] \mid y \in G \}\}))
$$
</div>

Avec :

- $G$ l'ensemble des gares
- $T[u][v]$ valant soit le temps de parcourt du tronçon allant de $u$ à $v$, soit $+\infty$ si le tronçon n'existe pas
- $M_k[u]$ le temps minimum d'un chemin entre $A$ et $u$ en au plus $k$ tronçons

Le temps de trajet minimum entre les deux gares $A$ et $x$ est donné par $M[x] = M_{|G|-1}[x]$.

**Attention**, il est bien nécessaire d'aller jusqu'à $M_{|G| - 1}[x]$, on ne peut pas s'arrêter dès que l'on atteint la gare d'arrivée (_ie._ dès que le temps devient fini) :

- $T[A][b] = 10$
- $T[A][c] = 1$
- $T[c][b] = 1$

Et on a $M_2[b] = 2 < T[A][b] = 10$.

#### Exemple

On considère les tronçons suivants :

![tronçons](./tronçons.png)

Ce qui donne la suite de liste suivante :

k | A | b | c | d | e | f | g 
==|===|===|===|===|===|===|===
0 | 0 |   |   |   |   |   |  
1 | 0 | 2 | 1 |   |   |   |   
2 | 0 | 2 | 1 | 11| 7 |   |
3 | 0 | 2 | 1 | 10| 7 |   | 8
4 | 0 | 2 | 1 | 10| 7 | 9 | 8
5 | 0 | 2 | 1 | 10| 7 | 9 | 8

Pour revenir en arrière et retrouver le chemin, on peu stocker le tronçon qui a rendu le chemin minimum (on a choisi ici plus petit ou égal. On privilégie les chemins minimaux les pus long) :


k | A | b | c | d | e | f | g 
==|===|===|===|===|===|===|===
0 | A |   |   |   |   |   |  
1 | A | A | A |   |   |   |   
2 | A | A | A | c | c |   |
3 | A | A | A | e | c |   | e
4 | A | A | A | e | c | g | e
5 | A | A | A |*f*| c | g | e

On peut ensuite _remonter_ pour retrouver le chemin. Pour aller de Q à d on est passé en sens inverse par d, f, g, e, c, A.

#### Stockage des solutions intermédiaires

La partie précédente nous a permis de dégager une équation de récurrence permettant de lier des sous-problèmes entre eux. Pour éviter d'avoir sans cesse à recalculer ces solutions il faut les stocker.

Dans le cas de notre problème l'équation de récurrence montre que pour trouver un chemin optimal à au plus $k$ tronçons entre deux gares il faut connaitre tous les chemins optimaux à au plus $k-1$ tronçons entre la gare de départ et toutes les autres gares. On n'a pas besoin de tout conserver, juste les valeurs précédentes suffisent.

#### Algorithme final

On suppose que :

- l'on associe à chaque gare un numéro allant de $0$ à $n-1$ ($|G| = n$), ce qui nous permet de stocker les temps intermédiaires dans un tableau $M$.
- les tronçons sont stockés dans une matrice $T$ telle que $T[i][j]$ vaut le temps  de trajet pour aller de la gare $i$ à la gare $j$ si le tronçon existe et $+\infty$ sinon

```python
from math import inf

def bellman(tronçons, n, gare_départ):
    M = [inf] * n
    M[gare_départ] = 0

    for k in range(n - 1):
        M2 = [inf] * n

        for g in range(n):
            M2[g] = min(M[g], min([M[x] + tronçons[x][g] for x in range(n)])
        M = M2

    return M
```

L'algorithme rend le tableau de temps intermédiaires qui contient le temps minimal entre la ville de départ et une gare $x$ quelconque. S'il n'existe pas de chemins entre la gare de départ et une gare $x$, alors $C[x]$ vaut $+\infty$.

{% info %}

- On a utilisé [`inf`{.language-} qui représente l'infini](https://docs.python.org/fr/3/library/math.html#math.inf)
- l'utilisation de $D$ permet d'éviter les effets de bord

{% endinfo %}

La complexité de cet algorithme est clairement en $\mathcal{O}(n^3)$ avec $n$ le nombre de gares.


## <span id="relation-C"></span>Deuxième exemple : existence de route entre deux villes quelconques

En reprenant les données du premier exemple, la liste de tronçons pour un ensemble de gares, on se pose la question de savoir s'il existe un chemin entre deux gares quelconques. On aimerait avoir une relation $C$ nous permettant de savoir si l'on peut voyager de la gare $x$ à la gare $y$ :

{% note "**Définition**" %}
Pour un ensemble de gares $G$, on note $C$ **_la relation chemin_**  telle que :

- $C[x][y]$ est **vrai** s'il existe un chemin entre les gares $x$ et $y$
- $C[x][y]$ est **faux** s'il n'existe pas de chemin entre les gares $x$ et $y$
- $C[x][x]$ est **vrai** pour toute gare $x$

{% endnote %}

Le premier exemple montre que la programmation dynamique permet de trouver le temps de chemin optimal entre une gare et toutes les autres en $\mathcal{O}(n^3)$ opérations. On peut alors résoudre notre problème en effectuant l'algorithme du premier exemple pour chaque gare $x$ et dire que $C[x][y]$ si et seulement si le temps minimum de trajet entre $x$ et $y$ est fini. Ceci nous prendrait en tout $\mathcal{O}(n^4)$ opérations.

Il est possible de faire mieux, encore une fois en utilisant la programmation dynamique, mais en changeant les sous-problèmes considérés. Ceci montre que les sous-problèmes que l'on peut considérer sont multiples, et peuvent conduire à complexités différentes. 

La notion de chemin s'écrit très bien sous la forme d'une relation $C$ car elle est :

- réflexive: pour tout $x$, on a $C[x][x]$ (le singleton $x$ permet de relier $x$ à lui-même)
- transitive: pour tout $x, y, z$, on a $C[x][y]$ et $C[y][z]$ implique $C[x][z]$ (on colle le chemin allant de $x$ à $y$ au chemin allant de $y$ à $z$)

L'intérêt de cette formalisation est qu'elle montre que la relation des chemins $C$ se crée :

1. en considérant la relation $T$ des tronçons ($C[x][y]$ s'il existe un tronçon entre les gares $x$ et $y$)
2. en fermant cette relation par transitivité

À première vue créer $C$ à partir de $T$ semble compliqué, mais l'exercice ci-après (qui explicite l'algorithme de [Algorithme de Roy](https://fr.wikipedia.org/wiki/Algorithme_de_Warshall)) montre qu'on peut le faire très simplement :

{% exercice %}
Soit $G = \\{ g_1, \dots g_n \\}$ les gares d'un réseau ferré et $T$ sa relation tronçon.

Montrez que si on note $G_i = \\{ g_1, \dots g_i \\}$, un chemin entre les gares $x$ et $y$ ayant comme gares de passage uniquement des éléments de $G_{i}$ peut se déduire de chemins ayant uniquement des gares de $G_{i-1}$ comme gares de passage.
{% endexercice %}
{% details "corrigé" %}
Il existe un chemin entre $x$ et $y$ ayant comme gares de passage uniquement des éléments de $G_{i}$ si :

- soit il existe un chemin entre $x$ et $y$ ayant comme gares de passage uniquement des éléments de $G_{i-1}$
- soit il existe les deux chemins suivants :
  - un chemin entre $x$ et $g_i$ ayant comme gares de passage uniquement des éléments de $G_{i-1}$
  - un chemin entre $g_i$ et $y$ ayant comme gares de passage uniquement des éléments de $G_{i-1}$

{% enddetails %}

Ici, le sous problème revient à restreindre le nombre de gares possible ! On a plus d'équation récurrente, mais un lien entre les chemins ne passant que par les éléments de $G_{i-1}$ et ceux passant passant par $G_{i}$. On peut ainsi reprendre la méthode de résolution du premier exemple :

{% exercice %}
Déduire un algorithme utilisant la programmation dynamique en $\mathcal{O}(n^3)$ permettant de trouver la relation chemin à partir de la relation tronçon.
{% endexercice %}
{% details "corrigé" %}

En notant $C_k[i][j]$ la relation telle que les gares $i$ et $j$ sont reliées par un chemins de gares de passage plus petites ou égale à $k$, $C_k[i][j]$ est vrai si l'une ou l'autre des assertions suivantes est vrai :

- $C_{k-1}[i][j]$ est vrai
- $C_{k-1}[i][k]$ et $C_{k-1}[k][j]$ sont vrais

Qui se résume en :

$$
C_k[i][j] = C_{k-1}[i][j] \text{ OU } (C_{k-1}[i][k] \text{ ET } C_{k-1}[k][j])
$$

Ce qui donne l'algorithme :

```python
for i in range(n):
    for j in range(n):
        C[i][j] = (T[i][j] != inf)

for k in range(n):
    D = [[False for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            D[i][j] = C[i][j] or (C[i][k] and C[k][j])
    C = D

return C
```

Notez que comme il ne peut pas y avoir d'effets de bord (une fois que la valeur est vraie, elle ne bouge plus), on peut se passer de la matrice $D$ et écrire l'algorithme :


```python
for i in range(n):
    for j in range(n):
        C[i][j] = (T[i][j] != inf)

for k in range(n):
    for i in range(n):
        for j in range(n):
            C[i][j] = C[i][j] or (C[i][k] and C[k][j])

return C
```
{% enddetails %}

Vous aurez certainement remarqué qu'on peut le faire, mais explicitez le :


{% exercice %}
Modifiez l'algorithme précédent pour remplacer la création de la matrice $C$ par la matrice $M[i][j]$ qui donne, comme pour le premier exemple) le temps minimum du chemin entre la gare $i$ et la gare $j$.
{% endexercice %}
{% details "corrigé" %}

Le temps de trajet minimum entre deux gares $x$ et $y$  ayant comme gares de passage uniquement des éléments de $G_{i}$ est :

- soit le temps de trajet minimum entre $x$ et $y$ ayant comme gares de passage uniquement des éléments de $G_{i-1}$
- soit la somme des temps de trajet minimum entre :
  - $x$ et $g_i$ ayant comme gares de passage uniquement des éléments de $G_{i-1}$
  - $g_i$ et $y$ ayant comme gares de passage uniquement des éléments de $G_{i-1}$

On peut donc écrire l'algorithme :

```python
from math import inf

for i in range(n):
    for j in range(n):
        M[i][j] = T[i][j]

for k in range(n):
    M2 = [[inf for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            M2[i][j] = min([M[i][j], M[i][k] + M[k][j]])
    M = M2

return M
```

De même que pour l'exercice précédent, il ne peut y avoir d'effet de bord, les temps de chemins ne faisant que diminuer, on peut se passer de la matrice $M2$ et écrire l'algorithme sous la forme :


```python
from math import inf

for i in range(n):
    for j in range(n):
        M[i][j] = T[i][j]

for k in range(n):
    for i in range(n):
        for j in range(n):
            M[i][j] = min([M[i][j], M[i][k] + M[k][j]])

return M
```
{% enddetails %}
{% info %}
Tout comme l'algorithme de Bellman-Ford, on peut On facilement modifier l'algorithme précédent pour qu'il conserve le chemin permettant de réaliser le temps de trajet minium.
{% endinfo %}

L'algorithme de la question précédente est de même complexité que celui du premier exemple et résout un problème plus général ! Il est connu sous le nom d'algorithme de [Roy-Floyd-Warshall](https://fr.wikipedia.org/wiki/Algorithme_de_Floyd-Warshall). Mais se pose alors la question : 


{% exercice %}
Quel est l'intérêt de l'algorithme du premier exemple (algorithme de Bellman-Ford) par rapport au second (algorithme de Roy-Floyd-Warshall) ?
{% endexercice %}
{% details "corrigé" %}
Les complexités temporelles sont les mêmes mais pas la complexité spatiale. Le second algorithme doit conserver toute une matrice de chemins, alors que le premier ne conserve qu'une ligne, celle concernant la gare de départ.
{% enddetails %}