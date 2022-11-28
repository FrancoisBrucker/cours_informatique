---
layout: layout/post.njk

title: Algorithmes généraux pour la recherche d'un chemin de poids minimum
authors: 
    - François Brucker

eleventyNavigation:
  key: "Algorithmes généraux pour la recherche d'un chemin de poids minimum"
  parent: "Graphes"
---

<!-- début résumé -->

Chemins de longueur minimum entre deux sommets pour un graphe orienté valué.

<!-- fin résumé -->

La recherche de chemins de poids minimum dans le cas général est plus complexe que le cas simple où la valuation est positive. On ne peut en particulier plus utiliser l'algorithme de Dijkstra car il ne garantit pas de trouver un chemin de longueur minimum.

L'exemple ci-après le montre :

![chemin poids négatif](chemin_poids_negatif.png)

Dijkstra trouvera $xy$ comme chemin de poids minimum entre $x$ et $y$ alors que c'est $xuy$.

## Algorithme de Bellman-Ford

Cas heureux, on peut résoudre les deux problèmes en même temps grâce à :

{% note %}
l'algorithme de [Bellman-Ford](https://fr.wikipedia.org/wiki/Algorithme_de_Bellman-Ford) qui :

* cherche un chemin de poids minimum entre deux sommets dans un graphe orienté valué
* donne un circuit absorbant entre $a$ et $b$ s'il y en a un

En $\mathcal{O}(\vert V \vert \cdot \vert E \vert)$ opérations.
{% endnote %}

La complexité de l'algorithme de Bellman-Ford est plus importante que celle de Dijkstra, évitez donc de l'utiliser si la valuation du graphe est positive.

Finissons cette partie par un exercice qui montre que les cycles absorbants peuvent être utiles ! En particulier pour devenir riche :

{% exercice %}
Soit $D$ un ensemble de devises et $f: D \times D \rightarrow \mathbb{R}^+$ la fonction qui à chaque couple de devises $(u, v)$ associe le taux de change pour convertir la devise $u$ en $v$ : 1 unité de $u$ vaut $f(u, v)$ unités de $v$.

Montrer que :

1. trouver une suite de devises $u_0\dots u_{k-1}$ tel que : $u_0 = u_{k-1}$ et $\Pi_{0 \leq i < k-1}f(u_i, u_{i+1}) > 1$ permet de devenir très riche.
2. on peut ramener ce problème à la recherche d'un circuit absorbant dans un graphe.
{% endexercice %}
{% details "solution" %}

S'il existe une suite telle que demandée alors pour 1 unité de devise $u_0$, en faisant tous les taux de change on obtient au final strictement plus que 1 unité : on génère de l'argent par conversion successive.

$\Pi_{0 \leq i < k-1}f(u_i, u_{i+1}) > 1$ est équivalent à $\sum_{0 \leq i < k-1}-\ln(f(u_i, u_{i+1})) < 0$. Il suffit de considérer le graphe orienté $G=(D, E)$ où $E$ est l'ensemble de couples de devises possibles valués par $-\ln(f(u, v))$.
{% enddetails %}

## Algorithme de Roy-Floyd-Warshall

Dans le cas d'un graphe orienté valué, si l'on cherche tous les chemins de poids minimum entre chaque paire de sommets, on peut utiliser :

{% note %}
L'algorithme de [Roy-Floyd-Warshall](https://fr.wikipedia.org/wiki/Algorithme_de_Floyd-Warshall) qui pour un graphe orienté valué :

* donne tous les chemins de poids minimum entre chaque paire de sommets
* donne un circuit absorbant s'il en existe

La complexité de cet algorithme est en $\mathcal{O}(\vert V \vert ^3)$ opérations.
{% endnote %}

La complexité de l'algorithme de Roy-Floyd-Warshall est plus grande que celle de Bellman-Ford, donc si vous n'avez besoin que de chercher les plus cours chemins ou les cycles absorbants entre 2 sommets il vaut mieux utiliser Bellman-Ford.

## Conclusion

Si vous devez résoudre un problème de recherche de chemin de poids minimum dans une graphe orienté $G$ valué par une fonction $f$ :

* si les poids sont tous positifs, on utilise l’algorithme de Dijkstra que l'on peut implémenter de telle sorte que sa complexité soit $\mathcal{O}(\vert E \vert + \vert V \vert\log_2(\vert V \vert))$
* si l'on cherche un chemin précis, on utilise l'algorithme de Bellman-Ford dont la complexité est $\mathcal{O}(\vert E \vert \cdot \vert V \vert)$
* si l'on cherche tous les chemins, on utilise l'algorithme de Roy-Floyd-Warshall dont la complexité est $\mathcal{O}(\vert V \vert^3)$

Notez que les complexités sont de plus en plus importantes.
