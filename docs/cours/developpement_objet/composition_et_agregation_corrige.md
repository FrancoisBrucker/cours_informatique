---
layout: page
title:  "Composition et agrégation corrigé"
category: cours
tags: mie
author: "François Brucker"
---


## But

Eléments de corrigé de la séance  [composition et agrégation]({% link cours/developpement_objet/composition_et_agregation.md %}).


## Elements de cours

Composition et agrégation permettent de lier des classes ensembles, et plus principalement lorsqu'une classe admet comme attribut des objets de l'autre classe. 

On considère deux cas d'usage : 
 
 - *agrégation* : quand les objets utilisés sont créés en dehors de la classe,
 - *composition* : quand les objets utilisés sont créés dans le constructeur de la classe qui les utilise.

Il est important de comprendre que si des objets n'ont pas été crée dans la classe qui l'utilise, ils peuvent être connus par d'autres méthode du programme et donc être modifiées par ceux-ci.
Il se passe la même chose lorsqu'une méthode retourne un objet qui est un attribut. Une fois qu'un objet a été *donné* au monde extérieur on ne contrôle plus son état et il peut être utilisé a priori par n'importe quoi d'autre dans le programme.

Le diagramme uml de l'agrégation est : 

![uml composition et agregation]({{ "img/uml_composition_agregation.png" }})

Pour que tout se passe comme prévu, il faut donc s'assurer que soit :

  1. on s'en fiche qu'ils changent
  2. on refait un nouvel objet à nous pour s'assurer qu'il ne changera pas
  3. on se rappelle de ce qu'on peut faire avec les objets à tout instant
  4. les objets que l'on retourne et qui sont des attributs sont non modifiables (des entiers, réels, chaînes de caractères, tuples, etc)

C'est la solution 1 que nous appliquons dans ce td. Les objets `dice` du `GreenCarpet` peuvent bouger (n'importe qui peut les lancer) sans que ça ne gène le fonctionnement de l'objet de classe `GreenCarpet`.

Refaire des nouveaux à chaque fois peut s'avérer coûteux s'ils ne sont pas modifiés souvent et il est illusoire de se rappeller tout le temps ce qu'on a le droit (ou pas) de faire avec des objets (encore plus quand le projet contient plusieurs personne ou que sa durée de développement/maintient est longue, c'est à dire plus de 2h...) 

La solution 4. est une solution très efficace lorsque les objets sont plus souvent lu que modifié. On ne créer que des objets qui ne peuvent pas être modifié : on appelle ça des 
[value object](https://en.wikipedia.org/wiki/Value_object). Ces objets possèdent des valeurs et des méthodes pour y accéder mais que l'on ne peut pas modifier. La seule façon de changer de valeur c'est de recréer de nouveaux objets. Pour que l'utilisation de ce genre d'objets soit fluide, on fait en sorte qu'ils puissent supporter l'opération `==`. 

Vous avez utilisé des value objects bien souvent en python comme : les  entiers, les réels ou encore les chaines de caractères. Enfin de nombreux objets modifiables en python ont leur contrepartie non modifiable comme les tuples qui sont des listes non modifiables ou encore les `frozenset`sont des ensembles non modifiables.

Une bonne façon de programmer est de n'utiliser par défaut que des objets non modifiables et que si le besoin s'en fait sentir de les rendre modifiables.

## séance tableau



## séance de code

### ressources 

[Les sources tex du sujet]({{ "ressources/TD_2.tex" }})

### 1.1

![un dé]({{ "img/dice_proba_no_class_att.png" }})

~~~ python
from dice import Dice

d1 = Dice()
d2 = Dice(3)
d3 = Dice(2)

for essai in range(10):
    for d in (d1, d2, d3):
        d.roll()
    
    print(d1.get_position(), d2.get_position(), d3.get_position())
~~~

### 1.2

#### uml 

![greencarpet]({{ "img/greenCarpet.png" }})

Les objets de la classe `GreenCarpet` créent à l'initalisation 5 dé de la classe `Dice` qu'ils mettront dans la liste `_dices_`. C'est une **composition**.

#### code 
Le code est dans la correction de la session de code ci-dessous.

#### roll ?

Il est possible d'avoir plusieurs méthodes roll car elles ne seront jamais appliquées au même objet (à gauche du `.`)

Lorsque l'on exécute la méthode roll d'un objet de type `GreenCarpet`, on exécutera la ligne `self.dices[i].roll()` (ou un truc du genre). Donc la méthode `roll` sera cherché dans l'objet à gauche du `.` donc `self.dices[i]`. De là, on cherchera l'objet de numéro `i` de `self.dices` donc de la liste de nom `dices` appartenant à l'objet de nom `self` qui est un objet de la classe `GreenCarpet` : cet objet est un objet de la classe `Dice` qui possède une méthode `roll` (cette méthode n'a rien à voir avec la méthode `roll` des `GreenCarpet`). 


#### Les espaces de noms

On suppose qu'on a le code suivant pour la classe `GreenCarpet` :

~~~ python
class GreenCarpet:
    # ...
    def roll(self):
        for dice in self.dices:
            dice.roll()
    # ...
~~~

Et dans la classe `Dice` :

~~~ python
import random

# ...

class Dice:
    # ...
    def roll(self):
        self.set_position(randam.randint(1, 6))
    # ...
~~~

On suppose que l'on veuille exécuter le fichier *main.py* qui contient les lignes :

~~~ python
from GreenCarpet import GreenCarpet

# ...

tapis_vert = GreenCarpet()

# ...

tapis_vert.roll()

~~~

Les différents objets et espaces de noms (les flèches avec un petit carré) sont rassemblés dans la figure ci-après :

![espaces de noms]( {{ "ressources/td2_1_2_5.png" }} )

L'exécution de la commande `tapis_vert.roll()` se déroule alors comme suit (on a mis le début jusqu'à l'excution de la méthode `dice.roll`) :

  1. c'est une l'exécution du nom `roll` de l'espace de nom associé à l'objet de nom `tapis_vert` de l'espace de nom de *main.py*
  2. il existe un nom `tapis_vert` dans l'espace de nom de *main.py* associé à un objet de la classe `GreenCarpet`.
  3. on cherche donc le nom `roll` dans l'espace de nom de cet objet. Il n'y est pas
  4. lorsqu'un nom n'est pas dans l'espace de nom d'un objet, on cherche dans sa classe et *bingo* c'est un nom de méthode. On exécute alors cette méthode :
     
     1. on crée un espace de nom pour cette méthode
     2. on place les paramètre de la méthode dans cet espace de nom. Ici il n'y a qu'un paramètre de nom `self` associé à l'objet appelant (c'est à dire l'objet de la classe `GreenCarpet`) 
     3. la méthode consiste en une boucle for, qui itère sur l'objet associé au nom `self.dices` dans l'espace de nom de la méthode.
     4. comme `self` est l'objet de la classe `GreenCarpet`, il possède un nom `dices` dans son espace de nom qui est une liste de 5 objets de la classe `Dice`
     5. lors de l'itération le nom `dice` crée par la boucle for sera associé itérativement à chaque élément de la liste, c'est à dire à chaque objet de la classe `Dice`
     6. La boucle for exécute l'objet associé au nom  `dice.roll`. 
     7. le nom `roll` n'existe pas dans l'objet de nom `dice` dans l'espace de nom de la méthode. Mais il existe dans sa classe, la classe `Dice`.
     8. on exécute la méthode `roll` de la classe dice :
        
        1. on crée un espace de nom pour cette méthode et on y place le nom `self` correspondant à l'objet à gauche du point, ici l'objet associé au nom `dice` dans l'espace de nom de la méthode `roll` de la classe `GreenCarpet`
        2. l'exécution de cette méthode cherche un nom `random.randint`. Ce nom n'existe pas dans l'espace de nom de la méthode, du coup on remonte. Quand un objet n'existe pas dans l'espace de nom d'une méthode, on cherche dans l'espace de nom principal. Notez que c'est différent du fait de cherche un nom dans un objet, pour lequel on remonte à sa classe. Pour un espace de nom de méthode, on monte à l'esapce de nom du fichier. Ici on le trouve puisque c'est dans un import. Le nom correspont au nom `randint` dans l'espace de nom `random` qui existe dans l'espace de nom du fichier *dice.py* (ouf).
        3. l'exécution du nom `random.randint` rend un entier qui est associé au nom `position` dans l'espace de nom de l'objet associé à `self` dans l'espace de nom de la méthode roll de `Dice`, ici un des dés.
    9. la méthode `roll` de la classe `Dice` est finie, son espace de nom disparait.
  5. une fois la boucle for finie, la méthode `roll` de `GreenCarpet` est finie, son espace de nom disparait. 



### 2

#### 2.1

![card]({{ "img/card_v1.png" }})

On pourra coder :

  - la valeur par un nombre 11 = "Valet", 12 = "reine" et 13 = "roi" par exemple
  - la couleur par une chaîne de caractère

La carte est un value object. Une fois créée on ne peut la modifier. On a ajouté une méthode `__eq__` pour que 2 deux cartes de même couleur et valeur puissent être identique même si ce ne sont pas les mêmes objets.

#### 2.2

Voir le diagramme UML de la question 2.3.

On a affaire à une agrégation puisque la classe `Deck` ne crée aucune carte. 


#### 2.3



Pour les 2 premières questions, on a donné pas un nom/nombre (1, 2, 3, 4 ou "pique", "cœur", "carreau", "trèfle") aux couleurs. Ceci n'est pas satisfaisant car c'est un [magic number](https://codeburst.io/software-anti-patterns-magic-numbers-7bc484f40544).

L'idée est de mettre des noms de constantes explicites et d'utiliser ces noms plutôt que les chaînes de caractères. Pour se rappeler des différentes possibilités, on place des constantes dans la définition de la classe.


On va montrer ici les attributs de classes avec les différentes couleurs de cartes et l'agrégation avec les decks qui
sont des tas de cartes qui existent déjà indépendamment.

![carddeck]({{ "img/card_deck.png"}})


## séance de code


~~~ python
from dice import Dice

d1 = Dice()
d2 = Dice()
d3 = Dice()

NOMBRE_LANCER = 42
moyenne = 0
for essai in range(NOMBRE_LANCER):     
    for d in (d1, d2, d3):        
        d.roll()
        moyenne += d.get_position()
    
moyenne /= NOMBRE_LANCER
print("moyenne :", moyenne)
~~~


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

    def __str__(self):
        return "Dice(position=" + str(self.position) + ", probabilities=" + str(self.probabilities)

    def __eq__(self, other):
        return self.position == other.position and self.probabilities == other.probabilities

    def __lt__(self, other):
        return self.position < other.position

    def __gt__(self, other):
        return self.position > other.position


class GreenCarpet:
    def __init__(self):
        self.dices = [Dice() for i in range(5)]

    def get_dices(self):
        return self.dices

    def roll(self, index=None):
        if index:
            self.dices[index].roll()
        else:
            for dice in self.dices:
                dice.roll()

    def get_dice_by_id(self, item):
        return self.dices[item]

    def __getitem__(self, item):
        return self.dices[item]

    def appears_more_than(self, nb_times):
        count = [0] * 7
        for dice in self.dices:
            count[dice.get_position()] += 1
        for i in range(len(count)):
            if count[i] >= nb_times:
                return True
        return False

    def is_pair(self):
        return self.appears_more_than(2)

    def is_three_of_a_kind(self):
        return self.appears_more_than(3)

    def is_square(self):
        return self.appears_more_than(4)

    def roll_until_number(self, number):
        while not self.appears_more_than(number):
            self.roll()

    def roll_until_pair(self):
        self.roll_until_number(2)

    def roll_until_three_of_a_kind(self):
        self.roll_until_number(3)

    def roll_until_square(self):
        self.roll_until_number(4)
~~~

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

def test_dice_creation_initial_position():
    dice = Dice(position=5)
    assert dice.get_position() == 5

def test_roll_proba():
    dice = Dice(probabilities=[1, 0, 0, 0, 0, 0])
    dice.roll()
    assert dice.get_position() == 1
~~~

~~~ python
def test_green_carpet_creation():
    carpet = GreenCarpet()
    assert len(carpet.dices) == 5


def test_green_carpet_roll():
    carpet = GreenCarpet()
    carpet.roll()
    for dice in carpet.get_dices():
        assert 1 <= dice.position <= dice.NUMBER_FACES

def test_is_three_of_a_kind():
    carpet = GreenCarpet()
    assert carpet.is_three_of_a_kind()
    carpet.dices[0].set_position(4)
    assert carpet.is_three_of_a_kind()
    carpet.dices[1].set_position(4)
    carpet.dices[2].set_position(4)
    assert carpet.is_three_of_a_kind()
    carpet.dices[0].set_position(5)
    assert not carpet.is_three_of_a_kind()


def test_is_square():
    carpet = GreenCarpet()
    assert carpet.is_square()
    carpet.dices[0].set_position(4)
    assert carpet.is_square()
    carpet.dices[1].set_position(4)
    carpet.dices[2].set_position(4)
    carpet.dices[3].set_position(4)
    assert carpet.is_square()
    carpet.dices[0].set_position(5)
    assert not carpet.is_square()


def test_roll_until():
    carpet = GreenCarpet()
    carpet.roll_until_number(2)
    assert carpet.is_pair()
~~~

## ressources 

Le code pour https://www.planttext.com/ qui permet de créer de jolis diagrammes UML. Ce n'est pas franchement utile pour les étudiants à moins que vous vouliez voir comment on arrive à faire de telles merveilles graphiques en uml avec un petit service web. 


~~~
@startuml


  class Dice {
  -_position
  -_probabilities
  + __init__(position=1, probabilities=None)
  +get_position()
  +set_position(position)
  +get_probabilities()
  +set_probabilities(proba)
  +roll()
}

class GreenCarpet {
 - _dices
    
 + __init__()
 + roll()
 + sum()
}

Dice --* GreenCarpet

@enduml
~~~


~~~
@startuml
class Card { 
__attributes__
 - value
 - color
__methods__
 +__init__(value, color)
 + __eq__(self, other)
 + get_value()
 + get_color()
}
@enduml
~~~

~~~
class Card { 
__class_attributes__
 - SPADES
 - HEARTS
 - CLUBS
 - DIAMONDS
__attributes__
 - value
 - color
__methods__
 +__init__(value, color)
 + __eq__(self, other)
 + get_value()
 + get_color()

}

class Deck {
    __attributes__
    - cards
    __methods__
    +__init__()
    +add(card)
    +show()
    +remove()
    
}

Card --o Deck
~~~



