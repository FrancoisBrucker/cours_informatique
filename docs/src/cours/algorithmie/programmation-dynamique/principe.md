---
layout: layout/post.njk

title: Principe

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


{% lien %}
[Page Wikipedia sur la programmation dynamique](https://fr.wikipedia.org/wiki/Programmation_dynamique)
{% endlien %}

Le principe de la programmation dynamique est simple :

{% note "**Principe**" %}
Une solution optimale à un problème est constituée de solutions optimales de sous-problèmes.
{% endnote  %}

Il s'applique aux problèmes d'optimisations et en particulier ceux que l'on peut écrire sous une forme récursive. Illustrons le avec la recherche de chemins le plus rapide. Supposons que le chemin le plus rapide entre la ville A et la ville B soit celui ci-dessous :

![opti A˜B](../opti-1.png)

Prenons une ville sur ce chemin, par exemple la ville C :

![opti A˜C˜B](../opti-2.png)

Alors :

- Le chemin le plus court entre la ville A et la ville C est le bout de chemin entre A et C sur le chemin le plus court entre A et B
- Le chemin le plus court entre la ville C et la ville B est le bout de chemin entre C et B sur le chemin le plus court entre A et B

En effet, s'il existait par exemple un chemin plus rapide entre A et C (le chemin rouge) :


![opti A-C˜B](../opti-3.png)

Il suffirait de passer par lui pour aller de A à C puis reprendre le chemin noir pour aller de C à B pour avoir un chemin encore plus rapide, ce qui est impossible par hypothèse.

Cet exemple est fondamental car c'est de lui qu'est né le principe de programmation dynamique par le mathématicien [Richard Bellman](https://fr.wikipedia.org/wiki/Richard_Bellman). C'est ce que nous allons tout de suite découvrir.

## Premier exemple : chemin le plus rapide

Il existe de nombreux algorithmes permettant de trouver un chemin optimal entre deux données (le plus rapide, le moins cher, ...). Nous allons ici utiliser comme données un réseau ferré et utiliser la méthode utilisée par Bellman lui-même et qui à donné le nom à la méthode générale.

Cet algorithme, appelé [_"algorithme de Bellman-Ford"_](https://fr.wikipedia.org/wiki/Algorithme_de_Bellman-Ford), est un algorithme très général de théorie des graphes. Nous allons en voir ici une version simplifiée dont le but est de vous faire sentir le principe général de la programmation dynamique et surtout comment l'utiliser comme un principe de résolution de problème.

### Données

On va utiliser un réseau ferré comme données. Il est constitué d'une liste de tronçons reliant deux gares, et chaque tronçon ne contient pas de gares intermédiaires. Aller d'une gare à une autre revient  à suivre une suite de tronçons.

### Méthode de résolution

Le principe de la programmation dynamique stipule que tout chemin optimal est constitué de sous-chemins eux aussi optimaux pour des sous-problèmes. La principale difficulté lorsque l'on cherche à modéliser un algorithme utilisant la programmation dynamique pour résoudre un problème est de déterminer ce que sont ces sous-problèmes.

#### Détermination des sous-problèmes

Dans le cas des chemins ferrés, on classer les chemins par rapport au nombre de leurs tronçons et là, un chemin optimal de $k$ tronçons entre la gare $A$ et la gare $B$ est constitué :

- d'un chemin optimal de $k-1$ tronçons de la gare $A$ à une gare $C$
- du tronçon entre la gare $C$ et la gare $B$

Si l'on connait les chemins optimaux de longueurs $k-1$ entre $A$ et toutes les autres gare $C$ on peut créer un chemin optimal entre $A$ et $B$ de $k$ tronçons.

On a alors l'équation de récurrence suivante :

<div>
$$
T_k(x, y) = \min (\{ T_{k-1}(x, y), \min (\{T_{k-1}(x, z) + T_1(z, y) \mid z \in G \}\}))
$$
</div>

Avec :

- $G$ l'ensemble des gares
- $T_1(u, v)$ valant soit le temps de parcourt pour le tronçon allant de $u$ à  $v$, soit $+\infty$ si le tronçon entre $u$ et $v$ n'existe pas.


Le temps minimum entre deux gares $x$ et $y$ est donné par $T_{|G|}(x, y)$.

**Attention**, il est bien nécessaire d'aller jusqu'à  $T_{|G|}(x, y)$, on ne peut pas s'arrêter dès que l'on atteint la gare d'arrivée (_ie._ le temps devient fini) :

- $T_1(A, B) = 10$
- $T_1(A, C) = 1$
- $T_1(C, B) = 1$

Et on a $T_2(A, B) = 2 < T_1(A, B) = 10$.

#### Stockage des solutions intermédiaires

La partie précédente nous a permis de dégager une équation de récurrence permettant de lier des sous-problèmes entre eux. Pour éviter d'avoir sans cesse à recalculer ces solutions il faut les stocker.

Dans le cas de notre problème l'équation de récurrence montre que pour trouver un chemin optimal à $k$ tronçons entre deux gare il faut connaitre tous les chemins optimaux à $k-1$ tronçons entre la gare de départ et toutes les autres gare.

#### Algorithme final

On suppose que :

- l'on associe à chaque gare un numéro allant de $0$ à $n-1$ ($|G| = n$), ce qui nous permet de stocker les temps intermédiaires dans un tableau $T$.
- les tronçons sont stockés dans une matrice symétrique valant le temps entre la gare $i$ et $j$ si le tronçon existe et $+\infty$ sinon


```python
from math import inf

def bellman(tronçons, n, gare_départ, gare_arrivée):
    T = [inf] * n

    for g in range(n):
        T[g] = tronçons[gare_départ][g]

    for k in range(n):
        T[g] = min(T[g], 
                   min([T[x] + tronçons[x][g] for x in range(n)])

    return T[gare_arrivée] 
```

{% info %}
On a utilisé [`inf`{.language-} qui représente l'infini](https://docs.python.org/fr/3/library/math.html#math.inf)
{% endinfo %}

## Méthode de résolution

{% note "**Méthode**" %}

Pour résoudre un problème d'optimisation en utilisant la programmation dynamique se fait en 3 étapes :

1. **choix** des sous-problèmes
2. **détermination ** de l'équation de récurrence liant les sous-problèmes entre eux
3. résolution de l'équation en **stockant** les résultats intermédiaires (très souvent les solutions optimales des sous-problèmes) pour éviter de les recalculer

{% endnote %}

Le gain algorithmique de l'utilisation de la programmation dynamique résulte dans le fait de stocker les résultats intermédiaires (les sous-problèmes optimaux) pour ne pas avoir à les recalculer. Cette approche est d'autant plus efficace que : 

1. l'équation de récurrence est simple à calculer,
2. le nombre de sous-problèmes à stocker est faible.

Enfin, la programmation dynamique nous assure de trouver **un** chemin optimal. Ce n'est très souvent pas un problème car on est généralement intéressé par une solution et pas par toutes les solutions possibles, mais il faut en être contient.

## Stockage des résultats intermédiaires

Il existe deux approches pour le stockage des résultats intermédiaires : [***l'approche bottom-up***](https://fr.wikipedia.org/wiki/Approches_ascendante_et_descendante#Approche_ascendante) et la [***mémoïsation***](https://fr.wikipedia.org/wiki/M%C3%A9mo%C3%AFsation). Nous allons montrer les deux techniques en nous aidant de la suite de Fibonacci dont l'équation de récurrence est :

$$
F(n) = F(n-1) + F(n-2)
$$

L'algorithme récursif naïf calculant $F(n)$ est :

```python
def F(n):
    if n <= 2:
        return 1
    else:
        return F(n - 1) + F(n - 2)

```

Sa complexité est rédhibitoire (on l'a vu, elle est exponentielle).

### Approche bottom-up

La première optimisation possible est l'approche bottom-up, qui consiste à commencer par les conditions aux limites de la récurrence puis de remonter petit à petit l'équation de récurrence jusqu'à arriver au problème initial.

Pour la suite de Fibonacci cela donne :

```python
def F(n):
    a = 1
    b = 0
    for i in range(n - 1):
        a, b = a + b, a
    return a
```

La complexité est maintenant linéaire et ne sont stockés que les éléments nécessaires à la résolution de la prochaine étape de l'équation de récurrence (la complexité spatiale est en $\mathcal{O}(1)$).

### Mémoïsation

La mémoïsation est le fait de stocker les résultats d'une fonction pour ne pas avoir à la rappeler plus tard et utiliser directement le résultat. C'est ce qui est mis en oeuvre dans les techniques de cache comme [le cache web](https://fr.wikipedia.org/wiki/Cache_web) ou encore [la mémoire cache](https://fr.wikipedia.org/wiki/M%C3%A9moire_cache).

C'est très utile si on a une équation de récurrence compliquée ou qu'on ne contrôle pas ce que l'on cherche.

La mémoïsation est un principe fondamental en algorithmie qui permet d'échanger de la complexité en nombre d'instruction par de la complexité spatiale : on échange du temps par de l'espace. Ce n'est pas toujours un échange profitable, savoir s'il faut utiliser la programmation dynamique se fait donc au cas par cas.

Pour le calcul de la suite de Fibonacci, cela donne si $n$ est plus petit que $N$ :

```python
cache = [None] * N

def F(n):
    if cache[n] != None:
        return cache[n]

    if n <= 2:
        f = 1
    else:  
        f = F(n - 1) + F(n - 2)

    cache[n] = f
    return f
```

Le fait que $F(n - 2)$ ne soit appelé qu'une fois que $F(n - 1)$ le soit, fait que son résultat a été mémoïsé puisqu'il a fallu le calculer lors de l'appel de $F(n - 1)$.

Il n'y a donc que $n$ appels récursifs, le second élément ayant été mémoïsé :

- la complexité est en $\mathcal{O}(n)$ 
- la complexité spatiale est également en $\mathcal{O}(n)$ (le tableau de mémoïsation)

## Exemples classiques

Il existe de nombreux cas d'applications de la programmation dynamique, beaucoup de problèmes pouvant s'écrire sous forme récursive, même s'ils ne sont pas initialement formulé ainsi. Ce n'est cependant une solution universelle car le nombre de sous-problèmes à considérer peut être énorme et donc ne pas donner d'avantage algorithmique clair par rapport à la solution brut force.

> TBD : <http://www-desir.lip6.fr/~spanjaard/pmwiki/uploads/ProgrammationDynamique.pdf>
> TBD : voyageur de commerce + sac à dos : <https://scheid.perso.math.cnrs.fr/Enseignement/GRO/pdyn.pdf>

### Sous-suite croissantes max

> TBD

### Carré vides maximaux

> TBD

