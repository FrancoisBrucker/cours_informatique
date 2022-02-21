---
layout: page
title:  "TDD et test pattern"
author: "François Brucker"
---

### RAZ de la todo list

On est arrivé à un point clé de notre projet. La classe `Money` permet de gérer plusieurs devises et de multiplier les montant par un entier.

A partir de maintenant, on va vous laisser un peu plus libre.

On va épurer la todo list en supprimant les améliorations possibles de `==` et la gestion des arrondis (que l'on vous laisse en exercice :-)) : 

#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5


### Addition 1/3

Avant de traiter l'addition de deux monnaies différentes, commençons par traiter le cas de 1 unique monnaie : 

#### tbd

 - $5 + 2.5CHF = $10 si le taux de change est 1:.5
 - **$5 + $5 = $10**


Commençons par écrire un test permettant de tester que $5 + $5 = $10 en supposant que :

  - on utilise la méthode `plus` de `Money` qui rend un objet `Money`
  - les objets de la classe `Money` sont toujours non mutables

Ce test réalisé, on l'oplémente (une obvious implémentation devrait suffire)


#### tests.py

On a ajouté le test ci-après à la batterie de test précédent


~~~ pyhton
def test_sum():
    sum = money.dollar(5).plus(money.dollar(5))

    assert money.dollar(10) == sum
~~~


#### money.py

~~~ python
def dollar(amount):
    return Money(amount, "USD")


def franc(amount):
    return Money(amount, "CHF")


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def currencies(self):
        return self.currency

    def __eq__(self, other):
        return self.currency == other.currency and self.amount == other.amount

    def __mul__(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def plus(self, other):
        return Money(self.amount + other.amount, self.currency)
~~~

#### addition

Tout comme `__mul__` il existe une méthode en python pour gérer l'addition : `__add__`. On modifie nos tests et le code pour l'utiliser.


#### tests.py

On a ajouté le test ci-après à la batterie de test précédent

~~~ python
def test_sum():
    sum = money.dollar(5) + money.dollar(5)

    assert money.dollar(10) == sum
~~~

#### money.py

~~~ python
class Money:
    
    # ...

    def __add__(self, other):
        return Money(self.amount + other.amount, self.currency)
~~~

### Addition 2/3

Notre implémentation de `+` qui rend un objet de type `Money` ne sera pas tenable longtemps. En effet `$5 + 2.5CHF` ne peut être un objet de type `Money`. Ce sont deux devises différentes qui vont avoir une valeur dépendant du cours actuel, qui va fluctuer sans cesse. Il faut donc résoudre deux problèmes :

  - comment stocker plusieurs devises
  - comment convertir une monnaie ou un ensemble de monnaies en une autre. 

#### tests. py


Pour imaginer cela rien de mieux qu'un test ! On va l'écrire à l'envers, en partant du résultat, car  on sait où on veut arriver : à $10 : 

~~~ python
def test_simple_addition():
    # ...
    assert money.dollar(10) == reduced
~~~

Ces $10 viennent d'une conversion en dollar d'une somme de deux monnaies, conversion qui -- d'un point de vue métier -- ne peut venir que d'une banque

~~~ python
def test_simple_addition():
    # ...
    reduced = bank.reduce(sum, "USD")
    assert money.dollar(10) == reduced
~~~

Banque qu'il faut créer : 

~~~ python
def test_simple_addition():
    # ...
    bank = Bank()
    reduced = bank.reduce(sum, "USD")
    assert money.dollar(10) == reduced
~~~

Il ne reste plus qu'à fabriquer notre expression pur avoir notre test final : 

~~~ python
def test_simple_addition():
    five = money.dollar(5)
    sum = five + five
    bank = Bank()
    reduced = bank.reduce(sum, "USD")
    assert money.dollar(10) == reduced
~~~

#### money.py

On fake le tout pour avoir un test qui passe et du pain sur la planche pour plus tard.

~~~ python
class Bank:
    def reduce(self, expression, currency):
        return dollar(10)
~~~

### Addition 3/3

L'implémentation réelle de tout ce qu'on a *faké* n'est pas si évidente que ça. On va donc devoir faire des choix restrictifs et ajouter à la todo list les généralisations à effectuer pour terminer le travail.

On va considérer que toute somme de deux monnaies est une nouvelle classe somme (on va cependant ajouter que la somme de 2 monnaies identiques devrait rendre une monnaie dans la todo list). 

Donc : 

  - on ajoute que la somme de deux monnaies $ devrait donner des $ dans la todo list 
  - on supprime du coup le test `test_sum` qui vérifie que $5 + $5 = $10 ce qui n'est plus vrai.
  - on ajoute un test pour montrer que la somme de deux monnaies est un objet contenant une partie gauche (la partie à gauche du `+`) et une partie droite (la partie à droite du `+`).


Une fois ceci fait, on implémente le tout en *obvious implementation*.

#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - **$5 + $5 = quelque chose qui correspond à $10**
  - $5 + $5 devrait rendre une Money


#### tests. py

~~~ python
def test_plus_returns_sum():
    five = money.dollar(5)
    three = money.dollar(3)
    sum = five + three
    assert sum.left == five
    assert sum.right == three
~~~

#### money.py

~~~ python
class Money:
    # ... 
    def __add__(self, other):
        return Sum(self, other)

class Sum:
    def __init__(self, left, right):
        self.left = left
        self.right = right
~~~


####  reduce 1/3

Il faut faire en sorte de trianguler pour l'implémentation de la méthode `reduce` de la banque (pour l'instant c'est un *fake* qui rend 10 dollar). Maintenant elle prend en paramètre une somme. On va donc faire un test qui vérifiera que `bank.reduce(money.dollar(3) + money.dollar(4), "USD")` rende bien 7 dollars. 

En implémentant la méthode (après avoir écrit le test bien sur), on considérera que la partie gauche et droite de la somme sont de la monnaie du deuxième paramètre pour l'instant.

En faisant cette implémentation, on va rajouter un todo pour noter que l'on doit aussi implémenter `Bank.reduce` pour un objet de type Money (et pas juste pour les sommes)

#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - **$5 + $5 = quelque chose qui correspond à $10**
  - $5 + $5 devrait rendre une `Money`
  - `Bank.reduce(Money)`

#### tests. py

~~~ python
def test_bank_reduce_sum():
    bank = Bank()
    assert money.dollar(7) == bank.reduce(money.dollar(4) + money.dollar(3), "USD")
~~~
#### money.py

~~~ python
class Bank:
    def reduce(self, expression, currency):
        return Money(expression.left.amount + expression.right.amount, currency)
~~~

#### reduce 2/3

Implémenter juste la méthode `reduce` pour la banque pose quelques problèmes. En particulier : la banque doit connaître l'implémentation de Money pour avoir accès à l'attribut amount.

Pour cela on va déplacer le corps de la méthode `reduce` de la `Bank` à `Sum`. Banque ne fera qu'appeler la méthode de `Sum`. Pour l'instant on ne va considérer qu'un seul paramètre pour la méthode `reduce` de `Sum`, la devise d'arrivée (on rajoutera la banque comme paramètre plus tard, lorsque l'on utilisera effectivement des conversions. On place tout de même cette fonctionnalité dans la todo list pour ne pas l'oublier).


#### money.py

~~~ python
class Bank:
    def reduce(self, expression, currency):
        return expression.reduce(currency)


class Sum:
    # ... 
    def reduce(self, currency):
        return Money(self.left.amount + self.right.amount, currency)
~~~

#### reduce 3/3 

L'étape précédente a permis de baisser le niveau de connaissance de la banque des objets qui l'entourent. C'est une bonne chose. Un bon programme utilise plein d'objets qui interagissent entre eux mais qui ne connaissent pas l'implémentation des autres classes. Les objets doivent être le plus découplé possible.

Monter le reduce au niveau de `Sum` nous permet également de traiter le cas où Bank.reduce à une Money comme paramètre. Il suffit de rajouter  une méthode `reduce` à Money ! 

Pour faire cela, on commence par faire un test où l'argument de reduce pour la banque est un objet de type `Money` puis on écrit le code correspondant. De même que précédemment, on va considérer que le seul paramètre de la méthode `reduce` pour `Money` est la devise d'arrivée et on ajoute dans la todo list qu'il faudra implémenter une conversion si nécessaire.


#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 + $5 = quelque chose qui correspond à $10~~
  - $5 + $5 devrait rendre une Money
  - ~~Bank.reduce(Money)~~
  - Sum.reduce avec conversion
  - Money.reduce avec conversion


#### tests. py

~~~ python
def test_reduce_money():
    bank = Bank()
    assert money.dollar(1) == bank.reduce(money.dollar(1), "USD")
~~~

#### money.py

~~~ python
class Money:
    # ...
    def reduce(self, currency):
        return self
~~~
 
### Taux de change 1/2

On va maintenant s'attaquer à la conversion. Commençons simple avec les objets de type `Money`


#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 + $5 = quelque chose qui correspond à $10~~
  - $5 + $5 devrait rendre une Money
  - ~~Bank.reduce(Money)~~
  - Sum.reduce avec conversion
  - **Money.reduce avec conversion**


On va écrire un test permettant de gérer le change :

  - on veut convertir $2 en CHF
  - le taux de change que l'on ajoute à la banque lors du test. par exemple 1CHF -> $2 (on y est presque en réalité)

Il faut donc ajouter une méthode `add_rate` à la banque dont les paramètres pourraient être la monnaie d'origine, la monnaie d'arrivée et le taux de change. 

Une fois le test créé, on implémente le tout. En commençant par un fake, puis petit à petit on ajoute la bonne implémentation. Cela peut être long car il vous faudra déterminer comment fonctionne le taux de change. 


#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 + $5 = quelque chose qui correspond à $10~~
  - $5 + $5 devrait rendre une Money
  - ~~Bank.reduce(Money)~~
  - Sum.reduce avec conversion
  - ~~Money.reduce avec conversion~~

#### tests. py

~~~ python
def test_reduce_money_conversion():
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    assert money.dollar(2) == bank.reduce(money.franc(1), "USD")


def test_identity_rate():
    bank = Bank()
    assert 1 == bank.rate("USD", "USD")
~~~

#### money.py

~~~ python
class Bank:
    def __init__(self):
        self._rate = dict()

    def reduce(self, expression, currency):
        return expression.reduce(self, currency)

    def add_rate(self, from_currency, to_currency, rate):
        self._rate[(from_currency, to_currency)] = rate
        self._rate[(to_currency, from_currency)] = 1 / rate

    def rate(self, from_currency, to_currency):
        if from_currency == to_currency:
            return 1
        return self._rate[(from_currency, to_currency)]

class Money:
    # ... 
    def reduce(self, bank, currency):
        return Money(self.amount * bank.rate(self.currency, currency), currency)
    
class Sum:
    # ... 
    def reduce(self, bank, currency):
        return Money(self.left.amount + self.right.amount, currency)    
~~~
 
### Taux de change 2/2

Pour l'instant notre conversion pour les sommes ne considère que les mêmes devises. On va travailler maintenant sur des devises différentes.



On va écrire un test pour convertir une somme de 2 devises différentes. Puis implémentez le tout.


#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 + $5 = quelque chose qui correspond à $10~~
  - $5 + $5 devrait rendre une Money
  - ~~Bank.reduce(Money)~~
  - ~~Sum.reduce avec conversion~~
  - ~~Money.reduce avec conversion~~

#### tests. py

~~~ python
def test_sum_reduce_different_currency():
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)

    assert money.franc(2) == bank.reduce(money.dollar(2) + money.franc(1), "CHF")
~~~

#### money.py

~~~ python
class Sum:
    # ... 
    def reduce(self, bank, currency):
        left_money = bank.reduce(self.left, currency)
        right_money = bank.reduce(self.right, currency)
        return Money(left_money.amount + right_money.amount, currency)
~~~

### Expressions

Pour finir, il nous reste à généraliser le tout. C'est à dire que l'on aimerait bien pouvoir multiplier une `Sum` par un entier par exemple ou additionner des `Sum entre elles`. 


A priori, une partie de la somme de sommes est déjà implémentée. 
Par exemple le test suivant doit passer : 

~~~ python
def test_sum_of_sum_1():
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    expression = money.dollar(1) + (money.franc(2) + money.dollar(1))
    assert money.franc(3) == bank.reduce(expression, "CHF")
~~~

Mais pas celui là : 

~~~ python
def test_sum_of_sum_2():
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    expression = (money.dollar(1) + money.franc(2)) + money.dollar(1)
    assert money.franc(3) == bank.reduce(expression, "CHF")
~~~

Pourquoi ? 

(réfléchissez un peu)

Implémentons la solution.

#### money.py

~~~ python
class Sum:
    # ... 
    def __add__(self, other):
        return Sum(self, other)
~~~

#### tests.py

Il ne reste plus qu'à tester la multiplication

~~~ python
def test_sum_of_sum():
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    expression = (money.franc(2) + money.dollar(1)) * 4
    assert money.franc(10) == bank.reduce(expression, "CHF")
~~~


#### money.py

~~~ python
class Sum:
    # ...
    
    def __mul__(self, multiplier):
        return Sum(self.left * multiplier, self.right * multiplier)
~~~
