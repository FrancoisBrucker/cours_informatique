---
layout: layout/post.njk 
title: "Projet : composition et agrégation"

eleventyNavigation:
  key: "Projet : composition et agrégation"
  parent: "Programmation Objet"
---

{% prerequis "**Prérequis** :" %}

* [Composition et agrégation](../composition-agrégation)

{% endprerequis %}

<!-- début résumé -->

Classes et objets, le code !

<!-- end résumé -->

## Coder des objets

La programmation objet ressemble comme deux gouttes d'eau à la programmation classique d'algorithmes. Les principes y sont juste poussés à l'extrême.

Commencez par vérifier que les exemples du cours fonctionnent.

{% faire %}
Créer un nouveau projet vscode dans un dossier nommé `panier`{.fichier} et recopiez-y les trois fichiers de la [partie composition et agrégation](../composition-agrégation#code-final).
{% endfaire %}

{% faire %}
Vérifiez que :

* tous les tests passent
* le programme principal fonctionne

{% endfaire %}

## Un Dé

A vous ! Mettez en application tout ce que vous avez vu pour créer une classe `Dice`{.language-}. Elle doit être capable de :

* créer un objet sans paramètre (sa position est alors 1),
* créer un objet avec sa position initiale,
* connaître et donner la valeur du dé (avec les méthodes `get_position`{.language-} et `set_position`{.language-}),
* lancer un dé en utilisant une méthode nommée `roll()`{.language-} (la valeur du dé doit être modifiée aléatoirement).

{% note %}
Les *getter* let les *setter* sont deux méthodes permettant de rendre ou de modifier un attribut d'un objet sans avoir à le manipuler directement.

Cela permet d'abstraire un attribut de son implémentation.
{% endnote %}

Pour justifier de passer par des méthodes plutôt que d'accéder directement aux attributs, je vous conseille de lire ce [fil de stackoverflow](https://stackoverflow.com/questions/1568091/why-use-getters-and-setters-accessors?rq=1), bien que vieux il dit encore tout ce qu'il faut savoir.

{% faire %}
Créez un dossier `des-des`{.fichier} qui sera la racine de votre projet.
{% endfaire %}

### Modèle du dé

{% faire %}

1. Proposez une modélisation UML de la classe `Dice`{.language-}.
2. donnez des exemples de manipulation d'objets de cette classe, comme :
   * créer un objet
   * modifier la valeur de sa position
   * obtenir sa position
   * le lancer

{% endfaire %}

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

## 5 dés

Méthode naïve pour manipuler 5 dés.

{% faire %}
Dans un fichier `main_5_des.py`{.fichier} Créez une liste avec 5 dés. Utilisez une boucle `for`{.language-} pour les lancer tous les 5, puis voir le résultat du lancer des 5 dés.
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

## Tapis vert

Nous allons créer une classe permettant de gérer nos 5 dès de façon plus pratique qu'avec notre liste.

Pour pouvoir jouer à des jeux de dés, implémentons une classe `TapisVert`{.language-}.

### Modèle du tapis vert

{% faire %}

1. Proposez une modélisation UML de la classe `TapisVert`{.language-}.
2. donnez des exemples de manipulation d'objets de cette classe comme :
   * créer un objet
   * donner un tuple contenant ses 5 dés
   * lancer les dés qu'il contient avec une méthode `roll()`{.language-} (la méthode `roll`{.language-} ne doit pas avoir de paramètres)

{% endfaire %}

### Code python du tapis vert

{% faire %}
Créez le code python de la classe `TapisVert`{.language-} (dans le fichier `dice.py`{.fichier})
{% endfaire %}

Pour ses tests vous pourrez :

{% faire %}

* Vérifier qu'après la création d'un objet `TapisVert`{.language-} on dispose bien de 5 dés positionnés sur 1.
* Vérifiez qu'après avoir lancé les dés, leurs positions sont toujours cohérentes avec le nombre de faces.
* Vérifiez que `TapisVert`{.language-} donne bien ses dés et non une copie de ceux-ci. Pour réaliser ceci vous pourrez implémenter le test suivant :
   1. demander les dés d'un objet de type `TapisVert`{.language-}
   2. modifier la position d'un dé
   3. redemander les dés de l'objet de type `TapisVert`{.language-} et vérifier que la position du dé est bien celle modifiée

{% endfaire %}

### Analyse du code

{% faire %}

1. Comment est-il possible d'avoir à la fois une méthode `roll`{.language-} pour `Dice`{.language-} et pour `TapisVert`{.language-} sans que python s'embrouille ?
2. Explicitez tous les namespaces utilisées (namespace de classe, d'objet, de fichier et de fonctions) lors de l'exécution de : `tapis_vert.roll()`{.language-}

{% endfaire %}

### Pour aller plus loin

{% faire %}

1. faites en sorte de pouvoir afficher joliment un objet `TapisVert`{.language-} (en affichant par exemple la valeurs de ses 5 dés)
2. Ajoutez des méthodes à `TapisVert`{.language-} permettant de savoir s'il a une paire, un brelan, un carré.
3. Ajoutez des méthodes à `TapisVert`{.language-} permettant de savoir s'il a une double-paire ou un full.

{% endfaire %}

### Pour aller encore plus loin

{% faire %}

Implémentez le jeu [poker d'as](https://fr.wikipedia.org/wiki/Poker_d%27as).

Notez qu'il faudra ajouter des méthodes permettant de bloquer un dé pour qu'il ne participe pas au lancer.

{% endfaire %}
