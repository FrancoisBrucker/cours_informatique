---
layout: page
title:  "Programmation événementielle"
category: cours
tags: mie
authors: 
  - Célia Châtel
  - François Brucker
---

## But


> **Elements de corrigé :** Ils sont disponibles [là]({% link misc/cartes-ui/programmation_evenementielle_corrige.md %}). Cependant, ils ne dispensent pas d'aller en cours, c'est une aide à la compréhension.

## Séance tableau

Le [sujet au format pdf]({{ "ressources/TD_4_impression.pdf" }}).


## Séance code

### Le dé

Reprenons notre exemple du dé pour construire une interface la plus simple possible affichant simplement la valeur d'un
dé et un bouton pour le relancer. On vous donne le code d'une interface possible vue en TD. Prenez le temps de le lancer, le
comprendre et modifier certaines choses pour expérimenter vous-mêmes.

~~~ python
from appJar import gui # on importe la classe représentant les fenêtres dans la librairie appJar
from dice import Dice

app = gui() # création de l'objet app qui est la fenêtre
app.setGeometry(500, 200) # définition de la taille de la fenêtre

dice = Dice() 
DICE_LABEL = "dice value"

def press_roll(button): # définition de la fonction qu'on utilisera quand quelqu'un clique sur le bouton
    dice.roll()
    app.setLabel(DICE_LABEL, str(dice.get_position())) # on change l'affichage du texte identifié par <DICE_LABEL> pour mettre la position du dé

app.addLabel("position", "Position : ", 0, 0) # ajout d'un texte identifié par <position> dans la fenêtre aux coordonnées 0, 0
app.addLabel(DICE_LABEL, str(dice.get_position()), 0, 1) # ajout d'un texte identifié par <DICE_LABEL> contenant la position du dé aux coordonnées 0, 1
app.addButton("Roll", press_roll, 0, 2) # ajout du bouton associé à la fonction press_roll

app.go() # lancement de l'application
~~~



### UI UI joue aux cartes

Vous allez utiliser ce que nous avons fait en TD lors de la séance 2 pour créer une UI permettant de jouer aux cartes.

Les images des cartes sont placées dans le fichier zip [resources.zip]({{ "ressources/resources.zip"}}) dézippez le pour pouvoir les utiliser.

#### La classe carte

Le code ci-après vous donne la classe carte et ses tests que vous allez utiliser par la suite. Copiez ce code dans deux fichiers `card.py` et `test_card.py`. Vérifiez que tous les tests passent.

##### card.py

~~~ python
class Card:
    SPADES = "spade"
    HEARTS = "heart"
    CLUBS = "club"
    DIAMONDS = "diamond"

    def __init__(self, value, color):
        self._value = value
        self._color = color

    def image(self):
        return "resources/Playing_card_" + self._color + "_" + str(self._value) + ".gif"
~~~
  
##### test_card.py

~~~ python
from card import Card

def test_creation():
    motorhead = Card(1, Card.SPADES)
    assert motorhead._value == 1
    assert motorhead._color == Card.SPADES


def test_image():
    assert Card(11, Card.DIAMONDS).image() == "resources/Playing_card_diamond_11.gif"
~~~
  

Comprendre les tests vous permet de comprendre le code. Passez un peu de temps pour voir et comprendre ce que l'on teste et pourquoi ça marche.
 
#### Choix d'une carte

Le code suivant crée une carte selon ce qui est sélectionné dans les *option boxes*.
Exécutez le code et comprenez comment tout ceci fonctionne. Assurez vous que vous avez bien dézippé le fichier `resources.zip` pour que python trouve bien les différentes images.



###### main.py

Lorsque l'on code on a au moins 3 fichiers : 
    
  - le fichier des fonctionnalités (ici `card.py`)
  - le fichier de test des fonctionnalités (ici `test_card.py`)
  - le programme en lui même. Ici notre application dans une fenêtre (le fichier `main.py`)


~~~ python
    from appJar import gui

    from card import Card


    app = gui()


    app.addLabelOptionBox("color", [Card.DIAMONDS, Card.SPADES, Card.CLUBS, Card.HEARTS], 0, 0)
    app.addLabelOptionBox("value", [str(i) for i in range(1, 14)], 0, 1)


    def on_click(button):
        color = app.getOptionBox("color")
        value = app.getOptionBox("value")
        app.setImage("card_image", Card(int(value), color).image())

    app.addButton("show card", on_click, 1, 0, 2)
    app.addImage("card_image", "resources/empty.gif", 2, 0, 2)

    app.go()
~~~

### Création d'un deck

Un deck est un tas de cartes. Nous allons créer petit à petit cette classe en lui ajoutant des fonctionnalités en
utilisant la méthode de [TDD](https://fr.wikipedia.org/wiki/Test_driven_development). 

#### Préparation

On commence ainsi par ajouter une classe vide dans le fichier `card.py` :

##### card.py

~~~ pyhton
class Deck:
    pass
~~~
    
    
Et un test vérifiant que l'on peut créer un Deck dans `test_card.py`

##### test_card.py

~~~ python
from card import Deck

def test_deck_creation():
    deck = Deck()
    assert deck is not None
~~~
    

Vérifiez que les tests passent.

#### Cycle de développement

On va maintenant ajouter petit à petit les tests qui vont nous permettre d'ajouter des fonctionnalités à la classe. On va toujours suivre le même *pattern* :

  1. ajouter un test et le voir planter en exécutant tous les tests
  2. ajouter la fonctionnalité voulue à la classe
  3. exécutez les tests et voir le tout fonctionner.


#### Fonctionnalité 1 : ajout de cartes


Un deck est un conteneur. Il doit être vide à la création et on doit pouvoir lui ajouter des cartes. 

On commence par un test vérifiant que l'on a créé une méthode `nb_cards` permettant de connaître le nombre de cartes contenues dans le deck : 

~~~ python
def test_deck_empty_at_creation():
    deck = Deck()
    assert deck.nb_cards() == 0
~~~

Le test va rater puisque vous n'avez pas pas encore écrit le code correspondant. 


On ajoute un test qui vérifie que l'on peut ajouter une carte au deck : 

~~~ python
def test_add_card():
    deck = Deck()
    deck.add(Card(1, Card.SPADES))
    assert deck.nb_cards() == 1
~~~ 

Puis on écrit le code correspondant (on pourra ajouter un attribut liste au deck. N'oubliez alors pas de l'initialiser dans le constructeur). On ne sait cependant pas si la bonne carte a été ajoutée. On va régler ce problème avec la fonctionnalité suivante.

#### Ajout/suppression de la carte du dessus

Un deck doit être une LIFO. Pour être sur que ceci soit ok, on va ajouter une méthode permettant de rendre la carte du dessus 


On commence par les tests :

~~~ python

def test_show():
    deck = Deck()
    deck.add(Card(1, Card.SPADES))
    card = Card(2, Card.SPADES)
    deck.add(card)
    assert deck.show() is card
~~~


Dans le test ci-dessus, on utilise le mot clé `is` qui signifie le même objet. Ainsi, même is deux objet sont similaires, `assert [] == []` rendra vrai (deux liste différente mais ayant le même contenu), elles ne sont pas les même `assert [] is []` rendra faux.


A vous de compléter le code. 

On peut enfin créer le test pour rendre la carte du dessus du deck.

On commence par tester le fait que l'on rend `None` si le deck est vide:


~~~ python
def test_remove_from_empty_deck():
    deck = Deck()
    
    assert deck.remove() is None
~~~

Faites le code correspondant.


Puis que l'on récupère bien les cartes dans l'ordre  : 

~~~ python
def test_remove():
    deck = Deck()
    deck.add(Card(1, Card.SPADES))
    card = Card(2, Card.SPADES)
    deck.add(card)
    
    assert deck.remove() is card
    assert deck.nb_cards() == 1
~~~


### UI


On vous demande d'utiliser l'UI précédente pour avoir :

  - deux decks côte à côte initialement vides
  - un bouton qui ajoute une carte (que l'on choisit grâce à deux menus   déroulants) au premier deck
- un bouton permettant de passer une carte du premier au second deck. 

Une façon (élégante) de gérer l'affichage des cartes pourra être de coder une méthode `image` à deck


Vous pouvez une fois ceci réalisé ajouter deux chaînes de caractères permettant de savoir le nombre de cartes dans chaque deck.    



### Pour aller plus loin 



#### Comparaisons de cartes

En utilisant les méthodes de comparaison vues à la toute fin de la première séance de code, codez les méthodes permettant de faire passer les tests suivants :

~~~ python
def test_card_equality():
    assert Card(1, Card.SPADES) == Card(1, Card.SPADES)
    assert Card(1, Card.SPADES) != Card(1, Card.DIAMONDS)

    assert Card(1, Card.SPADES) != Card(13, Card.DIAMONDS)


def test_card_lesser_than():
    assert not Card(3, Card.SPADES) < Card(3, Card.SPADES)
    assert Card(2, Card.SPADES) < Card(3, Card.SPADES)


def test_card_larger_than():
    assert not Card(3, Card.SPADES) > Card(3, Card.SPADES)
    assert Card(3, Card.SPADES) > Card(2, Card.SPADES)
~~~    
    


On pourra ensuite ajouter entre les 2 decks un champ permettant de savoir si la carte du deck de gauche est égale, inférieure ou supérieure à la carte du deck de droite.

#### Considérer deck comme une liste

La méthode `nb_cards` de deck a la même utilité que la fonction `len`que l'on utilise dans les listes. La méthode `__len__` permet d'utiliser la fonction `len` directement. Coder cette fonctionnalité, puis supprimez la méthode `nb_cards`. Il faudra changer le code de l'ui et les tests également.
