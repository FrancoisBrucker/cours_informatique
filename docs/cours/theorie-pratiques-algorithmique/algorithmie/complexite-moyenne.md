---
layout: page
title:  "Complexité en moyenne"
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [algorithmie]({% link cours/theorie-pratiques-algorithmique/algorithmie/index.md %}) / [complexité en moyenne]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-moyenne.md %})
>
> prérequis :
>
>* [complexité max/min]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-max-min.md %})
{: .chemin}

Lorsque le nombre d'opérations d'un algorithme dépend non seulement de la taille de ses entrées mais également de la structure de celles-ci, on a coutume de calculer sa complexité en moyenne :

> La **complexité en moyenne** d'un algorithme est le nombre moyen d'opérations nécessaires pour se terminer par rapport à une taille fixée de ses entrées.
{: .note}

Cette mesure est très utile en pratique car si la complexité maximale et minimale d'un algorithme est très différente, cela permet de savoir le nombre d'opérations espéré pour un tableau quelconque de taille donné.

## calcul de la complexité en moyenne

La complexité en moyenne d'un algorithme dépend des entrées de celui-ci et plus précisément du nombre de fois où une entrée donnée peut être choisie. Pour pouvoir la calculer de façon formelle, il faut connaitre ainsi le modèle probabiliste associé aux données :

> La **complexité en moyenne** de l'algorithme $A$ pour une entrée de taille $n$ est :
>
> $$C = \sum_{e \in \mathcal{E}} p_e \cdot C(e)$$
>
> Avec $\mathcal{E}$ l'ensemble des données de taille $n$, $p_e$ la probabilité d'exécuter l'algorithme avec l'entrée $e \in \mathcal{E}$ et $C(e)$ le nombre d'opérations utilisé par l'algorithme pour se terminer avec l'entrée $e$.
>
{: .note}

Si l'on a pas de modèle a priori, on considérera que chaque donnée est équiprobable : chaque entrée a la même probabilité d'être choisie, $p_e = \frac{1}{\mid \mathcal{E} \mid}$.

## exemple de la recherche d'un élément dans un tableau {#exemple-recherche}

Reprenons l'exemple de la [recherche d'un élément d'un un tableau]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-max-min.md %}#exemple-recherche) :

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

La complexité en moyenne est calculée en considérant le nombre d'opérations moyenne pris pour toutes les entrées d'une taille fixée.

Pour une entrée donnée, la complexité dépend de l'endroit où se trouve `valeur` dans le `tableau` : si `valeur` est à la position $i$ du tableau, il faudra $\mathcal{O}(i)$ opérations et si `valeur` n'est pas dans le tableau, il faudra $\mathcal{O}(n)$ opérations (avec $n$ la taille du tableau).

Si l'on note $p_i$  la probabilité que valeur soit à la position $i$ `tableau` et $p_{n}$ la probabilité qu'elle ne soit pas dans le tableau, la complexité moyenne de l'algorithme s'écrit :

$$C = \sum_{i=0}^{i = n} (p_i \cdot \mathcal{O}(i))$$

Pour pouvoir la calculer effectivement, il faut connaitre les $p_i$. Comme on a pas de modèle a priori, on va considérer que chaque tableau de taille $n$ à la même probabilité d'être choisie et donc que la position de `valeur` dans tableau est équiprobable : $p_i = \frac{1}{n + 1}$ :

$$C =  (\sum_{i=0}^{i = n}\frac{1}{n + 1} \mathcal{O}(i)) = \mathcal{O}(\frac{\sum_{i=0}^{i = n}(i)}{n +1})$$

Comme $\sum_{i=0}^{i = n}(i) = \frac{(n + 1)(n)}{2}$ on en déduit que :

$$C = \mathcal{O}(\frac{n}{2}) = \mathcal{O(n)}$$

Pour aller plus vite, on aurait pu dire que si notre modèle est équiprobable, `valeur` va se trouver en moyenne au milieu de notre tableau, et donc qu'il faut parcourir de l'ordre de $\frac{n}{2}$ éléments de `tableau`, la complexité en moyenne est de $\mathcal{O}(n/2) = \mathcal{O}(n)$ qui est la même que la complexité maximale.

> En moyenne la complexité l'algorithme `est_dans_tableau` est la même que la complexité maximale. La complexité minimale est très rarement atteinte.
{: .note}

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
* si la complexité minimale est égale à la complexité en moyenne (comme pour l'algorithme du [tri rapide]({% link cours/theorie-pratiques-algorithmique/algorithmie/etude-tris.md %}#tri-rapide)) alors la complexité minimale arrivera souvent
* si les trois complexités sont différentes, les cas minimum et maximum arriveront rarement.

En pratique — si l'algorithme dont on veut calculer les complexités est codé — la complexité en moyenne est très facile à estimer sans aucun calcul :

> Pour estimer la complexité en moyenne d'un algorithme codé, il suffit de mesurer le temps pris par l'algorithme pour s'exécuter pour des données aléatoires et d'en faire la moyenne (c'est un [estimateur sans biais de la moyenne théorique](https://fr.wikipedia.org/wiki/Estimateur_(statistique)#Estimateur_de_la_moyenne_de_Y)).
{: .note}
