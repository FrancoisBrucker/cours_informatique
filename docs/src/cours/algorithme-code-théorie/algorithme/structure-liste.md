---
layout: layout/post.njk 
title: "Structure : liste"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

prerequis:
    - "../complexité-moyenne/"
    - "../structure-tableau/"
---

<!-- début résumé -->

Mise en œuvre de la structure de liste, qui est une amélioration du de la structure de tableau.

<!-- end résumé -->

Une liste est une amélioration de la [structure de données tableau](../structure-tableau) qui, on l'a vu, possède les complexité de manipulation suivantes :

* la complexité dans le cas le pire de la création de la structure : $\mathcal{O}(1)$
* la complexité dans le cas le pire pour trouver l'élément d'indice $i$ : $\mathcal{O}(1)$
* la complexité dans le cas le pire de la suppression de la structure : $\mathcal{O}(1)$
* impossibilité de modifier la structure sans la recopier en $\mathcal{O}(n)$

Cette structure est adaptée lorsque l'on ne doit pas supprimer/ajouter des éléments en milieu de structures. Cependant, on doit connaître *a priori* le nombre maximum d'éléments.

## Liste

Les listes de python se comportent de manières différentes. Tout comme les tableaux ce sont des objets pouvant contenir une succession d'autres objets auxquels on peut accéder par un *indice**, mais on peut facilement ajouter/supprimer un nombre infini d'éléments en fin de liste.

{% info %}
Vous devriez savoir manipuler des listes comme personne. Mais si vous avez besoin d'une piqûre de rappel, n'hésitez pas à consulter la partie [listes]({{ "/cours/coder-en-python/listes"  }}) du cours sur les bases du code.
{% endinfo %}

## Structure d'un liste

En simplifiant un peu, une liste $t$ est une structure composée trois champs :

* un entier $n$ donnant le nombre d'élément actuellement dans la structure
* un entier $m$
* un tableau $t$ à $m$ éléments

Le $i$ème élément de la liste $l$, noté $l[i]$ est $t[i]$, le $i$ème élément du tableau contenu dans sa structure.

### Création

A la création de la liste, on affecte $m = m_0$ cases mémoires avec $m_0$ une constante ni trop petite, ni trop grande. 

### Ajout d'un élément

L'astuce des listes opère à chaque ajout d'un nouvel élément en fin de liste où l'on effectue l'algorithme suivant :

```python
si n ≥ m:
    on alloue un tableau t2 à 2 * m éléments et on recopie les m élément de t dans t2
    t = t2
    m = 2 * m
n = n + 1
```

Si l'on insère un élément au milieu de la liste, on commence par faire l'algorithme précédent pour ajouter une case au tableau, puis on décale d'une case vers la droite les éléments à partir du i ème et enfin on affecte le nouvel élément à $t[i]$.

### Suppression d'un élément

Pour supprimer le dernier élément d'une liste on n'a qu'une opération à faire :

```python
n = n-1
```

Si l'on supprime un élément au milieu de la liste, on commence par décaler d'une case vers la droite les éléments à partir du i+1 ème et enfin on fait $n=n-1$

## Complexités

Dans le cas le pire :

* La complexité dans le cas le pire de la création de la structure : $\mathcal{O}(1)$
* La complexité dans le cas le pire pour trouver l'élément d'indice $i$ : $\mathcal{O}(1)$
* La complexité dans le cas le pire de l'ajout d'un élément à la fin de la structure : $\mathcal{O}(n)$
* La complexité dans le cas le pire de la suppression d'un élément de la structure : $\mathcal{O}(1)$
* La complexité dans le cas le pire de la suppression du dernier élément de la structure : $\mathcal{O}(1)$

La seule complexité maximale non constante et l'ajout d'un élément à la fin de la structure. Cependant sa complexité dans le meilleurs des cas est en $\mathcal{O}(1)$. De plus, la complexité dans le cas le pire n'arrive que très rarement. Calculons ça précisément en ajoutant successivement $N$ éléments à la structure.

### Complexité d'ajout de $N$ éléments à la fin de la structure

Ajouter un élément à la fin de la structure peut très mal tomber : cela peut être juste au moment où l'on doit doubler la taille de la structure. C'est donc de complexité $\mathcal{O}(n)$ opérations s'il y avait $n$ élément dans la liste au moment de l'ajout... Mais ensuite, les $n-1$ suivants ajout vont **forcément** bien se passer et auront tous une complexité de $\mathcal{O}(1)$ opérations.

On a le résultat suivant :

<div id="preuve-liste-ajout"></div>
{% note %}
L'ajout de $N$ éléments à une liste prend $\mathcal{O}(N)$ opérations au maximum
{% endnote %}
{% details "preuve" %}

Commençons par calculer la complexité de l'ajout de $N^\star$ éléments à une liste initialement vide :

* Dans le cas le pire le dernier ajout entraîne un doublement de la taille de la structure : un nouveau tableau est créé en $\mathcal{O}(1)$ puis les $N^\star$ éléments de l'ancien tableau sont copiés dans le nouveau en $\mathcal{O}(N^\star)$ opérations
* Le précédent tableau  était de taille $N^\star-1$ et a nécessité $\mathcal{O}(N^\star)$ opérations pour être créé puis rempli (recopie de $\frac{N^\star}{2}$ anciens éléments puis insertion de $\frac{N^\star}{2}$ nouveaux éléments).
* Le tableau encore d'avant d'avant était de taille $n/2$ et son remplissage a pris $\mathcal{O}(\frac{N^\star}{2})$ opérations (recopie de $\frac{N^\star}{4}$ anciens éléments puis insertion de $\frac{N^\star}{4}$ nouveaux éléments)
* Le tableau encore encore d'avant d'avant était de taille $\frac{N^\star}{4}$ et son remplissage a pris $\mathcal{O}(\frac{N^\star}{4})$ opérations
* ...
* le $i$ème tableau précédent était de taille $\frac{N^\star}{2^i}$ et son remplissage a pris $\mathcal{O}(\frac{N^\star}{2^i})$ opérations
* ...
* le $\log_2(N^\star)$ tableau précédent était de taille $\frac{N^\star}{2^{\log_2(n}} = 1$ et son remplissage a pris un nombre d'opérations de $\mathcal{O}(\frac{N^\star}{2^{\log_2(n}}) = \mathcal{O}(1)$ opérations

La complexité totale du remplissage de la liste en parant de la liste vide est donc de :

$$
C(N^\star) = \mathcal{O}(N^\star + N^\star + \frac{N^\star}{2} + \frac{N^\star}{4} + \frac{N^\star}{8} + \dots + 1) = \mathcal{O}(N^\star + \sum_{i=0}^{\log_2(N^\star)}\frac{N^\star}{2^i}) = \mathcal{O}(N^\star(1+\sum_{i=0}^{\log_2(N^\star)}\frac{1}{2^i}))
$$

[Comme](https://fr.wikipedia.org/wiki/1/2_%2B_1/4_%2B_1/8_%2B_1/16_%2B_%E2%8B%AF) $\sum_{i=0}^{+\infty}\frac{1}{2^i} = 1$, on a :

$$
(1+\sum_{i=0}^{\log_2(N^\star)}\frac{1}{2^i})) \leq (1+\sum_{i=0}^{+\infty}\frac{1}{2^i})) \leq 2
$$

Et donc : $C(N^\star) = \mathcal{O}(N^\star)$

On est pas parti de la liste vide mais d'une liste à $M$ éléments, on cherche donc à estimer la complexité : $C(N + M) - C(M) = \mathcal{O}(N + M - M) = \mathcal{O}(N)$

{% enddetails %}

Comme la complexité d'ajout d'un élément à une liste n'est pas constante, on utilise la [complexité amortie](../complexité-amortie) pour donner sa complexité :

{% note %}
La complexité amortie de l'ajout de $N$ élément en fin de liste est en $\mathcal{O}(1)$ opérations.
{% endnote %}

La structure de liste est un cas *simple* où la complexité amortie est très utile car elle permet de mieux estimer la complexité : lorsque l'on ajoute $n$ fois un élément, cette opération n'est coûteuse qu'un petit nombre de fois :

{% note %}
Dans nos calculs de complexité on pourra utiliser $\mathcal{O}(1)$ comme complexité d'ajout d'un élément en fin de liste sans erreur puisque c'est sa complexité amortie.

De plus, l'implémentation des liste fait qu'au pire, on surestime le nombre d'opérations d'un facteur 2.
{% endnote %}

### Complexités de suppression de $N$ éléments à la fin de la structure

> TBD le faire.

## Attention

Un piège courant lorsque l'on débute avec les liste en python est d'ajouter un élément en fin de liste avec la commande : `l = l + [x]`{.language-}. C'est une erreur car la complexité est beaucoup plus importante que si l'on utilise la méthode `append`{.language-} :

* complexité de `l = l + [x]`{.language-} : $\mathcal{O}(\mbox{len}(l))$ car on crée une nouvelle liste !
* complexité de : `l.append(x)`{.language-} : $\mathcal{O}(1)$ car on ajoute à la fin d'une liste déjà existante
