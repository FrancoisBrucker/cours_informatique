---
layout: page
title:  "TDD et test pattern : partie 2/3"
author: "François Brucker"
---

Partie 2/3.

<!--more-->

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [code]({% link cours/algorithme-code-theorie/code/index.md %}) / [programmation objet]({% link cours/algorithme-code-theorie/code/programmation-objet/index.md %}) / [projet : TDD]({% link cours/algorithme-code-theorie/code/programmation-objet/projet-tdd.md %}) / [partie 2/3]({% link cours/algorithme-code-theorie/code/programmation-objet/projet-tdd-2.md %})
>
> **prérequis :**
>
> * [partie 1/3]({% link cours/algorithme-code-theorie/code/programmation-objet/projet-tdd-1.md %})
>
{: .chemin}

## todo list initiale

On reprend la tdo list de la fin de la partie 1 :

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`

## 6 -  les Francs

Le seul item dans la todolist qui ne soit pas de l'optimisation est : \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5.

Cela semble bien trop ambitieux pour une seule étape. On va la découper, en commençant par introduire les CHF.

### todo list {#todo-list-6.1}

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`
* **[-] 5 CHF * 2 = 10CHF**

### faire {#faire-6.1}

On est habitué depuis la première partie, on commence par faire un test. Ici, on ne va pas trop s'embêter : on va dupliquer le test des dollars pour les Francs.

* heureusement qu'on a un peu modifier les tests avant, non ?
* on a le droit de commettre les pires péchés pour faire marcher le projet (*that works*), ensuite on fait les choses bien (*clean code*)

*"test_monnaie.py"* :

```python
# ...

def test_multiplication_dollar():
    cinq = Dollar(5)

    assert Dollar(10) == cinq * 2
    assert Dollar(15) == cinq * 3


def test_multiplication_franc():
    cinq = Franc(5)

    assert Franc(10) == cinq * 2
    assert Franc(15) == cinq * 3

# ... 
```

> Faite fonctionner les tests en copiant/collant de `Dollar` une classe `Franc`
{: .a-faire}
{% details solution %}

*"monnaie.py"* :

```python
# ...

class Franc:
    def __init__(self, montant):
        self.montant = montant

    def __mul__(self, multiplicateur):
        return Franc(self.montant * multiplicateur)

    def __eq__(self, other):
        return self.montant == other.montant

# ...
```

{% enddetails %}

### todo list {#todo-list-6.2}

Tous les péchés qui ont été commis pour faire passer le test doivent être expiés. Pour s'en rappeler, on rajoute  ce qu'il faut corriger dans la todo list.

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`
* [X] 5 CHF * 2 = 10CHF
* [ ] duplication Franc/dollar
* [ ] même `==` (code identique dans 2 classes différentes)
* [ ] `*` presque identique.

Notez que même s'il n'y pas de duplication proprement dite entre les deux méthode `__mul__` elles sont trop semblable pour être honnêtes. On rajoute donc un item dans la toto-list pour voir si à un moment donné il ne faudra pas les unifier.

## 7 - même `==`  pour tous

### todo list {#todo-list-7.1}

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`
* [X] 5 CHF * 2 = 10CHF
* [ ] duplication Franc/dollar
* **[-] même `==` (code identique dans 2 classes différentes)**
* [ ] `*` presque identique.

### faire {#faire-7.1}

Pour avoir le même égal on va essayer d'avoir une unique classe qui la contienne. On pourrait faire hériter une monnaie réelle de l'autre mais c'est pas super (qui serait la classe principale ?).

Autant faire une classe abstraite qui les englobe tous les 2. On va ajouter pas à pas une classe mère aux deux classes `Franc` et `Dollar`.

> 1. Vérifiez que les tests passent
> 2. ajoutez une classe `Monnaie` qui ne fait rien
> 3. Vérifiez que les tests passent
> 4. faites hériter `Dollar` et `Franc` de la classe `Monnaie`
> 5. Vérifiez que les tests passent
{: .a-faire}
{% details solution %}

*"monnaie.py"* :

```python
class Monnaie:
    pass


class Dollar(Monnaie):
    # ...

class Franc(Monnaie):
    # ...

```

{% enddetails %}

Maintenant on va faire monter les méthodes identiques des classes filles à la classe mère.

> La méthode `__init__` est identique : remontez la dans la classe mère
{: .a-faire}
{% details solution %}

*"monnaie.py"* :

```python
class Monnaie:
    def __init__(self, montant):
        self.montant = montant



class Dollar(Monnaie):
    # pas de méthode __init__
    # ...

class Franc(Monnaie):
    # pas de méthode __init__
    # ...

```

{% enddetails %}

Attention, même si la méthode `__eq__` est identique pour les deux classe, on ne teste pas encore l'égalité ou non entre 2 `Franc`, on ne sait donc pas si le mouvement de `__eq__` dans la classe mère va se passer sans problème.

> Ajoutez des tests d'égalité et de différence pour les Francs
{: .a-faire}
{% details solution %}

*"test_monnaie.py"* :

```python
# ...

def test_egalite_dollar():
    assert Dollar(5) == Dollar(5)


def test_egalite_franc():
    assert Franc(5) == Franc(5)


def test_non_egalite_dollar():
    assert Dollar(5) != Dollar(6)


def test_non_egalite_franc():
    assert Franc(5) != Franc(6)

# ...
```

{% enddetails %}

On se rend compte que l'on ne teste pas l'inégalité entre `Dollar` et `Franc` : **on ne le fait pas tout de suite**, car on a pas fini notre item de la todo list

> **Test pattern :** On ne fait pas 2 choses en même temps. On résoud chaque item de la todo  list les uns à la suite des autres.
{: .note}

En revanche, comme il va falloir le faire :

> ajoutez la comparaison entre franc et dollar dans la todo list
{: .a-faire}

### todo list {#todo-list-7.2}

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`
* [X] 5 CHF * 2 = 10CHF
* [ ] duplication Franc/dollar
* **[-] même `==` (code identique dans 2 classes différentes)**
* [ ] `*` presque identique.
* [ ] compare Franc et Dollar

### faire {#faire-7.2}

Tout est prêt pour finaliser notre item :

> Remontez la méthode `__eq__` dans la classe mère.
{: .a-faire}
{% details solution %}

*"monnaie.py"* :

```python
class Monnaie:
    def __init__(self, montant):
        self.montant = montant

    def __eq__(self, other):
        return self.montant == other.montant


class Dollar(Monnaie):
    def __mul__(self, multiplicateur):
        return Dollar(self.montant * multiplicateur)


class Franc(Monnaie):
    def __mul__(self, multiplicateur):
        return Franc(self.montant * multiplicateur)
```

{% enddetails %}

### todo list {#todo-list-7.3}

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`
* [X] 5 CHF * 2 = 10CHF
* [ ] duplication Franc/dollar
* [X] même `==` (code identique dans 2 classes différentes)
* [ ] `*` presque identique.
* [ ] compare Franc et Dollar

## 8 -  Franc et Dollar

On peut maintenant s'occuper de la tâche que l'on vient de rajouter.

### todo list {#todo-list-8.1}

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`
* [X] 5 CHF * 2 = 10CHF
* [ ] duplication Franc/dollar
* [X] même `==` (code identique dans 2 classes différentes)
* [ ] `*` presque identique.
* **[-] compare Franc et Dollar**

### faire {#faire-8.1}

> Ajoutez un test qui vérifie que des francs ne sont pas des dollars
{: .a-faire}
{% details solution %}

*"test_monnaie.py"* :

```python
# ...

def test_franc_dollar():
    assert Franc(1) != Dollar(1)

# ...
```

{% enddetails %}

Et les tests ratent ! En effet, selon `__eq__` les Francs **sont** des dollars.

Une façon simple de corriger cela est de rajouter le fait que les 2 objets à comparer soient de la même classe.

> En python, la classe d'un objet est l'attribut spécial `__class__` présent dans chaque objet.

> Modifiez le code de `__eq__` pour vérifier que les classes des 2 objets sont bien différentes.
{: . a-faire}
{% details solution %}

*"monnaie.py"* :

```python
# ...

class Monnaie:
    # ...

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.montant == other.montant

    # ...

# ...
```

{% enddetails %}

> Votre **code smell** doit être en alerte maxiale !
{: .attention}

Ceci n'est en effet pas du tout une bonne façon de coder. Notre comparateur utilise ce que sont les devise d'un point de vue de python (deux classes différentes) pas d'un point de vue de la finance (devise ?). Ce n'est jamais bon. Ca risque (va) nous sauter à la figure tôt ou tard.

> Dans la mesure du possible, votre code doit être écrit du point de vue de ce que représentent les objets codées et non comment ils sont codés
{: .note}

On rajoute donc un todo pour montrer que cela nous embête tout de même un peu.

### todo list {#todo-list-8.2}

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`
* [X] 5 CHF * 2 = 10CHF
* [ ] duplication Franc/dollar
* [X] même `==` (code identique dans 2 classes différentes)
* [ ] `*` presque identique.
* [X] compare Franc et Dollar
* [ ] utilisation de devises plutôt que de classes ?

### 9 -  Duplication Franc/Dollar

### todo list {#todo-list-9.1}

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`
* [X] 5 CHF * 2 = 10CHF
* **[-] duplication Franc/dollar**
* [X] même `==` (code identique dans 2 classes différentes)
* [ ] `*` presque identique.
* [X] compare Franc et Dollar
* [ ] utilisation de devises plutôt que de classes ?

### faire {#faire-9.1}

Les 2 implémentations de `__mul__` sont très semblables : la seule chose qui les sépare est leurs retours (un `Franc` ou un `Dollar`).

C'est même la seule chose qui diffère entre `DOllar` et `Franc`... L'existence même des 2 classes est sujette à caution : est-il vraiment utile d'avoir 2 classes juste pour une comparaison ?

**On ne va garder qu'une seule classe**.

Pour réaliser cela, on va commencer par gommer leurs existences dans les tests. 

> ici : parler de factory. Design pattern évident > on crée les objet par des méthodes pas par des construteurs
{: .tbd}

Commençons par supprimer la classe dollar en passant par un factory dans le test `test_dollar_multiplication()`

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
