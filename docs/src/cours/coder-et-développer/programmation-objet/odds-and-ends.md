---
layout: layout/post.njk
title: "Autres améliorations"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous montrons ici quelques améliorations parfois utiles pour nos classes. Il n'est pas fondamental de les connaître lorsque l'on débute, mais deviennent (très) utiles lorsque l'on commence à prendre de la bouteille.

## Sérialisation des objets 

La façon la plus classique de représenter un objet sous la forme d'un texte est, [on l'a vu](../améliorer-ses-objets/#str){.interne}, d'utiliser la fonction `str()`{.language-} en combinaison avec la méthode spéciale `__str__`{.language-}. Cette représentation textuelle a pour but d'être affichée à l'écran.

Il existe une autre représentation textuelle, appelée [sérialisation](https://en.wikipedia.org/wiki/Serialization) :

{% note2 "**Définition**" %}
La sérialisation d'un objet est sa transformation sous une forme textuelle permettant de le reconstituer.
{% endnote2 %}

Par exemple la chaîne de caractère `"42" `{.language-} permet de reconstruire un objet de type entier valant $42$, on encore `"[1, 2, 3, 4]" `{.language-} permet de reconstruire une liste d'entiers.

L'appel à la sériation se fait en python en utilisant [la fonction `repr()`{.language-}](https://docs.python.org/fr/3.14/library/functions.html#repr) :

```python
>>> repr(1)
'1'
>>> repr([1, 2, 3, 4])
'[1, 2, 3, 4]'
``` 

Une forme classique de sérialisation consiste à écrire la chaîne de caractère qui permettrait de le créer, c'est à dire une chaîne de caractère permettant de reconstituer ses attributs. En programmation objet cela la signifie souvent écrire l'objet sous la forme d'un appel à un constructeur, si celui ci prend tous les paramètres en paramètre. Par exemple pour notre compteur dont le constructeur est :

```python
class Compteur:
    def __init__(self, pas=1, valeur=0):
        self.pas = pas
        self.valeur = valeur

    # ...

```

La sérialisation, appelée via la fonction spéciale `__str__`{.language-} consisterait en :

```python
class Compteur
    # ...
    def __repr__(self):
        return "Compteur(pas=" + str(self.pas) + ", valeur=" + str(self.valeur) + ")"
```

On a alors

```python
c = Compteur(pas=12)
c.incrémente()
c.incrémente()
print(repr(c))
```

va afficher :

```python
Compteur(pas=12, valeur=24)
```

Remarquez la différence avec `str`{.language-} qui est définie comme :

```python
class Carte:
    # ...

    def __str__(self):
        return "Le compteur vaut " + str(self.valeur)
    
    # ...

```

Et qui ne permet pas de reconstituer le compteur (il manque son pas) :

```python
c = Compteur(pas=12)
c.incrémente()
c.incrémente()
print(repr(c))
print(c)
```

va afficher :

```python
Compteur(pas=12, valeur=24)
Le compteur vaut 24
```


Il est toujours utile d'avoir une sérialisation de ses objets car on peut l'utiliser aussi pour l'afficher.

{% attention2 "**À retenir**" %}
En première approche, codez une méthode `__repr__`{.language-} pour toutes vos classes car par défaut si l'on ne définit par `__str__`{.language-}, c'est `__repr__`{.language-} qui est utilisé (le `__str__`{.language-} de la classe object rend le résultat de son `__repr__`{.language-}).

{% endattention2 %}

## Utiliser des méthodes comme des attributs

Pour notre compteur, on peut accéder directement aux attributs `valeur`{.language-} et `pas`{.language-}. On pourrait avoir envie de ne tolérer que des pas non nul mais pour l'instant rien ne nous empêche d'écrire :

```python
c = Compteur()
c.pas = 0
```

Et de créer un compteur qui n'incrémente jamais...

Pour éviter cela, on a vu que l'on pouvait [rendre l'attribut privé](../améliorer-ses-objets/#privé){.interne} et y accéder via des accesseurs :

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

Le code précédent alourdi le code et force l'utilisation de méthodes alors que c'est bien un attribut que l'on modifie. Python a une superbe fonctionnalité qui permet d'utiliser les accesseurs les mutateurs _comme_ si l'on utilisait directement un attribut ! Pour cela on utilise [la classe `property`{.language-}](https://docs.python.org/fr/3.11/library/functions.html#property) de python, qui s'écrit comme une variable de classe :

```python
class Compteur:
    def __init__(self, pas=1, valeur=0):
        assert pas != 0
        self._pas = pas

        self.valeur = valeur

    # ...

    def _get_pas(self):
        return self._pas

    def _set_pas(self, pas):
        assert pas != 0
        self._pas = pas

    pas = property(_get_pas, _set_pas)
```

On a rendu les accesseurs privé et peut les utiliser maintenant comme un attribut :

On peut maintenant écrire le code suivant :

```python
c = Compteur()
c.pas = 12
```

Qui utilisera le mutateur en sous-main. Si on ne veut pas permettre de modifier un attribut, il suffit de ne coder que l'accesseur et non le mutateur, par exemple si on ne veut veut pas laisser l'utilisateur modifier la valeur mais qu'on veut qu'il puisse la consulter on peut :

```python
class Compteur:
    def __init__(self, pas=1, valeur=0):
        assert pas != 0
        self._pas = pas

        self._valeur = valeur

    # ...

    def _get_valeur(self):
        return self._valeur

    valeur = property(_get_valeur)
```

Affecter une valeur produira une erreur :

```python
>>> c = Compteur()
>>> print(c.valeur)
0
>>> c.valeur = 12
Traceback (most recent call last):
  File "<python-input-27>", line 1, in <module>
    c.valeur = 12
    ^^^^^^^^
AttributeError: property 'valeur' of 'Compteur' object has no setter
```


## Méthodes de classes

On a déjà vu [les attributs de classes](../améliorer-ses-objets/#attribut-classe){.interne}, on peut faire pareil avec les méthodes. 

{% note2 "**Définition**" %}
Une **_méthode de classe_** est une méthode dont le premier paramètre est la classe de l'objet et non l'objet en lui même.

On peut les utiliser via la notation pointée avec la classe à gauche du point ou l'objet.

{% endnote2 %}

Le principal intérêt des méthodes de classes et de permettre des créations alternatives des objets. Par exemple pour notre compteur on pourrait avoir la méthode de classe suivante, définie par _un décorateur_ `@classmethod`{.language-} placé juste au-dessus de sa définition :

```python
class Compteur:
    # ...

    @classmethod
    depuis_compteur(cls, compteur):
        return cls(compteur.pas, compteur.valeur)

    # ...
```

Cette fonction nous permet d'écrire le code suivant qui crée des objets de type compteur en utilisant comme paramètre un autre compteur :

```python

c = Compteur()
c.incrémente()

c_copie = Compteur.depuis_compteur(c)
```

La ligne `@classmethod`{.language-} est ce qu'on appelle un décorateur. Python en utilise un peut partout pour spécifier l'utilisation des fonctions décorées. Par exemple pour définir :

- [les méthodes de classes](https://docs.python.org/3/library/functions.html#classmethod) comme on l'a vu
- [les méthodes statiques](https://docs.python.org/3/library/functions.html#staticmethod),
- [les propriétés](https://docs.python.org/fr/3.11/library/functions.html#property)
- ...

Créer ses propres décorateurs dépasse le cadre de cette introduction, sachez juste les utiliser. Si le sujet vous intéresse vous pourrez cependant regarder le lien suivant :

{% lien %}
[Les décorateurs en python](https://realpython.com/primer-on-python-decorators/).
{% endlien %}

## Autres méthodes spéciales

Il existe une foultitude de méthodes spéciales en python permettant de rendre vos objets plus agréable à coder :

{% lien %}
[Tutoriel sur les méthodes spéciales](https://gayerie.dev/docs/python/python3/dunder.html)
{% endlien %}

On peut citer :

- `__call__`{.language-} pour appeler un objet comme une fonction
- `__add__`{.language-}, pour additionner nos objets avec `+`{.language-}
- `__len__`{.language-} pour utiliser `len`{.language-} sur nos objets
- `__setitem__`{.language-} et `__getitem__`{.language-} pour simuler un conteneur
- ...

## Code final

Notre compteur a bien évolué depuis sa première mouture. Il permet maintenant d'être utilisé de façon bien plus intuitive.

```python
class Compteur:
    @classmethod
    depuis_compteur(cls, compteur):
        return cls(compteur.pas, compteur.valeur)

    def __init__(self, pas=1, valeur=0):
        assert pas != 0

        self._valeur = valeur
        self._pas = pas

    def _get_valeur(self):
        return self._valeur

    valeur = property(_get_valeur)

    def _get_pas(self):
        return self._pas

    def _set_pas(self, pas):
        assert pas != 0
        self._pas = pas
    
    pas = property(_get_pas, _set_pas)


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
