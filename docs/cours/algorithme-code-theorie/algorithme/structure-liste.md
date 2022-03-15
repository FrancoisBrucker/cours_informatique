---
layout: page
title:  "Structure : liste"
category: cours
---

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [algorithmie]({% link cours/algorithme-code-theorie/algorithme/index.md %}) / [structure : liste]({% link cours/algorithme-code-theorie/algorithme/structure-liste.md %})
>
> **prérequis :**
>
> * [complexité en moyenne]({% link cours/algorithme-code-theorie/algorithme/complexite-moyenne.md %})
>
{: .chemin}

## tableau

On l'a vu, pour un tableau on a les complexité suivantes :

* La complexité dans le cas le pire de la création de la structure : $\mathcal{O}(1)$
* La complexité dans le cas le pire pour trouver l'élément d'indice $i$ : $\mathcal{O}(1)$
* La complexité dans le cas le pire de l'ajout d'un élément à la structure : $\mathcal{O}(1)$ en fin de structure s'il reste de la place, sinon ajout impossible. $\mathcal{O}(n - i) = \mathcal{O}(n)$ à l'emplacement $i$.
* La complexité dans le cas le pire de la suppression d'un élément de la structure :  Pour un tableau $\mathcal{O}(1)$ en fin de structure. $\mathcal{O}(n - i) = \mathcal{O}(n)$ à l'emplacement $i$
* La complexité dans le cas le pire de la suppression de la structure : $\mathcal{O}(1)$

Cette structure est adaptée lorsque l'on ne doit pas supprimer/ajouter des éléments en milieu de structures. Cependant, on doit connaitre *a priori* le nombre maximum d'éléments.

## liste

Les listes de python se comportent de manières différentes. Tout comme les tableaux ce sont des objets pouvant contenir une succession d'autres objets auxquels on peut accéder par un *indice**, mais on peut facilement ajouter/supprimer un nombre infini d'éléments en fin de liste.

> vous devriez déjà savoir manipuler des listes par cœur. Mais comme enseigner, c'est répéter. Je le répète.

### création d'une liste

Pour créer un objet de type liste ne contenant pas d'éléments on peut procéder ainsi : `l = []` ou encore comme ça `l = list()`  (on crée un objet de type liste sans éléments que l'on référence par le nom `l`) .

On peut également créer des listes contenant déjà des éléments.
Le programme suivant par exemple crée une liste de nom l, contenant des objets de valeurs `1`, `2`, et `"toto"`, puis l'affiche :

```python
l = [1, 2, "toto"]
print(l)
```

La liste `l` contient 3 éléments, le premier d'indice 0 est un objet de type entier de valeur 1, le second — d'indice 1 — est un objet de type entier de valeur 2 et le troisième — d'indice 2 — est un objet de type chaine de caractères contenant *toto*. Pour accéder à ces paramètres on pourra utiliser :

* la fonction `len`. L'instruction `len(l)` rendra un objet de type entier contenant comme valeur la longueur de la liste, ici 3.
* l'opérateur de positionnement `[indice]`. `l[i]` rendra l'objet contenu à l'indice  `i` de la liste `l`. Ici les indices iront de 0 à 2 puisque la liste est de longueur 3.

### création d'une liste avec `range`

La fonction `range` crée un générateur (quelque chose qui produit des nombres). Elle peut s'utiliser de trois façons différentes qu'elle soit appelée avec un, deux ou trois paramètres~:

* de `0` à juste avant `paramètre`. Par exemple `range(10)` rendra un générateur de la suite des 10 entiers allant de 0 à 9.
* de `premier paramètre` à juste avant `deuxième paramètre`. Par exemple `range(4, 10)` rendra un générateur de la suite des 6 entiers allant de 4 à 9.
* `premier paramètre` à juste avant `deuxième paramètre`, avec un saut de `troisième paramètre`. Par exemple `range(10, -1, -1)` rendra un générateur de la suite 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0.

Un générateur **n'est pas** une liste. On peut l'utiliser tel quel dans les boucles, mais si on veut créer une liste contenant la suite des nombres produits par le générateur, on le convertit en liste avec le type `list`. Ainsi `list(range(10))` crée une liste `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`.

### suppression d'un élément d'une liste

On peut utiliser la commande `del` pour supprimer un indice d'une liste~: l'instruction `del l[1]` supprime de la liste de nom `l` l'indice 1. L'objet associé au nom `l` est **modifié**, il n'est plus que de longueur 2.

### ajout d'un élément d'une liste

Nous utiliserons essentiellement deux façons d'ajouter des éléments à une liste, tous les deux utilisant des *méthodes* des objets de type liste.

> Une *méthode* est liée à un type d'objet particulier.  Supposons que l'on ait un objet de nom `obj` et une méthode nommée `meth` associée au type de l'objet de nom  `obj`, l'instruction `obj.meth()` exécutera la méthode `meth` pour l'objet `obj`. Si la méthode nécessite des paramètres, ils seront placés à l'intérieur de la parenthèse, séparés par des virgules (par exemple `obj.meth(param1, param2)`).

Chaque type d'objet (liste, entier, chaines de caractères) possède de nombreuses méthodes bien utiles. Avant de se lancer dans de la grande programmation, il est souvent préférable de regarder dans la documentation s'il n'existe pas une méthode qui résout notre problème\dots

La liste des méthodes disponibles pour les objets de type liste est disponible là : <https://docs.python.org/3/tutorial/datastructures.html#more-on-lists>.

Pour ajouter des éléments à une liste, nous utiliserons les méthodes `append` et `insert`.

```python
l.append("a la fin")
l.insert(0, "au debut")
print(l)
```

### copie d'une sous-liste

On peut copier une partie de liste. Ainsi si `l[i]` rend l'objet qui est à l'indice `i` de la liste `l`, `l[i:j]` rendra une **liste** contenant les objets de l'indice `i` à l'indice `j - 1` (cela se comporte comme les paramètre de la fonction `range`).

## structure d'un liste

Une liste peut être implémentée de cette façon :

* on commence par créer un tableau de taille $t = k$, le nombre initial d'éléments étant $n = 0$.
* à chaque ajout d'éléments :
  1. test si $n < t$ :
     * si oui :
       * $n = n + 1$.
     * sinon :
       * on alloue un tableau $2 \timest$ éléments et $t = 2 \times t$
       * on copie les $n$ premiers éléments du tableau initial dans le nouveau tableau et on supprime le tableau initial.
       * $n = n + 1$.
  2. décalage de tous les éléments d'indice supérieur au rang de l'ajout et insertion de l'élément.

## complexités

* La complexité dans le cas le pire de la création de la structure : $\mathcal{O}(1)$
* La complexité dans le cas le pire pour trouver l'élément d'indice $i$ : $\mathcal{O}(1)$
* La complexité dans le cas le pire de l'ajout d'un élément à la structure : $\mathcal{O}(n)$
* La complexité dans le cas le pire de la suppression d'un élément de la structure : $\mathcal{O}(1)$
* La complexité dans le cas le pire de la suppression de la structure : $\mathcal{O}(1)$

### complexité d'ajout de $n$ éléments

Ajouter un élément à la structure peut très mal tomber. Cela peut être juste au moment où l'on doit doubler la taille de la structure. C'est donc de complexité $\mathcal{O}(n)$ opération s'il y avait $n$ élément dans la liste au moment de l'ajout.. Mais ensuite, les $n-1$ suivants ajout vont **forcément** bien se passer et auront tous une complexité de $\mathcal{O}(1)$ opérations.

On a même le résultat suivant :

> L'ajout de $n$ éléments à une liste originellement vide prend $\mathcal{O}(n)$ opérations au maximum
{: .note}
{% details preuve %}
Complexité d'ajout de $n$ éléments à une liste :

* Dans le cas le pire le dernier ajout entraine un doublement de la taille de la structure : un nouveau tableau est créé en $\mathcal{O}(1)$ puis les $n$ éléments de l'ancien tableau sont copiés dans le nouveau en $\mathcal{O}(n)$ opérations
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

On appelle **complexité amortie** d'un algorithme la complexité d'effectuer $n$ fois une opération le tout divisé par $n$. Dans le cas d'une structure simple, la complexité amortie est égale à la complexité puisque l'on fait $n$ fois la même chose mais pour des structure plus complexe comme les listes, lorsque l'on ajoute $n$ fois un élément, cette opération n'est coûteuse qu'un petit nombre de fois.

La complexité amortie d'ajout de $n$ éléments dans une liste est alors $\mathcal{O}(1)$. En effet :
${\mbox{complexité d'ajout de n éléments dans une liste }} / {n} = {\mathcal{O}(n)} / {n} = \mathcal{O}(1)$

Il est donc légitime d'admettre  que la complexité d'insertion d'un élément en fin de liste est en $\mathcal{O}(1)$ :
> On considère que La complexité de l'ajout d'un élément en fin de liste est en $\mathcal{O}(1)$ opérations.
{: .note}

La complexité amortie est un concept avancé. Il ne faut pas le confondre avec la complexité en moyenne, c'est bien $n$ fois la complexité maximale que l'on considère lorsque l'on effectue les opération successivement. C'est un moyen efficace de calculer la complexité d'un algorithme lorsque l'on utilise des structures dont l'opération coûteuse n'est faite qu'un petit nombre de fois.

## Attention

Un piège courant lorsque l'on débute avec les liste en python est d'ajouter un élément en fin de liste avec la commande : `l = l + [x]`. C'est une erreur car la complexité est beaucoup plus importante que si l'on utilise la méthode `append` :

* complexité de `l = l + [x]` : $\mathcal{O}(\mbox{len}(l))$ car on crée une nouvelle liste !
* complexité de : `l.append(x)` : $\mathcal{O}(1)$ car on ajoute à la fin d'une liste déjà existante
