---
layout: page
title:  "Héritage"
category: cours
authors: 
  - François Brucker
  - Célia Châtel
---

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [code]({% link cours/algorithme-code-theorie/code/index.md %}) / [programmation objet]({% link cours/algorithme-code-theorie/code/programmation-objet/index.md %}) / [projet : héritage]({% link cours/algorithme-code-theorie/code/programmation-objet/projet-heritage.md %})
>
> **prérequis :**
>
> * [héritage]({% link cours/algorithme-code-theorie/code/programmation-objet/heritage.md %})
> * [projet : composition et agrégation]({% link cours/algorithme-code-theorie/code/programmation-objet/projet-composition-agregation.md %})
{: .chemin}

Présentation du mécanisme d'héritage qui permettant de factoriser du code entre classes.

>a mettre à jour avec un vrai projet
{: .tbd}

## le cours

Refaite le code du cours pour comprendre mieux l'héritage en python.

### géométrie

Codez les classes `Point`, `Polygone` et `Triangle`. Testez les méthodes dans un programme principal nommé *"main_geometrie.py"*.

### odds and ends

refaite les exercices de la partie [odds and ends]({% link cours/developpement/programmation-objet/heritage.md %}#odds-and-ends) du cours sans regarder la solution.

Puis créez un objet `objet_a` de la classe `A` et un objet `objet_b` de la classe `B`. Essayez les lignes suivantes (une à la
fois) et prenez le temps de comprendre ce qu'elles font et pourquoi.

```python

print(objet_a.a)
print(objet_a.b)
print(objet_b.a)
print(objet_b.b)
objet_a.truc_que_fait_a()
objet_a.autre_truc()
objet_a.que_de_b()
objet_b.truc_que_fait_a()
objet_b.autre_truc()
objet_b.que_de_b()
print(A.CTE)
print(objet_a.CTE)
print(objet_b.CTE)
```

### donjons et dragons

Créez un personnage, un magicien et une guerrière. Faite en sorte que la guerrière et le personnage se tapent dessus à tour de rôle jusqu'à ce que une personne meure. Le dernier personnage est ensuite tué par le magicien en lui jetant des sorts jusqu'à ce qu'il meurt.

## Le dé

Nous allons ici réutiliser la classe `Dice` entamée la dernière fois. Pour être sûr de repartir sur de bonnes bases, utilisez l'implémentation minimale suivante (dans un fichier `dice.py`).

### code de Dice {#code-dice}

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

Nous voulons créer une version particulière d'un dé : un dé permettant de conserver les statistiques de ses lancers.

Implémentez la classe `StatDice` qui hérite de `Dice`, retient le nombre de fois que chaque valeur possible a été obtenue et permet de calculer les statistiques associées. Vous devez donc écrire :

* la méthode `__init__` sans oublier d'appeler le constructeur de la classe mère,
* une nouvelle méthode `set_position` qui utilise la méthode `set_position` du dé classique et met à jour les décomptes de lancers du dé
* une méthode `stats` qui renvoie les fréquences d'apparition de chaque valeur
* une méthode `mean` qui renvoie la moyenne des lancers du dé

On pourra stocker le nombre d'apparition de chaque face dans une liste où l'index + 1 correspond à la face.

### tests

Prenez le temps de tester votre code avec un fichier *"main.py"* et de bien comprendre quelle méthode est appelée et pourquoi quand vous utilisez un `StatDice`.
