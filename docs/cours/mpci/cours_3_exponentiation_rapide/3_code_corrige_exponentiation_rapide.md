---
layout: page
title:  "Code Exponentiation rapide"
category: cours
tags: informatique cours 
---

# introduction

Vous allez implémenter les 2 algorithmes en vrai et en python. 

Vous vous concentrerez  sur 3 points :

* on veut que notre code soit juste
* on veut pouvoir le modifier/ajouter des fonctionnalités rapidement
* on veut pouvoir partager notre code avec soit-même dans d'autres projet, son équipe ou le monde)

## le projet exponentiation.

suivez le guide.

### crée la structure du projet.

* on crée le projet dans le bon dossier
* on choisi son interpréteur. Nous allons utiliser un `system interpreter` mais libre à vous de faire un environnement virtuel.
* on crée fichier `exponentielle.py` et on met : `print("Bonjour monde !")` dedans
* on crée une configuration pour exécuter notre programme principal et, mentalement, on note le raccourci clavier.

On teste que si l'on exécute la configuration, il y a bien `bonjour monde !` qui s'affiche

### le code

On peut maintenant recopier le code de nos deux méthodes dans `exponentielle.py`. 

```python
def simple(nombre, exposant):
    resultat = 1
    compteur = exposant

    while compteur > 0:
        resultat *= nombre
        compteur -= 1
    return resultat


def rapide(nombre, exposant):
    resultat = 1
    compteur = exposant

    while compteur > 0:
        if compteur % 2 != 0:
            resultat *= nombre
            compteur -= 1
        else:
            nombre *= nombre
            compteur /= 2

    return resultat
```


### les tests

On écrit les tests qui vérifient que ça marche. On pourra ajouter les petits tests effectués lors de la partie analyse du code.

```python

def tests():
    assert simple(2, 0) == 1
    assert simple(2, 1) == 2
    assert simple(2, 4) == 2 ** 4
    assert rapide(2, 0) == 1
    assert rapide(2, 1) == 2
    assert rapide(2, 4) == 2 ** 4
``` 

*Nota Bene* : 

* code et test font parti d'un même ensemble. On ne peut pas avoir du code sans test
* On a l'habitude d'utiliser les commandes [`assert`](https://www.tutorialspoint.com/python3/assertions_in_python.htm) pour les tests.


Vérifiez que les tests *passent* : c'est à dire s'exécutent sans erreurs.

> Pour cela, après avoir copié/collé la fonction on ajoute à notre programme la ligne `tests()` qui va l'exécuter.

Ajoutez une erreur pour voir le programme planter.
Pour l'instant tous os tests doivent être exécutés, et s'il y a une erreur le programme plante à la première erreur : s'il y a plusieurs erreurs, on ne le sais pas.


On verra plus tard comment rendre ce processus automatique. Pour l'instant, on est rassuré, notre code fonctionne.



### le programme principal

Maintenant que l'on est sûr que notre code fonctionne, on peut l'utiliser. Pour cela on a l'habitude de mettre cette utilisation dans  une fonction `main()` qui sera exécutée : c'est notre **programme principal**.

On va créer une boucle de plus en plus grande qui donnera toutes les puissances de 2, calculées de façon simple et de façon rapide.


```python


def main():
    print("simple :")
    for exposant in range(10, 2000):
        print("2 **", exposant,"=", simple(2, exposant))

    print("rapide :")
    for exposant in range(10, 2000):
        print("2 **", exposant,"=", rapide(2, exposant))
```


#### version 2 du code

Une fois la première version du code écrite, on va le regarder et voir ce qui pourrait être améliorer. Ceci est un *skill* qui se travaille. En progressant, vous allez améliorer votre [code smell](https://fr.wikipedia.org/wiki/Code_smell)

Là, on pourrait déjà supprimer les [magic numbers](https://en.wikipedia.org/wiki/Magic_number_(programming)#Unnamed_numerical_constants) pour que changer une variable nous change les exposants pour `simple` et `rapide`


```python


def main():
    liste_exposants = range(2, 2000)

    print("simple :")
    for exposant in liste_exposants:
        print("2 **", exposant, "=", simple(2, exposant))

    print("rapide :")
    for exposant in liste_exposants:
        print("2 **", exposant, "=", rapide(2, exposant))
```

### jouons avec notre code

En changeant les valeurs de la liste on voit que la version simple va bien plus lentement que la version rapide.


## complexité en temps


mesurer le temps c'est pas simple parce que :

* pas seul sur la machine, tous les programme actif s'exécutent souvent en même temps en se [partageant du temps de processeur](https://fr.wikipedia.org/wiki/Temps_partag%C3%A9) 
* python fait des trucs sans nous le dire, comme vérifier de temps en temps que les objets ont tous des noms et les supprimer s'ils n'en ont plus (on appelle ça un [ramasse miette](https://fr.wikipedia.org/wiki/Ramasse-miettes_(informatique)))

Mais pour ce qui nous importe, on va dire que c'est pas grave parce que ça ne prend pas tellement de temps que ça. On va utiliser les fonctions simple du module [time](https://docs.python.org/3/library/time.html). Faisons une petite fonction de test pour voir comment on peut utiliser la mesure du temps dans notre programme.


```python
import time

def test_temps():
    depart = time.time()
    time.sleep(2)  # ne fait rien pendant 2 secondes
    fin = time.time()

    print(fin - depart)  # doit afficher environ 2

test_temps()
``` 

Que donne cette mesure pour nos algorithmes ? Est-ce que `rapide` est bien plus `efficace` que simple ?

```python
def mesure_temps_algorithmes():
    exposant = 200000

    depart = time.time()
    simple(2, exposant)
    end = time.time()

    print("simple", "exposant =", exposant, "temps =", end-depart)

    depart = time.time()
    rapide(2, exposant)
    end = time.time()

    print("rapide", "exposant =", exposant, "temps =", end-depart)

mesure_temps_algorithmes()
``` 


## dessin des complexité

<https://matplotlib.org/> 

On utilise matplotlib pour supperposer les 2 courbes.

C'est peut-être la pire bibliothèque de dessin avec toutes ses options inconsistantes, ces façons de gérer les import folklorique (en tous les pas informaticienne) et ses exemples qui n'en sont pas mais bon si on cherche un pet on peut faire des choses assez jolies.

```python
def main():
    liste_exposants = range(2, 200000, 2000)

    print("simple.")
    temps_simple = []
    for exposant in liste_exposants:
        depart = time.time()
        simple(2, exposant)
        end = time.time()

        delta = (end - depart)
        temps_simple.append(delta)

    print("rapide.")
    temps_rapide = []
    for exposant in liste_exposants:
        depart = time.time()
        rapide(2, exposant)
        end = time.time()

        delta = (end - depart)
        temps_rapide.append(delta)

    matplotlib.pyplot.plot(liste_exposants, temps_simple)
    matplotlib.pyplot.plot(liste_exposants, temps_rapide)
    matplotlib.pyplot.show()
``` 

On voit que la complexité de l'algorithme simple rssemble à ne droite vers la fin et que la complexité de l'algorithme rapide à l'air tout plat en comparaison.

Essayer de ne représenter que le temps de l'algorithme rapide pour voir si cela ressemble à ce que l'on devrait voir.


## code final


*Nota Bene* : L'ordre des import est important pour la lisibilité. On sépare les 3 blocs par des lignes vides.

1. ceux de python
2. les bibliothèque ajoutée mais qui ne sont pas de python (genre matplotlib)
3. les autre fichers de notre projet.


On essaie de respecter la PEP8 au maximum pour avoir un code clair. Pycharm vous aide. Il souligne en jaune les fautes de goûts. Testez le en supprimant aprs une `,` ou en ajoutant des lignes vides un peu partout.


```python

import time

import matplotlib.pyplot


def simple(nombre, exposant):
    resultat = 1
    compteur = exposant

    while compteur > 0:
        resultat *= nombre
        compteur -= 1
    return resultat


def rapide(nombre, exposant):
    resultat = 1
    compteur = exposant

    while compteur > 0:
        if compteur % 2 != 0:
            resultat *= nombre
            compteur -= 1
        else:
            nombre *= nombre
            compteur /= 2

    return resultat


def tests():
    assert simple(2, 0) == 1
    assert simple(2, 1) == 2
    assert simple(2, 4) == 2 ** 4
    assert rapide(2, 0) == 1
    assert rapide(2, 1) == 2
    assert rapide(2, 4) == 2 ** 4


def test_temps():
    depart = time.time()
    time.sleep(2)
    fin = time.time()

    print(fin - depart)


def mesure_temps_algorithmes():
    exposant = 200000

    depart = time.time()
    simple(2, exposant)
    end = time.time()

    print("simple", "exposant =", exposant, "temps =", end-depart)

    depart = time.time()
    rapide(2, exposant)
    end = time.time()

    print("rapide", "exposant =", exposant, "temps =", end-depart)


def main():
    liste_exposants = range(2, 200000, 2000)

    print("simple.")
    temps_simple = []
    for exposant in liste_exposants:
        depart = time.time()
        simple(2, exposant)
        end = time.time()

        delta = (end - depart)
        temps_simple.append(delta)

    print("rapide.")
    temps_rapide = []
    for exposant in liste_exposants:
        depart = time.time()
        rapide(2, exposant)
        end = time.time()

        delta = (end - depart)
        temps_rapide.append(delta)

    matplotlib.pyplot.plot(liste_exposants, temps_simple)
    matplotlib.pyplot.plot(liste_exposants, temps_rapide)
    matplotlib.pyplot.show()

# tests()
# test_temps()
# mesure_temps_algorithmes()


main()

```








