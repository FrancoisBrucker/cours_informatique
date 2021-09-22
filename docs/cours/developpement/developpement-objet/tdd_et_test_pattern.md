---
layout: page
title:  "TDD et test pattern"
category: cours
tags: MIE python tdd
author: "François Brucker"
---

## Test Driven Development by example


Vous allez suivre ici le livre séminal : [TDD by example](https://www.amazon.fr/Test-Driven-Development-Kent-Beck/dp/0321146530/ref=sr_1_1?ie=UTF8&qid=1538720480&sr=8-1&keywords=test+driven+development+by+example) de Kent Beck (Suivez son [twitter](https://twitter.com/kentbeck), ses posts sont souvent rigolos et toujours utiles). Initialement écrit pour le java, nous allons appliquer ses enseignements au python.

On y verra aussi quelques règles de refactoring que l'on peut voir dans [Refactoring: Improving the Design of Existing Code ](https://www.amazon.fr/Refactoring-Improving-Design-Existing-Code/dp/0201485672/ref=sr_1_2?ie=UTF8&qid=1539066441&sr=8-2) de [Martin fowler](https://martinfowler.com) (allez voir son site, y'a moult choses chouettes sur le code, l'agile, la vie et le reste)

Si vous connaissez tout ça par cœur, mais pas avant car ce n'est pas un livre pour débutant, allez lire [clean code](https://www.amazon.fr/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882) de Robert Martin (dit uncle bob). Ce livre contient, entre autres, le meilleur indicateur d'un bon code au monde, le WTFs/minute :

![WTFs/minute]({{ "img/wtfm.jpg"}})

## Quoi

Créer une application de change. 


|who     |number| price  | total       |
|--------|------|--------|-------------|
| Apple  | 1000 | $200   | $200 000    |
| Nestlé | 400  | 80 CHF |  32 000 CHF |
|||           **total**  | $248 000    |
                                

Avec le taux de conversion : 1 CHF = $0.5


## Comment ?

En programmant par les tests bien sur !

On commence par une todo list qui regroupe tout ce que l'on pense faire pour l'instant. Cette liste va diminuer lorsque l'on avancera sur le projet et grossir lorsque notre connaissance du projet va s'affiner.

Nous n'utiliserons pas ici notre code. Mais il faudra tout faire *from scratch*. On aura donc besoin : 

  - d'une todo list où tous nos items à faire pour l'instant sont écrit : le *backlog* 
  - de fichiers de tests
  - du code 

On verra tout au long du cours divers patterns de test et de développement pour que tout aille pour le mieux. Notre but est ici de faire : *clean code that works* Pour cela on va se fixer quelques règles : 

  - on écrit du code que si un test rate
  - élimine les duplications

Ces 2 règles impliquent un mode de fonctionnement : 

  1. red: 
    - écrire *rapidement* un *petit* test. 
    - lancer les test et le voir planter, voir même  ne correspondre à aucun code.
  2. green: 
    - écrire le code *minimal* qui permet de faire passer le test
    - lancer les tests et les voir tous réussir
  3. refactor: élimine les duplications tout en conservant le passage des tests.


Cela permet de prendre du plaisir à coder :

  - en écrivant du code on est sûr de ne rien casser
  - voir la todo list diminuer montre que l'on avance
  - comme tous les tests sont conservés on  sait que l'on ne travaille pas pour rien

Toutes ces règles visent à diminuer la peur qui bloque tout progrès.

## Code

On va développer petit à petit notre propre application de change en utilisant le TDD. Essayer de voir comment : 

  - chaque test couvre un petit ajout de fonctionnalités
  - rapidement et salement faire fonctionner les tests
  - souvent les tests sont lancés
  - le refactoring est fait par petites touches

### 1 - départ

#### ??

Commençons par remplir notre todo list : 

  - il faut plusieurs devises (ici CHF et $)
  - il faut multiplier les devises par des nombres (nb actions * prix)

La todolist (backlog) nous indique ce qu'il faut faire (dès que on voit une tâche à faire qui n'est pas dans la todo list, on la rajoute), ce sur quoi on travaille (on travaillera toujours sur un unique item) et ce que l'on a fait (il n'y a rien de plus satisfaisant que de barrer une ligne que l'on vient de finir).

Puis créez un projet avec pycharm. On y placera pour l'instant 1 unique fichier de tests, `tests.py`.
Prenez également une feuille de papier pour vos todos.

On ajoutera tout de suite une configuration permettant de lancer les tests avec py.test.

#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - $5 * 2 = $10

#### ??

Par quoi on commence ?

**PAR UN TEST !**

La bonne question est : que teste-t-on en premier ?

La deuxième ligne semble la plus simple. Donc allons-y : utilisons notre application pour multiplier les dollars.

#### tests.py

~~~ python
from money import Dollar

def test_multiplication():
    five = Dollar(5)
    five.times(2)
    
    assert 10 == five.amount
~~~


Utiliser dollar comme ça permet d'ajouter rapidement des fonctionnalités mais ajoute des choses à faire, que l'on ajoute dans la todo list :

#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - **$5 * 2 = $10**
  - utiliser `amount` ? Le rendre privé (le cacher à l'utilisateur (ici les tests))
  - five == 10 n'est pas vraiment super. non mutable
  - gestion des arrondis 

##### ??

Rien ne marche avec nos tests. On va donc lire attentivement les messages d'erreurs de python et les régler petit à petit.

Il est **TOUJOURS** plus simple de lire un message d'erreur que d'essayer de faire en sorte qu'ils n'arrivent pas en regardant le code.


  1. En lançant les tests on a : `E   ModuleNotFoundError: No module named 'money'` : on crée donc un fichier `money.py`
  2. L'erreur est maintenant : `E   ImportError: cannot import name 'Dollar' from 'money'` : on crée une classe `Dollar` et une unique instruction `pass` (qui ne fait rien mais permet de ne pas faire d'erreur lorsque l'on crée un bloc sans instructions)
  3. et ainsi de suite jusqu'à ce qu'il n'y ait plus d'erreur

L'interpréteur vous aide : utilisez le pour résoudre ce genre de problèmes !


Après plusieurs tentatives de plus en plus fructueuses (on ajoute à chaque fois le minimum possible pour faire passer l'erreur) on arrive à ce que nos tests passent !

#### money.py


~~~ python
class Dollar:
    def __init__(self, amount):
        self.amount = 10

    def times(self, multiplier):
        pass
~~~


#### ??

Halte là ! Ce n'est pas fini. Nos tests passent mais il reste un étape à faire : *supprimer les duplications*. Entre chaque étape on relance les tests pour être sûr que tout passe. Si on reste vert, on a pas cassé le code ! 

  1. le `10` du test est dupliqué avec le `10` du `self.amount`. C'est en fait `5 * 2`
  2. le `5` du `self.amount` est en fait une duplication du paramètre `amount`, et le `* 2` 
  3. `le * 2` est en fait utile avec la méthode `times()` on le rajoute donc dedans et le supprime de `self.amount` 
  4. `2` de la méthode `times` est en en fait une duplication du paramètre `multiplier`.
  5. on peut même utiliser l'opérateur `*=` dans la méthode `times`.


On ne vous demande pas de toujours faire comme ça, c'est une méthode qui marche lorsque l'on ne sait pas aller plus vite. C'est bourrin et sans interprétation possible. On vient de découvrir une règle du TDD pour faire passer des tests : **fake it**

#### money.py

~~~ python
class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        self.amount *= multiplier
~~~

#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 * 2 = $10~~
  - utiliser `amount` ? Le rendre privé
  - five == 10 n'est pas vraiment super. non mutable
  - gestion des arrondis 


### 2 - value object

On veut faire du **clean code that works**. Mais c'est très difficile même pour des très bons codeurs. Donc on va séparer le problème : 

  1. on commence par le *that works*
  2. on fini par le *clean code*

Que faire maintenant ? 

#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 * 2 = $10~~
  - utiliser `amount` ? Le rendre privé
  - **five == 10 n'est pas vraiment super. non mutable**
  - gestion des arrondis 

#### ?? 

Rendre des objets non mutable : des *value object* c'est super chouette. On a plus besoin de faire attention à eux. Une fois créés ils ne bougent plus. On peut donc les donner à des méthodes inconnues sans avoir peur qu'ils soient modifiés, ou les utiliser dans nos propres méthodes sans craindre qu'ils soient modifiés plus tard.

Si l'on veut modifier un value objet, il faut en créer un autre. Heureusement, dans la plupart du temps ce n'est pas très coûteux.

#### tests.py 

On voudrait pouvoir multiplier plein de fois différentes nos dollars et que ça ne pose pas de soucis. Genre : 

~~~ python
from money import Dollar

def test_multiplication():
    five = Dollar(5)
    five.times(2)
        
    assert 10 == five.amount

    five.times(3)
        
    assert 15 == five.amount
~~~    


Mais comme ça c'est pas possible : *value objects* to the rescue : 


~~~ python
from money import Dollar

def test_multiplication():
    five = Dollar(5)
    
    product = five.times(2)
    assert 10 == product.amount

    product = five.times(3)        
    assert 15 == product.amount
~~~


Pour être sur que notre objet n'est pas modifié, il faut faire 2 test à la suite.


#### money.py

Ce coup ci, pas besoin de grandes manipulations : il faut que la méthode *times* rende un objet `Dollar`. Si l'implémentation semble évidente, autant la coder de suite (mais après le test !).  On vient de découvrir une autre règle du TDD pour faire passer des tests (on va en utiliser 3) : **obvious implementation** (on change directement le code). 

Si le code à mettre n'est pas évident, on utilise la première règle, le **fake it** où l'on remplace petit à petit les duplications.

~~~ python
class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)
~~~

#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 * 2 = $10~~
  - utiliser `amount` ? Le rendre privé
  - ~~five == 10 n'est pas vraiment super. non mutable~~
  - gestion des arrondis 

### 3 - `==`

Pour vérifier que deux objets sont égaux, on ne va pas passer son temps à vérifier que tous leurs attributs soient les même. On va le faire une fois pour toute (ce qui évite les duplications). On le rajoute donc dans le tbd :

#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 * 2 = $10~~
  - utiliser `amount` ? Le rendre privé
  - ~~five == 10 n'est pas vraiment super. non mutable~~
  - gestion des arrondis 
  - **==**


On va utiliser pour cela des méthodes spéciales de python qui permettent d'utiliser les opérateurs `==` et `!=` même si on est pas des entiers. Mais avant d'aller plus loin, les tests.

#### tests.py 


~~~ python
from money import Dollar


def test_equality():
    assert Dollar(5) == Dollar(5)

def test_multiplication():
    five = Dollar(5)

    product = five.times(2)
    assert 10 == product.amount

    product = five.times(3)
    assert 15 == product.amount
 ~~~
 
Bien sur, le test rate. Par défaut, lorsque l'on a pas défini de méthode `__eq__` et `__ne__`, l'opérateur `==` regarde si ce sont les mêmes objets, ce qui n'est pas le cas.

#### money.py

Faisons passer le test : 

~~~ python
class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)
        
    def __eq__(self, other):
        return True
~~~

Avec ce code lorsque l'on écrit `x == y`, python le re-écrit en : `x.__eq__(y)`. Du coup notre *fake it* fait passer le test.

Mais ce n'est toujours pas ce que l'on veut. Pour cela on va utiliser la troisième règle du TDD : **triangulation**

#### tests.py 

On utilise la **triangulation** lorsque l'on ne sait pas trop quoi faire pour supprimer les duplications. On écrit alors un autre test pour le même problème. Si le test est différent du premier, pour qu'il passe il faudra supprimer des duplications. On ajoute alors autant de tests qu'il faut jusqu'à ce que les duplications aient disparues. Les tests que l'on rajoute dépendent donc des duplications que l'on a.

Dans notre cas, on répond toujours `True`, on va donc forger un test qui doit répondre `False` :

~~~ python
from money import Dollar


def test_equality():
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(6)

def test_multiplication():
    five = Dollar(5)

    product = five.times(2)
    assert 10 == product.amount

    product = five.times(3)
    assert 15 == product.amount
 ~~~


#### money.py

~~~ python
class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)
        
    def __eq__(self, other):
        return self.amount == other.amount
~~~

#### ?? 
    
Pour l'instant on ne teste pas si l'objet `other` a la propriété `amount`. Voir même si l'objet existe (`five == None` va planter plutôt que de répondre `False`). On va pas s'embêter avec ça pour l'instant, mais on va le rajouter à notre todolist.

#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 * 2 = $10~~
  - utiliser `amount` ? Le rendre privé
  - ~~five == 10 n'est pas vraiment super. non mutable~~
  - gestion des arrondis 
  - ~~==~~
  - == None
  - == autre chose qu'un Dollar


#### ?? 

Tiens si on en profitait pour voir toutes les méthodes spéciales que l'on pourrait utiliser ?

http://www.diveintopython3.net/special-method-names.html#acts-like-number

ou 

https://micropyramid.com/blog/python-special-class-methods-or-magic-methods/


Pourquoi on n'utiliserait pas `__mul__` ? 


### 4 - `__mul__` 

#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 * 2 = $10~~
  - utiliser `amount` ? Le rendre privé
  - ~~five == 10 n'est pas vraiment super. non mutable~~ 
  - gestion des arrondis 
  - ~~==~~
  - == None
  - == autre chose qu'un Dollar
  - **`__mul__`**


#### tests.py 

On va modifier le test de multiplication. 

~~~ python
from money import Dollar

def test_equality():
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(6)

def test_multiplication():
    five = Dollar(5)

    product = five * 2
    assert 10 == product.amount

    product = five * 3
    assert 15 == product.amount
 ~~~

Pour python écrire `five * 3` est équivalent à `five.__mul__(3)`. C'est l'objet de gauche qui est utilisé.

#### money.py

C'est assez simple pour être **obvious implementation** :

 ~~~ python
 class Dollar:
     def __init__(self, amount):
         self.amount = amount

     def __mul__(self, multiplier):
         return Dollar(self.amount * multiplier)
        
     def __eq__(self, other):
         return self.amount == other.amount
 ~~~

#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 * 2 = $10~~
  - utiliser `amount` ? Le rendre privé
  - ~~five == 10 n'est pas vraiment super. non mutable~~
  - gestion des arrondis 
  - ~~==~~
  - == None
  - == autre chose qu'un Dollar
  - ~~`__mul__`~~


### 5 - privacy

#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 * 2 = $10~~
  - **utiliser `amount` ? Le rendre privé**
  - ~~five == 10 n'est pas vraiment super. non mutable~~
  - gestion des arrondis 
  - ~~==~~
  - == None
  - == autre chose qu'un Dollar
  - ~~`__mul__`~~

Il ne manque pas grand chose pour que amount soit privé. Il suffit de ne pas en parler dans les tests. On peut le faire car dans la multiplication, on veut que `five * 2` soit égal à 10 dollars par exemple. Faisons le :

~~~ python
from money import Dollar

def test_equality():
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(6)

def test_multiplication():
    five = Dollar(5)

    product = five * 2
    assert Dollar(10) == product

    product = five * 3
    assert Dollar(15) == product
 ~~~


On peut même encore faire plus joli : 

~~~ python
from money import Dollar

def test_equality():
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(6)

def test_multiplication():
    five = Dollar(5)

    assert Dollar(10) == five * 2
    assert Dollar(15) == five * 3
 ~~~


Notez que l'on a utilisé une fonctionnalité que l'on vient de créer pour améliorer un test. C'est normal les tests et le code forment une seule entité. 

Maintenant si 2 tests plantent en même temps (si le `==` commence à rater par exemple), il faudra se rappeler quel est le test qui plante et les tests qui ne fonctionnent plus.

#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 * 2 = $10~~
  - ~~utiliser `amount` ? Le rendre privé~~
  - ~~five == 10 n'est pas vraiment super. non mutable~~
  - gestion des arrondis 
  - ~~==~~
  - == None
  - == autre chose qu'un Dollar
  - ~~`__mul__`~~

### 6 -  les Francs

Le seul item dans la todolist qui ne soit pas de l'optimisation est *5 + 2.5CHF = $10 si le taux de change est 1:.5*. Cela semble bien trop ambitieux pour une seule étape. On va la découper, en commençant par introduire les CHF : 

#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 * 2 = $10~~
  - ~~utiliser `amount` ? Le rendre privé~~
  - ~~five == 10 n'est pas vraiment super. non mutable~~
  - gestion des arrondis 
  - ~~==~~
  - == None
  - == autre chose qu'un Dollar
  - ~~`__mul__`~~
  - **5 CHF * 2 = 10CHF** 


#### tests.py 

On va dupliquer le test des dollars pour les Francs : 

  - heureusement qu'on a un peu modifier les tests avant, non ? 
  - on a le droit de commettre les pires péchés pour faire marcher le projet (that works), ensuite on fait les choses bien (clean code)


~~~ python
from money import Dollar, Franc

def test_equality():
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(6)

def test_dollar_multiplication():
    five = Dollar(5)

    assert Dollar(10) == five * 2
    assert Dollar(15) == five * 3
    
def test_franc_multiplication():
    five = Franc(5)

    assert Franc(10) == five * 2
    assert Franc(15) == five * 3
~~~
 

#### money.py

Idem que pour les tests, on copie/colle : 

~~~ python
class Franc:
     def __init__(self, amount):
         self.amount = amount

     def __mul__(self, multiplier):
         return Franc(self.amount * multiplier)
        
     def __eq__(self, other):
         return self.amount == other.amount
 
 
 class Dollar:
     def __init__(self, amount):
         self.amount = amount

     def __mul__(self, multiplier):
         return Dollar(self.amount * multiplier)
        
     def __eq__(self, other):
         return self.amount == other.amount
~~~



#### tbd

tous les péchés doivent être expiés, on rajoute donc ce qu'il faut corriger dans la todo list.


  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 * 2 = $10~~
  - ~~utiliser `amount` ? Le rendre privé~~
  - ~~five == 10 n'est pas vraiment super. non mutable~~
  - gestion des arrondis 
  - ~~`==`~~
  - `== None`
  - `==` autre chose qu'un Dollar
  - ~~`__mul__`~~
  - ~~5 CHF * 2 = 10CHF~~
  - duplication Franc/dollar
  - même `==` 
  - `*` presque identique.


### 7 - même `==`  pour tous

#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 * 2 = $10~~
  - ~~utiliser `amount` ? Le rendre privé~~
  - ~~five == 10 n'est pas vraiment super. non mutable~~
  - gestion des arrondis 
  - ~~`==`~~
  - `== None`
  - `==` autre chose qu'un Dollar
  - ~~`__mul__`~~
  - ~~5 CHF * 2 = 10CHF~~
  - duplication Franc/dollar
  - **même `==`** 
  - `*` presque identique.

#### ??

Pour avoir le même égal on va essayer d'avoir une unique classe qui la contienne. On pourrait faire hériter une monnaie réelle de l'autre mais c'est pas super. Autant faire une classe abstraite qui les englobe tous les 2.

#### money.py

On va faire pas à pas la modification d'ajout d'une classe mère aux deux classes et entre chaque étape on vérifie que les tests passent toujours.

  1. ajout de la classe Money qui ne fait rien
  2. ajout de money comme classe mère de `Franc` et `Dollar`

Maintenant on va faire monter les méthodes identiques des classes filles à la classe mère.

  3. `__init__` est identique : on le remonte
  4. `__eq__` est identique : on ne peut cependant pas le remonter car on ne teste pas l'égalité des Francs entres eux.
  5. on rajoute le test des Francs entres eux et on en profite pour rajouter un todo sur la comparaison entre Franc et Dollar. On ne le fait pas tout de suite car on a pas fini notre item. ON ne fait qu'une chose à la fois sinon plus rien ne fonctionne. On se rappelle qu'on ne **code que sur du vert**.
  6. on copie colle les tests du dollar


#### tests.py 

~~~ python
from money import Dollar, Franc


def test_equality():
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(6)
    
    assert Franc(5) == Franc(5)
    assert Franc(5) != Franc(6)

def test_dollar_multiplication():
    five = Dollar(5)

    assert Dollar(10) == five * 2
    assert Dollar(15) == five * 3
    
def test_franc_multiplication():
    five = Franc(5)

    assert Franc(10) == five * 2
    assert Franc(15) == five * 3
~~~


#### money.py

~~~ python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount


class Franc(Money):
    def __mul__(self, multiplier):
        return Franc(self.amount * multiplier)


class Dollar(Money):
    def __mul__(self, multiplier):
        return Dollar(self.amount * multiplier)
~~~

#### tbd


  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 * 2 = $10~~
  - ~~utiliser `amount` ? Le rendre privé~~
  - ~~five == 10 n'est pas vraiment super. non mutable~~
  - gestion des arrondis 
  - ~~==~~
  - == None
  - == autre chose qu'un Dollar
  - ~~`__mul__`~~
  - ~~5 CHF * 2 = 10CHF~~
  - duplication Franc/dollar
  - ~~même ==~~
  - `*` presque identique.
  - compare Franc et Dollar




### 8 -  Franc et Dollar 

#### tbd


  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 * 2 = $10~~
  - ~~utiliser `amount` ? Le rendre privé~~
  - ~~five == 10 n'est pas vraiment super. non mutable~~
  - gestion des arrondis 
  - ~~==~~
  - == None
  - == autre chose qu'un Dollar
  - ~~`__mul__`~~
  - ~~5 CHF * 2 = 10CHF~~
  - duplication Franc/dollar
  - ~~même ==~~
  - `*` presque identique.
  - **compare Franc et Dollar**



#### tests.py 


Allons-y pour un petit test en plus

~~~ python
from money import Dollar, Franc

def test_equality():
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(6)
    
    assert Franc(5) == Franc(5)
    assert Franc(5) != Franc(6)
    assert Franc(5) != Dollar(5)

def test_dollar_multiplication():
    five = Dollar(5)

    assert Dollar(10) == five * 2
    assert Dollar(15) == five * 3
    
def test_franc_multiplication():
    five = Franc(5)

    assert Franc(10) == five * 2
    assert Franc(15) == five * 3
~~~


#### money.py

Une façon simple de corriger cela est de rajouter le fait que les 2 objets à comparer soient de la même classe : la classe d'un objet est l'attribut spécial `__class__` présent dans chaque objet. 

~~~ python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.amount == other.amount


class Franc(Money):
    def __mul__(self, multiplier):
        return Franc(self.amount * multiplier)


class Dollar(Money):
    def __mul__(self, multiplier):
        return Dollar(self.amount * multiplier)
~~~


Attention, ceci n'est pas du tout une bonne façon de coder. Votre **code smell** (qui vient avec le temps) devrait vous avertir. Notre comparateur utilise ce que sont les devise d'un point de vue de python (deux classes différentes) pas d'un point de vue de la finance (devise ?). Ce n'est jamais bon. Ca risque (va) nous sauter à la figure tôt ou tard. On rajoute donc un todo pour montrer que cela nous embête tout de même un peu.

#### tbd

tous les péchés doivent être expiés, on rajoute donc ce qu'il faut corriger dans la todo list.


  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 * 2 = $10~~
  - ~~utiliser `amount` ? Le rendre privé~~
  - ~~five == 10 n'est pas vraiment super. non mutable~~
  - gestion des arrondis 
  - ~~==~~
  - == None
  - == autre chose qu'un Dollar
  - ~~`__mul__`~~
  - ~~5 CHF * 2 = 10CHF~~
  - duplication Franc/dollar
  - ~~même ==~~
  - `*` presque identique.
  - ~~compare Franc et Dollar~~
  - utilisation de devise ?


### 9 -  Duplication Franc/Dollar

#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 * 2 = $10~~
  - ~~utiliser `amount` ? Le rendre privé~~
  - ~~five == 10 n'est pas vraiment super. non mutable~~
  - gestion des arrondis 
  - ~~==~~
  - == None
  - == autre chose qu'un Dollar
  - ~~`__mul__`~~
  - ~~5 CHF * 2 = 10CHF~~
  - **duplication Franc/dollar**
  - ~~même ==~~
  - `*` presque identique.
  - ~~compare Franc et Dollar~~
  - utilisation de devise ?


#### ??

Les 2 implémentations de `__mul__` ont l'air extrêmement semblables. La seule chose qui les sépare est le retour soir d'un Franc soit d'un Dollar. En allant par là, l'existence même des 2 classes est sujette à caution : est-il vraiment utile d'avoir 2 classes juste pour une comparaison ?

Donc pour réunifier les 2 classes en une seule, on va commencer par gommer leurs existences dans les tests. Commençons par supprimer la classe dollar en passant par un factory dans le test `test_dollar_multiplication()`

#### tests.py 


Allons-y pour un petit test en plus

~~~ python
from money import Dollar, Franc
import money

def test_equality():
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(6)
    
    assert Franc(5) == Franc(5)
    assert Franc(5) != Franc(6)
    assert Franc(5) != Dollar(5)

def test_dollar_multiplication():
    five = money.dollar(5)

    assert Dollar(10) == five * 2
    assert Dollar(15) == five * 3
    
def test_franc_multiplication():
    five = Franc(5)

    assert Franc(10) == five * 2
    assert Franc(15) == five * 3
~~~


#### money.py

Un factory de la classe `Dollar` dans `money.py`

~~~ python
def dollar(amount):
    return Dollar(amount)


class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.amount == other.amount


class Franc(Money):
    def __mul__(self, multiplier):
        return Franc(self.amount * multiplier)


class Dollar(Money):
    def __mul__(self, multiplier):
        return Dollar(self.amount * multiplier)
~~~


Les tests passent (en ajoutant l'import des factory) ! Donc on remplace toute référence à `Dollar` en `money.dollar` dans les tests


#### tests.py 


~~~ python
from money import Franc
import money


def test_equality():
    assert money.dollar(5) == money.dollar(5)
    assert money.dollar(5) != money.dollar(6)

    assert Franc(5) == Franc(5)
    assert Franc(5) != Franc(6)

    assert Franc(5) != money.dollar(5)


def test_dollar_multiplication():
    five = money.dollar(5)

    assert money.dollar(10) == five * 2
    assert money.dollar(15) == five * 3


def test_franc_multiplication():
    five = Franc(5)

    assert Franc(10) == five * 2
    assert Franc(15) == five * 3
~~~
 


Avant de faire la même chose pour les Francs, posons nous la question de l'utilité de garder ces tests. Ont-ils une utilité dans le code ? Pas sûr puisque on ne fait plus qu'une seule classe, mais dons le doute on les conserve, mais on l'ajoute à la todo list.


~~~ python
import money


def test_equality():
    assert money.dollar(5) == money.dollar(5)
    assert money.dollar(5) != money.dollar(6)

    assert money.franc(5) == money.franc(5)
    assert money.franc(5) != money.franc(6)

    assert money.franc(5) != money.dollar(5)


def test_dollar_multiplication():
    five = money.dollar(5)

    assert money.dollar(10) == five * 2
    assert money.dollar(15) == five * 3


def test_franc_multiplication():
    five = money.franc(5)

    assert money.franc(10) == five * 2
    assert money.franc(15) == five * 3
~~~


On est maintenant dans une meilleure position qu'au début. Le code utilisateur n'étant pas au courant qu'il existe 2 classes différentes. On va pouvoir passer à la suite du programme les supprimer également dans le code.

#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 * 2 = $10~~
  - ~~utiliser `amount` ? Le rendre privé~~
  - ~~five == 10 n'est pas vraiment super. non mutable~~
  - gestion des arrondis 
  - ~~==~~
  - == None
  - == autre chose qu'un Dollar
  - ~~`__mul__`~~
  - ~~5 CHF * 2 = 10CHF~~
  - **duplication Franc/dollar**
  - ~~même ==~~
  - `*` presque identique.
  - compare Franc et Dollar
  - utilisation de devise ?
  - supprimer `test_franc_multiplication` ?


#### money.py


~~~ python
def dollar(amount):
    return Dollar(amount)


def franc(amount):
    return Franc(amount)


class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.amount == other.amount


class Franc(Money):
    def __mul__(self, multiplier):
        return Franc(self.amount * multiplier)


class Dollar(Money):
    def __mul__(self, multiplier):
        return Dollar(self.amount * multiplier)
~~~

### 10 - devises

Pour pouvoir supprimer les 2 sous classes, il va nous falloir un moyen de distinguer les Francs des Dollars. Donc autant travailler sur l'ajout d'une devise.


#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 * 2 = $10~~
  - ~~utiliser `amount` ? Le rendre privé~~
  - ~~five == 10 n'est pas vraiment super. non mutable~~
  - gestion des arrondis 
  - ~~==~~
  -  == None
  - == autre chose qu'un Dollar
  - ~~`__mul__`~~
  - ~~5 CHF * 2 = 10CHF~~
  - duplication Franc/dollar
  - ~~même ==~~
  - * presque identique.
  - compare Franc et Dollar
  - **utilisation de devise ?** 
  - supprimer `test_franc_multiplication` ?

#### tests.py 

On ajoute un test pour vérifier que les dollars et les francs ont des devises différentes.

~~~ python
import money


def test_currencies():
    assert "USD" == money.dollar(1).currencies()
    assert "CHF" == money.franc(1).currencies()
    
    
def test_equality():
    assert money.dollar(5) == money.dollar(5)
    assert money.dollar(5) != money.dollar(6)

    assert money.franc(5) == money.franc(5)
    assert money.franc(5) != money.franc(6)

    assert money.franc(5) != money.dollar(5)


def test_dollar_multiplication():
    five = money.dollar(5)

    assert money.dollar(10) == five * 2
    assert money.dollar(15) == five * 3


def test_franc_multiplication():
    five = money.franc(5)

    assert money.franc(10) == five * 2
    assert money.franc(15) == five * 3
~~~



#### money.py

une *obvious implementation* plus tard : 

~~~ python
def dollar(amount):
    return Dollar(amount)


def franc(amount):
    return Franc(amount)


class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.amount == other.amount


class Franc(Money):
    def __mul__(self, multiplier):
        return Franc(self.amount * multiplier)

    def currencies(self):
        return "CHF"

class Dollar(Money):
    def __mul__(self, multiplier):
        return Dollar(self.amount * multiplier)

    def currencies(self):
        return "USD"
~~~


On peut maintenant travailler à faire monter les currencies au niveau de `Money`. Commençons par les faire monter au niveu des classes. On va créer un attribut `currency` dans chaque classe et l'utiliser dans les méthodes. Il faut pour cela redescendre les `__init__` dans chaque classe.


~~~ python
def dollar(amount):
    return Dollar(amount)


def franc(amount):
    return Franc(amount)


class Money:
    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.amount == other.amount


class Franc(Money):
    def __init__(self, amount):
        self.amount = amount
        self.currency = "CHF"

    def currencies(self):
        return self.currency

    def __mul__(self, multiplier):
        return Franc(self.amount * multiplier)


class Dollar(Money):
    def __init__(self, amount):
        self.amount = amount
        self.currency = "USD"

    def currencies(self):
        return self.currency

    def __mul__(self, multiplier):
        return Dollar(self.amount * multiplier)
~~~


Afin de faire remonter l'attribut `currency` dans la classe Money, on va commencer par dire que currency est un paramètre des `__init__`. Comme toute devise est créé avec le factory, ça devrait passer et nous permettre ensuite de ne faire plus qu'une seule classe puisque seuls les paramètres des méthodes vont différer.

En ajoutant le paramètre les tests plantent ! C'est parce que l'on a oublié d'ajouter un paramètre aux factory : 

~~~ python
def franc(amount):
    return Franc(amount, None)
~~~


Les tests plantent encore... C'est parce que `__mul__` n'utilise pas le factory : 

~~~ python
class Franc(Money):
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = "CHF"

    def currencies(self):
        return self.currency

    def __mul__(self, multiplier):
        return franc(self.amount * multiplier)
~~~


Ouf, les tests passent. On peut faire pareil pour dollar : 

~~~ python
def dollar(amount):
    return Dollar(amount, None)


def franc(amount):
    return Franc(amount, None)


class Money:

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.amount == other.amount


class Franc(Money):
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = "CHF"

    def currencies(self):
        return self.currency

    def __mul__(self, multiplier):
        return franc(self.amount * multiplier)


class Dollar(Money):
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = "USD"

    def currencies(self):
        return self.currency

    def __mul__(self, multiplier):
        return dollar(self.amount * multiplier)
~~~


Il nous reste plus qu'à utiliser le paramètre `currency` des constructeurs dans les factory. Les classes se ressemblent de plus en plus : 

~~~ python
def dollar(amount):
    return Dollar(amount, "USD")


def franc(amount):
    return Franc(amount, "CHF")


class Money:

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.amount == other.amount


class Franc(Money):
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def currencies(self):
        return self.currency

    def __mul__(self, multiplier):
        return franc(self.amount * multiplier)


class Dollar(Money):
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def currencies(self):
        return self.currency

    def __mul__(self, multiplier):
        return dollar(self.amount * multiplier)
~~~


Le `__init__` est re le même, ainsi que `currencies`on peut les bouger dans money (courage on y est presque) :


~~~ python
def dollar(amount):
    return Dollar(amount, "USD")


def franc(amount):
    return Franc(amount, "CHF")


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def currencies(self):
        return self.currency

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.amount == other.amount


class Franc(Money):
    def __mul__(self, multiplier):
        return franc(self.amount * multiplier)


class Dollar(Money):
    def __mul__(self, multiplier):
        return dollar(self.amount * multiplier)
~~~

Tout est prêt pour maintenant supprimer les sous-classes.


#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 * 2 = $10~~
  - ~~utiliser `amount` ? Le rendre privé~~
  - ~~five == 10 n'est pas vraiment super. non mutable~~
  - gestion des arrondis 
  - ~~==~~
  - == None
  - == autre chose qu'un Dollar
  - ~~`__mul__`~~
  - ~~5 CHF * 2 = 10CHF~~
  - duplication Franc/dollar
  - ~~même ==~~
  - * presque identique.
  - compare Franc et Dollar
  - ~~utilisation de devise ?~~
  - supprimer `test_franc_multiplication` ?


Ici, utiliser une tâche annexe (les devises) nous a permis d'avancer vers notre but : supprimer les sous classes.



### 11 -  unification de `*`

Tout est prêt pour unifier les `__mul__` et ainsi faire disparaitre les dernières différences entre les 2 classes.

#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 * 2 = $10~~
  - ~~utiliser `amount` ? Le rendre privé~~
  - ~~five == 10 n'est pas vraiment super. non mutable~~
  - gestion des arrondis 
  - ~~==~~
  - == None
  - == autre chose qu'un Dollar
  - ~~`__mul__`~~
  - ~~5 CHF * 2 = 10CHF~~
  - duplication Franc/dollar
  - ~~même ==~~
  - **`*` presque identique.**
  - compare Franc et Dollar
  - ~~utilisation de devise ?~~
  - supprimer `test_franc_multiplication` ?


#### money.py 

Les deux `__mul__` ne changent que par la classe produite. Donc commençons par expliciter la construction en remplaçant le factory par l'utilisation explicite des constructeurs : 

~~~ python
def dollar(amount):
    return Dollar(amount, "USD")


def franc(amount):
    return Franc(amount, "CHF")


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def currencies(self):
        return self.currency

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.amount == other.amount


class Franc(Money):
    def __mul__(self, multiplier):
        return Franc(self.amount * multiplier, self.currency)


class Dollar(Money):
    def __mul__(self, multiplier):
        return Dollar(self.amount * multiplier, self.currency)
~~~


On peut maintenant ajouter une méthode `__mul__` das la classe money : 

~~~ python
def dollar(amount):
    return Dollar(amount, "USD")


def franc(amount):
    return Franc(amount, "CHF")


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def currencies(self):
        return self.currency

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.amount == other.amount

    def __mul__(self, multiplier):
        return Money(self.amount * multiplier, self.currency)


class Franc(Money):
    def __mul__(self, multiplier):
        return Franc(self.amount * multiplier, self.currency)


class Dollar(Money):
    def __mul__(self, multiplier):
        return Dollar(self.amount * multiplier, self.currency)
~~~


En supprimant la methode `__mul__` des Francs, et en rendant un `Money` dans le factory `franc`, les tests passent.

~~~ python
def dollar(amount):
    return Dollar(amount, "USD")


def franc(amount):
    return Money(amount, "CHF")


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def currencies(self):
        return self.currency

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.amount == other.amount

    def __mul__(self, multiplier):
        return Money(self.amount * multiplier, self.currency)


class Franc(Money):
    pass

class Dollar(Money):
    def __mul__(self, multiplier):
        return Dollar(self.amount * multiplier, self.currency)
~~~


Mais supprimer la méthode `__mul__` de `Dollar` casse les tests : le test d'égalité est cassé. C'est normal il compare des classes et pas des `currency`. On revient donc en arrière jusqu'à ce que les tests passes (on remet la méthode `__mul__` à `Dollar`) puis on corrige la méthode `__eq__` pour qu'elle compare les `currency` plutôt que les classes.

~~~ python
def dollar(amount):
    return Dollar(amount, "USD")


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


class Franc(Money):
    pass


class Dollar(Money):
    def __mul__(self, multiplier):
        return Dollar(self.amount * multiplier, self.currency)
~~~

On peut maintenant supprimer la méthode `__mul__` de `Dollar` et ainsi supprimer les 2 classes. ON vient de supprimer 2 items en un seul refactoring.

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
~~~



#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 * 2 = $10~~
  - ~~utiliser `amount` ? Le rendre privé~~
  - ~~five == 10 n'est pas vraiment super. non mutable~~
  - gestion des arrondis 
  - ~~==~~
  - == None
  - == autre chose qu'un Dollar
  - ~~`__mul__`~~
  - ~~5 CHF * 2 = 10CHF~~
  - ~~duplication Franc/dollar~~
  - ~~même ==~~
  - ~~ * presque identique.~~
  - compare Franc et Dollar
  - ~~utilisation de devise ?~~
  - supprimer `test_franc_multiplication` ?

Maintenant les tests d'égalité et de multiplication des `Franc` sont vraiment inutiles puisque le code est le même que celui de dollar : 


#### tests.py

~~~ python
import money


def test_currencies():
    assert "USD" == money.dollar(1).currencies()
    assert "CHF" == money.franc(1).currencies()


def test_equality():
    assert money.dollar(5) == money.dollar(5)
    assert money.dollar(5) != money.dollar(6)

    assert money.franc(5) != money.dollar(5)


def test_multiplication():
    five = money.dollar(5)

    assert money.dollar(10) == five * 2
    assert money.dollar(15) == five * 3
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
~~~


#### tbd

  - $5 + 2.5CHF = $10 si le taux de change est 1:.5
  - ~~$5 * 2 = $10~~
  - ~~utiliser `amount` ? Le rendre privé~~
  - ~~five == 10 n'est pas vraiment super. non mutable~~
  - gestion des arrondis 
  - ~~==~~
  - == None
  - == autre chose qu'un Dollar
  - ~~`__mul__`~~
  - ~~5 CHF * 2 = 10CHF~~
  - ~~duplication Franc/dollar~~
  - ~~même ==~~
  - ~~* presque identique.~~
  - ~~compare Franc et Dollar~~
  - ~~utilisation de devise ?~~
  - ~~supprimer `test_franc_multiplication` ?~~

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
