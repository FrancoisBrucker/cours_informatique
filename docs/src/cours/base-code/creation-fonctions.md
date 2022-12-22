---
layout: layout/post.njk 
title: Créer ses fonctions

eleventyNavigation:
  key: "Créer ses fonctions"
  parent: "Bases en code et python"
---

<!-- début résumé -->

Création de ses propres fonctions avec des blocs.

<!-- end résumé -->

Une fonction est un bloc de code exécutable. On peut lui associer un nom et exécuter ce code juste en l'appelant : ceci permet de ne pas copier/coller des lignes code identiques à différents endroit du programme.

Il n'est en effet jamais bon de copier/coller un bout de programme qui se répète plusieurs fois (corriger un problème dans ce bout de code reviendrait à le corriger autant de fois qu'il a été dupliqué...). Il est de plus souvent utile de séparer les éléments logiques d'un programme en unités autonomes, ceci rend le programme plus facile à relire.

## Définition d'une fonction

{% note %}
Une ***fonction*** est un [bloc](../blocs) auquel on donne un nom (le nom de la fonction) qui peut être exécuté lorsqu'on l'invoque par son nom.

```text
def <nom>(paramètre 1, paramètre 2, ..., paramètre n):
    instruction 1
    instruction 2
    ...
    instruction n
    return <objet>
```

{% endnote %}
{% info %}
Les paramètres et la dernière la dernière ligne avec `return`{.language-} sont optionnelles.
{% endinfo %}

La partie de programme suivant définit une fonction :

```python
def bonjour():
    print("Salutations")
```

La première ligne est la définition du bloc fonction. Il contient :

* un mot clé spécial précisant que l'on s'apprête à définir une fonction: `def`
* le nom de la fonction. Ici `bonjour`
* des parenthèses qui pourront contenir des paramètres (on verra ça plus tard)
* le `:` qui indique que la ligne d'après va commencer le bloc proprement dit
  
Ensuite vient le bloc fonction en lui-même qui ne contient ici qu'une seule ligne.

Si on exécute le bloc précédent, il ne se passe rien. En effet on n'a fait que définir la fonction. Pour l'utiliser, ajoutez `bonjour()` à la suite du bloc.

Une **fonction** s'utilise toujours en faisant suivre son nom d'une parenthèse contenant ses paramètres séparés par une virgule (notre fonction n'a pour l'instant pas de paramètres). Donner juste son nom ne suffit pas à l'invoquer.

## Nom d'une fonction

Un nom de fonction est variable comme une autre. Elle est affectée dans l'espace de nom du bloc dans lequel elle est défini.

Dans le code suivant, exécuté dans un interpréteur on regarde le type d'un nom associé à une fonction :

```python
>>> def bonjour():
...     print("Salutations")
... 
>>> type(bonjour)
<class 'function'>
```

On peut aussi associer la fonction à une autre variable comme on le ferait avec n'importe quel autre objet. Dans l'exemple suivant on associe la fonction à une autre variable, `x`{.language-} :

```python
>>> def bonjour():
...     print("Salutations")
... 
>>> x = bonjour
>>> x()
Salutations
```

En python, lorsque l'on exécute une fonction on dit qu'on **l'appelle**. ***Appeler une variable*** est alors le fait de mettre des `()` après son nom.

Si cela produit une erreur ce n'était pas une fonction. Regardez l'exemple ci-après, exécutable dans un interpréteur. On tente d'appeler un entier et python nous indique que ce n'est pas possible :

```python
>>> n = 3
>>> n()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
```

Enfin, en python être une fonction n'est rien d'autre que d'être un ***objet appelable***. Savoir si un objet est appelable ou pas se fait par la fonction `callable`{.language-} :

```python
>>> def bonjour():
...     print("Salutations")
... 
>>> callable(bonjour)
True
>>> callable(1)
False
>>> callable("ee")
False
```

{% info %}
Pour l'instant, on ne connaît que les fonctions comme objet appelable. Mais il y en a d'autres, souvent des objets que l'on crée soit même.
{% endinfo %}

## Paramètres d'une fonction

```python
def plus_moins(nombre):
    if nombre > 42:
        print("Supérieur à 42")
    else:
        print("Inférieur à 42")
```

Cette fonction nécessite donc un paramètre pour être invoquée. Testez alors `plus_moins(17)`{.language-}.
La variable nombre sera associée à l'objet entier de valeur 17 dans la fonction. La variable nombre n'existe que dans la fonction.

Python, à chaque exécution d'une fonction crée un espace de nom pour elle. Cet espace de nom sera détruit lorsque la fonction aura fini d'être exécutée. Une fois cet espace de nom crée, il associe le nom du paramètre à l'objet passé en paramètre.

{% attention %}
Les *paramètres* d'une fonction sont des **noms** de variables qui ne seront connus qu'à l'intérieur de la fonction. À l'exécution de la fonction, le nom de chaque paramètre est associé à l'objet correspondant.
{% endattention %}

Regardons le bout de code suivant, qui utilise la fonction `plus_moins`{.language-} définie précédemment :

```python
x = 12
plus_moins(x)
```

Lorsque python exécute la deuxième du code précédent il va :

1. créer un espace de nom pour la fonction
2. regarder les objets passés en paramètre. Ici c'est l'objet associé au nom `x`. Python cherche l'objet, c'est un entier valant 12.
3. python associe chaque objet à son nom **dans** l'espace de nom de la fonction : ici l'entier qui vaut 12 sera appelé `nombre` dans la fonction (le nom du paramètre dans la définition de la fonction).
4. python exécute la fonction.
5. à la fin de la fonction, l'espace de nom de la fonction est détruit (on ne détruit que les noms, pas les objets associés).

{% exercice %}
Créez et testez une fonction nommée `cube`{.language-} qui prend un entier en paramètre et affiche cet élément au cube.
{% endexercice %}
{% details "solution" %}

```python
def cube(x):
    print(x ** 3)
```

{% enddetails %}

{% exercice %}
Créez et testez une fonction nommée `puissance`{.language-} qui prend entiers entiers en paramètre et affiche le premier paramètre élevé à la puissance du second paramètre.
{% endexercice %}
{% details "solution" %}

```python
def puissance(x, y):
    print(x ** y)
```

{% enddetails %}

## Paramètres par défaut

```python
def plus_moins(nombre, seuil=42):
    if nombre > seuil:
        print("Supérieur à 42")
    else:
        print("Inférieur à 42")
```

On peut alors utiliser la fonction comme précédemment ou en utilisant le paramètre seuil `plus_moins(12, seuil=34)`{.language-}.

{% info %}
Comme le paramètre par défaut est le deuxième on peut aussi l'utiliser sans le nommer : `plus_moins(12, 34)`{.language-}
{% endinfo %}

{% exercice %}
Créez et testez une fonction nommée `puissance`{.language-} qui prend deux entiers en paramètre et affiche le premier paramètre élevé à la puissance du second paramètre. Le second paramètre vaut 2 par défaut.
{% endexercice %}
{% details "solution" %}

```python
def puissance(x, y=2):
    print(x ** y)
```

{% enddetails %}

## Retour d'une fonction

Toute fonction peut rendre une valeur. On utilise le mot-clef `return`{.language-} suivi de la valeur à rendre pour cela. Le fonction suivante rend le double de la valeur de l'objet passé en paramètre:

```python
def double(valeur):
    x = valeur * 2
    return x
```

Il ne sert à rien de mettre des instructions après une instruction `return`{.language-} car dès qu'une fonction exécute cette instruction, elle s'arrête en rendant l'objet en paramètre. Le retour d'une fonction est pratique pour calculer des choses et peut ainsi être affecté à une variable.

{% faire %}
Dans un [notebook](../notebooks) ou deans spyder, définissez la fonction précédente dans une cellule puis exécutez là.

Puis, dans une seconde cellules collez la ligne ci-après puis exécutez la.

```python
double(21)
```

{% endfaire %}

Le résultat de la cellule devrait être : 42.

En effet, le code précédent exécute la fonction de nom `double`{.language-} avec comme paramètre un entier de valeur 21. La fonction commence par associer à une variable nommée `valeur`{.language-} l'objet passé en paramètre (ici un entier de valeur `21`{.language-}), puis crée une variable de nom `x`{.language-} à laquelle est associée un entier de valeur `42`{.language-} et enfin se termine en retournant comme valeur l'objet de nom `x`{.language-}. Les variables `valeur`{.language-} et `x`{.language-} définies à l'intérieur de la fonction sont ensuite effacées (pas les objets, seulement les noms).

Cette valeur retournée est utilisée par la commande `print`{.language-} pour être affichée à l'écran.

{% attention %}
Les noms de paramètres d'une fonction et les variables déclarée à l'intérieur de la fonction n'existent qu'à l'intérieur de celle-ci. En dehors de ce blocs, ces variables n'existent plus.
{% endattention %}

{% exercice %}
Créez et testez une fonction nommée `puissance`{.language-} qui prend deux entiers en paramètre et rend le premier paramètre élevé à la puissance du second paramètre. Le second paramètre vaut 2 par défaut.
{% endexercice %}
{% details "solution" %}

```python
def puissance(x, y=2):
    return x ** y
```

{% enddetails %}

## fonction en paramètre

```python
def produit(x, y):
    return x * y

def calcul(fct, z):
    return z + fct(2, 17)

print(calcul(produit, 8))
```

{% exercice %}
Exécutez le code précédent et expliquer son fonctionnement
{% endexercice %}
{% details "solution" %}

On passe une fonction en paramètre de la fonction `calcul`{.language-}. Le retour de `calcul(produit, 8)`{.language-} est alors égal à $8 + (2 * 17) = 42$ puisque `fct`{.language-} est alors la fonction `produit`{.language-}.

{% enddetails %}

## Lambda

{% lien %}
<https://python-reference.readthedocs.io/en/latest/docs/operators/lambda.html>
{% endlien %}

Les lambda sont ue façon d'écrire rapidement une fonction avec une unique instruction.

Les deux codes suivant sont identiques :

```python
double = lambda x: 2 * x
```

et :

```python
def double(x):
    return 2 * x
```

Le principal intérêt de ces fonction est d'être utilisée comme paramètre d'autres fonction.

Par exemple avec `sort` et son paramètre key. Considérons la liste `l`{.language-} :

```python
l = [["au revoir", 2], ["bonjour", 1]]
```

Si on cherche à trier `l`{.language-}, la liste sera triée en comparant le 1er élément de chaque liste :

```python
l.sort()

print(l)  # donnera [['au revoir', 2], ['bonjour', 1]]
```

Si l'on veut trier de façon spécifique, on utilise le paramètre `key` qui est une fonction. Les éléments $x$ de la liste seront triés selon $key(x)$ plutôt que $x$ :

```python
def second(x):
    return x[1]

l.sort(key=second)

print(l)  # donnera [['bonjour', 1], ['au revoir', 2]]
```

Utiliser une fonction lambda permet de raccourcir le code précédent tout en le gardant très clair :

```python
l.sort(key=lambda x: x[1])

print(l)  # donnera [['bonjour', 1], ['au revoir', 2]]
```
