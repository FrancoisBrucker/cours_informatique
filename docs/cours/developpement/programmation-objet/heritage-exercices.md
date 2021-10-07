---
layout: page
title:  "Héritage"
category: cours
tags: mie
authors: 
  - François Brucker
  - Célia Châtel
---

Présentation du mécanisme d'héritage qui permettant de factoriser du code entre classes.

## implémentez les exemple du cours

### tests

### donjons et dragons utilisation
une utilisation  à mettre en oeuvre

vérifier bien que les @property fonctionne.

### Le dé

Nous allons ici réutiliser la classe `Dice` entamée la dernière fois. Pour être sûr de repartir sur de bonnes bases, utilisez l'implémentation minimale suivante (dans un fichier `dice.py`) :


~~~ python
import numpy.random


class Dice:
    NUMBER_FACES = 6

    def __init__(self, position=1, probabilities=None):
        self.position = position
        if probabilities:
            self.probabilities = probabilities
        else:
            self.probabilities = [1 / self.NUMBER_FACES] * self.NUMBER_FACES

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position

    def roll(self):
        self.set_position(numpy.random.choice([i for i in range(1, self.NUMBER_FACES + 1)], p=self.probabilities))
~~~


ainsi que les tests associés (dans un fichier `test_dice.py`):


~~~ python
def test_dice_creation_no_argument():
    dice = Dice()
    assert dice.get_position() == 1
    assert dice.probabilities == [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]


def test_dice_creation_initial_position():
    dice = Dice(position=5)
    assert dice.get_position() == 5
    assert dice.probabilities == [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]


def test_set_position():
    dice = Dice()
    assert dice.get_position() == 1
    dice.set_position(3)
    assert dice.get_position() == 3


def test_roll_no_proba():
    dice = Dice()
    dice.roll()
    assert 1 <= dice.get_position() <= dice.NUMBER_FACES


def test_roll_proba():
    dice = Dice(probabilities=[1, 0, 0, 0, 0, 0])
    dice.roll()
    assert dice.get_position() == 1
~~~


Créez un environnement de tests et vérifiez que les tests passent.

### Un dé qui compte


Nous voulons créer une version particulière d'un dé : un dé permettant de conserver les statistiques de ses lancers. Vous ferez des tests unitaires pour chaque fonctionnalité de ce nouvel objet.

Implémentez la classe `StatDice` qui hérite de `Dice`, retient le nombre de fois que chaque valeur possible a été obtenue et permet de calculer les statistiques associées. Vous devez donc écrire :

 - la méthode `__init__` sans oublier d'appeler le constructeur de la classe mère,
 - une nouvelle méthode `set_position` qui utilise la méthode `set_position` du dé classique et met à jour les décomptes de lancers du dé et un test unitaire pour vérifier que les comptes sont mis à jour,
 - une méthode `stats` qui renvoie les fréquences d'apparition de chaque valeur et un test unitaire qui vérifie que le calcul est bien fait,
 - une méthode `mean` qui renvoie la moyenne des lancers du dé et un test unitaire.

On pourra stocker le nombre d'apparition de chaque face dans une liste où l'index + 1 correspond à la face.

Prenez le temps de tester votre code (vous pourrez entre autres faire beaucoup de lancers d'un dé et vérifier qu'il suit la loi de probabilité que vous lui avez donnée) et de bien comprendre quelle méthode est appelée et pourquoi quand vous utilisez un `StatDice`.

