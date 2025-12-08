---
layout: layout/post.njk

title: Chaines de caractères

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les chaînes de caractères peuvent être vues comme un cas particulier de tuple.

## Cas particulier d'un tuple

Une chaîne de caractères peut être vue comme un conteneur de caractères. On peut donc accéder à un caractère particulier comme une liste :

```python

>>> "abcdefghijklmnopqrstuvwxyz"[2]
'c'
```

Ou même utiliser des [slices de liste](./listes/#slice){.interne} :

```python
>>> "abcdefghijklmnopqrstuvwxyz"[2:15:4]
'cgko'
```

En revanche, il est impossible de modifier une chaîne :

```python
>>> x = "Francois"
>>> x[4] = "ç"
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    x[4] = "ç"
    ~^^^
TypeError: 'str' object does not support item assignment
>>>
```

Entraînons nous un peut à manipuler les chaînes de caractères sous la forme d'un conteneur en reprenant le 23ème [nombre de Mersenne](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier) sous sa forme chaîne de caractères : `m23 = str(2 ** 11213 - 1)`{.language-}.

{% exercice %}
Quels sont les 10 premiers chiffres de `m23`{.language-} ?
{% endexercice %}
{% details "solution" %}

`str(m23)[:10]`{.language-}

{% enddetails %}

{% exercice %}
Quels sont les 10 derniers chiffres de `m23`{.language-} ?
{% endexercice %}
{% details "solution" %}

`str(m23)[-10:]`{.language-}

{% enddetails %}

{% exercice %}
Est-ce que `m23`{.language-} est un [palindrome](https://fr.wikipedia.org/wiki/Palindrome) ?
{% endexercice %}
{% details "solution" %}

`str(m23) == str(m23)[::-1]`{.language-} (`s[::-1]`{.language-} renverse la chaîne)

{% enddetails %}

En revanche, il est interdit de modifier une chaîne de caractère :

```python
>>> x = "chaîne"
>>> x[0] = "C"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

```

Enfin on ne le répétera jamais assez, python vient avec tout un tas de méthodes utilitaires permettant de résoudre nombre d'opérations courantes. Utilisez la documentation sur les [méthodes de chaînes](https://docs.python.org/3/library/stdtypes.html#string-methods) en python pour résoudre les exercices suivants :

{% exercice %}
Index de la première occurrence de `1234` dans m23. Et de la deuxième ?
{% endexercice %}
{% details "solution" %}

- `str(m23).find('1234')`{.language-}
- `str(m23).find('1234', 19260 + 1)`{.language-} : la première occurrence est à l'indice 19260, on cherche donc après.
- on peut faire en une ligne : `str(m23).find('1234', str(m23).find('1234') + 1)`{.language-}

{% enddetails %}

## `byte`{.language-} et `str`{.language-}

Par défaut toutes les chaînes de caractères sont de type `str`{.language-}, et encodées en `utf-8`. Si on veut connaître explicitement les octets d'une chaîne, il faut l'encoder en un autre format par la méthode `encode`{.language-} des chaînes de caractères qui rend un objet de type byte qui est une suite d'octets.

C'est comme une chaîne de caractères mais qui commence par `b` . On peut ensuite décoder un byte pour le retransformer en `str`{.language-} :

```python
x = "ma chaîne de caractères"
x_en_byte = x.encode('utf8')  # devient : b'ma cha\xc3\xaene de caract\xc3\xa8res'
re_x = x_en_byte.decode('utf8')
```

Ceci va s'avérer utile lorsque l'on récupérera des fichiers depuis internet. Ce seront des `byte` qu'il faudra re-écrire en `utf8`.

Les différents encoding possibles sont disponibles [dans la documentation](https://docs.python.org/3/library/codecs.html#standard-encodings).

## Exercices

On utilisera [les nombres de Mersenne](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier) comme prétexte à la manipulation de chaînes de caractères en python. Ces exercices sont pour une grande partie tirés d'un cours donné il y a quelques temps par Aristide Grange, à l'université Paul Verlaine de Metz.

{% exercice %}
Notez `m23` le 23ième nombre de Mersenne $2^{11213} -1$ :
{% endexercice %}
{% details "solution" %}

```python
m23 = 2 ** 11213 - 1
```

{% enddetails %}

{% exercice %}
Combien de chiffres en base 10, 2 et 16 possède ce nombre ?
{% endexercice %}
{% details "solution" %}

- en base 10 : `len(str(m23))`{.language-} : conversion de l'entier en chaîne de caractères puis son nombre de chiffres
- en base 2 : `len(bin(m23)) - 2`{.language-} : `bin` transforme un entier en sa représentation binaire. C'est une chaîne de caractères qui commence par `0b` donc on retranche 2 à la longueur.
- en base 16 : `len(hex(m23)) - 2`{.language-} : `hex` transforme un entier en sa représentation hexadécimale. C'est une chaîne de caractères qui commence par `0x` donc on retranche 2 à la longueur.

{% enddetails %}

### Méthodes

Utilisez la documentation sur les [méthodes de chaînes](https://docs.python.org/3/library/stdtypes.html#string-methods) en python pour résoudre les exercices suivants

{% exercice %}
Index de la première occurrence de `1234` dans m23. Et de la deuxième ?
{% endexercice %}
{% details "solution" %}

- `str(m23).find('1234')`{.language-}
- `str(m23).find('1234', 19260 + 1)`{.language-} : la première occurrence est à l'indice 19260, on cherche donc après.
- on peut faire en une ligne : `str(m23).find('1234', str(m23).find('1234') + 1)`{.language-}

{% enddetails %}

### Slice

Comme pour les listes, on peut [utiliser les _slices_](../listes/#slice){.interne} pour copier des parties de chaîne.

Ainsi `"abcdefghijklmnopqrstuvwxyz"[2:15:4]` vaut : `'cgko'`.

{% exercice %}
Quels sont les 10 premiers chiffres de m23 ?
{% endexercice %}
{% details "solution" %}

`str(m23)[:10]`{.language-}

{% enddetails %}

{% exercice %}
Quels sont les 10 derniers chiffres de m23 ?
{% endexercice %}
{% details "solution" %}

`str(m23)[-10:]`{.language-}

{% enddetails %}

{% exercice %}
Est-ce que m23 est un [palindrome](https://fr.wikipedia.org/wiki/Palindrome) ?
{% endexercice %}
{% details "solution" %}

`str(m23) == str(m23)[::-1]`{.language-} (`s[::-1]`{.language-} renverse la chaîne)

{% enddetails %}

## Chaînes formatées

On a déjà vu [les f-string](../principes/opérations/#f-string), on peut faire plus en utilisant :

- [la méthode `format`](https://docs.python.org/fr/3/library/string.html#formatstrings) qui est la méthode historique de formatage de chaines en python,
- [les chaînes de modèles](https://docs.python.org/fr/3.13/library/string.html#template-strings) conforme aux [normes d'internationalisation](https://www.i18next.com/).

{% info %}
En python 3.14 les t-string implémentent les template-string directement : <https://davepeck.org/2025/04/11/pythons-new-t-strings/>
{% endinfo %}
