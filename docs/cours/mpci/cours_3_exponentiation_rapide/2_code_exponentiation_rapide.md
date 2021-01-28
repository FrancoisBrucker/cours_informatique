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

* on crée le dossier de notre projet
* On le glisse dans vscode pour que l'éditeur le comprenne.
* on crée un fichier main.py et on vérifie en tapant `print("bonjour monde !")`:   
  * que l'on utilise le bon interpréteur python en exécutnt le programme
  * que le linter est opérationnel

### le code

On crée 2 fichiers :
* `exponentielle.py`
* `test_exponentielle.py`. 

#### exponentielle simple

1. Commencer par créer et tester le code de l'exponentielle simple.
2. Essayer de justifier les tests que vous avez utilisés pour tester votre code :
   * il doit y en avoir asser pour que vous soyez convincu que votre code fonctionne
   * il ne doit pas y en avoir trop (c'est à dire tester plusieurs fos des  choses qui vont faire la même chose dans le code)
3. une fois que le code est opérationnel (dont les tests passent), créer un programme qui demande deux nombres séparés par une virgule à l'utilisateur et rend l'exponentielle de ces nombres.

#### exponentielle rapide

Faites de même avec l'exponentielle rapide.

Votre programme principale va rendre et le résultat obtenu par l'algorithme simple t par l'algorithme rapide (les deux résultats doivent bien sur coïncider...)


### complexité en temps

L'algorithme rapide doit aller bien plus vite de l'algorithme lent. Vous allez essayer de le voir.

#### se rendre compte du problème 

Modifier votre programme principal pour qu'il calcul itérativement toutes les puissances de 2 de $2^1$ à $2^n$ où $n$ est un nombre donné (affecté au début du programme ou donné par un utilisateur).


Ces calculs doivent être fait pour les deux algorithmes : **vous pourrez faire deux fonctions différentes** dans le programme principal et les appeler l'une après l'autre.

Normalement la boucle qui calcule les puissances de 2 pour l'algorithme simple doit aller plus lentement que celle qui calcule toute les puissances de 2 pour l'algorithme rapide.

#### calcul du temps pris

mesurer le temps c'est pas simple parce que :

* pas seul sur la machine, tous les programme actif s'exécutent souvent en même temps en se [partageant du temps de processeur](https://fr.wikipedia.org/wiki/Temps_partag%C3%A9) 
* python fait des trucs sans nous le dire, comme vérifier de temps en temps que les objets ont tous des noms et les supprimer s'ils n'en ont plus (on appelle ça un [ramasse miette](https://fr.wikipedia.org/wiki/Ramasse-miettes_(informatique)))

Mais pour ce qui nous importe, on va dire que c'est pas grave parce que ça ne prend pas tellement de temps que ça. On va utiliser les fonctions simple du module [time](https://docs.python.org/3/library/time.html). Faisons une petite fonction de validation dans un nouveau fichier (que vous pourrez appeler *"expérimentation.py"* par exemple) pour voir comment on peut utiliser la mesure du temps dans notre programme.


```python
import time

def test_temps():
    depart = time.time()
    time.sleep(2)  # ne fait rien pendant 2 secondes
    fin = time.time()

    print(fin - depart)  # doit afficher environ 2

test_temps()
``` 

Adaptez le code ci-dessus pour que notre programme principal donne le temps mis pour faire tous les calculs avec simple et tous les calculs avec rapide.

## On raffine

### temps et complexité

Rendez deux listes : `temps_simple` et `temps_rapide` de longeur 2000 telle que `temps_simple[i]`  (*respectivement* `temps_rapide[i]`)contienne le temps mis par l'algorithme simple (*resp.* rapide) pour calculer $2^i$.

Comparez les deux listes :
* vers quoi doit tendre `temps_simple[i] / temps_rapide[i]` ?
* `log(temps_simple[i]) / temps_rapide[i]` ?

Vérifiez le expérimentalement.


### dessin des complexité

Utilisez [matplotlib](https://matplotlib.org/) pour supperposer les deux listes et voir si l'on obtient bien les courbes théoriques de complexité.
