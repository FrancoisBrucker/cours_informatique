---
layout: layout/post.njk 
title: Listes
---

{% chemin %}
[Cours]({{ "../.." }}) / [Bases en code et python]({{ ".." }}) / [{{title}}]({{ "." }})
{% endchemin %}

{% info %}
Utilisez la console de <https://console.basthon.fr/> pour exécuter les divers exemples et exercices
{% endinfo %}

<!-- début résumé -->

Les listes sont la structure principale lorsque l'on veut stocker plusieurs objets. La liste est un conteneur dont on peut accéder les éléments un à un.

<!-- end résumé -->

{% chemin "**Documentation :**" %}
<https://docs.python.org/fr/3/tutorial/introduction.html#lists>
{% endchemin %}

## Création

L'exemple suivant crée une liste de nom `x`{.language-python} qui contient l'entier 1 en 1ère position, l'entier 4 en 2ème position et la chaîne de caractères `"douze"`{.language-python} en troisième position :

```python
>>> x = [1, 4, "douze"]
```

## Accès à un élément d'une liste

On accède à un élément de la liste en faisant suivre le nom de la liste par des `[]` et en mettant l'index voulu dans les crochets :

```python
>>> x[0]
1
>>> x[1]
4
>>> x[2]
'douze'
```

Une chaîne de caractère, bien qu'elle ne soit pas une liste stricto sensu peut-être considérée comme une liste composée de caractères : on peut accéder à un caractère particulier de la chaîne comme on le ferait avec une liste.

{% exercice %}
Quel est la treizième lettre du mot "anticonstitutionnellement" ?
{% endexercice %}
{% details "solution" %}

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

{% exercice %}
Quel est la quatrième lettre avant la fin du mot "anticonstitutionnellement" ?
{% endexercice %}
{% details "solution" %}

```text
>>> "anticonstitutionnellement"[-4]
'm'
```

{% enddetails %}

## Modifier un élément d'une liste

Un élément d'une liste peut être considéré comme une variable. On peut donc réaffecter cet élément :

```python
>>> x = [1, 4, "douze"]
[1, 4, 'douze']
>>> x[1] = 42
>>> x
[1, 42, 'douze']
```

Attention aux effets de bords ! Modifier un objet le modifie quelque soit sont nom. Considérez l'exemple suivant :

```python
>>> x = [1, 4, "douze"]
>>> y = x
>>> x[1] = 42
>>> x
[1, 42, 'douze']
```

{% exercice %}
Que vaut `y` ?
{% endexercice %}
{% details "solution" %}

```python
>>> y
[1, 42, 'douze']
```

`x`{.language-python} et `y`{.language-python} sont le **même** objet sous deux noms différents.

{% enddetails %}

## Liste de listes

On peut créer des matrices facilement en utilisant des listes de listes. Considérez l'exemple suivant :

```python
>>> M = [[1, 2, 3], [4, 4, 6]]
```

On a crée une variable `M`{.language-python} qui contient une liste de 2 listes : c'est une matrice à 2 lignes et 3 colonnes.

* La 1ère ligne de la matrice est `M[0]`{.language-python} et la seconde `M[1]`{.language-python}
* l'élément à la 1ère ligne et deuxième colonne s'écrit : `M[0][1]`{.language-python}

## Copie d'une sous-liste

On peut copier une partie d'une liste.
Pour **copier la liste l à partir de l'indice i jusqu'à l'indice j avec un pas de k** par exemple : `l[i:j:k]`{.language-python}
Il n'est pas nécessaire de renseigner tous les champs.

{% exercice %}
que donne `l[::3]`{.language-python} ou `l[1::5]`{.language-python} pour la liste `[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]`{.language-python} ?
{% endexercice %}
{% details "solution" %}

```text
>>> l = list(range(3, 31, 3))
>>> l[::3]
[3, 12, 21, 30]
>>> l[1::5]
[6, 21]
```

{% enddetails %}
