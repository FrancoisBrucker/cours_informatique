---
layout: layout/post.njk

title:  "Corrigé Test 3 : programmation objet"
authors:
    - Valentin Emiya
    - François Brucker
---

## Barème

Une note sur 5 répartie comme suit :

1. sur 1 point
2. sur 1 point
3. sur 1 point
4. sur 1 point
5. sur 1 point

La note sur $20$ finale est obtenue en multipliant la note sur 5 par $4$

{% note "**Objectif du test**" %}

La note maximale étant sur 20 :

* **un élève *normal*** doit parvenir à faire parfaitement les 3 premières questions. Ce qui lui permet d'avoir 3/5, soit 12/20
* **un bon élève** doit parvenir à réussir l'équivalent de 4 questions. Ce qui lui permet d'avoir 4/5 et donc 16/20
* **un très bon élève** fait les 5 questions

{% endnote %}

* min : 3.6/20 (.9/5)
* max : 20/20 (5/5)
* moyenne : 12/20 (3/5)
* écart-type : 4.92/20 (1.23/5)
* 25% : 8/20 (2/5)
* médiane (50%) : 12.4/20 (3.1/5)
* 75% : 14.6/20 (3.65/5)

## Erreurs fréquemment rencontrées

### Des méthodes affreuses

Lorsque l'on code une méthode, elle se doit d'utiliser les attributs de l'objet qui l'appelle. Sinon ce n'est pas une bonne méthode objet.

Par exemple pour valeur :

L'exemple suivant est certes syntaxiquement correct, mais ce n'est pas une méthode valable puisqu'elle n'utilise aucun attribut de l'objet :

{% attention "**Faux**" %}

```python
class Fraction:
    def __init__(self, dénominateur, numérateur):
        self.dénominateur = dénominateur
        self.numérateur = numérateur

    def valeur(self, numérateur, dénominateur):
        return numérateur / dénominateur
```

{% endattention %}

Il ne faut pas non plus définir un attribut autre-part que dans la méthode `__init__`{.language-} c'est encore une fois du python syntaxiquement correct, mais il est plus simple de connaître tous les attributs en ne regardant **que** la méthode `__init__`{.language-} (sinon, vous serez obligé de regarder toutes les méthodes  pour connaître tous les attributs d'un objet) :

{% attention "**Très Faux**" %}

```python
class Fraction:
    def __init__(self, dénominateur, numérateur):
        self.dénominateur = dénominateur
        self.numérateur = numérateur

    def valeur(self):
        self._val = self.numérateur / self.dénominateur
        return self._val
```

{% endattention %}

Enfin, horreur suprême le code suivant qui redéfinit un attribut du même nom qu'une méthode :

{% attention "**Archi Super Très Faux**" %}

```python
class Fraction:
    def __init__(self, dénominateur, numérateur):
        self.dénominateur = dénominateur
        self.numérateur = numérateur
    def valeur(self):
        self.valeur = self.numérateur / self.dénominateur
        return self.valeur
```

{% endattention %}

En effet à la première exécution de la méthode, son nom est transformé en attribut... Ce qui empêche l'exécution du deuxième appel :

```python
>>> class Fraction:
...     def __init__(self, dénominateur, numérateur):
...         self.dénominateur = dénominateur
...         self.numérateur = numérateur
...     def valeur(self):
...         self.valeur = self.numérateur / self.dénominateur
...         return self.valeur
... 
>>> f = Fraction(3, 4)
>>> f.valeur()
1.3333333333333333
>>> f.valeur()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'float' object is not callable
>>> 
```

{% info %}
L'erreur `TypeError: 'float' object is not callable` signifie que l'on essaie d'exécuteur un réel comme une méthode (c'est à dire un réel suivie de parenthèses, par exemple `3.14()`{.language-})
{% endinfo %}

### de l'UML non réglementaire

* il faut donner les paramètres d'entrée de chaque méthode (sauf self qui est sous-entendue)
* une méthode a des `()`{.language-} (car on les exécute) et les attributs n'en on pas (on les lit/affecte).
* `__init__`{.language-} est une méthode à mettre dans l'uml

### Encore et toujours de booléen testé

Dans l'implémentation de la méthode `__eq__`{.language-}, j'ai beaucoup vu (mais moins que la dernière fois tout de même) l'inutile :

```python
if (condition 1) and (condition 2):
    return True
else:
    return False
```

Encore une fois :

```python
return (condition 1) and (condition 2)
```

Est plus, plus lisible, bref bien plus élégant.

## Question 1

```python
class Fraction:
    def __init__(self, dénominateur, numérateur):
        self.dénominateur = dénominateur
        self.numérateur = numérateur
```

## Question 2

```python
class Fraction:
    def __init__(self, dénominateur, numérateur):
        self.dénominateur = dénominateur
        self.numérateur = numérateur

    def valeur(self):
        return self.numérateur / self.dénominateur
```

## Question 3

```python
import math


class Fraction:
    def __init__(self, dénominateur, numérateur):
        self.dénominateur = dénominateur
        self.numérateur = numérateur

    def valeur(self):
        return self.numérateur / self.dénominateur

    def réduit(self):
        q = math.gcd(self.dénominateur, self.numérateur)
        return Fraction(self.dénominateur / q, self.numérateur / q)

```

## Question 4

* Nom : Fraction
* Attributs :
  * dénominateur : int
  * numérateur : int
* Méthodes :
  * `__init__`{.language-}(dénominateur : int, numérateur : int)
  * `valeur`{.language-}()
  * `réduit`{.language-}() : Fraction
  * `__eq__`{.language-}(Fraction) : bool

## Question 5

```python
import math


class Fraction:
    def __init__(self, dénominateur, numérateur):
        self.dénominateur = dénominateur
        self.numérateur = numérateur

    def valeur(self):
        return self.numérateur / self.dénominateur

    def réduit(self):
        q = math.gcd(self.dénominateur, self.numérateur)
        return Fraction(self.dénominateur / q, self.numérateur / q)
    
    def __eq__(self, other):
        x = self.réduit()
        y = other.réduit()

        return (x.dénominateur == y.dénominateur) and (numérateur == y.numérateur)

```
