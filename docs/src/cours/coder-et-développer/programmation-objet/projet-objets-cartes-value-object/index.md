---
layout: layout/post.njk
title: "Projet : Amélioration des objets cartes"

eleventyNavigation:
  prerequis:
    - "../projet-objets-cartes/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


## Protéger les attributs

Une fois la carte créée, il ne faudrait plus pouvoir la modifier. Or pour l'instant on a directement accès aux attributs, donc rien n'interdit de le faire.

### Accesseurs

Pour pallier ça, il suffit de définir un accesseur sans mutateur pour les 2 attributs valeur et couleur. Cela permet :

- d'accéder aux attribut
- une tentative de modification produira une erreur

On a alors créé un **_value object_** c'est à dire un objet non mutable, comme un entier ou une chaîne de caractères en python.
{% faire %}

En utilisant [`@property`{.language-}](../projet-objets-dés-accesseur/#property){.interne}, créez et testez des accesseurs pour les attributs valeur et couleur.

{% endfaire %}

Si on a le choix :

{% note "**Méthode de conception**" %}
Lorsque l'on crée un objet, si on a pas de raison particulière de le rendre modifiable on crée un **_value object_**. Cela évite les effets de bords (et rend la programmation concurrente et parallèle bien plus simple).
{% endnote %}

### Enum

Pour spécifier à l'utilisateur les valeurs et couleurs possibles, on utilise pour l'instant des constantes et des tuples. Ceci n'est cependant pas optimal.

Pour gérer les énumérations, python met à disposition [les Enum](https://docs.python.org/fr/3/library/enum.html). On peut gérer les couleurs ainsi :

```python
>>> from enum import Enum
>>> couleur = Enum("Couleur", [("pique", 4), ("coeur", 3), ("carreau", 2), ("trefle", 1)])
>>> print(couleur.pique.name)
pique
>>> print(couleur.pique.value)
4
>>> c = couleur.pique
>>> c
<Couleur.pique: 4>
>>> for c in couleur:
...     print(c)
...
Couleur.pique
Couleur.coeur
Couleur.carreau
Couleur.trefle

```

{% faire %}

Utilisez des `Enum`{.language-} pour gérer les couleurs et les valeurs des cartes
{% endfaire %}

Cette technique est redoutable : elle est à la fois lisible, sans magic number et portable ! Utilisez-la dès que vous voulez gérer des énumérations.

## Affichage à l'écran

La méthode spéciale  `__str__`{.language-} permet de remplacer notre méthode `texte()`{.language-}

{% faire %}
Codez la méthode `__str__`{.language-} d'une carte. Le code suivant doit pouvoir fonctionner :

```python
>>> from carte import Carte, AS, PIQUE
>>> ace_pique = Carte(AS, PIQUE)
>>> print(ace_pique)
as de pique
```

Faites un test de cette méthode en testant la représentation sous la forme d'une chaîne de caractères d'une `Carte`{.language-}.
{% endfaire %}
{% info %}

La représentation sous la forme d'une chaîne de caractères un objet `x` est le résultat de `str(x)`{.language-}.

{% endinfo %}

Lorsque l'on écrit `print(ace_pique)`{.language-}, python transforme l'objet en chaîne de caractères avec la commande `str`{.language-} qui elle-même cherche la méthode `__str__`{.language-}. Les trois instructions suivantes sont donc équivalentes :

1. `print(ace_pique)`{.language-}
2. `print(str(ace_pique))`{.language-}
3. `print(ace_pique.__str__())`{.language-}

Vous verrez parfois une autre méthode de représentation d'un objet utilisant la commande `repr()`{.language-}. Cette fonction doit permettre de reconstruire l'objet si nécessaire.

Par exemple :

```python
>>> from carte import Carte
>>> ace_pique = Carte("as", "pique")
>>> print(repr(ace_pique))
Carte('as', 'pique')
```

On utilise souvent `repr()`{.language-} pour du débogage (donc de l'affichage développeur), alors que `str()`{.language-} est utilisé pour de l'affichage utilisateur.

{% note %}

- on utilise `str(objet)` (créée avec la méthode `__str__`{.language-}) pour un affichage à l'écran. On transforme l'objet en un texte.
- on utilise `repr(objet)` (créée avec la méthode `__repr__`{.language-}) pour représenter l'objet sous la forme d'une chaîne de caractères. On doit pouvoir reconstruire un objet identique avec la commande [`eval`{.language-}](https://docs.python.org/fr/3/library/functions.html#eval) (`eval(repr(objet))`{.language-} doit rendre un objet similaire à `objet`{.language-}.

{% endnote %}

{% lien %}
Un petit tuto français pour expliciter les différences entre les deux représentations : <https://www.youtube.com/watch?v=ejGYAnf_X24>
{% endlien %}

{% exercice %}
Créez et testez la méthode `__repr__`{.language-}
{% endexercice %}
{% details "corrigé" %}

```python
class Carte:
    # ...

    def __repr__(self):
        return "Carte(" + repr(self.valeur) + ", " + repr(self.couleur) + ")"
    
    # ...

```

{% enddetails %}

## Comparaisons de cartes

Ajoutez à votre classe carte les opérateurs de comparaisons :

{% faire %}
Codez et testez les [opérateurs de comparaisons](../classes-et-objets/#comparaison){.interne} :

- `==`{.language-} qui correspond a à la méthode `__eq__`{.language-}
- `!=`{.language-} qui correspond a à la méthode `__ne__`{.language-}
- `<`{.language-} qui correspond a à la méthode `__lt__`{.language-}
- `>`{.language-} qui correspond a à la méthode `__gt__`{.language-}
- `<=`{.language-} qui correspond a à la méthode `__le__`{.language-}
- `>=`{.language-} qui correspond a à la méthode `__ge__`{.language-}

{% endfaire %}
{% info %}
N'hésitez pas à utiliser des opérateurs déjà codé. Vous pouvez par exemple utiliser les fonctions `==`{.language-} et `<`{.language-} pour coder les autres les comparaisons.
{% endinfo %}

## Refactoring

{% faire %}
Modifiez le code de la user story _"Ordonnancement"_ et du jeu en utilisant directement les comparateurs.
{% endfaire %}