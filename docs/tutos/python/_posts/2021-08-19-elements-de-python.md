---
layout: page
title:  éléments du langage python
categories: langage python
authors: 
    - Augustin Agbo-Kpati
    - François Brucker
    - Pascal Préa
---

On rassemble ici les notions qui n'ont pas encore été ajoutées au coure de développement.

<!--more-->

### Les structures de données

* list comprehenstion
* fonction lambda


#### Les dictionnaires

> * <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>
> * <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>

Un dictionnaire (ou [tableau associatif](http://fr.wikipedia.org/wiki/Tableau_associatif)) permet d'associer des clés à des valeurs, ces clés pouvant être des chaines de caractères ou des nombres. C'est en gros comme une 'liste' où l'on remplace les indices par à peu près ce que l'on veut.

```python
d = {} #on crée un dictionnaire vide
d["quarante deux"] = 42 #on associe à la clé "quarante deux" la valeur 42
d[3.14] = "pi" #on associe à la clé 3.14 la valeur "pi"
print("quarante deux" in d)
print(42 in d)
for cle in d:
    print("cle :", cle, "valeur :", d[cle])
```

> **Attention** : Un dictionnaire n'est pas ordonné, L'ordre dans lequel les valeurs sont examniés dans une boucle for par exmple n'est pas défini.

#### Les ensembles : set

> <https://docs.python.org/3/library/stdtypes.htm#set>

Un ensemble permet de garder des données en mémoire de manière non indexée. Contrairement aux listes, où l'on rangeait les éléments dans des cases distinctes, on ne peut **pas** accéder aux éléments d'un ensemble `d` avec `d[i]`.

#### Notion d'objets mutables

Les objets que nous avons rencontrés sont mutables, c'est à dire que lorsque on crée une liste `l = [1, 2, 3]`, il est toujours possible de changer la valeur d'un indice, ou d'ajouter un élément.

Cela n'est toutefois pas possible avec les [tuples](https://docs.python.org/3/library/stdtypes.html#tuples) par exemple.

Un tuple peut se créer de la manière suivante :

```python
t = (1, 2, 3)
```

Essayez maintenant des commandes telles que :

```python
t[0] = 10
t.append(42)
```

Cela nous renvoie alors des erreurs.

Pour ajouter un élément, il faut créer un autre tuple :

```python
t2 = t + (1, )
```

Le [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset) est un `set` (ensemble), mais cette fois non mutable.


### Boucle for

#### Les itérateurs

Pour faire simple, les itérateurs sont des objets qui permettent de créer des suites de données.
Prenons un exemple connu: `range()`

range permet de créer des itérateurs : `range(10)` est un itérateur qui va renvoyer les valeurs de 0 à 9.

Pour utiliser `for`, il faut un itérateur tel que: `for x in mon_iterateur` est la syntaxe.

Exemple :

```python
mon_iterateur = range(10)
for x in mon_iterateur:
    print(x)
```

Essayez ce code et comprenez le : les itérateurs sont de puissants objets python.

Vous pouvez créer votre propre itérateur à l'aide de l’instruction `yield`

```python
def mon_iterateur(valeur):
    for x in range(valeur):
        yield valeur * x

for x in mon_iterateur(5):
    print(x)
```

Ce qui va s'afficher sera :

```python
0
5
10
15
20
```

On peut également boucler sur une liste, qui est un **objet itérable** :

```python
l = ["Jet fuel", "can't", "melt", "steel beams"]
for mot in l:
    print(mot)
```

## Méthodes, fonctions et modules

### Les fonctions

#### Motivations

> <https://docs.python.org/3/reference/compound_stmts.html#function-definitions>

Il n'est jamais bon de copier/coller un bout de programme qui se répète plusieurs fois (corriger un problème dans ce bout de code reviendrait à le corriger autant de fois qu'il a été dupliqué...). Il est de plus souvent utile de séparer les éléments logiques d'un programme en unités autonomes, ceci rend le programme plus facile à relire.

Pour cela, on utilise des *fonctions*.

Une fonction est un [bloc](#blocs-id) auquel on donne un nom (le nom de la fonction) qui peut être exécuté lorsqu'on l'invoque par son nom.

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
  
Ensuite vient le bloc fonction en lui-même qui ne contient qu'une seule ligne.

Si on exécute le bloc précédent, il ne se passe rien. En effet on n'a fait que définir la fonction. Pour l'utiliser, ajoutez `bonjour()` à la suite du bloc.

>Une **fonction** s'utilise toujours en faisant suivre son nom d'une parenthèse contenant ses paramètres séparés par une virgule (notre fonction n'a pour l'instant pas de paramètres). Donner juste son nom ne suffit pas à l'invoquer.

#### Paramètres d'une fonction

```python
def plus_moins(nombre):
    if nombre > 42:
        print("Supérieur à 42")
    else:
        print("Inférieur à 42")
```

Cette fonction nécessite donc un paramètre pour être invoquée. Testez alors `plus_moins(17)`.
La variable nombre sera associée à l'objet entier de valeur 17 dans la fonction. La variable nombre n'existe que dans la fonction.

>Les *paramètres* d'une fonction sont des **noms** de variables qui ne seront connus qu'à l'intérieur de la fonction. À l'exécution de la fonction, le nom de chaque paramètre est associé à l'objet correspondant.
{: .attention}

#### Retour d'une fonction

Toute fonction peut rendre une valeur. On utilise le mot-clef `return` suivi de la valeur à rendre pour cela. Le fonction suivante rend le double de la valeur de l'objet passé en paramètre:

```python
def double(valeur):
    x = valeur * 2
    return x
```

Il ne sert à rien de mettre des instructions après une instruction `return` car dès qu'une fonction exécute cette instruction, elle s'arrête en rendant l'objet en paramètre. Le retour d'une fonction est pratique pour calculer des choses et peut ainsi être affecté à une variable.

Ainsi, avec la fonction double précédemment définie, testez :

```python
x = double(21)
print(x)
```

Le code précédent exécute la fonction de nom `double` avec comme paramètre un entier de valeur 21. La fonction commence par associer à une variable nommée `valeur` l'objet passé en paramètre (ici un entier de valeur `21`), puis crée une variable de nom `x` à laquelle est associée un entier de valeur `42` et enfin se termine en retournant comme valeur l'objet de nom `x`. Les variables `valeur` et `x` définies à l'intérieur de la fonction sont ensuite effacées (pas les objets, seulement les noms).

Cette valeur retournée est utilisée par la commande `print` pour être affichée à l'écran.

>Les noms de paramètres d'une fonction et les variables déclarée à l'intérieur de la fonction n'existent qu'à l'intérieur de celle-ci. En dehors de ce blocs, ces variables n'existent plus.
{: .attention}

#### Fonctions v.s. méthodes

Python vient avec de nombreuses fonctions que l'on peut utiliser. Vous en connaissez déjà comme `range`, `len`, ou encore `type`.

Ne confondez pas fonctions et méthodes. Une fonction s'exécute toute seule alors qu'une méthode a besoin d'un objet sur lequel elle s'applique (celui avant le `.`). Vous pouvez voir ça comme un 1er paramètre indispensable à l'exécution d'une méthode. Considérez le micro-programme suivant:

```python
ma_liste = range(5)
ma_liste.append(10)
```

La première ligne exécute une *fonction* (range) avec un paramètre qui rend une liste. La seconde instruction est une *méthode* (`append`) qui s'applique à l'objet de nom `ma_liste` et qui a un paramètre (ici un entier valant `10`).

Le point un peu délicat est que certaines méthodes ne rendent rien et modifient l'objet sur lequel elle est appliquée, c'est le cas des méthodes `append`, `insert` ou encore `reverse`, alors que d'autres rendent des objets, c'est le cas de `index` par exemple.

```python
ma_liste = range(5)
ma_liste.insert(2, "coucou")
un_indice = ma_liste.index("coucou")
print(un_indice)
print(ma_liste[un_indice])
```

### Visibilité d'un objet

Les noms des objets sont accessibles à l’intérieur du ''bloc unitaire'' dans lequel ils sont déclarés ainsi que dans les blocs unitaires contenus dans celui-ci. Les blocs unitaires sont :

* les fonctions,
* les modules (nous verrons cela),
* les classes (que nous ne verrons pas).

Les variables définies dans une fonction cachent les variables définies dans des blocs supérieurs. Ainsi,
le code suivant imprime 42 puisque la variable `x` déclarée dans le bloc unitaire de la fonction n'existe plus dans son bloc parent. La variable `x` valant 42 est masquée dans la fonction par une nouvelle variable de nom `x` valant 24.

```python
def f():
    x = 24

x = 42
f()
print(x)
```

De la même manière, que donne le programme suivant ? :

```python
def f(parametre):
    parametre = 24

f(2)
print(parametre)
```

>Les noms déclarés dans une fonction, y compris ses paramètres, restent dans la fonction.
{: .attention}

### Récursion

#### Modification d'objets dans une fonction

Dans un programme récursif, on a souvent besoin de modifier le même objet plusieurs fois. Même si la fonction récursive ne rend rien. Pour cela, on doit modifier les objets passés en paramètres. Pour comprendre comment cela marche, considérez la fonction suivante :

```python
def ajoute_max(liste_en_parametre):
    maximum_liste = max(liste_en_parametre)
    liste_en_parametre.append(maximum_liste)
```

Cette fonction ajoute à la fin d'une liste passée en paramètre son maximum (au passage, on a apprit une nouvelle fonction, `max`.
regardons le programme suivant qui utilise cette fonction :

```python
x = list(range(1, 6, 2))
ajoute_max(x)
print(x)
```

![nom et objets]({{ "/assets/tutos/bases-de-python/obj_nom.png" | relative_url }}){:style="margin: auto;display: block;"}

La figure précédente montre ce qu'il s'est passé dans le monde des noms et des objets. Il reste un objet sans nom après l'exécution de la fonction (un entier valant 9), il est détruit. On a pu ainsi modifier un objet sans utiliser de retour de fonction. C'est une technique puissante mais à n'utiliser qu'à bon escient.

### Modules

Un *module* (aussi appelé *bibliothèque* ou *library*) est un ensemble de fonctions utiles, utilisables dans de nombreux programmes. Plutôt que de refaire à chaque fois ces fonctions ou (c'est pire) de les copier/coller dans chaque programme, on les importe directement pour les utiliser.

>Il existe de nombreux modules, réalisant une foultitude d'opérations. Avant de se mettre à coder quelque chose, commencez toujours par vérifier (google
> est votre ami) s'il n'existe pas un module tout fait, vous gagnerez du temps. Python en fournit déjà de [nombreux](https://docs.python.org/3/library/index.html)

Pour utiliser un module, il faut commencer par l'importer avec la commande `import`. Par exemple avec le module `math`.

#### Importation directe du module

On met le nom complet avant chaque appel :

```python
import math
pi_sur_deux = math.pi / 2 #PI est défini dans le module math
x = math.cos(pi_sur_deux) #on utilise la fonction cosinus du module math
```

#### Importation d'une méthode particulière

Ceci peut être dangereux si des fonctions différentes possèdent le même nom.

```python
from math import cos, pi #importation directe de cos et de pi
x = cos(pi / 2)
```

#### Importation de toutes les fonctions du modules

Déconseillée dans la plupart des cas car on ne sait pas vraiment ce qui a été importé.

```python
from math import *
y = log(e)
```

#### Modules utiles

De nombreux modules existent pour python et permettent de réaliser aisément de très nombreuses tâches. Pour python, si avez les droits administrateurs on pourra utiliser l'utilitaire [pip](https://pypi.org/project/pip/) qui est l'installeur de package python3 (attention, si vous tapez juste pip, vous installerez des module pour la version 2 de python...).

Si vous n'avez pas de droits administrateur, ou pour une utilisation plus "pro" des modules, on préfèrera créer des environnements virtuels avec *virtualenv*, mais ceci  dépasse (de peu) le cadre de notre introduction à python.

>Si vous utilisez un interpréteur qui s'appelle `python3` et pas `python`, il est fort possible que le programme `python`(sans le 3) soit un interpréteur de la version 2 de python. Il vous faut alors utiliser la commande `pip3`et non `pip` (qui sera elle associée à l'interpréteur `python`)
{: .attention}

##### Le module random

> <https://docs.python.org/3/library/random.html>

Regardez [ces exemples](https://python.sdv.univ-paris-diderot.fr/08_modules/#85-module-random-generation-de-nombres-aleatoires) pour le module random.

Installé par défaut, il permet notamment de mélanger les éléments d'une liste, générer un nombre aléatoire, choisir un élément aléatoire dans une liste... Vous pouvez même simuler une loi Gaussienne (si, si).

##### openpyxl

> <http://openpyxl.readthedocs.org>

Permet de manipuler des [fichiers excel avec python](https://automatetheboringstuff.com/chapter12/).

Il s'installe avec pip : `pip install openpyxl` (ou `sudo pip3 install openpyxl` suivi de votre mot de passe si vous êtes sous unix/mac).

##### matplotlib

> <http://matplotlib.org>

Installé par défaut si vous utilisez l'interpréteur d'[anaconda](https://www.anaconda.com/), ce module permet d'afficher des graphiques en python.

##### Jupyter

> <http://jupyter.org>

Permet d'utiliser python de façon interactive (il s'installe aisément avec pip par exemple) 

## Retour sur les objets

Comme on l'a vu les objets sont partout en python, qu'ils soient `int`, `str`, `float`, ou même des fonctions.
Si vous avez bien compris l'exemple de la récursion et de la modification d'un objet passé en paramètre, alors vous vous demandez peut-être "pourquoi ne pas envoyer une fonction en paramètre d'une autre fonction ?"

Eh bien cela est tout à fait possible, exemple:

```python
def produit(x, y):
    return x * y

def calcul(fonction, z):
    return z + fonction(2, 17)

print(calcul(produit, 8)) #On envoie l'objet associé au nom 'produit' à la fonction 'calcul'
```

Ce programme affichera alors 42 ! Essayez-le pour vous en persuader.

## Les fichiers : lecture, écriture

> <https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files>

### Lecture

Pour lire le fichier ligne par ligne :

```python
f = open('fichier.txt', 'r')

for ligne in f:
    print(l)
f.close()
```

Ou de façon équivalente avec `with`, qui est la façon recommandée  car elle délimite l'utilisation du fichier dans un bloc :

```python
with open('fichier.txt', 'r') as f:
    for ligne in f:
        print(l)
```

On peut aussi compter le nombre de mots dans le texte, par exemple:

```python
    nombre_mots = 0
with open('fichier.txt', 'r') as f:
    for ligne in f:
        ligne = ligne.strip("\n")
        mots = ligne.split(' ')

        nombre_mots += len(mots)

print(nombre_mots)
```

### Écriture

Pour lire-écrire, ouvrez le fichier avec 'r+' au lieu de 'r'. Pour l'écriture seule, 'w'.

>Ouvrir en écriture un fichier existant **l'efface**. Pour ajouter des choses à la fin d'un fichier on utilise 'a' (pour append)
{: .attention}

Utilisez ensuite la méthode `write()`:

```python
with open('fichier.txt', 'w') as f:
    f.write('For the night is dark and full of terrors')
```
