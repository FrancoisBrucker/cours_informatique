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

## Principe du TDD

On rappelle le principe du TDD :

> **Principe du TDD :**
>
> 1. **rouge** :
>    * écrire *rapidement* un *petit* test
>    * lancer les tests et les voir planter, voir même  ne correspondre à aucun code.
> 2. **vert** :
>    * écrire le code *minimal* qui permet de faire passer le test
>    * lancer les tests et les voir tous réussir
> 3. **code/refactor** :
>    * élimine les duplications tout en conservant la validité des tests.
>
> La partie refactor, qui est la partie réelle où l'on code ne se fait **que sur du vert** : on est assuré de ne pas casser le code puisque les tests passent.
{: .note}

Cela va être bien présent dans cette partie ou l'on va drastiquement modifier notre code. On va créer des tests qui seront notre filet de sécurité puis une fois que tout est vert on codera **tout en conservant le vert**.

Cela permet, en plus d'avoir un feedback immédiat en cas d'erreur (les tests ne passent plus on est **rouge**), d'avoir confiance dans ce que l'on code (si c'est vert c'est quo'n a rien cassé).

## todo list initiale

On reprend la todo list de la fin de la partie 1 :

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`

## 6 -  les Francs

Le seul item dans la todo list qui ne soit pas de l'optimisation est : \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5.

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
* [ ] `*` presque identique

Notez que même s'il n'y pas de duplication proprement dite entre les deux méthode `__mul__` elles sont trop semblable pour être honnêtes. On rajoute donc un item dans la todo list pour voir si à un moment donné il ne faudra pas les unifier.

## 7 - même `==`  pour tous

### todo list {#todo-list-7.1}

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`
* [X] 5 CHF * 2 = 10CHF
* [ ] duplication Franc/dollar
* **[-] même `==` (code identique dans 2 classes différentes)**
* [ ] `*` presque identique

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

> **Test pattern :** On ne fait pas 2 choses en même temps. On résout chaque item de la todo  list les uns à la suite des autres.
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
* [ ] `*` presque identique
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
* [ ] `*` presque identique
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
* [ ] `*` presque identique
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

En python, la classe d'un objet est l'attribut spécial `__class__` présent dans chaque objet.

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

> Votre **code smell** doit être en alerte maximale !
{: .attention}

Ceci n'est en effet pas du tout une bonne façon de coder. Notre comparateur utilise ce que sont les devise d'un point de vue de python (deux classes différentes) pas d'un point de vue de la finance (devise ?). Ce n'est jamais bon. Ça risque (va) nous sauter à la figure tôt ou tard.

> Dans la mesure du possible, votre code doit être écrit du point de vue de ce que représentent les objets codées et non comment ils sont codés
{: .note}

On rajoute donc un item dans la todo list pour montrer que cela nous embête tout de même un peu.

### todo list {#todo-list-8.2}

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`
* [X] 5 CHF * 2 = 10CHF
* [ ] duplication Franc/dollar
* [X] même `==` (code identique dans 2 classes différentes)
* [ ] `*` presque identique
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
* [ ] `*` presque identique
* [X] compare Franc et Dollar
* [ ] utilisation de devises plutôt que de classes ?

### faire {#faire-9.1}

Les 2 implémentations de `__mul__` sont très semblables : la seule chose qui les sépare est leurs retours (un `Franc` ou un `Dollar`).

C'est même la seule chose qui diffère entre `Dollar` et `Franc`... L'existence des 2 classes est sujette à caution : est-il vraiment utile d'avoir 2 classes juste pour une comparaison ?

**On ne va garder qu'une seule classe**.

Mais avant cela on va s'assurer que les fonctionnalités des `Franc` et des `Dollars` sont bien toutes représentées dans nos tests, ceci nous permettra de supprimer les classes en confiance : leurs fonctionnalités sont préservées grâce aux tests on ne risque pas de supprimer une fonctionnalité par inadvertance.

> Regardez les fonctionnalités différentes ajouter un test pour chaque monnaie si ce n'est pas encore fait.
{: .a-faire}
{% details solution %}

Il n'y a rien à changer, tous les tests sont fait et pour les `Dollar` et pour les `Franc`.

{% enddetails %}

POur supprimer des bout de code, il ne faut pas qu'ils soient utilisés. Pour supprimer les classes `Franc` et `Dollar`, on va ainsi commencer par gommer leurs existences dans les tests (dans l'utilisation du code).

Une fois l'utilisation des classes masquées dans les tests, on pourra les supprimer tranquillement du code en gardant du vert.

### faire {#faire-9.2}

Gommer supprimer l'utilisation des classes, on va utiliser un design pattern :

> Un [design patterns](https://fr.wikipedia.org/wiki/Patron_de_conception), ou façons de faire, est pour ainsi dire de l'algorithmie objet. C'est une organisation de classes pratique pour résoudre des problèmes courant en développement.
>
> Ils permettent de résoudre nombre de problèmes courants en développement et d'éviter les [erreurs classiques](http://sahandsaba.com/nine-anti-patterns-every-programmer-should-be-aware-of-with-examples.html), aussi appelées [anti-pattern](https://fr.wikipedia.org/wiki/Antipattern).
{: .note}

Le pattern que l'on va utiliser est appelé **factory**, puisqu'il utilise des fonctions pour créer des objets.

> **design pattern :** [factory](https://refactoring.guru/fr/design-patterns/factory-method)
>
> On crée les objets via des fonctions sans (ou très peu) de paramètres plutôt qu'avec le constructeur.
>
> L'intérêt est que l'on a pas à se rappeler de toutes les possibilités du constructeur, les cas classiques d'objets sont directement accessible via une fonction.
{: .note}

Commençons par tester le *factory* la classe `Dollar`  dans le test `test_multiplication_dollar()` :

```python
from monnaie import Dollar, Franc
import monnaie

# ...

def test_multiplication_dollar():
    cinq = monnaie.dollar(5)

    assert Dollar(10) == cinq * 2
    assert Dollar(15) == cinq * 3

# ...
```

Bien sur nos tests ne passent pas (encore) :

```text
___________________________________________________
test_multiplication_dollar 
___________________________________________________

    def test_multiplication_dollar():
>       cinq = monnaie.dollar(5)
E       AttributeError: module 'monnaie' has no attribute 'dollar'

test_monnaie.py:6: AttributeError
```

Ici la fonction `dollar` définie dans le module `monnaie` (le fichier *"monnaie.py"*) est le
*factory* des objets de classe `Dollar`.

> Créez la fonction `dollar` dans le module `monnaie` pour faire passer les tests.
{: .a-faire}
{% details solution %}

*"monnaie.py"* :

```python
# ...

def dollar(montant):
    return Dollar(montant)

# ...
```

{% enddetails %}

Et hop ! Les tests passent : on est sur du vert. On va pouvoir modifier massivement nos tests.

### faire {#faire-9.3}

Maintenant que notre *factory* fonctionne (on est sur du vert), on remplace toute référence à `Dollar` en `monnaie.dollar` dans les tests.

> Remplacez toute référence à `Dollar` par `monnaie.dollar` dans les tests
{: .a-faire}
{% details solution %}

*"test_monnaie.py"* :

```python
from monnaie import Dollar, Franc
import monnaie


def test_multiplication_dollar():
    cinq = monnaie.dollar(5)

    assert monnaie.dollar(10) == cinq * 2
    assert monnaie.dollar(15) == cinq * 3


def test_multiplication_franc():
    cinq = Franc(5)

    assert Franc(10) == cinq * 2
    assert Franc(15) == cinq * 3


def test_egalite_dollar():
    assert monnaie.dollar(5) == monnaie.dollar(5)


def test_egalite_franc():
    assert Franc(5) == Franc(5)


def test_non_egalite_dollar():
    assert monnaie.dollar(5) != monnaie.dollar(6)


def test_non_egalite_franc():
    assert Franc(5) != Franc(6)


def test_franc_dollar():
    assert Franc(1) != monnaie.dollar(1)

```

{% enddetails %}

Avant de faire la même chose pour `Franc`, posons nous la question de l'utilité de garder ces tests. Ont-ils une utilité dans le code ? Pas sûr puisque on ne fait plus qu'une seule classe, mais dons le doute on les conserve, mais on l'ajoute à la todo list.

### todo list {#todo-list-9.2}

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`
* [X] 5 CHF * 2 = 10CHF
* **[-] duplication Franc/dollar**
* [X] même `==` (code identique dans 2 classes différentes)
* [ ] `*` presque identique
* [X] compare Franc et Dollar
* [ ] utilisation de devises plutôt que de classes ?
* [ ] supprimer les tests de `Franc` ?

### faire {#faire-9.4}

Maintenant que notre *factory* fonctionne (on est sur du vert), on remplace toute référence à `Franc` en `monnaie.franc` dans les tests.

> Remplacez toute référence à `Franc` par `monnaie.franc` dans les tests. POur cela procédez comme pour les `Dollar`:
>
> 1. on modifie 1 occurence de `Franc`par `monnaie.franc`
> 2. on fait passer les tests.
> 3. Une fois sur du vert on fait la modification en masse.
{: .a-faire}
{% details solution %}

*"monnaie.py"* :

```python
# ...

def franc(montant):
    return Franc(montant)

# ...
```

*"test_monnaie.py"* :

```python
import monnaie


def test_multiplication_dollar():
    cinq = monnaie.dollar(5)

    assert monnaie.dollar(10) == cinq * 2
    assert monnaie.dollar(15) == cinq * 3


def test_multiplication_franc():
    cinq = monnaie.franc(5)

    assert monnaie.franc(10) == cinq * 2
    assert monnaie.franc(15) == cinq * 3


def test_egalite_dollar():
    assert monnaie.dollar(5) == monnaie.dollar(5)


def test_egalite_franc():
    assert monnaie.franc(5) == monnaie.franc(5)


def test_non_egalite_dollar():
    assert monnaie.dollar(5) != monnaie.dollar(6)


def test_non_egalite_franc():
    assert monnaie.franc(5) != monnaie.franc(6)


def test_franc_dollar():
    assert monnaie.franc(1) != monnaie.dollar(1)

```

{% enddetails %}

On est maintenant dans une meilleure position qu'au début pour notre projet d'unifier les classes `Franc` et `Dollar` puisque Le code utilisateur n'est pas au courant qu'il existe deux classes différentes (grâce au *factory*).

On va pouvoir passer à la suite qui consiste à les supprimer également dans le code.

### todo list {#todo-list-9.3}

Il reste des duplications entre Franc et Dollar, mais pour les supprimer il faut passer par quelque chose qui les remplace. Il est donc plus judicieux de faire un autre item de notre liste.

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`
* [X] 5 CHF * 2 = 10CHF
* [ ] duplication Franc/dollar
* [X] même `==` (code identique dans 2 classes différentes)
* [ ] `*` presque identique
* [X] compare Franc et Dollar
* [ ] utilisation de devises plutôt que de classes ?
* [ ] supprimer les tests de `Franc` ?

## 10 - devises

Pour pouvoir supprimer les deux classes `Franc` et `Dollar`, il va nous falloir un moyen de les distinguer. Donc autant travailler sur l'ajout d'une devise.

### todo list {#todo-list-10.1}

Il reste des duplications entre Franc et Dollar, mais pour les supprimer il faut passer par quelque chose qui les remplace. Il est donc plus judicieux de faire un autre item de notre liste.

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`
* [X] 5 CHF * 2 = 10CHF
* [ ] duplication Franc/dollar
* [X] même `==` (code identique dans 2 classes différentes)
* [ ] `*` presque identique
* [X] compare Franc et Dollar
* **[-] utilisation de devises plutôt que de classes ?**
* [ ] supprimer les tests de `Franc` ?

### faire {#faire-10.1}

La classe `Devise` que l'on veut créer doit avoir un attribut qui nous permettra de distinguer les `Franc` des `Dollar`.

Faisons un test pour implémenter cette idée :

*"test_monnaie.py"* :

```python
# ...

def test_devise():
    assert "USD" == monnaie.dollar(1).devise
    assert "CHF" == monnaie.franc(1).devise

# ...
```

> Faites passer les tests en créant cet attribut dans les classes `Dollar` et `Franc`
{: .a-faire}
{% details solution %}

*"monnaie.py"* :

```python
# ...

def franc(montant):
    return Franc(montant)

# ...
```

On implémente cet attribut sous la forme d'un attribut de classe, en le définissant directement dans la classe.

*"monnaie.py"* :

```python
# ...

class Dollar(Monnaie):
    devise = "USD"

    # ...


class Franc(Monnaie):
    devise = "CHF"

    # ...

# ...
```

{% enddetails %}

On peut maintenant travailler à faire monter les devise au niveau de la classe `Monnaie`.

### faire {#faire-10.2}

L'idée est ici de placer la bonne devise lors dela création de l'objet dans `Monnaie`. Pour faire cela dans les règle de l'art on va utiliser un [pattern de refactoring](https://martinfowler.com/books/refactoring.html) qui permet de modifier le code sans problème.

On va utiliser :

> **refactoring pattern :** [Pull Up Field](https://refactoring.guru/fr/pull-up-field)
>
> Le but est de faire remonter un champ de sous-classes à la classe mère.
>
> Pour cela, on rend **identique** le champ dans chacune des sous-classes puis on le déplace dans la classe mère.
{: .note}

En premier lieu :

> Faite de l'attribut `devise` deux attributs affectés chacun affecté dans sa classe
{: .a-faire}
{% details solution %}

*"monnaie.py"* :

```python
# ...

class Dollar(Monnaie):
    def __init__(self, montant):
        super().__init__(montant)
        self.devise = "USD"

    # ...

class Franc(Monnaie):
    def __init__(self, montant):
        super().__init__(montant)
        self.devise = "CHF"

    # ...

# ...
```

{% enddetails %}

Afin de faire remonter l'attribut `devise` dans la classe `Monnaie`, il va falloir ajouter la devise en paramètre du constructeur.

Pour que cela se passe sans risque, on va commencer par juste ajouter le paramètre et voir ce que ça donne :

*"monnaie.py"* :

```python
# ...

class Monnaie:
    def __init__(self, montant, devise):
        self.montant = montant

    # ...

# ...
```

Et les tests plantent :

```text

    def __init__(self, montant):
>       super().__init__(montant)
E       TypeError: __init__() missing 1 required positional argument: 'devise'

monnaie.py:19: TypeError
```

On a oublié de modifier l'appel au constructeur dans les constructeur des classes. 

> Ajouter devise dans l'appel au `super` du constructeur des classes `Franc` et `Dollar`
{: .a-faire}
{% details solution %}

*"monnaie.py"* :

```python
# ...

class Dollar(Monnaie):
    def __init__(self, montant, "USD"):
        super().__init__(montant)
        self.devise = "USD"

    # ...

class Franc(Monnaie):
    def __init__(self, montant, "CHF"):
        super().__init__(montant)
        self.devise = "CHF"

    # ...

# ...
```

{% enddetails %}

Et nos tests passent ! On est sur du vert, c'est bien. On peut finir notre refactoring pattern :

> Faite remonter l'attribut `devise` dans `Monnaie`
{: .a-faire}
{% details solution %}

*"monnaie.py"* :

```python
# ...

class Monnaie:
    def __init__(self, montant, devise):
        self.montant = montant
        self.devise = devise

    # ...

class Dollar(Monnaie):
    def __init__(self, montant, "USD"):
        super().__init__(montant)

    # ...

class Franc(Monnaie):
    def __init__(self, montant, "CHF"):
        super().__init__(montant)

    # ...

# ...
```

{% enddetails %}

Et nos tests passent ! Félicitations, vous avez réussi votre premier refactoring pattern.

### faire {#faire-10.3}

Pour supprimer les classes, il faut créer nos objets avec la classe `Monnaie`. Notre problème est encore un problème de refactoring :

> **refactoring pattern :** [Pull Up Method](https://refactoring.guru/fr/pull-up-method)
>
> Le but est de faire remonter une méthode de sous-classes à la classe mère.
>
> Pour cela, on rend **identique** la méthode dans chacune des sous-classes puis on le déplace dans la classe mère.
{: .note}

Puisque si les constructeurs sont identique, on pourra facilement créer nos objets avec `Monnaie` plutôt qu'avec `Franc` ou `Dollar`. C'est encore impossible pour l'instant car les constructeurs sont :

* `__init__(self, montant)` pour `Franc` et `Dollar`
* `def __init__(self, montant, devise)` pour `Devise`

On va petit à petit modifier les constructeurs (et les effets de bords dans le code) pour les rendre identique.

> Ajoutez un champ devise au constructeur de `Franc` et lancez les tests.
{: .a-faire}
{% details solution %}
*"monnaie.py"* :

```python
# ...

class Franc(Monnaie):
    def __init__(self, montant, devise):
        super().__init__(montant, "CHF")

    # ...

# ...
```

{% enddetails %}

Les tests donnent :

```test
    def franc(montant):
>       return Franc(montant)
E       TypeError: __init__() missing 1 required positional argument: 'devise'

monnaie.py:6: TypeError
```

C'est le factory.

> Modifiez le factory pour qu'il corresponde au constructeur. On donnera `None` comme paramètre pour devise.
{: .a-faire}
{% details solution %}

*"monnaie.py"* :

```python
# ...

def franc(montant):
    return Franc(montant, None)

# ...
```

{% enddetails %}

> On met `None` comme paramètre car comme sa valeur n'est pas utile pour l'instant autant ne pas s'en occuper.

Les tests ratent toujours :

```text
    def __mul__(self, multiplicateur):
>       return Franc(self.montant * multiplicateur)
E       TypeError: __init__() missing 1 required positional argument: 'devise'

monnaie.py:31: TypeError
```

Ah, c'est inattendu... On avait oublié `__mul__`: elle n'utilise pas le factory pour créer ses objets.

> Modifiez la méthode `__mul__` de `Franc` pour qu'elle utilise le factory.
{: .a-faire}
{% details solution %}

*"monnaie.py"* :

```python
# ...

class Franc(Monnaie):
    # ...

    def __mul__(self, multiplicateur):
        return franc(self.montant * multiplicateur)

# ...
```

{% enddetails %}

Et nos tests passent !

> Faites la même chose pour `Dollar` en ajoutant un champ devise au constructeur.
>
> Faites en sorte que les tests passent.
{: .a-faire}
{% details solution %}

*"monnaie.py"* :

```python
# ...

def dollar(montant):
    return Dollar(montant, None)

# ...

class Dollar(Monnaie):
    def __init__(self, montant, devise):
        super().__init__(montant, "USD")

    def __mul__(self, multiplicateur):
        return dollar(self.montant * multiplicateur)

# ...
```

{% enddetails %}

### faire {#faire-10.4}

Maintenant que les signatures des constructeurs sont les mêmes, pour finir le travail il faut que le corps des fonctions soient égales.

> Le second paramètre du constructeur de `Franc` est pour l'instant inutile. Rendez le utile en utilisant son factory (la chaine `"CHF"` doit aller du factory au constructeur)
{: .a-faire}
{% details solution %}
*"monnaie.py"* :

```python
# ...

def franc(montant):
    return Franc(montant, "CHF")

# ...

class Franc(Monnaie):
    def __init__(self, montant, devise):
        super().__init__(montant, devise)

    def __mul__(self, multiplicateur):
        return franc(self.montant * multiplicateur)

# ...
```

{% enddetails %}

Les tests passent, on peut donc faire pareil avec `Dollar` :

> Le second paramètre du constructeur de `Dollar` est pour l'instant inutile. Rendez le utile en utilisant son factory (la chaine `"USD"` doit aller du factory au constructeur)
{: .a-faire}
{% details solution %}
*"monnaie.py"* :

```python
# ...

def dollar(montant):
    return Dollar(montant, "USD")

# ...

class Dollar(Monnaie):
    def __init__(self, montant, devise):
        super().__init__(montant, devise)

    def __mul__(self, multiplicateur):
        return dollar(self.montant * multiplicateur)

# ...
```

{% enddetails %}

Tout est enfin prêt : nos constructeurs sont identiques.

> Supprimez les constructeurs des classes `Dollar` et `Franc`
{: .a-faire}
{% details solution %}
*"monnaie.py"* :

```python
# ...

class Dollar(Monnaie):
    def __mul__(self, multiplicateur):
        return dollar(self.montant * multiplicateur)


class Franc(Monnaie):
    def __mul__(self, multiplicateur):
        return franc(self.montant * multiplicateur)

# ...
```

{% enddetails %}

Les testes passent : tout est prêt pour maintenant supprimer les sous-classes.

### todo list {#todo-list-10.2}

Il reste des duplications entre Franc et Dollar, mais pour les supprimer il faut passer par quelque chose qui les remplace. Il est donc plus judicieux de faire un autre item de notre liste.

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`
* [X] 5 CHF * 2 = 10CHF
* [ ] duplication Franc/dollar
* [X] même `==` (code identique dans 2 classes différentes)
* [ ] `*` presque identique
* [X] compare Franc et Dollar
* [X] utilisation de devises plutôt que de classes ?
* [ ] supprimer les tests de `Franc` ?

### 11 -  unification de `*`

Tout est prêt pour unifier les `__mul__` et ainsi faire disparaitre les dernières différences entre les 2 classes.

### todo list {#todo-list-11.1}

Il reste des duplications entre Franc et Dollar, mais pour les supprimer il faut passer par quelque chose qui les remplace. Il est donc plus judicieux de faire un autre item de notre liste.

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`
* [X] 5 CHF * 2 = 10CHF
* [ ] duplication Franc/dollar
* [X] même `==` (code identique dans 2 classes différentes)
* **[-] `*` presque identique**
* [X] compare Franc et Dollar
* [X] utilisation de devises plutôt que de classes ?
* [ ] supprimer les tests de `Franc` ?

### faire {#faire-11.1}

Les deux `__mul__` ne changent que par le factory utilisé.

> Remplacez le factory du retour de la méthode par un appel explicite à la classe.
{: .a-faire}
{% details solution %}
*"monnaie.py"* :

```python
# ...

class Dollar(Monnaie):
    def __mul__(self, multiplicateur):
        return Dollar(self.montant * multiplicateur, "USD)


class Franc(Monnaie):
    def __mul__(self, multiplicateur):
        return Franc(self.montant * multiplicateur; "CHF)

# ...
```

{% enddetails %}

les tests sont toujours Ok. Parfait.

On peut maintenant ajouter une méthode `__mul__` dans la classe money :

> Ajoutez une méthode `__mul__` dans `Monnaie`
{: .a-faire}
{% details solution %}
*"monnaie.py"* :

```python
# ...

class Monnaie:
    def __init__(self, montant, devise):
        self.montant = montant
        self.devise = devise

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.montant == other.montant

    def __mul__(self, multiplicateur):
        return Monnaie(self.montant * multiplicateur, self.devise)

# ...
```

{% enddetails %}

On va maintenant supprimer les méthodes `__mul__` des classes filles pour utiliser celle de `Monnaie`.

> Supprimez la méthode `__mul__` de la classe `Franc` et lancez les tests.
{: .a-faire}
{% details solution %}
*"monnaie.py"* :

```python
# ...

class Franc(Monnaie):
    pass

# ...
```

{% enddetails %}

Les tests ratent.

Et oui, on le savait quand on l'a fait que ça allait nous sauter à la figure : c'est le `__eq__` et sa comparaison entre classes.

En TDD il est **interdit** de modifier du code alors qu'on est rouge. On revient donc en arrière :

> Replacez la méthode `__mul__` dans `Franc` et assurez vous que les tests passent.
{: .a-faire}
{% details solution %}
*"monnaie.py"* :

```python
# ...

class Franc(Monnaie):
    def __mul__(self, multiplicateur):
        return Franc(self.montant * multiplicateur, "CHF")

# ...
```

{% enddetails %}

Maintenant qu'on est sur du vert, on peut modifier du code :

> Modifiez `__eq__` de `Monnaie` pour qu'il utilise l'attribut `devise` plutôt que la classe
{: .a-faire}
{% details solution %}
*"monnaie.py"* :

```python
# ...

class Monnaie:
    # ...

    def __eq__(self, other):
        return self.devise == other.devise and self.montant == other.montant

    # ...

# ...
```

{% enddetails %}

Les tests repassent ! On peut retenter la suppression de `__mul__` :

> Supprimez la méthode `__mul__` dans `Franc` et assurez vous que les tests passent.
{: .a-faire}
{% details solution %}
*"monnaie.py"* :

```python
# ...

class Franc(Monnaie):
    pass

# ...
```

{% enddetails %}

**victoire !** Nos tests passent.

On procède de même avec `Dollar` :

> Supprimez la méthode `__mul__` dans `Dollar` et assurez vous que les tests passent.
{: .a-faire}
{% details solution %}
*"monnaie.py"* :

```python
# ...

class Dollar(Monnaie):
    pass

# ...
```

{% enddetails %}

Jusqu'à présent tout va bien. On est toujours vert.

### todo list {#todo-list-11.2}

On a fini un item (`__mul__`) et on peut directement enchaîner sur le suivant :

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`
* [X] 5 CHF * 2 = 10CHF
* **[-] duplication Franc/dollar**
* [X] même `==` (code identique dans 2 classes différentes)
* [X] `*` presque identique
* [X] compare Franc et Dollar
* [X] utilisation de devises plutôt que de classes ?
* [ ] supprimer les tests de `Franc` ?

### faire {#faire-11.2}

On se sent en confiance.

> Utilisez le constructeur de `Monnaie`  pour les deux factory.
{: .a-faire}
{% details solution %}
*"monnaie.py"* :

```python
# ...

def dollar(montant):
    return Monnaie(montant, "USD")


def franc(montant):
    return Monnaie(montant, "CHF")

# ...
```

{% enddetails %}

Et enfin :

> Supprimez les classes `Dollar` et `Franc`
{: .a-faire}

### todo list {#todo-list-11.3}

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`
* [X] 5 CHF * 2 = 10CHF
* [X] duplication Franc/dollar
* [X] même `==` (code identique dans 2 classes différentes)
* [X] `*` presque identique
* [X] compare Franc et Dollar
* [X] utilisation de devises plutôt que de classes ?
* [ ] supprimer les tests de `Franc` ?

## Fin de Partie

Maintenant les tests d'égalité et de multiplication des `Franc` sont vraiment inutiles puisque le code est le même que celui de dollar :

> Suprimez les tests de concernant les francs.
{: .a-faire}
{% details solution %}
*"test_monnaie.py"* :

```python
import monnaie


def test_multiplication():
    cinq = monnaie.dollar(5)

    assert monnaie.dollar(10) == cinq * 2
    assert monnaie.dollar(15) == cinq * 3


def test_egalite():
    assert monnaie.dollar(5) == monnaie.dollar(5)


def test_non_egalite_dollar():
    assert monnaie.dollar(5) != monnaie.dollar(6)


def test_franc_dollar():
    assert monnaie.franc(1) != monnaie.dollar(1)


def test_devise():
    assert "USD" == monnaie.dollar(1).devise
    assert "CHF" == monnaie.franc(1).devise

```

{% enddetails %}

### todo list {#todo-list-fin}

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`
* [X] 5 CHF * 2 = 10CHF
* [X] duplication Franc/dollar
* [X] même `==` (code identique dans 2 classes différentes)
* [X] `*` presque identique
* [X] compare Franc et Dollar
* [X] utilisation de devises plutôt que de classes ?
* [X] supprimer les tests de `Franc` ?

## bilan

Vous voyez le développement organique en TDD. On a commencé par deux classes distinctes, puis en codant, on s'est rendu compte qu'elles étaient inutiles et on les a petit à petit supprimées.

Si vous aviez codés sans tests, cela aurait été impossible de réaliser cette opérations en un temps aussi court. De plus, vous n'auriez pas été tenté de le faire car les conséquences auraient pu être dramatique en effet de bord sur le code.

### élagage de la todo list

En supprimant les items effectués, il nous reste à faire ;

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [ ] `== None`
* [ ] `==` avec autre chose qu'un `Dollar`

### code

#### *"test_monnaie.py"*

```python
import monnaie


def test_multiplication():
    cinq = monnaie.dollar(5)

    assert monnaie.dollar(10) == cinq * 2
    assert monnaie.dollar(15) == cinq * 3


def test_egalite():
    assert monnaie.dollar(5) == monnaie.dollar(5)


def test_non_egalite_dollar():
    assert monnaie.dollar(5) != monnaie.dollar(6)


def test_franc_dollar():
    assert monnaie.franc(1) != monnaie.dollar(1)


def test_devise():
    assert "USD" == monnaie.dollar(1).devise
    assert "CHF" == monnaie.franc(1).devise

```

#### *"monnaie.py"*

```python
def dollar(montant):
    return Monnaie(montant, "USD")


def franc(montant):
    return Monnaie(montant, "CHF")


class Monnaie:
    def __init__(self, montant, devise):
        self.montant = montant
        self.devise = devise

    def __eq__(self, other):
        return self.devise == other.devise and self.montant == other.montant

    def __mul__(self, multiplicateur):
        return Monnaie(self.montant * multiplicateur, self.devise)

```
