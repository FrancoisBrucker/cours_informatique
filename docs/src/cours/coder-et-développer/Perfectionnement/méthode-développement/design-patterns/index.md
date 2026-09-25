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
[Projet Dé héritage](../../../apprendre-programmation/programmation-objet/projet-objets-dés-héritage/){.interne}
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

d_6 = D6()
d_20 = D20()

print(d_6.valeur, d_20.valeur)
d_6.lancer()
d_20.lancer()
print(d_6.valeur, d_20.valeur)


for _ in range(1000):
    d_6.lancer()
    d_20.lancer()

print('1000 lancers :', d_6.moyenne(), d_20.moyenne())
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


d_6 = d6()
d_20 = d20()

print(d_6.valeur, d_20.valeur)
d_6.lancer()
d_20.lancer()
print(d_6)

for _ in range(1000):
    d_6.lancer()
    d_20.lancer()

print('1000 lancers :', d_6.moyenne(), d_20.moyenne())

```

## Fluent interface

{% lien %}
[_Method chaining_](https://en.wikipedia.org/wiki/Method_chaining#Design_patterns)
{% endlien %}

Ce n'est pas un design pattern _stricto-sensu_, plutôt une règle de programmation : on essaie de rendre l'utilisation des méthodes fluide, chaînables sans avoir besoin de créer des variables intermédiaires.

Dans notre cas, il pourrait être intéressant de connaître la valeur du dé directement après un lancer pour pourvoir par exemple remplacer les lignes suivantes dans le fichier `main.py`{.fichier} :

```python
d_6.lancer()
d_20.lancer()
print(d_6.valeur, d_20.valeur)
```

par : 

```python
print(d_6.lancer().valeur, d_20.lancer().valeur)
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


d_6 = d6()
d_20 = d20()

stat6 = Stat()
d_6.add(stat6)

stat20 = Stat()
d_20.add(stat20)

print(d_6.valeur, d_20.valeur)
print(d_6.lancer().valeur, d_20.lancer().valeur)


for _ in range(1000):
    d_6.lancer()
    d_20.lancer()

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

Le pattern composite permet de composer deux dés de façon à pouvoir :

- les lancer simultanément
- obtenir la somme de leurs valeurs respectives

Ceci doit être possible en utilisant une classe `Somme`{.interne} :

```python
# ...

class Somme:
    def __init__(self, gauche, droite):
        self.gauche = gauche
        self.droite = droite

    valeur = property(lambda self: self.gauche.valeur + self.droite.valeur)

    def lancer(self):
        self.gauche.lancer()
        self.droite.lancer()

        return self

# ...

```

On peut l'utiliser ainsi, dans le fichier `main.py`{.fichier} :

```python
from dés import Somme

# ...

somme = Somme(d6(), d20())

print(somme.valeur)
print(somme.lancer().valeur)

```

Il ne nous reste plus qu'à rendre cette classe transparente pour l'utilisateur en créant la somme de deux dés directement dans la classe `DéGénérique`{.language-} :

```python
# ...

class DéGénérique:
    # ...

    def __add__(self, other):
        return Somme(self, other)

    # ...

# ...

```

Modifions notre  `main.py`{.fichier} en conséquence :

```python
# ...

somme = d6() + d20()

# ...

```

Terminons le travail en permettant d'écrire `s = d6() + d6() + d20()`{.language-}. Le pattern composite rend ça trivial, il suffit de déclarer la somme dans la classe `Somme`{.language-} :

```python
# ...

class Somme:
    # ...

    def __add__(self, other):
        return Somme(self, other)

# ...

```


Et le `main.py`{.fichier} mis à jour :

```python
# ...

somme = d6() + d6() + d20()

# ...

```

Continuons sur notre lancée. Un marteau enchanté fait : d6 + 4 dégâts. Il est pour l'instant impossible de gérer ceci avec nos objets, car un entier n'a pas d'attribut `valeur`{.language-} ni `lancer()`{.language-}.

Une solution simple pour résoudre ce problème est de vérifier si un objet possède l'attribut demandé avant de l'utiliser. Pour cela on utilise [la fonction `hasattr`{.language-}](https://docs.python.org/fr/3.14/builtins/functions.html#hasattr) qui possède 2 paramètres :

- le premier est l'objet pour lequel on veut faire la vérification
- le second est le **nom** de l'attribut/méthode (donc une chaîne de caractères) dont on veut tester l'existence.

Dans la somme cela donne :

```python
class Somme:
    # ...

    def lancer(self):
        if hasattr(self.gauche, "lancer"):
            self.gauche.lancer()
        if hasattr(self.droite, "lancer"):
            self.droite.lancer()

        return self

```

On pourrait faire pareil pour l'attribut valeur, mais ici on va plutôt utiliser la fonction [`getattr`{.language-} de python](https://docs.python.org/fr/3.14/builtins/functions.html#getattr) qui rend une valeur par dévaut si l'attribut n;est pas trouvé. Dans notre cas on rend directement l'objet (qui doit être un entier)  :

- le premier est l'objet pour lequel on veut faire la vérification
- le second est le nom de l'attribut/méthode à récupérer
- le troisième est le retour par défaut si l'attribut/méthode n'est pas trouvée.

Dans notre cas pour la property valeur des `Somme`{.language-} cela donne :

```python
class Somme:
    # ...

    valeur = property(
        lambda self: getattr(self.gauche, "valeur", self.gauche)
                     + getattr(self.droite, "valeur", self.droite)
    )

```

On peut maintenant modifier notre `main.py`{.language-} :

```python
somme = d6() + 4

print(somme.valeur)
print(somme.lancer().valeur)
```

## À vous

### Le problème de la boule de feu

Terminons la mise à jour de la classe Dé en lui permettant de résoudre le problème de la boule de feu qui fait `2d6 + 1` dégâts. On supposera que l'on ne peut multiplier que un entier à un dé ou une Somme (3d6 ou 4(d6 + 2d20)). On ne pourra jamais multiplier 2 dés ensemble (d6 * d20 est interdit).

{% faire %}
En implémentant une classe `Multiplication`{.language-} et en utilisant la méthode spéciale `rmul`{.language-} dans les dés. 
{% endfaire %}
{% info %}
pour calculer `a * b`{.language-} python fait plusieurs essais :

1. il essaye `A.__mul__(B)`{.language-}
2. si l'expression précédente rend une erreur de type `TypeError`{.language-} alors python tente `B.__rmul__(A)`{.language-}
{% endinfo %}

### Undo

On a déjà utilisé [le pattern memento](https://refactoring.guru/design-patterns/memento) lorsque l'on a fait de [la compositions et de l'agrégation de dés](../../../apprendre-programmation/programmation-objet/projet-composition-aggrégation-dés/#memento){.interne}, utilisez cette partie pour créer une liste de undo :

{% faire %}
En utilisant le design pattern memento et notre observer, créer une classe permettant de gérer les undo des dés
{% endfaire %}
{% info %}
Vous ne stockerez dans vos undos que les changements de valeurs (si un lancer garde la même valeur de dé ce n'est pas la peine de l'ajouter aux undos).
{% endinfo %}

### Redo

{% faire %}
Ajoutez une classe permettant de gérer les redo.
{% endfaire %}

### Builder

Lorsqu'on joue à un jeu de dés il y a toujours plein de règles différentes pour compter les points :

{% faire %}
Utilisez [le pattern Builder](https://refactoring.guru/design-patterns/builder) pour créer une façon de compter les points de jets de 5 dés où l'on veut être capable de reconnaître :

- la somme des valeurs > 15
- 5 valeurs identiques
- les suites

Et de créer des objets qui reconnaissent l'une, l'autre ou toute combinaison de ces 3 règles pour une liste de 5 dés.

{% endfaire %}


## Pour aller plus loin

- [MVC](https://fr.wikipedia.org/wiki/Mod%C3%A8le-vue-contr%C3%B4leur) ou [MVP](https://fr.wikipedia.org/wiki/Mod%C3%A8le-vue-pr%C3%A9sentation)
- [facade](https://fr.wikipedia.org/wiki/Fa%C3%A7ade_(patron_de_conception))
- [pas singleton](https://www.emaxilde.net/posts/2025/02/10/le-singleton-l-anti-pattern-par-excellence.html) ou encore [Singleton: The Root of all Evil](https://maximilianocontieri.com/singleton-the-root-of-all-evil)
- [Demeter law](https://en.wikipedia.org/wiki/Law_of_Demeter) voir aussi <https://medium.com/vattenfall-tech/the-law-of-demeter-by-example-fd7adbf0c324> ?