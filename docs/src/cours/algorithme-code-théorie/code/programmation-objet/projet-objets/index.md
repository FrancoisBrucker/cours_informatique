---
layout: layout/post.njk 
title: "Projet : objets"

eleventyNavigation:
  key: "Projet : objets"
  parent: "Programmation Objet"

prerequis:
    - "../coder-ses-objets/"
---

<!-- début résumé -->

Projet sur le codage d'objets en python.

<!-- end résumé -->

> TBD : à finir

## Un dé

Nous allons créer une classe permettant de jouer aux dés. Nous allons la construire petit à petit. La classe `Dé`{.language-} doit être capable de :

* créer un objet sans paramètre (sa position est alors 1),
* créer un objet avec une position initiale différente de 1,
* connaître et donner la valeur du dé,
* lancer un dé en utilisant une méthode nommée `lance()`{.language-} (la position du dé doit être modifiée aléatoirement).

{% faire %}

1. Proposez une modélisation UML de la classe `Dice`{.language-}.
2. donnez des exemples de manipulation d'objets de cette classe, comme :
   * créer un objet
   * modifier la valeur de sa position
   * obtenir sa position
   * le lancer

{% endfaire %}

### Projet

{% faire %}
Créez un dossier `projet-dice`{.fichier} sur votre ordinateur et ouvrez leu avec visual studio code pour un faire votre projet.
{% endfaire %}

### Classe initiale

{% faire %}

{% endfaire %}

position

### Roll



### getter et setter 

valeur()

change_valeur(new) avec un assert entre 1 et 6

pour aller plus loin : https://docs.python.org/fr/3/library/functions.html#property

### 

en rendant 


A vous ! Mettez en application tout ce que vous avez vu pour créer une classe `Dé`{.language-}. E
{% note %}
Les *getter* let les *setter* sont deux méthodes permettant de rendre ou de modifier un attribut d'un objet sans avoir à le manipuler directement.

Cela permet d'abstraire un attribut de son implémentation.
{% endnote %}

Pour justifier de passer par des méthodes plutôt que d'accéder directement aux attributs, je vous conseille de lire ce [fil de stackoverflow](https://stackoverflow.com/questions/1568091/why-use-getters-and-setters-accessors?rq=1), bien que vieux il dit encore tout ce qu'il faut savoir.


### Modèle du dé



### code python du dé

{% faire %}
Créez le code python de la classe `Dice`{.language-} (fichier `dice.py`{.language-}).
{% endfaire %}

Pour être sûr que tout fonctionne comme prévu :

{% faire %}
Ajoutez les tests de chaque méthode de la classe `Dice`{.language-} (fichier test_dice`{.fichier}).

Il est impossible de tester le hasard, donc pour la méthode `roll`{.language-} vérifiez juste que la position du dé est cohérente (entre 1 et 6) après l'utilisation de la méthode.

Vérifiez que vous avez bien 100% de couverture de code.
{% endfaire %}

Pour jouer avec notre classe dice :

{% faire %}
Créez un fichier `main_dice.py`{.fichier} qui :

1. demande à l'utilisateur :
   * la position initiale du dé
   * la valeur pour laquelle arrêter les lancers
2. lance le dé jusqu'à tant que la valeur demandée par l’utilisateur soit trouvée.
3. le programme affiche le nombre de lancer nécessaire (cela peut être 0)

{% endfaire %}

Pour afficher la position d'un dé, il faut tout d'abord chercher sa position. Améliorons ça :

{% faire %}
Créez une méthode  `__str__`{.language-} pour la classe `Dice`{.language-} qui rende la position du dé (sous la forme d'une chaîne de caractère).

Ajoutez son test et utilisez là (de façon implicite) dans le fichier `main_5_des.py`{.fichier} en affichant directement les dés à l'écran plutôt que leurs positions.
{% endfaire %}

Une autre amélioration :

{% faire %}
Faites en sorte que l'on puisse écrire : `d.roll().roll()`{.language-} si l'on veut lancer deux fois de suite le dé `d`{.language-}.

Cela permettra aussi d'afficher `d`{.language-} directement après l'avoir lancé : `print(d.roll())`{.language-}.
{% endfaire %}

## Une carte

méthode de classe
