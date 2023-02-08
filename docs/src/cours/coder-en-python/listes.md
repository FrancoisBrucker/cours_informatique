---
layout: layout/post.njk 
title: Listes

eleventyNavigation:
  key: "Listes"
  parent: "Coder en Python"
---

{% info %}
Utilisez la console de <https://console.basthon.fr/> pour exécuter les divers exemples et exercices
{% endinfo %}

<!-- début résumé -->

Les listes sont la structure principale lorsque l'on veut stocker plusieurs objets. La liste est un conteneur dont on peut accéder les éléments un à un.

<!-- end résumé -->

{% lien "**Documentation**" %}
<https://docs.python.org/fr/3/tutorial/introduction.html#lists>
{% endlien %}

## Création

### Directe

L'exemple suivant crée une liste de nom `x`{.language-} qui contient l'entier 1 en 1ère position, l'entier 4 en 2ème position et la chaîne de caractères `"douze"`{.language-} en troisième position :

```python
>>> x = [1, 4, "douze"]
```

### Avec range

La fonction [`range`{.language-}](../blocs#range) qui produit des itérateurs peut également permettre de créer des listes.

Par exemple :

```python
>>> list(range(5))
[0, 1, 2, 3, 4]
```

Crée une liste avec les 5 premiers entiers.

{% attention %}
La fonction `range`{.language-} ne crée **pas** de listes mais un itérateur.

```python
>>> range(5)
range(0, 5)
```

N'est **pas** une liste.

{% endattention %}

### <span id="list-comprehension"></span> Avec une *list comprehension*

{% lien %}
<https://docs.python.org/fr/3/tutorial/datastructures.html#list-comprehensions>
{% endlien %}

Enfin, les *list comprehension* sont une façon efficace de créer des listes de façon àla fois compacte et lisible.

```python
l = []
for i in range(10):
    l.append(i ** 2)
```

est équivalent à :

```python
l = [i ** 2 for i in range(10)]
```

{% exercice %}
Créez avec une *list comprehension* une liste contenant tous les entiers de 0 à 10.
{% endexercice %}
{% details "solution" %}

```python
>>> l = [i for i in range(11)]
>>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

{% enddetails %}

{% exercice %}
Créez avec une *list comprehension* une liste contenant toutes les sommes $i + j$ avec i allant de 0 à 10 et j allant de 2 à 5.
{% endexercice %}
{% details "solution" %}

```python
>>> l = [i + j for i in range(11) for j in range(2, 6)]
>>> l
[2, 3, 4, 5, 3, 4, 5, 6, 4, 5, 6, 7, 5, 6, 7, 8, 6, 7, 8, 9, 7, 8, 9, 10, 8, 9, 10, 11, 9, 10, 11, 12, 10, 11, 12, 13, 11, 12, 13, 14, 12, 13, 14, 15]
```

{% enddetails %}

{% exercice %}
Créez avec une *list comprehension* une liste contenant toutes les sommes $i + j$ avec les i pairs pour les entiers allant de 0 à 10 et j allant de 2 à 5.
{% endexercice %}
{% details "solution" %}

```python
>>> l = [i + j for i in range(11) if i % 2 == 0 for j in range(2, 6)]
>>> l
[2, 3, 4, 5, 4, 5, 6, 7, 6, 7, 8, 9, 8, 9, 10, 11, 10, 11, 12, 13, 12, 13, 14, 15]
```

{% enddetails %}

{% exercice %}
Créez avec une *list comprehension* une liste contenant toutes les sommes $i + j$ avec les i pairs pour les entiers allant de 0 à 10 et j allant de 2 à 5 si $j-i$ est négatif ou nul.
{% endexercice %}
{% details "solution" %}

```python
>>> l = [i + j for i in range(11) if i % 2 == 0 for j in range(2, 6) if j-i <= 0]
>>> l
[4, 6, 7, 8, 8, 9, 10, 11, 10, 11, 12, 13, 12, 13, 14, 15]
```

{% enddetails %}

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

Le nombre d'élément d'un conteneur, comme une liste, peut être donné par la fonction `len`{.language-}. Pour l'exemple précédent :

```python
>>> len(x)
3
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

Pour la chaîne `"PYTHON"`{.language-} :

| itérable  | P  | Y | T | H  | O | N |
| :-:  | :-: |:-:| :-:|:-:| :-:| :-:|
| numérotation à partir du début  | 0  | 1 | 2 | 3 | 4 | 5 |
| numérotation à partir de la fin | -6  | -5 | -4 | -3 | -2 | -1 |

{% exercice %}
Quel est la quatrième lettre avant la fin du mot "anticonstitutionnellement" ?
{% endexercice %}
{% details "solution" %}

```text
>>> "anticonstitutionnellement"[-4]
'm'
```

{% enddetails %}

## Itérer sur une liste

En tant que conteneur, une liste est un itérable. Elle peut peut donc faire partie d'une instruction for :

```python
l = ["bonjour", "tout", "le", "monde", "!"]
for mot in l:
    print(mot)
```

## Présence

Utiliser l'opérateur `in`{.language-} est très utile avec les listes.

```python
>>> l = ["bonjour", "tout", "le", "monde", "!"]
>>> "bonjour" in l
True
>>> 42 in l
False
```

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
Que vaut `y`{.language-} ?
{% endexercice %}
{% details "solution" %}

```python
>>> y
[1, 42, 'douze']
```

`x`{.language-} et `y`{.language-} sont le **même** objet sous deux noms différents.

{% enddetails %}

## Liste de listes

On peut créer des matrices facilement en utilisant des listes de listes. Considérez l'exemple suivant :

```python
>>> M = [[1, 2, 3], [4, 4, 6]]
```

On a crée une variable `M`{.language-} qui contient une liste de 2 listes : c'est une matrice à 2 lignes et 3 colonnes.

* La 1ère ligne de la matrice est `M[0]`{.language-} et la seconde `M[1]`{.language-}
* l'élément à la 1ère ligne et deuxième colonne s'écrit : `M[0][1]`{.language-}

{% exercice %}
Créez la matrice M à 5 ligne et 5 colonnes possédant que des 1 avec une unique *list comprehension*.
{% endexercice %}
{% details "solution" %}

```python
>>> M = [[1 for c in range(5)] for l in range(5)]
>>> M
[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
```

{% enddetails %}

{% exercice %}
Créez la matrice identité à 5 ligne et 5 colonnes possédant que des 1 avec une unique *list comprehension*. Il pourra être utile de se rappeler de [cette information](../operations#and-or-trick) avant de résoudre cet exercice.
{% endexercice %}
{% details "solution" %}

```python
>>> M = [[(((l == c) and 1) or 0) for c in range(5)] for l in range(5)]
>>> M
[[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
```

{% enddetails %}

## Suppression d'un élément d'une liste

On peut utiliser la commande `del`{.language-} pour supprimer un indice d'une liste~: l'instruction `del l[1]`{.language-} supprime de la liste de nom `l`{.language-} l'indice 1. L'objet associé au nom `l`{.language-} est **modifié**, il n'est plus que de longueur 2.

```python
>>> x = [1, 4, "douze"]
>>> del x[1]
>>> x
[1, 'douze']
```

## Ajout d'un élément dans une liste

Nous utiliserons essentiellement deux façons d'ajouter des éléments à une liste, tous les deux utilisant des [méthodes](../fonctions-méthodes#méthodes) des objets de type liste.

Pour ajouter des éléments à une liste, nous utiliserons les méthodes :

* `append`{.language-} qui ajoutent un élément en fin de liste :

    ```python
    >>> x = [1, 4, "douze"]
    >>> x.append("a la fin")
    >>> x
    [1, 4, 'douze', 'a la fin']
    ```

* `insert`{.language-} qui permettent d'ajouter un élément **avant** un indice passé en paramètre. Dans l'exemple, on ajoute un élément avant le l'élément d'indice 0, c'est à dire au début :

    ```python
    >>> x = [1, 4, "douze"]
    >>> x.insert(0, "au debut")
    >>> x
    ['au debut', 1, 4, 'douze']
    >>> 
    ```

## Copie

### D'une liste

On utilise le nom de la classe `list`{.language-} qui prend en paramètre un itérable pour créer une liste. Par exemple pour créer une copie de la liste `x = [1, 2, 13]`

```python
>>> x = [1, 2, 13]
>>> y = list(x)
```

Il est pratique de copier une liste car ensuite on peut modifier une liste sans peur des effets de bords :

```python
>>> y[1] = 42
>>> x
[1, 2, 13]
>>> y
[1, 42, 13]
```

Alors que :

```python
>>> x = [1, 2, 13]
>>> y = x
>>> y[1] = 42
>>> x
[1, 42, 13]
>>> y
[1, 42, 13]
```

### <span id="slice"></span> D'une sous-liste

On peut copier une partie d'une liste.
Pour **copier la liste l à partir de l'indice i jusqu'à l'indice j avec un pas de k** par exemple : `l[i:j:k]`{.language-}

Il n'est pas nécessaire de renseigner tous les champs. Si $l = [l_0, \dots, l_{n-1}]$, alors :

* `l[i:]`{.language-} sera la liste $[l_i, \dots, l_{n-1}]$
* `l[:i]`{.language-} sera la liste $[l_0, \dots, l_{i-1}]$
* `l[i:j]`{.language-} sera la liste $[l_i, \dots, l_{j-1}]$

{% exercice %}
que donne `l[::3]`{.language-} ou `l[1::5]`{.language-} pour la liste `[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]`{.language-} ?
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

### Méthodes des listes

{% lien "**Documentation**" %}
<https://docs.python.org/fr/3/tutorial/datastructures.html#more-on-lists>
{% endlien %}

Les méthodes de listes, comme les méthodes de chaînes de caractères, sont très utiles. A défaut de les apprendre par cœur, sachez retrouver la documentation pour voir si ce que vous cherchez à faire n'est pas déjà fait.

Par exemple pour ajouter ou supprimer des éléments d'une liste :

* `append`{.language-} ajoute un élément à la fin d'une liste. Par exemple `l.append(3)`{.language-} ajoute l'entier 3 à la fin d'une liste (si `l`{.language-} valait `[1, 4]`{.language-} avant, elle vaudra `[1, 4, 3]`{.language-} après)
* `insert`{.language-} ajoute un élément à un index donné d la liste d'une liste. Par exemple `l.insert(1, "X")`{.language-} insère `"X"`{.language-} à l'indice 1 (si `l`{.language-} valait `[1, 4]`{.language-} avant, elle vaudra `[1, "X", 4]`{.language-} après)
* `del`{.language-} supprime l'élément à l'indice de la liste. Par exemple `del l[0]`{.language-} supprime l'élément d'indice 0 dune liste (si `l`{.language-} valait `[1, 4]`{.language-} avant, elle vaudra `[4]`{.language-} après)

{% exercice %}
Attention à `remove`{.language-}, `extend`{.language-} ou `pop`{.language-} qui ne font pas ce qu'on croit qu'elle font.

Que font-elles ?
{% endexercice %}
{% details "solution" %}

Voir la [documentation du tutoriel](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) :

* `remove`{.language-} supprime le **premier** élément trouvé, pas tous
* `extend`{.language-} ajoute les éléments d'une **liste** passée en paramètre à la la liste à gauche du `.`
* `pop`{.language-} supprime le dernier élément de la liste et le rend

{% enddetails %}

Il existe aussi de nombreuses méthodes de chaines de caractères qui utilisent des listes. Citons en deux :

* `split()`{.language-} est une méthode de `str`{.language-} qui produit des chaines
* `join(liste)`{.language-} est une méthode de `str{.language-} qui produit une chaîne à partir d'une liste de chaines de caractère passé en paramètre

Attention cependant lorsque vous utilisez des méthodes :

{% attention %}
Certaines méthodes ne **modifient** la liste d'autre produisent de nouvelles liste. LIsez bien la documentation associée à la méthode pour l'utiliser correctement.sur lequel elle est appliquée.
{% endattention %}

Par exemple les méthodes `append`{.language-}, `insert`{.language-}, `sort`{.language-} ou encore `reverse`{.language-} modifient la liste alors que `index`{.language-} ne le fait pas par exemple.

{% faire %}
Testez le code suivant pour voir la différence ;

```python
ma_liste = list(range(5))
ma_liste.insert(2, "coucou")
un_indice = ma_liste.index("coucou")
print(un_indice)
print(ma_liste[un_indice])
```

{% endfaire %}

## Opérateurs de listes

Comme pour les chaines de caractères :

* l'opération `+`{.language-} désigne la concaténation entre deux listes
* l'opération `*`{.language-} par en entier $i$ recopie la liste (ses éléments) $i$ fois.

Par exemple :

```python
>>> [1, 4, "douze"] + [42]
[1, 4, 'douze', 42]
>>> [1, 4, "douze"] * 3
[1, 4, 'douze', 1, 4, 'douze', 1, 4, 'douze']
```

Remarquez que :

* `[1, 4, "douze"] + 42`{.language-} produit une erreur puisque `42`{.language-} est un entier et pas une liste.
* `3 * [1, 4, "douze"]`{.language-} fonctionne également

Attention aux effets de bords :

```python
>>> M = [[0, 0, 0]] * 3
>>> M
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> M[1][1] = 1
```

{% exercice %}
Que vaut `M`{.language-} ?
{% endexercice %}
{% details "solution" %}

```python
>>> M
[[0, 1, 0], [0, 1, 0], [0, 1, 0]]
```

C'est en effet la **même** liste qui a été dupliquée !

{% enddetails %}
