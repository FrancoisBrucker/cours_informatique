---
layout: page
title:  "Bases de python : opérations sur les objets"
author: "François Brucker"
---

> [bases de python]({% link cours/bases-python/index.md %}) / [opérations sur les objets]({% link cours/bases-python/operations.md %})
{: .chemin}

Les opérations sur les objets vont des opérations arithmétiques (a + b, a - b, ...) aux tests (a < b) en passant par les opérations logiques (a et b)

## nombres

Les opérations peuvent s'effectuer sur les trois types numériques que sont les entier (classe `int`), les réels (classe `float`) et les complexes (classe `complex`)

### opérateurs

Outre les classiques opérations :

* `+` (addition)
* `-` (soustraction)
* `/` (division)
* `*` (multiplication)

python possède aussi :

* `//` division entière
* `%` reste de la division
* `**` exposant.

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

### raccourcis d'affectation

Python permet aussi de faire l'opération et de procéder immédiatement à sa réaffectation avec les opérateurs :

* `x += 1` est équivalent à `x = x + 1`
* `x -= 1` est équivalent à `x = x - 1`
* `x /= 3` est équivalent à `x = x / 3`
* `x *= 2` est équivalent à `x = x * 2`

## chaines de caractères (concatenation et *)

Les chaînes de caractères possède 2 opérateurs :

* l'addition qui concatène deux chaînes
* la multiplication d'un entier $i$ par une chaîne $c$ qui concatène $i$ fois $c$ à elle même.

Par exemple :

```python
>>> "x" + "y"
'xy'
>>> 3 * "x"
'xxx'
```

> Recopiez 10 fois : `"j'aime bien faire du python"` en une ligne de python
{: .a-faire}
{% details solution %}
On peut écrire :

```python
>>> 10 * "J'aime bien faire du python. "
"J'aime bien faire du python. J'aime bien faire du python. J'aime bien faire du python. J'aime bien faire du python. J'aime bien faire du python. J'aime bien faire du python. J'aime bien faire du python. J'aime bien faire du python. J'aime bien faire du python. J'aime bien faire du python. "

```

{% enddetails %}

## listes

Comme pour les chaines de caractères :

* l'opération `+` désigne la concaténation entre deux listes
* l'opération `*` par en entier $i$ recopie la liste (ses éléments) $i$ fois.

Par exemple :

```python
>>> [1, 4, "douze"] + [42]
[1, 4, 'douze', 42]
>>> [1, 4, "douze"] * 3
[1, 4, 'douze', 1, 4, 'douze', 1, 4, 'douze']
```

> Remarquez que :
>
> * `[1, 4, "douze"] + [42]` produit une erreur puisque `42` est un entier et pas une liste.
> * `3 * [1, 4, "douze"]` fonctionne également

Attention aux effets de bords :

```python
>>> M = [[0, 0, 0]] * 3
>>> M
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> M[1][1] = 1
```

> Que vaut `M` ?
{: .a-faire}
{% details %}

```python
>>> M
[[0, 1, 0], [0, 1, 0], [0, 1, 0]]
```

C'est en effet la **même** liste qui a été dupliquée !

{% enddetails %}

## booleen

### comparaisons

Comparateurs classiques :

* `<` : strictement plus petit
* `<=` : plus petit ou égal
* `>` : strictement plus grand
* `>=` : plus grand ou égal
* `==` : égal
* `!=` : différent
* `is` : égalité d'objets (en pratique uniquement utilisé pour comparer à `None`)

Les comparaisons rendent un booléen. Par exemple : `2 <= 3` rend le booléen `True`.

### opérations logiques

* `or` : ou logique
* `and` : et logique
* `not` : négation
