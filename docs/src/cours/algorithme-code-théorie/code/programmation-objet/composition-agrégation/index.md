---
layout: layout/post.njk 
title: Composition et agrégation

eleventyNavigation:
  key: "Composition et agrégation"
  parent: "Programmation Objet"

prerequis:
    - "../classes-et-objets/"
---

<!-- début résumé -->

Le but de cette séance est de consolider les concepts fondamentaux de classe et d'objet et d'ajouter les notions de
composition, d'agrégation et d'attributs de classe.

<!-- end résumé -->

## Liens entre classes

Composition et agrégation permettent de lier des classes ensembles, et plus principalement lorsqu'une classe admet comme attribut des objets de l'autre classe.

Ce qui les distingue :

{% note "**Définition** :" %}

* ***agrégation*** : quand les objets utilisés sont créés en dehors de la classe,
* ****composition*** : quand les objets utilisés sont créés dans le constructeur de la classe qui les utilise.

{% endnote %}

Il est important de comprendre que si des objets n'ont pas été crées dans la classe qui l'utilise, ils peuvent être connus par d'autres méthodes du programme et donc être modifiées par celles-ci.

Les exemples de composition et d'agrégation de *la vraie vie* sont souvent un peu bizarres. Mais par exemple :

* Un livre est composé de pages : pour créer le livre on a créé les pages : c'est une **composition**
* Les télécommandes ont besoin de piles pour fonctionner, mais on peut les remplacer : c'est une **agrégation**.

## Schémas uml

Lorsque l'on utilise la composition ou l'agrégation de nos classes dans des schéma uml, on liera la classe composé (*resp.* agrégée) à la classe l'utilisant par une flèche. Cette flèche sera différente pour une composition ou une agrégation :

![uml composition et agrégation](classes-3.png)

## Exemple du panier de fruit

Prenons un autre exemple, le panier de fruits. Je voudrais modéliser un panier de fruits. Il doit avoir les propriétés suivantes :

* il doit être vide initialement
* je dois pouvoir ajouter des fruits dans le panier
* je dois pouvoir montrer les fruits que j'ai dans le panier
* je dois pouvoir reprendre un fruit du panier

### Modélisation uml

Comme à notre habitude commençons par créer une boîte uml presque vide :

```text
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

Pour que l'on puisse faire ces différentes méthodes, il faut que `Panier`{.language-} puisse stocker ses fruit. On lui ajoute donc un attribut qui sera une liste.

```text
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

### Composition et agrégation

* Le stock est une **composition** : il est créé avec le panier
* les fruits sont une **agrégation** : ils sont ajoutés par une méthode dans l'objet.

### Code python

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

### Attention

{% attention %}
Si une classe est composée d'autres objets, ces parties peuvent être modifiées en dehors de la classe, même pour une composition.
{% endattention %}

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

La seconde solution reviendrait à donner un nouveau panier à chaque fois en modifiant la méthode `montre_panier()`{.-} :

```python
class Panier:
    # ...

    def montre_panier(self):
      return list(self.stock)
    
    #...
```

#### 3ère solution

Enfin, la dernière solution reviendrait à ne pas pouvoir modifier l'attribut et à le recréer à chaque modification, par exemple dans la méthode `ajoute_fruit()`{.language-}. On utilise un [tuple](https://python.doctor/page-apprendre-tuples-tuple-python) :

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

Selon que l'on aura beaucoup d'ajouts ou beaucoup de visualisation du panier, on choisira l'une au l'autre solution. Mais si on a pas d'idée, on préférera **toujours** la 3ème solution qui est la plus robuste.

Le fait d'avoir des objets qui ne se modifient pas est appelé [value object](https://en.wikipedia.org/wiki/Value_object).

Ces objets possèdent des valeurs et des méthodes pour y accéder mais que l'on ne peut pas modifier. La seule façon de changer de valeur c'est de recréer de nouveaux objets. Pour que l'utilisation de ce genre d'objets soit fluide, on fait en sorte qu'ils puissent supporter l'opération `==`{.language-}.

Vous avez utilisé des value objects bien souvent en python comme : les  entiers, les réels ou encore les chaines de caractères. Enfin de nombreux objets modifiables en python ont leur contrepartie non modifiable comme les `tuple`{.language-} qui sont des listes non modifiables ou encore les `frozenset`{.language-} sont des ensembles non modifiables.

{% note %}
Une bonne façon de programmer est de n'utiliser par défaut que des objets non modifiables et que si le besoin s'en fait sentir de les rendre modifiables.
{% endnote %}

## Tests des objets

Lorsque l'on crée ses propres objets, il est important de tester leurs fonctionnalités. On procède alors ainsi :

* chaque méthode doit être testée
* chaque test doit être indépendant

Dans la mesure du possible, on ne teste pas la valeur des attributs. On utilise des méthodes publique pour tester. En effet les attributs montrent l'implémentation de la classe et pas son usage.

### Exemple

Par exemple, pour notre panier. Fichier `test_panier.py`{.fichier} :

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

{% note %}

* pour l'initialisation, on vérifie juste que notre objet existe. Comme il n'a pas de paramètre, on ne peut pas tester grand chose d'autre
* On crée pour chaque test un nouvel objet, pour être sur que les tests n'interfèrent pas les uns avec les autres
* Chaque test doit permettre d'utiliser la méthode testée comme elle doit être utilisée dans le code

{% endnote %}

## Code final { #code-final }

Vous devez avoir 3 fichiers :

### Code de la classe

Fichier : `panier.py`{.fichier}

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

### Programme principal

Fichier `main.py`{.fichier} :

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

### Tests

Fichier `test_panier.py`{.fichier} :

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
