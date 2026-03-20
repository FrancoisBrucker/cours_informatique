---
layout: layout/post.njk
title: Améliorer ses objets

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- TBD 

à mettre à la fin :

supprimer str d'ici et ne mettre que repr

parler d'attributs de classes aussi

et enfin pur les property, utiliser : x = property(get, set) <https://docs.python.org/3/library/functions.html#property> et dire que l'on peut aussi le faire avec des décorateur
-->


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


## Représentation sous la forme de chaînes de caractères

Essayez de taper dans le fichier `main.py`{.fichier} :

```python
c = Compteur()
print(c)
```

Vous devriez obtenir quelque chose comme :

```python
<__main__.Compteur object at 0x107149100>
```

Ce n'est pas vraiment très lisible. Python offre des méthodes spéciales qui nous permettent de représenter un objet lorsque l'on veut l'afficher. Ces méthodes se présentent toujours sous la forme `__nom_de_la_méthode__`{.language-} et sont utilisés par python dans des cas spécifiques. On a déjà vu `__init__`{.language-}, mais il y en a beaucoup d'autres (voir la [documentation officielle](https://docs.python.org/3/reference/datamodel.html#special-method-names)). Elles sont rès pratiques car elles permettent d'utiliser nos objets de façon intuitive, comme si on utilisait des objets de python (affichage à l'écran, comparaison, exécution comme une fonction, ...).

### Sérialisation des objets 

La façon la plus classique de représenter un objet sous la forme d'[une sérialisation](https://en.wikipedia.org/wiki/Serialization), c'est à dire une chaîne de caractère permettant de reconstruire l'objet si nécessaire. En python cela la signifie souvent écrire l'objet sous la forme d'un appel à un constructeur :

```python
class Compteur
    # ...
    def __repr__(self):
        return "Compteur(pas=" + str(self.pas) + ", valeur=" + str(self.valeur) + ")"
```

La méthode spéciale `__repr__`{.language-} va être utilisée par défaut lorsque l'on doit représenter l'objet sous la forme d'une chaîne de caractères. Avec l'ajout de la méthode spéciale ci-dessus, le code suivant :

```python
c = Compteur(pas=12)
c.incrémente()
c.incrémente()
print(c)
```

va afficher :

```python
Compteur(pas=12, valeur=24)
```

La méthode spéciale `__repr__`{.language-} est appelée via [la fonction `repr()`{.language-}](https://docs.python.org/fr/3.14/library/functions.html#repr) de python :

```python
c = Compteur(pas=12)
c.incrémente()
c.incrémente()
print(repr(c))
```

Et cela marche même pour les listes ! Le code suivant :

```python
c = Compteur(pas=12)
c.incrémente()
c.incrémente()
l = [c]
print(l)
```

Va afficher : `[Compteur(pas=12, valeur=24)]`{.language-}

{% attention2 "**À retenir**" %}
Codez une méthode `__repr__`{.language-} pour toutes vos classes. Il est toujours utile d'avoir une sérialisation de ses objets.
{% endattention2 %}

### Affichage

Pour être totalement exhaustif, la fonction `print`{.language-} de python n'appelle pas la fonction `repr()`{.language-}, mais la [la fonction `str()`{.language-}](https://docs.python.org/fr/3.14/library/functions.html#repr) dont le but est de transformer un objet en chaîne de caractères en vue de son affichage à l'écran : il n'est pas nécessaire de pouvoir recréer l'objet à partir de sa représentation, mais juste d'informer l'utilisateur de la valeur d'un objet. Par exemple pour notre compteur :

```python
class Compteur
    # ...
    def __str__(self):
        return "Le compteur vaut " + str(self.valeur)
```

Avec cette nouvelle méthode le code suivant `print(Compteur())`{.language-} affichera `le compteur vaut 0`{.language-} à l'écran. On ne peut pas reconstruire l'objet (il manque son pas) mais montre bien la grandeur pertinente à présenter à l'utilisateur.

Quand est utilisé `repr()`{.language-} ou `str()`{.language-} dépend des cas. Par défaut on conseille de ne coder la méthode `__str__`{.language-} que si c'est nécessaire et sinon de se contenter de sa sérialisation (c'est le résultat de `repr(self)`{.language-} qui est rendu par défaut). 

{% attention2 "**À retenir**" %}
Ne créez la méthode `__str__`{.language-} que si vous avez besoin d'avoir un affichage pour l'utilisateur différent d'une sérialisation.
{% endattention2 %}

### Les méthodes pour le compteur

Notre compteur devient :

```python
class Compteur:
    def __init__(self, pas=1, valeur=0):
        self.valeur = valeur
        self.pas = pas

    def incrémente(self):
        self.valeur = self.valeur + self.pas

    def __repr__(self):
        return "Compteur(pas=" + str(self.pas) + ", valeur=" + str(self.valeur) + ")"

    def __str__(self):
        return "Le compteur vaut " + str(self.valeur)

```


## <span id="comparaison"></span> Comparaison

On pourrait avoir envie de comparer des valeurs de compteurs. On pourrait comparer directement les attributs, mais ce serait tout de même plus simple si l'on pouvait écrire :

```python

c1 = Compteur(valeur=1)
c2 = Compteur(valeur=4)

print(c1 < c2)

```

Pour l'instant, cela ne fonctionnepas. Si on teste ça avec votre code tel qu'il est, on obtiendra :

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

On peut aussi ajouter plus grant que et égal pour obtenir les comparaisons :

```python
class Compteur:

    # ...

    def __lt__(self, other):
        return self.valeur < other.valeur

    def __gt__(self, other):
        return other.valeur < self.valeur

    def __eq__(self, other):
        return other.valeur == self.valeur

```

{% lien %}
Les différents opérateurs de comparaison que l'on peut ajouter à nos objets sont décrits [dans la documentation](https://docs.python.org/fr/3/reference/datamodel.html#object.__lt__).

{% endlien %}

## Utiliser des méthodes comme des attributs

Pour notre compteur, on peut accéder directement aux attributs `valeur`{.language-} et `pas`{.language-}. On pourrait avoir envie de ne tolérer que des pas non nul mais pour l'instant rien ne nous empêche d'écrire :

```python
c = Compteur()
c.pas = 0
```

Et de créer un compteur qui n'incrémente jamais...

Pour éviter cela, on peut :

- restreindre l'accès à l'attribut `valeur` : rendre l'attribut _privé_
- permettre de modifier l'attribut `valeur` qu'en utilisant une méthodes spécifique : un _mutateur_

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

        self.valeur = valeur
        self._pas = pas

    # ...

    def get_pas(self):
        return self._pas

    def set_pas(self, pas):
        assert pas != 0
        self._pas = pas


```

- en python les variables privées sont précédées d'un `_`{.language-} pour prévenir le développeur qu'il ne faut pas qu'il utilise ces attributs directement (ce n'est qu'une convention)
- on utilise la fonction assert qui va faire planter le programme si on donne un pas valant 0.

Le code précédent alourdi le code et force l'utilisation de méthodes alors que c'est bien un attribut que l'on modifie. Python a une superbe fonctionnalité qui permet d'utiliser les accesseur les mutateur _comme_ si l'on utilisait directement un attribut !

{% lien %}
- [les décorateurs python](https://realpython.com/primer-on-python-decorators/)
- [Le décorateur `@property`{.language-}](https://docs.python.org/fr/3.11/library/functions.html#property)
{% endlien %}

L'utilisation générale des décorateur dépasse le cadre de ce cours, nous allons juste utiliser ceux de python permettant de décorer des accesseurs et des mutateurs ici. Le code suivant utilise le décorateur property qui transforme les accesseur en attributs :


```python
class Compteur:
    def __init__(self, pas=1, valeur=0):
        assert pas != 0

        self.valeur = valeur
        self._pas = pas

    # ...

    @property
    def pas(self):
        return self._pas

    @property.setter
    def pas(self, pas):
        assert pas != 0
        self._pas = pas


```

On peut maintenant écrire le code suivant :

```python
c = Compteur()
c.pas = 12
```

Qui utilisera le mutateur en sous-main.

{% info %}
Si on ne veut pas permettre de modifier un attribut, il suffit de ne coder que l'accesseur et non le mutateur !
{% endinfo %}

## Méthodes/attributs de classes

Terminons cette partie par une amélioration souvent pratique, les méthodes de classes. Ce sont des méthodes :

- dont le premier paramètre est la classe et non l'objet
- qui sont utilisées via la classe

Le principal intérêt des méthodes de classes et de permettre des créations alternatives des objets. 

### Méthodes de classes

Par exemple pour notre compteur on pourrait avoir la méthode suivante :

```python
class Compteur:
    # ...

    @classmethod
    depuis_compteur(cls, compteur):
        return cls(compteur.pas, compteur.valeur)

    # ...
```

Ce qui nous permet d'écrire le code suivant qui crée des objets de type compteur en utilisant comme paramètre un autre compteur :

```python

c = Compteur()
c.incrémente()

c_copie = Compteur.depuis_compteur(c)
```

On voit que les méthodes de classes :

- sont définies via un décorateur
- leur premier argument est la classe
- sont appelées en utilisant la notation pointée depuis la classe

{% note2 "**Définition**" %}

**_Les méthodes de classes_** fonctionnent comme les méthodes classiques sauf que :

- elles sont appelées en utilisant une classe et pas un objet pour la notation pointée
- le premier paramètre dans leur définition est la classe (nommé `cls`{.language-}) et pas un objet

{% endnote2 %}

### Attributs de classes

> TBD

## Code final

Notre compteur a bien évolué depuis sa première mouture. Il permet maintenant d'être utilisé de façon bien plus intuitive.

```python
class Compteur:
    @classmethod
    depuis_compteur(cls, compteur):
        return cls(compteur.pas, compteur.valeur)

    def __init__(self, pas=1, valeur=0):
        assert pas != 0

        self.valeur = valeur
        self._pas = pas

    @property
    def pas(self):
        return self._pas

    @property.setter
    def pas(self, pas):
        assert pas != 0
        self._pas = pas

    def incrémente(self):
        self.valeur = self.valeur + self.pas

    def __repr__(self):
        return "Compteur(pas=" + str(self.pas) + ", valeur=" + str(self.valeur) + ")"

    def __str__(self):
        return "Le compteur vaut " + str(self.valeur)

    def __lt__(self, other):
        return self.valeur < other.valeur

    def __gt__(self, other):
        return other.valeur < self.valeur

    def __eq__(self, other):
        return other.valeur == self.valeur

```