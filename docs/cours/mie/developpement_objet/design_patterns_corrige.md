---
layout: page
title:  "Design Patterns corrigé"
category: cours
tags: mie
---

## But

Eléments de corrigé de la séance  [design patterns]({% link cours/mie/developpement_objet/design_patterns.md %}).



## Éléments de cours

IL existe 3 grands types de design pattern, on pourra en donner un exemple pour chaque.

On peut prendre la liste initiale des design pattern du [GOF](https://en.wikipedia.org/wiki/Design_Patterns) mais je déconseille singleton qui tient plus de l'anti-pattern que du pattern...

Pour les trois types, on verra :  

  - **type creational** : *factory*. Créer les objets via des méthodes presque sans paramètre et avec un nom adapté plutôt qu'avec un contructeur avec des milliers de paramètres
  - **type structural** : *composite*. On essayera de le voir dans la prochaine séance.
  - **type behavioural** : *strategy*. Même fonction mais algorithmes différents (pour un tri par exemple)


Parler aussi des anti-pattern, c'est à dire des mauvaises façons de faire qui arrivent d'elles-mêmes si on ne fait pas attention. Voir par exemple : [là](http://sahandsaba.com/nine-anti-patterns-every-programmer-should-be-aware-of-with-examples.html)


## Fun fact 

 Le nom de *duck typing*  vient des Monty Python et plus particulièrement la séquence où [l'on brûle une sorcière](https://www.youtube.com/watch?v=gUXB_jLiT3A) dans Sacré Graal. Le [nom même du langage](https://en.wikipedia.org/wiki/Python_(programming_language)#History) vient d'eux et pas de l'[animal](https://www.youtube.com/watch?v=NoX-4Hm1rPU). Les informaticiens ont une passion presque maladive pour les Monthy Python. Par exemple le terme de spam vient aussi d'eux, ou plutôt d'un de [leur sketch](https://www.youtube.com/watch?v=cFrtpT1mKy8) de leur émission de la BBC qui s'appelait le Monthy Python's flying circus (un de mes sketch préféré étant l'[expédition au Kilimandjaro](https://www.youtube.com/watch?v=1T9Yp-2TYzo) mais on pourrait en citer des dizaines d'autres)),

Cela ne résout bien sûr pas des problèmes aussi compliqués que [tracer 7 lignes rouges perpendiculaires entre elles](https://www.youtube.com/watch?time_continue=2&v=BKorP55Aqvg)


## Première amélioration

Il est important que les propriétés d'un objet soient protégées. Ici, on fait rentrer une liste (`choices`) dans l'objet. Comme on ne veut pas qu'elle puisse être modifiée, il faut la recopier dans l'objet.

La méthode `roll` rend `self` ce qui permet de chainer les instructions et rend possible des choses du genre : 
`print(Choice([1, 2, 2, 3]).roll().get_position())`. C'est important de comprendre comment tout ça fonctionne : 

  1. on lit de droite à gauche
  2. on applique la méthode à l'objet à gauche du point.
  3. puis on remonte les appels pour voir si cela marche.

Pour l'instruction précédente : 

  - on affiche à l'écran (c'est la méthode `print`) l'objet `A` qui est le résultat de `Choice([1, 2, 2, 3]).roll().get_position()`
 - cet objet `A` est le résultat de la méthode `get_position()` appliquée à l'objet `B` qui est `Choice([1, 2, 2, 3]).roll()`
 - cet objet est `B` le résultat de `roll()` appliqué à l'objet `C` qui est le résultat de `Choice([1, 2, 2, 3])` 
 - l'objet `C` et un objet de classe `Choice`

On peut donc remonter : 

  - `C` est un objet de classe Choice
  - `B` est le résultat de `roll` appliqué à `C`, c'est donc `C`
  - `A` est un entier valant 1, 2, ou 3
  - on affiche `A`, c'est à dire 1, 2 ou 3


#### choice.py


~~~ python
import random


class Choice:
    def __init__(self, choices):
        self.choices = tuple(choices)
        self._position = self.choices[0]
    
    def get_position(self):
        return self._position

    def roll(self):
        self.position = self.choices[random.randint(0, len(self.choices) - 1)]
        return self
~~~

Dans le constructeur, on utilise `self.choices[0]` car on sait que cela va marcher : c'est un tuple. Si on avait écrit : `self._position = choices[0]` on essaie d'obtenir le 1er élément du paramètre choices qui peut être un itérable sans être une liste ou un tuple (un ensemble, un dictionnaire).

#### tests.py


~~~ python
import pytest

from choice import Choice


def test_init():
    d1 = Choice([1])
    assert d1.choices == (1, )


def test_initial_position():
    d1 = Choice([1, 2])
    assert d1.get_position() == 1


def test_roll():
    d1 = Choice([1])
    d1.roll()
    assert d1.get_position() == 1


def test_copy_choices():
    initial_list = ["a"]
    d1 = Choice(initial_list)
    initial_list[0] = "CHANGE"
    d1.roll()
    assert d1.get_position() == "a"


def test_no_modification():
    d1 = Choice([1])
    with pytest.raises(Exception):
        d1.choices[0] = 2
~~~

## factory

Ce [pattern](https://www.geeksforgeeks.org/design-patterns-set-2-factory-method/) est super pour créer des objets. En gros, plutôt que d'apprendre par cœur des paramètres d'initialisation, les objets courants sont créés par des méthodes.


On va procéder par étapes.

### des dés dans le main.

~~~ python
def a_dice():
    N = 1000
    d6 = Choice(list(range(1, 7)))

    results = []
    for number in range(N):
        results.append(d6.roll().get_position())

    count = Counter(results)
    print(count)
    for key, value in count.items():
        print(key, "proba: ", value / N, "; number: ", value)


def two_dice():
    N = 1000
    two_d6_choices = []
    
    for i range(1, 7):
        for j in range(1, 7):
            two_d6_choices.append(i + j)

    two_d6 = Choice(two_d6_choices)
    results = []
    for number in range(N):
        results.append(two_d6.roll().get_position())

    count = Counter(results)
    print(count)
    for key, value in count.items():
        print(key, "proba: ", value / N, "; number: ", value)
~~~

### On place le tout dans le fichier de la classe

#### choice.py

~~~ python
import random

class Choice:
    def __init__(self, choices):
        self.choices = tuple(choices)
        self.position = self.choices[0]

    def get_position(self):
        return self.position

    def roll(self):
        self.position = self.choices[random.randint(0, len(self.choices) - 1)]
        return self


def dice():
        return Choice(range(1, 7))    

def two_dices():
    return Choice([i + j for i in range(1, 7) for j in range(1, 7)])
~~~

#### tests.py

~~~ python
import pytest

from collections import Counter

from choice import Choice
import choice


def test_init():
    d1 = Choice([1])
    assert d1.choices == (1, )


def test_initial_position():
    d1 = Choice([1, 2])
    assert d1.get_position() == 1


def test_roll():
    d1 = Choice([1])
    d1.roll()
    assert d1.get_position() == 1


def test_sets():
    assert Choice({1}).roll().get_position() == 1


def test_copy_choices():
    initial_list = ["a"]
    d1 = Choice(initial_list)
    initial_list[0] = "CHANGE"
    d1.roll()
    assert d1.get_position() == "a"


def test_no_modification():
    d1 = Choice([1])
    with pytest.raises(Exception):
        d1.choices[0] = 2


def test_factory_dice():
    d = choice.dice()
    assert d.choices == (1, 2, 3, 4, 5, 6)


def test_factory_two_dice():
    d = choice.two_dices()
    assert Counter(d.choices) == {2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1}
~~~


## Memento


Pour créer un [Memento](https://www.geeksforgeeks.org/memento-design-pattern/), la façon la plus simple est d'utiliser des conventions. On dira que le Memento fonctionne pour tout objet ayant deux méthodes : 
  - `get_position`
  - `set_position`

Ce qui donne : 

~~~ python
class Memento:
    def __init__(self, object_to_save):
        self._stored_state = object_to_save.get_position()
        self._object_to_restore = object_to_save
    
    def restore(self):
        self._object_to_restore.set_position(self._stored_state)
~~~


#### choice.py

~~~ python
import random

class Choice:
    def __init__(self, choices):
        self.choices = tuple(choices)
        self.position = self.choices[0]

    def get_position(self):
        return self.position
        
    def set_position(self, new):
        self.position = new
        

    def roll(self):
        self.set_position(self.choices[random.randint(0, len(self.choices) - 1)])
        return self


def dice():
        return Choice(range(1, 7))    

def two_dices():
    return Choice([i + j for i in range(1, 7) for j in range(1, 7)])
~~~

#### memento.py

On stocke un état et un objet pour pouvoir le restaurer plus tard : 

  - l'objet et son état sont stockés à l'initialisation
  - une méthode `restore()` permet de remettre l'objet à l'état qu'il avait à l'initialisation du Memento.

#### test_memento.py

~~~ python
import choice
from memento import Memento


def test_memento():
    dice = choice.dice()
    dice.set_position(2)

    memento = Memento(dice)
    dice.set_position(6)

    memento.restore()
    assert dice.get_position() == 2
~~~

## Undo

#### undo.py

~~~ python
from memento import Memento

class Undo:
    def __init__(self, ):
        self._actions = []

    def nb_undos(self):
        return len(self._actions)
        
    def save(self, dice):
        self._actions.append(Memento(dice))
    
    def restore(self):
        if self._actions:
            x = self._actions.pop()
            x.restore()
~~~


#### test_undo.py

~~~ python
import choice
from undo import Undo

def test_init():
    dice = choice.dice()
    dice.set_position(1)
    undo = Undo()
    assert undo.nb_undos() == 0
    

def test_save_restore_once():
    dice = choice.dice()
    undo = Undo()

    dice.set_position(1)
    undo.save(dice)
    dice.set_position(5)
    
    
    assert undo.nb_undos() == 1
    
    undo.restore()
    assert dice.get_position() == 1

def test_save_restore_several():
    dice = choice.dice()
    undo = Undo()

    dice.set_position(1)
    
    undo.save(dice)
    dice.set_position(5)

    undo.save(dice)
    dice.set_position(6)
    
    
    assert undo.nb_undos() == 2
    
    undo.restore()
    assert dice.get_position() == 5
    assert undo.nb_undos() == 1
    
    undo.restore()
    assert dice.get_position() == 1
    assert undo.nb_undos() == 0
~~~

#### main.py

~~~ python
import choice
from undo import Undo

dice = choice.dice()

undo = Undo()

for i in range(10):
    undo.save(dice)
    dice.roll()
    print(dice.get_position())
    
print("--------")

for i in range(10):
    undo.restore()
    print(dice.get_position())
~~~

Qui pourra rendre le code suivant : 

~~~
    1
    2
    4
    3
    2
    5
    3
    2
    4
    4
    --------
    4
    4
    2
    3
    5
    2
    3
    4
    2
    1
~~~


### Un undo dans dice


#### choiceUndo.py

On a bien fait de modifier la méthode `roll` de `Choice` pour qu'elle utilise `set_position`, ceci nous permet de ne modifier que `set_position` pour la classe `ChoiceUndo`.


~~~ python
from choice import Choice

class ChoiceUndo(Choice):
    def __init__(self, choices, undo):
        super().__init__(choices)
        self.undo = undo

    def set_position(self, new):
        self.undo.save(self)
        super().set_position(new)
~~~
