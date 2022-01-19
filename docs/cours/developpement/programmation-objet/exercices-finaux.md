---
layout: page
title:  "Exercices finaux"
category: cours
tags: mie
authors: 
  - Célia Châtel
  - François Brucker
---


Veillez à ce que votre code fonctionne. On vous demande à la fois le code python et un rapport permettant de comprendre comment votre code fonctionne.

Créez un dossier *"cartes-ui"* qui sera votre projet vscode.

> Vous n'avez pas besoin d'utiliser `pytest` ici. Lorsque l'on vous demande de créer un fichier de test, créez un programme python qui permet d'exécuter les différentes méthodes.

## But

Vous allez utiliser ce que nous avons fait pendant ce cours pour créer une UI permettant de jouer aux cartes.

Les images des cartes sont placées dans le fichier zip [resources.zip]({{ "./resources.zip"}}).

> dézippez le dans le dossier de votre projet pour pouvoir les utiliser.
{: .a-faire}

Si vous n'avez pas de programmes permettant de dézipper, vous pouvez utiliser [7-zip](https://www.7-zip.org/download.html) (téléchargez la version64 bit pour windows)

## La classe carte

Le code ci-après vous donne la classe carte et ses tests que vous allez utiliser par la suite.

### carte.py

Copiez le fichier *"card.py"* suivant dans votre projet :

```python
class Carte:
    PIQUE = "spade"
    COEUR = "heart"
    CARREAU = "diamond"
    TREFLE = "club"
    

    def __init__(self, valeur, couleur):
        self._valeur = valeur
        self._couleur = couleur

    def image(self):
        return "resources/Playing_card_" + self._couleur + "_" + str(self._valeur) + ".gif"
```

> 1. explicitez dans le rapport :
>    * à quoi servent les 4 valeurs `PIQUE`, `COEUR`, `CARREAU` et `TREFLE`. Affichez le contenu de l'une d'elle.
>    * que signifie le `_`avant les attributs.
> 2. Créez un programme nommé *"test_card.py"* qui doit mettre en évidence comment on peut :
>    * créer une carte : créez un as de pique en utilisant le point précédent
>    * vérifier que l'image associée est bien un as de pique (vérifiez le en regardant le nom de l'image associée)
{: .a-faire}

### main.py

Créez un fichier *"main_carte.py"* et copiez-y le code suivant :

```python
from appJar import gui

from carte import Carte


app = gui()


app.addLabelOptionBox("couleur", ["\u2660", "\u2665", "\u2666", "\u2663"], 0, 0)
app.addLabelOptionBox("valeur", [str(i) for i in range(1, 14)], 0, 1)


def on_click(button):
    couleur = app.getOptionBox("couleur")
    valeur = app.getOptionBox("valeur")
    if couleur == "\u2660":
        app.setImage("Carte_image", Carte(int(valeur), Carte.PIQUE).image())
    elif couleur == "\u2665":
        app.setImage("Carte_image", Carte(int(valeur), Carte.COEUR).image())
    elif couleur == "\u2666":
        app.setImage("Carte_image", Carte(int(valeur), Carte.CARREAU).image())
    elif couleur == "\u2663":
        app.setImage("Carte_image", Carte(int(valeur), Carte.TREFLE).image())
    

app.addButton("affiche carte", on_click, 1, 0, 2)
app.addImage("Carte_image", "resources/empty.gif", 2, 0, 2)

app.go()
```

> Dans le rapport, explicitez comment fonctionne le programme.
{: .a-faire}

## Création d'un deck

Un deck est une pile de cartes. Le deck est initialement vide et on peut ajouter une carte en bas de la pile (méthode `ajoute`) ou supprimer celle du dessus de la pile (méthode `supprime`). On a de plus une méthode permettant de connaitre le nombre de cartes dans le deck (méthode `nombre`) et une méthode permettant de voir la carte du dessus du deck (méthode `voir`).

> 1. Dans le rapport donner le modèle UML du deck et préciser le lien qui l'unie à la classe `Carte`.
> 2. créez un fichier *"deck.py"* dans votre projet et implémentez la classe `Deck`.
> 3. créez un fichier *"test_deck"* dans votre projet qui permet d'utiliser les méthodes de la classe `Deck`.
{: .a-faire}

## UI

>On vous demande de modifier l'UI précédente pour avoir :
>
> * deux decks côte à côte initialement vides
> * un bouton qui ajoute une carte (que l'on choisit grâce à deux menus déroulants) au premier deck
> * un bouton permettant de passer une carte du premier au second deck.
> * connaître le nombre de cartes dans chaque deck
{: .a-faire}

Vous nommerez ce programme *"main_deck"*.

> Pour afficher la carte du dessus du deck, vous créerez une méthode `image` à deck qui rendra l'image de la carte sur le dessus du deck. Vous expliciterez dans le rapport comment fonctionne cette méthode.
{: .a-faire}

## jeu de la bataille

### Comparaisons de cartes

> Implémentez les comparateurs égal (méthode spéciale `__eq__`), plus grand (`__gt__`) et plus petit (`__lt__`) pour vos cartes.
> Modifiez l'UI (appelez ce fichier *"main_comparaison"*) pour qu'elle affiche entre les deux carte `=`, `<`, `>` ou `<>` (si les deux cartes sont incomparables)
{: .a-faire}

### programme final

> Créez un programme nommé *"main.py"* qui permet de jouer à la [bataille](https://fr.wikipedia.org/wiki/Bataille_(jeu)#R%C3%A8gle_actuelle). Il faudra qu'il y ait un bouton coup suivant qui jouera le coup suivant de la partie.
{: .a-faire}

Vous ne ferez qu'afficher le résultat s'il y a bataille, pas les cartes cachées lors de la résolution de la bataille.

> Dans le rapport final, vous expliciterez comment vous avez codé le programme et comment il fonctionne
{: .a-faire}
