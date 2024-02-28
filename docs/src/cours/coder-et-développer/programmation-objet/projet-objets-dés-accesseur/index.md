---
layout: layout/post.njk
title: "Projet : Amélioration des objets dés"

eleventyNavigation:
  prerequis:
    - "../projet-objets-dés-accesseur/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous allons améliorer le code du dés pour accéder aux attributs de l'objet de façon indirecte. Lorsqu'un attribut d'un objet est soumis à un contrôle, par exemple position qui ne peut prendre comme valeur des entiers entre 1 et 6, il est de coutume de ne pas accéder directement à celui-ci, mais de passer par des méthodes pour le modifier et y accéder

## Mutateur ou _setter_

{% note %}
Un **_mutateur_** (**_setter_**) est une méthode dont le but est de modifier un attribut. On la nomme usuellement : `set_[nom de l'attribut](nouvelle_valeur)`{.language-}
{% endnote %}

{% faire %}
Créez une méthode `Dé.set_position(nouvelle_position)`{.language-} qui modifie la position du dé.

Faites en sorte que la position ne puisse être plus petite que 1 (si `nouvelle_position`{.language-} < 1 alors l'attribut vaut 1) ni plus grande que 6 (si `nouvelle_position`{.language-} > 6 alors l'attribut vaut 6).

Créez un test pour la méthode `Dé.set_position(nouvelle_position)`{.language-} et modifiez, s'ils y en a, les tests qui modifient directement l'attribut positions pour qu'ils utilisent le _setter_.

{% endfaire %}

Le but est de faire disparaître l'utilisation directe de l'attribut dans le code. Une fois qu'on ne le verra plus, c'est comme s'il n'existait plus.

Avant de continuer, nous allons éliminer les 2 constantes non nommées 1 et 6 que nous venons certainement de créer (si vous ne l'avez pas fait, bravo !).

Les nombres 1 et 6 sont les bornes du dé, il faut les nommer en tant que tel, sinon on va oublier leur signification et le code sera plus dire à modifier plus tard :

<span id="mantra-no-magic-numbers"></span>
{% note "**Coding mantra**" %}

[NO MAGIC NUMBER](<https://fr.wikipedia.org/wiki/Nombre_magique_(programmation)#Constantes_num%C3%A9riques_non_nomm%C3%A9es>)
{% endnote %}

{% faire %}
Ajouter les constantes `MIN_VALEUR = 1`{.language-} et `MAX_VALEUR = 6`{.language-} dans le fichier `dé.py`{.fichier} et utilisez les dans tout le code. Y compris le test du lacer de dé.
{% endfaire %}

{% info %}
Changer ses valeurs changera la nature de tous les dés crées.

{% endinfo %}

## Accesseur ou _getter_

Si l'on veut accéder à un attribut sans l'utiliser directement, il faut le faire _via_ une méthode. Cela peut être pratique si l'attribut n'est pas directement donné dans l'objet mais est construit (par exemple des coordonnées polaires d'un objet point2D où ses attributs sont en réalité ses coordonnées cartésiennes)

{% faire %}
Créez une méthode `Dé.get_position()`{.language-} qui rend la position du dé.

Créez un test pour cette méthode.
{% endfaire %}

Afin de faire disparaître l'existence de l'attribut dans le code :

{% faire %}
modifiez tous les tests et les codes des programmes qui utilisent directement l'attribut `position`{.language-} pour qu'ils utilisent l'accesseur.
{% endfaire %}

On peut maintenant rendre l'attribut `position`{.language-} privé.

{% note "**Définition**" %}
Un attribut **_privé_** est un attribut qui ne doit pas être utilisé autre-part que dans les définitions de méthodes de la classe. Les attribut directement utilisables dans le code sont dit **_public_**.

Tout code voulant accéder ou modifier à cet attribut **doit** passer par son accesseur/mutateur.
{% endnote %}

En python, un attribut privé est précédé d'**un** `_`{.language-}. Par exemple, l'attribut `position`{.language-} est public alors que l'attribut `_position`{.language-} est privé.

{% faire %}
Rendez l'attribut `position`{.language-} de la classe `Dé`{.language-} privé.
{% endfaire %}

En python, la notion d'attribut privé ou public n'existe pas vraiment, ce sont juste des conventions entre codeur. Il est ainsi tout à fait possible d'utiliser un attribut privé partout (mais c'est _bad karma_). Le seul endroit où l'utilisation directe d'un attribut privé est autorisé, c'est dans le test de son accesseur.

## <span id="property"></span> Property

Python a une superbe fonctionnalité qui permet d'utiliser les accesseur les mutateur _comme_ si l'on utilisait directement un attribut !

{% lien %}
[Le décorateur `@property`{.language-}](https://docs.python.org/fr/3.11/library/functions.html#property)
{% endlien %}

La façon la plus clair d'utiliser cela est d'utiliser des [décorateurs](https://realpython.com/primer-on-python-decorators/). Leur utilisation générale en programmation dépasse le cadre de ce cours, nous allons juste utiliser ceux de python permettant de décorer des accesseurs et des mutateurs ici.

Considérons une classe qui possède, entre autres choses un attribut nommé `toto`{.language-} :

```python

class MaClasse:
   def __init__(self):
      # ...

      self.toto = 0

      # ...

   # ...

```

Cet attribut est public et on peut l'utiliser librement :

```python
>>> mon_objet = MaClasse()
>>> mon_objet.toto = 42
>>> print(mon_objet.toto)
```

Si l'on rend cet attribut privé, il faut utiliser des accesseurs/mutateurs :

```python

class MaClasse:
   def __init__(self):
      self._toto = 0

   def get_toto(self):
      return self._toto

   def set_toto(self, nouveau_toto):
      self._toto = nouveau_toto

```

C'est plus safe, car maintenant, on peut faire attention à ce que l'on donne comme valeur à l'attribut, mais son utilisation est bien plus lourde :

```python
>>> mon_objet = MaClasse()
>>> mon_objet.set_toto(42)
>>> print(mon_objet.get_toto())
```

Python permet de combiner les deux approches avec les décorateurs `@property`{.language-} :

```python

class MaClasse:
   def __init__(self):
      self._toto = 0

   @property
   def toto(self):
      return self._toto

   @toto.setter
   def toto(self, nouveau_toto):
      self._toto = nouveau_toto

```

Ce qu'on a fait :

- on _décore_ la première méthode `MaClasse.toto()`{.language-} par le décorateur `@property`{.language-} pour lui signifier que cette méthode est l'accesseur de l'attribut `toto`{.language-}
- on _décore_ la seconde méthode `MaClasse.toto()`{.language-} par le décorateur `@toto.setter`{.language-} pour signifier que cette méthode est le mutateur de l'attribut `toto`{.language-}

L'utilisation est alors pratique comme un attribut public et safe comme un attribut privé :

```python
>>> mon_objet = MaClasse()
>>> mon_objet.toto = 42  # c'est le mutateur qui est utilisé par directement l'attribut
>>> print(mon_objet.toto)  # c'est l'accesseur qui est utilisé par directement l'attribut
```

{% faire %}
Utilisez l'attribut privé `Dé._position`{.language} avec un décorateur `@property`{.language-}.

Modifiez tous les tests et les programmes principaux.
{% endfaire %}

## Finalement

{% faire %}
Vérifier que tout fonctionne :

- les tests
- la user story
- le programme principal

{% endfaire %}
