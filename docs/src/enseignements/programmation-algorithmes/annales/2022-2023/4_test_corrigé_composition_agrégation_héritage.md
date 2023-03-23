---
layout: layout/post.njk

title:  "Corrigé Test 4 : composition agrégation héritage"
authors:
    - François Brucker
---

## Barème

Une note sur 6 à raison d'un point par question.

La note sur $20$ finale est obtenue en multipliant la note sur 6 par $5$

{% note "**Objectif du test**" %}

En 30 minutes :

* **un élève *normal*** doit parvenir à faire parfaitement les 2 premières questions et à entamer la 3ème. Ce qui lui permet d'avoir 2.5/6, soit 12.5/20
* **un bon élève** doit parvenir à réussir les 3 premières questions et à entamer la 4ème. Ce qui lui permet d'avoir 3.5/6 et donc 17.5/20
* **un très bon élève** fait plus que les 4 premières questions.
{% endnote %}

## Erreurs fréquemment rencontrées

Vous êtes retombés dans vos anciens travers de ne pas travailler le cours. Vous essayez de vous raccrocher aux branches de vos connaissances du S1 qui - malheureusement pour vous - ne fonctionnent pas en programmation objet. La conséquence est directe : soit vous ratez complètement votre test soit la note est meh.

Les meilleurs fait toutes les questions, le test n'était donc pas trop long. Il vérifiait juste la compréhension du cours.

{% attention %}

L'approximation ne pardonne pas en informatique car le code ne fonctionne tout simplement pas... Il faut vous mettre  sérieusement au travail à la fois pendant les TDs et entre les cours en révisant. Vous ne pouvez pas vivre sur vos acquis en informatique au S2.

{% endattention %}

### Programme `main.py`{.fichier}

Le fichier `main.py`{.fichier} est fait pour être exécuté. Vous ne **pouvez pas** rendre un test où le programme `main.py`{.fichier} fait des erreurs. À la limite vous commentez ce qui ne va pas, mais le fichier doit pouvoir s'exécuter.

### Fonction vs attribut

Encore bien trop d'erreurs et de confusion sur ce qu'est un attribut ou une méthode et de comment les utiliser dans le programme principal.

* Une méthode s'appelle comme une fonction, avec des parenthèses
* un attribut est une variable dans l'espace de nom de l'objet

### Méthode `__add__`{.language-}

La méthode `Somme.__add__(other)`{.language-} doit rendre un nouvel objet. Beaucoup ont ajouté `other`{.language-} à l'objet existent ce qui n'est pas correct.

### Composition d'objets

Quand on fait de la composition d'objet, on utilise au maximum les objets : il faut donc utiliser la méthode `DéGénérique.lancer()`{.language-} dans `Somme.lancer()`{.language-} et ne pas la redéfinir.

## Corrigé

### Question 1

#### 1.1

Fichier `dés.py`{.fichier} :

```python
from random import randrange


class DéGénérique:
    def __init__(self, max, position=1):
        self._max = max
        self._position = position

    def position(self):
        return self._position

    def lancer(self):
        self._position = randrange(1, self._max + 1)


class D6(DéGénérique):
    def __init__(self, position=1):
        super().__init__(6, position)


class D20(DéGénérique):
    def __init__(self, position=1):
        super().__init__(20, position)

```

#### 1.2

Fichier `main.py`{.fichier} :

```python
from dés import D6, D20

d6 = D6()
d20 = D20()

print(d6.position(), d20.position())
d6.lancer()
d20.lancer()
print(d6.position(), d20.position())

```

### Question 2

#### 2.1

Fichier `dés.py`{.fichier} :

```python
# ...

class Somme:
    def __init__(self, gauche, droite):
        self.gauche = gauche
        self.droite = droite

    def position(self):
        return self.gauche.position() + self.droite.position()

    def lancer(self):
        self.gauche.lancer()
        self.droite.lancer()

# ...

```

#### 2.2

Fichier `main.py`{.fichier} :

```python
from dés import Somme

# ...

somme = Somme(d6, d20)

print(somme.position())
somme.lancer()
print(somme.position())

```

### Question 3

#### 3.1

Fichier `dés.py`{.fichier} :

```python
# ...

class DéGénérique:
    # ...

    def __add__(self, other):
        return Somme(self, other)

    # ...

# ...

```

#### 3.2

Fichier `main.py`{.fichier} :

```python
# ...

somme = d6 + d20

# ...

```

### Question 4

#### 4.1

Fichier `dés.py`{.fichier} :

```python
# ...

class Somme:
    # ...

    def __add__(self, other):
        return Somme(self, other)

# ...

```

#### 4.2

Fichier `main.py`{.fichier} :

```python
# ...

somme = d6 + d20

# ...

```

### Question 5

#### 5.1

Fichier `dés.py`{.fichier} :

```python
# ...

class Cte(DéGénérique):
    def __init__(self, position):
        super().__init__(position, position)

    def lancer(self):
        pass


class DéGénérique:
    # ...

    def __add__(self, other):
        if isinstance(other, int):
            other = Cte(other)

        return Somme(self, other)

    # ...

class Somme:
    # ...

    def __add__(self, other):
        if isinstance(other, int):
            other = Cte(other)

        return Somme(self, other)

    # ...

# ...

```

#### 5.2

Fichier `main.py`{.fichier} :

```python
# ...

marteau_magique = D6() + 4
print(marteau_magique.position())
marteau_magique.lancer()
print(marteau_magique.position())

# ...

```

### Question 6

#### 6.1

Fichier `dés.py`{.fichier} :

```python
# ...

class DéGénérique:
    # ...

    def __rmul__(self, multiplicateur):
        return Fois(self, multiplicateur)
    
    # ...

# ...

class Somme:
    # ...

    def __rmul__(self, multiplicateur):
        return Fois(self, multiplicateur)
    
    # ...


class Fois:
    def __init__(self, dé, multiplicateur):
        self.dé = dé
        self.multiplicateur = multiplicateur

    def position(self):
        return self.multiplicateur * self.dé.position()

    def lancer(self):
        self.dé.lancer()

    def __add__(self, other):
        return Somme(self, other)

    def __rmul__(self, multiplicateur):
        return Fois(self.dé, self.multiplicateur * multiplicateur)


```

#### 6.2

Fichier `main.py`{.fichier} :

```python
# ...

les_dés = 3 * (un_d6 + d20)

print(les_dés.position())
les_dés.lancer()
print(les_dés.position())

```

### Fichier finaux

Fichier `dés.py`{.fichier} :

```python
from random import randrange


class DéGénérique:
    def __init__(self, max, position=1):
        self._max = max
        self._position = position

    def position(self):
        return self._position

    def lancer(self):
        self._position = randrange(1, self._max + 1)

    def __add__(self, other):
        if isinstance(other, int):
            other = Cte(other)

        return Somme(self, other)

    def __rmul__(self, multiplicateur):
        return Fois(self, multiplicateur)


class D6(DéGénérique):
    def __init__(self, position=1):
        super().__init__(6, position)


class D20(DéGénérique):
    def __init__(self, position=1):
        super().__init__(20, position)


class Cte(DéGénérique):
    def __init__(self, position):
        super().__init__(position, position)

    def lancer(self):
        pass


class Somme:
    def __init__(self, gauche, droite):
        self.gauche = gauche
        self.droite = droite

    def position(self):
        return self.gauche.position() + self.droite.position()

    def lancer(self):
        self.gauche.lancer()
        self.droite.lancer()

    def __add__(self, other):
        if isinstance(other, int):
            other = Cte(other)

        return Somme(self, other)

    def __rmul__(self, multiplicateur):
        return Fois(self, multiplicateur)


class Fois:
    def __init__(self, dé, multiplicateur):
        self.dé = dé
        self.multiplicateur = multiplicateur

    def position(self):
        return self.multiplicateur * self.dé.position()

    def lancer(self):
        self.dé.lancer()

    def __add__(self, other):
        return Somme(self, other)

    def __rmul__(self, multiplicateur):
        return Fois(self.dé, self.multiplicateur * multiplicateur)

```

Fichier `main.py`{.fichier} :

```python
from dés import D6, D20, Somme
# from dés import Somme  # pour la question 2

print("question 1 :")
d6 = D6()
d20 = D20()

print(d6.position(), d20.position())
d6.lancer()
d20.lancer()
print(d6.position(), d20.position())

print("questions 2 et 3 :")

# somme = Somme(d6, d20)  # pour la question 2
somme = d6 + d20

print(somme.position())
somme.lancer()
print(somme.position())

print("question 4 :")

un_d6 = D6()
un_autre_d6 = D6()
un_d20 = D20()

d6_plus_d6_plus_d20 = un_d6 + un_d20 + un_d6
print(d6_plus_d6_plus_d20.position())
d6_plus_d6_plus_d20.lancer()
print(d6_plus_d6_plus_d20.position())

print("question 5 :")

marteau_magique = D6() + 4
print(marteau_magique.position())
marteau_magique.lancer()
print(marteau_magique.position())

print("question 6 :")

les_dés = 3 * (un_d6 + d20)

print(les_dés.position())
les_dés.lancer()
print(les_dés.position())

```
