---
layout: layout/post.njk
title: "Projet : Amélioration des objets dés"

eleventyNavigation:
  prerequis:
    - "../projet-objets-dés/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Nous allons améliorer la classé que nous avions crée lors du projet précédent (en prérequis).

{% details "Un code possible du Dé" %}

Fichier `dé.py`{.fichier} :

```python 
import random

class Dé:
    def __init__(self):
        self.position = 1 

    def lancer(self):
        self.position = random.randrange(1, 6 + 1)
    
    def texte(self):
        if self.position == 1:
            return "⚀"
        elif self.position == 2:
            return "⚁"
        elif self.position == 3:
            return "⚂"
        elif self.position == 4:
            return "⚃"
        elif self.position == 5:
            return "⚄"
        else:
            return "⚅"

```

Fichier `test_dé.py`{.fichier} :

```python
from dé import Dé


def test_init():
    assert isinstance(Dé(), Dé)


def test_position():
    assert Dé().position == 1


def test_lancer():
    dé = Dé()
    dé.lancer()
    assert 1 <= dé.position <= 6


def test_dé_texte():
    dé = Dé()
    assert dé.texte() == "⚀"
    dé.position = 4
    assert dé.texte() == "⚃"

```

{% enddetails %}

## Valeur par défaut

{% faire %}
Faites en sorte que l'on puisse créer des dés avec une position initiale, On doit pouvoir :

- créer un dé sans paramètre, `Dé()`{.language-}, et sa position doit être sur la position 1
- créer un dé avec un paramètre qi sera sa position par défaut `Dé(4)`{.language-} par exemple.

{% endfaire %}
{% faire %}
Ajoutez des tests pour prendre en compte de cette nouvelle fonctionnalité.
{% endfaire %}

## Afficher des dés

{% faire %}
Remplacez la méthode `Dé.texte()`{.language-} par la méthode `Dé.__str__()`{.language-}.
{% endfaire %}
{% faire %}
Modifiez les tests pour prendre en compte de cette nouvelle méthode.
{% endfaire %}


## min et max dans classe

Notre classe `Dé`{.language-} contient 2 [magic numbers](https://fr.wikipedia.org/wiki/Nombre_magique_(programmation)#Constantes_num%C3%A9riques_non_nomm%C3%A9es) qui sont les bornes du lancé. Supprimons-les :

{% faire %}
Créez deux attributs de classes `MIN_VALEUR`{.language-} et `MAX_VALEUR`{.language-} qui vont permettre de supprimer les magics numbers de la méthode `Dé.lancer()`{.language-}
{% endfaire %}
