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
---

<!-- début résumé -->

Mise en œuvre de la structure de liste, qui est une amélioration du de la structure de tableau.

<!-- end résumé -->

## Tableau

On l'a vu, pour un tableau on a les complexité suivantes :

* La complexité dans le cas le pire de la création de la structure : $\mathcal{O}(1)$
* La complexité dans le cas le pire pour trouver l'élément d'indice $i$ : $\mathcal{O}(1)$
* La complexité dans le cas le pire de l'ajout d'un élément à la structure : $\mathcal{O}(1)$ en fin de structure s'il reste de la place, sinon ajout impossible. $\mathcal{O}(n - i) = \mathcal{O}(n)$ à l'emplacement $i$.
* La complexité dans le cas le pire de la suppression d'un élément de la structure :  Pour un tableau $\mathcal{O}(1)$ en fin de structure. $\mathcal{O}(n - i) = \mathcal{O}(n)$ à l'emplacement $i$
* La complexité dans le cas le pire de la suppression de la structure : $\mathcal{O}(1)$

Cette structure est adaptée lorsque l'on ne doit pas supprimer/ajouter des éléments en milieu de structures. Cependant, on doit connaître *a priori* le nombre maximum d'éléments.

## Liste

Les listes de python se comportent de manières différentes. Tout comme les tableaux ce sont des objets pouvant contenir une succession d'autres objets auxquels on peut accéder par un *indice**, mais on peut facilement ajouter/supprimer un nombre infini d'éléments en fin de liste.

{% info %}
Vous devriez savoir manipuler des listes comme personne. Mais si vous avez besoin d'une piqûre de rappel, n'hésitez pas à consulter la partie [listes]({{ "/cours/coder-en-python/listes"  }}) du cours sur les bases du code.
{% endinfo %}

## Structure d'un liste

Une liste peut être implémentée de cette façon :

* on commence par créer un tableau de taille $t = k$, le nombre initial d'éléments étant $n = 0$.
* à chaque ajout d'éléments :
  1. test si $n < t$ :
     * si oui :
       * $n = n + 1$.
     * sinon :
       * on alloue un tableau $2 \times t$ éléments et $t = 2 \times t$
       * on copie les $n$ premiers éléments du tableau initial dans le nouveau tableau et on supprime le tableau initial.
       * $n = n + 1$.
  2. décalage de tous les éléments d'indice supérieur au rang de l'ajout et insertion de l'élément.

## Complexités

* La complexité dans le cas le pire de la création de la structure : $\mathcal{O}(1)$
* La complexité dans le cas le pire pour trouver l'élément d'indice $i$ : $\mathcal{O}(1)$
* La complexité dans le cas le pire de l'ajout d'un élément à la structure : $\mathcal{O}(n)$
* La complexité dans le cas le pire de la suppression d'un élément de la structure : $\mathcal{O}(1)$
* La complexité dans le cas le pire de la suppression de la structure : $\mathcal{O}(1)$

### complexité d'ajout de $n$ éléments

Ajouter un élément à la structure peut très mal tomber. Cela peut être juste au moment où l'on doit doubler la taille de la structure. C'est donc de complexité $\mathcal{O}(n)$ opération s'il y avait $n$ élément dans la liste au moment de l'ajout.. Mais ensuite, les $n-1$ suivants ajout vont **forcément** bien se passer et auront tous une complexité de $\mathcal{O}(1)$ opérations.

On a même le résultat suivant :

{% note %}
L'ajout de $n$ éléments à une liste originellement vide prend $\mathcal{O}(n)$ opérations au maximum
{% endnote %}
{% details "preuve" %}
Complexité d'ajout de $n$ éléments à une liste :

* Dans le cas le pire le dernier ajout entraîne un doublement de la taille de la structure : un nouveau tableau est créé en $\mathcal{O}(1)$ puis les $n$ éléments de l'ancien tableau sont copiés dans le nouveau en $\mathcal{O}(n)$ opérations
* Le précédent tableau  était de taille $n-1$ et a nécessité $\mathcal{O}(n)$ opérations pour être créé puis rempli (recopie de $n/2$ anciens éléments puis insertion de $n/2$ nouveaux éléments).
* Le tableau encore d'avant d'avant était de taille $n/2$ et son remplissage a pris $\mathcal{O}(n/2)$ opérations (recopie de $n/4$ anciens éléments puis insertion de $n/4$ nouveaux éléments)
* Le tableau encore encore d'avant d'avant était de taille $n/4$ et son remplissage a pris $\mathcal{O}(n/4)$ opérations
* ...
* le $i$ème tableau précédent était de taille $n / {2^i}$ et son remplissage a pris $\mathcal{O}(n/{2^i})$ opérations
* ...
* le $\log_2(n)$ tableau précédent était de taille $n / {2^{\log_2(n}} = 1$ et son remplissage a pris un nombre d'opérations de $\mathcal{O}(n / {2^{\log_2(n}}) = \mathcal{O}(1)$ opérations

La complexité totale est donc de :

$$
C(n) = \mathcal{O}(n + n + \frac{n}{2} + \frac{n}{4} + \frac{n}{8} + \dots + 1) = \mathcal{O}(n + \sum_{i=0}^{\log_2(n)}\frac{n}{2^i}) = \mathcal{O}(n(1+\sum_{i=0}^{\log_2(n)}\frac{1}{2^i}))
$$

[Comme](https://fr.wikipedia.org/wiki/1/2_%2B_1/4_%2B_1/8_%2B_1/16_%2B_%E2%8B%AF) $\sum_{i=0}^{+\infty}\frac{1}{2^i} = 1$, on a :

$$
(1+\sum_{i=0}^{\log_2(n)}\frac{1}{2^i})) \leq (1+\sum_{i=0}^{+\infty}\frac{1}{2^i})) \leq 2
$$

Et donc : $C(n) = \mathcal{O}(n)$

{% enddetails %}

Comme la complexité d'ajout d'un élément à une liste n'est pas constante, il nous faut un nouvel outil pour en appréhender sa complexité :

{% note "**Définition** "%}
On appelle ***complexité amortie*** d'un algorithme la complexité d'effectuer $n$ fois une opération le tout divisé par $n$.
{% endnote %}

Dans le cas d'une structure simple, la complexité amortie est égale à la complexité puisque l'on fait $n$ fois la même chose mais pour des structure plus complexe comme les listes, lorsque l'on ajoute $n$ fois un élément, cette opération n'est coûteuse qu'un petit nombre de fois.

La complexité amortie d'ajout de $n$ éléments dans une liste est alors $\mathcal{O}(1)$. En effet :
${\mbox{complexité d'ajout de n éléments dans une liste }} / {n} = {\mathcal{O}(n)} / {n} = \mathcal{O}(1)$

Il est donc légitime d'admettre  que la complexité d'insertion d'un élément en fin de liste est en $\mathcal{O}(1)$ :

{% note %}
On considère que La complexité de l'ajout d'un élément en fin de liste est en $\mathcal{O}(1)$ opérations.
{% endnote %}

La complexité amortie est un concept avancé. Il ne faut pas le confondre avec la complexité en moyenne, c'est bien $n$ fois la complexité maximale que l'on considère lorsque l'on effectue les opération successivement. C'est un moyen efficace de calculer la complexité d'un algorithme lorsque l'on utilise des structures dont l'opération coûteuse n'est faite qu'un petit nombre de fois.

## Attention

Un piège courant lorsque l'on débute avec les liste en python est d'ajouter un élément en fin de liste avec la commande : `l = l + [x]`{.language-}. C'est une erreur car la complexité est beaucoup plus importante que si l'on utilise la méthode `append`{.language-} :

* complexité de `l = l + [x]`{.language-} : $\mathcal{O}(\mbox{len}(l))$ car on crée une nouvelle liste !
* complexité de : `l.append(x)`{.language-} : $\mathcal{O}(1)$ car on ajoute à la fin d'une liste déjà existante
