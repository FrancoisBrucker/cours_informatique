---
layout: page
title:  "exercices sur la création d'objets et leurs composition : corrigé"
category: cours
tags: informatique cours 
authors: 
  - François Brucker
  - Célia Châtel
---

## dice 

### modèle UML  {#dice-uml}

Diagramme UML du dé :

![dice]({{ "/assets/cours/developpement/programmation-objet/dice_no_class_att.png" | relative_url }}){:style="margin: auto;display: block}

### code python {#dice-python}

Fichier *"dice.py"*

```python
import random


class Dice:
    def __init__(self, position=1):
        self._position = position

    def get_position(self):
        return self._position

    def set_position(self, nouvelle_position):
        self._position = nouvelle_position

    def roll(self):
        self._position = random.randint(1, 6)
```

### main {#dice-main}

Fichier *"main_dice.py"* :

```python
from dice import Dice

d = Dice()
print(d.get_position())

d2 = Dice(4)
print(d2.get_position())

d.set_position(6)
print(d.get_position())

d2.roll()
print(d2.get_position())
```

### tests {#dice-tests}

Fichier *"test_dice.py"* :

```python
from dice import Dice


def test_dice_creation_no_argument():
    dice = Dice()
    assert dice.get_position() == 1


def test_set_position():
    dice = Dice()
    assert dice.get_position() == 1
    dice.set_position(3)
    assert dice.get_position() == 3


def test_roll():
    dice = Dice()
    dice.roll()
    assert 1 <= dice.get_position() <= 6
```

### 5 dés

```python
from dice import Dice

  tapis = []
  for i in range(5):
      tapis.append(Dice())

  print("======")
  for d in tapis:
      print(d.get_position())

  for d in tapis:
      d.roll()

  print("======")
  for d in tapis:
      print(d.get_position())
```

## tapis vert

### uml {#tapis-vert-uml}

Diagramme UML du tapis-vert :

![tapis vert]({{ "/assets/cours/developpement/programmation-objet/tapisvert-uml.png" | relative_url }}){:style="margin: auto;display: block}

>Notez le lien de composition entre les deux classes.

### code python {#tapis-vert-python}

Fichier *"tapisvert.py"* :

```python
from dice import Dice


class TapisVert:
    def __init__(self):
        temp = []
        for i in range(5):
            temp.append(Dice())
        self._dices = tuple(temp)

    def get_des(self):
        return self._dices

    def roll(self):
        for dice in self._dices:
            dice.roll()

    def somme(self):
        s = 0
        for d in self._dices:
            s += d.get_position()
        return s
```

### main {#tapis-vert-main}

Fichier *"main_tapisvert.py"* :

```python
from tapisvert import TapisVert

tv = TapisVert()

for d in tv.get_des():
    print(d.get_position())
print('-----')
print(tv.somme())
print('=====')

tv.roll()
for d in tv.get_des():
    print(d.get_position())
print('-----')
print(tv.somme())
print('=====')

```

### tests {#tapis-vert-tests}

```python
from tapisvert import TapisVert


def test_init():
    tv = TapisVert()
    assert tv is not None


def test_somme():
    tv = TapisVert()

    assert tv.somme() == 5


def test_roll():
    tv = TapisVert()
    tv.roll()
    for d in tv.get_des():
        assert 1 <= d.get_position() <= 6
```

## pour aller plus loin

### str pour les dés

```python

class Dice:
    # ...

    def __str__(self):
        return "Dice(position=" + str(self._position) + ")"
    
    # ...
```

### analyse du code

Les différents objets et espaces de noms (les flèches avec un petit carré) sont rassemblés dans la figure ci-après :

![espace de noms]({{ "/assets/cours/developpement/programmation-objet/espace_nom_tapis_vert.png" | relative_url }}){:style="margin: auto;display: block}

L'exécution de la commande `tapis_vert.roll()` se déroule alors comme suit (on a mis le début jusqu'à l'exécution de la méthode `dice.roll`) :

1. c'est une l'exécution du nom `roll` de l'espace de nom associé à l'objet de nom `tapis_vert` de l'espace de nom de *main.py*
2. il existe un nom `tapis_vert` dans l'espace de nom de *main.py* associé à un objet de la classe `TapisVert`.
3. on cherche donc le nom `roll` dans l'espace de nom de cet objet. Il n'y est pas
4. lorsqu'un nom n'est pas dans l'espace de nom d'un objet, on cherche dans sa classe et *bingo* c'est un nom de méthode. On exécute alors cette méthode :
   1. on crée un espace de nom pour cette méthode
   2. on place les paramètre de la méthode dans cet espace de nom. Ici il n'y a qu'un paramètre de nom `self` associé à l'objet appelant (c'est à dire l'objet de la classe `TapisVert`)
   3. la méthode consiste en une boucle for, qui itère sur l'objet associé au nom `self.dices` dans l'espace de nom de la méthode.
   4. comme `self` est l'objet de la classe `TapisVert`, il possède un nom `dices` dans son espace de nom qui est une liste de 5 objets de la classe `Dice`
   5. lors de l'itération le nom `dice` crée par la boucle for sera associé itérativement à chaque élément de la liste, c'est à dire à chaque objet de la classe `Dice`
   6. La boucle for exécute l'objet associé au nom  `dice.roll`.
   7. le nom `roll` n'existe pas dans l'objet de nom `dice` dans l'espace de nom de la méthode. Mais il existe dans sa classe, la classe `Dice`.
   8. on exécute la méthode `roll` de la classe `Dice` :
      1. on crée un espace de nom pour cette méthode et on y place le nom `self` correspondant à l'objet à gauche du point, ici l'objet associé au nom `dice` dans l'espace de nom de la méthode `roll` de la classe `TapisVert`
      2. l'exécution de cette méthode cherche un nom `random.randint`. Ce nom n'existe pas dans l'espace de nom de la méthode, du coup on remonte. Quand un objet n'existe pas dans l'espace de nom d'une méthode, on cherche dans l'espace de nom principal. Notez que c'est différent du fait de cherche un nom dans un objet, pour lequel on remonte à sa classe. Pour un espace de nom de méthode, on monte à l'espace de nom du fichier. Ici on le trouve puisque c'est dans un import. Le nom correspond au nom `randint` dans l'espace de nom `random` qui existe dans l'espace de nom du fichier *dice.py* (ouf).
      3. l'exécution du nom `random.randint` rend un entier qui est associé au nom `position` dans l'espace de nom de l'objet associé à `self` dans l'espace de nom de la méthode roll de `Dice`, ici un des dés.
   9. la méthode `roll` de la classe `Dice` est finie, son espace de nom disparait.
5. une fois la boucle for finie, la méthode `roll` de `TapisVert` est finie, son espace de nom disparait.

### paires etc pour le tapis vert

```python
class TapisVert:
    # ...

    def _nb_des_identiques(self, nb_times):
        count = [0] * 7
        for dice in self.dices:
            count[dice.get_position()] += 1
        for i in range(len(count)):
            if count[i] >= nb_times:
                return True
        return False

    def est_pair(self):
        return self._nb_des_identiques(2)

    def est_brelan(self):
        return self._nb_des_identiques(3)

    def est_carre(self):
        return self._nb_des_identiques(4)

    def _lance_jusqua_nb_identique(self, number):
        while not self._nb_des_identiques(number):
            self.roll()

    def roll_jusqua_pair(self):
        self._lance_jusqua_nb_identique(2)

    def roll_jusqua_brelan(self):
        self._lance_jusqua_nb_identique(3)

    def roll_jusqua_carre(self):
        self._lance_jusqua_nb_identique(4)

    # ...
```
