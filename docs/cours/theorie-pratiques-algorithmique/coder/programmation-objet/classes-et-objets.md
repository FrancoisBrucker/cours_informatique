---
layout: page
title:  "classes et objets"
category: cours
tags: informatique cours 
authors: 
  - François Brucker
  - Célia Châtel
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [coder]({% link cours/theorie-pratiques-algorithmique/coder/index.md %}) / [programmation objet]({% link cours/theorie-pratiques-algorithmique/coder/programmation-objet/index.md %}) / [classes et objets]({% link cours/theorie-pratiques-algorithmique/coder/programmation-objet/classes-et-objets.md %})
{: .chemin}

Le but de la programmation objet n'est pas d'utiliser des concepts plus ou moins fumeux (classes abstraites, encapsulation et polymorphismes) mais d'écrire du code :

* facile à lire
* maintenable
* facile à étendre en ajoutant des fonctionnalités
  
Si un concept objet va à l'encontre de ce principe dans votre programme **NE L'UTILISEZ PAS**. C'est souvent vrai pour l'héritage qui n'a d'utilité que dans des cas très précis...

Un objet est un bout de code auquel est associé :

* des fonctionnalités (des méthodes) qui sont communes à tous les objets de sa classe
* des choses à lui tout seul (des attributs) qui lui permettent de se différentier des autres objets de sa classe même s'il a les mêmes fonctionnalités.

Un objet, n'est donc pas isolé, il partage ses fonctionnalités avec tous les objets de sa *classe*. Pour s'y retrouver entre, classes, objets méthode et attribut et trouver qui appartient à qui, python utilise les *namespaces* (espaces de noms). Cela lui permet le même code pour plusieurs objets.

## classes et objets

Lorsque l'on écrit du code python, on ne fait que manipuler des objets. Les entier, les chaines de caractères et même les fonctions peuvent être considérées comme des objets.

De façon générale, on peut considérer un **objet** comme étant *une structure de données* sur laquelle on peut *effectuer des opérations*. Pour pouvoir facilement créer une structure particulière et donner un moyen simple d'effectuer les opérations sur celle-ci, on utilise des **classes**.

Pour résumer, une classe :

* permet de créer un type d'objet (une structure de donnée précise)
* définit les opérations (méthodes) que l'on peut effectuer sur ces objets.

Un objet issu d'une certaine classe :

* possède la même structure de données que les autres objets de la classe mais les valeurs de celle-ci lui sont uniques : ses **attributs**
* possède un lien vers les méthodes définies dans sa class et on peut les utiliser via la notation pointée : ses **méthodes**

Exemple :

```text
objet.méthode(paramètre 1, ..., paramètre n)
```

On cherchera `méthode` définie pour l'`objet`.

### but

* factorisation du code ! c'est bien
* lisibilité avec la notation `.`
* compartimentation du code : chaque partie du code et chaque opération est compartimentée, ce qui permet de les tester et des améliorer indépendamment du reste du code.
* plutôt que de créer un gros programme complexe, on crée plein de petits programmes indépendants (les objets) qui interagissent entre eux.

Ces principes sont mis en ouvre de façon différentes selon les langages mais on retrouvera toujours ces notions.

### exemple d'objets en python

#### chaine de caractères

Les chaines de caractères sont des objets de la classe ([str](https://docs.python.org/fr/3/library/string.html)) :

```text
>>> type("une chaine")
<class 'str'>
```

Les méthodes définies dans la classe `str`, comme `upper()` par exemple sont utilisables par tous les objets de la classe `str` (dans l'exemple ci-après par l'objet `"coucou"` et l'objet `"toi"`) :

```python
>>> "coucou".upper()
'COUCOU'
>>> "toi".upper()
'TOI'
```

La notation pointée permet de dire que c'est la méthode à droite du `.` que l'on cherche dans l'objet à gauche du point.

> En python, ce la se fait en cherchant le nom `upper` dans le *namespace* (espace de nom) de l'objet à gauche du point.

Le code suivant produit donc une erreur car la fonction `upper`n'existe pas ! C'est la méthode définie dans la classe `str` qui s'appelle `upper` qui existe...

```text
>>> upper("coucou")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'upper' is not defined
```

Ce qui fait que le résultat est différent lorsque l'on applique la méthode `upper` à `"bonjour"` et `"toi"` est que ces deux objets, bien que de la même classe, sont différents : dan l'un il y a les caractère "bonjour", dans l'autres les caractères "toi".

On appelle les spécificités de chaque objet, c'est à dire les valeurs de sa structure de données, des **attributs**.

> un objet `str` est bien plus que juste ses caractères : **Un objet est bien plus que ses composants**

#### entiers

Les entiers sont aussi des objets d'une classe : `int`.

```text
>>> type(1)
<class 'int'>
```

Contrairement à la classe `str`, la classe `int` ne définit pas de méthode mais des opérations. Par exemple `__add__` définit l'addition d'un entier par un autre objet. C'est pratique que tout soit défini dans la classe , cela nous permettra à nous aussi de faire nos propres additions.

Les deux écritures sont identiques en python, mais bien sur, nous préférerons la première, bien plus simple à écrire et à comprendre :

1. `1 + 2`
2. `(1).__add__(2)`

> Remarquez que l'opération `+` n'est pas identique pour `1 + 2` et `1.0 + 2`. Dans le premier cas c'est l'addition définie dans `int` qui est utilisé, dans le second cas c'est celle définie dans `float` qui est utilisée.

### créer des objets

Pour créer des objets d'une classe, on utilise un **constructeur**.

En python, c'est le nom de la classe. Par Exemples :

* `list(range(5))` : crée une liste (de type `list`) avec le résultat de la fonction `range`
* `float("3.1415")` : crée un réel à partir de la chaine de caractère `"3.1415"`.
* `int(3.1415)` : crée un entier à partir du réel `3.1415`.

> Certains objets se créent juste avec leur valeur comme les entiers, les réels ou les chaines de caractères. En python `3` est équivalent à `int(3)` par exemple.

## outils

On va utiliser un outil *papier* pour écrire nos classe (l'[uml](https://fr.wikipedia.org/wiki/UML_(informatique))) et un outil clavier (le python).

### uml

L'uml est une façon de représenter des objets et des classes. Nous allons l'utiliser pour décrire les classes que nous allons créer.

> [un tutoriel uml](https://www.sparxsystems.fr/resources/tutorials/uml/datamodel.html) pour comprendre sa notation et son utilité.

L'uml peut être très compliqué. Nous allons uniquement l'utiliser ici comme une représentation synthétique d'une classe/objet. Vous le verrez dans les exemples ci-dessous mais, en gros, une classe en uml c'est :

```uml
-----------------------
| Nom de la Classe    |
|---------------------|
| Attributs : propre  |
| à chaque objet      |
|---------------------|
| méthodes : commun   |
| à tous les objets   |
-----------------------
```

* pour chaque attribut on pourra préciser le *type* (entier, chaine de caractère, une classe particulière d'objet, ...) si c'est important
* pour chaque méthode on donnera sa [signature](https://developer.mozilla.org/fr/docs/Glossaire/Signature/Fonction) complète (son nom et ses paramètres) pour que l'on puisse l'utiliser.

### python

Comme le python va être notre langage de programmation, regardons quelques convention d'usage lorsque l'on programme objet en python.

> En python, beaucoup de choses sont des [conventions](https://en.wikipedia.org/wiki/Convention_over_configuration) (variable privée, premier nom est self, ...) mais tout le monde s'y tient car la lecture du code en devient aisée.

#### constructeur

En python, le constructeur d'une classe sera **toujours** la méthode : `__init__`. C'est une méthode spéciale.

#### variables spéciales

En regardant du code python, vous allez voir beaucoup de noms qui commencent par des `_`. Ils sont une signification spéciale en python :

* qui commencent par `_` : non public. Ce sont des attributs ou méthodes que l'utilisateur n'est pas sensé utiliser. Ils sont uniquement là pour le bon fonctionnement de la classe.
* qui commencent par `__` : privé (non disponibles pour les descendants lorsque l'on fait de l'héritage). Ces attributs ou méthodes sont réservé exclusivement à être utilisé dans la classe.
* qui commencent et finissent par `__` : méthodes spécifiques de python qui ont un sens (par exemple __str__, __eq__), elles sont utilisées dans des cas précis et documentés.

#### espace de nom (namespaces)

La gestion des noms en python se fait via des [espaces de noms](http://sebastianraschka.com/Articles/2014_python_scope_and_namespaces.html). L'ordre dans lequel ces noms sons cherché pour être associé à un objet est logique et se règle en sachant quel namespace est utilisé.

On fera des exercices pour travailler avec les différents namespaces.

#### ressource

* Le [tuto python sur les classes de python](https://docs.python.org/3/tutorial/classes.html). Ce cours est là pour vous montrer tout ce qu'il y a dedans, à part (peut-être) la partie sur l'héritage et les itérateurs.
* les [namespaces](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)

## Premier exemple : le Compteur

On souhaite créer un objet `Compteur` qui retient le compte de quelque chose et est capable d'ajouter 1 à son compte quand on le lui demande.

On va tenter de proposer une modélisation UML de cet objet simple, puis de le coder en python.

### code d'utilisation

 Cette modélisation doit être capable de répondre au code suivant, dans le fichier *"main.py"* :

``` python
from compteur import Compteur
    
c1 = Compteur()
c2 = Compteur()
c1.ajoute()
c2.ajoute()
c1.ajoute()

print(c2.donne_valeur())
```

#### analyse du programme

C'est du python. On va essayer de comprendre le code pour produire une représentation uml de la classe `Compteur`.

1. on importe le mot `Compteur` et on l'exécute 2 fois pour l'affecter à 2 noms différents : cela **ne doit pas être** une fonction normale, sinon `c1` et `c2` seraient identiques.
2. on suppose donc que `Compteur` est une *classe* et que l'on a crée 2 **objets** `c1` et `c2`.

**Les objets d'une classe partagent les mêmes méthodes**, donc :

* `ajoute()` doit faire la même chose pour `c1` et `c2`
* je dois pouvoir écrire : `c1.donne_valeur()`, même si ce n'est pas écrit dans le code.

De plus, comme j'appelle `c1.ajoute()` et `c2.ajoute()` sans paramètre on doit surement modifier un attribut des objets `c1` et `c2`, car les **attributs sont spécifique à chaque objet d'une classe**

#### exécution du programme

A la lecture du code, on *a envie* que le code fasse ça :

1. on crée 2 compteurs
2. on en incrémente 1 deux fois et l'autre qu'une seule fois
3. on affiche à l'écran la valeur d'un des compteurs (celui qui a été incrémenté 1 fois) : 1

### schéma uml

Un objet est un ensemble de fonctionnalités récurrente dans un programme. Ici un
compteur. Les fonctionnalités sont :

* ajouter une unité à un compteur
* connaître la valeur du compteur.

Pour que l'on puisse avoir plusieurs compteurs (si on n'a qu'un seul compteur, ce n'est pas la peine de faire des objets), il faut que chaque compteur ait une valeur à lui.

On a donc ce qu'il faut pour notre classe :

* un nom : Compteur
* des méthodes (**= fonctionnalités = ce qui est pareil pour tous les objets**) : `ajoute` et `donne_valeur`
* un attribut (**= ce qui est différent pour chaque objet**) : `value`

Pour créer un diagramme uml, je commence toujours par le nom de la classe, puis j'imagine comment je vais l'utiliser (ici incrémenter un compteur). Une fois que je sais comment je vais l'utiliser, je vois ce qu'il faut ajouter à chaque objet pour qu'il puisse stocker les informations nécessaires à son utilisation : ce sont les attributs (ici un entier pour stocker le nombre de fois où on l'a incrémenté).

Ce qui donne le diagramme uml du compteur :

![compteur]({{ "/assets/cours/developpement/programmation-objet/counter_init.png" | relative_url }}){:style="margin: auto;display: block}

>On a utilisé ici un `_` en début de nom de la variable `value` pour signifier qu'elle est *privée*, c'est à dire que personne d'autre n'a le droit de l'utiliser à part l'objet. Cette convention n'est pas indispensable à utiliser car il est parfois un peut flou de savoir si telle ou telle attribut et *privé* ou *publique*...

### code python

La classe python qui correspond à l'uml précédent est celui-ci, contenu dans le fichier *"compteur.py"*, placé dans le même dossier que le fichier *"main.py"* :

``` python
class Compteur:
    def __init__(self):
        self.valeur = 0
           
    def ajoute(self):
        self.valeur = self.valeur + 1
    
    def donne_valeur(self):
        return self.valeur
```

La définition d'une classe est un bloc python :

```text

class <nom de la classe>:
    def __init__(self, paramètre 1, ..., paramètre n):
        instruction 1
        ...
        instruction n
    def méthode 1(self, paramètre 1, ..., paramètre n):
        instruction 1
        ...
        instruction n
        ...
    def méthode n(self, paramètre 1, ..., paramètre n):
        instruction 1
        ...
        instruction n
```

* `__init__` est le constructeur. L'usage courant est de déclarer tous les attributs d'un objets dans celui-ci.
* deux méthodes : `ajoute` et `donne_valeur`

En python, lorsque l'on définit une classe, le 1er paramètre de chaque méthode est **toujours** `self`. A l'exécution, python donnera à ce paramètre l'objet qui appelle la méthode, on ne le vois pas lorsque l'on écrit le code.

Par exemple dans le code la ligne `c1.ajoute()` sera transformée par python en : `Compteur.ajoute(c1)` qui peut se lire : on exécute la fonction `ajoute` de l'espace de nom du bloc `Compteur` avec comme paramètre `c1`.

La première façon d'écrire (`c1.ajoute()`) est plus simple à comprendre **pour un humain** et évite les erreurs (la méthode est appliquée à l'objet à gauche du point), alors que la seconde est plus facile à comprendre **pour un ordinateur** en utilisant les espaces de noms et le passage explicite de l'objet appelant.

>`self` qui peut souvent paraître magique. Ce premier paramètre est l'objet qui a appelé la méthode (à gauche du *.*). C'est la manière explicite de python de montrer quel objet est utilisé. Vous pouvez appeler ce premier paramètre comme vous voulez, mais c'est **très très** déconseillé car votre code en deviendra
moins lisible (tout le monde utilise le nom `self`).

### exécution du code

En python, tout peut être vu comme un *namespace* particulier, un endroit où sont rangés des noms : noms de variables, de fonctions, de classes, etc.

Les namespaces possibles sont :

* le namespace global
* la classe, ici `Compteur`. Contient tout ce qui est défini dans la classe comme les méthodes ou les constantes.
* l'objet : ici deux objets `c1` et `c2` de la classe `Compteur`. Chaque objet contient tout ce qui est défini pour l'objet en particulier (par exemple dans le `__init__` quand l'objet est appelé self)
* les méthodes : ce qui n'existe que de l'exécution de la méthode à la fin de son exécution

Plusieurs namespaces peuvent cohabiter en même temps, pour connaître celui qui va être utilisé, python va du [local au global](http://sebastianraschka.com/Articles/2014_python_scope_and_namespaces.html). S'il n'y a pas d'inclusion (comme une fonction dans une fonction), cela donne :

1. fonction (inclut les méthodes)
2. objet
3. classe
4. global
5. built-in (les mots du langage python)

> S'il y a inclusion de namespaces, on suit la règle [LEGB](http://sebastianraschka.com/Articles/2014_python_scope_and_namespaces.html#3-legb---local-enclosed-global-built-in)

Pour le code de *"main.py"*, ligne à ligne :

0. lorsque python commence l'exécution du fichier, il crée le namespace global. C'est le namespace le plus haut.
1. `from compteur import Compteur` : cherche un fichier *"compteur.py"* dans le répertoire courant. Python l'exécute (il lit chaque ligne) avec son propre namespace. Une fois ceci fait, il prend le nom `Compteur` dans ce namespace et l'ajoute au namespace global. On peut donc utiliser le nom `Compteur` qui est défini dans le namespace de *"compteur.py"*
2. `c1 = Compteur()` :
   * en informatique `=` n'est pas symétrique. A gauche un nom à droite un objet. Ici ceci signifie que l'on ajoute le nom `c1` au namespace global et que sa valeur sera le résultat de `Compteur()`
   * `Compteur()` : est le résultat de l'exécution du nom `Compteur`. Les parenthèses (et les paramètres éventuels) après un nom l'exécute. On aurait pu tout à fait écrire `c1 = Compteur` on aurait alors eu un nom `c1` qui sera égal à la classe `Compteur`.
   * `Compteur` est dans le namespace global grâce à la ligne précédente. Exécuter une classe revient à :
     * créer un namespace vierge
     * chercher la méthode `__init__` de la classe et l'exécuter en passant le nouveau namespace en premier paramètre :
        * pour exécuter une fonction on crée un namespace pour elle.
        * on place le nom `self` qui vaut ici le nouveau namespace créé
        * la première ligne crée le nom `value` dans le namespace nommé `self`
        * la fonction étant terminée, on supprime le namespace de la fonction (qui contenait le nom `self`)
        * on rend l'objet
   * l'objet (qu'on peut assimiler au namespace) créé est associer au nom `c1`
3. idem que la ligne précédente avec un nouvel objet
4. `c1.ajoute()` : python cherche le nom `ajoute`. Il regarde d'abord dans l'objet de nom `c1`. Ça n'y est pas. Il regarde donc au dessus : dans le namespace de la classe qui définit le nom `ajoute` (une fonction). C'est cette fonction qui est utilisée. Comme pour toutes les fonctions définies dans une classe et utilisée par un objet, le premier paramètre (le self dans le namespace de la méthode) est l'objet. On peut donc ensuite l'utiliser dans le namespace de la méthode pour modifier un attribut dans le namespace de l'objet (ici le position de l'objet).
5. idem que la ligne d'avant
6. idem que la ligne d'avant
7. `print(c1.donne_valeur())` : pareil que la ligne 4. `donne_valeur` est défini dans la classe. On essaye ici d'afficher à l'écran le résultat de l'exécution de la méthode `donne_valeur` appliquée à l'objet de nom `c1`

Exécutez le code de la partie précédente un utilisant le code python de la
classe ci-avant. Montrez tous les *namespaces* utilisés.

> `objet.nom` est **toujours** résolu de façon identique en python : on commence par chercher le nom dans l'objet et si on ne le trouve pas on cherche dans la classe

## Deuxième exemple : Compteur à pas choisi

On souhaite maintenant pouvoir choisir le pas de notre compteur (c'est-à-dire ajouter 2 à chaque fois plutôt que 1 par exemple).

Pour faire cela on va ajouter un paramètre dans le constructeur.

### ajout d'un paramètre dans le constructeur

Nous allons ajouter un paramètre dans le constructeur pour que chaque compteur puisse connaitre son pas :

Fichier *"compteur.py"* :

``` python
class Compteur:
    def __init__(self, pas):
        self.valeur = 0
        self.pas = pas

# ...           
```

Il faut alors changer le code pour construire les objets avec ce nouveau paramètre :

Fichier *"main.py"* :

```python
from compteur import Compteur
    
c1 = Compteur(3)
c2 = Compteur(1)

#...
```

>Notez bien que le premier paramètre de la définition de la classe est **TOUJOURS** self. Le premier paramètre de l'utilisation de la méthode est alors le second dans sa définition.
{: .attention}

Et il faut modifier la méthode `ajoute(self)` pour qu'elle prenne en compte le pas :

```python
class Compteur:
    # ...
    def ajoute(self):
        self.valeur = self.valeur + self.pas
    # ...
```

On définit toujours les différents attributs de l'objet dans le constructeur `__init__` de la même façon :

```python
self.nom_attribut = valeur_attribut
```

Cette façon de faire permet à chaque objet (le paramètre `self`) d'être différent. Lors de l'utilisation de méthode, l'objet est toujours passé en premier paramètre, ce qui permet de réutiliser tous les attributs définis dans le constructeur.

### paramètre par défaut

Le soucis avec la méthode précédente, c'est que même si le pas est de `1` il faut le définir dans la construction de l'objet. Nous allns hanger ça en mettant un [paramètre par défaut](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values).

En python cela donne (fichier *"compteur.py"*) :

```python
class Compteur:
    def __init__(self, pas=1):
        self.valeur = 0
        self.pas = pas

    def ajoute(self):
        self.valeur = self.valeur + self.pas

    def donne_valeur(self):
        return self.valeur
```

On peut utiliser deux fois le même nom `pas` car ils sont dans des namespaces différent :

* un dans le namespace de la fonction (créé lorsque l'on exécute la fonction et détruit à la fin. Attention : on détruit les noms pas les objets)
* un dans l'objet lui-même.
  
Le code final de *"main.py"* pourra alors être :

```python
from compteur import Compteur
    
c1 = Compteur(3)
c2 = Compteur()
c1.ajoute()
c2.ajoute()
c1.ajoute()

print(c2.donne_valeur())
```

### valeur initiale

Finissons cette partie en ajoutant une valeur initiale à notre compteur :

Fichier *"compteur.py"* :

```python
class Compteur:
    def __init__(self, pas=1, valeur=0):
        self.valeur = valeur
        self.pas = pas

    def ajoute(self):
        self.valeur = self.valeur + self.pas

    def donne_valeur(self):
        return self.valeur
```

On peut créer de compteur de plein de façon différente maintenant. Par exemple :

* `Compteur()` : créera un compteur de `valeur=0` et de `pas=1`,
* `Compteur(3)` : créera un compteur de `valeur=0` et de `pas=3`,
* `Compteur(3, 12)` : créera un compteur de `valeur=12` et de `pas=3`,
* `Compteur(pas=3)` : créera un compteur de `valeur=0` et de `pas=3`,
* `Compteur(valeur=12)` : créera un compteur de `valeur=12` et de `pas=1`

### Pour aller plus loin

Python dispose de méthodes spéciales qui peuvent être invoquées en utilisant une syntaxe particulière. On a déjà vu `__init__`, mais il y en a d'autres.

Vous en trouverez une liste
exhaustive dans la [documentation officielle](https://docs.python.org/3/reference/datamodel.html#special-method-names). Nous allons
en utiliser ici quelques-unes sur notre classe. Ces méthodes se présentent toujours sous la forme `__nom_de_la_methode__`.

Essayez de taper dans le fichier *"main.py"* :

```python
c = Compteur()
print(c)
```

Vous devriez obtenir quelque chose comme :

```python
<__main__.Compteur object at 0x107149100>
```

La fonction `print` appelle la méthode `__str__` de notre classe. En effet, `print` affiche à l'écran une chaine de caractère. L'Objet à afficher est donc converti en `str` avant.  

 Comme nous n'avons pas défini cette méthode, c'est donc la méthode par défaut de tous les objets python qui est appelée. Comme vous le constatez, elle n'est pas très intéressante pour nous. Il faut donc la définir dans notre classe.

On va faire en sorte de pouvoir lire les valeur de notre objet sous la forme d'une chaine de caractère :

```python
class Compteur
    # ...
    def __str__(self):
        return "Compteur(pas=" + str(self.pas) + ", valeur=" + str(self.valeur) + ")"
```

Avec cette nouvelle méthode, le code précédent donne :

```python
Compteur(pas=1, valeur=0)
```

Ce qui est bien plus lisible.

Finissons en essayons de comparer deux compteurs :

```python
c1 = Compteur(valeur=1)
c2 = Compteur(valeur=4)
c1 < c2
```

Si on testez ça avec votre code tel qu'il est, on obtiendra :

```text
TypeError: '<' not supported between instances of 'Compteur' and 'Compteur'
```

Python vous explique qu'il ne connaît pas l'opérateur `<` pour les objets de notre classe. Pour pouvoir utiliser
directement les opérateurs `<` et `>`, il faut définir respectivement les méthodes `__lt__(self, other)` et
`__gt__(self, other)`. On pourra aussi ajouter `__eq__(self, other)` pour tester l'égalité.

Nous allons ici juste comparer deux compteur pour la comparaison "plus petit que" :

```python
class Compteur
    # ...
    def __lt__(self, other):
        return self.valeur < other.valeur
```

> On peut maintenant comparer 2 compteurs, ou un compteur à toute autre objet qui possède l'attribut valeur.

### code

Les deux fichiers sont dans le même dossier *"compteur"* qui fait office de projet vscode.

Fichier *"compteur.py"* :

```python
class Compteur:
    def __init__(self, pas=1, valeur=0):
        self.valeur = valeur
        self.pas = pas

    def __str__(self):
        return "Compteur(pas=" + str(self.pas) + ", valeur=" + str(self.valeur) + ")"

    def __lt__(self, other):
        return self.valeur < other.valeur
        
    def ajoute(self):
        self.valeur = self.valeur + self.pas

    def donne_valeur(self):
        return self.valeur        
```

Fichier *"main.py"* :

```python

from compteur import Compteur
    
c1 = Compteur(3)
c2 = Compteur()
c1.ajoute()
c2.ajoute()
c1.ajoute()

print(c1.donne_valeur(), c1)
print(c2.donne_valeur(), c2)

print(c1 < c2)
```
