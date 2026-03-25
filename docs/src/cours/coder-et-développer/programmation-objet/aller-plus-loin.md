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

supprimer repr d'ici et ne mettre que str

parler d'attributs de classes aussi

et enfin pur les property, utiliser : x = property(get, set) <https://docs.python.org/3/library/functions.html#property> et dire que l'on peut aussi le faire avec des décorateur
-->



## Représentation sous la forme de chaînes de caractères

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

> TBD différent de affichage.

### Les méthodes pour le compteur

Notre compteur devient :

```python
class Compteur:
    # ...

    def __repr__(self):
        return "Compteur(pas=" + str(self.pas) + ", valeur=" + str(self.valeur) + ")"

    # ...
```


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


### Attributs

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


