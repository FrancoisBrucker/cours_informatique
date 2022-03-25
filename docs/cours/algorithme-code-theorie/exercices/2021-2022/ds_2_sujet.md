---
layout: page
title:  "DS 2 : projet de code"
category: cours
tags: code python
---

## documents à rendre

1. le code (on doit pouvoir taper `python main.py` pour lancer le jeu)
2. un ficher markdown comportant les différentes étapes du projet que vous avez effectuées

## sujet

Création d'un [jeu du snake](https://fr.wikipedia.org/wiki/Snake_(genre_de_jeu_vid%C3%A9o))

* à chaque update (toutes les 1/10 secondes), le snake avance dans une des quatre directions haut, bas, gauche ou droite. Initialement, la tête du snake est placée au milieu de l'écran et il se déplace vers le haut.
* lorsque l'on appuie sur une touche de direction, la direction du snake change. On ne peut cependant pas aller à l'opposé de la direction actuelle
* lorsque l'on appuie sur la touche espace, le jeu se met en pause (le snake s'arrête de bouger et le score s'arrête d'augmenter). En appuyant sur la barre d'espace, le jeu redémarre.

Initialement, le jeu est en pause. Il faut appuyer sur la barre d'espace pour que le snake se déplace. La direction par défaut est vers le haut.

Le snake est composé de carrés de 20 pixels de long qui se suivent en se touchant par un côté. Initialement, le snake est constitué de 3 carrés.

Position initiale du snake (□ est la tête du snake) :

```text
 □
 O
 O
```

A chaque déplacement le 1er carré se déplace de 20 pixels dans la direction de déplacement, les carrés suivant se plaçant là où était le carré précédent (attention, le snake ne peut pas reculer).

Exemple. Position initiale du snake composé de 6 carrés (0 est la tête du snake) :

```text
  O□
  O
OOO
```

Déplacement vers le haut (de 20pixels) :

```text
   □
  OO
  O
 OO
```

Le jeu s'arrête si :

* le snake sort de l'écran
* un carré composant le snake se superpose avec un autre après un déplacement.

Le score augmente de 1 toutes les secondes où le snake est vivant et que le jeu n'est pas en pause. Initialement, le score vaut 0 et est affiché en haut à droite de l'écran.

Toutes les 5 secondes vont apparaître à l'écran (à une position aléatoire mais pas sur le snake) des disques de rayon 40 pixels. Lorsque le snake passe dessus, son score augmente de 5 et sa taille augmente de 5 carrés (le snake va grossir de 1 carré à chacun des 5 déplacements suivants) :

Exemple de grossissement du snake.

Position initiale :

```text
 OO□
```

On veut faire augmenter la taille du snake de 2 carrés. On suppose également que le snake se déplace vers le haut.

Après le 1er déplacement, le snake à grossi de 1 carré (X est le nouveau carré) : 

```text
   □
 XOO
```

Après le 2ème déplacement, le snake a encore grossi de  carré (X est le nouveau carré) : 

```text
   □
   O
 XOO
```

Finalement, le snake se déplace *normalement*. Par exemple, s'il continue de se déplacer vers le haut :

```text
   □
   O
   O
  OO
```

etc...

Pour aller plus loin :

* bonus qui diminuent la taille
* bonus qui augmentent le score
* malus qui font mourir le snake lorsque qu'il passe dessus.
