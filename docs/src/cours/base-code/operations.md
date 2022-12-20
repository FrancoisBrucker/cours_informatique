---
layout: layout/post.njk 
title: Opérations sur les objets

eleventyNavigation:
  key: "Opérations sur les objets"
  parent: "Bases en code et python"
---

{% info %}
Utilisez la console de <https://console.basthon.fr/> pour exécuter les divers exemples et exercices
{% endinfo %}

<!-- début résumé -->

Les opérations sur les objets vont des opérations arithmétiques (a + b, a - b, ...) aux tests (a < b) en passant par les opérations logiques (a et b).

<!-- end résumé -->

## Nombres

Les opérations peuvent s'effectuer sur les trois types numériques que sont les entier (classe `int`{.language-}), les réels (classe `float`{.language-}) et les complexes (classe `complex`{.language-})

### Opérateurs

Outre les classiques opérations :

* `+`{.language-} (addition)
* `-`{.language-} (soustraction)
* `/`{.language-} (division)
* `*`{.language-} (multiplication)

python possède aussi :

* `//`{.language-} division entière
* `%`{.language-} reste de la division
* `**`{.language-} exposant.

{% exercice %}
Que vaut le quotient et le reste de la division entière de 4538 par 23 ?
{% endexercice %}
{% details "solution" %}

```text
>>> 4538 // 23
197
>>> 4538 % 23
7
>>> (4538 // 23) * 23 + 7
4538
```

{% enddetails %}

### Raccourcis d'affectation

Python permet aussi de faire l'opération et de procéder immédiatement à sa réaffectation avec les opérateurs :

* `x += 1`{.language-} est équivalent à `x = x + 1`{.language-}
* `x -= 1`{.language-} est équivalent à `x = x - 1`{.language-}
* `x /= 3`{.language-} est équivalent à `x = x / 3`{.language-}
* `x *= 2`{.language-} est équivalent à `x = x * 2`{.language-}

## Chaînes de caractères (concatenation et *)

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

{% exercice %}
Recopiez 10 fois : `"j'aime bien faire du python"` en une ligne de python
{% endexercice %}
{% details "solution" %}
On peut écrire :

```python
>>> 10 * "J'aime bien faire du python. "
"J'aime bien faire du python. J'aime bien faire du python. J'aime bien faire du python. J'aime bien faire du python. J'aime bien faire du python. J'aime bien faire du python. J'aime bien faire du python. J'aime bien faire du python. J'aime bien faire du python. J'aime bien faire du python. "

```

{% enddetails %}

## Listes

Comme pour les chaines de caractères :

* l'opération `+`{.language-} désigne la concaténation entre deux listes
* l'opération `*`{.language-} par en entier $i$ recopie la liste (ses éléments) $i$ fois.

Par exemple :

```python
>>> [1, 4, "douze"] + [42]
[1, 4, 'douze', 42]
>>> [1, 4, "douze"] * 3
[1, 4, 'douze', 1, 4, 'douze', 1, 4, 'douze']
```

Remarquez que :

* `[1, 4, "douze"] + 42`{.language-} produit une erreur puisque `42`{.language-} est un entier et pas une liste.
* `3 * [1, 4, "douze"]`{.language-} fonctionne également

Attention aux effets de bords :

```python
>>> M = [[0, 0, 0]] * 3
>>> M
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> M[1][1] = 1
```

{% exercice %}
Que vaut `M` ?
{% endexercice %}
{% details "solution" %}

```python
>>> M
[[0, 1, 0], [0, 1, 0], [0, 1, 0]]
```

C'est en effet la **même** liste qui a été dupliquée !

{% enddetails %}

## Booléens

### Comparaisons

Comparateurs classiques :

* `<`{.language-} : strictement plus petit
* `<=`{.language-} : plus petit ou égal
* `>`{.language-} : strictement plus grand
* `>=`{.language-} : plus grand ou égal
* `==`{.language-} : égal
* `!=`{.language-} : différent
* `is`{.language-} : égalité d'objets (en pratique uniquement utilisé pour comparer à `None`)

Les comparaisons rendent un booléen. Par exemple : `2 <= 3`{.language-} rend le booléen `True`{.language-}.

### Opérations logiques

* `or`{.language-} : ou logique
* `and`{.language-} : et logique
* `not`{.language-} : négation
