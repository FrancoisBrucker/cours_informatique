---
layout: page
title:  "étude / alignement de séquences"
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [algorithmie]({% link cours/algorithme-code-theorie/algorithme/index.md %}) / [étude : alignement de séquences]({% link cours/algorithme-code-theorie/algorithme/etude-alignement-sequences.md %})
>
> prérequis :
>
> * [étude : recherche de sous-chaines]({% link cours/algorithme-code-theorie/algorithme/etude-recherche-sous-chaines.md %})
>
{: .chemin}

Nous allons voir dans cette étude comment définir/calculer une distance entre 2 chaînes de caractères. Nous utiliserons la [distance d'édition](https://fr.wikipedia.org/wiki/Distance_de_Levenshtein), très utilisée.

## définition

Soient $a$ et $b$ deux chaines de caractères définies sur un alphabet $\mathcal{A}$. Commençons par supposer qu'elles sont de même longueur (disons $n$). On peut compter les différences entre $a$ et $b$ :

$$
d(a, b) = \vert \{i \mid a[i] \neq b[i], 0 \leq i < n \} \vert
$$

> La distance entre *"MISOS"* et *"TILOS"* est de 2 différences.

Parfois, ce comptage brute des différences n'est pas suffisant. Si l'on cherche à trouver les erreurs de frappe, on pourra par exemple supposer que deux mots sont proches si les lettres qui les composent sont proches sur le clavier.

> *"ORNE"* sera plus proche de *"ORBE"* que de *"URNE"* si l'on compte l'éloignement des touches sur le clavier.

Il faut donc généraliser notre distance en se donnant une distance de substitution $d$ définie entre deux caractères, que l'on généralise ensuite à la comparaison de deux chaînes :

$$
d(a, b) = \sum_{i=0}^{n-1}d(a[i], b[i])
$$

Cette définition de distance est cependant un peu frustre puisque qu'elle ne permet de comparer que deux mots ayant le même nombre de caractères. Il faut donc à nouveau généraliser.

L'idée est de compter le nombre d'opérations élémentaires nécessaire pour passer d'un mot à l'autre. Les opérations élémentaires pouvant être :

* l'ajout d'un caractère
* la suppression d'un caractère
* la substitution d'un caractère

> Cette façon de faire pour comparer 2 chaînes de caractères est très utilisé en biologie lorsque l'on compare deux séquences d'ADN car les opérations élémentaires correspondent aux processus biologique d'évolution.

Par exemple pour passer de *"MEROUS"* à *"MARLOU"*, on peut :

* changer un *"E"* en *"A"* : *"MAROUS"*
* changer un *"O"* en *"L"* : *"MARLUS"*
* changer un *"U"* en *"O"* : *"MARLOS"*
* changer un *"S"* en *"U"* : *"MARLOU"*

Ce qui donne une distance de 4 (c'est notre distance qui compte le nombre de caractères différents)

Mais on peut aussi :

* changer un *"E"* en *"A"* : *"MAROUS"*
* ajouter un *"L"* : *"MARLOUS"*
* supprimer un *"S"* : *"MARLOU"*

La distance est maintenant de 3.

Remarquez que l'on a bien une [distance](https://fr.wikipedia.org/wiki/Distance_(math%C3%A9matiques)#D%C3%A9finition) :

* symétrique
* séparation
* inégalité triangulaire

Enfin, ce compte peut être généralisé comme précédemment en utilisant une **distance élémentaire entre caractères** $d: \mathcal{A} \cup \{ \epsilon \} \rightarrow \mathbb{R}^+$. Ses propriétés doivent être :

* $\epsilon$ est le caractère vide, il n'appartient pas à l'alphabet au départ
* $d(x, y) = d(y, x)$
* $d(x, x) = 0$ pour tout $x \in \mathcal{A}$
* $d(x, y) > 0$ pour tout $x\neq y \in \mathcal{A}$

Le caractère vide $\epsilon$ est là pour simuler le coût pour supprimer un caractère ($d(x, \epsilon)$) ou en insérer un ($d(\epsilon, x)$). On appelle alors **coût élémentaires** les valeurs :

* $d(x, \epsilon)$ nommées **coût de suppression**,
* $d(\epsilon, x)$ nommées **coût d'insertion**
* $d(x, y)$ avec $x$ et $y$ 2 caractères, nommées **coût de substitution**

Par symétrie le coût d'insertion d'un caractère est égal à son coût de suppression.

> La **distance d'édition** entre les chaînes $a$ et $b$ est la somme minimum des coûts élémentaires pour passer de $a$ à $b$.
{: .note}

Notez que cette distance existe toujours puisque pour passer d'une chaîne $a$ à une chaine $b$, on peut toujours commencer par supprimer tous les caractères de $a$ puis insérer tous les caractères de $b$ :

$$
d(a, b) = d(b, a) \leq \sum_{i}d(a[i], \epsilon) + \sum_{i}d(\epsilon, b[i]) =  \sum_{i}d(b[i], \epsilon) + \sum_{i}d(\epsilon, a[i])
$$

>Ceci est très utilisé en biologie où l'on compare des protéines entre elles. Par exemple, lorsque l'on compare 2 protéines entre elles via leurs séquences d'acides aminées, on utilise une distance entre acide aminés basée sur les propriétés physico-chimiques de ceux-ci ou basé sur l'évolution des séquences (voir par exemple [matrice protéiques](http://www.dsi.univ-paris5.fr/bio2/autof2/mod4_3b.htm)).

## propriétés

Avant de parler des propriétés de la distance d'édition, commençons par parler de ses limitations :

* Les coûts élémentaires sont indifférents à la position dans la chaine
* les coûts élémentaires ne dépendant pas des lettres alentours

Ces limitations ne sont souvent pas gênantes et permettent un calcul aisé (on le verra) de cette distance.

### alignement

Etant donné une distance d'édition entre deux chaînes de caractères, la liste des opérations élémentaires permettant de passer d'une chaîne à l'autre peut se représenter par un **alignement**. Par exemple l'alignement entre `MEROUS` et `MARLOU` précédent va s'écrire :

```text
MER-OUS
| | || 
MARLOU-
```

Il se lit comme ça :

* La chaîne initiale est au-dessus et la chaîne finale en dessous
* les caractères qui ne bougent pas sont représentées avec un `|` :
* les insertions sont représentés par un `-` là où le caractère est inséré dans la chaîne de départ:
* les suppression sont représentés par un `-` là où le caractère est supprimé dans la chaîne d'arrivée :

Cela correspond bien à notre passage de  `MEROUS` et `MARLOU` :

1. une substitution
2. une insertion
3. une suppression

Par symétrie des distances élémentaires, on peut bien sur faire le contraire (on transforme les insertions en suppression et vice versa) b:

```text
MARLOU-
| | || 
MER-OUS
```

De façon formelle :

> Un alignement entre la chaîne $a =a_0\dots a_{n-1}$ et $b = b_0\dots b_{m-1}$ est un couple $(a^\star, b^\star)$ tel que :
>
> * $a^\star =a^\star_0\dots a^\star_{L-1}$
> * $b^\star =b^\star_0\dots b^\star_{L-1}$
> * chaque caractère de $a^\star$ et $b^\star$ sont soit `-` soit des caractères des chaines
> * $a^\star$ (respectivement $b^\star$) privé des caractères `-` est égal à $a$ (*resp.* $b$)
>  $(a^\star_i, b^\star_i) \neq (-, -)$ pour tout $0 \leq i < L$
>
{: .note}

On remarque que : $\max(n, m) - 1 \leq L < n + m$.

Enfin, on a clairement que :

> La distance d'édition entre deux chaînes $a$ et $b$ correspond à l'alignement $(a^\star, b^\star)$ de coût minimum entre celles-ci.
>
> $$
> S(a^\star, b^\star) = \sum_{i=0}^{L-1} d(a^\star_i, b^\star_i)
> $$
>
{: .note}

Notez bien que si le coût est minimum, il **peut** y avoir plusieurs alignements ayant ce coût : l'alignement optimal **n'est pas** unique.

### nombres d'alignements

Il peut y avoir beaucoup (beaucoup) d'alignements possible entre 2 séquences.

{% details exercice : trouver au moins 3 alignements différents entre les séquences ACTGC et ACGTC %}

```text
ACTG-C
|  |
A-CGTC
```

```text
ACTGC
||  |
ACGTC
```

```text
ACTG-C
|| | |
AC-GTC
```

et bien d'autres encore sont possibles.

{% enddetails %}

On peut remarquer que ce nombre ne dépend que de la longueur des chaines $a$ et $b$, par de leur contenu. On note alors $f(n, m)$ le nombre possible d'alignements entre une chaines de longueur $n$ et une chaîne de longueur $m$.

Comme un alignement ne peut finir sur $(-, -)$, on ne peut qu'avoir 3 possibilités :

* $(a_{n-1}, b_{m-1})$
* $(a_{n-1}, -)$
* $(-, b_{m-1})$

Aligner $a$ et $b$ revient alors soit à aligner :

* $a[:-1]$ et $b[:-1]$
* aligner $a[:-1]$ et $b$
* aligner $a$ et $b[:-1]$

Ce qui se donne l'équation de récurrence suivante :

$$
f(n, m) = f(n − 1, m − 1) + f(n − 1, m) + f(n, m − 1)
$$

On peut alors prouver, si $n=m$ que :

$$
f(n, n) \sim \frac{(1 + \sqrt{2})^{2n + 1}}{\sqrt{n}}
$$

Ce nombre est affreusement énorme :

* pour $n = 10$, on a déjà  $f(10, 10) \sim 34537380$
* pour $n = 10$, on a déjà  $f(100, 100) \sim 8.67 \cdot 10^{75}$

> Il n'y a qu'environ $10^{80}$ particules dans l'univers.

## calcul

La distance d'édition entre $a$ et $b$ est équivalente à trouver le meilleurs alignement entre $a$ et $b$. Il n'est — heureusement —  pas nécessaire de  les  calculer tous pour trouver le meilleur. Il suffit d'utiliser notre équation de récurrence. On en déduit que la distance d'édition entre $a$ et $b$ est soit :

* égale à la distance d'édition entre $a[:-1]$ et $b[:-1]$ plus le coût élémentaire de substitution des 2 derniers caractères : $d(a[-1], b[-1])$
* égale à la distance d'édition entre $a[:-1]$ et $b$ plus le coût élémentaire de la suppression du dernier caractère de $a$ : $d(a[-1], -)$
* égale à la distance d'édition entre $a$ et $b[:-1]$ plus le coût élémentaire de l'insertion du dernier caractère de $b$ $d(-, b[-1])$

Donc, pour tout $i$ et $j$ :

$$
d(a[:i+1], b[:j+1]) = \min \begin{cases}
      d(a[:i], b[:j]) + d(a[i], b[j]) & \text{substitution}\\
      d(a[:i], b[:j + 1]) + d(a[i], -) & \text{suppression}\\
      d(a[:i + 1], b[:j]) + d(-, b[j]) & \text{insertion}\\
    \end{cases}
$$

Ceci nous donne une représentation matricielle de l'alignement et de la distance d'édition :

|           | $-$ | $a[0]$ | ... | $a[i-1]$           | $a[i]$                | $a[n-1]$|
|-----------|-----|---------------|-----|--------------------|-----------------------|---------|
|    $-$    | 0   |  $d(a[0], -)$ |     |    $d(a[:i], -)$                | $d(a[:i], -)  + d(a[i], -)$                    | $d(a[:n], -)$ |
|$b[0]$     |$d(-, b[0])$ |        |     |                    |                       |         |
|...        |     |        |     |                    |                       |         |
|$b[j-1]$   | $d(-, b[:j])$    |        |     | $d(a[:i],b[:j])$   | $d(a[:i+1],b[:j])$    |         |
|$b[j]$     | $d(-, b[:j]) + d(b[j], -)$    |        |     | $d(a[:i],b[:j+1])$ |  $d(a[:i+1],b[:j+1])$ |         |
|...        |     |        |     |                    |                       |         |
|$b[m-1]$   | $d(-, b[:m])$    |        |     |                    |                       |$d(a,b)$ |

Et nous donne un algorithme très facile pour la calculer, puisqu'il suffit re remplir la première ligne et la première colonne, puis de progresser ligne à ligne avec la formule :

```python
M[i + 1][j + 1] = min(M[i][j] + d(a[j], b[i]), 
                      M[i + 1][j] + f(-, b[i]),
                      M[i][j + 1] + f(a[j], -))
```

 On appellera cette matrice **matrice d'édition**. Et elle calculable en $\mathcal{O}(mn)$ opérations, ce qui est bien plus petit que le nombre total d'alignements !

> La technique de création algorithmique utilisée est appelée [programmation dynamique](https://fr.wikipedia.org/wiki/Programmation_dynamique) : un chemin optimal est constitué de sous-chemins eux-mêmes optimaux.

## alignement à partir de la matrice

>remontée
{: .tbd}

## exemple

Distance élémentaire :

| |A|C|G|T
|A|0| | |
|C|2|0| |
|G|2|2|0|
|T|2|2|2|0
|-|1|1|1|1

Aller de `ACTGATT` (horizontal) à `GCTAATCG` (vertical).

> Créez la matrice d'édition *vierge* à utiliser
{: .a-faire}
{% details solution %}

| |-|A|C|T|G|A|T|T
|-| | | | | | | |
|G| | | | | | | |
|C| | | | | | | |
|T| | | | | | | |
|A| | | | | | | |
|A| | | | | | | |
|T| | | | | | | |
|C| | | | | | | |
|G| | | | | | | |

{% enddetails  %}

> Remplissez la première ligne et la première colonne
{: .a-faire}
{% details solution %}

| |-|A|C|T|G|A|T|T
|-|0|1|2|3|4|5|6|7
|G|1| | | | | | |
|C|2| | | | | | |
|T|3| | | | | | |
|A|4| | | | | | |
|A|5| | | | | | |
|T|6| | | | | | |
|C|7| | | | | | |
|G|8| | | | | | |

{% enddetails  %}

> Remplissez le reste de la matrice ligne à ligne
{: .a-faire}
{% details solution %}

| |-|A|C|T|G|A|T|T
|-|0|1|2|3|4|5|6|7
|G|1|2|3|4|3|4|5|6
|C|2|3|2|3|4|5|6|7
|T|3|4|3|2|3|4|5|6
|A|4|3|4|3|4|3|4|5
|A|5|4|5|4|5|4|5|6
|T|6|5|6|5|6|5|4|5
|C|7|6|5|6|7|6|5|6
|G|8|7|6|7|6|7|6|7

{% enddetails  %}

> Donnez la distance d'édition entre `ACTGATT` et `GCTAATCG`
{: .a-faire}

{% details solution %}
la dernière colonne de la dernière ligne de la matrice ($M[-1][-1]$) vaut 7 : c'est la distance d'édition
{% enddetails  %}

> Donnez un alignement réalisant la distance d'édition entre `ACTGATT` et `GCTAATCG`
{: .a-faire}
{% details solution %}

> à faire
{: .tbd}

{% enddetails  %}

## algorithme

Nous allons créer l'algorithme en plusieurs parties :

1. rendre une fonction de coût élémentaire
2. rendre la matrice d'édition
3. utiliser la matrice d'édition pour connaitre la distance d'édition
4. utiliser la matrice d'édition pour connaitre un alignement optimal

### distance élémentaire

La distance élémentaire doit associer un réel positif à :

* un couple de caractère pour une substitution
* un caractère pour une insertion ou une suppression

Ces informations peuvent être stockées dans un dictionnaire `dist` avec comme clés :

* $(x, y)$ avec $x$ et $y$ deux caractères. On peut de plus supposer que $x \leq y$
* $x$ avec $x$ un caractère

En supposant que l'on ait un dictionnaire `dist` de ce type, il sera plus aisé de d'avoir une fonction de signature `f(x, y=None)` telle que :

* si $x$ et $y$ sont donné, rend `dist[(x, y)]` si $x < y$ et `dist[(y, x)]` sinon.
* si uniquement $x$ est renseigné ($y$ vaut `None`), la fonction devrait rendre $d[x]$.

On peut alors créer une fonction qui prend en paramètre ce dictionnaire et rend une fonction de calcul. Ceci est facile à faire en python, et savoir créer une fonction qui rend une fonction est une compétence qui peut se révéler utile :

```python
def crer_fonction(dist):
    def f(x, y=None):
        if y is None:
            return dist[x]
        elif x < y:
            return dist[(x, y)]
        else:
            return dist[(y, x)]
    return f
```

### matrice d'édition

Maintenant qu'on a la fonction d'édition élémentaire, on peut écrire l'algorithme qui crée la matrice d'édition

```python
def calcul_matrice(a, b, f):
    M = [[0] * len(a) for i in len(b)]
    M[0][0] = 0
    for j in range(len(a)):
        M[0][j] = M[0][j + 1] + f(a[j])
    for i in range(len(b)):
        M[i][0] = M[j + 1][0] + f(b[i])
    
    for i in range(len(b)):
        for j in range(len(a)):
            M[i + 1][j + 1] = min(M[i][j] + f(a[j], b[i]),
                                  M[i + 1][j] + f(b[i]), 
                                  M[i][j + 1] + f(a[j]))

    return M
```

La distance d'édition entre $a$ et $b$ est alors `M[-1][-1]`.

### alignement à partir de la matrice d'édition

La matrice d'édition nous permet de retrouver l'alignement, en *remontant* la matrice.


Ecrivez l'algorithme qui, à partir de deux séquences $a$ et $b$ et d'une distance élémentaire écrite sous forme d'une fonction rend la matrice d'édition.


 permet de rendre la matrice
> écrire l'algorithme + complexité
{: .tbd}


> chemin = alignement
{: .tbd}

