---
layout: page
title:  "exercices sur la création d'objets et leurs composition"
category: cours
tags: informatique cours 
authors: 
  - François Brucker
  - Célia Châtel
---

Classes et objets, le code !

## Un Dé

On veut créer une classe `Dice`. Elle doit être capable de :

* créer un objet sans paramètre,
* créer un objet avec sa valeur initiale,
* connaître et donner la valeur du dé (avec les méthodes `get_position` et `set_position`),
* lancer un dé (la valeur du dé doit être modifiée).

### Modèle {#dice-modele}

1. Proposez une modélisation UML de la classe `Dice`.
2. donnez des exemples de manipulation d'objets de cette classe, comme créer un objet, modifier la valeur de sa position, obtenir sa position et le lancer.

### code python {#dice-python}

Créez le code python de la classe `Dice` (fichier *"dice.py"*). Pour vérifier que votre code fait ce qu'on lui demande, vous devez créer un fichier *main.py* et essayez de :

* de créer un objet sans argument et de vérifier dans quelle position il est
* de créer un objet en choisissant sa position et de vérifier sa position,
* de modifier la position d'un dé créé et de vérifier qu'elle a bien été changée,
* de lancer le dé et de vérifier que sa position est toujours cohérente avec le nombre de faces.

> Vérifier que tout fonctionne dans vscode.
{.note}

### tests {#dice-tests}

Ajoutez finalement les tests de chaque méthode de la classe `Dice` (fichier *"test_dice"*).

> Vérifier que vos tests fonctionnent dans vscode.
{.note}

## 5 dés

Créez une liste avec 5 dés. Utilisez une boucle `for` pour les lancer tous les 5, puis voir le résultat.

## Tapis vert

Pour pouvoir jouer à des jeux de dés, implémentons une classe `TapisVert`.

Cette classe doit avoir :

* 5 dés comme attribut (un attribut  nommée `dice` de type `tuple` qui contiendra 5 dés),
* pouvoir lancer les 5 dés simultanément (une méthode `roll()` sans paramètre),
* pouvoir donner les 5 dés,
* connaître la somme des valeurs des dés (un méthode `sum()` sans paramètre).

### Modèle {#tapis-vert-modele}

1. Proposez une modélisation UML de la classe `TapisVert`.
2. donnez des exemples de manipulation d'objets de cette classe, comme créer un objet, modifier la valeur de sa position, obtenir sa position et le lancer.

### code python {#tapis-vert-python}

Créez le code python de la classe `TapisVert` (fichier *"dice.py"*). Pour vérifier que votre code fait ce qu'on lui demande, vous devez créer un fichier *main.py* et essayez de :

* de créer un objet sans argument et de vérifier dans quelle position sont les dés
* de changer la position des 5 dés et de vérifier que la somme fonctionne
* de lancer les dés et de vérifier que leurs positions est toujours cohérente avec le nombre de faces.

> Vérifier que tout fonctionne dans vscode.
{.note}

### tests {#tapis-vert-tests}

Ajoutez finalement les tests de chaque méthode de la classe `Dice` (fichier *"test_dice"*).

> Vérifier que vos tests fonctionnent dans vscode.
{.note}

### Analyse du code

1. Comment est-il possible d'avoir à la fois une méthode `roll` pour `Dice` et pour `TapisVert` sans que python s'embrouille ?
2. Explicitez tous les namespaces utilisées (namespace de classe, d'objet, de fichier et de fonctions) lors de l'exécution de : `tapis_vert.roll()`

### Pour aller plus loin

1. ajouter une méthode `__str__` pour la classe `Dice` histoire de pouvoir faire un `print` sympathique pour les dés.
2. Ajoutez une méthode permettant de relancer les dés tant qu'on n'obtient pas une paire, un brelan, etc.
