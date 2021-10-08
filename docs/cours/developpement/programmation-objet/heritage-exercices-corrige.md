---
layout: page
title:  "Héritage"
category: cours
authors: 
  - François Brucker
  - Célia Châtel
---

Présentation du mécanisme d'héritage qui permettant de factoriser du code entre classes.

## le cours

Refaite le code du cours pour comprendre mieux l'héritage en python.

### géométrie

Codez les classes `Point`, `Polygone` et `Triangle`. Testez les méthodes dans un programme principal nommé *"main_geometrie.py"*.

### odds and ends

refaite les exercice de la partie [odds and ends]({% link cours/developpement/programmation-objet/heritage.md %}#odds-and-ends) du cours sans regarder la solution.

Puis créez un objet `objet_a` de la classe `A` et un objet `objet_b` de la classe `B`.

```python
objet_a = A(10)
objet_b = B(3, 7)
```

Essayez les lignes suivantes (une à la
fois) et prenez le temps de comprendre ce qu'elles font et pourquoi.

* `print(objet_a.a)` : affiche 10
* `print(objet_a.b)` : produit une erreur, `b` est un attribut de `B`, pas de `A`
* `print(objet_b.a)` : par héritage et utilisation du constructeur de la classe mère, affiche 3
* `print(objet_b.b)` : affiche 7
* `objet_a.truc_que_fait_a()` : affiche `"Autre truc dans la classe mère"`
* `objet_a.autre_truc()` : produit une erreur, `autre_truc`  est défini dans la classe `B`
* `objet_a.que_de_b()` : produit une erreur, `autre_truc`  est défini dans la classe `B`
* `objet_b.truc_que_fait_a()` : par héritage, affiche `"Autre truc dans la classe mère"`
* `objet_b.autre_truc()` : affiche `"C'est mon autre truc à moi"`, méthode définie dans `B`
* `objet_b.que_de_b()`  :  affiche `"Méthode seulement de la classe fille"`, méthode définie dans `B`
* `print(A.CTE)` : affiche `"un attribut de classe"`
* `print(objet_a.CTE)` : affiche `"un attribut de classe"` car si le nom n'est pas dans l'espace de nom de l'objet, on le cherche dans sa classe
* `print(objet_b.CTE)` : affiche `"un attribut de classe"`  par héritage.

### donjons et dragons

Créez un personnage, un magicien et une guerrière. Faite en sorte que la guerrière tue le personnage en combat rapproché, puis que le magicien tue la guerrière avec un de ses sorts dans un programme principal *"main_donjons"*.

```python
import random


class Personnage:
    def __init__(self, vie, attaque):
        self._vie = vie
        self.attaque = attaque

    def se_faire_taper(self, personnage):
        self.vie -= personnage.attaque

    def taper(self, personnage):
        personnage.se_faire_taper(self)

    @property
    def vie(self):
        return self._vie

    @vie.setter
    def vie(self, valeur):
        self._vie = valeur
        if self._vie <= 0:
            self._vie = 0
            print("je suis mort")


class Guerriere(Personnage):
    def __init__(self, vie, attaque, blocage):
        super().__init__(vie, attaque)
        self.blocage = blocage

    def se_faire_taper(self, personnage):
        if self.blocage >= random.randint(0, 100):
            super().se_faire_taper(personnage)


class Magicien(Personnage):
    def __init__(self, vie, attaque, attaque_magique):
        super().__init__(vie, attaque)
        self.attaque_magique = attaque_magique

    def lancer_sort(self, personnage):
        personnage.vie -= self.attaque_magique

xena = Guerriere(10, 2, 50)
peon = Personnage(5, 1)
gandalf = Magicien(4, 1, 3)

while xena.vie > 0 and peon.vie > 0:
    print("xena : ", xena.vie, " peon : ", peon.vie)
    xena.taper(peon)
    peon.taper(xena)


print("xena : ", xena.vie, " peon : ", peon.vie)

if xena.vie > 0:
    surviant = xena
else:
    surviant = peon

while surviant.vie > 0:
    print("survivant : ", surviant.vie)
    gandalf.lancer_sort(surviant)
```

## Le dé

Nous allons ici réutiliser la classe `Dice` entamée la dernière fois. Pour être sûr de repartir sur de bonnes bases, utilisez l'implémentation minimale suivante (dans un fichier `dice.py`).

### code de Dice

```python
import random


class Dice:
    NUMBER_FACES = 6

    def __init__(self, position=1):
        self._position = position

    def get_position(self):
        return self._position

    def set_position(self, new_position):
        self._position = new_position

    def roll(self):
        self.set_position(random.randint(1, self.NUMBER_FACES))
```

### Un dé qui compte

```python
import random


class Dice:
    NUMBER_FACES = 6

    def __init__(self, position=1):
        self._position = position

    def get_position(self):
        return self._position

    def set_position(self, new_position):
        self._position = new_position

    def roll(self):
        self.set_position(random.randint(1, self.NUMBER_FACES))


class StatDice(Dice):
    def __init__(self, position=1):
        super().__init__(position)
        self._memory = [0] * (self.NUMBER_FACES + 1)

    @property
    def memory(self):
        return tuple(self._memory)

    def set_position(self, new_position):
        super().set_position(new_position)
        self._memory[new_position] += 1

    def stats(self):
        n_roll = max(1, sum(self._memory))

        return [x / n_roll for x in self._memory]

    def mean(self):
        n_roll = max(1, sum(self._memory))
        valeur = 0
        for i in range(len(self._memory)):
            valeur += i * self._memory[i]
        return valeur / n_roll


d = StatDice()

for i in range(10000):
    d.roll()

print(d.memory)
print(d.stats())
print(d.mean())
```
