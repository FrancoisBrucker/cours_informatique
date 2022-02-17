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

## Le dé

Nous allons ici réutiliser la classe `Dice` entamée lors du [projet : composition et agrégation]({% link cours/algorithme-code-theorie/code/programmation-objet/projet-composition-agregation.md %}). Pour être sûr de repartir sur de bonnes bases, utilisez l'implémentation minimale ci-après.

### code {#code-dice}

#### classe

Fichier *"dice.py"* :

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

#### tests

Fichier *"test_dice.py"* :

```python
from dice import Dice


def test_dice_creation_no_argument():
    dice = Dice()
    assert dice.get_position() == 1


def test_dice_creation_argument():
    dice = Dice(4)
    assert dice.get_position() == 4


def test_dice_set_position():
    dice = Dice()
    assert dice.get_position() == 1
    dice.set_position(3)
    assert dice.get_position() == 3


def test_dice_roll():
    dice = Dice()
    dice.roll()
    assert 1 <= dice.get_position() <= 6

```

### Un dé qui compte

Nous voulons créer une version particulière d'un dé : un dé permettant de conserver les statistiques de ses lancers.

Implémentez la classe `StatDice` qui hérite de `Dice`, retient le nombre de fois que chaque valeur possible a été obtenue et permet de calculer les statistiques associées.

> Vous devez donc écrire et tester pour la classe `StatDice` :
>
> * la méthode `__init__` sans oublier d'appeler le constructeur de la classe mère,
> * une nouvelle méthode `set_position` qui utilise la méthode `set_position` du dé classique et met à jour les décomptes de lancers du dé
> * une méthode `stats` qui renvoie les nombres d'apparition de chaque valeur
>
{: .a-faire}

On pourra stocker le nombre d'apparition de chaque face dans une liste où l'indice + 1 correspond à la face.

### programme

> Créez un programme qui lance $N=1000$  fois votre dé (par exemple) et rend ses statistiques.
>
> Vous utiliserez ensuite ces statistiques pour faire un [test d'adéquation du $\chi^2$](https://fr.wikipedia.org/wiki/Test_du_%CF%87%C2%B2#Exemple_1_:_d%C3%A9termination_de_l'%C3%A9quilibrage_d'un_d%C3%A9) pour vérifier que votre dés est bien équiprobable.
{: .a-faire}

Un test d'adéquation du $\chi^2$ permet de s'assurer que le résultat d'une expérience est conforme à ce qu'on devrait avoir théoriquement.

Pour cela on calcule le nombre :

$$
\chi^2 = \sum_{i=1}^I\frac{(O_i - T_i)^2}{T_i}
$$

Où :

* $I$ : l'ensemble des possibilités (pour nous $I=6$ puisque la valeur d'un dés pour aller de 1 à 6)
* $O_i$ est le nombre de cas **observés** pour la modalité $i$ (pour nous c'est le nombre de fois où le dé à eu la position $i$)
* $T_i$ est le nombre de cas **théorique** que l'on devrait avoir (dans notre cas $\frac{N}{6}$ si on a lancé $N$ fois notre dé)

Plus ce nombre est petit, plus l'expérience est conforme à la théorie.

De façon formelle :

* si la théorie est conforme à la réalité, le nombre $\chi^2$  suit une loi du chi2 à $N-1$ degrés de libertés (ici 5 degrés de libertés)
* la probabilité $P_{\mbox{df}}(X \geq K)=\alpha$ nous donne la chance d'obtenir $K$ ou plus pour une loi du chi2 à df degrés de libertés.

Pour nous $df = 5$ et si on prend $\alpha = .1$ on trouve : $P_{5}(X \geq 9.236) = .1$ (pour connaitre ces valeurs, on utilise des tables comme [celle-ci](https://people.richland.edu/james/lecture/m170/tbl-chi.html)).

Donc si on trouve un $\chi^2$ plus grand ou égal que $9.206$, il y a moins de 10% de chance que l'on ait obtenu ce nombre si l'on suivait une loi du chi2 à df degrés de liberté :

* Il y a moins de 10% de chance de se tromper en supposant que notre expérience ne suit pas la théorie
* Il y a moins de 10% de chance de supposer que notre dé n'est pas équilibré

C'est que l'on appelle le [risque de première espèce](https://fr.wikipedia.org/wiki/Test_statistique#Risque_de_premi%C3%A8re_esp%C3%A8ce_et_confiance) lorsque l'on fait des [test statistiques](https://fr.wikipedia.org/wiki/Test_statistique)

> Le test du chi2 est très pratique lorsque l'on veut vérifier nos hypothèse théoriques sont satisfaites expérimentalement.

## donjons et dragons

### personnages

En reprenant le cours :

> Créez (et testez) les classes personnage, magicien et guerrière.
{: .a-faire}

### bataille

> Créez un programme doit faire en sorte qu'une guerrière et un personnage se tapent dessus à tour de rôle jusqu'à ce que une personne meure. Le dernier héros en vie est ensuite tué par le magicien en lui jetant des sorts jusqu'à ce qu'il meurt.
>  
> Vous donnerez le nombre de tour nécessaire pour cela.
{: .a-faire}

### équipement

> Proposez un modèle de classe d'équipement :
>
> * tout personnage peut porter de l'équipement
> * chaque équipement peut servir soit (pas exclusif) :
>   * en défense : lors d'une attaque, le score d'armure est retranchée à l'attaque
>   * en attaque : lors d'une attaque, l'attaque du personnage est augmenté du score d'attaque
>   * la méthode `has(event)` doit répondre True si l'équipement répond à `event` et `False` sinon. L'évènement sera soit `ATTAQUE` soit `DEFENSE` et permettra de savoir si l'objet est utilisable ou pas dans telle ou telle circonstance.
>
> La classe d'équipement est là pour être héritée par des objets *réels*. Créez des classes d'équipements comme les armures (qui n'ont qu'un score d'armure) ou des armes (qui n'ont qu'un score d'attaque)
{: .a-faire}

Une fois le modèle fait, implémenté et testé :

> Modifier votre programme pour que le personnage et la guerrière ait des équipements différents.
{: .a-faire}
