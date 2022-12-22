---
layout: layout/post.njk 
title: "Projet : héritage"

eleventyNavigation:
  key: "Projet : héritage"
  parent: "Programmation Objet"

prerequis:
    - "../héritage/"
    - "../projet-composition-agrégation"
---

<!-- début résumé -->

Mise en œuvre du mécanisme d'héritage.

<!-- end résumé -->

## Le dé

Nous allons ici réutiliser la classe `Dice`{.language-} entamée lors du [projet : composition et agrégation](../projet-composition-agrégation). Pour être sûr de repartir sur de bonnes bases, utilisez l'implémentation minimale ci-après.

### Code { #code-dice }

{% faire %}

Reprenez le code ci-après et :

1. Vérifiez que les tests passent.
2. Créez un programme principal (un fichier `main.py`{.fichier}) qui crée un dé et le lance 10 fois avant de donner la moyenne des valeurs lancées.

{% endfaire %}

#### Classe

Fichier `dice.py`{.fichier} :

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

#### Tests

Fichier `test_dice.py`{.fichier} :

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

Implémentez la classe `StatDice`{.language-} qui hérite de `Dice`{.language-}, retient le nombre de fois que chaque valeur possible a été obtenue et permet de calculer les statistiques associées.

{% faire %}

Vous devez donc écrire et tester pour la classe `StatDice`{.language-} :

* la méthode `__init__`{.language-} sans oublier d'appeler le constructeur de la classe mère,
* une nouvelle méthode `set_position`{.language-} qui utilise la méthode `set_position`{.language-} du dé classique et met à jour les décomptes de lancers du dé
* une méthode `stats`{.language-} qui renvoie les nombres d'apparition de chaque valeur

{% endfaire %}

On pourra stocker le nombre d'apparition de chaque face dans une liste où l'indice + 1 correspond à la face.

### Programme

{% faire %}

Créez un programme qui lance $N=1000$  fois votre dé (par exemple) et rend ses statistiques.

Vous utiliserez ensuite ces statistiques pour faire un [test d'adéquation du $\chi^2$](https://fr.wikipedia.org/wiki/Test_du_%CF%87%C2%B2#Exemple_1_:_d%C3%A9termination_de_l'%C3%A9quilibrage_d'un_d%C3%A9) pour vérifier que votre dés est bien équiprobable.

{% endfaire %}

Un test d'adéquation du $\chi^2$ permet de s'assurer que le résultat d'une expérience est conforme à ce qu'on devrait avoir théoriquement.

Pour cela on calcule le nombre :

$$
\chi^2 = \sum_{i=1}^I\frac{(O_i - T_i)^2}{T_i}
$$

Où :

* $I$ : l'ensemble des possibilités (pour nous $I=6$ puisque la valeur d'un dés pour aller de 1 à 6)
* $O_i$ est le nombre de cas **observés** pour la modalité $i$ (pour nous c'est le nombre de fois où le dé a eu la position $i$)
* $T_i$ est le nombre de cas **théoriques** que l'on devrait avoir (dans notre cas $\frac{N}{6}$ si on a lancé $N$ fois notre dé)

Plus ce nombre est petit, plus l'expérience est conforme à la théorie.

De façon formelle :

* si la théorie est conforme à la réalité, le nombre $\chi^2$  suit une loi du chi2 à $I-1$ degrés de libertés (ici 5 degrés de libertés)
* la probabilité $P_{\mbox{df}}(X \geq K)=\alpha$ nous donne la chance d'obtenir $K$ ou plus pour une loi du chi2 à df degrés de libertés.

Pour nous $df = 5$ et si on prend $\alpha = .1$ on trouve : $P_{5}(X \geq 9.236) = .1$ (pour connaître ces valeurs, on utilise des tables comme [celle-ci](https://people.richland.edu/james/lecture/m170/tbl-chi.html)).

Donc si on trouve un $\chi^2$ plus grand ou égal que $9.206$, il y a moins de 10% de chance d'obtenir ce nombre si l'on suit une loi du chi2 à df degrés de liberté : Il y a moins de 10% de chance de se tromper en supposant que notre expérience ne suit pas la théorie. Dans notre cas, cela signifie qu'il y a moins de 10% de chance de supposer que notre dé n'est pas équilibré.

C'est que l'on appelle le [risque de première espèce](https://fr.wikipedia.org/wiki/Test_statistique#Risque_de_premi%C3%A8re_esp%C3%A8ce_et_confiance) lorsque l'on fait des [test statistiques](https://fr.wikipedia.org/wiki/Test_statistique)

{% info %}

Le test du chi2 est très pratique lorsque l'on veut vérifier nos hypothèse théoriques sont satisfaites expérimentalement.
{% endinfo %}

## Donjons et dragons

### Personnages

En reprenant [le cours](../héritage#exemple-D&D) :

{% faire %}

Créez (et testez) les classes personnage, magicien et guerrière.

{% endfaire %}

### Bataille

{% faire %}

Créez un programme qui demande à l'utilisateur :

* les caractéristiques d'une guerrière (points de vie, attaque et score de défense
* les caractéristiques d'un [gobelin](https://www.aidedd.org/dnd/monstres.php?vf=gobelin) (points de vie, attaque)
* les caractéristiques d'un magicien (points de vie, attaque et attaque magique)

Puis,  faites en sorte que la guerrière et le Gobelin se tapent dessus à tour de rôle jusqu'à ce qu'un des deux ne meure.

Le dernier héros en vie est ensuite tué par le magicien qui le kite en lui jetant des sorts (comme un fourbe), puis le loote pour aller tout revendre au marchand du bourg (mais c'est une autre histoire et d'autres implémentations).

Vous donnerez le nombre de tours nécessaires pour cela (testez plusieurs possibilités).

{% endfaire %}
