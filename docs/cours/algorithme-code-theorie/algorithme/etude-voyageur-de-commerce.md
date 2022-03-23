---
layout: page
title:  "étude : voyageur de commerce"
category: cours
---

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [algorithmie]({% link cours/algorithme-code-theorie/algorithme/index.md %}) / [étude : voyageur de commerce]({% link cours/algorithme-code-theorie/algorithme/etude-voyageur-de-commerce.md %})
>
> **prérequis :**
>
> * [algorithmes gloutons]({% link cours/algorithme-code-theorie/algorithme/methode-gloutons.md %})
>
{: .chemin}

Nous allons étudier ici un problème d'intérêt pratique ainsi que certains problèmes connexes. L'étude de ces problèmes nous permettra d'utiliser des technique de design d'algorithmes connus comme les algorithmes gloutons ou d'en découvrir d'autres comme la programmation dynamique.

En plus d'être des problèmes courant, ils de plus très jolis algorithmiquement. On espère que vous aimerez la ballade.

## Voyageur de commerce

Le [problème du voyageur de commerce](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_voyageur_de_commerce) peut se formuler ainsi :

*"un voyageur de commerce doit visiter $n$ villes dans la journée. Il veut donc partir de chez lui, parcourir toutes les villes puis revenir chez lui en ayant parcouru le minimum de distance"*.

Il existe de nombreuses formalisation de ce problème, nous allons en donner 2. Commençons par la première, qui est la plus utilisée car elle s'applique directement aux villes sur une carte (la distance routière entre 2 villes étant une distance) :

> **Voyageur de commerce euclidien** : Soit $V$ un ensemble de $n$ éléments et $d: V \times V \rightarrow \mathbb{R}^+$ une distance (donc symétrique et respectant l'inégalité triangulaire) sur $V$.
>
> Donnez un ordre $v_1, \dots, v_n$ entre les villes minimisant :
>
> $$
> \sum_{i=1}^{i=n-1} d(v_i, v_{i+1}) + d(v_n, v_1)
> $$
>
{: .note}

> exemple
{: .tbd}

La seconde formulation, plus générale, nécessite l'utilisation de *graphes*. Nous n'allons pas faire un cours de graphe ici (une introduction est disponible [ici]({% link cours/graphes/index.md %}) pour les personnes intéressées), juste donner quelques définitions (simples) utiles :

> Un **graphe** $G = (V, E)$ est un couple où $E$ est un ensemble de sous-ensemble à 2 éléments de $V$. $E$ est l'ensemble des **sommets** de $G$ et $E$ l'ensemble des **arêtes** (on notera les arêtes $xy$ plutôt que $\{x, y\}$ pour rendre les notations plus digestes).
>
> * une **valuation** d'un graphe $G = (V, E)$ est une fonction $\omega: E \rightarrow \mathbb{R}^+$
> * un **chemin** est une suite de sommets $v_1,\dots, v_i, \dots, v_m$ tels que :
>   * $v_iv_{i+1} \in E$ pour tout $1\leq i < m$,
>   * $v_iv_{i+1} \neq v_jv_{j+1}$ si $i \neq j$
> * un **cycle** est un chemin dans le premier et le dernier élément sont identiques.
>
{: .note}

De là, la définition générale du voyageur de commerce est :

> **Problème du voyageur de commerce** :
>
> * **Données** :
>   * un graphe $G = (V, E)$ à $n$ sommets
>   * une valuation $\omega$ sur $G$
> * **question** :
>   * donnez un cycle $v_1, \dots, v_i, \dots, v_n = v_1$ passant par tous les sommets tel que $\sum_{i=1}^{i=n-1} d(v_i, v_{i+1}) + d(v_n, v_1)$ soit minimal.
>
{: .note}

Remarquez que si le *problème du voyageur de commerce euclidien* admet toujours une solution (tous les parcours entre les villes sont possibles), le problème du  le voyageur de commerce euclidien est un sous-problème du problème de voyageur de commerce. Avant de s'attaquer à ces problèmes, commençons par nous échauffer en considérant quelques problèmes de graphes connexes, traitant de chemins et de cycles

## problèmes de graphes

Le problème 
Avant d'étudier le problème général, commençons par un problème plus simple : "est-il possible d'atteindre toutes les villes" ? Il n'est en effet pas dit qu'il existe une solution pour le *problème du voyageur de commerce*, ni même qu'il soit possible de p

### connexité

> **Problème de connexité d'un graphe** :
>
> * **Données** :
>   * un graphe $G = (V, E)$ à $n$ sommets
> * **question** :
>   * peut-on trouver un chemin entre $x$ et $y$, quelque soient $x, y \in V$ ?
>
{: .note}

Les graphes qui répondent OUI à cette question sont dit **connexes**.

Remarquez que le problème de connexité est équivalent au problème suivant (pour un graphe donné, les réponses aux deux problèmes sont identiques), qui semble cependant plus simple :

> **Problème des chemins à partir d'un sommet** :
>
> * **Données** :
>   * un graphe $G = (V, E)$ à $n$ sommets
>   * un sommet $x \in V$
> * **question** :
>   * peut-on trouver un chemin entre $x$ et $y$, quelque soit $xy \in V$ ?
>
{: .note}
{% details preuve de l'équivalence %}

Soit $G = (V, E)$ un graphe. Il est clair que s'il est connexe, le *problème des chemins à partir d'un sommet* est aussi vrai, $\forall x \in V$

Réciproquement, supposons que le problème *problème des chemins à partir d'un sommet* est vrai pour $G$ et un sommet $x^\star$

Soient alors $x \neq y \in V$. Il existe :

* un chemin $u_1\dots u_k$ entre $x^\star$ et $x$ ($u_1 = x^\star$ et $u_k = x$)
* un chemin $v_1\dots v_l$ entre $y$ et $x^\star$ ($v_l = y$ et $v_l = x^\star$)

On peut alors noter $i^\star$ le plus grand indice tel qu'il existe $j^\star$ avec : $u_{i^\star$} = v_j^\star$. Comme $u_1 = v_l$, $i^\star$ existe.

La suite $v_1 \dots v_{j^\star} u_{i^\star+1} \dots u_k$ est alors un chemin entre $x$ et $y$. 

Comme $x$ et $y$ ont été pris au hasard, on en conclut que $G$ est connexe.

{% enddetails %}



### cycle hamiltonien

Passer une seule fois par chaque ville

NP-difficile

(remarque sommet est dur passer par toutes les arêtes, c'est facile)

## problèmes NP-complets

nous pb optimisation => pb de décision + dichotomie


réduction : https://fr.wikipedia.org/wiki/R%C3%A9duction_(complexit%C3%A9)

et SAT


on peut montrer que (si vous insistez on pourra le faire)


déf (avec les mains) + on sait que c'est dur et donc on peut se passer de chercher une solution optimale.

-> voyageur de commerce dur 2x :
* trouver le chemin hamiltonien
* si facile de trouver un chemin hamiltonien (euclidien), il y en a trop.


euler euclidien

marche sur les graphes de b des sommets impair

## résolution exacte par programmation dynamique


## heurisitique

### gloutons

### 2-opt

### à performance garantie

2 optimal

on peut faire mieux (christofides, lien wiki) et c'est le min.

## code

csv ou json avec villes + coordonnées gps

connexité et labyrinte ?

