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

Supposons que j'ai un objet de la "classe 2" `o` qui veut appeler la méthode 1 : `o.methode1()`

1. on va chercher `methode1` dans l'espace de nom de `o` : il n'y est pas.
2. on va alors chercher dans sa classe, `classe2` : elle ne définit pas `méthode1`
3. on cherche alors dans la classe mère de classe 2, `classe1` : `méthode1` est définie, on utilise son code.

> si l'on arrive jusqu'à la classe `object` et qu'elle ne contient pas le nom recherché une erreur est lancée.

#### appeler directement

Supposons que dans la définition de `méthode1` de la classe `2'` on particulariser la méthode `méthode1` de la `classe1`. On appelle alors la méthode `méthode1` de la classe 1 dans la définition de la `méthode1` de la classe `2'`.

>si l'on ne retrouve pas la méthode dans la classe mère, on remonte la hiérarchie. De là tenter d'utiliser la méthode `méthode1`  de la classe `1'` en définissant la  méthode `méthode1`  de la classe `2''` va en fait exécuter la méthode  méthode `méthode1`  de la classe `object`

méthode 1 de classe 1 qui appelle méthode 1 de object

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

> La classe object est toujours le dernier élément de la liste

### quand utiliser l'héritage

La composition et l'agrégation permettent de factoriser des fonctionnalités alors que l'héritage factorise du code. On va donc toujours favoriser la composition à l'héritage si c'est possible.

Il y a cependant des cas où l'héritage est très utile :

* lorsque l'on veut spécifier une classe (un cas particulier)
* lors de l'utilisation de bibliothèques

La règle est que lorsque l'héritage doit re-écrire toutes les méthodes de sa classe mère pour qu'il n'y ait pas de conflit, alors il faut changer d'approche. Une classe et sa classe mère doivent partager beaucoup de méthodes (ou que les méthodes soient des cas particuliers)

### héritage multiple

Python autorise l'[héritage multiple](https://docs.python.org/fr/3/tutorial/classes.html#multiple-inheritance)

Règle du diamant en python mais, sans une très bonne raison, **il ne faut pas l'utiliser** dans nos propre programme, car ça le rend trop confus.

Certains langages, comme le java ou par exemple, interdisent carrément l'héritage multiple.

## Exercice 1

L'idée est juste de présenter avec quelque chose de simple et facile à se représenter la notion d'héritage. On donnera l'UML des classes dans tous les cas et le code seulement s'il est lié à l'héritage.

Classe `Point` :

![point]({{ "img/point.png"}})

Rien de particulier, pour la classe `Polygon` qui est une agrégation avec points :

![polygon]({{ "img/polygon.png"}})

C'est bien une agrégation puisque utilise des objets `Point` comme attribut mais ces points existent indépendamment du polygone et on les ajoute dans l'attribut `vertices` lors de la création de l'objet.

Classe `Triangle`:

![triangle]({{"img/triangle.png"}})

L'héritage arrive ici. On fait une version restreinte du polygone très simple. La classe `Triangle` hérite de `Polygon`, on appelle donc le constructeur de ce dernier lors de la création d'un `Triangle`.

Ceci est explicite en python :


~~~ python
class Triangle(Polygon):
  def __init__(self, point1, point2, point3):
    super().__init__([point1, point2, point3])
~~~

Le mot clé `super()` désigne la classe parente, ici `Polygon`.Ce mot clé permet d'utiliser toutes les méthodes de la classe parente, ici `__init__`. Remarquez que l'on utilise la méthode `__init__` sans utiliser le premier paramètre (`self`) qui est implicitement l'objet courant. 

L'UML complet donne donc :

![polygone_uml_entier]({{ "img/polygone_uml_entier.png" }})

> TBD
> ajouter appelle à __str__ comme recherche pure d'une classe dans la hiérarchie
> ajouter cercle inscrit. en paramètre


### Exercice 2

La classe `Personnage` ne pose normalement pas de problèmes :

![personnage]({{ "img/personnage.png" }})

On précise le code de `taper` et `se_faire_taper` qui permet à chacun de se faire taper comme il l'entend :


~~~ python
def taper(self, personnage):
    personnage.se_faire_taper(self)

def se_faire_taper(self, personnage):
    self.set_vie(self.get_vie() - personnage.get_attaque())
~~~


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

Le magicien permet de montrer l'ajout d'une méthode qui n'était pas du tout dans la classe mère :

![magicien]({{ "img/magicien.png"}})

Le code n'est pas difficile, on se passera donc de l'écrire complètement. Il faut :

  - ajouter une méthode `lancer_sort`
  - ajouter un paramètre et son attribut associé `attaque_magique` au constructeur
  - ajouter une méthode `se_faire_toucher_par_un_sort(magicien)` avec un paramètre de type Magicien dans la classe Personnage.

> **Nota Bene :** Ces exemples sur l'héritage sont un peu forcés. C'est parce que l'héritage n'est que très peu utilisé en code pure. Il est même considéré comme préjudiciable dans la plupart des cas (voir )[là](https://codeburst.io/inheritance-is-evil-stop-using-it-6c4f1caf5117) ou encore [là](http://neethack.com/2017/04/Why-inheritance-is-bad/)). 
> >Un cas d'utilisation reconnu est cependant lorsque l'on veut utiliser des classes définies dans un module quelconque et la mettre un peu à notre sauce. Comme dans des bibliothèques graphiques par exemple.

## points de vigilance

Toujours très aimé mais l'intérêt est plus réduit qu'on ne peu le penser. Avant de faire de l'héritage regardez si une composition et un agrégation ne feraient pas mieux le travail.


attention : aux variable de la classe qui ne doivent pas être redéfini dans l'héritage (mais on ne sais pas lesquelles c'est...)
En python `__variable`  n'est pas passée aux descendants.

Si l'on redéfini toutes les classes de la classe mere sans les utililser : pas un bon signe.

héritage multiple autorisé en python, mais c'est très compliqué. règle de u diamant : c'est fait pour simplifier le code pas le rendre necore plus compliqué.


## variables de classe

parler des variables de classes. 

