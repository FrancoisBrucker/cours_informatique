---
layout: page
title:  "TDD et test pattern"
author: "François Brucker"
---

Nous allons dans cette séance suivre ici le livre [TDD by example](https://www.amazon.fr/Test-Driven-Development-Kent-Beck/dp/0321146530/ref=sr_1_1?ie=UTF8&qid=1538720480&sr=8-1&keywords=test+driven+development+by+example) de Kent Beck (Suivez son [twitter](https://twitter.com/kentbeck), ses posts sont souvent rigolos et toujours utiles).

Initialement écrit pour le java, nous allons appliquer ses enseignements au python.

<!--more-->

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [code]({% link cours/algorithme-code-theorie/code/index.md %}) / [programmation objet]({% link cours/algorithme-code-theorie/code/programmation-objet/index.md %}) / [projet : TDD]({% link cours/algorithme-code-theorie/code/programmation-objet/projet-tdd.md %})
>
> **prérequis :**
>
> * [projet : héritage]({% link cours/algorithme-code-theorie/code/programmation-objet/projet-heritage.md %})
>
{: .chemin}

## But

En suivant le déroulé du livre [TDD by example](https://www.amazon.fr/Test-Driven-Development-Kent-Beck/dp/0321146530/ref=sr_1_1?ie=UTF8&qid=1538720480&sr=8-1&keywords=test+driven+development+by+example), vous allez apprendre à écrire du code par les tests.
Vous allez y apprendre le [nindo](https://naruto.fandom.com/fr/wiki/Nind%C3%B4) de la proatique d'un bon code :

> Créer du code **propre** qui **fonctionne**
>
> (*clean code that works* en version originale)
{: .note}

Outre la méthode, nous verrons également quelques tehcniques pour y arriver de façon claire et pratique, comme des règles de refactoring (issues de [Refactoring: Improving the Design of Existing Code](https://www.amazon.fr/Refactoring-Improving-Design-Existing-Code/dp/0201485672/ref=sr_1_2?ie=UTF8&qid=1539066441&sr=8-2) de [Martin fowler](https://martinfowler.com) (allez voir son site, y'a moult choses chouettes sur le code, l'agile, la vie et le reste)).

Ceci devrait vous permettre de diminuer le nombre de WTFs/minute, qui est le meilleur indicateur au monde d'un bon code (issu du livre [clean code](https://www.amazon.fr/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882) de [Robert C. Martin](https://fr.wikipedia.org/wiki/Robert_C._Martin). Ce n'est pas un livre pour débutant mais si vous avez déjà compris le tdd, c'est un super pour finaliser votre compréhension) :

![WTFs/minute](./assets/wtfm.jpg){:style="margin: auto;display: block"}

> Faites l'effort de suivre cette séance en codant **en même temps** le projet. Tout est donné mais le voir fonctionner pour de vrai est plus impressionnant que de juste le lire.
{: .note}

On va exécuter les tests un gazillion de fois. Pour eviter la luxation de l'index il faut retenir les raccourcis claviers qui vont vous permettre de lancer les tests sans problème :

* dédiez un terminal pour cela. Une fois la commande tapée, il vous suffit de faire *flèche du haut* pour revenir à la commande précédente et l'exécuter
* lorsque vos tests passent, il est intéressant d'utiliser le raccourci clavier de votre éditeur pour exécuter tous les tests (sous [vscode](https://docs.microsoft.com/fr-fr/visualstudio/ide/default-keyboard-shortcuts-in-visual-studio?view=vs-2022#bkmk_test-global-shortcuts)).

## Projet

Vous allez créer dans cette séance une application de change entre Franc suisse (CHF) et dollars US ($).

|qui     |combien| prix   | total       |
|--------|-------|--------|-------------|
| Apple  | 1000  | $200   | $200 000    |
| Nestlé | 400   | 80 CHF |  32 000 CHF |
|||           **total**   | $248 000    |

Avec le taux de conversion : 1 CHF = $0.5

### Comment ?

En programmant par les tests bien sur !

On commence par une todo list qui regroupe tout ce que l'on pense faire pour l'instant. Cette liste va diminuer lorsque l'on avancera sur le projet et grossir lorsque notre connaissance du projet va s'affiner.

Nous n'utiliserons pas ici notre code. Mais il faudra tout faire *from scratch*. On aura donc besoin :

* d'une todo list où tous nos items à faire pour l'instant sont écrit : le *backlog*
* de fichiers de tests
* du code

On verra tout au long du cours divers patterns de test et de développement pour que tout aille pour le mieux. Notre but est ici de faire du :

> *clean code that works*
{: .note}

Pour cela on va se fixer quelques règles :

* on écrit du code que si un test rate
* on élimine les duplications

Ces 2 règles impliquent un mode de fonctionnement de note production code :

>
> 1. **rouge** :
>    * écrire *rapidement* un *petit* test
>    * lancer les tests et les voir planter, voir même  ne correspondre à aucun code.
> 2. **vert** :
>    * écrire le code *minimal* qui permet de faire passer le test
>    * lancer les tests et les voir tous réussir
> 3. **refactor** :
>    * élimine les duplications tout en conservant la validité des tests.
>
{: .note}

Cela permet de prendre du plaisir à coder :

* en écrivant du code dont est sûr qu'il ne cassera rien
* en voyant la todo list diminuer ce qui montre qu'on progresse
* comme tous les tests sont conservés on sait que l'on ne travaille pas pour rien

> Toutes ces règles visent à diminuer la peur qui bloque tout progrès
{: .note}

### Code

On va développer petit à petit notre propre application de change en utilisant le TDD. La logique est :

* chaque test couvre un petit ajout d'une fonctionnalité
* la première chose à faire sera de (rapidement et salement) faire fonctionner les tests
* toute les modifications de code sont effectuées alors que les testent passent
* le refactoring est fait par petites touches

## 1 - départ

### faire {#faire-1.1}

Commençons par noter ce qu'il faut faire pour que notre application de change fonctionne :

* il faut plusieurs devises (ici CHF et $)
* il faut multiplier les devises par des nombres (nb actions * prix)

Cette todo-list (ou *backlog*) nous indique :

1. **ce qu'il faut faire** : dès que on voit une tâche à faire qui n'est pas dans la todo list, on la rajoute,
2. **ce sur quoi on travaille** : on travaillera toujours sur **un unique** item à la fois
3. **ce que l'on a fait** : il n'y a rien de plus satisfaisant que de barrer une ligne que l'on vient de finir.

> 1. Créez un nouveau projet sous vscode dans un dossier que vos appellerez *"projet-tdd"*.
> 2. On a besoin que d'un unique fichier pour l'instant : *"test_change.py"*.
> 3. Prenez également une feuille de papier pour vos todos.
>
{: .a-faire}

### todo list {#todo-list-1.1}

Première todo-list :

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] \\$5 * 2 = \\$10

### faire {#faire-1.2}

Par quoi on commence ?

**PAR UN TEST !**

La bonne question n'est donc pas "que fait-on en premier" mais :

**Que teste-t-on en premier ?**

La deuxième ligne semble la plus simple. Donc allons-y, mettons en **gras** l'item de la todo list qu'on veut faire :

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* **[-] \\$5 * 2 = \\$10**

Puis :

> codons un test qui  valide cette item dans le fichier *"test_change.py"*
{: .a-faire}

```python
from monnaie import Dollar


def test_multiplication():
    cinq = Dollar(5)
    cinq.fois(2)
    
    assert 10 == cinq.montant
```

Nous n'avons pas encore écrit de classe `Dollar`, mais on l'utilise déjà...

> En TDD on utilise notre code avant de l'écrire. Avoir une idée de comment utiliser le code nous donne une idée de comment il doit fonctionner.
{: .note}

L'écriture de notre test (un cas d'utilisation de la classe dollar qui valide l'item courant de la todo-list) nous montre des choses que l'on doit pouvoir faire, et par là augmente notre todo-list avec des choses à implémenter ou des questions auxquelles il va falloir répondre un jour.

### todo list {#todo-list-1.2}

Le test nous pose quelques questions quand à l'utilisation dela classe dollar. Notre todo-list devient :

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* **[-] \\$5 * 2 = \\$10**
* [ ] utiliser `montant` ? Le rendre privé (le cacher à l'utilisateur (ici les tests))
* [ ] `cinq == $10` (ce n'est pas vraiment super car nos \\$5 initiaux valent maintenant \\$10). rendre `Dollar` non modifiable
* [ ] gestion des arrondis (lorsque les montants seront des réels)

### faire {#faire-1.3}

Rien ne marche avec nos tests lorsqu'on les exécute via le terminal :

```shell
» python -m pytest test_change.py
======================== test session starts =========================
platform darwin -- Python 3.9.9, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /projet-tdd
plugins: dash-1.19.0, cov-3.0.0
collected 0 items / 1 error

============================== ERRORS ================================
__________________ ERROR collecting test_change.py ___________________
ImportError while importing test module '/projet-tdd/test_change.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/python3.9/importlib/__init__.py:127: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
test_change.py:1: in <module>
    from money import Dollar
E   ModuleNotFoundError: No module named 'monnaie'
====================== short test summary info =======================
ERROR test_change.py
!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!
========================= 1 error in 0.13s ===========================
```

Ca en fait des erreurs !

Mais c'est une chance, car les messages d'erreurs vont nous permettre de faire un programme qui fonctionne. Il suffit de les supprimer une à une.

> Apprenez à **lire** les messages d'erreurs !
>
> Il est est souvent plus simple d'exécuter un code et de lire ce qui ne marche pas plutôt qe de réfléchir pour savoir si ça va fonctionner.
{: .note}

On va donc lire attentivement les messages d'erreurs de python et les régler petit à petit. Un message d'erreur **est informatif** si on se force à les lire.

Nos tests ratent à cause d'une erreur. On le voit à cette ligne :

```text
E   ModuleNotFoundError: No module named 'monnaie'
```

L'erreur est explicite :

> Créez un fichier *"monnaie.py"* vide dans le projet.
{: .a-faire}

On relance nos tests et maintenant l'erreur est :

```text
E   ImportError: cannot import name 'Dollar' from 'monnaie' (/projet-tdd/monnaie.py)
```

Encore une fois, l'erreur est explicite : il n'existe pas de module `monnaie`. Créons en un :

> Créez une classe `Dollar` vide dans le fichier *"monnaie.py"*.
{: .a-faire}

Pour créer une classe vide, il suffit de mettre une unique instruction `pass` (qui ne fait rien mais permet de ne pas faire d'erreur lorsque l'on crée un bloc sans instructions) :

```python
class Dollar:
    pass
```

On relance nos tests et maintenant l'erreur (toujours explicite) est :

```text
    def test_multiplication():
>       cinq = Dollar(5)
E       TypeError: Dollar() takes no arguments
```

Qu'à cela ne tienne, ajoutons un argument à la création de dollar :

> Ajoutez un argument à la création d'un objet de la classe `Dollar` :
>
> ```python
> class Dollar:
>   def __init__(self, montant):
>       pass
>
> ```
>
{: .a-faire}

On relance nos tests et maintenant :

```text
E       AttributeError: 'Dollar' object has no attribute 'fois'
```

On sait faire, on ajoute une méthode vide pour que cette erreur disparaisse :

> Ajoutez une méthode `fois` vide dans la classe `Dollar` :
>
> ```python
> class Dollar:
>     def __init__(self, montant):
>         pass
> 
>     def fois(self, multiplicateur):
>         pass
>
> ```
>
{: .a-faire}

On relance nos tests et... encore une erreur. Heureusement, comme toutes les autres elle est facile à résoudre :

```text
    def test_multiplication():
        cinq = Dollar(5)
        cinq.fois(2)
    
>       assert 10 == cinq.montant
E       AttributeError: 'Dollar' object has no attribute 'montant'
```

On voit de plus que `montant`doit être égal à 10, donc vite vite, on corrige cette erreur :

> Ajoutez un attribut `montant` qui vaut 10 à tout objet `Dollar` :
>
> ```python
> class Dollar:
>     def __init__(self, montant):
>         self.montant = 10
> 
>     def fois(self, multiplicateur):
>         pass
>
> ```
>
{: .a-faire}

On relance nos tests et...

```text
» python -m pytest test_change.py
======================== test session starts =========================
platform darwin -- Python 3.9.9, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /projet-tdd
plugins: dash-1.19.0, cov-3.0.0
collected 1 item
test_change.py .

========================== 1 passed in 0.01s =========================
```

 **Incroyable !** Nos tests passent (c'est émouvant).

> Corriger petit à petit un test pour qu'il passe ne nécessite presque pas d'intelligence. Il suffit de se laisser guider par l'interpréteur python.
{: .note}

### faire {#faire-1.4}

**Halte là !** Ce n'est pas fini.

Nos tests passent mais il reste un étape à faire : **refactor** : *supprimer les duplications*.

La première duplication évidente est le nombre `10` du test qui est dupliqué avec le `10` du `self.montant`. Comme on en a l'habitude maintenant, on va supprimer cette duplication petit à petit :

Après chaque modification, on s'assure que les tests passent : on ne modifie du code que si tout est vert. Ceci nous assure que l'on ne casse pas le programme.

Dans la classe `Dollar` :

```python
class Dollar:
    def __init__(self, montant):
        self.montant = 10

    # ...
```

Le `10` est en fait un `5 * 2` (On crée au départ $5).

On effectue la modification :

```python
class Dollar:
    def __init__(self, montant):
        self.montant = 5 * 2

    # ...
```

Et on lance nos tests pour vérifier que rien n'est cassé.

Le `5` qu'on vient de rajouter est aussi une duplication du test `cinq = Dollar(5)`. Modifions alors le code :

```python
class Dollar:
    def __init__(self, montant):
        self.montant = montant * 2

    # ...
```

Et on vérifie que les tests passent.

Le `2` est aussi une duplication, mais elle vient d'une autre ligne du test : `cinq.fois(2)`. COmençons donc pas déplacer notre 2 dans la méthode `fois`pour voir si c'est possible :

```python
class Dollar:
    def __init__(self, montant):
        self.montant = montant

    def fois(self, multiplicateur):
        self.montant *= 2

```

On lance nos tests... et... ça passe !

On peut supprimer le 2 dans le code de la classe `Dollar` et supprimer cette duplication :

```python
class Dollar:
    def __init__(self, montant):
        self.montant = montant

    def fois(self, multiplicateur):
        self.montant *= multiplicateur

```

Nos tests continuent de passer et nous n'avons plus de duplication: on peut supprimer la tâche de la todo-list

### todo list {#todo-list-1.3}

Le test nous pose quelques questions quand à l'utilisation dela classe dollar. Notre todo-list devient :

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [X] \\$5 * 2 = \\$10
* [ ] utiliser `montant` ? Le rendre privé (le cacher à l'utilisateur (ici les tests))
* [ ] `cinq == $10` (ce n'est pas vraiment super car nos \\$5 initiaux valent maintenant \\$10). rendre `Dollar` non modifiable
* [ ] gestion des arrondis (lorsque les montants seront des réels)

#### bilan {#bilan-1}

La procédure utilisée dans cette étape cera générale :

1. on crée un test
2. on éxécute nos tests et on voit que ça ne marche pas. Le test que l'on vient d'écrire est le seul test qui doit rater : **rouge**
3. on change le code pour que nos tests fonctionne. Le but est que le test passe donc on peut comêtre les pires attrocités pour cela (comme on a fait en mettant directement 10 à montant par exemple). Pour cela, la façon la plus simple est de se laisser guider par l'interpréteur.
4. Une fois que les tests passent, on est **vert**. A partir de là, on ne modifiera **jamais** de code si tout les tesrs ne passent pas
5. on supprime petit à petit les duplications tout en s'assurant que les tests sont toujours vert

La méthode qu'on a utilisé pour faire passer nos tests en duplicant la réponse du test dans le code à un nom :

> Dupliquer la réponse du test dans le code est la méthode appelée : **fake it**.
{: .note}

## 2 - value object

On veut faire du **clean code that works**. Mais c'est très difficile même pour des très bons codeurs. On va ainsi séparer le problème :

  1. on commence par le *that works*
  2. on fini par le *clean code*

> La règle d'un bon code est de procéder par ordre :
>
> 1. faire du code qui fonctionne
> 2. faire du code propre
> 3. faire du code rapide
>
> Il ne faut cependant pas s'arrêter à 1, sinon votre code ne sera pas maintenable dans le temps.
{: .note}

Que faire maintenant ?

### todo list {#todo-list-2.1}

On choisit **toujours** l'élément le plus simple à faire dans la todo-list. Ici, le quatrième item semble le facileemtn implémentable :

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [X] \\$5 * 2 = \\$10
* [ ] utiliser `montant` ? Le rendre privé (le cacher à l'utilisateur (ici les tests))
* **[-] `cinq == $10` (ce n'est pas vraiment super car nos \\$5 initiaux valent maintenant \\$10). rendre `Dollar` non modifiable**
* [ ] gestion des arrondis (lorsque les montants seront des réels)

### faire {#faire-2.1}

> Un objet non modifiable est appelé **value object**.
{: .note}

C'est super chouette d'avoir des objets non modifiable, on a pas besoin de faire attention à eux : une fois créés ils ne bougent plus.

Ceci nous permet de les donner à des méthodes inconnues sans avoir peur qu'ils soient modifiés, ou les utiliser dans nos propres méthodes sans craindre qu'ils soient modifiés plus tard. Le seul point négatif d'un value object est que l'on doit regcréer un nouvel objet si on veut le changer. Heureusement, dans la plupart du temps ce n'est pas très coûteux.

> ici
{: .tbd}

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
