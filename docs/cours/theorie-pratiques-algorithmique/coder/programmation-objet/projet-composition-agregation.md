---
layout: page
title:  "exercices sur la création d'objets et leurs composition"
category: cours
tags: informatique cours 
authors: 
  - François Brucker
  - Célia Châtel
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [coder]({% link cours/theorie-pratiques-algorithmique/coder/index.md %}) / [programmation objet]({% link cours/theorie-pratiques-algorithmique/coder/programmation-objet/index.md %}) / [projet : composition et agrégation]({% link cours/theorie-pratiques-algorithmique/coder/programmation-objet/projet-composition-agregation.md %})
>
>* [composition et agrégation]({% link cours/theorie-pratiques-algorithmique/coder/programmation-objet/composition-agregation.md %})
{: .chemin}

Classes et objets, le code !

## aide au code

Dans toute la partie code, vous utiliserez la [couverture de code]({% link cours/theorie-pratiques-algorithmique/coder/programmation-objet/composition-agregation.md %}#couverture-code), pour vérifier que les tests vérifient bien les lignes de votre code.

De plus, maintenant que vous avez pris l'habitude de faire du joli code en utilisant un linter, vous pouvez utiliser [black](https://black.readthedocs.io/en/stable/) pour le faire automatiquement. Suivez le [tuto]({% post_url tutos/editeur/vsc/2021-09-14-vsc-python-modules-supplementaires %}#black) pour l'installer.

## Un Dé

On veut créer une classe `Dice`. Elle doit être capable de :

* créer un objet sans paramètre,
* créer un objet avec sa valeur initiale,
* connaître et donner la valeur du dé (avec les méthodes `get_position` et `set_position`),
* lancer un dé en utilisant une méthode nommée `roll()` (la valeur du dé doit être modifiée aléatoirement).

> Les *getter* let les *setter* sont deux méthodes permettant de rendre ou de modifier un attribut d'un objet sans avoir à le manipuler directement.
>
> Cela permet d'abstraire un attribut de son implémentation.
{: .note}

Pour justifier de passer par des méthodes plutôt que d'accéder directement aux attributs, lisez ce [fil stackoverflow](https://stackoverflow.com/questions/1568091/why-use-getters-and-setters-accessors?rq=1), bien que vieux il dit encore tout ce qu'il faut savoir.

### Modèle {#dice-modele}

> 1. Proposez une modélisation UML de la classe `Dice`.
> 2. donnez des exemples de manipulation d'objets de cette classe, comme créer un objet, modifier la valeur de sa position, obtenir sa position et le lancer.
{: .a-faire}

### code python {#dice-python}

Créez le code python de la classe `Dice` (fichier *"dice.py"*). Pour vérifier que votre code fait ce qu'on lui demande, vous devez créer un fichier *main.py* et essayez de :

* de créer un objet sans argument et de vérifier dans quelle position il est
* de créer un objet en choisissant sa position et de vérifier sa position,
* de modifier la position d'un dé créé et de vérifier qu'elle a bien été changée,
* de lancer le dé et de vérifier que sa position est toujours cohérente avec le nombre de faces.

> Implémentez le tout et Vérifier que tout fonctionne.
{: .a-faire}

### tests {#dice-tests}

> Ajoutez finalement les tests de chaque méthode de la classe `Dice` (fichier *"test_dice"*).
{: .a-faire}

## 5 dés

Méthode naïve pour manipuler 5 dés.

> Dans un ficheir *main_des.py* Créez une liste avec 5 dés. Utilisez une boucle `for` pour les lancer tous les 5, puis voir le résultat du lancé des 5 dés.
{: .a-faire}

## Tapis vert

Pour pouvoir jouer à des jeux de dés, implémentons une classe `TapisVert`.

Cette classe doit avoir :

* 5 dés comme attribut (un attribut  nommée `dice` de type `tuple` qui contiendra 5 dés),
* pouvoir lancer les 5 dés simultanément (une méthode `roll()` sans paramètre),
* pouvoir donner les 5 dés,
* connaître la somme des valeurs des dés (un méthode `sum()` sans paramètre).

### Modèle {#tapis-vert-modele}

> 1. Proposez une modélisation UML de la classe `TapisVert`.
> 2. donnez des exemples de manipulation d'objets de cette classe, comme créer un objet, modifier la valeur de sa position, obtenir sa position et le lancer.
{: .a-faire}

### code python {#tapis-vert-python}

Créez le code python de la classe `TapisVert` (fichier *"dice.py"*). Pour vérifier que votre code fait ce qu'on lui demande, vous devez créer un fichier *main.py* et essayez de :

* de créer un objet sans argument et de vérifier dans quelle position sont les dés
* de changer la position des 5 dés et de vérifier que la somme fonctionne
* de lancer les dés et de vérifier que leurs positions est toujours cohérente avec le nombre de faces.

> Implémentez le tout et Vérifier que tout fonctionne.
{: .a-faire}

### tests {#tapis-vert-tests}

Ajoutez finalement les tests de chaque méthode de la classe `Dice` (fichier *"test_dice"*).

> Vérifier que vos tests fonctionnent dans vscode.
{: .note}

### Analyse du code

> 1. Comment est-il possible d'avoir à la fois une méthode `roll` pour `Dice` et pour `TapisVert` sans que python s'embrouille ?
> 2. Explicitez tous les namespaces utilisées (namespace de classe, d'objet, de fichier et de fonctions) lors de l'exécution de : `tapis_vert.roll()`
{: .a-faire}

### Pour aller plus loin

> 1. ajouter une méthode `__str__` pour la classe `Dice` histoire de pouvoir faire un `print` sympathique pour les dés.
> 2. faites en sorte de pouvoir afficher joliement les valeurs des dés d'un objet `TapisVert`
> 3. Ajoutez une méthode à `TapisVert` permettant de relancer les dés tant qu'on n'obtient pas une paire, un brelan, etc.
{: .a-faire}
