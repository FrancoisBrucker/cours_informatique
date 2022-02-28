---
layout: page
title:  "exercices sur la création d'objets et leurs composition"
category: cours
tags: informatique cours 
authors: 
  - François Brucker
  - Célia Châtel
---

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [code]({% link cours/algorithme-code-theorie/code/index.md %}) / [programmation objet]({% link cours/algorithme-code-theorie/code/programmation-objet/index.md %}) / [projet : composition et agrégation]({% link cours/algorithme-code-theorie/code/programmation-objet/projet-composition-agregation.md %})
>
> **prérequis :**
>
> * [composition et agrégation]({% link cours/algorithme-code-theorie/code/programmation-objet/composition-agregation.md %})
{: .chemin}

Classes et objets, le code !

## aide au code

Dans toute la partie code, vous utiliserez la [couverture de code]({% link cours/algorithme-code-theorie/code/programmation-objet/composition-agregation.md %}#couverture-code), pour vérifier que les tests vérifient bien les lignes de votre code.

De plus, maintenant que vous avez pris l'habitude de faire du joli code en utilisant un linter, vous pouvez utiliser [black](https://black.readthedocs.io/en/stable/) pour le faire automatiquement. Suivez le [tuto]({% link _tutoriels/editeur/vsc/2021-09-14-vsc-python-modules-supplementaires.md %}#black) pour l'installer.

## les tests

Les tests sont bien sur toujours obligatoires ! Vous testerez chaque fonction que vous développerez.

> Lorsque l'on teste un objets et ses méthodes, on essaie dans la mesure du possible de ne pas avoir besoin des attributs. On ne vérifie que les résultats de la méthode, pas comment l'objet stocke ses informations.
>
> On teste des **fonctionnalités** pas une **implémentation particulière de celles-ci**.
{: .note}

## Un Dé

On veut créer une classe `Dice`. Elle doit être capable de :

* créer un objet sans paramètre (sa position est alors 1),
* créer un objet avec sa position initiale,
* connaître et donner la valeur du dé (avec les méthodes `get_position` et `set_position`),
* lancer un dé en utilisant une méthode nommée `roll()` (la valeur du dé doit être modifiée aléatoirement).

> Les *getter* let les *setter* sont deux méthodes permettant de rendre ou de modifier un attribut d'un objet sans avoir à le manipuler directement.
>
> Cela permet d'abstraire un attribut de son implémentation.
{: .note}

Pour justifier de passer par des méthodes plutôt que d'accéder directement aux attributs, je vous conseille de lire ce [fil de stackoverflow](https://stackoverflow.com/questions/1568091/why-use-getters-and-setters-accessors?rq=1), bien que vieux il dit encore tout ce qu'il faut savoir.

### Modèle {#dice-modele}

> 1. Proposez une modélisation UML de la classe `Dice`.
> 2. donnez des exemples de manipulation d'objets de cette classe, comme :
>    * créer un objet
>    * modifier la valeur de sa position
>    * obtenir sa position
>    * le lancer
>
{: .a-faire}

### code python {#dice-python}

> Créez le code python de la classe `Dice` (fichier *"dice.py"*).
{: .a-faire}

Pour être sûr que tout fonctionne comme prévu :

> Ajoutez les tests de chaque méthode de la classe `Dice` (fichier *"test_dice"*).
>
> Il est impossible de tester le hasard, donc pour la méthode `roll` vérifiez juste que la position du dé est cohérente (entre 1 et 6) après l'utilisation de la méthode.
>
> Vérifiez que vous avez bien 100% de couverture de code.
{: .a-faire}

Pour jouer avec notre classe dice :

> Créez un fchier *"main_dice.py"* qui :
>
> 1. demande à l'utilisateur :
>    * la position initiale du dé
>    * la valeur pour laquelle arrêter les lancers
> 2. lance le dé jusqu'à tant que la valeur demandée par l'utilsateur soit trouvée.
> 3. le programme affiche le nombre de lancer nécessaire (cela peut être 0)
>
{: .a-faire}

## 5 dés

Méthode naïve pour manipuler 5 dés.

> Dans un fichier *"main_5_des.py"* Créez une liste avec 5 dés. Utilisez une boucle `for` pour les lancer tous les 5, puis voir le résultat du lancer des 5 dés.
{: .a-faire}

Pour afficher la position d'un dé, il faut tout d'abord chercher sa position. Améliorons ça :

> créez une méthode  `__str__` pour la classe `Dice` qui rende la position du dé (sous la forme d'une chaine de caractère).
>
> ajoutez son test et utilisez là (de façon implicite) dans le fichier *"main_5_des.py"* en *printant* directement les dés plutôt que leurs positions.
{: .a-faire}

Une autre amélioration :

> Faites en sorte que l'on puisse écrire : `d.roll().roll()` si l'on veut lancer deux fois de suite le dé `d`.
>
> Cela permettra aussi d'afficher `d` directement après l'avoir lancé : `print(d.roll())`.
{: .a-faire}

## Tapis vert

Nous allons créer une classe permettant de gérer nos 5 dès de façon plus pratique qu'avec notre liste.

Pour pouvoir jouer à des jeux de dés, implémentons une classe `TapisVert`.

### Modèle {#tapis-vert-modele}

> 1. Proposez une modélisation UML de la classe `TapisVert`.
> 2. donnez des exemples de manipulation d'objets de cette classe comme :
>    * créer un objet
>    * donner un tuple contenant ses 5 dés
>    * lancer les dés qu'il contient avec une méthode `roll()` (la méthode `roll` ne doit pas avoir de paramètres)
{: .a-faire}

### code python {#tapis-vert-python}

> Créez le code python de la classe `TapisVert` (dans le fichier *"dice.py"*)
{: .a-faire}

Pour ses tests vous pourrez :

> * vérifier qu'après la création d'un objet `TapisVert` on dispose bien de 5 dés positionnés sur 1.
> * vérifiez qu'après avoir lancé les dés, leurs positions sont toujours cohérentes avec le nombre de faces.
> * vérifiez que `TapisVert` donne bien ses dés et non une copie de ceux-ci. Pour réaliser ceci vous pourrez implémenter le test suivant :
>    1. demander les dés d'un objet de type `TapisVert`
>    2. modifier la position d'un dé
>    3. redemander les dés de l'objet de type `TapisVert` et vérifier que la position du dé est bien celle modifiée
{: .a-faire}

### Analyse du code

> 1. Comment est-il possible d'avoir à la fois une méthode `roll` pour `Dice` et pour `TapisVert` sans que python s'embrouille ?
> 2. Explicitez tous les namespaces utilisées (namespace de classe, d'objet, de fichier et de fonctions) lors de l'exécution de : `tapis_vert.roll()`
{: .a-faire}

### Pour aller plus loin

> 1. faites en sorte de pouvoir afficher joliment un objet `TapisVert` (en affichant par exemple la valeurs de ses 5 dés)
> 2. Ajoutez des méthodes à `TapisVert` permettant de savoir s'il a une paire, un brelan, un carré.
> 3. Ajoutez des méthodes à `TapisVert` permettant de savoir s'il a une double-paire ou un full.
{: .a-faire}

### Pour aller encore plus loin

> Implémentez le jeu [poker d'as](https://fr.wikipedia.org/wiki/Poker_d%27as).
>
> Notez qu'il faudra ajouter des méthodes permettant de bloquer un dé pour qu'il ne participe pas au lancer.
{: .a-faire}
