---
layout: page
title:  "Bases de python : création de fonctions"
authors: 
    - Augustin Agbo-Kpati
    - François Brucker
    - Pascal Préa
---

> [bases de python]({% link cours/bases-python/index.md %}) /  [création de fonctions]({% link cours/bases-python/creation-fonctions.md %})
{: .chemin}

Une fonction est un bloc de code exécutable. On peut lui associer un nom et exécuter ce code juste en l'appelant : ceci permet de ne pas copier/coller des lignes code identiques à différents endroit du programme.

Il n'est en effet jamais bon de copier/coller un bout de programme qui se répète plusieurs fois (corriger un problème dans ce bout de code reviendrait à le corriger autant de fois qu'il a été dupliqué...). Il est de plus souvent utile de séparer les éléments logiques d'un programme en unités autonomes, ceci rend le programme plus facile à relire.

## définition d'une fonction

Une fonction est un **bloc** auquel on donne un nom (le nom de la fonction) qui peut être exécuté lorsqu'on l'invoque par son nom.

```text
def <nom>(paramètre 1, paramètre 2, ..., paramètre n):
    instruction 1
    instruction 2
    ...
    instruction n
    return <objet>
```

>notez que les paramètres et la dernière avec `return` sont optionnelles.

La partie de programme suivant définit une fonction:

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

## nom d'une fonction

Un nom de fonction est variable comme une autre. Elle est affectée dans l'espace de nom du bloc dans lequel elle est défini.

Dans le code suivant, exécuté dans un interpréteur on regarde le type d'un nom associé à une fonction :

```text
>>> def bonjour():
...     print("Salutations")
... 
>>> type(bonjour)
<class 'function'>
```

On peut aussi associer la fonction à une autre variable comme on le ferait avec n'importe quel autre objet. Dans l'exemple suivant on associe la fonction à une autre variable, `x` :

```text
>>> def bonjour():
...     print("Salutations")
... 
>>> x = bonjour
>>> x()
Salutations
```

En python, lorsque l'on exécute une fonction on dit qu'on **l'appelle**. **Appeler une variable* est alors le fait de mettre des `()` après son nom.

Si cela produit une erreur ce n'était pas une fonction. Regardez l'exemple ci-après, exécutable dans un interpréteur. On tente d'appeler un entier et python nous indique que ce n'est pas possible :

```text
>>> n = 3
>>> n()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
```

Enfin, en python être une fonction n'est rien d'autre que d'être un *objet appelable*. Savoir si un objet est appelable ou pas se fait par la fonction `callable` :

```text
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

> Pour l'instant, on ne connait que les fonctions comme objet apellable. Mais il y en a d'autres, souvent des objets que l'on crée soit même.

## Paramètres d'une fonction

```python
def plus_moins(nombre):
    if nombre > 42:
        print("Supérieur à 42")
    else:
        print("Inférieur à 42")
```

Cette fonction nécessite donc un paramètre pour être invoquée. Testez alors `plus_moins(17)`.
La variable nombre sera associée à l'objet entier de valeur 17 dans la fonction. La variable nombre n'existe que dans la fonction.

Python, à chaque exécution d'une fonction crée un espace de nom pour elle. Cet espace de nom sera détruit lorsque la fonction aura fini d'être exécutée. Une fois cet espace de nom crée, il associe le nom du paramètre à l'objet passé en paramètre.

>Les *paramètres* d'une fonction sont des **noms** de variables qui ne seront connus qu'à l'intérieur de la fonction. À l'exécution de la fonction, le nom de chaque paramètre est associé à l'objet correspondant.
{: .attention}

Regardons le bout de code suivant, qui utilise la fonction `plus_moins` définie précédemment :

```python
x = 12
plus_moins(x)
```

Lorsque python exécute la deuxième du code précédent il va :

1. créer un espace de nom pour la fonction
2. regarder les objets passés en paramètre. Ici c'est l'objet associé au nom `x`. Python cherche l'objet, c'est un entier valant 12.
3. python associe chaque objet à son nom **dans** l'espace de nom de la fonction : ici l'entier qui vaut 12 sera appelé `nombre` dans la fonction (le nom du paramètre dans la définition de la fonction).
4. python exécute la fonction.
5. à la fin de la fonction, l'espace de nom de la fonction est détruit (on ne detruit que les noms, pas les objets associés).

## paramètres par défaut

```python
def plus_moins(nombre, seuil=42):
    if nombre > seuil:
        print("Supérieur à 42")
    else:
        print("Inférieur à 42")
```

On peut alors utiliser la fonction comme précédemment ou en utilisant le paramètre seuil `plus_moins(12, seuil=34)`.

> comme le paramètre par défaut est le deuxième on peut aussi l'utiliser sans le nommer : `plus_moins(12, 34)`.

## Retour d'une fonction

Toute fonction peut rendre une valeur. On utilise le mot-clef `return` suivi de la valeur à rendre pour cela. Le fonction suivante rend le double de la valeur de l'objet passé en paramètre:

```python
def double(valeur):
    x = valeur * 2
    return x
```

Il ne sert à rien de mettre des instructions après une instruction `return` car dès qu'une fonction exécute cette instruction, elle s'arrête en rendant l'objet en paramètre. Le retour d'une fonction est pratique pour calculer des choses et peut ainsi être affecté à une variable.

> Dans un fichier, définissez la fonction précédente puis ajouter les 2 lignes ci-après. Quel est le résultat ?
{: .a-faire}

```python
x = double(21)
print(x)
```

Le code précédent exécute la fonction de nom `double` avec comme paramètre un entier de valeur 21. La fonction commence par associer à une variable nommée `valeur` l'objet passé en paramètre (ici un entier de valeur `21`), puis crée une variable de nom `x` à laquelle est associée un entier de valeur `42` et enfin se termine en retournant comme valeur l'objet de nom `x`. Les variables `valeur` et `x` définies à l'intérieur de la fonction sont ensuite effacées (pas les objets, seulement les noms).

Cette valeur retournée est utilisée par la commande `print` pour être affichée à l'écran.

>Les noms de paramètres d'une fonction et les variables déclarée à l'intérieur de la fonction n'existent qu'à l'intérieur de celle-ci. En dehors de ce blocs, ces variables n'existent plus.
{: .attention}

## Fonctions v.s. méthodes

Python vient avec de nombreuses fonctions que l'on peut utiliser. Vous en connaissez déjà comme `range`, `len`, ou encore `type`.

Ne confondez pas fonctions et méthodes. Une fonction s'exécute toute seule alors qu'une méthode a besoin d'un objet sur lequel elle s'applique (celui avant le `.`). Vous pouvez voir ça comme un 1er paramètre indispensable à l'exécution d'une méthode. Considérez le programme suivant:

```python
ma_liste = list(range(5))
ma_liste.append(10)
```

La première ligne crée une liste. La seconde instruction est une *méthode* (`append`) qui s'applique à l'objet de nom `ma_liste` et qui a un paramètre (ici un entier valant `10`).

> On peut voir les méthodes comme des fonctions définies dans l'espace de nom de l'objet.

Attention cependant lorsque vous utilisez des méthodes. Certaines méthodes ne rendent rien et modifient l'objet sur lequel elle est appliquée, c'est le cas des méthodes `append`, `insert` ou encore `reverse`, alors que d'autres rendent des objets, c'est le cas de `index` par exemple.

> Testez le code suivant pour voir la différence ;
{: .a-faire}

```python
ma_liste = list(range(5))
ma_liste.insert(2, "coucou")
un_indice = ma_liste.index("coucou")
print(un_indice)
print(ma_liste[un_indice])
```

## fonction en paramètre

```python
def produit(x, y):
    return x * y

def calcul(fct, z):
    return z + fct(2, 17)

print(calcul(produit, 8))
```

> exécutez le code précédent et expliquer son fonctionnement
{: .a-faire}
{% details solution %}

On passe une fonction en paramètre de la fonction `calcul`. Le retour de `calcul(produit, 8)` est alors égal à $8 + (2 * 17) = 42$ puisque `fct` est alors la fonction `produit`.

{% enddetails %}
