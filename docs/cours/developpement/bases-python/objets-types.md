---
layout: page
title:  "Bases de python : Objets types et types d'objets"
authors: 
    - Augustin Agbo-Kpati
    - François Brucker
    - Pascal Préa
---


Python connait 5 classes d'objets de base qui permettent de faire la grande majorité des programmes.

## Les 5 classes de base

>[Documentation correspondante](https://docs.python.org/3/library/stdtypes.html#built-in-types).

* Chaînes de caractères
  * exemple : `"python"` ou `'python'`
  * quelque chose qui commence et fini par `"` ou qui commence et fini par `'` ou encore qui commence et fini par `"""`.
* Réels
  * exemple : `2.91` ou `2.0`
  * un nombre avec une décimale (qui peut être nulle) notée par un `.`
* Entiers
  * exemple : `42` ou `0`
  * un nombre sans décimale
* Complexes (la notation utilise j à la place de i)
  * exemple : 3+2j, 1j
  * un réel ou entier avec une partie imaginaire, notée `j`, entière ou imaginaire.
* Booléens
  * exemple : `True` ou `False`
  * que 2 possibilités, `True` ou `False`

> Tout objet de python à sa classe.

### classes d'un objet

Afin de connaître la classe d'un objet, on peut utiliser la fonction `type` :

```python
type(42) 
```

Qui rendra :  `<class 'int'>`. Les entiers sont donc de classe `'int'` en python.

> Quelle est la classe associée à chacun des types de bases ?
{: .a-faire}

{% details solution %}

Dans un interpréteur :

```python
>>> type("2")
<class 'str'>
>>> type(2.0)
<class 'float'>
>>> type(2)
<class 'int'>
>>> type(2+0j)
<class 'complex'>
>>> type(True)
```

{% enddetails %}
{: .a-faire}

### changer de classe

Il est possible de créer un nouvel objet à partir d'un objet d'une autre classe. Par exemple, un réel à partir d'une chaine de caractère :

```python
float("3.1415")
```

Va rendre un objet entier valant 2 à partir d'une chaine de caractère avec le caractère "2".

Ou transformer un réel en entier :

```python
int(3.1415)
```

Ou encore transformer un booléen en chaine de caractère :

```python
str(True)
```

> En utilisant la classe [int()](https://docs.python.org/fr/3.9/library/functions.html#int) trouvez la représentation décimale du nombre binaire : 1001100011
{: .a-faire}
{% details solution %}

Dans un interpréteur :

```python
>>> int("1001100011", base=2)
611
```

{% enddetails %}
{: .a-faire}

> En utilisant le fait que la fonction `len(chaine de caractère)` donne le nombre de caractères de la chaine (par exemple `len("abc")` rend `3`), et que l'exposant eb python s'écrit `**` (par exemple `2**8` rend `256`) donnez le nombre de chiffre du 27ème [nombre de Mersenne premier](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier).
{: .a-faire}
{% details solution %}

Dans un interpréteur :

```python
>>> len(str(2 ** 44497 - 1))
13395
```

{% enddetails %}
{: .a-faire}

On effectue souvent ce genre d'opération de façon implicite pour les booléen. Ainsi, un entier est vrai s'il est non nul.

> Vérifiez le.
{: .a-faire}
{% details solution %}

Dans un interpréteur :

```python
>>> bool(42)
True
```

{% enddetails %}
{: .a-faire}

> Quand-est qu'une chaine de caractère est fausse ?
{: .a-faire}
{% details solution %}

Une chaine de caractère est fausse si elle est vide et vraie sinon.

Dans un interpréteur :

```python
>>> bool("")
False
>>> bool("False")
True
```

{% enddetails %}
{: .a-faire}

## Action sur les objets

Agir sur des objets en python prend deux formes (en apparence) différentes :

* les méthodes
* les opérations

### méthodes d'une classes

Les méthodes sont moyens d'agir sur un objet. On les utilise de cette façon :

```pyhton
objet.methode(paramètre 1, paramètre 2, ..., paramètre n)
```

On applique `méthode` à `objet` en utilisant les `paramètres` de la méthode.

> Une méthode ne s'utilise **jamais** seule. Elle s'applique à ce qu'il y a à gauche d'elle.

Chaque classe vient avec des méthodes. Si les nombre et booléens ont peux de méthode, les [chaines de caractères en ont tout un tas](https://docs.python.org/3/library/stdtypes.html#string-methods).

> Combien y a-t-il de 0 dans le 27ème [nombre de Mersenne premier](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier).
{: .a-faire}
{% details solution %}

Dans un interpréteur :

```python
>>> str(2 ** 44497 - 1).count("")
1332
```

{% enddetails %}
{: .a-faire}

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
{: .a-faire}

### attributs d'une classe

C'est plus rare, mais certaines classes possèdent  des également des *attributs* en plus des méthodes. Ce sont des valeurs associées à l'objet.

Par exemple les objets de la classe complex qui possède les attibuts `real` et `imag` pour rendre la partie réelle et imaginaire d'un complexe.

```pyhton
>>> (1+2j).real
1.0
>>> (1+2j).imag
2.0
```
