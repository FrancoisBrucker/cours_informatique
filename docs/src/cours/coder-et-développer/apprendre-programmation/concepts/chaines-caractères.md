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

Ou même utiliser des [slices de liste](../listes/#slice){.interne} :

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

### <span id="méthodes"></span>Méthodes des chaînes de caractères

Les chaines de caractères ont [tout un tas de méthodes](https://docs.python.org/fr/3/library/stdtypes.html#string-methods).

Essayons de les apprendre avec ces petits exercices :

{% exercice %}
Transformez le 23ème [nombre de Mersenne](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier) ($2^{11213}-1$) en une chaîne de caractère
{% endexercice %}
{% details "solution" %}

```python
>>> x = str(2 ** 11213 - 1)
```

{% enddetails %}

{% exercice %}
En utilisant la méthode [`count`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.count), comptez le nombre de 0 du 23ème [nombre de Mersenne premier](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier).
{% endexercice %}
{% details "solution" %}

Dans un interpréteur :

```python
>>> x.count("0")
348
```

{% enddetails %}

{% exercice %}
En utilisant la méthode [`replace`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.replace), changez les 2 en 7 dans le 23ème [nombre de Mersenne premier](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier).
{% endexercice %}
{% details "solution" %}

Dans un interpréteur :

```python
>>> y = int(x.replace("2", "7"))
```

{% enddetails %}

{% exercice %}
Avec les méthodes [`count`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.count), [`index`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.index) et [`rindex`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.rindex) :

Dans le 23e nombre de Mersenne :

- combien y a-t-il de "42" ?
- quel est l'indice du premier "42" ?
- quel est l'indice du dernier "42" ?

{% endexercice %}
{% details "solution" %}

```python
>>> str(2 ** 11213 - 1).count("42")
33
>>> str(2 ** 11213 - 1).index("42")
29
>>> str(2 ** 11213 - 1).rindex("42")
3327

```

{% enddetails %}
{% exercice %}
Remplacez les 2 par des 7 dans le 23e nombre de Mersenne 

{% endexercice %}
{% details "solution" %}

Attention, une fois que l'on a changer les 2 en 7 on ne peut pas juste retransformer les 7 en 2... Il faut commencer par mettre les 2 de côté puis transformer les 7 en 2 et enfin reprendre les 2 mis de coté et les transformer en 7 :

```python
>>> x = str(2 ** 11213 - 1)
>>> y = x.replace("2","?")
>>> z = y.replace("7","2")
>>> t = z.replace("?","7")
```

On peut le faire en une seule ligne :

```python
str(2 ** 11213 - 1).replace("2","x").replace("7","2").replace("x","7")
```

De part l'associativité à gauche, la commande précédente est équivalente à :

```python
((str(2 ** 11213 - 1).replace("2","x")).replace("7","2")).replace("x","7")
```

Il est aisé de comprendre ce que ça fait en procédant de droite à gauche :

1. `replace("x","7")`{.language-} est appliqué à ce qui est à sa gauche donc `str(2 ** 11213 - 1).replace("2","x").replace("7","2")`{.language-}
2. `replace("7","2")`{.language-} est appliqué à ce qui est à sa gauche donc `str(2 ** 11213 - 1).replace("2","x")`{.language-}
3. `replace("2","x")`{.language-} est appliqué à ce qui est à sa gauche donc `str(2 ** 11213 - 1)`{.language-}

En remontant les opérations précédentes :

1. le résultat de `str(2 ** 11213 - 1)`{.language-} sera une chaîne de caractère représentant le 23ème nombre premier de Mersenne
2. `str(2 ** 11213 - 1).replace("2","x")`{.language-} on a remplacé les 2 par des "x" dans la chaîne précédente
3. `str(2 ** 11213 - 1).replace("2","x").replace("7","2")`{.language-} on a remplacé les 7 par des 2 de la chaîne précédente
4. `str(2 ** 11213 - 1).replace("2","x").replace("7","2").replace("x","7")`{.language-} on a remplacé les "x" par des 2 dans la chaîne précédente

On a donc au final échangé les 2 et les 7 du 23ème nombre premier de Mersenne

{% enddetails %}

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

#### <span id="f-string"></span>Chaînes formatées

{% lien "**Documentation**" %}

<https://docs.python.org/fr/3/tutorial/inputoutput.html#tut-f-strings>

{% endlien %}

On peut  créer des chaînes en utilisant _implicitement_ la concatenation en utilisant **_les chaines formatées_** (_format-string_ ou encore _f-string_).

Par exemple :

```python
>>> nom = "Ada"
>>> bonjour = f"Bonjour {nom} !"
>>> print(bonjour)
Bonjour Ada !
```

Remarquez le `f`{.language-} avant le début de la chaîne, il indique à python qu'il doit remplacer l'expression entre accolade par un objet. Si on oublie le `f`{.language-}, on obtient une chaîne classique :

```python
>>> nom = "Ada"
>>> bonjour = "Bonjour {nom} !"
>>> print(bonjour)
Bonjour {nom} !
```

L'utilisation de chaînes formatées remplace une concaténation explicite :

```python
>>> bonjour = "Bonjour " + nom + " !"
>>> print(bonjour)
Bonjour Ada !
```

En étant bien plus lisible.

Attention, c'est bien une concaténation à la création de la chaîne. Une chaîne ne va pas se modifier magiquement lorsque l'on modifie une variable :

```python
>>> nom = "Ada"
>>> bonjour = f"Bonjour {nom} !"
>>> print(bonjour)
Bonjour Ada !
>>> nom = "Dominique"
>>> print(bonjour)
Bonjour Ada !
```

Enfin, comme les accolades sont une expression, on peut écrire ce genre de choses :

```python
>>> réponse = f"La réponse universelle est {40 + 2}"
>>> print(réponse)
La réponse universelle est 42
```

Et, enfin, si on veut écrire une accolade, on l'insère : `f"{'{'}"`{.language-}.

