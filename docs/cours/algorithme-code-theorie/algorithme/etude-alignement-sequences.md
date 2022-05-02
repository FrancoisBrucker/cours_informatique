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

> * definition problème
> * où on le retrouve (biologie/ correcteur orth)
> * analyse des possible
> * algorithme par programmation dynamique
> * problème connexe : alignement local
{: .tbd}

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

Enfin, on a clairement que :

> La distance d'édition entre deux chaînes correspond à l'alignement de coût minimum entre celles-ci.
{: .note}

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

### 
> généralisation différences. Attention doit rester symétrique. 
{: .tbd}

## calcul

## alignement local
