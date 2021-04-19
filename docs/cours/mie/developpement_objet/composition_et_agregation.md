---
layout: page
title:  "Composition et agrégation"
category: cours
tags: mie
author: "François Brucker"
---

## But

Le but de cette séance est de consolider les concepts fondamentaux de classe et d'objet et d'ajouter les notions de
composition, d'agrégation et d'attributs de classe. Vous (re)découvrirez aussi les tests unitaires.

> **Elements de corrigé :** Ils sont disponibles [là]({% link cours/mie/developpement_objet/composition_et_agregation_corrige.md %}). Cependant, ils ne dispensent pas d'aller en cours, c'est une aide à la compréhension.


## Séance tableau
 
Le [sujet au format pdf]({{ "ressources/TD_2_impression.pdf" }}).

## Séance code

### Dice et tests unitaires

On vous propose l'implémentation minimale suivante de la classe `Dice` que vous avez du réaliser la dernière fois.

#### dice.py

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
    self.position = numpy.random.choice([i for i in range(1, self.NUMBER_FACES + 1)], p=self.probabilities)
~~~

#### main.py

Ecrivez un petit programme qui crée 5 dés, les lance 10 fois et affiche à l'écran la moyenne de la somme des 5 dés.


#### test_dice.py

Pour être sur que l'on puisse utiliser nos dés, on ajoute des tests permettant de vérifier le bon fonctionnement de nos classes. 

Tout ce que vous allez implémenter dans tous les TP à partir de celui-ci doit être vérifié par des tests unitaires. 


Configurez l'environnement de tests pour faire passer les tests unitaires. Prenez le temps de
regarder la structure des tests. Si tous ces tests passent êtes vous assurés que l'implémentation est correcte ? 


~~~ python
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
    assert 1 <= dice.get_position() <= dice.NUMBER_FACES
~~~

On n'a pas testé : 

  - la création avec un argument. Ajoutez un test qui vérifie que l'argument est bien la position du dé.
  - les probabilités. Ajoutez un test qui vérifie que si une probabilité est à 1 et les autres à 0, on trouve bien la bonne valeur après un roll.

### GreenCarpet

Implémentez la classe `GreenCarpet` vue en TD.

On va utiliser les tests pour la créer **au fur et à mesure**. L'idée est de rajouter un test d'une petite fonctionnalité que l'on n'a pas encore puis de rajouter le code correspondant. Cette méthode est appelée *Test Driven Development*. Elle se décompose en plusieurs étapes :
 
 - écrire un test qui teste une fonctionnalité qu'on veut implémenter,
 - vérifier qu'il échoue (car le code qu'il teste n'existe pas), afin de vérifier que le test est valide,
 - écrire juste le code correspondant au test,
 - vérifier que le test passe,
 - recommencer avec une autre fonctionnalité.


On pourra ainsi. Dans l'ordre : 

  - commencer par vérifier que l'on peut créer un objet de la classe GreenCarpet
  - qu'un objet de la classe `GreenCarpet` a un attribut nommé `dice` qui contient 5 dés.
  - que la classe `GreenCarpet` contient une méthode roll() qui lance tous les dés.
  - que la classe `GreenCarpet` contient une méthode somme() qui rend la somme de la valeur des 5 dés.

Une fois ceci fait, créez un fichier *main.py* qui modifie le programme de la question précédente en utilisant la classe `GreenCarpet`.

### Pour aller plus loin

Ajoutez une méthode permettant de relancer les dés tant qu'on n'obtient pas une paire, un brelan, etc.
