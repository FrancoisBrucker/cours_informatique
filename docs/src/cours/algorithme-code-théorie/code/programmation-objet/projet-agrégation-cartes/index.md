---
layout: layout/post.njk 
title: "Projet agrégation : cartes"

eleventyNavigation:
  key: "Projet agrégation : cartes"
  parent: "Programmation Objet"

prerequis:
    - "../composition-agrégation/"
    - "../projet-objets-cartes/"
---

<!-- début résumé -->

Projet utilisant l'agrégation d'objets pour jouer aux cartes.

<!-- end résumé -->

Nous allons ici continuer ce que nous avons commencé lors du projet cartes. Donc si vous ne l'avez pas déjà fait, commencez par le faire :

{% aller %}
[Projet objets : cartes](../projet-objets-cartes/)
{% endaller %}

Pour les besoin de ce TD, nous allons présupposer que vous avez une classe `Dé`{.language-} qui fonctionne. La version minimale que nous allons utiliser ici est disponible ci-après. Mais ne vous sentez pas obliger de l'utiliser.

{% details "**une implémentation de la classe `Carte`{.language-}**" %}

fichier `carte.py`{.fichier} :

```python
SEPT = "sept"
HUIT = "huit"
NEUF = "neuf"
DIX = "dix"
VALET = "valet"
DAME = "dame"
ROI = "roi"
AS = "as"

PIQUE = "pique"
COEUR = "cœur"
CARREAU = "carreau"
TREFLE = "trèfle"


VALEURS = [SEPT, HUIT, NEUF, DIX, VALET, DAME, ROI, AS]
COULEURS = [TREFLE, CARREAU, COEUR, PIQUE]


class Carte:
    def __init__(self, valeur, couleur):
        self._couleur = couleur
        self._valeur = valeur

    @property
    def couleur(self):
        return self._couleur

    @property
    def valeur(self):
        return self._valeur

    def __str__(self):
        return self.valeur + " de " + self.couleur

    def __repr__(self):
        return "Carte(" + repr(self.valeur) + ", " + repr(self.couleur) + ")"

    def __eq__(self, other):
        return (self.valeur == other.valeur) and (self.couleur == other.couleur)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if VALEURS.index(self.valeur) != VALEURS.index(other.valeur):
            return VALEURS.index(self.valeur) < VALEURS.index(other.valeur)

        return COULEURS.index(self.couleur) < COULEURS.index(other.couleur)

    def __le__(self, other):
        return (self == other) or (self < other)

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return (self == other) or (self > other)

```

fichier `test_carte.py`{.fichier} :

```python
import carte
from carte import Carte


def test_constructeur():
    assert isinstance(Carte(carte.SEPT, carte.TREFLE), Carte


def test_str():
    assert str(Carte(carte.SEPT, carte.TREFLE)) == "sept de trèfle"


def test_repr():
    assert repr(Carte(carte.SEPT, carte.TREFLE)) == "Carte('sept', 'trèfle')"


def test_property():
    assert Carte(carte.SEPT, carte.TREFLE).valeur == carte.SEPT
    assert Carte(carte.SEPT, carte.TREFLE).couleur == carte.TREFLE


def test_operator():
    assert Carte(carte.DIX, carte.COEUR) == Carte(carte.DIX, carte.COEUR)
    assert Carte(carte.DIX, carte.COEUR) != Carte(carte.DIX, carte.CARREAU)
    assert Carte(carte.DIX, carte.COEUR) <= Carte(carte.DIX, carte.COEUR)
    assert Carte(carte.DIX, carte.COEUR) > Carte(carte.DIX, carte.CARREAU)
    assert Carte(carte.DIX, carte.CARREAU) < Carte(carte.DIX, carte.COEUR)

```

{% enddetails %}

Le but du projet est :

{% note "**But du projet**" %}

Implémenter une classe `Deck`{.language-} permettant de regrouper toutes les méthodes nécessaire au maniement d'un ensemble de cartes.

{% endnote %}

## Classe `Deck`{.language-}

{% exercice %}
En reprenant la dernière partie du [projet objet : cartes](../projet-objets-cartes/), proposez une modélisation d'une classe UML d'une classe `Deck`{.language-} permettant de jouer au jeu simplifié de la bataille en précisant son lien avec la classe `Carte`{.language-} si l'on suppose un deck initialement vide.
 {% endexercice %}
