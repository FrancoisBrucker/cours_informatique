---
layout: page
title:  éléments du langage python
categories: langage python
authors: 
    - Augustin Agbo-Kpati
    - François Brucker
    - Pascal Préa
---

On rassemble ici les notions qui n'ont pas encore été ajoutées au cours de développement.

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

## Modules utiles

De nombreux modules existent pour python et permettent de réaliser aisément de très nombreuses tâches. Pour python, si avez les droits administrateurs on pourra utiliser l'utilitaire [pip](https://pypi.org/project/pip/) qui est l'installeur de package python3 (attention, si vous tapez juste pip, vous installerez des module pour la version 2 de python...).

Si vous n'avez pas de droits administrateur, ou pour une utilisation plus "pro" des modules, on préfèrera créer des environnements virtuels avec *virtualenv*, mais ceci  dépasse (de peu) le cadre de notre introduction à python.

On utilise l'utilitaire `pip` via python avec la commande : `python -m pip [des commandes pip]` (ou `python3 -m pip3 [des commandes pip]` si vous êtes sous mac ou linux)

>Si vous utilisez un interpréteur qui s'appelle `python3` et pas `python`, il est fort possible que le programme `python`(sans le 3) soit un interpréteur de la version 2 de python. Il vous faut alors utiliser la commande `pip3`et non `pip` (qui sera elle associée à l'interpréteur `python`)
{: .attention}

### Le module random

> <https://docs.python.org/3/library/random.html>

Regardez [ces exemples](https://python.sdv.univ-paris-diderot.fr/08_modules/#85-module-random-generation-de-nombres-aleatoires) pour le module random.

Installé par défaut, il permet notamment de mélanger les éléments d'une liste, générer un nombre aléatoire, choisir un élément aléatoire dans une liste... Vous pouvez même simuler une loi Gaussienne (si, si).

### openpyxl

> <http://openpyxl.readthedocs.org>

Permet de manipuler des [fichiers excel avec python](https://automatetheboringstuff.com/chapter12/).

Il s'installe avec pip : `python -m pip install openpyxl` (ou `sudo python3 -m pip3 install openpyxl` suivi de votre mot de passe si vous êtes sous unix/mac).

### matplotlib

> <http://matplotlib.org>

Installé par défaut si vous utilisez l'interpréteur d'[anaconda](https://www.anaconda.com/), ce module permet d'afficher des graphiques en python.

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
