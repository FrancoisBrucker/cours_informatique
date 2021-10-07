---
layout: page
title:  "Héritage"
category: cours
tags: mie
authors: 
  - François Brucker
  - Célia Châtel
---

Présentation du mécanisme d'héritage qui permettant de factoriser du code entre classes.

## principe de l'héritage

Dans un programme, les classes sont organisées hiérarchiquement, la classe *racine* étant appelé *object*.

![classes héritage]({{ "/assets/cours/developpement/programmation-objet/classes_heritage.png" | relative_url }}){:style="margin: auto;display: block}

Dans la figure précédente :

* la classe **object** est la *racine*
* la classe **1** est la *classe mère* de la classe **2**
* la classe **2** est une *classe fille* de la classe **1**

La figure montre également la désignation UML de l'héritage : une flèche avec un triangle vide.

### utilisation de l'héritage

L'héritage permet d'utiliser les attributs et méthodes créées dans les classes mères de façon simple :

1. soit en cherchant dans la hiérarchie des classes l'attribut ou l'objet appelé depuis une classe fille
2. soit en appelant directement un attribut ou un objet de la classe mère.

#### chercher dans la hiérarchie

Supposons que j'ai un objet de la "classe 2" `obj` qui veut appeler la méthode 1 : `obj.methode1()`

1. on va chercher `methode1` dans l'espace de nom de `obj` : il n'y est pas.
2. on va alors chercher dans sa classe, `classe2` : elle ne définit pas `méthode1`
3. on cherche alors dans la classe mère de classe 2, `classe1` : `méthode1` est définie, on utilise son code.

> si l'on arrive jusqu'à la classe `object` et qu'elle ne contient pas le nom recherché une erreur est lancée.

#### appeler directement

Supposons que dans la définition de `méthode1` de la classe `2'` on particulariser la méthode `méthode1` de la `classe1`. On appelle alors la méthode `méthode1` de la classe 1 dans la définition de la `méthode1` de la classe `2'`.

>si l'on ne retrouve pas la méthode dans la classe mère, on remonte la hiérarchie. De là tenter d'utiliser la méthode `méthode1`  de la classe `1'` en définissant la  méthode `méthode1`  de la classe `2''` va en fait exécuter la méthode  méthode `méthode1`  de la classe `object`

### connaitre la hiérarchie

En python, si l'on veut connaitre l'ordre dans lequel les classes vont être examinée lors de la remontée de la hiérarchie, on peut utiliser la méthode `mro()` des classes. Cette méthode regarde l'attribut `__mro__`.

Par exemple, dans un interpréteur :

```python
>>> str.mro()
[<class 'str'>, <class 'object'>]
>>> str.__mro__
(<class 'str'>, <class 'object'>)
>>> 
```

L'ordre dans lequel est examinée les classe pour les chaines de caractères est donc : d'abord la classe `str` puis la classe `object`

> La classe `object` est toujours le dernier élément de la liste

### quand utiliser l'héritage

La composition et l'agrégation permettent de factoriser des fonctionnalités alors que l'héritage factorise du code. On va donc toujours favoriser la composition à l'héritage si c'est possible.

Il y a cependant des cas où l'héritage est très utile :

* lorsque l'on veut spécifier une classe : la nouvelle classe est un cas particulier de la classe mère**
* lors de l'utilisation de bibliothèques : on particularise à nos besoin une classe générique donnée par un module que l'on a pas écrit.

La règle est que lorsque l'héritage doit re-écrire toutes les méthodes de sa classe mère pour qu'il n'y ait pas de conflit, alors il faut changer d'approche. Une classe et sa classe mère doivent partager beaucoup de méthodes (ou que les méthodes soient des cas particuliers)

### héritage multiple

Python autorise l'[héritage multiple](https://docs.python.org/fr/3/tutorial/classes.html#multiple-inheritance), mais sans très bonne raison il est plus que recommandé de ne pas l'utiliser. Il existe **toujours** une solution utilisant l'héritage simple qui sera plus facile à comprendre et surtout à maintenir dans le temps.

D'ailleurs, certains langages, comme le java ou par exemple, interdisent carrément l'héritage multiple.

> Si cela vous intéresse, python utilise la règle [de linéarisation C3](https://en.wikipedia.org/wiki/C3_linearization) pour réaliser l'ordre de priorité des classes (le mro), ceci permet de résoudre le [problème du diamant](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_diamant) en héritage multiple.

## Exemple 1 : héritage simple

On présente ici un premier exemple d'utilisation de l'héritage, en combinaison d'une composition.

On veut manipuler des polygones. On veut pouvoir :

* créer un polygone à partir d'une liste de sommets donnée
* calculer l'aire du polygone
* calculer le périmètre du polygone

### classes Point et Polygone

Pour cela, on va créer une classe `Point` et une classe `Polygone` :

* classe `Point` :
  * on se restreint à la 2D
  * coordonnées cartésiennes
  * distance à un autre point pour pouvoir plus facilement calculer le périmètre ensuite
* classe `Polygone` :
  * création avec une liste de Point
  * calcul du périmètre
  * calcul de l'aire

On va supposer que le [polygone est simple](https://fr.wikipedia.org/wiki/Polygone_simple) pour simplifier le calcul de l'aire...

#### uml

Point et polygone entretiennent un lien d'agrégation (les points sont passé au polygone à sa construction). Le modèle UML suivant :

![point polygone]({{ "/assets/cours/developpement/programmation-objet/heritage_point_poly.png" | relative_url }}){:style="margin: auto;display: block}

#### code python

On peut alors avoir le code python suivant pour créer les classes :

```python
from math import sqrt


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self):
        self._y = y

    def distance(self, other):
        x1 = self.get_x()
        x2 = other.get_x()

        y1 = self.get_y()
        y2 = other.get_y()

        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


class Polygone:
    def __init__(self, points):
        self._points = tuple(points)

    def périmètre(self):
        d = 0
        pivot = self._points[0]
        for point in self._points[1:]:
            d += pivot.distance(point)
            pivot = point
        d += pivot.distance(self._points[0])

        return d

    def aire(self):
        a = 0
        pivot = self._points[0]
        for point in self._points[1:]:
            a += pivot.get_x() * point.get_y() - pivot.get_y() * point.get_x()
            pivot = point

        point = self._points[0]
        a += pivot.get_x() * point.get_y() - pivot.get_y() * point.get_x()

        return 0.5 * abs(a)

```

> On a rendu les attributs des classes privé. La convention en python pour rendre un attribut privé est de lui coller un `_` avant son nom.

Remarques :

1. Remarquez que l'on utiliser toujours les méthodes (si elles existent) pour accéder aux attributs, cela permettra si besoin de changer les attributs de la classes (passer en coordonnées polaires par exemple) sans changer le code des méthodes.
2. Pour la classe polygone, on recrée une liste de points pour être sur que le nombre de points reste constant (la liste est passée en paramètre et peut donc être modifiées à 'extérieur de la classe)
3. Notez que l'on ne recrée pas les points, ils peuvent donc changer car ils sont passés en paramètre de la construction du polygone

On peut tester le code avec, par exemple :

```python
points = [Point(0, 0), Point(0, 2), Point(1, 2), Point(1, 0)]
polygone = Polygone(points)
print(polygone.périmètre())
print(polygone.aire())
```

### un polygone particulier

Comment modéliser une classe triangle ?

Comme un triangle **est un** polygone simple, on peut utiliser l'héritage pour cela.

#### modélisation UML

Elle est très simple :

![triangle]({{ "/assets/cours/developpement/programmation-objet/heritage_triangle.png" | relative_url }}){:style="margin: auto;display: block}

Notez que pour l'héritage, on ne remet pas les attributs/méthodes définis dans les classes mères.

#### code python du Triangle

La classe `Triangle` hérite de `Polygon`, on appelle donc le constructeur de ce dernier lors de la création d'un `Triangle`.

Ceci est explicite en python :

```python
class Triangle(Polygone):
    def __init__(self, point1, point2, point3):
        super().__init__([point1, point2, point3])
```

Le mot clé `super()` désigne la classe parente, ici `Polygone`. Ce mot clé permet d'utiliser toutes les méthodes de la classe parente, ici `__init__`. Remarquez que l'on utilise la méthode `__init__` sans utiliser le premier paramètre (`self`) qui est implicitement l'objet courant.

Si on regarde l'ordre dans lequel est examiné les espaces de nom, on a (c'est la commande `Triangle.mro()`) :

```python
[<class '__main__.Triangle'>, <class '__main__.Polygone'>, <class 'object'>]
```

> Un petit tuto sur [la fonction super](https://he-arc.github.io/livre-python/super/index.html )

On peut maintenant utiliser toutes les méthodes définies dans Polygone puisque le constructeur de `Triangle` appelle directement le constructeur de `Polygone` : à la fin du constructeur, il existera une liste de points dans le triangle.

```python
    triangle = Triangle(Point(0, 0), Point(1, 1), Point(2, 0))
    print(triangle.périmètre())
    print(triangle.aire())
```

Pour trouver le périmètre, python fonctionne ainsi :

1. existe-t-il un nom `périmètre` dans l'objet `triangle` : NON
2. existe-t-il un nom `périmètre` dans la classe de l'objet `triangle`, `Triangle` : NON
3. existe-t-il un nom `périmètre` dans la classe mère de `Triangle`, `Polygone` : OUI

Une fois la méthode trouvée, on l'exécute en plaçant l'objet (ici notre `triangle` en 1er paramètre, c'est à dire `self` de la méthode `périmètre` définie dans `Polygone`).

## Exemple 2 : donjons et dragons

On va simuler des personnage d'*heroic fantasy*. Pour cela, on commence par créer une classe `Personnage` qui sera particularisée petit à petit.

### classe Personnage

Le personnage générique doit :

* avoir un score d'attaque
* avoir des points de vie
* pouvoir modifier son score d'ataque et ses points de vie
* taper un autre personnage (lui faire perdre un nombre de point de vie égale à son score d'attaque)
* se faire taper par un autre personnage

#### UML du personnage

![personnage]({{ "/assets/cours/developpement/programmation-objet/heritage_personnage.png" | relative_url }}){:style="margin: auto;display: block}

#### code python du personnage

On a décidé ici de ne pas mettre de méthode get et set, mais de laisser libre accès aux attributs. C'est un choix possible. L'UML dérive donc un peut du code python ce qui est normal, chaque langage ayant ses spécificités.

```python
class Personnage:
    def __init__(self, vie, attaque):
        self.vie = vie
        self.attaque = attaque

    def se_faire_taper(self, personnage):
        self.vie -= personnage.get_attaque()

    def taper(self, personnage):
        personnage.se_faire_taper(self)
```

Voyez comment on a utilisé la méthode `se_faire_taper` pour définir la méthode `taper`.

### la classe guerrière

La guerrière dispose d'un score de bloquage qui représente son pourcentage de chances de ne pas perdre de vie quand un autre personnage l'attaque.

#### modèle UML de la guerrière

c'est un personnage, on peut donc utiliser l'héritage.



#### code python de la guerrière

On ajoute la guerrière :

![guerriere]({{ "img/guerriere.png"}})

On donne ci-après une partie du code de la guerrière  (on a en particulier pas écrit la méthode `bloque` qui fait le tirage pour savoir si on bloque ou pas). Faites attention et comprenez bien : 

  -  l'appel à `super().__init__()` au début du constructeur de la classe fille,
  - qu'on ajoute un attribut à la guerrière par rapport au personnage normal,
  - la méthode `se_faire_taper(personnage)` utilise la méthode `se_faire_taper` de la classe `Personnage` seulement si la guerrière ne bloque pas le coup. Le `super().methode_de_la_mere()` permet d'accéder à la méthode de la classe mère même de même nom qu'une méthode (différente) de la classe fille.


~~~ python
class Guerriere(Personnage):
    def __init__(self, vie, attaque, blocage):
        super().__init__(vie, attaque)
        self.blocage = blocage

    def se_faire_taper(self, personnage):
        if not self.bloque(personnage):
            super().se_faire_taper(personnage)
~~~

Prenez le temps de faire des exemples d'utilisation et de vérifier que tous les cas marchent. En particulier qu'est-ce qui est appelé quand on fait `guerriere.se_faire_taper(bonhomme)` avec un objet `guerriere` de la classe `Guerriere` ?


### le magicien

Le magicien peut faire tout ce que peut faire un personnage normal mais il dispose en plus d'un score d'attaque magique qui détermine les dégâts qu'il fait en lançant un sort. Modéliser la classe \texttt{Magicien}.

Le magicien permet de montrer l'ajout d'une méthode qui n'était pas du tout dans la classe mère :

![magicien]({{ "img/magicien.png"}})

Le code n'est pas difficile, on se passera donc de l'écrire complètement. Il faut :

  - ajouter une méthode `lancer_sort`
  - ajouter un paramètre et son attribut associé `attaque_magique` au constructeur
  - ajouter une méthode `se_faire_toucher_par_un_sort(magicien)` avec un paramètre de type Magicien dans la classe Personnage.

> **Nota Bene :** Ces exemples sur l'héritage sont un peu forcés. C'est parce que l'héritage n'est que très peu utilisé en code pure. Il est même considéré comme préjudiciable dans la plupart des cas (voir )[là](https://codeburst.io/inheritance-is-evil-stop-using-it-6c4f1caf5117) ou encore [là](http://neethack.com/2017/04/Why-inheritance-is-bad/)). 
> >Un cas d'utilisation reconnu est cependant lorsque l'on veut utiliser des classes définies dans un module quelconque et la mettre un peu à notre sauce. Comme dans des bibliothèques graphiques par exemple.



## odds and ends

### héritage de méthodes

Écrivez une classe `A` qui a :

 - un attribut `a`
 - une méthode `truc_que_fait_a()` qui affiche "Truc défini dans la classe mère"
 - une méthode `autre_truc()` qui affiche "Autre truc dans la classe mère"

Écrivez une classe `B` qui hérite de A et qui a :

 - un attribut `b`
 - le constructeur à 2 paramètres, un qui est initialisé dans la classe A, l'autre initialisé dans B
 - une méthode `autre_truc()` qui affiche "C'est mon autre truc à moi"
 - une méthode `que_de_b()` qui affiche "Méthode seulement de la classe fille"

Faites bien attention à utiliser proprement le mot-clé `super` dans le constructeur de la classe fille.

Créez un objet `objet_a` de la classe `A` et un objet `objet_b` de la classe `B`. Essayez les lignes suivantes (une à la
fois) et prenez le temps de comprendre ce qu'elles font et pourquoi.

~~~ python
print(objet_a.a)
print(objet_a.b)
print(objet_b.a)
print(objet_b.b)
objet_a.truc_que_fait_a()
objet_a.autre_truc()
objet_a.que_de_b()
objet_b.truc_que_fait_a()
objet_b.autre_truc()
objet_b.que_de_b()
~~~


### combinaison de méthodes

Ajoutez :

  - dans la  classe `A` : une méthode `j_herite(x)` qui prend un paramètre `x` qui est une chaine de caractère et affiche la valeur de x
  - dans la  classe `B` : une méthode `j_herite(x)` qui commence par appeler la méthode de la classe mère puis affiche la valeur de x en majuscules

Vérifiez que tout se passe comme prévu.

### attributs de classes

tbd
