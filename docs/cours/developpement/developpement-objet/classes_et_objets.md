---
layout: page
title:  "Classes et objets"
author: "François Brucker"
---


## But

On va voir dans cette séance les notions de classe, d'objet, d'attribut et de méthode.

> **Elements de corrigé :** Ils sont disponibles [là]({% link cours/developpement/developpement-objet/classes_et_objets_corrige.md %}). Cependant, ils ne dispensent pas d'aller en cours, c'est une aide à la compréhension.

## Séance tableau

Le [sujet au format pdf]({{ "ressources/TD_1_impression.pdf" }}).

## Séance code

> **Warning :** On suppose que vous avez tous fait du python dans votre vie. Si ce n'est pas le cas, faites quelques tutos pour vous mettre en jambe.

### Dice
#### Un dé tout simple

Implémentez la première version de la classe `Dice` vue dans le TD1 dans un fichier nommé *dice.py*. Elle doit être capable de :

  - créer un objet sans paramètre
  - créer un objet avec une position initiale
  - connaître et changer la position du dé
  - lancer le dé

Pour vérifier que votre code fait ce qu'on lui demande, vous devez créer un fichier de tests *essai_dice.py* pour
essayer votre classe. Prenez le temps d'essayer :

  - de créer un objet sans argument et de vérifier dans quelle position il est,
  - de créer un objet en choisissant sa position et de vérifier sa position,
  - de modifier la position d'un dé créé et de vérifier qu'elle a bien été changée,
  - de lancer le dé et de vérifier que sa position est toujours cohérente avec le nombre de faces.

#### Un dé pipé

Nous allons maintenant améliorer notre dé avec la deuxième version de la classe vue en TD : le dé pipé. Il faudra donc ajouter un nouvel attribut permettant de renseigner les probabilités de chaque face. On ajoutera ces probabilités en paramètre optionnel à l'initialisation du dé et sous forme de *setter/getter*.


Pour l'initialisation, ajoutez cet attribut et essayez de créer un nouveau dé en utilisant ce paramètre.

Modifiez la méthode `roll` pour prendre en compte les probabilités. Pour lancer le dé au hasard en respectant les probabilités voulues, vous pouvez utiliser `numpy.random.choice`. Regardez la [doc](https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html) pour savoir comment l'utiliser et avec quels paramètres.

> **Nota Bene :**
>Pour utiliser numpy, vous devez l'importer en haut de votre fichier avec `import numpy`.


Essayez les nouvelles fonctionnalités:

  - créer un dé avec une distribution de probabilités particulière,
  - changer la distribution de probabilités d'un dé,
  - lancer un dé pipé en vérifiant qu'il suit (à peu près) la loi de probabilités donnée.

### Pour aller plus loin

Python dispose de méthodes spéciales qui peuvent être invoquées en utilisant une syntaxe particulière (par exemple les
opérations arithmétiques `+, -, *, \` entre objets que nous avons créés nous-mêmes). Vous en trouverez une liste
exhaustive sur la [doc officielle](https://docs.python.org/3/reference/datamodel.html#special-method-names). Nous allons
en utiliser ici quelques-unes sur notre classe. Ces méthodes se présentent toujours sous la forme `__nom_de_la_methode__`.


Essayez de taper :

~~~ python
d = Dice()
print(d)
~~~

Vous devriez obtenir quelque chose comme :

~~~ python
<dice.Dice object at 0x7f40e518a668>
~~~

Le `print` appelle la méthode `__str__` de notre classe. Nous ne l'avons pas définie, c'est donc la méthode par défaut de tous les objets python qui est appelée. Comme vous le constatez, elle n'est pas très intéressante pour nous. Il faut donc la définir dans notre classe.

Définissez une méthode permettant d'écrire le dé comme une chaîne de caractères sous la forme `"Dice(position=1,
probabilities=[1, 0, 0, 0, 0, 0])"` et vérifiez qu'elle fonctionne.

On voudrait également pouvoir vérifier si un dé a fait un meilleur lancer qu'un autre en faisant tout simplement :

~~~ python
d1 = Dice(1)
d2 = Dice(6)
d1 < d2
~~~

Si vous testez ça avec votre code tel qu'il est, vous obtiendrez :

~~~ python
TypeError: '<' not supported between instances of 'Dice' and 'Dice'
~~~

Python vous explique qu'il ne connaît pas l'opérateur `<` pour les objets de notre classe. Pour pouvoir utiliser
directement les opérateurs `<` et `>`, il faut définir respectivement les méthodes `__lt__(self, other)` et
`__gt__(self, other)`. On pourra aussi ajouter `__eq__(self, other)` pour tester l'égalité.

Ajoutez les méthodes `__lt__`, `__gt__` et `__eq__` et testez les.

