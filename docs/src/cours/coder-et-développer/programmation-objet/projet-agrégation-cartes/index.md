---
layout: layout/post.njk 
title: "Projet agrégation : cartes"

eleventyNavigation:
  prerequis:
    - "../projet-objets-cartes-amélioration/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons ici continuer ce que nous avons commencé lors des précédents projets cartes et utiliser l'agrégation pour pouvoir jouer à la bataille.

Pour les besoins de ce projet, nous allons présupposer que vous avez une classe `Carte`{.language-} qui fonctionne. La version minimale que nous allons utiliser ici est disponible ci-après. Mais ne vous sentez pas obligé.e de l'utiliser.

{% details "**une implémentation de la classe `Carte`{.language-}**" %}

fichier `carte.py`{.fichier} :

```python
from enum import Enum


class Carte:
    VALEURS = Enum(
        "valeur",
        [
            ("sept", 7),
            ("huit", 8),
            ("neuf", 9),
            ("dix", 10),
            ("valet", 11),
            ("dame", 12),
            ("roi", 13),
            ("as", 14),
        ],
    )
    COULEURS = Enum(
        "Couleur", [("pique", 4), ("cœur", 3), ("carreau", 2), ("trèfle", 1)]
    )

    def __init__(self, valeur, couleur):
        self._couleur = couleur
        self._valeur = valeur

    def __str__(self):
        valeur = ["7", "8", "9", "10", "V", "D", "R", "1"]
        couleur = ["♣︎", "♦", "♥", "♠"]
        return valeur[self._valeur.value - 7] + couleur[self._couleur.value - 1]

    def __eq__(self, other):
        return (self._valeur == other._valeur) and (self._couleur == other._couleur)

    def __ge__(self, other):
        return (self._valeur.value >= other._valeur.value) or (
            (self._valeur.value == other._valeur.value)
            and (self._couleur.value >= other._couleur.value)
        )

    def __ne__(self, other):
        return not (self == other)

    def __gt__(self, other):
        return (self != other) and (self <= other)

    def __le__(self, other):
        return other >= self

    def __lt__(self, other):
        return other > self

```

fichier `test_carte.py`{.fichier} :

```python
from carte import Carte


def test_constructeur():
    assert isinstance(Carte(Carte.VALEURS.sept, Carte.COULEURS.trèfle), Carte)


def test_str():
    assert str(Carte(Carte.VALEURS.sept, Carte.COULEURS.trèfle)) == "7♣︎"


def test_operator():
    dix_cœur = Carte(Carte.VALEURS.dix, Carte.COULEURS.cœur)
    dix_carreau = Carte(Carte.VALEURS.dix, Carte.COULEURS.carreau)
    
    assert dix_cœur == dix_cœur
    assert dix_cœur != dix_carreau
    assert dix_cœur <= dix_cœur
    assert dix_cœur > dix_carreau
    assert dix_carreau < dix_cœur

```

{% enddetails %}


Le but des projets carters est de pouvoir jouer à une variante de [la bataille](https://fr.wikipedia.org/wiki/Bataille_(jeu)) :

{% note "**But**" %}

On veut pouvoir mélanger un jeu de 32 cartes (sans joker) puis le séparer en 2 *pioches* de 16 cartes, un tas par joueur.

A chaque tour les deux joueurs prennent la première carte de leur pioche et la révèle. Le joueur ayant la plus grande carte (7 < 8 < 9 < 10 < V < D < R < 1 et si égalité de rang alors : ♠ > ♥ > ♦ > ♣︎) prend les deux cartes et les place dans sa pile de défausse (initialement vide).

Lorsqu'un joueur doit prendre une carte alors que sa pioche est vide, il mélange les cartes de sa défausse qui forment une nouvelle pioche. Si la pioche et la défausse sont vides, le joueur perd la partie.

{% endnote %}


## Classe `Deck`{.language-}

Vous allez implémenter une classe `Deck`{.language-} permettant de regrouper toutes les méthodes nécessaires au maniement d'un ensemble de cartes.


{% exercice %}
Proposez une modélisation d'une classe UML d'une classe `Deck`{.language-} permettant de jouer au jeu simplifié de la bataille en précisant son lien avec la classe `Carte`{.language-} si l'on suppose un deck initialement vide.
 {% endexercice %}
{% details "corrigé" %}

![deck uml](deck-uml.png)

{% enddetails %}

## Code

{% faire %}
Implémentez la classe `Deck`{.language-} dans le fichier `deck.py`{.fichier}  et ses tests dans le fichier `test_deck.py`{.fichier}
{% endfaire %}

Pour pouvoir jouer au jeu de la bataille, il faut une fonction qui crée un jeu :

{% faire %}
Créez une fonction `jeu32()`{.language-} dans le fichier `deck.py`{.fichier} qui rend un `Deck`{.language-} contenant un jeu de 32 cartes.
{% endfaire %}

Enfin, il faut un moyen de facilement transférer des cartes d'un Deck à l'autre :

{% faire %}
Créez et testez une méthode `Deck.transfert(deck, nombre)`{.language-} qui transfère les `nombre`{.language-} premières cartes du deck au deck passé en paramètre.

{% endfaire %}

## Jeu

{% faire %}

Reprenez le jeu de la dernière partie du [projet objet : cartes](../projet-objets-cartes/){.interne} et remplacez ses fonctions par la nouvelle classe `Deck`{.language-}.

{% endfaire %}
{% details "**une implémentation du jeu sans `Deck`{.language-}**" %}

```python
import random

import carte
from carte import Carte


paquet = []
for valeur in carte.VALEURS:
    for couleur in carte.COULEURS:
        paquet.append(Carte(valeur, couleur))

random.shuffle(paquet)

pioche1 = paquet[:16]
défausse1 = []
pioche2 = paquet[16:]
défausse2 = []

MAX_TOUR = 1000

N = 1

while N <= MAX_TOUR and min(len(pioche1), len(pioche2)) > 0:
    print(
        "Tour ",
        N,
        "1 : ",
        len(pioche1),
        "/",
        len(défausse1),
        " ; 2 : ",
        len(pioche2),
        "/",
        len(défausse2),
    )

    carte1 = pioche1.pop()
    carte2 = pioche2.pop()

    print("    1 : ", carte1)
    print("    2 : ", carte2)

    if carte1 > carte2:
        défausse1.extend([carte1, carte2])
        print("    Joueur 1 gagne la carte de l'adversaire")
    else:
        défausse2.extend([carte1, carte2])
        print("    Joueur 2 gagne la carte de l'adversaire")

    if not pioche1:
        pioche1 = défausse1
        random.shuffle(pioche1)
        défausse1 = []

    if not pioche2:
        pioche2 = défausse2
        random.shuffle(pioche2)
        défausse2 = []

    print(pioche1, pioche2)
    N += 1

    # input()

print(N, MAX_TOUR)
if not pioche1:
    print("joueur 1 gagne.")
elif not pioche2:
    print("joueur 2 gagne.")
else:
    print("match nul.")

```

{% enddetails %}


> TBD à intégrer au TD

Vous pouvez maintenant finir le projet en codant le jeu !

La règle du jeu est :

1. mélangez un jeu de 32 cartes en deux **pioches** de 16 cartes, une pour chaque joueur (vous pourrez commencer par créer un paquet de 32 cartes, puis le mélanger en utilisant [`random.shuffle`{.language-}](https://docs.python.org/fr/3/library/random.html#random.shuffle) et enfin distributer les 16 première cartes à un joueur et les 16 dernières à l'autre)
2. chaque joueur dispose également d'une **défausse**, initialement vide
3. N = 1
4. chaque joueur dévoile la carte du dessus de leur pioche
5. le joueur ayant la carte la plus élevée remporte la carte de l'adversaire et pose les deux cartes (la sienne et celle de son adversaire) dans sa défausse
6. si un joueur n'a plus de cartes dans sa pioche, il mélange les cartes de sa défausse pour en faire un nouvelle pioche
7. si un joueur n'a plus de carte dans sa pioche, il perd la partie
8. N = N + 1
9. si N est inférieur ou au nombre maximum de tour, retour en 4, sinon le jeu s'arrête.

{% faire %}
Codez le jeu dans un fichier `main.py`{.fichier}
{% endfaire %}
