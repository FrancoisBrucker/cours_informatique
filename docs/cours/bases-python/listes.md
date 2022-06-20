---
layout: page
title:  "Bases de python : listes"
authors: 
    - Augustin Agbo-Kpati
    - François Brucker
    - Pascal Préa
---


> <https://docs.python.org/3/tutorial/datastructures.html#more-on-lists>

Les listes sont la structure principale lorsque l'on veut stocker plusieurs objets. La liste est un conteneur dont on peut acceder les éléments un à un.

L'exemple suivant crée une liste de nom `x` qui contient l'entier 1 en 1ère position, l'entier 4 en 2ème position et la chaque de caractères `"12"` en troisième position. On y accède par leur index, qui commence à zéro :

```python
x = [1, 4, "12"]
print(x[0]) # va afficher 1
print(x[2]) # va afficher "12"
```

> Les `[]` permettent d'accéder à un indice donné de la liste.
{: .note}

Les listes, comme les chaines de caractères ont beaucoup de méthodes qui permettent de faire beaucoup d'opérations. Regardez du côté du tutoriel python et de [son complément sur les listes](https://docs.python.org/fr/3/tutorial/datastructures.html#more-on-lists) pour avoir une idées des possibilités.

## Création directe

On peut créer une liste directement:

* Soit en créant une liste vide puis en ajoutant des éléments un à un. `l = []` `l.append(1)`
* Soit en créant la liste déjà pré-remplie. `l = [1, 2, True, "Hello World"]`. Cette liste contient 4 éléments et est **indexée à partir de 0**.

La fonction `len()` permet d'obtenir la longueur de la liste. Sur le dernier exemple, `len(l)` rend `4`.
On peut alors accéder aux éléments de la liste à l'aide d'un indice variant entre `0` et `len(l) - 1`. Ainsi  avec `l[3]` on obtient la chaîne de caractère "Hello World".

## Création à l'aide de range()

La fonction [range](https://docs.python.org/3/library/stdtypes.html#range) permet de créer des listes de nombres.

Attention cependant, range rend un *itérateur* qui ne peut être utilisé tout seul. Il faut écrire `list(range(10))` et non pas juste `range(10)` si on veut la liste de tous les entiers de 0 à 9.

> Créez une liste de tous les multiples de 3 strictement plus grand que 1 jusqu'à 30
{: .a-faire}
{% details solution %}
list(range(3, 31, 3))
{% enddetails %}
{: .a-faire}

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

## Copie d'une sous-liste

On peut copier une partie d'une liste.
Pour **copier la liste l à partir de l'indice i jusqu'à l'indice j avec un pas de k** par exemple : `l[i:j:k]`
Il n'est pas nécessaire de renseigner tous les champs.

> que donne `l[::3]` ou `l[1::5]` pour la liste de tous les multiples de 3 strictement plus grand que 1 jusqu'à 30
{: .a-faire}
{% details solution %}
Dans un terminal :

```text
>>> l = list(range(3, 31, 3))
>>> l[::3]
[3, 12, 21, 30]
>>> l[1::5]
[6, 21]
```

{% enddetails %}
{: .a-faire}
