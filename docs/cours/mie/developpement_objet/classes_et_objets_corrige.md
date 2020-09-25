---
layout: page
title:  "Classes et objets élémnts de corrigé"
category: cours
tags: mie corrigé
---


## But

Eléments de corrigé de la séance  [Classes et objets]({% link cours/mie/developpement_objet/classes_et_objets.md %}).

## Elements de cours

Cette partie donne des liens et quelques guides sur les notions vues dans la *séance tableau*. Vous pouvez commencer directement par le corrigé de cette dernière et revenir ici si vous cherchez des compléments.

### classes, objet

Le but de la programmation objet n'est pas d'utiliser des concepts fumeux (classes abstraites, encapsulation et polymorphismes) mais d'écrire du code :

  - facile à lire
  - maintenable
  - facile à étendre en ajoutant des fonctionnalités
  
Si un concept objet va à l'encontre de ce principe dans votre programme **NE L'UTILISEZ PAS**. C'est souvent vrai pour l'héritage qui n'a d'utilité que dans des cas très précis...

Un objet est un bout de code auquel est associé :

  - des fonctionnalités (des méthdoes) qui sont communes à tous els objets de sa classe
  - des choses à lui tout seul (des attributs) qui lui permettent de se différentier des autres objets de sa classe même s'il a les fonctionnalités. 

Donc lorsque l'on crée un objet on crée le framework de tous les objets similaire : sa classe. Python utilise les *namespaces* (espaces de noms) pour savoir ce qui est appelé comme objet/méthode et ainsi utiliser le même code pour plusieurs objets.

### uml

[un tuto uml](https://www.sparxsystems.fr/resources/tutorials/uml/datamodel.html).

L'uml peut être très compliqué. Nous allons uniquement l'utiliser ici comme une représentation synthétique d'une classe/objet. Vous le verrez dans les exemples ci-dessous mais, en gros, une classe en uml c'est : 

~~~
-----------------------
| Nom de la Classe    |
|---------------------|
| Attributs : propre  |
| à chaque objet      |
|---------------------|
| méthodes : commun   |
| à tous les objets   |
-----------------------
~~~

  - Pour chaque attribut on pourra préciser le *type* (entier, chaine de caractère, une classe particulière d'objet, ...) si c'est important
  - pour chaque méthode on donnera sa [signature](https://developer.mozilla.org/fr/docs/Glossaire/Signature/Fonction) complète (son nom et ses paramètres) pour que l'on puisse l'utiliser.


### python

En python, beaucoup de choses sont des [conventions](https://en.wikipedia.org/wiki/Convention_over_configuration) (variable privée, premier nom est self, ...) mais tout le monde s'y tient car la lecture du code en devient aisée.

#### variables spéciales

En regardant du code python, vous allez voir beaucoup de noms qui commencent par des `_`. Ils sont une signification spéciale en python :

  - qui commencent par `_` : non public (c'est en fait une convention)
  - qui commencent par `__` : privé (non disponibles pour les descendants)
  - qui commencent et finissent par `__` : méthodes spécifiques de python qui ont un sens (par exemple __str__, __eq__), elles sont utilisées dans des cas précis et documentés.


#### namespaces 

La gestion des noms en python se fait via des [espaces de noms](http://sebastianraschka.com/Articles/2014_python_scope_and_namespaces.html). L'ordre dans lequel ces noms sons cherché pour être associé à un objet est logique et se règle en sachant quel namespace est utilisé. Les namespaces possibles sont rappelés plus bas dans la
  correction de l'exercice dédié.

#### Gestion des attributs 

L'usage courant est de déclarer tous les attributs d'un objets dans son *constructeur* qui est la méthode `__init__`. Cela permet de voir d'un seul coup d'oeil les attributs spécifiques aux objets d'une classe donnée.


Attentions aux attributs de classes (self.attribut != Class.attribut). L'ordre d'évaluation de python est de regarder d'abord  dans l'objet puis dans sa classe (les méthodes s'y trouvent par exemple) :

  - les attributs de classes s'écrivent comme des méthodes (ils se placent, comme les méthodes, dans le namespace de la classe)
  - `Class.attribute` masqué par `self.attribute` si existe car le namespace de l'objet est vu avant celui de la classe).


### Ressources 

Divers tutos sur le net pour aborder les notions objet/python utilisées cette séance

#### Python général

  - le [tuto python](https://informatique.centrale-marseille.fr/tutos/post/python-bases.html) et le [tuto officiel](https://docs.python.org/3/tutorial/index.html). Vous êtes sencé connaître tout ça (vu en prépa ou avant)
  - la [PEP8](https://www.python.org/dev/peps/pep-0008)


#### Classes et objets

  - le [tuto python sur les classes](https://docs.python.org/3/tutorial/classes.html). Ce cours est là pour vous montrer tout ce qu'il y a dedans, à part (peut-être) la partie sur l'héritage et les itérateurs
  - [Sam & Max](http://sametmax.com/le-guide-ultime-et-definitif-sur-la-programmation-orientee-objet-en-python-a-lusage-des-debutants-qui-sont-rassures-par-les-textes-detailles-qui-prennent-le-temps-de-tout-expliquer-partie-1/) : l'objet d'un point de vue python. Sans philosophie, juste vue comme un moyen d'écrire du code. J'aime. Attention cependant, sam&max est parfois un peu NSFW (je vous aurais prévenu)...
  

#### Quelques concepts utiles et importants en python 

  - les [arguments par défaut](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values)
  - les [namespaces](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)


## Séance tableau

### ressources 

[Les sources tex du sujet]({{ "ressources/TD_1.tex" }})


### Un compteur

Le premier exemple est très simple pour permettre d'introduire dans un premier temps l'UML, de regarder des exemples de
code utilisant l'objet et enfin de montrer le code en python de la classe en elle-même.

L'idée est tout d'abord de montrer qu'un objet est un ensemble de fonctionnalités récurrente dans un programme. Ici un
compteur. Les fonctionnalités sont : 

  - ajouter une unité à un compteur
  - connaître la valeur du compteur.


Commencez par écrire le code d'utilisation du TD. Puis à côté sur le tableau créez le diagramme UML permettant d'exécuter le code. Regardez  qui peut être vu comme une utilisation de la classe (c'est les méthodes) et de là ce qu'il est nécessaire de stocker dans les objets pour qu'ils puissent fonctionner (ici garder la trace d'un compteur). 

De là, donnez tout le code de la classe python au tableau à côté des deux autres formes (UML et utilisation). Comprenez le lien entre UML et code python, puis comment tout ça mache ensemble en exécutant à la main le code d'utilisation (on suivra le déroulement précis de chaque instruction.)


#### UML

Pour que l'on puisse avoir plusieurs compteurs (si on n'a qu'un seul compteur, ce n'est pas la peine de faire des objets), il faut que chaque compteur ait une valeur à lui.

On a donc ce qu'il faut pour notre classe : 

 - un nom : Counter
 - des méthodes (= fonctionnalités = ce qui est pareil pour tous les objets) : `count` et `get_value`
 - un attribut (= ce qui est différent pour chaque objet) : `value`

Diagramme UML du compteur :
![counter]({{ "img/counter_init.png"}})


> **Nota Bene :** On a utilisé ici un `_` en début de nom de la variable `value` pour signifier qu'elle est *privée*, c'est à dire que personne d'autre n'a le droit de l'utiliser à part l'objet. Cette convention n'est pas indispensable à utiliser car il est parfois un peut flou de savoir si telle ou telle attribut et *privé* ou *publique*...


#### Python

En python, tout peut être vu comme un *namespace* particulier, un endroit où sont rangés des noms : noms de variables, de fonctions, de classes, etc.

Les namespaces possibles sont :

  - le namespace global
  - la classe, ici `Counter`. Contient tout ce qui est défini dans la classe comme les méthodes ou les constantes.
  - l'objet : ici un objet counter de la classe `Counter`. Contient tout ce qui est défini pour l'objet en particulier (par exemple dans le `__init__` quand l'objet est appelé self)
  - les méthodes : ce qui n'existe que de l'exécution de la méthode à la fin de son exécution


Plusieurs namespaces peuvent cohabiter en même temps, pour connaître celui qui va être utilisé, python va du [local au global](http://sebastianraschka.com/Articles/2014_python_scope_and_namespaces.html). S'il n'y a pas d'inclusion (comme une fonction dans une fonction), cela donne :

  1. fonction (inclut les méthodes)
  2. objet
  3. classe
  5. global
  5. built-in (les mots du langage python comme `list` ou encore `range`)

S'il y a inclusion de namespaces, on suit la règle [LEGB](http://sebastianraschka.com/Articles/2014_python_scope_and_namespaces.html#3-legb---local-enclosed-global-built-in)

Pour les exemples :

  - `from counter import Counter` : cherche un fichier *"counter.py"* dans le répertoire courant. L'exécute avec son propre namespace. Prend ensuite le nom `Counter` dans *counter.py* et l'ajoute au namespace global. On peut donc utiliser le nom `Counter` qui est défini dans le namespace de *counter.py*
  - `c1 = Counter()` : 
      - en informatique `=` n'est pas symétrique. A gauche un nom à droite un objet. Ici ceci signifie que l'on ajoute le nom `c1` au namespace global et que sa valeur sera le résultat de `Counter()`
      - `Counter()` : est le résultat de l'exécution du nom `Counter`. Les parenthèses (et les paramètres éventuels) après un nom l'exécute. On aurait pu tout à fait écrire `c1 = Counter` on aurait alors eu un nom counter qui sera égal à la classe Counter. 
      - `Counter` est dans le namespace global grâce à la ligne précédente. Exécuter une classe revient à : 
           - créer un namespace vierge
           - chercher la méthode `__init__` de la classe et l'exécuter en passant le nouveau namespace en premier paramètre :
               - pour exécuter une fonction on crée un namespace pour elle.
               - on place le nom `self` qui vaut ici le nouveau namespace créé
               - la première ligne crée le nom `value` dans le namespace nommé `self`
               - la fonction étant terminée, on supprime le namespace de la fonction (qui contenait le nom `self`)
               - on rend l'objet
      - l'objet (qu'on peut assimiler au namespace) créé est associer au nom `c1`
  - `c1.count()` : python cherche le nom `count`. Il regarde d'abord dans l'objet de nom `c1`. Ça n'y est pas. Il regarde donc au dessus : dans le namespace de la classe qui définit le nom `count` (une fonction). C'est cette fonction qui est utilisée. Comme pour toutes les fonctions définies dans une classe et utilisée par un objet, le premier paramètre (le self dans le namespace de la méthode) est l'objet. On peut donc ensuite l'utiliser dans le namespace de la méthode pour modifier un attribut dans le namespace de l'objet (ici le position de l'objet).
  - `print(c1.get_value())` : pareil qu'au dessus. `get_value` est défini dans la classe. On essaye ici d'afficher à l'écran le résultat de l'exécution de la méthode `get_value` appliquée à l'objet de nom `c1`



> **Nota Bene :**
>`self` qui peut souvent paraître magique. Ce premeier paramètre est l'objet qui a appelé la méthode (à gauche du *.*). C'est la manière explicite de python de montrer quel objet est utilisé. Vous pouvez appeler ce premier paramètre comme vous voulez, mais c'est **très très** déconseillé car votre code en deviendra moins lisible (tout le monde utilise le nom `self`)


#### Un paramètre par défaut

On peut ajouter un paramètre par défaut en python.  L'UML de ce qu'on veut est :

![counter_step]({{ "img/counter_step.png"}})

En python cela donne : 

~~~ python
class Counter:
    def __init__(self, step=1):
        self.value = 0
        self.step = step
    def count(self):
        self.value = self.value + self.step
 def get_value(self):
    return self.value  
~~~

On peut utiliser deux fois le même nom step car ils sont dans des namespaces différent : 

  - un dans le namespace de la fonction (créé lorsque l'on exécute la fonction et détruit à la fin. Attention : on détruit les noms pas les objets)
  - un dans l'objet lui-même.
  
  
Que l'on peut utiliser comme ça : 

~~~ python
c1 = Counter(3)
c2 = Counter()
c1.count()
c2.count()
c1.count()    
~~~


> **Nota bene :** Notez bien que le premier paramètre de la définition de la classe est **TOUJOURS** self. Le premier paramètre de l'utilisation de la méthode est alors le second dans sa définition.



Les namespaces ne font que stocker des noms, ils peuvent donc être créés et détruits sans détruire des objets. Seul un objet qui n'est référencé dans aucun namespace est effacé car on ne peut plus y accéder (ie. une personne meurt vraiment quand plus personne ne pense à elle).


### Un dé

Commencez simple avec les éléments minimaux pour créer un dé. Le faire d'abord en UML, mettre des exemples d'utilisation du dé en python, puis mettre le code de la classe.

Diagramme UML du dé classique :

![dice]({{ "img/dice_no_class_att.png"}})

Montrez bien comment on utilise la classe en écrivant quelque lignes de code l'utilisant.

Diagramme UML du dé pipé :

![dice_proba]({{ "img/dice_proba_no_class_att.png"}})

On ajoute juste un attribut pour la distribution de proba sous forme de liste de proba de chaque face.
Pour le `roll`, on peut utiliser le `numpy.random.choice(liste_de_valeurs, p=liste_de_probas)`.

## Séance code


> **Attention :** Vous commencerez à coder en utiliser le module `random` puis vous utiliserez celui de `numpy`. N'oubliez pas de changer l'import (la fonction `choice` du module random de python ne permet pas de choisir les probabilités).


Dans le code donné ici on utilise l'attribut de classe `NUMBER_FACES`. Vous pouvez complètement faire sans. Les attributs de classes viendront plus tard (à la deuxième séance), prenez ça comme un teaser.


> **Nota Bene:** Dans les séances de code, ce qui est important c'est **le chemin** (votre écriture progressive du code) pas **l'arrivée** (le corrigé). Copier/coller le corrigé ne vous apportera rien à part des reproches de l'enseignant. 

### Dice

~~~ python
import numpy.random

class Dice:
  NUMBER_FACES = 6

  def __init__(self, position=1, probabilities=None):
    self.position = position
    if probabilities:
      self.probabilities = probabilities
    else:
      self.probabilities = [1 / self.NUMBER_FACES] * self.NUMBER_FACES

  def get_position(self):
    return self.position

  def set_position(self, new_position):
    self.position = new_position

  def roll(self):
    self.position = numpy.random.choice([i for i in range(1, self.NUMBER_FACES + 1)], p=self.probabilities)

  def __str__(self):
    return "Dice(position=" + str(self.position) + ", probabilities=" + str(self.probabilities)

  def __eq__(self, other):
    return self.position == other.position and self.probabilities == other.probabilities

  def __lt__(self, other):
    return self.position < other.position

  def __gt__(self, other):
    return self.position > other.position
~~~


### Tests

>**Nota Bene :** On importe `*` dans le code ci-après. Ce n'est habituellement pas une bonne pratique parce qu'on ne sais pas ce qu'on importe précisément. 
> C'est cependant toléré dans les tests si on teste **TOUTES** les méthodes définies dans le fichier que l'on importe.


~~~ python
from dice import *


def test_dice_creation_no_argument():
    dice = Dice()
    assert dice.get_position() == 1
    assert dice.probabilities == [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]


def test_dice_creation_initial_position():
    dice = Dice(position=5)
    assert dice.get_position() == 5
    assert dice.probabilities == [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]


def test_str():
    dice = Dice(position=1, probabilities=[1, 0, 0, 0, 0, 0])
    assert str(dice) == "Dice(position=1, probabilities=[1, 0, 0, 0, 0, 0]"


def test_set_position():
    dice = Dice()
    assert dice.get_position() == 1
    dice.set_position(3)
    assert dice.get_position() == 3


def test_roll_no_proba():
    dice = Dice()
    dice.roll()
    assert 1 <= dice.get_position() <= dice.NUMBER_FACES


def test_roll_proba():
    dice = Dice(probabilities=[1, 0, 0, 0, 0, 0])
    dice.roll()
    assert dice.get_position() == 1


def test_eq():
    dice = Dice(position=1)
    different_dice = Dice(position=2)
    equal_dice = Dice(position=1)
    assert dice != different_dice
    assert dice == equal_dice


def test_lt():
    small_dice = Dice(position=1)
    large_dice = Dice(position=2)
    assert small_dice < large_dice


def test_gt():
    small_dice = Dice(position=1)
    large_dice = Dice(position=2)
    assert large_dice > small_dice
~~~
