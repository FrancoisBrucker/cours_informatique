---
layout: page
title:  "TDD et test pattern : partie 1/3"
author: "François Brucker"
---

Partie 1/3.

<!--more-->

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [code]({% link cours/algorithme-code-theorie/code/index.md %}) / [programmation objet]({% link cours/algorithme-code-theorie/code/programmation-objet/index.md %}) / [projet : TDD]({% link cours/algorithme-code-theorie/code/programmation-objet/projet-tdd.md %}) / [partie 1/3]({% link cours/algorithme-code-theorie/code/programmation-objet/projet-tdd-1.md %})
>
> **prérequis :**
>
> * [projet : TDD]({% link cours/algorithme-code-theorie/code/programmation-objet/projet-tdd.md %})
>
{: .chemin}

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
> 2. On a besoin que d'un unique fichier pour l'instant : *"test_monnaie.py"*.
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

> codons un test qui  valide cette item dans le fichier *"test_monnaie.py"*
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
» python -m pytest test_monnaie.py
======================== test session starts =========================
platform darwin -- Python 3.9.9, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /projet-tdd
plugins: dash-1.19.0, cov-3.0.0
collected 0 items / 1 error

============================== ERRORS ================================
__________________ ERROR collecting test_monnaie.py ___________________
ImportError while importing test module '/projet-tdd/test_monnaie.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/python3.9/importlib/__init__.py:127: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
test_monnaie.py:1: in <module>
    from money import Dollar
E   ModuleNotFoundError: No module named 'monnaie'
====================== short test summary info =======================
ERROR test_monnaie.py
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
» python -m pytest test_monnaie.py
======================== test session starts =========================
platform darwin -- Python 3.9.9, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /projet-tdd
plugins: dash-1.19.0, cov-3.0.0
collected 1 item
test_monnaie.py .

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

> **premier pattern du TDD :**
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

Pour vérifier que nos 5 dollaors restent 5 dollars, on peut faire un test du style :

```python
from money import Dollar

def test_multiplication():
    cinq = Dollar(5)
    cinq.fois(2)
        
    assert 10 == cinq.montant

    cinq.fois(3)
        
    assert 15 == cinq.montant
```

> On execute nos tests et — comme attendu — ça rate.
{: .a-faire}

Ce test n'est cependant pas vraiment satisfaisant pour au moins deux raisons :

1. cela semble un peut compliqué de changer montant tout en gardant 5 quelque-part
2. le code est vraiment étrange. Comment `cinq` pourrait-il valloir 15 ?

La seconde raison est de loin la plus importante. Notre code est étrange et peu lisible (bref, *ça ne sent pas bon*). C'est souvent le signe qu'il se passe quelque chose de mal.

> Le **[code smell](https://en.wikipedia.org/wiki/Code_smell)** est la capacité qu'à un bon développeur de reconnaître un soucis profond juste en lisant l'organisation ou l'utilisation d'un code.
>
> Le code smell s'acquiert avec le temps, mais vous pouvez acccélérer son accisition en lisant du obon code
{: .note}

Une façon simple et élégante de régler notre soucis est d'utiliser des objet qui ne peuvent être modifiés.

> Un objet non modifiable est appelé [**value object**](https://martinfowler.com/bliki/ValueObject.html).
{: .note}

C'est super chouette d'avoir des objets non modifiable, on a pas besoin de faire attention à eux : une fois créés ils ne bougent plus.

Ceci nous permet de les donner à des méthodes inconnues sans avoir peur qu'ils soient modifiés, ou les utiliser dans nos propres méthodes sans craindre qu'ils soient modifiés plus tard. Le seul point négatif d'un value object est que l'on doit regcréer un nouvel objet si on veut le changer. Heureusement, dans la plupart du temps ce n'est pas très coûteux.

> En python, de nombreux objet sont des values objcet. On peut citer les chaines de caractères, les entiers, les réels ou encore le booleens.
>
> De plus, de nombreuses stuctures modifiables ont leurs contrepartie non modifiables. Par exemple les [tuples](https://docs.python.org/fr/3/library/stdtypes.html) pour les listes ou les [frozenset](https://docs.python.org/fr/3/library/stdtypes.html) pour les ensembles.

Pour un *value object*, à la place de modifier un objet il faut en rendre un nouveau on en rende un nouveau : la méthode `fois` doit rendre un objet. Modifions notre test  :

*"test_monnaie.py"* :

```python
from monnaie import Dollar


def test_multiplication():
    cinq = Dollar(5)
    dix = cinq.fois(2)

    assert 10 == dix.montant

    quinze = cinq.fois(3)

    assert 15 == quinze.montant

```

Le test est bien plus joli : il est lisible et compréhensible. Bon bien sur, ce n'est que le début :

> On execute nos tests et — comme attendu — ça rate.
{: .a-faire}

Ce coup ci, pas besoin de grandes manipulations pour faire passer le test. Il faut que la méthode *fois* rende un objet `Dollar`. Si l'implémentation semble évidente, autant la coder de suite (mais après le test !).  On vient de découvrir une autre règle :

> **Second pattern du TDD :** l'implémentation directe du test est appelée : **obvious implementation**.
{: .note}

> Faite une implémentation de la méthode `fois`
{: .a-faire}

{% details solution %}
*"monnaie.py"* :

```python
class Dollar:
    def __init__(self, montant):
        self.montant = montant

    def fois(self, multiplicateur):
        return Dollar(self.montant * multiplicateur)
```

{% enddetails %}

> On execute nos tests et ça passe !
{: .a-faire}

On a en même temps fait passer le test et fini l'implémentation.

### todo list {#todo-list-2.2}

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [X] \\$5 * 2 = \\$10
* [ ] utiliser `montant` ? Le rendre privé (le cacher à l'utilisateur (ici les tests))
* [X] `cinq == $10` (ce n'est pas vraiment super car nos \\$5 initiaux valent maintenant \\$10). rendre `Dollar` non modifiable
* [ ] gestion des arrondis (lorsque les montants seront des réels)

## 3 - `==`

Pour vérifier que deux objets sont égaux, on ne va pas passer son temps à vérifier que tous leurs attributs soient les mêmes. On va le faire une fois pour toute (ce qui évitera en plus les duplications). On le rajoute donc dans la todo liste :

### todo list {#todo-list-3.1}

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [X] \\$5 * 2 = \\$10
* [ ] utiliser `montant` ? Le rendre privé (le cacher à l'utilisateur (ici les tests))
* [X] `cinq == $10` (ce n'est pas vraiment super car nos \\$5 initiaux valent maintenant \\$10). rendre `Dollar` non modifiable
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* **[-] `==`**

### faire {#faire-3.1}

On va utiliser pour cela des méthodes spéciales de python qui permettent d'utiliser les opérateurs `==` et `!=` même si ce n'est pas pour comparer des entiers. Mais avant d'aller plus loin, les tests.

*"test_monnaie.py"* :

```python
# ...

def test_egalite():
    assert Dollar(5) == Dollar(5)

# ...
```

> On lance les tests.
{: .a-faire}

Bien sur, le test rate. Par défaut, lorsque l'on a pas défini de méthode `__eq__`, l'opérateur `==` regarde si ce sont les mêmes objets, ce qui n'est pas le cas.

L'implémentation n'étant pas forcément évidente :

> Commençons par faire marcher le test en utilisant la techique *fake it* :
{: .a-faire}
{% details solution %}
*"monnaie.py"* :

```python
class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)
        
    def __eq__(self, other):
        return True
```

{% enddetails %}

Avec ce code lorsque l'on écrit `x == y`, python le re-écrit en : `x.__eq__(y)`. Du coup notre *fake it* fait passer le test.

Maintenant, les choses sérieuses : on supprime les duplications. On suppose que l'on ne sait pas résoudre le problème. Pour trouver une solution, on utilise le dernier pattern du TDD :

> **Troisième pattern du TDD :** pour supprimer ds duplications non évidente on utilise la **triangulation**
{:.note}

Pour utiliser la triangulation, on écrit deux tests différents pour le même problème : si le test est différent du premier, pour que les deux testent passent en même temps, il faudra supprimer des duplications.

On ajoute alors autant de tests que nécessaire jusqu'à ce que toutes les duplications aient disparues. Les tests que l'on rajoute dépendent donc des duplications que l'on a.

Dans notre cas, on répond toujours `True`, on va donc forger un test qui doit répondre `False`.

> Créez un test qui répond `False` à l'égalité
{: .a-faire}

{% details solution %}

*"test_monnaie.py"* :

```python
# ...

def test_egalite():
    assert Dollar(5) == Dollar(5)


def test_non_egalite():
    assert Dollar(5) != Dollar(6)

# ...
```

{% enddetails %}

> On lance les tests et maintenant un teste rate.
{: .a-faire}

La duplication est dans le montant de l'objet.

> Supprimez la duplication de la méthode `__eq__`.
{: .a-faire}

{% details solution %}
*"monnaie.py"* :

```python
class Dollar:
    # ...
    def __eq__(self, other):
        return self.montant == other.montant
```

{% enddetails %}
> On peut mainteannt re-exécuter le test, qui passe.
{: .a-faire}

Ce traitement de l'égalité est frustre, on ne vérifie pas :

* si l'objet `other` a la propriété `montant`
* voir même si l'objet existe (`cinq == None` va planter plutôt que de répondre `False`)

On va pas s'embêter avec ça pour l'instant, mais on va tout de même le rajouter à notre todo list.

### todo list {#todo-list-3.2}

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [X] \\$5 * 2 = \\$10
* [ ] utiliser `montant` ? Le rendre privé (le cacher à l'utilisateur (ici les tests))
* [X] `cinq == $10` (ce n'est pas vraiment super car nos \\$5 initiaux valent maintenant \\$10). rendre `Dollar` non modifiable
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [X] `==`
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`

## 4 - `__mul__`

La méthode `__eq__` n'est pas la seule utilisée en python pour donner des comportement spéciaux au objets (il en [existe beaucop d'autres](https://micropyramid.com/blog/python-special-class-methods-or-magic-methods/). Notre objet `Dollar` devant se comporter plus ou moins comme un nombre, on peut implémenter les [méthodes spéciales utiles pour ressembler à des nombres](https://diveintopython3.net/special-method-names.html#acts-like-number).

Comencçons par implémenter [`__mul__`](https://docs.python.org/3/library/operator.html#operator.__mul__).

### todo list {#todo-list-4.1}

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [X] \\$5 * 2 = \\$10
* [ ] utiliser `montant` ? Le rendre privé (le cacher à l'utilisateur (ici les tests))
* [X] `cinq == $10` (ce n'est pas vraiment super car nos \\$5 initiaux valent maintenant \\$10). rendre `Dollar` non modifiable
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [X] `==`
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`
* **[-] `__mul__`**

### faire {#faire-4.1}

Pour le test, il suffit de modifier le test de la multiplication :

*"test_monnaie.py"* :

```python
# ...

def test_multiplication():
    cinq = Dollar(5)
    dix = cinq * 2

    assert 10 == dix.montant

    quinze = cinq * 3

    assert 15 == quinze.montant

# ...
```

> En faire une *obvious implementation* :
{: .a-faire}

{% details solution %}
*"monnaie.py"* :

```python
class Dollar:
    def __init__(self, montant):
        self.montant = montant

    def __mul__(self, multiplicateur):
        return Dollar(self.montant * multiplicateur)

    def __eq__(self, other):
        return self.montant == other.montant

```

{% enddetails %}

### todo list {#todo-list-4.2}

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [X] \\$5 * 2 = \\$10
* [ ] utiliser `montant` ? Le rendre privé (le cacher à l'utilisateur (ici les tests))
* [X] `cinq == $10` (ce n'est pas vraiment super car nos \\$5 initiaux valent maintenant \\$10). rendre `Dollar` non modifiable
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [X] `==`
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`
* [X] `__mul__`

## 5 - privacy

Tput est prêt pour travailler sur l'attribut `montant`.

### todo list {#todo-list-5.1}

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [X] \\$5 * 2 = \\$10
* **[-] utiliser `montant` ? Le rendre privé (le cacher à l'utilisateur (ici les tests))**
* [X] `cinq == $10` (ce n'est pas vraiment super car nos \\$5 initiaux valent maintenant \\$10). rendre `Dollar` non modifiable
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [X] `==`
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`
* [X] `__mul__`

### faire {#faire-5.1}

Il ne manque pas grand chose pour que `montant` soit privé. Il suffit de ne pas en parler dans les tests et de ne comparer que des objets entres eux :

*"test_monnaie.py"* :

```python
# ...

def test_multiplication():
    cinq = Dollar(5)

    dix = cinq * 2
    assert Dollar(10) == dix

    quinze = cinq * 3
    assert Dollar(15) == quinze

#... 
```

On peut même encore faire plus joli :

```python
# ...

def test_multiplication():
    cinq = Dollar(5)

    assert Dollar(10) == cinq * 2
    assert Dollar(15) == cinq * 3

#... 
```

Notez que l'on a utilisé une fonctionnalité que l'on vient de créer (`__mul__`) pour améliorer un test. C'est normal les tests et le code forment une seule entité.

> Maintenant si 2 tests plantent en même temps (si le `==` commence à rater par exemple), il faudra se rappeler quel est le test qui plante et les tests qui ne fonctionnent plus.
>
> Ceci arrive inévitablement.
{: .attention}

On fait petit à petit disparaitre des tests les références explicites à l'implémentation des classes. C'est une bonne pratique.

> **Test pattern :** Lorsque l'on teste, il est important de toujours tester du point de vue de l'utilisation. Il faut éviter le plus possible de tester des attebiuts internes à la classe.
{: .note}

### todo list {#todo-list-5.2}

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [X] \\$5 * 2 = \\$10
* [X] utiliser `montant` ? Le rendre privé (le cacher à l'utilisateur (ici les tests))
* [X] `cinq == $10` (ce n'est pas vraiment super car nos \\$5 initiaux valent maintenant \\$10). rendre `Dollar` non modifiable
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [X] `==`
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`
* [X] `__mul__`

## Fin de la partie 1

### todo list {#todo-list-fin-1}

On peut épurer notre todo-list en supprimant les items déjà résolus. On obtient :

* [ ] \\$5 + 2.5CHF = \\$10 si le taux de change est 1:.5
* [ ] gestion des arrondis (lorsque les montants seront des réels)
* [ ] `== None`
* [ ] `==`avec autre chose qu'un `Dollar`

### code {#code-fin-1}

A la fin de cette partie, on a 2 fichiers.

#### *"monnaie.py"*

```python
class Dollar:
    def __init__(self, montant):
        self.montant = montant

    def __mul__(self, multiplicateur):
        return Dollar(self.montant * multiplicateur)

    def __eq__(self, other):
        return self.montant == other.montant

```

#### *"test_monnaie.py"*

```python
from monnaie import Dollar


def test_multiplication():
    cinq = Dollar(5)

    assert Dollar(10) == cinq * 2
    assert Dollar(15) == cinq * 3


def test_egalite():
    assert Dollar(5) == Dollar(5)


def test_non_egalite():
    assert Dollar(5) != Dollar(6)

```
