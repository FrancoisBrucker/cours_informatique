---
layout: layout/post.njk 
title: Complexité amortie

eleventyNavigation:
  key: "Complexité amortie"
  parent: Algorithme
---

{% prerequis "**Prérequis** :" %}

* [Complexité max/min](../complexité-max-min)

{% endprerequis %}

<!-- début résumé -->

Définition, utilité et utilisation de la complexité amortie d'un algorithme.

<!-- end résumé -->

Si lors de l'exécution d'un algorithme $A$, une opération $O$ (ou une fonction) de celui-ci se répète plusieurs fois et que sa
complexité diffère selon les appels, le calcul de la complexité de $A$ va nécessiter une analyse fine de de **toutes** les exécutions de l'opération $O$ car borner la complexité par le maximum conduit (souvent) à surestimer grandement la complexité réelle.

{% note "**Définition :**" %}
L'***analyse amortie*** est regroupe un ensemble des techniques permettant de calculer globalement la complexité maximale $C$ de $m$ exécutions successives d'un algorithme.

La ***complexité amortie*** de cet algorithme est alors $\frac{C}{m}$.
{% endnote %}
{% attention %}
La complexité amortie est une moyenne de complexité maximale, ce n'est **pas** une [complexité en moyenne](../complexité-moyenne) qui est une moyenne probabiliste.

Le temps moyen d'exécution pourra être supérieur à la complexité en moyenne si on a pas de chance alors qu'il ne pourra **jamais** excéder la complexité amortie.
{% endattention %}

Pour illustrer ces techniques d'analyse amortie nous allons utiliser deux exemples (ultra classiques).

## Algorithmes exemples

Les deux exemples ci-dessous sont paradigmatiques de l'analyse amortie où une même opération peut avoir une complexité très faible ou très importante selon les cas. Une analyse fine de la complexité montrera que dans l'exécution globale de l’algorithme ces complexités sont liées et qu'une opération de complexité importante sera forcément suivie de c'opérations de faibles complexité.

### Piles

{% note "**Définition :**" %}
Une [pile](https://fr.wikipedia.org/wiki/Pile_(informatique)) est une une structure de donnée informatique fondamentale. Qui possède 3 opérations :

* une méthode `push(x)`{.language-} qui ajoute l'élément `x`{.language-} à la structure en $\mathcal{O}(1)$ opérations
* une méthode  `pop()`{.language-} qui supprime l'élément le plus **récemment** ajouté à la structure  en $\mathcal{O}(1)$ opérations et le renvoie
* une fonction  `len(P)`{.language-} qui renvoie le nombre d'éléments de la pile `P`{.language-} en $\mathcal{O}(1)$ opérations

{% endnote %}

Une pile peut être vue comme une pile d'assiette. On ajoute et on supprime les assiettes depuis le haut de la pile.

{% info %}
Ne confondez pas pile et [file](https://fr.wikipedia.org/wiki/File_(structure_de_données)). La file supprime l'élément le plus **anciennement** ajouté.
{% endinfo %}

{% exercice %}
Implémentez une structure de pile en python.
{% endexercice %}
{% details "solution" %}
On utilise une liste et les méthodes :

* `append`{.language-} pour ajouter un élément à la structure
* `pop`{.language-} pour supprimer un élément de la structure

La fonction `len`{.language-} nous permet de connaître le nombre d'élément dans la structure.

Dans un interpréteur python :

```python
>>> P = list()
>>> P.append(2)
>>> P.append(5)
>>> len(P)
2
>>> x = P.pop()
>>> print(x)
5
>>> x = P.pop()
>>> len(P)
0
>>> print(x)
2
>>> 
```

{% enddetails %}

On crée la fonction suivante, dont la complexité de la fonction `K-pop(k, P)`{.language-} est — clairement — de $\mathcal{O}(1 + \min(k, \mbox{len}(P)))$ :

```text
Nom : k-pop
Entrées : 
    k : un entier
    P : une pile
Programme :
    k = min(k, len(P))
    Soit L une liste de taille k
    répéter k fois:
        x = P.pop()
        ajoute x à la fin de L
    Retour L

```

{% exercice "**Problème :**" %}
Soit $A$ un algorithme $A$ utilisant une pile $P$ via les opérations `len`{.language-}, `push`{.language-} et `k-pop`{.language-}. On suppose que l'algorithme effectue $m$ de ces opérations pendant son exécution.

Quel est la complexité totale de ces $m$ opérations ? En déduire la complexité amortie de ces opérations.
{% endexercice %}

La difficulté du calcul vient du fait que la complexité de la fonction `k-pop`{.language-} n'est pas constante. Bornons-là. On a effectué $m$ opérations, la taille maximale de la pile est donc de $m-1$ (si on a effectué $m-1$ opérations `push`{.language-} avant de la vider entièrement avec une instruction `k-pop`{.language-}) : la complexité de `k-pop`{.language-} est bornée par $\mathcal{O}(m)$.

On en conclut que la complexité de l'utilisation de la pile $P$ par l'algorithme $A$ est bornée par $m$ fois la complexité maximale des opérations `len`{.language-}, `push`{.language-} et `k-pop`{.language-} donc $\mathcal{O}(m^2)$.

On le démontrera précisément ci-après, mais on peut intuitivement voir que cette borne surestime grandement la complexité réelle :

* Pour que `k-pop`{.language-} ait une complexité de $\mathcal{O}(m)$, il faut avoir $\mathcal{O}(m)$ opérations `push`{.language-} avant. On ne peut donc pas avoir beaucoup d'opérations `k-pop`{.language-}  avec cette grande complexité
* Après une exécution de `k-pop`{.language-} avec une complexité de $\mathcal{O}(m)$, la pile est vide. Les exécutions suivante de `k-pop`{.language-} seront de complexité très faible.

### Compteur binaire

Dans ce problème, on encode un nombre binaire de $n$ bits par une liste $N$ à $n$ éléments. Pour $n=3$ par exemple, $N = [0, 0, 1]$ correspondra à $1$ et $N = [1, 1, 0]$ à 6.

Soit lors l'algorithme suivant, écrit en python :

```python#
def successeur(N):
    i = len(N) - 1

    while (i >= 0) and (N[i] == 1):
        N[i] = 0
        i -= 1

    if i >= 0:
        N[i] = 1
```

A un nombre `N`{.language-} écrit au format binaire donné, `successeur(N)`{.language-} va l'incrémenter de 1.

{% exercice %}
Prouver que l'algorithme précédent trouve bien le successeur d'un nombre $0 \leq N < 2^n - 1$.

Quel est le successeur de $N = [1, \dots, 1]$ ?
{% endexercice %}
{% details "solution" %}

A tout entier binaire $N= [a_0, \dots, a_{n-1}]$ son successeur vaut $N' = [a_0, \dots, a_{i-1}, 1, 0 \dots, 0]$ où $i$ est l'indice maximum tel que $a_i = 0$.

A l'issue de la boucle `while`{.language-} de la ligne 4, $i$ vaut :

* $-1$ si  $N$ valait initialement $N = [1, \dots, 1]$
* le plus grand indice tel que $N[i] = 0$ (avec $N$ la valeur initial de l'entier)

Note algorithme calcule donc :

* le successeur de $N$ si $0 \leq N < 2^N - 1$
* $[0, \dots 0]$ si $N = 2^n - 1$

{% enddetails %}

L'algorithme suivant affiche à l'écran tous les entiers écrit sous la forme binaire :

```python
def tous(n):

    N = [0] * n

    for i in range(2 ** n):
        successeur(N)
        print(N)
```

{% exercice "**Problème :**" %}
La complexité de l'exécution `tous(n)`{.language} dépend de l'exécution $2^n$ fois de l'algorithme `successeur(N)`{.language-}.

Quel est la complexité totale de l'exécution des $2^n$ opérations ? En déduire la complexité amortie de ces opérations.
{% endexercice %}

Comme pour l'exemple de la pile, la difficulté du calcul vient du fait que la complexité de la fonction `successeur(N)`{.language-} n'est pas constante :

* au mieux, $N[-1] = 0$ et la complexité de `successeur(N)`{.language-} est $\mathcal{O}(1)$,
* au pire, $N = [1] * n$ et la complexité de `successeur(N)`{.language-} est $\mathcal{O}(n)$,

La complexité totale de l'exécution des $2^n$ instances de `successeur(N)`{.language-} est :  $\mathcal{O}(n \cdot 2^n)$.

La aussi on le démontrera précisément, mais on peut intuitivement voir que cette borne surestime grandement la complexité réelle car si lors d'une exécution de l'algorithme `successeur(N)`{.language-}, $N[-1] = 1$ alors lors de l'exécution suivant on aura $N[-1] = 0$. La complexité de `successeur(N)`{.language-} ne peut donc être importante qu'au pire une fois sur deux.

## Analyse par Agrégat

{% note %}
La technique de **l'analyse par agrégat** consiste à considérer l'ensemble des $m$ exécutions comme un **tout**.

On évalue la complexité des $m$ opérations en même temps, sans distinguer les différentes opérations.
{% endnote %}

### Exemple de la pile

Au cours des $m$ exécutions, on peut considérer ue l'on a fait appel :

* $m'$ fois à la fonction `k-pop`{.language-},
* $m''$ fois à la fonction `push`{.language-},
* $m - m' - m''$ fois à la fonction `len`{.language-}.

Le nombre total d'éléments *popés* au cours des $m'$ exécutions de la fonction `k-pop`{.language-} ne peut excéder le nombre total $m''$ d'éléments *pushés*. La complexité totale des $m'$ exécutions de `k-pop`{.language-} vaut donc $\mathcal{O}(m' + m'')$.

Comme la complexité d'un appel à `push`{.language-} ou à `len`{.language-} vaut invariablement $\mathcal{O}(1)$, on en conclut que la complexité totale recherchée vaut :

$$
C = \mathcal{O}(m' + m'') + \mathcal{O}(m'') + \mathcal{O}(m - m' - m'') = \mathcal{O}(m + m'') = \mathcal{O}(m)
$$

Cette complexité est bien inférieure à notre première estimation de la complexité (qui valait $\mathcal{O}(m^2)$). La complexité amortie d'une opération est ainsi de : $\frac{C}{m} = \mathcal{O}(1)$. Le coût moyen d'une opération `k-pop`{.language-}, `push`{.language-} ou `len`{.language-} est constant, sans distinction de l'opération !

### Exemple du compteur

La complexité d'une exécution de `successeur(N)`{.language-} est égale au nombre de bits qu'elle a modifié dans `N`{.language-}. Comme les $2^n$ exécutions de `successeur(N)`{.language-} vont parcourir une et une seule fois tous les nombre de 0 à $2^n$ on en conclut que :

* le dernier bit de $N$ est modifié à chaque appel
* l'avant-dernier bit de $N$ est modifié que si le dernier bit de $N$ valait $1$ : il est modifié tous les 2 appels
* l'avant-avant-dernier bit de $N$ est modifié que si les deux derniers bits de $N$ valaient $1$ : il est modifié tous les 4 appels
* ...
* le $i$ bit avant la fin de $N$ est modifié que si les $i-1$ derniers bits de $N$ valaient $1$ : il est modifié tous les $2^{i-1}$ appels
* ...
* le premier bit de $N$ est modifié que si les $n-1$ derniers bits de $N$ valaient $1$ : il est modifié tous les $2^{n-1}$ appels

La complexité totale des $2^n$ appels à `successeur(N)`{.language-} vaut donc :

$$
C = \sum_{i=0}^{n-1}(2^n \cdot \frac{1}{2^i}) = 2^n \cdot  \sum_{i=0}^{n-1}\frac{1}{2^i}
$$

On utilise alors le fait que : $\sum_{i=0}^{n-1} \frac{1}{2^i} = 2 - \frac{1}{2^{n-1}}$ (immédiat par récurrence, il existe également [une preuve directe](https://fr.wikipedia.org/wiki/1/2_%2B_1/4_%2B_1/8_%2B_1/16_%2B_%E2%8B%AF)), ce qui permet d'obtenir :

$$
C = 2^n \cdot  (2 - \frac{1}{2^{n-1}}) \leq 2^{n+1}
$$

On a donc une complexité de $\mathcal{O}(2^{n+1}) = \mathcal{O}(2^{n})$ et une complexité amortie de $\mathcal{O}(1)$. Du calcul précédent donnant $C \leq 2^{n+1}$ on en conclut que chacune des $2^n$ exécutions de l'algorithme `successeur(N)`{.language-} va changer 2 bits en moyenne.

{% exercice %}
Vérifiez expérimentalement qu'en moyenne, sur tous les appels de `successeur(N)`{.language-} pour l'algorithme `tous(n)`{.language-}, le nombre de bits changé est inférieur à 2.
{% endexercice %}
{% details "solution" %}

```python
def successeur(N):
    i = len(N) - 1

    while i >= 0 and (N[i] == 1):
        N[i] = 0
        i -= 1

    if i >= 0:
        N[i] = 1

    return len(N) - i


def tous(n):

    N = [0] * n
    total = 0
    for i in range(2**n):
        total += successeur(N)
        print(N)

    return total / 2**n


x = tous(5)
print(x)

```

{% enddetails %}

## Analyse comptable



## Analyse par potentiel


 fil rouge du
On peut 
Lorsque les temps d'exécution d'un même algorithme peuvent varier fortement selon ses paramètres, on a vu que l'on peut calculer sa complexité en moyenne pour se donner une idée de la complexité attendue avec un jeu de paramètres donné, mais quelconque.

Il existe cependant un cas où l'on peut faire bien mieux : lorsque l'on effectue plusieurs fois le même sur de

 algorithme 
> TBD : lorsque l'on a des opérations de coût différents et que l'on veut une complexité exacte ou
> que l'on a $m$ exécution successives avec certaines qui coûtent cher et d'autres non..
> TBD : exemple du compteur avec les 3 façon de le calculer
