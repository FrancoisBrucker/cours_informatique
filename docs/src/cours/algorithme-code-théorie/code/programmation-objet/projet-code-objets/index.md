---
layout: layout/post.njk 
title: "Projet : objets"

eleventyNavigation:
  key: "Projet : objets"
  parent: "Programmation Objet"
---

{% prerequis "**Prérequis** :" %}

* [coder ses objets](../coder-ses-objets)

{% endprerequis %}

<!-- début résumé -->

Projet sur le codage d'objets en python.

<!-- end résumé -->

Vous allez coder une version simplifiée de la [bataille navale](https://fr.wikipedia.org/wiki/Bataille_navale_(jeu)), avec un unique bateau.

Vous allez travailler avec la boucle de programmation du cours :

1. on code une petite fonctionnalité
2. on vérifie dans le programme principale ou dans un programme principal de test que cette fonctionnalité fonctionne
3. on convertit cette vérification en test que l'on conserve

On testera les fonctionnalités dans un fichier `main_fonctionnalité.py`{.fichier} qui sera refait à chaque test de fonctionnalité.

Le fichier `main.py` contiendra le jeu en lui même.

## Grille

Commençons par l'objet grille. On aimerait que cet objet :

* puisse être construit avec 2 paramètres déterminant le nombre de lignes et le nombre de colonnes de la grille
* contienne un attribut matrice contenant un tableau de ayant le bon nombre de lignes et de colonnes, chaque case ayant le caractère `'.'`{.language-}

{% faire %}
Commencez par écrire le code qui crée un objet grille vide, Vérifier qu'il est bien créé dans le programme principal puis faire le test qui vérifie sa bonne création.
{% endfaire %}

Maintenant que l'on a mis en place le code de création de l'objet :

{% faire %}
Codez le constructeur pour qu'il crée la matrice remplie de `'.'`, vous pourrez faire un test qui vérifie que l'attribut est bien rempli.
{% endfaire %}

Maintenant que l'on peut créer une matrice, représentez la matrice dans le programme principal.

Pour notre projet de bataille navale, Il nous reste à créer une méthode `tirer` qui prend deux paramètres en entrée — `ligne`{.language-} et `colonne`{.language-} — et qui marque le caractère `'o'`{.language-} aux coordonnées indiquée de la grille.

On fera attention au fait que les paramètres `x` et `y`  soient cohérent avec la grille.

{% faire %}
Codez la méthode `tirer(ligne, colonne)`{.language-} de la classe `Grille`{.language-}. Vous ferez attention au fait que si les paramètres ne sont pas cohérent avec la grille, tout se passe comme si on avait tiré en-dehors (l grille reste inchangée).

Vous ferez un test qui vérifie votre fonction.
{% endfaire %}

Enfin dans le programme principal :

{% faire %}
Créer un programme qui :

1. affiche une grille à 5 lignes et 8 colonnes
2. demande à l'utilisateur de rentrer deux coordonnées x et y
3. tier à l'endroit indiqué
4. retourne en 1
{% endfaire %}

## Bateau

On va ajouter des bateaux à la grille :

{% faire %}
Créez une classe `Bateau` dans le fichier `bateau.py`{.fichier}  qui doit posséder comme attribut :

* une ligne
* une colonne
* une longueur
* un booléen nommé vertical qui est vrai si le bateau est placé à la vertical

Créer aussi un constructeur qui devra considérer que par défaut la longueur du du bateau est de 1 et qu'il est placé en position horizontale (il n'y a pas de paramètres par défaut pour la ligne et la colonne).

Vous testerez que les paramètre par défaut sont bien placés.
{% endfaire %}

Ce bateau doit avoir une méthode touché prenant un paramètre grille qui doit répondre `True` si l'on a tiré sur le bateau
et `False` sinon.

{% faire %}
Codez la méthode de `touché(ligne, colonne)`{.language-} de la classe `Bateau`{.language-}.

Vérifiez dans `main_fonctionnalité.py`{.fichier} que la méthode `touché(ligne, colonne)`{.language-} fonctionne et examinant les cas possibles. Une fois que vous êtes satisfait, transférez vos vérifications en tests dans le fichier `test_bateau.py`{.fichier}
{% endfaire %}

## Grille et bateau

{% faire %}
Ajoutez une méthode `ajoute(bateau)`{.language-} à la classe `Grille`{.language-} qui place le bateau `bateau`{.language-} sur la grille en remplaçant le caractère par `X` aux positions du bateau. On ne pourra le faire que si le bateau rentre en entier dans la grille (vous le testerez).
{% endfaire %}

Testez que la méthode  méthode fonctionne. Par exemple, vous pourrez vérifier que pour une grille `g`{.language-} de 2 lignes et 3 colonnes :

* la grille devient égale à `[[".", ".", "."], ["X", "X", "."]]`{.language-} après l'appel `g.ajoute(Bateau(2, 1, longueur=2, vertical=False))`{.language-}
* la grille est inchangée (elle reste égale à  `[[".", ".", "."], [".", ".", "."]]`{.language}) après les appels aux méthodes : `g.ajoute(Bateau(2, 1, longueur=2, vertical=True))`{.language-} et `g.ajoute(Bateau(2, 1, longueur=4, vertical=True))`{.language-}

{% faire %}
Ajoutez une méthode `coulé`{.language-} à la classe `Bateau`{.language-} qui vérifie s'il est coulé. La méthode `coulé`{.language-} prendra un paramètre grille (on vérifiera s'il y a des `'o'` sur toutes les cases du bateau).

Vous testerez cette méthode.
{% endfaire %}

## Fin

{% faire %}
Placez un bateau aléatoire sur la grille et demandez à l'utilisateur de jouer jusqu'à tant que le bateau soit coulé. Vous devez prévenir l'utilisateur si son tir à touché le bateau.

Un fois le bateau coulé, vous afficherez le bateau sur la grille.
{% endfaire %}
