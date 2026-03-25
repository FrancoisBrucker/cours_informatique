---
layout: layout/post.njk
title: Améliorer ses objets

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Nous allons utiliser plusieurs techniques permettant de fluidifier l'usage des objets. Nous allons prendre comme exemple le compteur dont la classe est pour l'instant :


```python
class Compteur:
    def __init__(self):
        self.valeur = 0

    def incrémente(self):
        self.valeur = self.valeur + 1

```


## Paramètres par défaut

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

{% attention2 "**À retenir**" %}
Notez bien que le premier paramètre de la définition de la classe est **TOUJOURS** self. Le premier paramètre de l'utilisation de la méthode est alors le second dans sa définition.
{% endattention2 %}

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

{% exercice %}
Ajoutez au `Compteur`{.language-} un paramètre déterminant sa valeur initiale. Il faudra pouvoir créer des compteurs de multiples façon :

- `Compteur()`{.language-} : créera un compteur de `valeur=0`{.language-} et de `pas=1`{.language-},
- `Compteur(3)`{.language-} : créera un compteur de `valeur=0`{.language-} et de `pas=3`{.language-},
- `Compteur(3, 12)`{.language-} : créera un compteur de `valeur=12`{.language-} et de `pas=3`{.language-},
- `Compteur(pas=3)`{.language-} : créera un compteur de `valeur=0`{.language-} et de `pas=3`{.language-},
- `Compteur(valeur=12)`{.language-} : créera un compteur de `valeur=12`{.language-} et de `pas=1`{.language-}

{% endexercice %}
{% details "corrigé" %}

```python
class Compteur:
    def __init__(self, pas=1, valeur=0):
        self.valeur = valeur
        self.pas = pas

    def incrémente(self):
        self.valeur = self.valeur + self.pas

```

{% enddetails %}


## Attributs

On peut grandement améliorer la gestion des attributs des objets.

### Attributs privés

Il peut arriver que l'on ne veuille pas qu'un attribut soit modifié ou qu'on le modifie à une valeur non possible. Par exemple, on pourrait avoir envie de ne tolérer que des pas non nul mais pour l'instant rien ne nous empêche d'écrire :

```python
c = Compteur()
c.pas = 0
```

Et de créer un compteur qui n'incrémente jamais...


Pour éviter cela, on peut :

- restreindre l'accès à l'attribut `pas` : rendre l'attribut _privé_
- permettre de modifier l'attribut `pas` qu'en utilisant une méthodes spécifique : un _mutateur_

{% note2 "**Définition**" %}
Un attribut **_privé_** est un attribut qui ne doit pas être utilisé autre-part que dans les définitions de méthodes de la classe. Les attribut directement utilisables dans le code sont dit **_public_**.

Tout code voulant accéder ou modifier à cet attribut **doit** passer par son accesseur/mutateur.
{% endnote2 %}

{% note2 "**Définition**" %}
Un **_accesseur_** (**_getter_**) est une méthode dont le but est de rendre un attribut. On la nomme usuellement : `get_[nom de l'attribut]()`{.language-}
{% endnote2 %}


{% note2 "**Définition**" %}
Un **_mutateur_** (**_setter_**) est une méthode dont le but est de modifier un attribut. On la nomme usuellement : `set_[nom de l'attribut](nouvelle_valeur)`{.language-}
{% endnote2 %}

En python cela s'écrirait ainsi :

```python
class Compteur:
    def __init__(self, pas=1, valeur=0):
        assert pas != 0
        self._pas = pas

        self.valeur = valeur

    # ...

    def get_pas(self):
        return self._pas

    def set_pas(self, pas):
        assert pas != 0
        self._pas = pas


```

- en python les variables privées sont précédées d'un `_`{.language-} pour prévenir le développeur qu'il ne faut pas qu'il utilise ces attributs directement (ce n'est qu'une convention)
- on utilise la fonction assert qui va faire planter le programme si on donne un pas valant 0.

### Attributs de classes

Chaque classe ayant un espace de nommage, rien ne nous empêche de l'utiliser pour autre chose que des méthodes. On peut par exemple écrire ce genre de choses en créant une classe de compteur à pas fixe, qui définit **un attributs de classes**, que l'on peut ensuite utiliser :

```python
class CompteurFixe:
    PAS = 1

    def __init__(self, valeur=0):
        self.valeur = 0
    
    def incrémente(self):
        self.valeur = self.valeur + type(self).PAS


```

On utilise explicitement le fait que `PAS`{.language-} est un attribut de la classe de l'objet. Notez que de par le fonctionnement des espaces de nommages, on aura plutôt tendance à écrire la chose suivante qui est équivalente (puisque `PAS`{.language-} n'est pas défini dans l'objet on le cherche dans sa classe):

```python
class CompteurFixe:
    PAS = 1

    def __init__(self, valeur=0):
        self.valeur = valeur
    
    def incrémente(self):
        self.valeur = self.valeur + self.PAS

```

## Méthodes spéciales

Pour rendre l'utilisation des objets pus agréable et intuitive, python va associer des méthodes spécifiques à des actions spécifiques. Ces méthodes sont appelées méthodes spéciales :

{% note2 "**Définition**" %}
**_Les méthodes spéciales_** de python se présentent sous la forme `__nom_de_la_méthode__`{.language-} et sont utilisés par python dans des cas spécifiques. [La documentation officielle](https://docs.python.org/3/reference/datamodel.html#special-method-names) les liste. Elles sont rès pratiques car elles permettent d'utiliser nos objets de façon intuitive, comme si on utilisait des objets de python (affichage à l'écran, comparaison, exécution comme une fonction, ...).
{% endnote2 %}

On a déjà vu une méthode spéciale : `__init__`{.language-} qui est exécutée lorsque l'on appelle une classe, mais il y en a bien d'autres. Nous allons en voir 2, très pratiques.

### Représentation sous la forme de chaînes de caractères

Essayez de taper dans le fichier `main.py`{.fichier} :

```python
c = Compteur()
print(c)
```

Vous devriez obtenir quelque chose comme :

```python
<__main__.Compteur object at 0x107149100>
```


Dans les projets dés et cartes on a créé une méthode `texte()`{.language-} qui rendait une chaîne de caractères pour ce genre de choses, mais python offre une possibilité plus simple en utilisant méthodes spéciales.

Ainsi, La méthode spéciale `__str__`{.language-} est utilisée lorsque l'on cherche à transformer un objet en chaîne de caractère avec [la fonction `str()`{.language-}](https://docs.python.org/fr/3.14/library/functions.html#str).

Ainsi si on défini :

```python
class Compteur
    # ...
    def __str__(self):
        return "Le compteur vaut " + str(self.valeur)
```

On pourra écrire :

```python
c = Compteur()
print(str(c))
```

Et qui va maintenant nous rendre :

```python
Le compteur vaut 0
```

Notez que pour la fonction `print`{.language-} on peut même écrire directement `print(c)`{.language-} car par défaut l'interpréteur python remplace `print(c)`{.language-} par `print(str(c))`{.language-}.

{% attention2 "**À retenir**" %}
La méthode `__str__`{.language-} permet : 

- de transformer un objet `o`{.language-} en chaîne de caractères via la fonctions `str(o)`{.language-}
- de l'afficher à l'écran en utilisant  `print(o)`{.language-} (qui est équivalent à `print(str(o))`{.language-}).
{% endattention2 %}

### <span id="comparaison"></span> Comparaisons

On pourrait avoir envie de comparer des valeurs de compteurs. On pourrait comparer directement les attributs, mais ce serait tout de même plus simple si l'on pouvait écrire :

```python

c1 = Compteur(valeur=1)
c2 = Compteur(valeur=4)

print(c1 < c2)

```

Pour l'instant, cela ne fonctionne pas. Si on teste ça avec votre code tel qu'il est, on obtiendra :

```text
TypeError: '<' not supported between instances of 'Compteur' and 'Compteur'
```

Python vous explique qu'il ne connaît pas l'opérateur `<`{.language-} pour les objets de notre classe. Pour pouvoir utiliser
directement les opérateurs `<`{.language-} et `<=`{.language-}, il faut définir respectivement les méthodes `__lt__(self, other)`{.language-} (_lower than_) et `__le__(self, other)`{.language-} (_lower or equal than_). On pourra aussi ajouter `__eq__(self, other)`{.language-} pour tester l'égalité.

Par exemple pour ajouter la comparaison _strictement plus petit que_, on ajoute la méthode :

```python
class Compteur
    # ...

    def __lt__(self, other):
        return self.valeur < other.valeur
    
    # ...
```

On peut aussi ajouter plus grant que et égal pour obtenir les comparaisons :

```python
class Compteur:

    # ...

    def __lt__(self, other):
        return self.valeur < other.valeur

    def __le__(self, other):
        return self.valeur <= other.valeur

    def __eq__(self, other):
        return other.valeur == self.valeur

    # ...
```

{% lien %}
Les différents opérateurs de comparaison que l'on peut ajouter à nos objets sont décrits [dans la documentation](https://docs.python.org/fr/3/reference/datamodel.html#object.__lt__).

{% endlien %}

## Code final

Notre compteur a bien évolué depuis sa première mouture. Il permet maintenant d'être utilisé de façon bien plus intuitive.

```python
class Compteur:
    def __init__(self, pas=1, valeur=0):
        assert pas != 0
        self._pas = pas

        self.valeur = valeur

    def get_pas(self):
        return self._pas

    def set_pas(self, pas):
        assert pas != 0
        self._pas = pas

    def incrémente(self):
        self.valeur = self.valeur + self.pas

    def __str__(self):
        return "Le compteur vaut " + str(self.valeur)

    def __lt__(self, other):
        return self.valeur < other.valeur

    def __le__(self, other):
        return self.valeur <= other.valeur

    def __eq__(self, other):
        return other.valeur == self.valeur

```