---
layout: layout/post.njk
title: Encodage de graphes
authors: 
    - François Brucker

eleventyNavigation:
  key: "Encodage de graphes"
  parent: "Graphes"
---

<!-- début résumé -->

Comment *encoder* la structure *tableau blanc* (*ie.* *tableau noir* pour les plus nostalgiques d'entres nous) de graphe en une structure informatique permettant d'utiliser les graphes dans des algorithmes.

Nous montrerons quatre encodages, chacun ayant ses avantages et ses inconvénients.

<!-- fin résumé -->

Nous utiliserons pour chacun de ces encodages le graphe orienté avec boucle ci-après comme exemple :

![un graphe orienté](../structure/graphe_oriente_boucle.png)

$G = (V, E)$ où :

* $V$ : est une liste de $n$ sommets
* $E$ : est une liste de $m$ couples de sommets.

{% info %}
Les différentes implémentations sont faites en python.
{% endinfo %}

## Opérations à implémenter

{% note %}
On se restreint ici à la **structure de graphe orienté avec boucle**, un graphe (non orienté) étant un cas particulier.

Nous ne nous intéresserons pas à la structure de multi-graphe, qui s'implémente difficilement autrement que par une liste d'arcs.
{% endnote %}

Lorsque l'on encode une structure en informatique, il faut commencer par définir les opérations que l'on veut pouvoir effectuer. On distingue usuellement des opérations en deux groupes : les opération de construction/suppression et les opérations de manipulation. Pour un graphe :

* construction de la structure :
  * création de la structure
  * ajout d'un sommet
  * ajout d'un arc
* suppression de la structure :
  * destruction de la structure  
  * suppression d'un sommet
  * suppression d'un arc
* manipulation de la structure :
  * savoir si $xy$ est un arc
  * savoir si $x$ est un sommet
  * parcourir tous les voisins d'un sommet
  * parcourir tous les sommets
  * parcourir toutes les arêtes

Il faut ensuite calculer la complexité de chaque opération, qui vont dépendre de l'encodage.

De là :

{% note %}
L'encodage utilisé pour exécuter un algorithme va dépendre des opérations qu'il va effectuer sur la structure.
{% endnote %}

## <span id="liste"></span> Encodage par une liste

Structure simple, on utilise deux listes (une pour les sommets, une pour les arcs).

### <span id="exemple-liste"></span> Construction

```python
  V = ['a', 'b', 'c', 'd', 'e']
  E = [('a', 'b'), ('b', 'b'), ('b', 'c'), ('c', 'd'), 
        ('d', 'a'), ('e', 'd'), ('a', 'e'), ('e', 'a')]
```

* complexité de stockage : $\mathcal{O}(n + m)$
* création de la structure : $\mathcal{O}(n + m)$
* destruction de la structure : $\mathcal{O}(1)$

Pour ajouter et supprimer des arcs, il faut faire attention. En python ajouter ou supprimer un élément dans une liste dépend de l'endroit où on le fait :

{% note "***python***" %}
Ajouter ou supprimer un élément dans une liste prend :

* $\mathcal{O}(1)$ opérations si c'est le dernier élément de la liste
* $\mathcal{O}(\vert L\vert)$ opérations si c'est un élément quelconque (il faut décaler les éléments après l'élément ajouté/supprimé)

On essaiera **toujours** d'ajouter/supprimer des éléments en fin de liste.
{% endnote %}

* ajout d'un sommet : $\mathcal{O}(1)$ car on l'ajoute en fin de liste
* ajout d'un arc : $\mathcal{O}(1)$ car on l'on ajoute en fin de liste
* suppression d'un sommet : $\mathcal{O}(n)$ dans le cas général car on ne sait pas la position du sommet à supprimer dans la liste $V$
* suppression d'un arc : $\mathcal{O}(m)$ dans le cas général car on ne sait pas la position de l'arc à supprimer dans la liste $E$

### <span id="prop-liste"></span> Opérations

Structure de stockage la plus simple. N'est optimisé pour aucune opération spécifique :

* manipulation de la structure :
  * savoir si $xy$ est une arête :
    * implémentation : `('a', 'b') in E`{.language-}
    * complexité : $\mathcal{O}(m)$ il faut parcourir toute la liste $E$
  * savoir si $x$ est un sommet :
    * implémentation : `'a' in V`{.language-}
    * complexité : $\mathcal{O}(n)$ il faut parcourir toute la liste $V$
  * parcourir tous les voisins d'un sommet :
    * implémentation : `[uv for uv in E if uv[1] == 'b']`{.language-} (rend tous les arcs de destination `'b'`{.language-})
    * complexité : $\mathcal{O}(m)$ il faut parcourir toute la liste $E$
  * parcourir tous les sommets : $\mathcal{O}(n)$
  * parcourir toutes les arêtes : $\mathcal{O}(m)$

{% attention %}
Ce n'est pas parce qu'en python on peut écrire `'a' in V`{.language-} que sa complexité est $\mathcal{O}(1)$... Il **faut** parcourir toute la liste `V`{.language-} pour savoir si `'a'`{.language-} y est.
{% endattention %}

## <span id="liste-adjacence"></span> Encodage par une liste d'adjacence

Structure plus complexe que la liste, elle nécessite un re-codage des sommets sous la forme d'entiers pour fonctionner.

### <span id="exemple-liste-adj"></span> Construction

```python
  V = ['a', 'b', 'c', 'd', 'e']
  E = [[1, 4], [1, 2], [3], [0], [3, 0]]
```

Dans $E$ chaque sommet est désigné par son indice dans $V$ et $E[i]$ est le voisinage sortant du sommet $i$.

{% note %}
Pour utiliser cette structure, on considère  que **les sommets sont des entiers** allant de $0$ à $n-1$. La liste $V$ n'est là que pour pouvoir associer plus tard un sommet à autre chose qu'un entier (dépendant de l'application).
{% endnote %}

* complexité de stockage : $\mathcal{O}(n+m)$ ($E$ est de taille $\sum_x\delta^+(x) = m$)
* création de la structure : $\mathcal{O}(n + m)$
* destruction de la structure : $\mathcal{O}(1)$

Ajout/suppression de sommets/arcs :

* ajout d'un sommet : $\mathcal{O}(1)$ il suffit d'ajouter un entier de plus
* ajout d'un arc : $\mathcal{O}(1)$ car on l'on ajoute en fin de liste
* suppression d'un sommet : $\mathcal{O}(n + m)$ car il faut décaler tous les indices des sommets de $V$ et les répercuter dans $E$ (il faut tout re-écrire)
* suppression d'un arc :
  * implémentation : `del E[4].(3)`{.language-} pour supprimer l'arc $(e, d)$
  * complexité : $\mathcal{O}(n)$. Si on veut supprimer l'arc $(i, j)$  il faut supprimer $j$ dans $E[i]$ ce qui prend $\delta^+(i) < n$ opérations (il faut supprimer un élément quelconque d'une liste)

{% info %}
On utilise souvent une variante de cette structure qui utilise des [tableaux associatifs](https://fr.wikipedia.org/wiki/Tableau_associatif) à la place des listes. Voir par exemple [l'implémentation en python](https://www.python.org/doc/essays/graphs/). On troque alors les complexités maximale par des complexités en moyennes, mais on a plus besoin de l'encodage des éléments sous la forme d'entiers.
{% endinfo %}

### <span id="prop-liste-adj"></span> Opérations

L'intérêt de cette encodage est que certaines opérations sont optimisées :

* manipulation de la structure :
  * savoir si $(i, j)$ est un arc :
    * implémentation : `j in E[i]`{.language-}
    * complexité $\mathcal{O}(\delta(i))$
  * savoir si $i$ est un sommet :
    * implémentation : `0 <= i < len(V)`{.language-}
    * complexité : $\mathcal{O}(1)$ c'est un entier.
  * parcourir tous les voisins d'un sommet $i$ :
    * implémentation : `E[i]`{.language-}
    * complexité : $\mathcal{O}(\delta(i))$. On parcourt $E[i]$.
  * parcourir tous les sommets : $\mathcal{O}(n)$
  * parcourir toutes les arêtes :
    * implémentation : `[(i, j) for j in E[i] for i in range(len(V))]`{.language-}
    * complexité : $\mathcal{O}(m)$ : on parcourt tous les $E[i]$ pour $0\leq i < n$

## <span id="mat-adj"></span> Encodage par matrice d'adjacence

Tout comme la liste d'adjacence, cette structure nécessite un re-codage des sommets sous la forme d'entiers pour fonctionner.

### <span id="exemple-mat-adj"></span> Construction

```python
V = ['a', 'b', 'c', 'd', 'e']
E = [[0, 1, 0, 0, 1], 
     [0, 1, 1, 0, 0], 
     [0, 0, 0, 1, 0],
     [1, 0, 0, 0, 0],
     [1, 1, 0, 1, 1]]
```

Dans $E$ chaque sommet est désigné par son indice dans $V$ et $E[i][j]$ vaut $1$ si $(i, j)$ est un arc et 0 sinon.

{% note %}
Pour utiliser cette structure, on considère  que **les sommets sont des entiers** allant de $0$ à $n-1$. La liste $V$ n'est là que pour pouvoir associer plus tard un sommet à autre chose qu'un entier (dépendant de l'application).
{% endnote %}

* complexité de stockage : $\mathcal{O}(n^2)$ ($E$ est matrice carré à $n$ lignes)
* création de la structure : $\mathcal{O}(n + m)$
* destruction de la structure : $\mathcal{O}(1)$

Ajout/suppression de sommets/arcs :

* ajout d'un sommet : $\mathcal{O}(n)$. On ajoute un élément à la fin de chaque ligne de $E$ ($n$ fois $\mathcal{O}(1)$ opérations) et on ajoute une liste de $n+1$ éléments à la fin de $E$.
* ajout d'un arc : $\mathcal{O}(1)$ car on l'on écrit 1 dans une case de la matrice.
* suppression d'un sommet : $\mathcal{O}(n^2)$ car il faut décaler tous les indices des sommets de $V$ et chaque ligne de $E$ et supprimer une ligne de $E$
* suppression d'un arc : $\mathcal{O}(1)$ car on l'on écrit 0 dans une case de la matrice.

{% info %}
Cet encodage permet de traiter les ***graphes valués*** (la valeurs de $E[i][j]$ est la valuation de l'arête $xy$).
{% endinfo %}

### <span id="prop-mat-adj"></span> Opérations

L'intérêt de cette encodage est que le fait de savoir si un arête est présente dans le graphe est optimisé :

* manipulation de la structure :
  * savoir si $(i, j)$ est un arc :
    * implémentation : `E[i][j] == 1`{.language-}
    * complexité : $\mathcal{O}(1)$
  * savoir si $i$ est un sommet :
    * implémentation : `0 <= i < len(V)`{.language-}
    * complexité : $\mathcal{O}(1)$ c'est un entier.
  * parcourir tous les voisins d'un sommet $i$ :
    * implémentation : `[j for j in range(len(V) if E[i](j] == 1]`{.language-}
    * complexité :   $\mathcal{O}(n)$ On parcourt toute la ligne $E[i]$
  * parcourir tous les sommets : $\mathcal{O}(n)$
  * parcourir toutes les arêtes :
    * implémentation : `[(i, j) for i in range(len(V)) for j in range(len(V)) if E[i][j] == 1]`{.language-}
    * complexité : $\mathcal{O}(n^2)$ : on parcourt toute la matrice $E[i][j]$ pour $0\leq i, j < n$

## <span id="dict"></span> Encodage par dictionnaire

C'est le [codage canonique des graphes en python](https://www.python.org/doc/essays/graphs/). Il ressemble fortement au codage par liste d'adjacence, mais ne nécessite pas de ré-encodage des sommets.

### <span id="exemple-dict"></span> Construction

```python
G = {
  'a': {'b', 'e'},
  'b': {'b', 'c'},
  'c': {'d'},
  'd': {'a'},
  'e': {'a', 'd'},
}
```

On utilise à la fois un [dictionnaire](https://docs.python.org/fr/3/tutorial/datastructures.html#dictionaries) pour stocker le voisinage de chaque éléments, lui même codé sous la forme d'un [ensemble](https://docs.python.org/fr/3/tutorial/datastructures.html#sets).

{% note %}
On remplace parfois l'ensemble de voisinage par une liste de voisinage. Cela augmente cependant la complexité de savoir si un élément est un voisin.
{% endnote %}

### <span id="prop-prop"></span> Opérations

L'intérêt de cette encodage est que l'on arrive à obtenir le meilleurs des deux mondes **en moyenne**.

* manipulation de la structure :
  * savoir si $(i, j)$ est un arc :
    * implémentation : `j in G[i]`{.language-}
    * complexité $\mathcal{O}(1)$ en moyenne ($\mathcal{O}(\delta(i))$ au maximum)
  * savoir si $i$ est un sommet :
    * implémentation : `i in G`{.language-}
    * complexité : $\mathcal{O}(1)$ en moyenne ($\mathcal{O}(n)$ au maximum)
  * parcourir tous les voisins d'un sommet $i$ :
    * implémentation : `G[i]`{.language-}
    * complexité : $\mathcal{O}(\delta(i))$. On parcourt $G[i]$.
  * parcourir tous les sommets : $\mathcal{O}(n)$
  * parcourir toutes les arêtes :
    * implémentation : `[(i, j) for j in G[i] for i in G]`{.language-}
    * complexité : $\mathcal{O}(m)$ : on parcourt tous les $E[i]$ pour $0\leq i < n$

## Quand utiliser quoi ?

Selon ce qu'on a besoin de faire, on utilisera plutôt une structure de donnée qu'une autre, voir changera de structure si le passage d'une structure de données à l'autre est simple.

On remarque tout de suite que les trois premières structures sont  mauvaise pour ajouter et/ou supprimer un sommet dans un graphe. On ne pourra donc pas les utiliser dans des applications où le graphe a un nombre variable de sommets au court du temps. Heureusement, ce genre d'application est peu courante. La dernière structure est optimale, mais seulement en moyenne. Si l'on cherche la performance garantie, ce n'est donc pas vers ce genre de structure qu'il faut s'orienter.

### Utilisation de l'encodage en liste

* positif :
  * structure optimale en taille.
  * l'ajout de sommets et d'arêtes est optimale
* négatif :
  * tout le reste

{% exercice %}
Quand utiliser cette structure ?
{% endexercice %}
{% details "solution" %}
Cette structure est optimale pour le stockage, mais très mauvaise pour tout le reste. On l'utilise donc quasi-exclusivement comme moyen de stocker ou de transmettre un graphe.

{% enddetails  %}

### Utilisation de l'encodage par liste d'adjacence

* positif :
  * parcourir tous les voisins d'un sommet
  * ajout d'un sommet
* négatif :
  * savoir si $xy$ est une arête
  * suppression d'arête

{% exercice %}
Quand utiliser cette structure ?
{% endexercice %}
{% details "solution" %}
Optimale pour parcourir un graphe dont les arc sont fixés. On utilisera cette structure lorsque l'algorithme très souvent parcourir les voisinages de sommets d'un graphe fixe.
{% enddetails  %}

### Utilisation de l'encodage par matrice d'adjacence

* positif :
  * savoir si $xy$ est une arête
  * ajout ou suppression d'arêtes
* Négatif :
  * parcourir tous les voisins d'un sommet
  * taille

{% exercice %}
Quand utiliser cette structure ?
{% endexercice %}
{% details "solution" %}

Optimale pour ajouter/supprimer des arc et savoir si un arc est présent ou non. On utilisera cette structure lorsque l'algorithme très souvent modifier les arcs du graphe et/ou savoir si un arc est présent ou non.
{% enddetails  %}

### Utilisation de l'encodage par dictionnaire

* positif :
  * complexité en $\mathcal{O}(1)$ en moyenne pour toutes les opérations
* Négatif :
  * complexité maximale mauvaise

{% exercice %}
Quand utiliser cette structure ?
{% endexercice %}
{% details "solution" %}

Lorsque la complexité maximale la plus faible n'est pas recherchée mais que l'on veut obtenir de bonnes performances dans le cas général.
{% enddetails  %}

{% note %}

Dans la suite de ce cours on utilisera toujours cet encodage par défaut car elle est efficace globalement et facile à implémenter (elle ne nécessite pas de ré-encodage).

{% endnote %}

## Bibliothèques

Il existe plusieurs bibliothèques de gestion de graphes en python. [Cette page](https://wiki.python.org/moin/PythonGraphLibraries) en cite trois, activement maintenues.
