---
layout: page
title:  "Bases de python : conditions"
author: "François Brucker"
---


> <https://docs.python.org/3/reference/compound_stmts.html#the-if-statement>

Permet d'exécuter un bloc si une condition loigique est vraie :

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

Notez qu'il peut y avoir autant de bloc `elif` que l'on veut (même 0) et qu'il n'est pas nécessaire d'avoir de `else`.

> Utilisez ce que vous avez appris pour vrifier la [conjecture de syrcuse](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse) pour les 100 premiers entiers
Exemple :
{:.a-faire}
{% details solution %}

```python

for x in range(100):
    while x > 1:
        if x % 2  == 0:
            x /= 2
        else:
            x = 3 * x + 1
```

{% enddetails %}
{:.a-faire}