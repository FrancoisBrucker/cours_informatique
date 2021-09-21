---
layout: page
title:  "Bases de python : Objets types et types d'objets"
author: "François Brucker"
---

Les opérations sur les objets vont des opérations arithmétiques (addition) aux tests (est plus grand que) en passant par les opérations logiques (a et b)

## nombres

<https://docs.python.org/3/library/operator.html#mapping-operators-to-functions>

Les opération peuvent s'effectuer sur les trois types numériques que sont les entier (classe `int`), les réels (classe `float`) et les complexes (classe `complex`)

Outre les classiques opérations `+` (addition), `-` (soustraction), `/` (difision) et `*` (multiplication), python possède aussi `//` division entière,  `%` reste de la division entière et `**` exposant.

> que vaut le quotient et le reste de la division entière de 4538 par 23 ?
{: .a-faire}
{% details solution %}
Dans un terminal :

```text
>>> 4538 // 23
197
>>> 4538 % 23
7
>>> (4538 // 23) * 23 + 7
4538
```

{% enddetails %}
{: .a-faire}

Python permet aussi de faire l'opération et de procéder immédiatement à sa réaffectation avec les opérateurs :

* `x += 1` est équivalent à `x = x + 1`
* `x -= 1` est équivalent à `x = x - 1`
* `x /= 3` est équivalent à `x = x / 3`
* `x *= 2` est équivalent à `x = x * 2`

## chaines de caractères (concatenation et *)

```python
>>> "x" + "y"
'xy'
>>> 3 * "x"
'xxx'
```

> Recopiez 10 fois : `"j'aime bien faire du python"`
{: .a-faire}
{% details solution %}
Si l'on sait que le caractère `\n` correspond à aller à la ligne, on peut écrire :

```python
>>> print(10 * "j'aime bien faire du python\n")
j'aime bien faire du python
j'aime bien faire du python
j'aime bien faire du python
j'aime bien faire du python
j'aime bien faire du python
j'aime bien faire du python
j'aime bien faire du python
j'aime bien faire du python
j'aime bien faire du python
j'aime bien faire du python

```

{% enddetails %}
{: .a-faire}

## listes

Comme pour les chaines de caractères, l'opération `+` désigne la concaténation. L'opération `*` par en entier, tout comme les chaine recopie la liste (ses éléments) plusieurs fois.

## booleen

### comparaisons

<https://docs.python.org/3/library/stdtypes.html#comparisons>

Les comparaisons rendent un booléen. Par exemple : `2 <= 3` rend le booléen `True`.

### opérations logiques

<https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not>

