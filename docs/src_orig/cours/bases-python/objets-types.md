---
layout: page
title:  "Bases de python : Objets types et types d'objets"
authors: 
    - Augustin Agbo-Kpati
    - François Brucker
    - Pascal Préa
---

> [bases de python]({% link cours/bases-python/index.md %}) / [objets types et types d'objets]({% link cours/bases-python/objets-types.md %})
{: .chemin}


Python connaît 5 classes d'objets de base qui permettent de faire la grande majorité des programmes.

> Utilisez <https://basthon.fr/> en console pour exécuter les divers exemples et exercices

## Les 6 classes de base

>[Documentation correspondante](https://docs.python.org/3/library/stdtypes.html#built-in-types).

* Chaînes de caractères
  * exemple : `"python"` ou `'python'`
  * quelque chose qui commence et fini par `"` ou qui commence et fini par `'` ou encore qui commence et fini par `"""`.
* Réels
  * exemple : `2.91` ou `2.0`
  * un nombre avec une décimale (qui peut être nulle) notée par un `.`
* Entiers
  * exemple : `42` ou `0`
  * un nombre sans décimale
* Complexes (la notation utilise j à la place de i)
  * exemple : 3+2j, 1j
  * un réel ou entier avec une partie imaginaire, notée `j`, entière ou imaginaire.
* Booléens
  * exemple : `True` ou `False`
  * que 2 possibilités, `True` ou `False`
* le vide, utilisé pour noter l'absence de valeur
  * ne contient qu'un unique élément noté `None`

> Tout objet de python à sa classe.

## classes d'un objet

Tout objet a un *type*, aussi appelé *classe*. Pour connaître la classe d'un objet, on peut utiliser la fonction `type` :

```python
type(42) 
```

Qui rendra :  `<class 'int'>`. Les entiers sont donc de classe `'int'` en python.

> Utiliser <https://basthon.fr/> en console pour connaître la classe de chaque objet de base.
{: .a-faire}

{% details solution %}

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
```

{% enddetails %}

## changer de classe

Il est possible de créer un nouvel objet à partir d'un objet d'une autre classe en le convertissant. Pour cela, on utilise le nom de la classe comme une fonction : `a(b)` convertissant l'objet `b` dans un objet de la classe `a`.

### réels, entiers et chaînes de caractères

On peut par exemple transformer un réel en entier :

```python
int(3.1415)
```

> Quel est le résultat de cette instruction ?
{: .a-faire}

{% details solution %}

```python
>>> int(3.1415)
3
```

C'est un entier valant 3.

{% enddetails %}

Ou en entier en réel : 

```python
float(3)
```

> Quel est le résultat de cette instruction ?
{: .a-faire}

{% details solution %}

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

> Une chaîne de caractère n'est **pas** un réel ou un entier.
{: .attention}

>La conversion de chaînes de caractères en entier ou en réels est très courante lorsque l'on récupère des entrées tapées par un utilisateur qui sont toujours *a priori* considérées comme des chaînes de caractères

### conversion booléennes

On effectue souvent ce genre d'opération de façon implicite pour les booléen. Ainsi, un entier est vrai s'il est non nul.

> Vérifiez le.
{: .a-faire}
{% details solution %}

```python
>>> bool(42)
True
```

{% enddetails %}

> Quand-est qu'une chaîne de caractère est fausse ?
{: .a-faire}
{% details solution %}

Une chaîne de caractère est fausse si elle est vide et vraie sinon.

```python
>>> bool("")
False
>>> bool("False")
True
```

{% enddetails %}
