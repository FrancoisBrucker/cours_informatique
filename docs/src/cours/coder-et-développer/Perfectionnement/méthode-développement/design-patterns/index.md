---
layout: layout/post.njk
title: "Design Patterns"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Les [design patterns](https://fr.wikipedia.org/wiki/Patron_de_conception), patron de conception ou plus prosaïquement "_façons de faire_", sont pour ainsi dire de l'algorithmie objet : ils permettent de résoudre nombre de problèmes courants en développement et d'éviter les erreurs classiques.

{% info %}
Le terme de _design pattern_ a été initialement donné dans le livre [Design Patterns: Elements of Reusable Object-Oriented Software](https://en.wikipedia.org/wiki/Design_Patterns) pour le langage C++.
{% endinfo %}

Ils permettent de résoudre de façon efficace des problèmes courants en programmation. Il est utile de connaître une liste actuelle de design patterns (certains de la liste originelle, comme [singleton](<https://fr.wikipedia.org/wiki/Singleton_(patron_de_conception)>) ne sont plus utilisés et d'autres, comme [MVP](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93presenter) sont apparus), car ils donnent souvent de bonnes idées pour résoudre les problèmes que l'on se pose.

{% attention2 "**À retenir**" %}
Les design pattern sont très utilisés par les bibliothèques (par exemple [les design pattern de react](https://refine.dev/blog/react-design-patterns/)), les reconnaître vous permettra 'aller vite dans la compréhension de celles-ci.
{% endattention2 %}

Le site suivant contient une liste actualisée de design patterns :

{% lien "Design et refactoring pattern" %}
- [Refactoring GURU : design pattern](https://refactoring.guru/design-patterns)
- [Refactoring GURU : refactoring pattern](https://refactoring.guru/refactoring)

{% endlien %}

Il existe aussi leurs doubles maléfiques, les anti-patterns, qui sont des solutions évidentes -- et mauvaises -- à des problèmes courants. Là aussi, il est bon de connaître une liste actualisée d'anti-pattern, comme par exemple :

{% lien "Anti pattern" %}
- [Définition d'un anti-pattern](https://fr.wikipedia.org/wiki/Antipattern)
- [Quelques anti-patterns classiques](http://sahandsaba.com/nine-anti-patterns-every-programmer-should-be-aware-of-with-examples.html)
{% endlien %}

Nous allons utiliser la classe `Dé`{.language-} qui nous a accompagné tout au long du cours de programmation objet et lui ajouter quelques design pattern pour encore une fois l'améliorer.

{% lien %}
[Projet Dé héritage](/cours/coder-et-développer/apprendre-programmation/programmation-objet/projet-objets-dés-héritage/){.interne}
{% endlien %}
{% details "code", "open" %}

Fichier `dés.py`{.language}
```python 
from random import randrange

import random

class Stat:
    def __init__(self):
        self.historique = []

    def sauve(self):
        self.historique.append(self.valeur)

    def moyenne(self):
        return sum(self.historique) / max(1, len(self.historique))

class DéGénérique(Stat):
    MIN_VALEUR = 1

    def __init__(self, max, valeur=1):
        super().__init__()

        self.MAX_VALEUR = max
        self._valeur = valeur
    
    valeur = property(lambda self: self._valeur)

    def lancer(self):
        self._valeur = random.randrange(self.MIN_VALEUR, self.MAX_VALEUR + 1)
        self.sauve()


class D6(DéGénérique):
    def __init__(self, valeur=1):
        super().__init__(6, valeur)


class D20(DéGénérique):
    def __init__(self, valeur=1):
        super().__init__(20, valeur)
```

Fichier `main.py`{.fichier} :

```python 
from dés import D6, D20

d6 = D6()
d20 = D20()

print(d6.valeur, d20.valeur)
d6.lancer()
d20.lancer()
print(d6.valeur, d20.valeur)


for _ in range(1000):
    d6.lancer()
    d20.lancer()

print('1000 lancers :', d6.moyenne(), d20.moyenne())
```

{% enddetails %}

## Créer des objets grâce à une factory

{% lien %}
- [Pattern factory](https://refactoring.guru/design-patterns/factory-method)
- [_Creational pattern_](https://en.wikipedia.org/wiki/Creational_pattern)
{% endlien %}

Le pattern factory est un design pattern faisant parti des pattern de création d'objet. Il stipule que l'on doit créer des objets via des fonctions avec le moins de paramètres possible et avec un nom adapté plutôt qu'avec un constructeur possédant des milliers de paramètres.

Dans notre cas ce pattern permet également de faire disparaître les deux classes qui n'existent que via leur constructeur :

```python 
from random import randrange

import random

class Stat:
    def __init__(self):
        self.valeur = 1
        self.historique = []

    def sauve(self):
        self.historique.append(self.valeur)

    def moyenne(self):
        return sum(self.historique) / max(1, len(self.historique))

class DéGénérique(Stat):
    MIN_VALEUR = 1

    def __init__(self, max, valeur=1):
        super().__init__()

        self.MAX_VALEUR = max
        self.valeur = valeur

    def lancer(self):
        self.valeur = random.randrange(self.MIN_VALEUR, self.MAX_VALEUR + 1)
        self.sauve()


def d6(valeur=1):
    return DéGénérique(6, valeur)

def d20(valeur=1):
    return DéGénérique(20, valeur)

```

On peut alors utiliser directement les fonctions de création dans le fichier `main.py`{.fichier} :

```python
from dés import d6, d20


d6 = d6()
d20 = d20()

print(d6.valeur, d20.valeur)
d6.lancer()
d20.lancer()
print(d6.valeur, d20.valeur)

for _ in range(1000):
    d6.lancer()
    d20.lancer()

print('1000 lancers :', d6.moyenne(), d20.moyenne())

```

## Fluent interface

{% lien %}
[_Method chaining_](https://en.wikipedia.org/wiki/Method_chaining#Design_patterns)
{% endlien %}

Ce n'est pas un design pattern _stricto-sensu_, plutôt une règle de programmation : on essaie de rendre l'utilisation des méthodes fluide, chaînables sans avoir besoin de créer des variables intermédiaires.

Dans notre cas, il pourrait être intéressant de connaître la valeur du dé directement après un lancer pour pourvoir par exemple remplacer les lignes suivantes dans le fichier `main.py`{.fichier} :

```python
d6.lancer()
d20.lancer()
print(d6.valeur, d20.valeur)
```

par : 

```python
print(d6.lancer().valeur, d20.lancer().valeur)
```

{% info %}
Ok, ce n'est pas très impressionnant ici, mais si vous utilisez la bibliothèque pandas pour l'analyse ds données par exemple. vous verrez [la puissance de ce genre d'écriture](https://www.stat4decision.com/fr/method-chaining-avec-la-librairie-pandas/).
{% endinfo %}

Pour ceci il suffit de changer la méthode `Dé.lancer`{.language-} :

```python

class DéGénérique(Stat):

    # ...

    def lancer(self):
        self.valeur = random.randrange(self.MIN_VALEUR, self.MAX_VALEUR + 1)
        self.sauve()

        return self

    # ...
```

## Pattern observer

{% lien %}
- [Pattern observer](https://refactoring.guru/design-patterns/observer)
- [_Behavioural pattern_](https://en.wikipedia.org/wiki/Behavioral_pattern)
{% endlien %}


Le pattern observer est à la base de [la programmation évènementielle](https://fr.wikipedia.org/wiki/Programmation_%C3%A9v%C3%A9nementielle) utilisée pour développer des interfaces graphique.

Dans notre cas, il va être utile d'utiliser ce pattern pour supprimer l'héritage.

Commençons par préparer le pattern en ajoutant la méthode permettant d'ajouter un observateur et la notification :

```python
class DéGénérique(Stat):
    # ...

    def __init__(self, max, valeur=1):
        # ...

        self._observateurs = []
            

    # ...

    def add(self, observateur):
        self._observateurs.append(observateur)

    def remove(self, observateur):
        self._observateurs.remove(observateur)

    def notify(self):
        for o in self._observateurs:
            o.update(self)

```

Et on peut supprimer la l'héritage pour placer la notification après lancé :

```python
class DéGénérique:
    # ...

    def lancer(self):
        self._valeur = random.randrange(self.MIN_VALEUR, self.MAX_VALEUR + 1)
        self.notify()

        return self

```

On peut maintenant créer l'observateur qui va sauver nos jet et en calculer la moyenne :

```python
class Stat:
    def __init__(self):
        self.historique = []

    def update(self, dé):
        self.historique.append(dé.valeur)

    def moyenne(self):
        return sum(self.historique) / max(1, len(self.historique))

```

Et le `main.py`{.fichier} devient :

```python
from dés import d6, d20, Stat


d6 = d6()
d20 = d20()

stat6 = Stat()
d6.add(stat6)

stat20 = Stat()
d20.add(stat20)

print(d6.valeur, d20.valeur)
print(d6.lancer().valeur, d20.lancer().valeur)


for _ in range(1000):
    d6.lancer()
    d20.lancer()

print('1000 lancers :', stat6.moyenne(), stat20.moyenne())

```

L'observateur découple l'objet qui fait et l'objet qui observe, ce qui est une bonne chose. De plus il permet d'ajouter d'autre types d'observateurs sans effort comme vous allez le faire plus tard.

{% lien %}
[Couplage en informatique](https://fr.wikipedia.org/wiki/Couplage_(informatique))
{% endlien %}

## Pattern composite

{% lien %}
- [Pattern composite](https://refactoring.guru/design-patterns/composite)
- [_Structural pattern_](https://en.wikipedia.org/wiki/Structural_pattern)
{% endlien %}

> TBD
> TBD: https://fr.wikipedia.org/wiki/Composite_(patron_de_conception)
> enseignements/MPCI/programmation-algorithmes/annales/2022-2023/4_test_sujet_composition_agrégation_héritage/

## Pattern Memento

> TBD on l'a déjà vu, on le remets avec l'observer

## On s'entraîne


> TBD refactor [old](./design-patterns-old) et [old corrigé](./design-patterns-corrige)


### Memento

> reprendre le memento de la composition et le mettre dans un observer pour créer un undo (donner les specs)
> attention : ne sauver QUE quand la valeur change (ie. différente du dernier élément stocké)
> 
> premiere partie /enseignements/MPCI/programmation-algorithmes/annales/2021-2022/5_test_sujet/
> behavioural pattern


#### Undo list

Nous pouvons maintenant créer une classe `Undo` (dans le fichier `undo.py`) qui va nous permettre de sauver des dés (et leurs valeurs) et de les restaurer à la demande. Cette classe doit pouvoir :

- sauver un dé avec la méthode : `save(dice)` (un `Memento` sera créé dans la méthode `save` exemple comme ça : `Memento(dice)`)
- restaurer la dernière valeur sauvée avec la méthode `restore()`
- connaître le nombre d'items sauvegardés avec une méthode `nb_undos()`

Bien sur vous créerez un fichier de tests `test_undo.py` qui testera les 3 fonctionnalités ci-dessus. Une façon d'utiliser les différents objets est décrite ci-après :

```python
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
```

#### Un undo dans dice

Pour ne pas toujours avoir à sauver le dé avant un roll, on pourra utiliser une classe fille de `Choice` dont le `set_position` sauve l'état dans un undo avant de modifier la position. L'objet undo devant être unique dans le programme, il faudrait que le code suivant fonctionne :

```python
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
```

Respectez le DRY ! Ne recodez que le minimum possible, c'est à dire une classe `ChoiceUndo` qui hérite de `Choice` et qui ne diffère de celle-ci que par la méthode `set_position` (et le constructeur bien sûr).

Faites le même essai avec 10 utilisations de la méthode `roll()`.

### TapisVert

> méthode de comptage avec un builder

## Pour aller plus loin

- [MVC](https://fr.wikipedia.org/wiki/Mod%C3%A8le-vue-contr%C3%B4leur) ou [MVP](https://fr.wikipedia.org/wiki/Mod%C3%A8le-vue-pr%C3%A9sentation)
- [facade](https://fr.wikipedia.org/wiki/Fa%C3%A7ade_(patron_de_conception))
- [pas singleton](https://www.emaxilde.net/posts/2025/02/10/le-singleton-l-anti-pattern-par-excellence.html) ou encore [Singleton: The Root of all Evil](https://maximilianocontieri.com/singleton-the-root-of-all-evil)
- [Demeter law](https://en.wikipedia.org/wiki/Law_of_Demeter) voir aussi <https://medium.com/vattenfall-tech/the-law-of-demeter-by-example-fd7adbf0c324> ?