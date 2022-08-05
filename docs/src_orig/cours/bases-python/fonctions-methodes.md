---
layout: page
title:  "Bases de python : fonctions et méthodes"
authors: 
    - François Brucker
    - Pierre Brucker
---


> [bases de python]({% link cours/bases-python/index.md %}) / [fonctions et méthodes]({% link cours/bases-python/fonctions-methodes.md %})
{: .chemin}

Les fonctions et les méthodes sont des moyens d'effectuer des opérations sur les objets ou de créer de nouveaux objets. La puissance d'un langage de programmation vient aussi du fait de ses nombreuses fonctions et méthodes mises à la dispositions des utilisateurs.

## fonctions

Une fonction est un type d'objet pouvant être exécuté. Par exemple la fonction `print`.

C'est un objet :

```python
>>> type(print)
<class 'builtin_function_or_method'>
```

On *exécute* l'objet en faisant suivre son nom de parenthèses :

```python
>>> print()

```

L'exécution de la fonction `print` à produit un retour à la ligne.

De nombreuses fonctions peuvent être exécutées avec des *paramètres* qui sont placées les un à la suite des autres entre les parenthèses et séparés par des virgules :

```python
>>> print("coucou", "les gens", "!")
coucou les gens !
```

L'exécution de la fonction `print` avec les trois paramètres `"coucou"`, `"les gens"` et `"!"` affichera à l'écran les 3 paramètres séparé par un caractère ` `, puis ira à la ligne.

Toutes les fonctions de python sont documentées. On peut y accéder :

* via le site de python. L'aide de la fonction `print` est là : <https://docs.python.org/fr/3/library/functions.html#print>
* en console en utilisant la fonction `help` : `help(print)` donne l'aide de `print`

### paramètres d'une fonction

En regardant l'aide de la fonction `print` :

```text
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

On remarque que les premiers paramètres sont sans noms (value, ...) puis les paramètres ont des noms (`sep`, `end`, `file`, `flush`) suivi d'une valeur. Ce sont des paramètres qui ont une valeur par défaut (par défaut `sep` vaut `" "`).

> Les paramètres sans valeurs par défaut sont obligatoires lorsque l'on appelle une fonction, les paramètres ayant une valeur par défaut sont optionnels.
{: .note}

On cependant bien sur utiliser, en le nommant, un paramètre ayant une valeur par défaut :

```python
>>> print("coucou", "les gens", "!", sep="***")
coucou***les gens***!
```

### fonction usuelles

Les fonctions natives de python sont décrite ici : <https://docs.python.org/fr/3/library/functions.html>. Certaines sont plus utiles que d'autres. Nous allons en citer certaines.

#### print

<https://docs.python.org/fr/3/library/functions.html#print>

Affiche à l'écran ses paramètres.

#### type

<https://docs.python.org/fr/3/library/functions.html#type>

Donne le type d'un objet.

> On l'a utilisée dans la partie [objets types et types d'objets]({% link cours/bases-python/objets-types.md %}).

#### len

<https://docs.python.org/fr/3/library/functions.html#len>

Rend le nombre d'éléments d'un conteneur (liste ou chaîne de caractères).

> Quel est le nombre de caractères du mot "anticonstitutionnellement" ?
{: .a-faire}
{% details %}

```python
>>> len("anticonstitutionnellement")
25
```

{% enddetails %}

#### nom de classes

`int`, `float`,  `complex`, `str`, `bool` et `list` permettent de créer des objets du nom du type.

On a déjà vu cette possibilité dans la partie [objets types et types d'objets]({% link cours/bases-python/objets-types.md %}), c'est très utile pour changer un objet de classe. Mais utilisons ce qu'on a vu maintenant pour aller plus loin :

> Créez le nombre complexe $1+2i$
{: .a-faire}
{% details %}

L'aide de `complex` : <https://docs.python.org/fr/3/library/functions.html#complex>, nous indique l'on peut créer notre objet comme ça :

```python
>>> complex(1, 2)
(1+2j)
```

Remarquez que les deux paramètres de la fonction sont nommées : `real` et `imag`. On peut donc tout aussi bien écrire :

```python
>>> complex(real=1, imag=2)
(1+2j)
```

Voir, puisque les éléments sont nommées :

```python
>>> complex(imag=2, real=1)
(1+2j)
```

{% enddetails %}

> Créez une copie de la liste `x = [1, 2, 13]`
{: .a-faire}
{% details %}

```python
>>> x = [1, 2, 13]
>>> y = list(x)
```

Il est pratique de copier une liste car ensuite on peut modifier une liste sans peur des effets de bords :

```python
>>> y[1] = 42
>>> x
[1, 2, 13]
>>> y
[1, 42, 13]
```

Alors que :

```python
>>> x = [1, 2, 13]
>>> y = x
>>> y[1] = 42
>>> x
[1, 42, 13]
>>> y
[1, 42, 13]
```

{% enddetails %}

> En utilisant [int()](https://docs.python.org/fr/3/library/functions.html#int) qui crée des entiers, trouvez la représentation décimale du nombre binaire : 1001100011
{: .a-faire}
{% details solution %}

On utilise le paramètre base de la classe `int` :

```python
>>> int("1001100011", base=2)
611
```

{% enddetails %}

Allez, un dernier pour la route :

> En utilisant le fait que la fonction `len(chaine de caractère)` donne le nombre de caractères de la chaîne (par exemple `len("abc")` rend `3`), et que l'exposant eb python s'écrit `**` (par exemple `2**8` rend `256`) donnez le nombre de chiffre du 27ème [nombre de Mersenne premier](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier).
{: .a-faire}
{% details solution %}

```python
>>> len(str(2 ** 44497 - 1))
13395
```

{% enddetails %}

#### input

<https://docs.python.org/fr/3/library/functions.html#input>

Permet de demander une chaine de caractère à un utilisateur. Par exemple :

```python
>>> x = input()
23
>>> x
'23'
```

On demande à l'utilisateur de taper quelque chose puis d'appuyer sur la touche entrée. Ce qu'à taper l'utilisateur est rendu sous la forme d'une **chaîne de caractère**.

> Tout ce qui vient de l'utilisateur est une **chaîne de caractère**. Si l'on veut que ce soit un nombre par exemple, il faut le convertir. Comme par exemple : `i = int(input())` qui converti en entier le résultat de la fonction `input`.
{: .attention}

#### range

[range](https://docs.python.org/fr/3/library/stdtypes.html#ranges) est une fonction particulière, elle permet de créer, en combinaison avec `list` des listes.

> On ne crée **pas** de liste directement avec `range`.
{: .a-faire}

Par exemple :

```python
>>> list(range(5))
[0, 1, 2, 3, 4]
```

Crée une liste avec les 5 premiers entiers.

Mais :

```python
>>> range(5)
range(0, 5)
```

N'est **pas** une liste.

La fonction range peut être utilisée de plusieurs manières :

* avec un paramètre : va créer des entiers allant de 0 à *juste avant* le premier paramètre. Exemple `list(range(5))` rend la liste `[0, 1, 2, 3, 4]`
* avec deux paramètres : va créer des entiers allant du premier paramètre  à *juste avant* le second paramètre. Exemple `list(range(2, 5))` rend la liste `[2, 3, 4]`
* avec trois paramètres : va créer des entiers allant du premier paramètre  à *juste avant* le second paramètre touts les troisièmes paramètres. Exemple `list(range(1, 12, 3))` rend la liste `[1, 4, 7, 10]`

## méthodes

Les méthodes sont un autre moyen d'agir sur un objet. On les utilise de cette façon :

```pyhton
objet.methode(paramètre 1, paramètre 2, ..., paramètre n)
```

On applique `méthode` à `objet` en utilisant les `paramètres` de la méthode.

> Une méthode ne s'utilise **jamais** seule. Elle s'applique à ce qu'il y a à gauche d'elle.
{: .attention}

Prenez le temps de regarder les différentes méthodes des classes de base de python. Souvent elle vous permettent de faire rapidement une opération compliquée. C'est en particulier vrai pour les chaines de caractères et les listes.

### méthodes des chaines de caractères

Chaque classe vient avec des méthodes. Si les nombre et booléens ont peu de méthode, les chaines de caractères par exemple en ont [tout un tas](https://docs.python.org/fr/3/library/stdtypes.html#string-methods).

Essayons de les apprendre avec ces petits exercices :

> Avec le mot `"choucroute garnie"` :
>
> * combien y a-t-il de "ou" ?
> * quel est l'indice du premier "e" ?
> * quel est l'indice du dernier "e" ?
{: .a-faire}
{% details %}

```python
>>> mot.count("ou")
2
>>> mot.index("e")
9
>>> mot.rindex("e")
16
```

{% enddetails %}

> Transformez le 27ème [nombre de Mersenne premier](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier) en une chaîne de caractère
{: .a-faire}
{% details solution %}

Dans un interpréteur :

```python
>>> x = str(2 ** 44497 - 1)
```

{% enddetails %}

> En utilisant la méthode [count](https://docs.python.org/fr/3/library/stdtypes.html#str.count), comptez le nombre de 0 du 27ème [nombre de Mersenne premier](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier).
{: .a-faire}
{% details solution %}

Dans un interpréteur :

```python
>>> x.count("0")
1332
```

{% enddetails %}

> En utilisant la méthode [replace](https://docs.python.org/fr/3/library/stdtypes.html#str.replace), changez les 2 en 7 dans le nombre de 0 du 27ème [nombre de Mersenne premier](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier).
{: .a-faire}
{% details solution %}

Dans un interpréteur :

```python
>>> y = int(x.replace("2", "7"))
```

{% enddetails %}

On peut chainer les méthodes, la sortie d'une méthode devenant l'entrée de la prochaine. Par exemple, avec 2 méthodes :

```python
objet.methode_1().methode_2()
```

Signifie que méthode2() est appliquée à l'objet résultat de `objet.methode1()`

Et avec n méthodes :

```python
objet.methode1().methode2(). ... .methode_n()
```

Signifie que `methode_n()` est appliquée au résultat de `objet.methode_1(). ... .methode_n-1()`

> Que fait :
>
> ```python
> str(2 ** 44497 - 1).replace("2","x").replace("7","2").replace("x","7")
> ```
>
{: .a-faire}
{% details solution %}

Il est aisé de comprendre ce que ça fait en procédant de droite à gauche :

1. `replace("x","7")` est appliqué à ce qui est à sa gauche donc `str(2 ** 44497 - 1).replace("2","x").replace("7","2")`
2. `replace("7","2")` est appliqué à ce qui est à sa gauche donc `str(2 ** 44497 - 1).replace("2","x")`
3. `replace("2","x")` est appliqué à ce qui est à sa gauche donc `str(2 ** 44497 - 1)`

En remontant les opérations précédentes :

1. le résultat de `str(2 ** 44497 - 1)`  sera une chaine de caractère représentant le 27ème nombre premier de Mersenne
2. `str(2 ** 44497 - 1).replace("2","x")` on a remplacé les 2 par des "x" dans la chaine précédente
3. `str(2 ** 44497 - 1).replace("2","x").replace("7","2")` on a remplacé les 7 par des 2 de la chaine précédente
4. `str(2 ** 44497 - 1).replace("2","x").replace("7","2").replace("x","7")` on a remplacé les "x" par des 2 dans la chaine précédente

On a donc au final échangé les 2 et les 7 du 27ème nombre premier de Mersenne

{% enddetails %}

### méthodes des listes

La page <https://docs.python.org/fr/3/tutorial/datastructures.html#more-on-lists> vous montre les nombreuses méthodes des listes. Elles permettent de les utiliser très efficacement.

Par exemple pour ajouter ou supprimer des éléments d'une liste :

* `append` ajoute un élément à la fin d'une liste. Par exemple `l.append(3)` ajoute l'entier 3 à la fin d'une liste (si `l`valait `[1, 4]` avant, elle vaudra `[1, 4, 3]` après)
* `insert` ajoute un élément à un index donné d la liste d'une liste. Par exemple `l.inster(1, "X")` insère `"X"` à l'indice 1 (si `l`valait `[1, 4]` avant, elle vaudra `[1, "X", 4]` après)
* `del` supprime l'élément à l'indice de la liste. Par exemple `del l[0]` supprime l'élément d'indice 0 dune liste (si `l` valait `[1, 4]` avant, elle vaudra `[4]` après)

> Attention à `remove`, `extend` ou `pop` qui ne font pas ce qu'on croit qu'elle font. Que font-elles ?
{: .a-faire}
{% details solution %}

Voir la [documentation du tutoriel](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) :

* `remove` supprime le **premier** élément trouvé, pas tous
* `extend` ajoute les éléments d'une **liste** passée en paramètre à la la liste à gauche du `.`
* `pop` supprime le dernier élément de la liste et le rend

{% enddetails %}

### liste et chaines

Juste quelques méthodes utiles :

* `split()` est une méthode de `str` qui produit des chaines
* `join(liste)` est une méthode de `str` qui produit une chaine à partir d'une liste de chaines de caractère passé en paramètre

## attributs d'une classe

C'est plus rare, mais certaines classes possèdent  des également des *attributs* en plus des méthodes. Ce sont des valeurs associées à l'objet.

Par exemple les objets de la classe `complex` qui possède les attributs `real` et `imag` pour rendre la partie réelle et imaginaire d'un complexe.

```pyhton
>>> (1+2j).real
1.0
>>> (1+2j).imag
2.0
```
