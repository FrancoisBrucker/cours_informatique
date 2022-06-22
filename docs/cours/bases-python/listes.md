---
layout: page
title:  "Bases de python : listes"
authors: 
    - François Brucker
---


Les listes sont la structure principale lorsque l'on veut stocker plusieurs objets. La liste est un conteneur dont on peut acceder les éléments un à un.

L'exemple suivant crée une liste de nom `x` qui contient l'entier 1 en 1ère position, l'entier 4 en 2ème position et la chaque de caractères `"12"` en troisième position : 

```python
>>> x = [1, 4, "douze"]
```

> Une chaîne de caractère est considérée comme une liste de caractères.

## accès à un élément d'une listes

On accède à un élément de la liste en faisant suivre le nom de la liste par des `[]` et en mettant l'index voulu dans les crochets :

```python 
>>> x[0]
1
>>> x[1]
4
>>> x[2]
'douze'
```

> Quel est la treizième lettre du mot "anticonstitutionnellement" ?
{: .a-faire}
{% details solution %}

```text
>>> "anticonstitutionnellement"[12]
't'
```

{% enddetails %}


On peut aussi commencer par la fin, d'index -1 : 

```python 
>>> x[-1]
'douze'
>>> x[-2]
4
>>> x[-3]
1
```

> Quel est la quatrième lettre avant la fin du mot "anticonstitutionnellement" ?
{: .a-faire}
{% details solution %}

```text
>>> "anticonstitutionnellement"[-4]
'm'
```

{% enddetails %}

## Copie d'une sous-liste

On peut copier une partie d'une liste.
Pour **copier la liste l à partir de l'indice i jusqu'à l'indice j avec un pas de k** par exemple : `l[i:j:k]`
Il n'est pas nécessaire de renseigner tous les champs.

> que donne `l[::3]` ou `l[1::5]` pour la liste `[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]` ?
{: .a-faire}
{% details solution %}

```text
>>> l = list(range(3, 31, 3))
>>> l[::3]
[3, 12, 21, 30]
>>> l[1::5]
[6, 21]
```

{% enddetails %}