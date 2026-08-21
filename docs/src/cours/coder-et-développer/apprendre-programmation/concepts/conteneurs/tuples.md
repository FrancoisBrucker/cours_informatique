---
layout: layout/post.njk
title: Tuples

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Un tuple est une liste non-modifiable : les objets present dans le tuple sont déterminés à sa creation. On crée un tuple comme une liste en remplaçant les crochets par des parenthèses :

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

## Créer un tuple de 1 élément

```python
t = (2,)
```

Si vous oubliez la virgule, vous ne ferez que mettre des parenthèses autour de l'entier 2.

## Créer un tuple issu d'une itération

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

## Attention

Si un tuple n'est pas modifiable, ce nest pas le cas des objets qui le compose.

```python
>>> t = ((1, 2), [1, 2])
>>> t[1].append(3)
>>> t
((1, 2), [1, 2, 3])

```
