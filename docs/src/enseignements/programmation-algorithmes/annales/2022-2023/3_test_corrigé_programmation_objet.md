---
layout: layout/post.njk

title:  "Corrigé Test 3 : programmation objet"
authors:
    - Valentin Emiya
    - François Brucker
---

Vous allez écrire une classe `Fraction`{.language-} utilisant les *méthodes spéciales* vues en cours.

{% info %}
Vous devez rendre un fichier markdown, mais rien ne vous empêche de coder en python dans un fichier annexe pour vérifier que votre code est juste.
{% endinfo %}

Les objets de la classe `Fraction`{.language-} possèdent deux attributs : `numérateur`{.language-} et `dénominateur`{.language-} et représentent la fraction `numérateur / dénominateur`{.language-}.

## Question 1

```python
import math


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

Écrivez le modèle UML de la classe `Fraction`{.language-}.

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
        réduit_self = self.réduit()
        réduit_other = other.réduit()

        return ((réduit_self.dénominateur == réduit_other.dénominateur) and 
                (réduit_self.dénominateur == réduit_other.dénominateur))

```
