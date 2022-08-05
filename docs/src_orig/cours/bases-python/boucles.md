---
layout: page
title:  "Bases de python : boucles"
authors: 
    - Augustin Agbo-Kpati
    - François Brucker
    - Pascal Préa
---

tbd fibonnacci

Deux types de boucles existent en python : les boucles *tant que* (`while`) et les boucles *pour chaque* (`for`)

## Boucle while

> <https://docs.python.org/3/reference/compound_stmts.html#the-while-statement>

```text
while <condition logique>:
    instruction 1
    instruction 2
    ...
    instruction n
```

Par exemple le bloc `while` suivant :

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

> calculez la factorielle de 45.
{: .a-faire}
{% details solution %}

```python
factorielle = x = 45
while x >= 1:
    factorielle = factorielle * x
    x -= 1
print(factorielle)
```

{% enddetails %}
{: .a-faire}

### Boucle for

> <https://docs.python.org/3/reference/compound_stmts.html#the-for-statement>

```text
for <nom> in <conteneur>:
    instruction 1
    instruction 2
    ...
    instruction n
```

On peut directement utiliser range si on veut dans une boucle for, on est pas obligé de la transformer en liste avant, ainsi si on peut afficher à l'écran les 10 premiers entiers à partir de 0 on eut écrire :

```pyhton
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

> essayez les deux exemples précédents dans un interpréteur.
{: .a-faire}
