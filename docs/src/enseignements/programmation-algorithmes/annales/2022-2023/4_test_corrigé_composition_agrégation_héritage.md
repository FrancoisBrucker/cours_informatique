---
layout: layout/post.njk

title:  "Corrigé Test 4 : composition agrégation héritage"
authors:
    - François Brucker
---

## Barème

> TBD

## Erreurs fréquemment rencontrées

> TBD

## Corrigé

### Question 1

> TBD

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

    def somme(self, other):
        return Somme(self, other)

    def fois(self, multiplicateur):
        return Fois(self, multiplicateur)


class D6(DéGénérique):
    def __init__(self, position=1):
        super().__init__(6, position)


class D20(DéGénérique):
    def __init__(self, position=1):
        super().__init__(20, position)


class Somme:
    def __init__(self, gauche, droite):
        self.gauche = gauche
        self.droite = droite

    def position(self):
        return self.gauche.position() + self.droite.position()

    def lancer(self):
        self.gauche.lancer()
        self.droite.lancer()

    def somme(self, other):
        return Somme(self, other)

    def fois(self, multiplicateur):
        return Fois(self, multiplicateur)


class Fois:
    def __init__(self, dé, multiplicateur):
        self.dé = dé
        self.multiplicateur = multiplicateur

    def position(self):
        return self.multiplicateur * self.dé.position()

    def lancer(self):
        self.dé.lancer()

    def somme(self, other):
        return Somme(self, other)

    def fois(self, multiplicateur):
        return Fois(self.dé, self.multiplicateur * multiplicateur)

```

Fichier `main.py`{.fichier} :

```python
from dés import D6, D20

d6 = D6()
d20 = D20()

print(d6.position(), d20.position())
d6.lancer()
d20.lancer()
print(d6.position(), d20.position())

somme = d6.somme(d20)

print(somme.position())
somme.lancer()
print(somme.position())


un_d6 = D6()
un_autre_d6 = D6()
un_d20 = D20()

d6_plus_d6_plus_d20 = un_d6.somme(un_d20).somme(un_d6)
print(">", d6_plus_d6_plus_d20.position())
d6_plus_d6_plus_d20.lancer()
print(d6_plus_d6_plus_d20.position())

print(hasattr(un_d6, "position"))

les_dés = un_d6.somme(d20).fois(3)

print(les_dés.position())
les_dés.lancer()
print(les_dés.position())

```