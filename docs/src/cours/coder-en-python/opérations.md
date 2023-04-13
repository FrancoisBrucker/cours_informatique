---
layout: layout/post.njk 
title: Opérations sur les objets

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
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

## Chaînes de caractères

Trois opérateur sont courants pour les chaînes de caractères :

* la concaténation avec l'opérateur `+`{.language-}
* la multiplication avec l'opérateur `*`{.language-}
* test de présence avec l'opérateur `in`{.language-}

### Concatenation et multiplication

Les chaînes de caractères possèdent 2 opérateurs :

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
Recopiez 10 fois : `"j'aime bien faire du python"`{.language-} en une ligne de python
{% endexercice %}
{% details "solution" %}
On peut écrire :

```python
>>> 10 * "J'aime bien faire du python. "
"J'aime bien faire du python. J'aime bien faire du python. J'aime bien faire du python. J'aime bien faire du python. J'aime bien faire du python. J'aime bien faire du python. J'aime bien faire du python. J'aime bien faire du python. J'aime bien faire du python. J'aime bien faire du python. "

```

{% enddetails %}

{% exercice %}
Affectez la chaîne de caractères `"j'aime bien faire du"`{.language-} à la variable `x`{.language-}. Puis ajoutez `" python"`{.language-} à `x`{.language-} en une ligne de python
{% endexercice %}
{% details "solution" %}
On peut écrire :

```python
>>> x = "J'aime bien faire du"
>>> x += " python."
>>> print(x)
J'aime bien faire du python.
```

{% enddetails %}

### <span id="chaines-in"></span> Test de présence

Une chaîne de caractère peut être vue comme un conteneur (ordonné) de caractères. Savoir si un caractère ou une sous-chaîne est présent dans une chaîne peut se faire alors avec l'opérateur `in`{.language-}, qui rend un booléen :

* `"c" in "coucou"`{.language-} rendra `True`
* `"cou" in "coucou"`{.language-} rendra `True`
* `"cc" in "coucou"`{.language-} rendra `False`

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

* `not`{.language-} : négation
* `or`{.language-} : ou logique
* `and`{.language-} : et logique

Notez que les opérateurs logiques s'appliquent à tous les objets, python va comparer leurs représentations sous la forme de booléen. Par exemple
`not 2`{.language-} va rendre `True`{.language-} (l'entier 2 est `True`{.language-} représenté comme un booléen).

De même, les opérateurs `or`{.language-} et `and`{.language-} vont rendre des objets comparé, dont les représentation binaires correspondent aux opérateurs logiques :

* `x or y`{.language-} rendra :
  * `x`{.language} si la représentation sous la forme d'un booléen de de `x`{.language-} est `True`{.language}
  * `y`{.language} si la représentation sous la forme d'un booléen de de `x`{.language-} est `False`{.language}
* `x and y`{.language-} rendra :
  * `y`{.language} si la représentation sous la forme d'un booléen de de `x`{.language-} est `True`{.language}
  * `x`{.language} si la représentation sous la forme d'un booléen de de `x`{.language-} est `False`{.language}

Cela ne change rien à l'utilisation classique des opérations logiques puisque la représentation sous forme de booléen de l'objet rendu est conforme à ce qu'on attend :

* `True`{.language-} si un des deux paramètres est considéré comme vrai pour `or`{.language-}, `False`{.language-} sinon.
* `True`{.language-} si un des les deux paramètres sont considérés comme vrai pour `and`{.language-}, `False`{.language-} sinon.

<span id="and-or-trick"></span>
{% info %}
Python a choisi cette façon de faire pour permettre des notations abrégées comme :

* `(x > 0) and log(x)`{.language-} qui rendra soit `False`{.language-} si `x <= 0`{.language-} soit `log(x)`{.language-} sinon.
* `((x > 0) and log(x)) or None`{.language-} qui rendra soit `None`{.language-} si `x <= 0`{.language-} soit `log(x)`{.language-} sinon

{% endinfo %}
