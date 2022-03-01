---
layout: page
title:  "Complexité en moyenne"
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [algorithmie]({% link cours/algorithme-code-theorie/algorithme/index.md %}) / [complexité en moyenne]({% link cours/algorithme-code-theorie/algorithme/complexite-moyenne.md %})
>
> **prérequis :**
>
> * [complexité max/min]({% link cours/algorithme-code-theorie/algorithme/complexite-max-min.md %})
>
{: .chemin}

Lorsque le nombre d'opérations d'un algorithme dépend non seulement de la taille de ses entrées mais également de la structure de celles-ci, on a coutume de calculer sa complexité en moyenne :

> La **complexité en moyenne** d'un algorithme est le nombre moyen d'opérations nécessaires pour se terminer par rapport à une taille fixée de ses entrées.
{: .note}

Cette mesure est très utile en pratique car si la complexité maximale et minimale d'un algorithme est très différente, cela permet de savoir le nombre d'opérations espéré pour un tableau quelconque de taille donné.

## calcul de la complexité en moyenne

Pour un algorithme $A$ donné, soit $\mathcal{E}$ l'ensemble contenant toutes Ses entrées de taille $n$ (c'est à dire qu'il faut $n$ cases mémoires pour stocker une entrée). S'il faut $C(e)$ opérations pour exécuter l'algorithme avec l'entrée $e$, on a que :

* la complexité $C^n_\max$ de l'algorithme vaut $C^n_\max = \max \\{C(e) \mid e \in \mathcal{E}\\}$
* la complexité minimum $C^n_\min$ de l'algorithme vaut $C^n_\min = \min \\{C(e) \mid e \in \mathcal{E}\\}$

L'espérance de la complexité, c'est à dire la complexité *normale* si l'algorithme est exécutée pour une entrée au hasard, est appelée **complexité en moyenne**.

Elle dépend des entrées de celui-ci et plus précisément du nombre de fois où une entrée donnée peut être choisie. Pour pouvoir la calculer de façon formelle, il faut connaitre ainsi le modèle probabiliste associé aux données :

> La **complexité en moyenne** de l'algorithme $A$ pour une entrée de taille $n$ est :
>
> $$C = \sum_{e \in \mathcal{E}} p_e \cdot C(e)$$
>
> Avec $\mathcal{E}$ l'ensemble des données de taille $n$, $p_e$ la probabilité d'exécuter l'algorithme avec l'entrée $e \in \mathcal{E}$ et $C(e)$ le nombre d'opérations utilisé par l'algorithme pour se terminer avec l'entrée $e$.
>
{: .note}

Si l'on a pas de modèle a priori, on considérera que chaque donnée est équiprobable : chaque entrée a la même probabilité d'être choisie, $p_e = \frac{1}{\mid \mathcal{E} \mid}$.

## exemple de la recherche d'un élément dans un tableau {#exemple-recherche}

Reprenons l'exemple de la [recherche d'un élément d'un un tableau]({% link cours/algorithme-code-theorie/algorithme/complexite-max-min.md %}#exemple-recherche) :

```python
def est_dans_tableau(valeur, tableau):
    for x in tableau:
        if x == valeur:
            return True
    return False
```

On avait déterminé ses complexités par rapport à la taille $n$ du tableau :

* la complexité maximale de l'algorithme `est_dans_tableau` est $\mathcal{O}(n)$ (on parcourt tout le tableau sans trouver `valeur`)
* la complexité minimale de l'algorithme `est_dans_tableau` est $\mathcal{O}(1)$ (`valeur` est le premier élément du tableau)

Si l'on note $\mathcal{E}$ l'ensemble de tous les tableau de taille $n$, il y en a une infinité. Notre calcul de la complexité en moyenne est donc ardu. Pour simplifier le problème, analysons la complexité selon l'endroit où se trouver `valeur` dans le `tableau` :

* si `valeur` est à l'indice $0$ du tableau, il faudra $\mathcal{O}(1)$ opération pour exécuter l'algorithme
* si `valeur` est à l'indice $1$ du tableau, il faudra deux fois plus d'opérations que s'il était à l'indice $0$, donc  $2 \cdot \mathcal{O}(1)$ opérations pour exécuter l'algorithme
* si `valeur` est à l'indice $2$ du tableau, il faudra trois fois plus d'opérations que s'il était à l'indice $0$, donc  $3 \cdot \mathcal{O}(1)$ opérations pour exécuter l'algorithme
* ...
* si `valeur` est à l'indice $i$ du tableau, il faudra $i+1$ fois plus d'opérations que s'il était à l'indice $0$, donc  $(i+1) \cdot \mathcal{O}(1) = \mathcal{O}(i + 1)$ opérations pour exécuter l'algorithme
* ...
* si `valeur` est à l'indice $n-1$ du tableau, il faudra $n$ fois plus d'opérations que s'il était à l'indice $0$, donc  $n \cdot \mathcal{O}(1) = \mathcal{O}(n)$ opérations pour exécuter l'algorithme
* si `valeur` n'est pas dans le tableau, il faudra $n+1$ fois plus d'opérations que s'il était à l'indice $0$, donc  $(n+1) \cdot \mathcal{O}(1) = \mathcal{O}(n+1)$ opérations pour exécuter l'algorithme

L'ensemble $\mathcal{E}$ de tous les tableaux de taille $n$ peut alors se segmenter en $n+1$ ensembles :

* les ensembles $\mathcal{E}_i$, pour $0 \leq i < n$, qui regroupent les tableaux contenant `valeur` en position $i$
* l'ensemble $\mathcal{E}_n$, qui regroupe tous les tableaux ne contenant pas `valeur`

La complexité en moyenne s'écrit alors :

$$
\begin{array}{lcl}
C & = & \sum_{e \in \mathcal{E}} p_e \cdot C(e) \\
&=& \sum_{0 \leq i \leq n} (\sum_{e \in \mathcal{E}_i} p_e \cdot C(e)) \\
&=& \sum_{0 \leq i \leq n} ((\sum_{e \in \mathcal{E}_i} p_e) \cdot \mathcal{O}(i+1)) \\
\end{array}
$$

En notant $p_{i}$ la probabilité qu'à un tableau d'être dans $\mathcal{E}_i$ ($p_i =\sum_{e \in \mathcal{E}_i} p_e$)  on a alors :

$$
\begin{array}{lcl}
C & = & \sum_{0 \leq i \leq n} (p_i \cdot \mathcal{O}(i+1)) \\
\end{array}
$$

Pour pouvoir calculer $C$ effectivement, il faut connaitre les $p_i$. Comme on a pas de modèle a priori, on va considérer que chaque tableau de taille $n$ à la même probabilité d'être choisie et donc que la position de `valeur` dans tableau est équiprobable : $p_i = \frac{1}{n + 1}$ :

$$C =  (\sum_{i=0}^{i = n}\frac{1}{n + 1} \mathcal{O}(i+1)) = \mathcal{O}(\frac{\sum_{i=0}^{i = n}(i +1)}{n +1})$$

Comme $\sum_{i=0}^{i = n}(i + 1) = \frac{(n + 2)(n + 1)}{2}$ on en déduit que :

$$C = \mathcal{O}(\frac{n+1}{2}) = \mathcal{O(n)}$$

> En moyenne la complexité l'algorithme `est_dans_tableau` est la même que la complexité maximale. La complexité minimale est très rarement atteinte.
{: .note}

Pour aller plus vite dans le calcul, on aurait pu dire que si notre modèle est équiprobable, `valeur` va se trouver en moyenne au milieu de notre tableau, et donc qu'il faut parcourir de l'ordre de $\frac{n}{2}$ éléments de `tableau`, la complexité en moyenne est de $\mathcal{O}(n/2) = \mathcal{O}(n)$ qui est la même que la complexité maximale.

Ce n'est pas une preuve, mais ça donne une idée de ce qu'il faut prouver.

## intérêt

Pour tout algorithme, on a les inégalités suivantes :

>
>$$\mbox{complexité minimale} \leq \mbox{complexité en moyenne} \leq \mbox{complexité (maximale)}$$
>
>La complexité en moyenne nous indique, pour un modèle de données, si les cas extrêmes (complexité minimale et maximale) arrivent fréquemment ou pas.
>
> La complexité en moyenne nous donne le nombre d'opérations *normal* qu'on aura si on exécute l'algorithme.
{: .note}

Ainsi :

* si la complexité maximale est égale à la complexité en moyenne (comme pour l'algorithme de la [recherche d'un élément d'un tableau]({#exemple-recherche})) alors la complexité maximale arrivera souvent
* si la complexité minimale est égale à la complexité en moyenne (comme pour l'algorithme du [tri rapide]({% link cours/algorithme-code-theorie/algorithme/etude-tris.md %}#tri-rapide)) alors la complexité minimale arrivera souvent
* si les trois complexités sont différentes, les cas minimum et maximum arriveront rarement.

En pratique — si l'algorithme dont on veut calculer les complexités est codé — la complexité en moyenne est très facile à estimer sans aucun calcul :

> Pour estimer la complexité en moyenne d'un algorithme codé, il suffit de mesurer le temps pris par l'algorithme pour s'exécuter pour des données aléatoires et d'en faire la moyenne (c'est un [estimateur sans biais de la moyenne théorique](https://fr.wikipedia.org/wiki/Estimateur_(statistique)#Estimateur_de_la_moyenne_de_Y)).
{: .note}
