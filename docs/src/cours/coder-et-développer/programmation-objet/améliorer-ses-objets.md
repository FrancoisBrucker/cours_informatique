---
layout: layout/post.njk
title: Améliorer ses objets

eleventyNavigation:
  prerequis:
    - "../../mémoire-espace-nommage/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons utiliser plusieurs techniques permettant de fluidifier l'usage des objets.

## Ajout d'un paramètre dans le constructeur

On souhaite par pouvoir choisir le pas de notre compteur (c'est-à-dire ajouter 2 à chaque fois plutôt que 1 par exemple). Pour faire cela on va ajouter un paramètre dans le constructeur pour que chaque compteur puisse connaître son pas :

Fichier `compteur.py`{.fichier} :

```python
class Compteur:
    def __init__(self, pas):
        self.valeur = 0
        self.pas = pas

# ...
```

Il faut alors changer le code pour construire les objets avec ce nouveau paramètre :

Fichier `main.py`{.fichier} :

```python
from compteur import Compteur

c1 = Compteur(3)
c2 = Compteur(1)

#...
```

{% attention %}
Notez bien que le premier paramètre de la définition de la classe est **TOUJOURS** self. Le premier paramètre de l'utilisation de la méthode est alors le second dans sa définition.
{% endattention %}

Et il faut modifier la méthode `incrémente(self)`{.language-} pour qu'elle prenne en compte le pas :

```python
class Compteur:
    # ...
    def incrémente(self):
        self.valeur = self.valeur + self.pas
    # ...
```

{% note %}
On définira **toujours** les différents attributs de l'objet dans le constructeur `__init__`{.language-}.
On le fera de cette façon :

```python
self.nom_attribut = valeur_attribut
```

{% endnote %}

Cette façon de faire :

- attributs dans les objets
- méthodes (fonctions) dans les classes

permet à chaque objet (le paramètre `self`{.language-}) d'être différent tout en utilisant les mêmes méthodes.

{% note %}
Lors de l'utilisation d'une méthode, l'objet est passé en premier paramètre, ce qui permet de réutiliser tous ses attributs.
{% endnote %}

### Paramètres par défaut

Le souci avec la méthode précédente, c'est que même si le pas est de `1`{.language-}, il faut le définir dans la construction de l'objet. Nous allons changer ça en mettant un [paramètre par défaut](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values).

En python cela donne (fichier `compteur.py`{.fichier}) :

```python
class Compteur:
    def __init__(self, pas=1):
        self.valeur = 0
        self.pas = pas

    def incrémente(self):
        self.valeur = self.valeur + self.pas

```

On peut utiliser deux fois le même nom `pas`{.language-} car ils sont dans des espaces de noms différents :

- un dans l'espace de noms de la fonction (créé lorsque l'on exécute la fonction et détruit à la fin. Attention : on détruit les noms pas les objets)
- un dans l'objet lui-même.

Le code final de `main.py`{.fichier} pourra alors être :

```python
from compteur import Compteur

c1 = Compteur(3)
c2 = Compteur()
c1.incrémente()
c2.incrémente()
c1.incrémente()

print(c2.valeur)
```

### Valeur initiale

Finissons cette partie en ajoutant une valeur initiale à notre compteur :

Fichier `compteur.py`{.fichier} :

```python
class Compteur:
    def __init__(self, pas=1, valeur=0):
        self.valeur = valeur
        self.pas = pas

    def incrémente(self):
        self.valeur = self.valeur + self.pas

```

On peut créer de compteur de plein de façon différente maintenant. Par exemple :

- `Compteur()`{.language-} : créera un compteur de `valeur=0`{.language-} et de `pas=1`{.language-},
- `Compteur(3)`{.language-} : créera un compteur de `valeur=0`{.language-} et de `pas=3`{.language-},
- `Compteur(3, 12)`{.language-} : créera un compteur de `valeur=12`{.language-} et de `pas=3`{.language-},
- `Compteur(pas=3)`{.language-} : créera un compteur de `valeur=0`{.language-} et de `pas=3`{.language-},
- `Compteur(valeur=12)`{.language-} : créera un compteur de `valeur=12`{.language-} et de `pas=1`{.language-}

## <span id="méthodes-spéciales"></span> Méthodes spéciales

Python dispose de méthodes spéciales qui peuvent être invoquées en utilisant une syntaxe particulière. On a déjà vu `__init__`{.language-}, mais il y en a d'autres.

Elles sont rès pratiques car elles permettent d'utiliser nos objets de façon intuitive, comme si on utilisait des objets de python (affichage à l'écran, comparaison, exécution comme une fonction, ...).

Vous en trouverez une liste
exhaustive dans la [documentation officielle](https://docs.python.org/3/reference/datamodel.html#special-method-names). Nous allons
en utiliser ici quelques-unes sur notre classe. Ces méthodes se présentent toujours sous la forme `__nom_de_la_méthode__`{.language-}

### <span id="représentation"></span>Représentation

Essayez de taper dans le fichier `main.py`{.fichier} :

```python
c = Compteur()
print(c)
```

Vous devriez obtenir quelque chose comme :

```python
<__main__.Compteur object at 0x107149100>
```

La fonction `print`{.language-} appelle la méthode `__str__`{.language-} de notre classe. En effet, `print`{.language-} affiche à l'écran une chaîne de caractères. L'objet à afficher est donc converti en `str`{.language-} avant.

Comme nous n'avons pas défini cette méthode, c'est donc la méthode par défaut de tous les objets python qui est appelée. Comme vous le constatez, elle n'est pas très intéressante pour nous. Il faut donc la définir dans notre classe.

On va faire en sorte de pouvoir lire les valeur de notre objet sous la forme d'une chaîne de caractères :

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

### <span id="comparaison"></span> Comparaison

Finissons en essayant de comparer deux compteurs :

```python

c1 = Compteur(valeur=1)
c2 = Compteur(valeur=4)

print(c1 < c2)

```

Si on teste ça avec votre code tel qu'il est, on obtiendra :

```text
TypeError: '<' not supported between instances of 'Compteur' and 'Compteur'
```

Python vous explique qu'il ne connaît pas l'opérateur `<`{.language-} pour les objets de notre classe. Pour pouvoir utiliser
directement les opérateurs `<`{.language-} et `>`{.language-}, il faut définir respectivement les méthodes `__lt__(self, other)`{.language-} (_lower than_) et
`__gt__(self, other)`{.language-} (_greater than_). On pourra aussi ajouter `__eq__(self, other)`{.language-} pour tester l'égalité.

Par exemple pour ajouter la comparaison _strictement plus petit que_, on ajoute la méthode :

```python
class Compteur
    # ...
    def __lt__(self, other):
        return self.valeur < other.valeur
    # ...
```

{% note %}
On peut maintenant comparer 2 compteurs, ou un compteur à toute autre objet qui possède l'attribut valeur.
{% endnote %}

{% faire %}
Ajoutez les comparaisons :

- strictement plus grand que
- égal

Au compteur.
{% endfaire %}

{% lien %}
Les différents opérateurs de comparaison que l'on peut ajouter à nos objets sont décrits [dans la documentation](https://docs.python.org/fr/3/reference/datamodel.html#object.__lt__).

{% endlien %}

## <span id="code-final"></span> Code

Les deux fichiers sont dans le même dossier `compteur/`{.fichier} qui fait office de projet vscode.

Fichier `compteur.py`{.fichier} :

```python/
class Compteur:
    def __init__(self, pas=1, valeur=0):
        self.valeur = valeur
        self.pas = pas

    def __str__(self):
        return "Compteur(pas=" + str(self.pas) + ", valeur=" + str(self.valeur) + ")"

    def __lt__(self, other):
        return self.valeur < other.valeur

    def __gt__(self, other):
        return other.valeur < self.valeur

    def __eq__(self, other):
        return other.valeur == self.valeur

    def incrémente(self):
        self.valeur = self.valeur + self.pas

```

Fichier `main.py`{.fichier} :

```python/
from compteur import Compteur

c1 = Compteur(3)
c2 = Compteur()
c1.incrémente()
c2.incrémente()
c1.incrémente()

print(c1.valeur, c1)
print(c2.valeur, c2)

print(c1 < c2)

```
