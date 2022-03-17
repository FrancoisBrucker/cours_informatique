# déroulé du projet arkanoïd

## tache 1

Création d'une fenêtre de 640x480 non redimensionnable avec :

* un label du nombre de vie (2 par défaut), en bas à gauche
* un label avec le score (0 par défaut), en haut à droite

![fenêtre](./tache-1.png)

## tâche 2

* ajout du sol : une ligne à hauteur 50
* ajout du vaisseau :
  * doit être placé sur le sol
  * un rectangle (de hauteur 20 et de longueur 50) de couleur #47B6FF

![fenêtre](./tache-2.png)

## tâche 3

Faire déplacer le vaisseau de gauche à droite sans cogner les bords.

Comme la gestion des déplacement doit être interne au vaisseau, il faut qu'il puisse avoir sa classe à lui. On va donc réaliser cette tâche en 2 temps.

### tache 3.1

Création de la classe Vaisseau

* classe : Vaisseau
* attributs :
  * `forme` un rectangle pyglet de longueur 50, de hauteur 20, initialement placé au centre de la fenêtre
* méthode :
  * `__init__(sol, largeur_fenetre)` : position du sol et largeur de la fenêtre de jeu
  * `draw()`

Pour tester cette classe, vous pourrez vérifier que le vaisseau est bien initialement placé au centre de la fenêtre en comparant :

* la valeur de `vaisseau.forme.x` à sa valeur théorique selon la taille de l'écran.
* la valeur de `vaisseau.forme.y` à la hauteur du sol

### tâche 3.2

Ajout des méthodes et des attributs permettant de déplacer le vaisseau.

Il nous faut côté `Fenetre` :

1. modifier la classe fenêtre pour qu'elle prenne en compte les touches "flèche gauche" et "flèche droite"
2. que l'on change la position du vaisseau à au plus 60 fps (tous les 1/60 secondes)

On doit gérer les mouvement côté `Vaisseau` en ajoutant :

* un attribut `vitesse` qui donne le déplacement en pixel par seconde (500 pixel/s)
* une méthode `bouge(dt, direction)` qui déplace le curseur selon :
  * la direction (-1 à gauche, 0 on ne bouge pas et +1 à droite)
  * par défaut le déplacement sera de sa vitesse fois `dt` sauf si cela le fait dépasser l'écran à gauche ou à droite et dans ce cas là le vaisseau est collé au bord

Pour tester cette méthode vous pourrez faire 4 tests :

* `test_bouge_droite()` : qui vérifie que la position change bien lorsque l'on  veut se déplacer à droite
* `test_bouge_gauche()` : qui vérifie que la position change bien lorsque l'on  veut se déplacer à gauche
* `test_bouge_negatif()` : qui vérifie que l'on se cogne bien au bord gauche de l'écran
* `test_bouge_depasse_taille()` : qui vérifie que l'on se cogne bien au bord droit de l'écran

Pour faire passer ces tests, vous pourrez modifier à la main les différents paramètres comme la vitesse (`vaisseau.vitesse`) ou la position du vaisseau (`vaisseau.forme.x`) pour que votre test soit facile à écrire.

> Félicitations, votre programme doit pouvoir faire bouger le vaisseau ! Vérifiez le.

### tâche 4

La balle et la faire bouger selon une direction donnée.

elle rebondit (selon la normale de la surface) sur :

* 3 bords de l'écran sur 4
* sur le vaisseau

