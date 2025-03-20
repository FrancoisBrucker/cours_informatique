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

![opti A˜B](./opti-1.png)

Prenons une ville sur ce chemin, par exemple la ville C :

![opti A˜C˜B](./opti-2.png)

Alors :

- Le chemin le plus court entre la ville A et la ville C est le bout de chemin entre A et C sur le chemin le plus court entre A et B
- Le chemin le plus court entre la ville C et la ville B est le bout de chemin entre C et B sur le chemin le plus court entre A et B

En effet, s'il existait par exemple un chemin plus rapide entre A et C (le chemin rouge) :

![opti A-C˜B](./opti-3.png)

Il suffirait de passer par lui pour aller de A à C puis reprendre le chemin noir pour aller de C à B pour avoir un chemin encore plus rapide, ce qui est impossible par hypothèse.

Cet exemple est fondamental car c'est de lui qu'est né le principe de programmation dynamique par le mathématicien [Richard Bellman](https://fr.wikipedia.org/wiki/Richard_Bellman).

Il existe de nombreux cas d'applications de la programmation dynamique, beaucoup de problèmes pouvant s'écrire sous forme récursive, même s'ils ne sont pas initialement formulés ainsi. Ce n'est cependant une solution universelle car le nombre de sous-problèmes à considérer peut être énorme et donc ne pas donner d'avantage algorithmique clair par rapport à la solution _brut force_ (énumérer et analyser tous les cas possibles).

## Méthode de résolution

{% note "**Méthode**" %}

Pour résoudre un problème d'optimisation en utilisant la programmation dynamique se fait en 3 étapes :

1. **choix** des sous-problèmes
2. **détermination** de l'équation de récurrence liant les sous-problèmes entre eux
3. résolution de l'équation en **stockant** les résultats intermédiaires (très souvent les solutions optimales des sous-problèmes) pour éviter de les recalculer

{% endnote %}

Le gain algorithmique de l'utilisation de la programmation dynamique résulte dans le fait de stocker les résultats intermédiaires (les sous-problèmes optimaux) pour ne pas avoir à les recalculer. Cette approche est d'autant plus efficace que :

1. l'équation de récurrence est simple à calculer,
2. le nombre de sous-problèmes à stocker est faible.

Enfin, la programmation dynamique nous assure de trouver **un** chemin optimal. Ce n'est très souvent pas un problème car on est généralement intéressé par une solution et pas par toutes les solutions possibles, mais il faut en être contient.

## Stockage des résultats intermédiaires

Il existe deux approches pour le stockage des résultats intermédiaires : [**_l'approche bottom-up_**](https://fr.wikipedia.org/wiki/Approches_ascendante_et_descendante#Approche_ascendante) et la [**_mémoïsation_**](https://fr.wikipedia.org/wiki/M%C3%A9mo%C3%AFsation). Nous allons montrer les deux techniques en nous aidant de la suite de Fibonacci dont l'équation de récurrence est :

$$
F(n) = F(n-1) + F(n-2)
$$

L'algorithme récursif naïf calculant $F(n)$ est :

```pseudocode
algorithme F(n: entier) → entier:
    si n ≤ 2:
        rendre 1
    sinon:
        rendre F(n - 1) + F(n - 2)

```

Sa complexité est rédhibitoire (on l'a vu, elle est exponentielle).

### Approche bottom-up

La première optimisation possible est l'approche bottom-up, qui consiste à commencer par les conditions aux limites de la récurrence puis de remonter petit à petit l'équation de récurrence jusqu'à arriver au problème initial. C'est la méthode que l'on a utilisée pour les deux premiers exemples.

Pour la suite de Fibonacci cela donne :

```pseudocode
algorithme F(n: entier) → entier:
    a ← 1
    b ← 0
    
    pour chaque i de [0, n - 1[:
        a, b ← a + b, a
    
    rendre a
```

La complexité est maintenant linéaire et ne sont stockés que les éléments nécessaires à la résolution de la prochaine étape de l'équation de récurrence (la complexité spatiale est en $\mathcal{O}(1)$).

### Mémoïsation

La mémoïsation est le fait de stocker les résultats d'une fonction pour ne pas avoir à la rappeler plus tard et utiliser directement le résultat. C'est ce qui est mis en oeuvre dans les techniques de cache comme [le cache web](https://fr.wikipedia.org/wiki/Cache_web) ou encore [la mémoire cache](https://fr.wikipedia.org/wiki/M%C3%A9moire_cache).

C'est très utile si on a une équation de récurrence compliquée ou qu'on ne contrôle pas ce que l'on cherche.

La mémoïsation est un principe fondamental en algorithmie qui permet d'échanger de la complexité temporelle (nombre d'instructions) en complexité spatiale : on échange du temps par de l'espace. Ce n'est pas toujours un échange profitable, savoir s'il faut utiliser la programmation dynamique se fait donc au cas par cas.

Pour le calcul de la suite de Fibonacci, cela donne si $n$ est plus petit que $N$ :

```pseudocode
cache ← un tableau d'entiers de taille N
cache[:] ← -1

algorithme F(n: entier) → entier:
    si cache[n] ≠ -1:
        rendre cache[n]

    si n ≤ 2:
        f ← 1
    else:
        f ← F(n - 1) + F(n - 2)

    cache[n] ← f
    rendre f
```

Le fait que $F(n - 2)$ ne soit appelé qu'une fois que $F(n - 1)$ l'ait été, fait que son résultat a été mémoïsé puisqu'il a fallu le calculer lors de l'appel de $F(n - 1)$.

Il n'y a donc que $n$ appels récursifs, le second élément ayant été mémoïsé :

- la complexité est en $\mathcal{O}(n)$
- la complexité spatiale est en $\mathcal{O}(N)$ (le tableau de mémoïsation)

Notez qu'il faut initialiser le cache et donc avoir une opération préalable de complexité $\mathcal{O}(N)$ pour initialiser le tableau de cache.

## Exemples

### Sous-suite croissante maximum

{% lien %}
[Problème de la sous-suite croissante maximum](https://fr.wikipedia.org/wiki/Plus_longue_sous-suite_strictement_croissante)
{% endlien %}

Le problème est le suivant :

{% note "**Problème**" %}
Soit $T$ un tableau à $n$ éléments. On cherche la longueur de la suite ${(s\_i)}\_{i\geq 0}$ la plus grande possible telle que $T[s_i] < T[s_{i+1}]$ pour tout $i$.
{% endnote %}

En reprenant l'exemple de Wikipedia la suite $(6, 1, 4, 9, 5, 11)$ possède plusieurs sous-suites croissantes, comme $(6, 9, 11)$, $(1, 4, 9, 11)$ ou encore $(1,4, 5, 11)$. Les plus longues sous-suites étant de longueur 4.

Nous allons résoudre ce problème par programmation dynamique en définissant $N[i]$ comme étant la longueur maximale de la suite pour le tableau $T[i:]$ (on a supprimé les $i$ premiers éléments de $T$. Le tableau $T[0:]$ est le tableau initial et $T[2:]$ est le tableau auquel on a supprimé les deux premiers éléments).

{% exercice %}
Si $n$ est la taille de $T$, montrez que :

- $N[i] \geq 1$ pour tout $0\leq i < n$
- $N[n-1] = 1$

{% endexercice %}
{% details "corrigé" %}

Clair.

{% enddetails %}

Les constatations préliminaires précédentes permettent de trouver une relation de récurrence entre les $N[i]$ :

{% exercice %}
Déterminez une relation de récurrence entre $N[i]$ et les $N[j]$ pour les $j>i$ tels que $T[i] < T[j]$.
{% endexercice %}
{% details "corrigé" %}

<div>
$$
N[i] = 1 + \max(\{0, \max(\{ N[j] \mid j>i, T[j] > T[i]\}) \})
$$
</div>

{% enddetails %}

La relation de récurrence précédente permet de créer des algorithmes de résolution. Vous allez en créer deux :

{% exercice %}
Proposez un algorithme récursif et utilisant la mémoïsation pour résoudre le problème.
{% endexercice %}
{% details "corrigé" %}

Pour une taille de tableau plus petite que $N$, on a :

```python
cache = [None] * N

def sous_suite(T, i):
    if cache[i] != None:
        return cache[i]

    if i >= len(T) -1:
        v = 1
    else:
        v = 1 + max(0,
                     max([sous_suite(T, j) for j in range(i + 1, len(T)) if T[j] > T[i]]))

    cache[i] = v
    return v

print(sous_suite(T, 0))
```

Tout comme pour la mémoïsation de la suite de Fibonacci, on ne calcule `sous_suite(T, i)`{.language-} qu'une seule fois.
Chaque calcul peut demander le calcul de tous les `sous_suite(T, j)`{.language-}, pour tous les $j>i$, donc une complexité de $\mathcal{O}(n)$ lorsque tous les résultats seront dans le cache. La complexité totale de `sous_suite(T, 0)`{.language-} est donc de $\mathcal{O}(n^2)$.

{% enddetails %}

{% exercice %}
Proposez un algorithme itératif et bottom-up pour résoudre le problème.
{% endexercice %}
{% details "corrigé" %}
Il faut partir de ce que l'on connaît, $N[n-1]$, puis redescendre itérativement vers $N[0]$.

```python
def sous_suite(T):
    N = [1] * len(T)

    for i in range(len(T) - 2, -1, -1):
        N[i] = 1 + max(0,
                        max([N[j] for j in range(i + 1, len(T)) if T[j] > T[i]]))

    return N[0]

print(sous_suite(T))
```

La complexité est clairement en $\mathcal{O}(n^2)$.

{% enddetails %}

### Découpage d'un câble

{% lien %}
[Découper un cable](https://www.youtube.com/watch?v=tufup6HlwWg)
{% endlien %}

Ce problème est un classique de la programmation dynamique. Il apparaît de manière détournée dans nombre d'autre problème, il est donc bon de connaître et le problème et sa résolution.

On suppose que l'on possède un câble de $n$ mètres que l'on revendre par bouts. Pour cela on dispose d'un tableau $P$ de taille $n+1$ indiquant en $P[k]$ le prix de vendre d'une longueur de $0\leq k \leq n$ mètres de notre câble (si on ne peut pas vendre de cable de longueur $k$, on aura $P[k] = 0$).

La question est de trouver un tableau $V$ de $n+1$ entiers tel que :

- $\sum V[i] \leq n$
- $M_n = \sum (V[i] \cdot P[i])$ soit maximum parmi tous les tableaux $V'$ de taille $n+1$ tels que $\sum V'[i] \leq n$.

Ce tableau représente le prix maximum que l'on peut tirer de la vente de notre cable en $V[i]$ bouts de longueur $i$ pour $0\leq i \leq n$.

{% exercice %}
Exprimez $M_n$ en fonction de $M_m$ avec $m\leq n$.
{% endexercice %}
{% details "corrigé" %}
On pose $M_0 = 0$ et pour $n > 0$ :

<div>
$$
M_n = \max(\\{ M_m + P[n-m] \vert 0 \leq m < n \\})
$$
</div>

{% enddetails %}
{% exercice %}
En déduire un algorithme en $\mathcal{O}(n^2)$ utilisant la programmation dynamique permettant de calculer $M_n$.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme vente(n → entier, P → [entier]) → entier:
    M ← un tableau d'entiers de taille n + 1
    M[0] ← 0

    pour chaque m de [1, n]:
        M[m] ← 0
        pour chaque k de [0, m[:
            si M[m] < M[k] + P[m-k]:
                 M[m] ← M[k] + P[m-k]

    rendre M[n]
```

{% enddetails %}

{% exercice %}
Modifiez l'algorithme précédent pour qu'il rende $V[i]$. Assurez-vous que cet algorithme soit bien de complexité $\mathcal{O}(n^2)$ en temps et $\mathcal{O}(n)$ en espace.
{% endexercice %}
{% details "corrigé" %}

On ajoute un tableau, `D` qui va stocker le découpage idéal $n-k$ tel que $M_n = M_k + P[n-k]$. Puis on utilise les valeurs de `D` pour créer `V`.

```pseudocode
algorithme vente(n → entier, P → [entier]) → [entier]:
    M ← un tableau d'entiers de taille n + 1
    M[0] ← 0
    D ← un tableau d'entiers de taille n + 1
    D[0] ← 0

    pour chaque m de [1, n]:
        M[m] ← 0
        D[0] ← 0
        pour chaque k de [0, m[:
            si M[m] < M[k] + P[m-k]:
                 M[m] ← M[k] + P[m-k]
                 D[0] ← m - k

    V ← un tableau d'entiers de taille n + 1
    V[:] ← 0

    pour chaque m de [0, n]:
        V[D[m]] ← V[D[m]] + 1 
    
    rendre V
```

{% enddetails %}

### Déplacement optimaux

> TBD touriste à Manhattan 7. <https://www.mathly.fr/prog_dyn.pdf>

### Fiabilité maximale

Un système complexe est composé de $n$. Chaque composant à un coût $c_i$ et une probabilité de panne valant $p_i$.

On cherche à obtenir le système le plus fiable possible, pour un coût total inférieur à $C$, en dupliquant les composants si nécessaire. Le $i$ composant étant en panne que si ses $n_i$ duplications sont en panne.

{% exercice %}
Quelle est la probabilité que les $n_i$ duplications du composant $i$ soient en panne ?
{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}
{% exercice %}
En déduire la probabilité de panne du système total.
{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}

{% exercice %}
Trouver le nombre de duplications nécessaires pour chaque composant afin de créer un système de fiabilité maximale à un coût inférieur à $C$.
{% endexercice %}
{% details "corrigé" %}

> TBD

{% enddetails %}
