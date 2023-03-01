---
layout: layout/post.njk 
title: "Projet composition d'objets : dés"

eleventyNavigation:
  key: "Projet composition d'objets : dés"
  parent: "Programmation Objet"

prerequis:
    - "../composition-agrégation/"
    - "../projet-objets-dés/"
---

<!-- début résumé -->

Classes et objets, vers l'infini et au-delà (carrément !). Nous allons ici combiner des objets que l'on a créé dans d'autres objets que l'on a également créé.

<!-- end résumé -->

Dans les premiers projets objets, vous avez codé des classes toutes seules. Le but de ces projets introductifs étaient de vous montrer comment rassembler les différentes parties d'un concept en un tout appelé classe et l'utiliser *via* des objets.

Cette partie est la suite du projet dés. Donc si vous ne l'avez pas déjà fait, commencez par le faire :

{% aller %}
[Projet objets : dés](../projet-objets-dés/)
{% endaller %}

Pour les besoin de ce TD, nous allons présupposer que vous avez une classe `Dé`{.language-} qui fonctionne. La version minimale que nous allons utiliser ici est disponible ci-après. Mais ne vous sentez pas obliger de l'utiliser.

{% details "**une implémentation de la classe `Dé`{.language-}**" %}

fichier `dé.py`{.fichier} :

```python
import random

MIN_VALEUR = 1
MAX_VALEUR = 6


class Dé:
    def __init__(self, position=1):
        self._positon = 1  # init
        self.position = position  # utilisation du mutateur

    def lancer(self):
        self.position = random.randrange(MIN_VALEUR, MAX_VALEUR + 1)

        return self

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, nouvelle_position):
        if nouvelle_position < MIN_VALEUR:
            nouvelle_position = MIN_VALEUR
        elif nouvelle_position > MAX_VALEUR:
            nouvelle_position = MAX_VALEUR

        self._position = nouvelle_position
```

fichier `test_dé.py`{.fichier} :

```python
from dé import Dé, MIN_VALEUR, MAX_VALEUR

def test_init():
    assert type(Dé()) == Dé

def test_position():
    assert Dé().position == 1
    assert Dé(position=3).position == 3

def test_lancer():
    assert MIN_VALEUR <= Dé().lancer().position <= MAX_VALEUR

def test_set_position():
    dé = Dé()

    dé.position = 4
    assert dé.position == 4

    dé.position = 12
    assert dé.position == MAX_VALEUR

    dé.position = -1
    assert dé.position == MIN_VALEUR

def test_get_position():
    dé = Dé()

    dé.position = 4
    assert dé.position == dé._position

```

{% enddetails %}

Il va nous falloir manipuler 5 dés ensemble pour réaliser le but de notre projet :

{% note "**But du projet**" %}

Jouer au [poker d'as](https://fr.wikipedia.org/wiki/Poker_d%27as).

{% endnote %}

Nous n'atteindrons pas ce but à la fin du projet, mais libre à vous de le continuer et de le finir.

## 5 dés

Méthode naïve pour manipuler 5 dés : la liste de dés.

Pour illustrer cette étape et progresser dans notre projet de jeu, faisons une petite user story :

{% note "**User Story**" %}

* Nom : "jets de dés"
* Utilisateur : un joueur compulsif
* Story : On veut pouvoir lancer des dés et voir le résultat
* Actions :
  1. créer une liste
  2. créer 5 dés que l'on ajoute un à un à la liste
  3. lancer les 5 dés
  4. afficher les valeurs des dés de la liste

{% endnote %}

{% faire %}
Créez la user story dans le fichier `story_jets.py`{.fichier}
{% endfaire %}

## Composition

L'utilisation d'une liste permet de groper les 5 dés, mais il faut toujours les lancer individuellement. Cela pourrait être pratique de lancer automatiquement tous les dés.

### Classe `TapisVert`{.language-}

On aimerait avoir une structure, nommée `TapisVert`{.language-}, qui :

* crée et stocke 5 dés
* permette de lancer les dés stockés en une fois avec une méthode `lancer`{.language}
* rendre les dés contenus dans sa structure via une liste ou un tuple

{% faire %}

1. Proposez une modélisation UML de cette classe, montrez la relation qu'elle entretien avec la classe `Dé`{.language-}.
2. modifier la user story "jets de dés" pour qu'elle utilise cette classe

{% endfaire %}
{% details "corrigé" %}
> TBD
{% enddetails %}

Avant de commencer à coder, comprenez comment il est possible que la méthode `TapisVert.lancer()`{.language-} peut utiliser la méthode `Dé.lancer()`{.language-} alors que les deux méthodes ont le même nom.

Maintenant que vous voyez comment faire codez là :

{% faire %}
Ajoutez le code de la classe `TapisVert`{.language-} dans le fichier `dé.py`{.fichier}).

Ajoutez les test de cette nouvelle classe au fichier `test_dé.py`{.fichier}. Vous pourrez par exemple tester  :

* qu'après la création d'un objet `TapisVert`{.language-} on dispose bien de 5 dés positionnés sur 1.
* qu'après avoir lancé les dés, leurs positions sont toujours cohérentes avec le nombre de faces.
* que `TapisVert`{.language-} donne bien ses dés et non une copie de ceux-ci. Pour réaliser ceci vous pourrez implémenter le test suivant :
   1. demander les dés d'un objet de type `TapisVert`{.language-}
   2. modifier la position d'un dé
   3. redemander les dés de l'objet de type `TapisVert`{.language-} et vérifier que la position du dé est bien celle modifiée

{% endfaire %}

### Affichage

Afin de pouvoir coder plus rapidement nos story, il faut une méthode de représentation de nos objets.

Commençons par le `Dé`{.language-} :
{% faire %}
Créez une méthode `Dé.__str__`{.language-} qui permettent d'écrire :

```python
>>> from dé import Dé
>>> d = Dé()
>>> d.position = 4
>>> print(d)
⚃
>>> 
```

{% endfaire %}
{% info %}
Vous pourrez utilisez les caractères : `"⚀"`{.language-}, `"⚁"`{.language-}, `"⚂"`{.language-}, `"⚃"`{.language-}, `"⚄"`{.language-} et `"⚅"`{.language-} pour vos représentations.
{% endinfo %}

On peut maintenant utiliser `Dé.__str__`{.language-} pour que `TapisVert.__str__`{.language-} soit facile à coder :

{% faire %}
Créez une méthode `TapisVert.__str__`{.language-} qui permettent d'écrire :

```python
>>> from dé import TapisVert
>>> tapis_vert = TapisVert()
>>> print(tapis_vert)
⚀ - ⚀ - ⚀ - ⚀ - ⚀
>>> tapis_vert.lancer()
>>> print(tapis_vert)
⚀ - ⚁ - ⚁ - ⚀ - ⚁
>>> 
```

{% endfaire %}
{% details "corrigé" %}
On peut utiliser deux trucs. Le premier est de construire une liste avec les représentations sous la forme d'une chaîne de caractères des dés. Par exemple :

```python
>>> from dé import TapisVert
>>> tapis_vert = TapisVert()
>>>[str(x) for x in tapis_vert.dés]
['⚀', '⚀', '⚀', '⚀', '⚀']
```

Puis utiliser la méthode `str.join`{.language-} de python qui est super utile pour concaténer des listes de chaînes de caractères :

```python
>>> l = ["coucou", "les", "amis"]
>>> "*".join(l)
'coucou*les*amis'
```

Ces deux astuces nous permettent d'écrire le code :

```python
class TapisVert:
    # ...

    def __str__(self):
        return " - ".join([str(x) for x in self.dés])

    # ...

```

{% enddetails %}

## Reconnaissance

Pour jouer au poker d'as, il nous faudra reconnaître des formes de jets de dés (comme les paires, ou encore les full). Créons une user story pour coder cette fonctionnalité :

{% note "**User Story**" %}

* Nom : "formes de jets"
* Utilisateur : un joueur compulsif
* Story : On veut pouvoir savoir quelles formes de dés sont présentes
* Actions :
  1. jeter 5 dés
  2. vérifier s'il y a une paire, un brelan ou un carré
  3. recommencer en 1

{% endnote %}

{% faire %}
Créez la story dans le fichier `story-formes-dés.py`{.fichier}.

Pour cela, l'utilisateur pourra appuyer sur la entrée pour lancer les dés d'un objet de type `TapisVert`{.language-}, afficher les 5 dés et indiquer s'il y a une paire, un brelan ou un carré avec des méthodes `TapisVert.possède_paire()`{.language-}, `TapisVert.possède_brelan()`{.language-}, et `TapisVert.possède_carré()`{.language-} qui rendent des booléens.
{% endfaire %}

Et maintenant le code des différentes méthodes à implémenter :

{% faire %}
Ajoutez dans `TapisVert`{.language-} les méthodes nécessaires et testez-les en simulant des lancez ayant une forme particulière.

{% endfaire %}

{% info %}

Pour coder cela de façon simple, vous pourrez coder deux méthodes supports :

* une méthode qui rend une liste $L$ de taille 7 telle que $L[i]$ donne le nombre de dés ayant la position $i$ ($1 \eq i \leq 6$)
* une méthode qui prend en paramètre un nombre $n$ et qui rend `True` s'il existe au moins $n$ dés ayant la même position. Ceci permettra de coder de la même manières les différentes fonctions demandées.

{% endinfo %}
