---
layout: page
title:  "Bases de python : listes"
authors: 
    - Augustin Agbo-Kpati
    - François Brucker
    - Pascal Préa
---


> <https://docs.python.org/3/tutorial/datastructures.html#more-on-lists>

## Création directe


* Soit en créant une liste vide puis en ajoutant des éléments un à un. `l = []` `l.append(1)`

La fonction `len()` permet d'obtenir la longueur de la liste. Sur le dernier exemple, `len(l)` rend `4`.
On peut alors accéder aux éléments de la liste à l'aide d'un indice variant entre `0` et `len(l) - 1`. Ainsi  avec `l[3]` on obtient la chaîne de caractère "Hello World".


## Ajout, suppression d'éléments d'une liste

Trois méthode principal de listes :

* `append` ajoute un élément à la fin d'une liste. Par exemple `l.append(3)` ajoute l'entier 3 à la fin d'une liste (si `l`valait `[1, 4]` avant, elle vaudra `[1, 4, 3]` après)
* `insert` ajoute un élément à un index donné d la liste d'une liste. Par exemple `l.inster(1, "X")` insère `"X"` à l'indice 1 (si `l`valait `[1, 4]` avant, elle vaudra `[1, "X", 4]` après)
* `del` supprime l'élément à l'indice de la liste. Par exemple `del l[0]` supprime l'élément d'indice 0 dune liste (si `l` valait `[1, 4]` avant, elle vaudra `[4]` après)

> Attention à `remove`, `extend` ou `pop` qui ne font pas ce qu'on croit qu'elle font. Que font-elles ?
{: .a-faire}
{% details solution %}
Voir la [documentation du tutoriel](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists).
{% enddetails %}
{: .a-faire}

