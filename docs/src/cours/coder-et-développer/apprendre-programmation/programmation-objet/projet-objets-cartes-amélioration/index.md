---
layout: layout/post.njk
title: "Projet : Amélioration des objets cartes"

eleventyNavigation:
  prerequis:
    - "../projet-objets-cartes/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons améliorer la classé que nous avions crée lors du projet précédent (en prérequis).

{% details "Un code possible d'une carte" %}

Fichier `carte.py`{.fichier} :

```python 
SEPT = 7
HUIT = 8
NEUF = 9
DIX = 10
VALET = 11
DAME = 12
ROI = 13
AS = 14

PIQUE = 4
COEUR = 3
CARREAU = 2
TREFLE = 1


VALEURS = (SEPT, HUIT, NEUF, DIX, VALET, DAME, ROI, AS)
COULEURS = (TREFLE, CARREAU, COEUR, PIQUE)


class Carte:
    def __init__(self, valeur, couleur):
        self.couleur = couleur
        self.valeur = valeur

    def texte(self):
        valeur = ["7", "8", "9", "10", "V", "D", "R", "1"]
        couleur = ["♣︎", "♦", "♥", "♠"]
        return valeur[self.valeur - 7] + couleur[self.couleur - 1]

    def plus_grande_ou_égale_que(self, other):
        return (self.valeur > other.valeur) or (
            (self.valeur == other.valeur) and (self.couleur >= other.couleur)
        )

```

Fichier `test_carte.py`{.fichier} :

```python
import carte
from carte import Carte


def test_constructeur():
    assert isinstance(Carte(carte.SEPT, carte.TREFLE), Carte)


def test_texte():
    assert Carte(carte.SEPT, carte.TREFLE).texte() == "7♣︎"


def test_plus_grande_ou_égale_que():
    assert Carte(carte.AS, carte.TREFLE).plus_grande_ou_égale_que(Carte(carte.VALET, carte.PIQUE))
    assert Carte(carte.AS, carte.TREFLE).plus_grande_ou_égale_que(Carte(carte.AS, carte.TREFLE))
    assert Carte(carte.AS, carte.PIQUE).plus_grande_ou_égale_que(Carte(carte.AS, carte.TREFLE))
    assert not Carte(carte.VALET, carte.PIQUE).plus_grande_ou_égale_que(Carte(carte.AS, carte.TREFLE))

```

{% enddetails %}

## Affichage d'une carte

{% faire %}
Remplacez la méthode `Carte.texte()`{.language-} par la méthode `Carte.__str__()`{.language-}.
{% endfaire %}
{% faire %}
Modifiez les tests pour prendre en compte de cette nouvelle méthode.
{% endfaire %}

##  Attribut de classes

Pour créer les cartes on utilise des constantes définies dans le fichier `carte.py`{.fichier}. Commençons par mettre ces constantes directement dans la classe pour ne pas avoir à tout importer :

{% faire %}
Placez les différentes constantes relatives aux valeurs et aux couleur des cartes en attributs de classe et modifiez les tests en conséquence.

{% endfaire %}

Cependant, pour spécifier à l'utilisateur les valeurs et couleurs possibles, utilisez des constantes et des tuples n'est cependant pas optimal. Pour gérer les énumérations, python met à disposition [les Enum](https://docs.python.org/fr/3/library/enum.html). 

On pourrait ainsi gérer les couleurs ainsi :

```python
>>> from enum import Enum
>>> couleur = Enum("Couleur", [("Pique", 4), ("Cœur", 3), ("Carreau", 2), ("Trèfle", 1)])
>>> print(couleur.pique.name)
pique
>>> print(couleur.pique.value)
4
>>> c = couleur.pique
>>> c
<Couleur.pique: 4>
>>> for c in couleur:
...     print(c)
...
Couleur.pique
Couleur.cœur
Couleur.carreau
Couleur.trèfle

```

{% faire %}
Utilisez des `Enum`{.language-} pour gérer les constantes `VALEURS`{.language-} et `COULEURS`{.language-},puis supprimez les constantes relatives aux différentes valeurs et couleurs individuelles (on n'utilisera que les enum). 

Modifiez les tests en conséquence.
{% endfaire %}

Cette technique est redoutable : elle est à la fois lisible, sans magic number et portable ! Utilisez-la dès que vous voulez gérer des énumérations.

## Comparaisons

Une fois la carte créée, il ne faudrait plus pouvoir la modifier. Or pour l'instant on a directement accès aux attributs, donc rien n'interdit de le faire, rendons nos attributs privés :

{% faire %}

Rendez les attributs valeurs et couleurs de chaque carte privé.

{% endfaire %}

{% note "**Méthode de conception**" %}
Lorsque l'on crée un objet, si on a pas de raison particulière de le rendre modifiable on crée un **_value object_**. Cela évite les effets de bords (et rend la programmation concurrente et parallèle bien plus simple).
{% endnote %}

## Comparaisons de cartes

Ajoutez à votre classe carte les opérateurs de comparaisons :

{% faire %}
Codez et testez les [opérateurs de comparaisons](../améliorer-ses-objets#comparaison){.interne} :

- `==`{.language-} qui correspond a à la méthode `__eq__`{.language-}
- `!=`{.language-} qui correspond a à la méthode `__ne__`{.language-}
- `<`{.language-} qui correspond a à la méthode `__lt__`{.language-}
- `>`{.language-} qui correspond a à la méthode `__gt__`{.language-}
- `<=`{.language-} qui correspond a à la méthode `__le__`{.language-}
- `>=`{.language-} qui correspond a à la méthode `__ge__`{.language-}

{% endfaire %}
{% info %}
N'hésitez pas à utiliser des opérateurs déjà codé. Vous pouvez par exemple utiliser les fonctions `==`{.language-} et `<=`{.language-} pour coder les autres les comparaisons.
{% endinfo %}
