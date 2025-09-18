---
layout: layout/post.njk

title: Conteneurs

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

En plus des 6 types de bases, python met à notre disposition plusieurs objets qui peuvent _contenir_ d'autres objets.

Un conteneur est un objet itérable et possède l'opérateur `in`{.language-} (comme on l'a déjà vu avec les [chaînes de caractères](../../principes/opérations#chaines-in){.interne}). On pourra ainsi toujours utiliser `x in C`{.language-} pour savoir si l'objet `x`{.language-} est dans le conteneur `C`{.language-}.

Parmi ces conteneurs, la **_liste_** est certainement la plus utilisée.

## Listes et tuples

### Listes

{% aller %}
[Listes](listes){.interne}
{% endaller %}

### Tuples

Un tuple est une liste non-modifiable : les objets present dans le tuple sont déterminés à sa creation. On crée un tupe comme une liste en remplaçant les crochets par des parenthèses :

```python
>>> t = (1, "deux", 3)
```

On les utilise ensuite comme une liste :

```python
>>> len(t)
3
>>> t[1]
'deux'
```

Les méthodes de listes qui ne modifient pas la liste sont utilisables, par exemple :

```python
>>> t.index(3)
2
```

Mais modifier les éléments d'un tuple est interdit :

```python
>>> t[0] = "un"
Traceback (most recent call last):
  File "<python-input-8>", line 1, in <module>
    t[0] = "un"
    ~^^^
TypeError: 'tuple' object does not support item assignment
```

Tout comme les méthodes modifiant la liste :

```python
>>> t.append(4)
Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    t.append(4)
    ^^^^^^^^
AttributeError: 'tuple' object has no attribute 'append'
```

Les tuples sont très pratiques lorsque l'on veut créer un conteneur qui puisse être donner à d'autres méthodes ou fonctions sans crainte qu'elle soit modifié. Dans le doute : utilisez des tuples plutôt que des listes, cela vous évitera des problèmes.

On finira cette partie par quelques cas d'usage courant.

#### Créer un tuple de 1 élément

```python
t = (2,)
```

Si vous oubliez la virgule, vous ne ferez que mettre des parenthèses autour de l'entier 2.

#### Créer un tuple issu d'une itération

Comme un tuple est fixé à sa création, pour créer un tuple issue d'une itération, on commence par créer une liste puis on la transforme en tuple :

```python
>>> l = []
>>> for i in range(10):
...     l.append(i **2)
...
>>> t = tuple(l)
>>> t
(0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
```

#### Attention

Si un tuple n'est pas modifiable, ce nest pas le cas des objets qui le compose.

```python
>>> t = ((1, 2), [1, 2])
>>> t[1].append(3)
>>> t
((1, 2), [1, 2, 3])

```

## <span id="ensembles-dictionnaires"></span>Ensembles et dictionnaires

Les deux autres conteneurs à connaître sont les **_ensembles_** et les **_dictionnaires_**. Ces deux structures sont très utiles lorsque l'on manipule des données mais sont plus complexes à manipuler que des listes. Prenez le temps d'apprendre à utiliser leurs nombreux avantages.

Les ensembles et les dictionnaires sont tous deux des conteneurs, donc itérables mais contrairement aux listes, leur ordre d'itération est **inconnu**. Il peut changer d'une itération à l'autre.

### Ensembles

{% aller %}
[Ensembles](ensembles){.interne}
{% endaller %}

### Dictionnaires

{% aller %}
[Dictionnaires](dictionnaires){.interne}
{% endaller %}

## Chaînes de caractères

Les chaînes de caractères peuvent être vues comme un cas particulier de liste.

### Cas particulier d'un tuple

Une chaîne de caractères peut être vue comme un conteneur de caractères. On peut donc accéder à un caractère particulier comme une liste :

```python

>>> "abcdefghijklmnopqrstuvwxyz"[2]
'c'
```

Ou même utiliser des [slices de liste](./listes/#slices){.interne} :

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

Entraînons nous un peut à manipuler les chaînes de caractères sous la forme d'un conteneur en reprenant le 27ème [nombre de Mersenne](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier) sous sa forme chaîne de caractères : `m27 = str(2 ** 44497 - 1)`{.language-}.

{% exercice %}
Quels sont les 10 premiers chiffres de `m27`{.language-} ?
{% endexercice %}
{% details "solution" %}

`str(m27)[:10]`{.language-}

{% enddetails %}

{% exercice %}
Quels sont les 10 derniers chiffres de `m27`{.language-} ?
{% endexercice %}
{% details "solution" %}

`str(m27)[-10:]`{.language-}

{% enddetails %}

{% exercice %}
Est-ce que  `m27`{.language-} est un [palindrome](https://fr.wikipedia.org/wiki/Palindrome) ?
{% endexercice %}
{% details "solution" %}

`str(m27) == str(m27)[::-1]`{.language-} (`s[::-1]`{.language-} renverse la chaîne)

{% enddetails %}

En revanche, il est interdit de modifier une chaine de caractère :

```python
>>> x = "chaine"
>>> x[0] = "C"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

```

Enfin on ne le répètera jamais assez, python vient avec tout un tas de méthodes utilitaires permettant de résoudre nombre d'opérations courantes. Utilisez la documentation sur les [méthodes de chaînes](https://docs.python.org/3/library/stdtypes.html#string-methods) en python pour résoudre les exercices suivants :

{% exercice %}
Index de la première occurrence de `1234` dans m27. Et de la deuxième ?
{% endexercice %}
{% details "solution" %}

- `str(m27).find('1234')`{.language-}
- `str(m27).find('1234', 19260 + 1)`{.language-} : la première occurrence est à l'indice 19260, on cherche donc après.
- on peut faire en une ligne : `str(m27).find('1234', str(m27).find('1234') + 1)`{.language-}

{% enddetails %}

### Méthodes de chaînes de caractères

#### `byte`{.language-} et `str`{.language-}

Par défaut toutes les chaînes de caractères sont de type `str`{.language-}, et encodées en `utf-8`. Si on veut connaître explicitement les octets d'une chaîne, il faut l'encoder en un autre format par la méthode `encode`{.language-}  des chaînes de caractères qui rend un objet de type byte qui est une suite d'octets.

C'est comme une chaîne de caractères mais qui commence par `b` . On peut ensuite décoder un byte pour le retransformer en `str`{.language-} :

```python
x = "ma chaîne de caractères"
x_en_byte = x.encode('utf8')  # devient : b'ma cha\xc3\xaene de caract\xc3\xa8res'
re_x = x_en_byte.decode('utf8')
```

Ceci va s'avérer utile lorsque l'on récupérera des fichiers depuis internet. Ce seront des `byte` qu'il faudra re-écrire en `utf8`.

Les différents encoding possibles sont disponibles [dans la documentation](https://docs.python.org/3/library/codecs.html#standard-encodings).

#### Exercices

On utilisera [les nombres de Mersenne](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier) comme prétexte à la manipulation de chaînes de caractères en python. Ces exercices sont pour une grande partie tirés d'un cours donné il y a quelques temps par Aristide Grange, à l'université Paul Verlaine de Metz.

{% exercice %}
Notez `m27` le 27ième nombre de Mersenne $2^{44497} -1$ :
{% endexercice %}
{% details "solution" %}

```python
m27 = 2 ** 444497 - 1
```

{% enddetails %}

{% exercice %}
Combien de chiffres en base 10, 2 et 16 possède ce nombre ?
{% endexercice %}
{% details "solution" %}

- en base 10 : `len(str(m27))`{.language-} : conversion de l'entier en chaîne de caractères puis son nombre de chiffres
- en base 2 : `len(bin(m27)) - 2`{.language-} : `bin` transforme un entier en sa représentation binaire. C'est une chaîne de caractères qui commence par `0b` donc on retranche 2 à la longueur.
- en base 16 : `len(hex(m27)) - 2`{.language-} : `hex` transforme un entier en sa représentation hexadécimale. C'est une chaîne de caractères qui commence par `0x` donc on retranche 2 à la longueur.

{% enddetails %}

##### Méthodes de chaînes de caractères

Utilisez la documentation sur les [méthodes de chaînes](https://docs.python.org/3/library/stdtypes.html#string-methods) en python pour résoudre les exercices suivants

{% exercice %}
Index de la première occurrence de `1234` dans m27. Et de la deuxième ?
{% endexercice %}
{% details "solution" %}

- `str(m27).find('1234')`{.language-}
- `str(m27).find('1234', 19260 + 1)`{.language-} : la première occurrence est à l'indice 19260, on cherche donc après.
- on peut faire en une ligne : `str(m27).find('1234', str(m27).find('1234') + 1)`{.language-}

{% enddetails %}

##### Slice

{% aller %}
Comme pour les listes, on peut [utiliser les *slices*]({{"/cours/utiliser-python/listes/"  }}#slice){.interne} pour copier des parties de chaîne.
{% endaller %}

Ainsi `"abcdefghijklmnopqrstuvwxyz"[2:15:4]` vaut : `'cgko'`.

{% exercice %}
Quels sont les 10 premiers chiffres de m27 ?
{% endexercice %}
{% details "solution" %}

`str(m27)[:10]`{.language-}

{% enddetails %}

{% exercice %}
Quels sont les 10 derniers chiffres de m27 ?
{% endexercice %}
{% details "solution" %}

`str(m27)[-10:]`{.language-}

{% enddetails %}

{% exercice %}
Est-ce que m27 est un [palindrome](https://fr.wikipedia.org/wiki/Palindrome) ?
{% endexercice %}
{% details "solution" %}

`str(m27) == str(m27)[::-1]`{.language-} (`s[::-1]`{.language-} renverse la chaîne)

{% enddetails %}


### Chaînes formatées

On a déjà vu [les f-string](../principes/opérations/#f-string), on peut faire plus en utilisant :

- [la méthode `format`](https://docs.python.org/fr/3/library/string.html#formatstrings) qui est la méthode historique de formatage de chaines en python,
- [les chaînes de modèles](https://docs.python.org/fr/3.13/library/string.html#template-strings) conforme aux [normes d'internationalisation](https://www.i18next.com/).

> TBD en python 3.14 les t-string implémentent les template-string directement : <https://davepeck.org/2025/04/11/pythons-new-t-strings/>