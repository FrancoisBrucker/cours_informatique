---
layout: layout/post.njk 
title:  "Programmation événementielle corrigé"
category: cours
tags: mie
author: "François Brucker"
---

## But

Eléments de corrigé de la séance  [programmation événementielle]({% link misc/cartes-ui/programmation_evenementielle.md %}).

## Elements de cours

On utiise [appjar](http://appjar.info) une bibliothèque graphique permettant d'apprendre les interfaces graphiques. On la déconseille fortement pour des applications pro, mais pour apprendre, elle est très bien.


On utilisera le [pattern MVC](http://sametmax.com/quest-de-que-mvc-et-a-quoi-ca-sert/ ) pour la création de nos interfaces, c'est un pattern très pratique pour gérer des systèmes avec des [événements](https://fr.wikipedia.org/wiki/Programmation_événementielle)

Pour vous initier doucements aux interfaces, en particulier web, je ne saurais trop vous conseiller de lire [Don't make me think](https://www.amazon.fr/KRUG-DONT-MAKE-THINK-_p2/dp/0321344758/ref=sr_1_2?adgrpid=56877079420), qui est à la bibliothèque. Il est certes un peu vieux maintenant mais il est otujours éclairant sur ce que cherche un utilisateur.

## Séance tableau

### Programmation d'UI


Pour tout design d'UI on prendra soin de tout justifier. C'est la partie visible de notre code, il est donc indispensable que ce soit travaillé. Une mauvaise UI est  synonyme de mauvaise application.	


#### Design


![me2]({{ "img/fenetre_1_bouton.png" }})

La fenêtre ci-dessus est un exemple possible. D'autres design sont bien sûr acceptables, mais on doit pouvoir tout justifier. Ici :

  - tout doit avoir un nom (boutons et fenêtre ici)
  - on a mis le bouton à droite pour que le rapport avec le texte soit clair 
  

On testerait en vérifiant que : 

  - initialement la valeur du champ texte vaut 1
  - en cliquant sur le bouton, la valeur augmente (on clique 2 fois pour être sur)
  
  
#### Modèle MVC


Le modèle [MVC](https://fr.wikipedia.org/wiki/Modèle-vue-contrôleur) n'est qu'une possiblité pour créer des interfaces de façon *propre* (c'est à dire facilement modifiable). Le principe directeur de toute méthode est de pouvoir retrouver facilement ses petits et donc de séparer au maximum les rôles de chaque partie. POur le modèle MVC on a 3 parties : l'affichage (Vue), les données (Modèle) et les liens entre les 2 (Contrôleur).


Tout ce qui est affiché dans une interface, ou tapé par un utilisateur est du texte (même ce qui est entier) : il ne faut pas utiliser le champ texte comme zone de stockage.

Parlez également du fait que l'on ne contrôle pas lorsque le bouton est appelé. Il faut créer une fonction/méthode qui sera appelée lorsque le bouton sera cliqué. On appelle cela de la programmation évènementielle : on ne fait que réagir aux actions de l'utilisateur ou du système.


![mvc]({{ "img/MVC.png"}})


Note sur les UML : 

  - on n'a pas mis de type pour le bouton. Le type en uml est facultatif.
  - on n'a pas mis de nom de variable pour les méthodes
  
  
Pour le test unitaire, il ne faut pas utiliser la vue. On vérifie donc uniquement que le contrôleur fonctionne et modifie bien le modèle.


#### MVC et appjar.info


On va lier les lignes de code au modèle MVC. On doit retrouver les différentes parties, mais agencées à la mode appjar. En utilisant un autre gestionnaire de fenêtre (comme QT, par exemple) on aurait eu un autre découpage. L'important est de bien décomposer son UI en 3 parties au moins formellement.


Le modèle MVC permet de créer des classes, mais dans l'application elles ne sont pas forcément nécessaires : 

  - pour le modèle, il n'y a que des attributs auxquels on accède. Le fait qu'ils soient privé n'est vraiment pas indispensable. Du coup, pour ne pas réinventer la roue, on utilise un dictionnaire pour cette classe. 
  - pour le contrôleur, il n'y a qu'une méthode. On le remplace par une unique fonction.
  
Le modèle UML n'est qu'une aide pour le découpage du code. Le suivre aveuglément ajoute de la complexité inutilement :
  
  - Vue : l'objet de nom `app` et de classe `gui`. 
  - Modèle : le dictionnaire de nom `model`
  - Contrôleur : la fonction `press`


La bibliothèque [appjar](http://appjar.info/) est documentée et utile pour s'initier aux UIs.

Pour le code : 

  - la vue : on crée des objets graphiques de noms `"valeur"` (un label) et `"plus_un"` (un bouton). Les getter et setter sont accessibles via ces noms. On crée les objets (`addLabel` par exemple), puis on les manipule (`setLabel`). Les nombres à la fin de la création correspondent à ligne et colonne de la fenêtre.
  - on peut utiliser dans la fonction `press` des choses qui ne sont pas encore définies puisque le code ne sera lu que lorsque l'on pressera le bouton. A cette étape là tout sera défini.
  - l'action du contrôleur est passé à la vue en donnant la fonction utilisée pour le clic : lorsque l'on clique sur l'entité de la vue appelée "plus_un", on exécute la fonction `press` avec comme paramètre ce sur quoi on a cliqué (ie . le bouton). On n'a pas besoin de ce paramètre ici.
  - `app.go()` crée la fenêtre. Tout le code en-dessous n'est donc pas lu tant que la fenêtre est active. Il faut donc que tout le contrôleur soit défini avant cette ligne.
 

Dans le contrôleur, on utilise une structure du type `value = value + 1`. On crée donc un nouveau nom `value` dans le namespace concerné qui est égal à la valeur de l'ancien nom `value` + 1.

On ne peut donc pas utiliser uniquement comme Modèle une variable nommée `value` dans le namespace global car si on peut lire un nom (donc `value`) on ne peut créer de nom que dans son propre namespace, ici celui de la fonction (à moins de dire que `value` est de type `global` mais il est déconseillé de faire ce genre de choses. Les namespaces existent pour une raison et passer outre va _forcement_ finir en catastrophe).

Ici, on utilise le nom `model` du namespace global, mais on modifie une variable de son namespace à lui de nom `value`.
   
#### Fenêtre 2 boutons

![me2]({{ "img/fenetre_2_boutons.png"}})

Le bouton `-1` a été mis à gauche car on lit de gauche à droite (-1, texte, +1 se comprend *intuitivement*)

En rendant le texte éditable, il faut interdire de taper autre chose que des entiers et copier la nouvelle valeur dans le modèle.

En créant des interfaces qui interagissent avec un utilisateur, il faut toujours avoir à l'esprit la règle de Murphy qui stipule que s'il peut y avoir des erreurs, il y en aura. Il faut donc toujours faire en sorte que l'erreur ne soit pas possible ou tout du moins vérifier ce qui est écrit par un utilisateur. 



~~~ python
	from appJar import gui

	model = {
	    "value": 0
	}

	def press_plus1(button):
	    model["value"] += 1
	    app.setLabel("value", str(model["value"]))

	def press_moins1(button):
	    if model["value"] > 0:
	         model["value"] -= 1
         
	    app.setLabel("value", str(model["value"]))


	app = gui()
	app.addButton("-1", press_moins1, 0, 0)
	app.addLabel("value", str(model["value"]), 0, 1)
	app.addButton("+1", press_plus1, 0, 2)

	app.go()
	print("c'est fini.")
~~~

On a mis le bouton `-1` à gauche pour que l'on comprenne mieux la relation entre les différentes parties de l'UI.

### Fonctions et namespaces

Cette partie est là pour expliquer comment on peut associer une action à un click sur un bouton en ne passant que le nom de la fonction.

Voir le corrigé de la première séance pour les namespaces. Ici on montre que :
  
  - une méthode ou fonction est une variable comme une autre
  - l'ordre d'évaluation des namespace permet de créer des fonctions à partir de fonctions
  
#### Les fonctions sont des variables comme les autres

Pas de réelles difficultés, on associe juste la méthode append définie dans la class `list` et appliquée à l'objet `une_liste` à une variable nommée `ma_liste` du namespace global. 

Lorsque l'on utilise cette variable, c'est une fonction (elle est de type `<class 'builtin_function_or_method'>`) et elle ajoute l'argument à la liste de nom `ma_liste`.


#### Fonctions de fonction

La première fonction teste que le retour est bien une fonction et que 0 est un élément neutre.
La seconde essai sur un exemple différent de 0.

~~~ python
def test_ajoute_0():
    ajoute_0 = ajoute(0)
    assert ajoute_0(0) == 0

def test_ajoute_different():
	assert ajoute(41)(1) == ajoute(1)(41) == 42
~~~

Question piège. Qu'est censé rendre `ajoute("truc")("bidule")` ? Si on est dans le mode de pensée python, on utilise la concaténation de chaînes de caractères et donc c'est censé rendre "trucbidule". Et c'est le cas avec la proposition de code suivant (attention, pour les chaînes de caractères, `+` n'est pas commutatif...): 


~~~ python
def ajoute(valeur_a_ajouter):
	def ajoute(valeur):
		return valeur_a_ajouter + valeur
	return ajoute
~~~


Bien faire les namespaces et les noms pour comprendre comment tout ça marche pour de vrai (ici le `ajoute` local masque le `ajoute` du namespace qui possède le nom de la fonction `ajoute` du dessus).

### Les dés

Une façon de faire le code ci-après. L'UML est quasi-identique au précédent. J'ai ajouté la bonne pratique de mettre les noms des boutons en constante et un moyen de dimensionner la fenêtre.


~~~ python
    from appJar import gui
    from dice import Dice


    dice = Dice()
    DICE_LABEL = "dice value"


    def on_click(button):
        dice.roll()

        app.setLabel(DICE_LABEL, dice.get_value())

    app = gui()
    app.setGeometry(400, 200)
    
    app.addLabel(DICE_LABEL, dice.get_value(), 0, 0)
    app.addButton("roll", on_click, 0, 1)


    app.go()
~~~


## séance code

### card.py

On a mis les deux classes dans le même fichier. On aurait tout aussi bien pu mettre une classe par fichier comme en Java. Comme le fichier reste petit en taille, on a considéré que c'est encore OK de ne garder qu'un unique fichier. Dans cette correction, on utilise `__len__` pour la classe `Deck` pour pouvoir utiliser la commande `len` de python et être plus lisible mais on demande aux étudiants d'écrire plutôt une méthode `nb_cards` pour ne pas les embrouiller avec les méthodes spécifiques de python.

~~~ python
class Card:
    SPADES = "spade"
    HEARTS = "heart"
    CLUBS = "club"
    DIAMONDS = "diamond"

    def __init__(self, value, color):
        self._value = value
        self._color = color

    def __str__(self):
        return "Card(" + str(self._value) + ", " + str(self._color) + ")"

    def image(self):
        return "resources/Playing_card_" + self._color + "_" + str(self._value) + ".gif"


class Deck:
    def __init__(self):
        self._cards = []

    def __len__(self):
        return len(self._cards)

    def add(self, card):
        self._cards.append(card)

    def show(self):
        return self._cards[-1]

    def remove(self):
        if len(self._cards) > 0:
            return self._cards.pop()
        else:
            return None

    def image(self):
        if len(self._cards) == 0:
            return 'resources/empty.gif'
        else:
            return self.show().image()    
~~~


### test_card.py

On a été obligé de tester des attributs privés dans test `test_creation` (la variable [motorhead](https://www.youtube.com/watch?v=aSsqavYIgNc)). On n'aime pas trop faire ça, normalement, on préfère ne tester que les fonctionnalités. Ce test est un état intermédiaire. Une fois le test du `==` réalisé (voir "pour aller plus loin"), on pourra supprimer ce test.


~~~ python
    from card import Card, Deck


    def test_creation():
        motorhead = Card(1, Card.SPADES)
        assert motorhead._value == 1
        assert motorhead._color == Card.SPADES


    def test_str():
        assert str(Card(1, Card.SPADES)) == 'Card(1, spade)'


    def test_image():
        assert Card(11, Card.DIAMONDS).image() == "resources/Playing_card_diamond_11.gif"


    def test_deck_creation():
        deck = Deck()
        assert deck is not None


    def test_deck_empty_at_creation():
        deck = Deck()
        assert len(deck) == 0


    def test_add_card():
        deck = Deck()
        deck.add(Card(1, Card.SPADES))
        assert len(deck) == 1


    def test_show():
        deck = Deck()
        deck.add(Card(1, Card.SPADES))
        card = Card(2, Card.SPADES)
        deck.add(card)

        assert deck.show() is card


    def test_remove_from_empty_deck():
        deck = Deck()

        assert deck.remove() is None


    def test_remove():
        deck = Deck()
        deck.add(Card(1, Card.SPADES))
        card = Card(2, Card.SPADES)
        deck.add(card)

        assert deck.remove() is card
        assert len(deck) == 1


    def test_image_emty_deck():
        assert Deck().image() == 'resources/empty.gif'
~~~


### main.py

On a fabriqué une méthode `update_ui` qui est appelée à chaque fois que l'UI change. Ceci permet de ne mettre qu'à un endroit toutes les modifications possibles.

On a également lié la même méthode à deux boutons différents : `on_click_move_card`. La différence se fait à l'appel, le paramètre de la méthode étant le label (qui sert également d'identifiant) du bouton.

~~~ python
from appJar import gui

from card import Card, Deck

deck_left = Deck()
deck_right = Deck()


app = gui()


app.addLabelOptionBox("color", [Card.DIAMONDS, Card.SPADES, Card.CLUBS, Card.HEARTS], 0, 0)
app.addLabelOptionBox("value", [str(i) for i in range(1, 14)], 0, 1)


def update_ui():
    app.setImage("left_deck_image", deck_left.image())
    app.setImage("right_deck_image", deck_right.image())
    app.setLabel("left_len", str(len(deck_left)))
    app.setLabel("right_len", str(len(deck_right)))


def on_click(button):
    color = app.getOptionBox("color")
    value = app.getOptionBox("value")
    deck_left.add(Card(int(value), color))
    update_ui()

app.addButton("add card", on_click, 1, 0, 2)

app.addImage("left_deck_image", deck_left.image(), 2, 0, 2)
app.addImage("right_deck_image", deck_right.image(), 2, 3, 2)

app.addLabel("left_len", str(len(deck_left)), 3, 1)
app.addLabel("right_len", str(len(deck_right)), 3, 4)


def on_click_move_card(button):
    if button == "->" and len(deck_left) > 0:
        deck_right.add(deck_left.remove())
    elif button == "<-" and len(deck_right) > 0:
        deck_left.add(deck_right.remove())

    update_ui()

app.addButton("->", on_click_move_card, 4, 0, 2)
app.addButton("<-", on_click_move_card, 4, 3, 2)

app.go()
~~~


### Pour aller plus loin.


Tout est placé dans un unique code.

~~~ python
from appJar import gui

class Card:
    SPADES = "spade"
    HEARTS = "heart"
    CLUBS = "club"
    DIAMONDS = "diamond"

    def __init__(self, value, color):
        self._value = value
        self._color = color

    def __str__(self):
        return "Card(" + str(self._value) + ", " + str(self._color) + ")"

    def __eq__(self, other):
        return self._value == other._value and self._color == other._color

    def __lt__(self, other):
        return (other._value == 1 and self._value != 1) or 1 < self._value < other._value

    def __gt__(self, other):
        return (self._value == 1 and other._value != 1) or self._value > other._value > 1

    def image(self):
        return "resources/Playing_card_" + self._color + "_" + str(self._value) + ".gif"


class Deck:
    def __init__(self):
        self._cards = []

    def __len__(self):
        return len(self._cards)

    def add(self, card):
        self._cards.append(card)

    def show(self):
        return self._cards[-1]

    def remove(self):
        if len(self._cards) > 0:
            return self._cards.pop()
        else:
            return None

    def image(self):
        if len(self._cards) == 0:
            return 'resources/empty.gif'
        else:
            return self.show().image()


deck_left = Deck()
deck_right = Deck()


app = gui()


app.addLabelOptionBox("color", [Card.DIAMONDS, Card.SPADES, Card.CLUBS, Card.HEARTS], 0, 0)
app.addLabelOptionBox("value", [str(i) for i in range(1, 14)], 0, 1)


def update_ui():
    app.setImage("left_deck_image", deck_left.image())
    app.setImage("right_deck_image", deck_right.image())
    app.setLabel("left_len", str(len(deck_left)))
    app.setLabel("right_len", str(len(deck_right)))

    if len(deck_left) == 0 or len(deck_right) == 0:
        app.setLabel("compare", "?")
    elif deck_left.show() == deck_right.show():
        app.setLabel("compare", "=")
    elif deck_left.show() > deck_right.show():
        app.setLabel("compare", ">")
    else:
        app.setLabel("compare", "<")


def on_click(button):
    color = app.getOptionBox("color")
    value = app.getOptionBox("value")
    deck_left.add(Card(int(value), color))
    update_ui()

app.addButton("add card", on_click, 1, 0, 2)

app.addImage("left_deck_image", deck_left.image(), 2, 0, 2)
app.addImage("right_deck_image", deck_right.image(), 2, 4, 2)

app.addLabel("left_len", str(len(deck_left)), 3, 1)
app.addLabel("right_len", str(len(deck_right)), 3, 5)
app.addLabel("compare", "?", 2, 3)

def on_click_move_card(button):
    if button == "->" and len(deck_left) > 0:
        deck_right.add(deck_left.remove())
    elif button == "<-" and len(deck_right) > 0:
        deck_left.add(deck_right.remove())

    update_ui()

app.addButton("->", on_click_move_card, 4, 0, 2)
app.addButton("<-", on_click_move_card, 4, 4, 2)

app.go()   
~~~


## Ressources
 

Pour https://www.planttext.com/


~~~ uml
@startuml
@startuml

title Modèle MVC


class Vue {
  - str texte
  - bouton
  
  + str get_texte()
  + set_texte(str)
  + associe_action(fct)
}


class Modèle {
    - int valeur
    
    +int get_valeur()
    + set_valeur(int)
}
class Contrôleur {
  + ajoute_1()
}

Vue <|-up- Modèle: Mise à jour
Contrôleur  <|-up-|> Vue
Contrôleur  <|-up-|> Modèle

@enduml
~~~
