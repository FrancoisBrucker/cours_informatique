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

{% lien %}
[Code de la classe Dé](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/coder-et-d%C3%A9velopper/apprendre-programmation/programmation-objet/projet-objets-d%C3%A9s/code)

{% endlien %}

## Valeur par défaut

{% exercice %}
Faites en sorte que l'on puisse créer des dés avec une position initiale, On doit pouvoir :

- créer un dé sans paramètre, `Dé()`{.language-}, et sa position doit être sur la position 1
- créer un dé avec un paramètre qi sera sa position par défaut `Dé(4)`{.language-} par exemple.

{% endexercice %}
{% details "corrigé" %}

Fichier `dé.py`{.fichier} :

```python
class Dé:
    def __init__(self, position=1):
        self.position = position

```

{% enddetails %}
{% exercice %}
Ajoutez des tests pour prendre en compte de cette nouvelle fonctionnalité.
{% endexercice %}
{% details "corrigé" %}

Fichier `test_dé.py`{.fichier} :

```python
def test_position():
    assert Dé().position == 1
    assert Dé(position=4).position == 4

```

On utilise toujours la technique qui consiste à utiliser directement un objet créé via le constructeur.
{% enddetails %}

## Afficher des dés

{% exercice %}
Remplacez la méthode `Dé.texte()`{.language-} par la méthode `Dé.__str__()`{.language-}.
{% endexercice %}
{% details "corrigé" %}

Fichier `dé.py`{.fichier} :

```python
class dé:

    # ..

    def __str__(self):
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

On utilise toujours la technique qui consiste à utiliser directement un objet créé via le constructeur.
{% enddetails %}

{% exercice %}
Modifiez les tests pour prendre en compte de cette nouvelle méthode.
{% endexercice %}
{% details "corrigé" %}

Fichier `test_dé.py`{.fichier} :

```python
def test_str():
    dé = Dé()
    assert str(dé) == "⚀"
    dé.position = 4
    assert str(dé) == "⚃"

```

{% enddetails %}
{% exercice %}
Implémentez la méthode spéciale `__repr__`{.language-} et restez là en utilisant la fonction `repr`{.language-}.
{% endexercice %}
{% details "corrigé" %}

Fichier `dé.py`{.fichier} :

```python
class dé:

    # ..

    def __repr__(self):
        return f"Dé(position={self.position})"
```

Fichier `test_dé.py`{.fichier} :

```python
def test_repr():
    assert repr(Dé()) == "Dé(position=1)"

```

{% enddetails %}


## min et max dans classe

Notre classe `Dé`{.language-} contient 2 [magic numbers](https://fr.wikipedia.org/wiki/Nombre_magique_(programmation)#Constantes_num%C3%A9riques_non_nomm%C3%A9es) qui sont les bornes du lancé. Supprimons-les :

{% exercice %}
Créez deux attributs de classes `MIN_VALEUR`{.language-} et `MAX_VALEUR`{.language-} qui vont permettre de supprimer les magics numbers de la méthode `Dé.lancer()`{.language-}
{% endexercice %}
{% details "corrigé" %}

Fichier `dé.py`{.fichier} :

```python
class dé:
    MIN_VALEUR = 1
    MAX_VALEUR = 6

    def __init__(self, position=1):
        self.position = position

    def lancer(self):
        self.position = random.randrange(self.MIN_VALEUR, self.MAX_VALEUR + 1)

```

{% enddetails %}


## Comparaisons

{% exercice %}
Créez et testez la comparaison `<` entree deux dés (méthode spéciale `__lt__`{.language-}).
{% endexercice %}
{% details "corrigé" %}

Fichier `dé.py`{.fichier} :

```python
class dé:

    # ...

    def __lt__(self, other):
        return self.position < other.position

```


Fichier `test_dé.py`{.fichier} : 

```python
def test_lt():
    d1 = Dé()
    d2 = Dé()
    assert not d1 < d2

    d2.position = 5
    assert d1 < d2
    assert not d2 < d1

```

{% enddetails %}

Cette comparaison permet de trier des listes de dés !

{% faire %}
Créez le fichier `main.py`{.fichier} et placez y le code suivant que vous pourrez tester :

```python
from dé import Dé

liste_d = [Dé() for _ in range(5)]

print(liste_d)

for d in liste_d:
    d.lancer()

print(liste_d)
liste_d.sort()
print(liste_d)
```

{% endfaire %}

## Code final

{% lien %}
- [Code de la classe python](https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/coder-et-d%C3%A9velopper/apprendre-programmation/programmation-objet/projet-objets-d%C3%A9s-am%C3%A9lioration/code)
- [Téléchargement du code](https://download-directory.github.io?url=https://github.com/FrancoisBrucker/cours_informatique/tree/main/docs/src/cours/coder-et-d%C3%A9velopper/apprendre-programmation/programmation-objet/projet-objets-d%C3%A9s-am%C3%A9lioration/code?filename=projet-compteur)
{% endlien %}