---
layout: layout/post.njk 
title: Blocs

eleventyNavigation:
  key: "Blocs"
  parent: "Bases en code et python"
---

{% info %}
Utilisez la console de <https://console.basthon.fr/> pour exécuter les divers exemples et exercices
{% endinfo %}

<!-- début résumé -->

Les blocs python qui permettent de grouper un ensemble de lignes de codes ensemble. On verra les blocs `while`, `for` et les blocs `if/elif/else`.

<!-- end résumé -->

Si python ne pouvait qu'exécuter ligne à ligne un code on ne pourrait pas faire grand chose. Le principe des programmes est de pouvoir grouper les instructions en bloc.

## Définition d'un bloc

En python, un bloc est toujours défini de la même manière  :

* Ce qui va identifier le bloc pour son exécution (une condition, son nombre d'exécution, son nom) et se finit par un `:`{.language-}
* Les instructions le constituant.

Pour séparer les blocs les un des autres, et savoir ce qui le définit, le langage Python utilise l'indentation (4 espaces par défaut): un bloc est donc une suite d'instructions ayant la même indentation.

```text
type de bloc:
    instruction 1
    instruction 2
    ...
    instruction n
```

Ces différents blocs sont pratiques car ils vont nous permettre :

* répéter des blocs
* d'exécuter des blocs conditionnellement

## Répétition de blocs

Deux types de boucles existent en python : les boucles *tant que* (`while`{.language-}) et les boucles *pour chaque* (`for`{.language-})

### Bloc while : boucle tant que

{% lien "**Documentation**" %}
<https://docs.python.org/3/reference/compound_stmts.html#the-while-statement>
{% endlien %}

```text
while <condition logique>:
    instruction 1
    instruction 2
    ...
    instruction n
```

Par exemple le bloc `while`{.language-} suivant :

```python
b = 6
while b > 0:
    print(b)
    b = b - 1
```

qui va afficher :

```text
6
5
4
3
2
1
```

{% exercice %}
Calculez la factorielle de 45.
{% endexercice %}
{% details "solution" %}

```python
factorielle = x = 45

while x >= 1:
    factorielle = factorielle * x
    x -= 1

print(factorielle)
```

{% enddetails %}

### Bloc for : boucle pour chaque

{% lien "**Documentation**" %}
<https://docs.python.org/3/reference/compound_stmts.html#the-for-statement>
{% endlien %}

```text
for <nom> in <conteneur>:
    instruction 1
    instruction 2
    ...
    instruction n
```

On peut directement utiliser range si on veut dans une boucle for, on est pas obligé de la transformer en liste avant, ainsi si on peut afficher à l'écran les 10 premiers entiers à partir de 0 on eut écrire :

```python
for x in range(10):
    print(x)
```

On peut également boucler sur une liste :

```python
l = ["bonjour", "tout", "le", "monde", "!"]
for mot in l:
    print(mot)
```

De même, une chaîne de caractères étant un conteneur de caractères, on peut boucler sur elles :

```python
for c in "bonjour":
    print(c)
```

{% exercice %}
Essayez les deux exemples précédents dans une console.
{% endexercice %}
{% details "solution" %}

```python
>>> l = ["bonjour", "tout", "le", "monde", "!"]
>>> for mot in l:
...     print(mot)
... 
bonjour
tout
le
monde
!
>>> 
```

et :

```python
>>> for c in "bonjour":
...     print(c)
... 
b
o
n
j
o
u
r
>>>
```

{% enddetails %}

## Blocs if : Exécution conditionnelle

{% lien "**Documentation**" %}
<https://docs.python.org/3/reference/compound_stmts.html#the-if-statement>
{% endlien %}

Permet d'exécuter un bloc si une condition logique est vraie :

```text
if <condition logique>:
    instruction 1
    instruction 2
    ...
    instruction n
elif <condition logique>:
    instruction 1
    instruction 2
    ...
    instruction n
else:
    instruction 1
    instruction 2
    ...
    instruction n
```

Notez qu'il peut y avoir autant de bloc `elif`{.language-} que l'on veut (même 0) et qu'il n'est pas nécessaire d'avoir de `else`{.language-}.

{% exercice %}
Utilisez ce que vous avez appris pour vérifier la [conjecture de Syracuse](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse) pour les 100 premiers entiers
Exemple :
{% endexercice %}
{% details "solution" %}

```python

for x in range(100):
    while x > 1:
        if x % 2  == 0:
            x /= 2
        else:
            x = 3 * x + 1
```

{% enddetails %}
