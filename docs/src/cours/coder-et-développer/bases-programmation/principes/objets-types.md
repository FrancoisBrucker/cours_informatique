---
layout: layout/post.njk 
title: Objets types et types d'objets

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Python connaît 6 classes d'objets de base qui permettent de faire la grande majorité des programmes.

{% info %}
Utilisez la console de <https://console.basthon.fr/> pour exécuter les divers exemples et exercices
{% endinfo %}

## Six classes de base

{% lien "**Documentation**" %}
<https://docs.python.org/fr/3/library/stdtypes.html#built-in-types>
{% endlien %}

* Chaînes de caractères
  * exemple : `"python"`{.language-} ou `'python'`{.language-}
  * quelque chose qui commence et fini par `"`{.language-} ou qui commence et fini par `'`{.language-} ou encore qui commence et fini par `"""`{.language-}.
* Réels
  * exemple : `2.91`{.language-} ou `2.0`{.language-}
  * un nombre avec une décimale (qui peut être nulle) notée par un `.`{.language-}
* Entiers
  * exemple : `42`{.language-} ou `0`{.language-}
  * un nombre sans décimale
* Complexes (la notation utilise j à la place de i)
  * exemple : `3+2j`{.language-}, `1j`{.language-}
  * un réel ou entier avec une partie imaginaire, notée `j`{.language-}, entière ou imaginaire.
* Booléens
  * exemple : `True`{.language-} ou `False`{.language-}
  * que 2 possibilités, `True`{.language-} ou `False`{.language-}
* le vide, utilisé pour noter l'absence de valeur
  * ne contient qu'un unique élément noté `None`{.language-}

{% note %}
Tout objet de python à sa classe.
{% endnote %}

## Classes d'un objet

Tout objet a une ***classe***, aussi appelé ***type***. Pour connaître la classe d'un objet, on peut utiliser la fonction `type`{.language-}. Par exemple :

```python
type(42) 
```

Qui rendra :  `<class 'int'>`{.language-}. Les entiers sont donc de classe `'int'`{.language-} en python.

{% exercice %}
Dans la console de <https://console.basthon.fr/>, donnez la classe de chaque objet de base/
{% endexercice %}

{% details "solution" %}

```python
>>> type("2")
<class 'str'>
>>> type(2.0)
<class 'float'>
>>> type(2)
<class 'int'>
>>> type(2+0j)
<class 'complex'>
>>> type(True)
<class 'bool'>
```

{% enddetails %}

## Changer de classe

Il est possible de créer un nouvel objet à partir d'un objet d'une autre classe en le convertissant. Supposons que l'on veuille convertir un objet `b`{.language-} dans la classe de nom `classe_a`{.language-} Pour cela, on utilise le nom de la classe de destination, suivie d'une parenthèse où l'on place notre objet à convertir (comme si `classe_a`{.language-} était une fonction) :

```python
classe_a(objet_de_classe_b)  # transforme l'objet b en objet de classe classe_a
```

### Réels, entiers et chaînes de caractères

On peut par exemple transformer un réel en entier :

{% exercice %}
Quel est le résultat de l'instruction suivante :
{% endexercice %}

```python
int(3.1415)
```

{% details "solution" %}

```python
>>> int(3.1415)
3
```

C'est un entier valant 3.

{% enddetails %}

Ou en entier en réel :

{% exercice %}
Quel est le résultat de l'instruction suivante :
{% endexercice %}

```python
float(3)
```

{% details "solution" %}

```python
>>> float(3)
3.0
```

C'est un réel valant 3.0

{% enddetails %}

On peut aussi transformer une chaîne de caractères en entier ou en réel. Par exemple :

```python
float("3.1415")
```

Va rendre un objet réel valant 3.1415 à partir d'une chaîne de caractère avec le caractère "3.1415".

{% attention %}
Une chaîne de caractère n'est **pas** un réel ou un entier.
{% endattention %}

{% note %}
La conversion de chaînes de caractères en entier ou en réels est très courante lorsque l'on récupère des entrées tapées par un utilisateur qui sont **toujours** des chaînes de caractères
{% endnote %}

### Conversion booléennes

On effectue souvent ce genre d'opération de façon implicite pour les booléens. Ainsi, un entier est vrai s'il est non nul.

{% exercice %}
Vérifiez le.
{% endexercice %}
{% details "solution" %}

```python
>>> bool(42)
True
```

{% enddetails %}

Tous les objets peuvent être converti en booléen.

{% exercice %}
Quand-est qu'une chaîne de caractère est fausse ?
{% endexercice %}

{% details "solution" %}

Une chaîne de caractère est fausse si elle est vide et vraie sinon.

```python
>>> bool("")
False
>>> bool("False")
True
```

{% enddetails %}

On peut aussi faire le contraire :

{% exercice %}
Que vaut la conversion de booléens en entier ?
{% endexercice %}

{% details "solution" %}

Une chaîne de caractère est fausse si elle est vide et vraie sinon.

```python
>>> int(True)
1
>>> int(False)
0
```

{% enddetails %}

### Conversions impossibles

Il n'est pas possible de convertir tout en tout bien sur, par exemple `int("quarante-deux")`{.language-} produit une erreur.
