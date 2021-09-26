---
layout: page
title:  "Composition et agrégation"
category: cours
tags: mie
author: "François Brucker"
---

Le but de cette séance est de consolider les concepts fondamentaux de classe et d'objet et d'ajouter les notions de
composition, d'agrégation et d'attributs de classe. Vous (re)découvrirez aussi les tests unitaires.

## composition et agréagation

Composition et agrégation permettent de lier des classes ensembles, et plus principalement lorsqu'une classe admet comme attribut des objets de l'autre classe.

Ce qui les distingue :

* **agrégation** : quand les objets utilisés sont créés en dehors de la classe,
* **composition** : quand les objets utilisés sont créés dans le constructeur de la classe qui les utilise.

Il est important de comprendre que si des objets n'ont pas été crées dans la classe qui l'utilise, ils peuvent être connus par d'autres méthodes du programme et donc être modifiées par celles-ci.

Les exemple de composition et d'agrégation de *la vraie vie* sont souvent un peu bizarre. Mais par exemple :

* Un livre est composé de pages : pour créer le livre on a créé les pages : c'est une **composition**
* Les télécommandes ont besoin de piles pour fonctionner, mais on peut les remplacer : c'est une **agrégation**.

> Si une classe est composée d'autres objets, ces parties peuvent être modifiées en dehors de la classe, même pour une compositio. 
{: .attention}

Il se passe la même chose lorsqu'une méthode retourne un objet qui est un attribut. Une fois qu'un objet a été *donné* au monde extérieur on ne contrôle plus son état et il peut être utilisé a priori par n'importe quoi d'autre dans le programme.

Pour illustrer l'avertissemnt 

Pour que tout se passe comme prévu, il faut donc s'assurer que soit :

  1. on s'en fiche qu'ils changent
  2. on refait un nouvel objet à nous pour s'assurer qu'il ne changera pas
  3. on se rappelle de ce qu'on peut faire avec les objets à tout instant
  4. les objets que l'on retourne et qui sont des attributs sont non modifiables (des entiers, réels, chaînes de caractères, tuples, etc)

### schémas uml

Le diagramme uml de l'agrégation est : 

![uml composition et agregation]({{ "img/uml_composition_agregation.png" }})


C'est la solution 1 que nous appliquons dans ce td. Les objets `dice` du `GreenCarpet` peuvent bouger (n'importe qui peut les lancer) sans que ça ne gène le fonctionnement de l'objet de classe `GreenCarpet`.

Refaire des nouveaux à chaque fois peut s'avérer coûteux s'ils ne sont pas modifiés souvent et il est illusoire de se rappeller tout le temps ce qu'on a le droit (ou pas) de faire avec des objets (encore plus quand le projet contient plusieurs personne ou que sa durée de développement/maintient est longue, c'est à dire plus de 2h...) 

La solution 4. est une solution très efficace lorsque les objets sont plus souvent lu que modifié. On ne créer que des objets qui ne peuvent pas être modifié : on appelle ça des 
[value object](https://en.wikipedia.org/wiki/Value_object). Ces objets possèdent des valeurs et des méthodes pour y accéder mais que l'on ne peut pas modifier. La seule façon de changer de valeur c'est de recréer de nouveaux objets. Pour que l'utilisation de ce genre d'objets soit fluide, on fait en sorte qu'ils puissent supporter l'opération `==`. 

Vous avez utilisé des value objects bien souvent en python comme : les  entiers, les réels ou encore les chaines de caractères. Enfin de nombreux objets modifiables en python ont leur contrepartie non modifiable comme les tuples qui sont des listes non modifiables ou encore les `frozenset`sont des ensembles non modifiables.

Une bonne façon de programmer est de n'utiliser par défaut que des objets non modifiables et que si le besoin s'en fait sentir de les rendre modifiables.


## exemple : des cartes

### modèle simple

pb du roi valet ? pour ordre

### composition

compose valeur à chaque carte

### les courleurs

en mettant des constantes

## le jeu de carte

deck : agregation

### probleme

### creation

## bilan

value object pour les cartes : on ne doit pas pouvoir les modiifer.

## utilisation des tests

on teste chaque methode et des faon de construire les objets.



 
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
