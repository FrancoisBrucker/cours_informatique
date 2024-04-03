---
layout: layout/post.njk
title:  "Design Patterns"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Les [design patterns](https://fr.wikipedia.org/wiki/Patron_de_conception), ou façons de faire, sont pour ainsi dire de l'algorithmie objet : ils permettent de résoudre nombre de problèmes courants en développement et d'éviter les [erreurs classiques](http://sahandsaba.com/nine-anti-patterns-every-programmer-should-be-aware-of-with-examples.html), aussi appelées [anti-pattern](https://fr.wikipedia.org/wiki/Antipattern).
Il existe 3 grands types de design pattern, on pourra en donner un exemple pour chaque.

{% info %}
Le terme de *design pattern* a été initialement donné dans le livre [Design Patterns: Elements of Reusable Object-Oriented Software](https://en.wikipedia.org/wiki/Design_Patterns) pour le langage C++. 
{% endinfo %}

On classe habituellement les designs patterns en trois types : 

- [**les types creational**](https://en.wikipedia.org/wiki/Creational_pattern) qui créent des objets.
- [**les types structural**](https://en.wikipedia.org/wiki/Structural_pattern) qui mettent les objets en relation.
- [**les types behavioural**](https://en.wikipedia.org/wiki/Behavioral_pattern) qui regroupent les objets ayant même comportement.

Ils permettent de résoudre de façon efficace des problèmes courants en programmation. Il est utile de connaitre une liste actuelle de design patterns (certains de la liste originelle, comme [singleton](https://fr.wikipedia.org/wiki/Singleton_(patron_de_conception)) ne sont plus utilisés et d'autres, comme [MVP](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93presenter) sont apparus), car ils donnent souvent de bonnes idées pour résoudre les problèmes que l'on se pose. Le site suivant contient une liste actualisée de design patterns :

{% lien %}
[Refactoring GURU : design pattern](https://refactoring.guru/design-patterns)
{% endlien %}

Il existe aussi leurs doubles maléfiques, les anti-patterns, qui sont des solutions évidentes -- et mauvaises -- à des problèmes courants. Là aussi, il est bon de connaitre une liste actualisée d'anti-pattern, comme par exemple :


{% lien %}
[Quelques anti patterns](http://sahandsaba.com/nine-anti-patterns-every-programmer-should-be-aware-of-with-examples.html)
{% endlien %}


Nous allons, encore une fois, utiliser la classe `Dé`{.language-} et l'*améliorer* selon le problème posé.


## Les bases

> Un dé avec les faces initiales choisies + la position initiale.

On se rappelle comment bien commencer un projet, avec trois fichiers :

- le code
- les tests
- le programme

On commence avec les 3 fichiers ci-après. Exécutez le main et les tests. Les 3 tests doivent passer.

Fichier `main.py`{.fichier} :

```python
from choice import Choice

d6 = Choice(list(range(1, 7)))

for etape in range(100):
    print(d6.roll().get_position())
```

Fichier `choices.py`{.fichier} :

```python
import random


class Choice:
    def __init__(self, choices):
        self.choices = choices
        self.position = choices[0]

    def get_position(self):
        return self.position

    def roll(self):
        self.position = self.choices[random.randrange(len(self.choices))]
        return self
```

{% faire %}
Regardez le code de la méthode `roll` pourquoi rendre `self` ?
{% endfaire %}
{% details solution %}
Pour vouvoir chainer nos opérations. En rendant self, on peut écrire des choses du genre :

```python
choice = Choices([1, 2, 3, 4])

print(choice.roll().get_position())
```

{% enddetails %}

Fichier `tests.py`{.fichier} :

```python
from choice import Choice


def test_init():
    d1 = Choice([1])
    assert d1.choices == [1]


def test_initial_position():
    d1 = Choice([1, 2])
    assert d1.get_position() == 1


def test_roll():
    d1 = Choice([1])
    d1.roll()
    assert d1.get_position() == 1
```

## Première amélioration

Choice prend l'objet `choices` et le garde. Cela pose plusieurs problèmes. En particulier :

* si on modifie l'objet passé en paramètre, cela change le comportement de choice.
* on expose l'attribut `choices` par un attribut public.

Pour résoudre ces soucis on va copier l'objet `choices` et rendre l'attribut non modifiable. Pour cela, on va écrire des tests pour mettre en  lumière le problème puis corriger le code. Il faudra certainement changer d'autres tests dans le processus de réécriture du code.

On commence par écrire un petit test :

```python
def test_copy_choices():
    initial_list = ["a"]
    d1 = Choice(initial_list)
    initial_list[0] = "CHANGE"
    d1.roll()
    assert d1.get_position() == "a"
```

Regardez-le planter. Que s'est-il passé ? Puis proposez une solution.

Enfin, on peut tester la deuxième objection avec le test ci-après. Le but de ce test est de vérifier que l'attribut  `choices` est non mutable. Il cherche à produire une erreur : modifier un élément [non mutable](https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747).


~~~ python
import pytest 

def test_no_modification():
    d1 = Choice([1])
    with pytest.raises(Exception):
        d1.choices[0] = 2
~~~

 La façon dont pytest gère les erreurs est décrite [ici](https://docs.pytest.org/en/latest/assert.html#assertions-about-expected-exceptions) : le test précédent est vrai si le code plante et produit une erreur. essayer de comprendre la structure de ce test.


## pattern factory

[Le pattern factory](https://refactoring.guru/fr/design-patterns/factory-method) en est un exemple, il permet de créer des objets via des méthodes presque sans paramètre et avec un nom adapté plutôt qu'avec un constructeur avec des milliers de paramètres

> faire avec les fonctions et constantes dans le fichier
> en amélioration, mettre les constantes en attributs de classes (les valeurs des dés) et en méthodes de classes (les factory)
> Un dé 6, un dé 20 et un dé avec ce qu'on veut.

### Premières expérimentations

Commencez par créer dans le fichier `main.py` un objet simulant 1 dé à six faces (dont les faces valent 1, 2, 3, 4, 5 ou 6). On ne va pas faire de test pour cela, car nos tests sont censés couvrir ce genre d'usage. 

En revanche, on peut calculer les probabilités d'apparitions de chaque face :

  1. lancez N fois le dé (N = 1000) 
  2. comparez les probabilités d'apparition de chaque face par rapport à la théorie (1/6)

Pour aller vite, on pourra utiliser la classe `Counter` du module `collections` de python (voir [la définition](https://docs.python.org/3.7/library/collections.html#collections.Counter), ou [des exemples](https://data-flair.training/blogs/python-counter/)). Le module [collections](https://docs.python.org/3.7/library/collections.html#module-collections) de python, c'est plein de bonnes choses. 

> N'hésitez pas à regarder les différents modules de la [bibliothèque standard](https://docs.python.org/3.7/library/index.html) de python avant de recoder la roue...


>**Nota Bene :** On prendra soin de créer une constante N, pour éviter l'anti-pattern "magic number"


Refaite la même chose pour simuler la somme d'un lancer de 2 dés à 6 faces (2d6 si on jargonne) avec un seul objet `Choice`.  

### On place le tout dans le fichier de la classe

Une fois que vous êtes satisfait de vos fonctions, ajoutez les dans le fichier `choices.py`, ce qui rajoutera des fonctions de créations d'objets et modifiez votre `main.py` pour utiliser ces nouvelles fonctions.

Comme maintenant ce sont des fonctions de votre programme et non plus une utilisation de votre code, il faut ajouter des tests pour ces deux fonctions. Faites le.

> **Nota Bene :** Pour que vos tests ne soient pas trop fastidieux, vous pouvez vérifier que les possibilités correspondent aux comptes que vous avez effectués avec les objets Counter (du module collections).

## Composite

> https://fr.wikipedia.org/wiki/Composite_(patron_de_conception)
> enseignements/MPCI/programmation-algorithmes/annales/2022-2023/4_test_sujet_composition_agrégation_héritage/


## Memento

> https://refactoring.guru/fr/design-patterns/memento

> premiere partie /enseignements/MPCI/programmation-algorithmes/annales/2021-2022/5_test_sujet/
> behavioural pattern

> un dé et une autre classe, la liste avec un save du test. . avec et sans 

### Adaptation des objets au pattern

Le pattern memento nécessite de pouvoir changer la valeur de nos objets. On va donc rajouter une méthode `set_position` à nos objets choice.

On sait maintenant comment faire :

  1. faites un test vérifiant que `set_position` existe et fonctionne,
  2. regardez le planter,
  3. ajouter une méthode `set_position` à `Choice`,
  4. regardez le test réussir.

Pour l'instant, on fera une méthode `set_position` la plus simple possible car elle ne sera utilisée que pour le memento. En particulier, on ne vérifiera pas la validité de la valeur remise dans choice, ce n'est pas utile maintenant. Le coder serait du codage préventif et c'est [YAGNI](https://fr.wikipedia.org/wiki/YAGNI). 

Attention cependant. Pour respecter le [DRY](https://fr.wikipedia.org/wiki/Ne_vous_r%C3%A9p%C3%A9tez_pas) la modification d'un attribut ne doit se faire qu'à un seul endroit : ici la méthode `set_position`. Il faut donc modifier la méthode `roll` pour qu'elle l'utilise.


### Création d'un memento

Créez la classe `Memento` dans le fichier `memento.py` et ses tests dans le fichier :`test_memento.py`.

La classe Memento doit avoir :

  - un objet comme paramètre du constructeur ayant les méthodes `get_position` et `set_position`. Ici un `Choice`.
  - une méthode `restore()` qui permet à l'objet sauvé de reprendre la valeur qu'il avait à la création du memento.

Vous pouvez par exemple transformer le code ci-après en test(s) :


~~~ python
import choice 

dice = choice.dice()
dice.set_position(2)

memento = Memento(dice)
dice.set_position(6)

memento.restore()
print(dice.get_position())  # doit valoir 2
~~~

### Undo list

Nous pouvons maintenant créer une classe `Undo` (dans le fichier `undo.py`) qui va nous permettre de sauver des dés (et leurs valeurs) et de les restaurer à la demande. Cette classe doit pouvoir :

  - sauver un dé avec la méthode : `save(dice)` (un `Memento` sera créé dans la méthode `save` exemple comme ça : `Memento(dice)`)
  - restaurer la dernière valeur sauvée avec la méthode `restore()`
  - connaître le nombre d'items sauvegardés avec une méthode `nb_undos()`

Bien sur vous créerez un fichier de tests `test_undo.py` qui testera les 3 fonctionnalités ci-dessus. Une façon d'utiliser les différents objets est décrite ci-après :

~~~ python
import choice 
from undo import Undo

dice = choice.dice()

undo = Undo()

undo.save(dice)
dice.set_position(5)
print(dice.get_position()) # vaut 5
undo.save(dice)
dice.roll() # dès que l'on change la valeur (ici possiblement différent de 5)


undo.restore()
print(dice.get_position()) # vaut 5
~~~

### Un undo dans dice


Pour ne pas toujours avoir à sauver le dé avant un roll, on pourra utiliser une classe fille de `Choice` dont le `set_position` sauve l'état dans un undo avant de modifier la position. L'objet undo devant être unique dans le programme, il faudrait que le code suivant fonctionne :

~~~ python
from undo import Undo
from choiceUndo import ChoiceUndo

undo = Undo()

d = ChoiceUndo(range(1, 7), undo)

d.set_position(1)
print(d.get_position())  # 1
d.set_position(4)
print(d.get_position())  # 4
undo.restore()
print(d.get_position())  # 1
~~~

Respectez le DRY ! Ne recodez que le minimum possible, c'est à dire une classe `ChoiceUndo` qui hérite de `Choice` et qui ne diffère de celle-ci que par la méthode `set_position` (et le constructeur bien sûr).


Faites le même essai avec 10 utilisations de la méthode `roll()`.

## Observer

> base de la programmation évènementielle
> savoir lorsqu'un dé change. S'abonner à la valeur ?

> seconde partie /enseignements/MPCI/programmation-algorithmes/annales/2021-2022/5_test_sujet/
> https://en.wikipedia.org/wiki/Observer_pattern
