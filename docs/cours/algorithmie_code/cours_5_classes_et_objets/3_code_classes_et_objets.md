---
layout: page
title:  "code : classes et objets"
category: cours
tags: informatique cours 
author: "François Brucker"
---

## Introduction

Classes et objets, le code !

On va essayer de vous montrer ici le mantra vrai en code et en développement : **Make it work. Make it right. Make it fast** (dans cet ordre).

Il signifie que l'on commence par mettre en place l'algorithme le code, puis grâce aux tests qui nous assurent qu'il fonctionne, on peut l'améliorer sans risquer de tout casser (les tests doivent toujours continuer de fonctionner). Enfin, on optimise sa vitesse en mesurant les temps de fonctionnement et en agissant sur les parties lentes (on ne le fera pas ici).

## Dice

### Un dé tout simple

Implémentez la première version de la classe `Dice` vue dans la séance tableau dans un fichier nommé *dice.py*. Elle doit être capable de :

* créer un objet sans paramètre
* créer un objet avec une position initiale
* connaître et changer la position du dé
* lancer le dé

Pour vérifier que votre code fait ce qu'on lui demande, vous devez créer un fichier *main.py* et essayez de :

* de créer un objet sans argument et de vérifier dans quelle position il est
* de créer un objet en choisissant sa position et de vérifier sa position,
* de modifier la position d'un dé créé et de vérifier qu'elle a bien été changée,
* de lancer le dé et de vérifier que sa position est toujours cohérente avec le nombre de faces.

Convertissez ces essais en tests dans un fichier *tests_dice.py*. Ce fichier vous assure que votre classe fonctionne et que l'on peut maintenant essayer de l'adapter.

### Un dé pipé

Nous allons maintenant améliorer notre dé avec la deuxième version de la classe vue en TD : le dé pipé. Il faudra donc ajouter un nouvel attribut permettant de renseigner les probabilités de chaque face. On ajoutera ces probabilités en paramètre optionnel à l'initialisation du dé et sous forme de *setter/getter*.

Pour l'initialisation, ajoutez cet attribut et essayez de créer un nouveau dé en utilisant ce paramètre.

Modifiez la méthode `roll` pour prendre en compte les probabilités. Pour lancer le dé au hasard en respectant les probabilités voulues, vous pouvez utiliser `numpy.random.choice`. Regardez la [doc](https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html) pour savoir comment l'utiliser et avec quels paramètres.

> **Nota Bene :**
>Pour utiliser numpy, vous devez l'importer en haut de votre fichier avec `import numpy`.

Comme tout à l'heure, vérifiez que vos nouvelles fonctionnalités fonctionnent (en adaptant le fichier *main.py*), puis transformez ces essaies en tests:

* créer un dé avec une distribution de probabilités particulière,
* changer la distribution de probabilités d'un dé,
* lancer un dé pipé en vérifiant qu'il suit (à peu près) la loi de probabilités donnée.

> **Remarque :** Il est important que le programme principal, même s'il n'est pas un programme utilisable et ne fait que montrer les fonctionnalités codées "raconte une histoire". On doit montrer que ces fonctionnalités peuvent être utile dans un cas d'usage : on parle de [user stories](https://fr.wikipedia.org/wiki/R%C3%A9cit_utilisateur).

## Pour aller plus loin

Python dispose de méthodes spéciales qui peuvent être invoquées en utilisant une syntaxe particulière (par exemple les
opérations arithmétiques `+, -, *, \` entre objets que nous avons créés nous-mêmes). Vous en trouverez une liste
exhaustive sur la [doc officielle](https://docs.python.org/3/reference/datamodel.html#special-method-names). Nous allons
en utiliser ici quelques-unes sur notre classe. Ces méthodes se présentent toujours sous la forme `__nom_de_la_methode__`.

Essayez de taper :

```python
d = Dice()
print(d)
```

Vous devriez obtenir quelque chose comme :

```python
<dice.Dice object at 0x7f40e518a668>
```

Le `print` appelle la méthode `__str__` de notre classe. Nous ne l'avons pas définie, c'est donc la méthode par défaut de tous les objets python qui est appelée. Comme vous le constatez, elle n'est pas très intéressante pour nous. Il faut donc la définir dans notre classe.

Définissez une méthode permettant d'écrire le dé comme une chaîne de caractères sous la forme `"Dice(position=1,
probabilities=[1, 0, 0, 0, 0, 0])"` et vérifiez qu'elle fonctionne.

On voudrait également pouvoir vérifier si un dé a fait un meilleur lancer qu'un autre en faisant tout simplement :

```python
d1 = Dice(1)
d2 = Dice(6)
d1 < d2
```

Si vous testez ça avec votre code tel qu'il est, vous obtiendrez :

```python
TypeError: '<' not supported between instances of 'Dice' and 'Dice'
```

Python vous explique qu'il ne connaît pas l'opérateur `<` pour les objets de notre classe. Pour pouvoir utiliser
directement les opérateurs `<` et `>`, il faut définir respectivement les méthodes `__lt__(self, other)` et
`__gt__(self, other)`. On pourra aussi ajouter `__eq__(self, other)` pour tester l'égalité.

Ajoutez les méthodes `__lt__`, `__gt__` et `__eq__` et testez les.
