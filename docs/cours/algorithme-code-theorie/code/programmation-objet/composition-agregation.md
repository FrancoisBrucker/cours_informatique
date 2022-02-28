---
layout: page
title:  "Composition et agrégation"
category: cours
authors: 
  - François Brucker
  - Célia Châtel
---

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [code]({% link cours/algorithme-code-theorie/code/index.md %}) / [programmation objet]({% link cours/algorithme-code-theorie/code/programmation-objet/index.md %}) / [composition et agrégation]({% link cours/algorithme-code-theorie/code/programmation-objet/composition-agregation.md %})
>
> **prérequis :**
>
> * [classes et objets]({% link cours/algorithme-code-theorie/code/programmation-objet/classes-et-objets.md %})
{: .chemin}

Le but de cette séance est de consolider les concepts fondamentaux de classe et d'objet et d'ajouter les notions de
composition, d'agrégation et d'attributs de classe.

## liens entre classes

Composition et agrégation permettent de lier des classes ensembles, et plus principalement lorsqu'une classe admet comme attribut des objets de l'autre classe.

Ce qui les distingue :

>
>* **agrégation** : quand les objets utilisés sont créés en dehors de la classe,
>* **composition** : quand les objets utilisés sont créés dans le constructeur de la classe qui les utilise.
{: .note}

Il est important de comprendre que si des objets n'ont pas été crées dans la classe qui l'utilise, ils peuvent être connus par d'autres méthodes du programme et donc être modifiées par celles-ci.

Les exemple de composition et d'agrégation de *la vraie vie* sont souvent un peu bizarre. Mais par exemple :

* Un livre est composé de pages : pour créer le livre on a créé les pages : c'est une **composition**
* Les télécommandes ont besoin de piles pour fonctionner, mais on peut les remplacer : c'est une **agrégation**.

## schémas uml

Lorsque l'on utilise la composition ou l'agrégation de nos classes dans des schéma uml, on liera la classe composé (*resp.* agrégée) à la classe l'utilisant par une flèche. Cette flèche sera différente pour une composition ou une agrégation :

![uml composition et agrégation](./assets/classes-3.png){:style="margin: auto;display: block;"}

## exemple du panier de fruit

Prenons un autre exemple, le panier de fruits. Je voudrais modéliser un panier de fruits. Il doit avoir les propriétés suivantes :

* il doit être vide initialement
* je dois pouvoir ajouter des fruits dans le panier
* je dois pouvoir montrer les fruits que j'a dans le panier
* je dois pouvoir reprendre un fruit du panier

### modélisation uml

Comme à notre habitude commençons par créer une boîte uml presque vide :

```uml
-----------------------
| Panier              |
|---------------------|
| ?                   |
|---------------------|
| __init__()          |
| ajoute(Fruit)       |
| montre_panier()     |
| supprime(Fruit)     |
-----------------------
```

Pour que l'on puisse faire ces différentes méthodes, il faut que `Panier` puisse stocker ses fruit. On lui ajoute donc un attribut qui sera une liste.

```uml
-----------------------
| Panier              |
|---------------------|
| stock: list         |
|---------------------|
| __init__()          |
| ajoute(Fruit)       |
| montre_panier()     |
| supprime(Fruit)     |
-----------------------
```

### composition et agrégation

* Le stock est une **composition** : il est crée avec le panier
* les fruits sont une **agrégation** : ils sont ajouté par une méthode dans l'objet.

### code python

Ceci s'implémente aisément en python :

```python
class Panier:
    def __init__(self):
        self.stock = []

    def ajoute(self, fruit):
        self.stock.append(fruit)

    def montre_panier(self):
        return self.stock

    def supprime(self, fruit):
        self.stock.remove(fruit)
```

On peut alors utiliser notre classe, par exemple :

```python
panier = Panier()

print(panier.montre_panier())

panier.ajoute("pomme")

print(panier.montre_panier())

panier.ajoute("pomme")
panier.ajoute("poire")

print(panier.montre_panier())

panier.supprime("pomme")
print(panier.montre_panier())
```

### attention

> Si une classe est composée d'autres objets, ces parties peuvent être modifiées en dehors de la classe, même pour une composition.
{: .attention}

Dans notre exemple, une méthode retourne un objet qui est un attribut. Une fois qu'un objet a été *donné* au monde extérieur on ne contrôle plus son état et il peut être utilisé a priori par n'importe quoi d'autre dans le programme.

Regardez le code suivant :

```python

panier = Panier()

print(panier.montre_panier())

panier.ajoute("pomme")

copie = panier.montre_panier()

copie.append("champignon")
print(panier.montre_panier())
```

On a ajouté un champignon à notre panier sans que l'objet panier ne le sache !

Ce n'est pas forcément un problème, sauf si on vérifiait que ce qu'on ajoute dans le panier doit être un fruit.

Pour que tout se passe comme prévu, il faut donc s'assurer que pour les attributs , soit :

1. on s'en fiche qu'ils changent
2. on refait un nouvel objet à nous pour s'assurer qu'il ne changera pas
3. les objets que l'on retourne et qui sont des attributs sont non modifiables (des entiers, réels, chaînes de caractères, tuples, etc)

#### 1ère solution

La 1ère solution est ce qu'on a pour l'instant.

#### 2nde solution

La seconde solution reviendrait à donner un nouveau panier à chaque fois en modifiant la méthode `donne_panier()` :

```python
class Panier:
    # ...

    def montre_panier(self):
      return list(self.stock)
    
    #...
```

Enfin, la dernière solution reviendrait à ne pas pouvoir modifier l'attribut et à le recréer à chaque modification, par exemple dans la méthode `ajoute_fruit()`. On utilise un [tuple](https://python.doctor/page-apprendre-tuples-tuple-python) :

```python
class Panier:
    def __init__(self):
      self.stock = tuple()

    # ...

    def ajoute(self, fruit):
        temp = []
        temp.extend(self.stock)
        temp.append(fruit)

        self.stock = tuple(temp)
    
    #...
```

Selon que l'on aura beaucoup d'ajout ou beaucoup de montrage de panier, on choisira l'une au l'autre solution. Mais si on a pas d'idée, on préférera **toujours** la 3ème solution qui est la plus robuste.

Le fait d'avoir des objet qui ne se modifient pas est appelé [value object](https://en.wikipedia.org/wiki/Value_object).

Ces objets possèdent des valeurs et des méthodes pour y accéder mais que l'on ne peut pas modifier. La seule façon de changer de valeur c'est de recréer de nouveaux objets. Pour que l'utilisation de ce genre d'objets soit fluide, on fait en sorte qu'ils puissent supporter l'opération `==`.

Vous avez utilisé des value objects bien souvent en python comme : les  entiers, les réels ou encore les chaines de caractères. Enfin de nombreux objets modifiables en python ont leur contrepartie non modifiable comme les `tuple` qui sont des listes non modifiables ou encore les `frozenset` sont des ensembles non modifiables.

> Une bonne façon de programmer est de n'utiliser par défaut que des objets non modifiables et que si le besoin s'en fait sentir de les rendre modifiables.
{: .note}

#### 3ère solution

Enfin la troisième solution revient à rendre un tuple dans la méthode `montre_panier` :

```python
class Panier:
    # ...

    def montre_panier(self):
      return tuple(self.stock)
    
    #...
```

C'est la solution la plus simple puisque le reste du code reste identique et l'on a juste fait en sorte de sécuriser notre attribut.

## tests

Lorsque l'on crée ses propres objets, il est important de tester leurs fonctionnalités. On procède alors ainsi :

* chaque méthode doit être testée
* chaque test doit être indépendant

Dans la mesure du possible, on ne teste pas la valeur des attributs. On utilise des méthodes publique pour tester. En effet les attributs montrent l'implémentation de la classe et pas son usage.

### exemple

Par exemple, pour notre panier. Fichier *"test_panier.py"* :

```python
from panier import Panier


def test_init():
    panier = Panier()
    assert panier is not None


def test_montre_panier_vide():
    panier = Panier()
    assert panier.montre_panier() == tuple()


def test_ajoute():
    panier = Panier()
    panier.ajoute("pomme")
    assert panier.montre_panier() == ("pomme",)


def test_supprime_dans_panier():
    panier = Panier()
    panier.ajoute("pomme")
    panier.supprime("pomme")

    assert panier.montre_panier() == tuple()
```

> * pour l'initialisation, on vérifie juste que notre objet existe. Comme il n'a pas de paramètre, on ne peut pas tester grand chose d'autre
> * On crée pour chaque test un nouveau objet, pour être sur que les tests n'interfèrent pas les uns avec les autres
> * Chaque test doit permettre d'utiliser la méthode testée comme elle doit être utilisée dans le code
{: .note}

### couverture de code {#couverture-code}

Les tests doivent nous permettre d'avoir confiance dans la qualité du code. Il faut donc que les tests vérifient tous les cas du code (passent bien par tous les blocs `alors` et `sinon` du code par exemple).

Un outil pour vérifier cela est la [couverture de code](https://fr.wikipedia.org/wiki/Couverture_de_code). On exécute les tests et on regarde, fichier par fichier quelles sont les lignes qui ont été vue pour ces tests.

Le [tuto couverture de code]({% link _tutoriels/editeur/vsc/2021-09-14-vsc-python-modules-supplementaires.md %}#code-coverage) vous montre comment l'installer. Son fonctionnement est le suivant :

1. on exécute les tests dans le terminal en ajoutant l'extension coverage  `python3 -m pytest --cov=.`
2. le résultat est donné dans le terminal.

```text
---------- coverage: platform darwin, python 3.9.9-final-0 -----------
Name             Stmts   Miss  Cover
------------------------------------
main.py             10     10     0%
panier.py           13      0   100%
test_panier.py      16      0   100%
------------------------------------
TOTAL               39     10    74%
```

On voit que l'exécution des tests à eu besoin d'utiliser 100% du fichier *"test_panier.py"* (ce qui est normal) et 100% du fichier *"panier.py"*. Le fichier *"main.py"* n'a pas été utilisé du tout (aucune des 10 lignes n'a été vue), ce qui est normal.

> Il faut tenter de passer par 100% du code utile dans nos tests.
{: .note}

Pour s'en rendre compte, on peut commenter le test `test_supprime_dans_panier` et re-exécuter les tests. j'obtiens alors :

```text
---------- coverage: platform darwin, python 3.9.9-final-0 -----------
Name             Stmts   Miss  Cover
------------------------------------
main.py             10     10     0%
panier.py           13      3    77%
test_panier.py      11      0   100%
------------------------------------
TOTAL               34     13    62%
```

3 lignes de `panier.py` n'ont pas été vue. POur savoir exactement les quelles, la commande `python3 -m pytest --cov=. --cov-report term-missing` donne :

```text
---------- coverage: platform darwin, python 3.9.9-final-0 -----------
Name             Stmts   Miss  Cover   Missing
----------------------------------------------
main.py             10     10     0%   1-17
panier.py           13      3    77%   15-18
test_panier.py      11      0   100%
----------------------------------------------
TOTAL               34     13    62%
```

C'est bien l'intérieur de la fonction `test_supprime_dans_panier`.

> Notez que la ligne contenant la définition de la fonction a été vue. En effet, lors de l'import du fichier *"panier.py"*, le ficher est lu, donc les noms des fonctions sont mises dans l'espace de nom du module.

## projet final

Vous devez avoir 3 fichiers :

### *"panier.py"*

```python
class Panier:
    def __init__(self):
        self.stock = []

    def ajoute(self, fruit):
        self.stock.append(fruit)

    def montre_panier(self):
        return tuple(self.stock)

    def supprime(self, fruit):
        self.stock.remove(fruit)
        
```

### le programme principal *"main.py"*

```python
from panier import Panier

panier = Panier()

print(panier.montre_panier())

panier.ajoute("pomme")

print(panier.montre_panier())

panier.ajoute("pomme")
panier.ajoute("poire")

print(panier.montre_panier())

panier.supprime("pomme")

print(panier.montre_panier())

```

### *"test_panier.py"*

```python
from panier import Panier


def test_init():
    panier = Panier()
    assert panier is not None


def test_montre_panier_vide():
    panier = Panier()
    assert panier.montre_panier() == tuple()


def test_ajoute():
    panier = Panier()
    panier.ajoute("pomme")
    assert panier.montre_panier() == ("pomme",)


def test_supprime_dans_panier():
    panier = Panier()
    panier.ajoute("pomme")
    panier.supprime("pomme")

    assert panier.montre_panier() == tuple()

```

### couverture de code

Avec le projet ci-dessus, j'ai 100% de couverture du code :

```text
---------- coverage: platform darwin, python 3.9.9-final-0 -----------
Name             Stmts   Miss  Cover   Missing
----------------------------------------------
main.py             10     10     0%   1-18
panier.py            9      0   100%
test_panier.py      16      0   100%
----------------------------------------------
TOTAL               35     10    71%
```
