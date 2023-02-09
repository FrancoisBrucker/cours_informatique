---
layout: layout/post.njk 
title: Variables

eleventyNavigation:
  key: "Variables"
  parent: "Coder en Python"
---

{% info %}
Utilisez la console de <https://console.basthon.fr/> pour exécuter les divers exemples et exercices
{% endinfo %}

<!-- début résumé -->

Les variables permettent à l'interpréteur de se rappeler d'objets qu'il a crée lors d'exécutions précédentes. Sans elles, on ne pourrait exécuter que des lignes indépendantes les unes entre elles : bref, on ne pourrait rien faire d'intéressant.

<!-- end résumé -->

{% note %}
Une variable est un ***nom*** auquel est associé un objet.

Pour associer un nom à un objet on utilise l’opérateur d’affectation `=`{.language-} tel que:

```txt
nom = objet
```

{% endnote %}

A gauche de l’opérateur `=`{.language-} se trouve un **nom** (en gros, quelque chose ne pouvant commencer par un nombre) et à droite un **objet**. Dans toute la suite du programme, dès que l'interpréteur python rencontrera le nom, il le remplacera par l'objet.

{% attention %}
Un nom n'est **PAS** une chaîne de caractères. Une chaîne de caractère est un objet alors qu’un nom n’est qu’un alias vers un objet.
{% endattention %}

Il est important de comprendre que l’opérateur d’affectation `=`{.language-} n’est pas symétrique. À gauche, des noms et à droite, des objets.

## <span id="espace-nom"></span> Espace de nom

Un **espace de noms** est un endroit où python stocke les noms. Une variable est un nom d'un espace de noms. Les espaces de noms sont hiérarchisées et tout en haut se trouve l'espace de nom **global** qui est créé lorsque l'interpréteur est lancé.

{% info %}
Si vous voulez en savoir plus sur les espaces de noms, vous pouvez consulter le cours sur [la mémoire et espace de noms]({{ "/cours/algorithme-code-théorie/code/mémoire-espace-noms" | url }})
{% endinfo %}

## Affectation des objets à l'espace de noms

Attardons nous un moment sur ces notions car elles seront cruciales plus tard pour appréhender les possibilités offertes par les objets.

Considérons le programme suivant :

```python
x = 1
y = 1
x = y
```

![association nom variable](python-nom-et-objets.png)

La figure montre le résultat après chaque instruction. On voit qu’un même objet peut parfaitement
avoir plusieurs noms. Cependant, à un nom correspond un unique objet. Les objets qui n’ont plus de
noms sont supprimés à intervalles réguliers (c’est ce qu’on appelle le [garbage collector](https://towardsdatascience.com/memory-management-and-garbage-collection-in-python-c1cb51d1612c)) puisque l’on ne peut plus y accéder.

Le mécanisme décrit précédemment (remplacement des noms par les objets référencés avant exécution
de l’instruction) montre que l’on peut affecter plusieurs noms en même temps, comme le montre l’exemple suivant qui échange les objets des noms `i`{.language-} et `j`{.language-} :

```python
i = 2
j = 3
i, j = j, i
```

Enfin, il est possible d'affecter plusieurs noms à un même objet. Par exemple l'exemple suivant affecte le même entier 1 aux noms `x`{.language-} et `y`{.language-} :

```python
x = y = 1
```

## Supprimer un nom

On peut supprimer un nom en utilisant le mot clé `del`{.language-}.

Dans une console :

```python
>>> x = 2
>>> print(x)
2
>>> del x
>>> print(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
```

## Exercices

Faites les différents exercice ci-après dans une console (certains exercices sont liés) :

{% exercice %}
Affectez la valeur 3 à la variable `a`{.language-}, puis affichez à l'écran la valeur associée à la variable `a`{.language-}.
{% endexercice %}
{% details "solution" %}

```python
>>> a=3
>>> print(a)
3
```

{% enddetails %}
{% exercice %}
Affectez la *nouvelle* valeur 6 à la variable `a`{.language-}, puis affichez à l'écran la valeur associée à la variable `a`{.language-}.
{% endexercice %}
{% details "solution" %}

```python
>>> a=6
>>> print(a)
6
```

{% enddetails %}
{% exercice %}
Affectez la valeur 2 à la variable `A`{.language-}, puis affichez à l'écran la valeur associée aux variables `a`{.language-} et `A`{.language-}.
{% endexercice %}
{% details "solution" %}

```python
>>> A = 2
>>> print(a)
6
>>> print(A)
2
```

Les variables sont [sensibles à la casse](https://fr.wikipedia.org/wiki/Sensibilit%C3%A9_%C3%A0_la_casse) : a est différent de A.

{% enddetails %}

{% exercice %}
Affectez la valeur 4 à la variable `b`{.language-}, puis affectez le résultat de la somme des variables `a`{.language-} et `b`{.language-} à variable `c`{.language-}

{% endexercice %}
{% details "solution" %}

```python
>>> b = 4
>>> c = (a+b)/2
>>> print(b)
4
>>> print(c)
5.0
```

`c`{.language} est un réel.

{% enddetails %}

{% exercice %}
Affectez en une ligne les valeurs 3 et 12 respectivement aux variables `j`{.language-} et `k`{.language-}

{% endexercice %}
{% details "solution" %}

```python
>>> i, j = 3, 12
```

{% enddetails %}

{% exercice %}
Affectez en une ligne la valeur 3 aux variables `x`{.language-}, `y`{.language-} et `z`{.language-}.

{% endexercice %}
{% details "solution" %}

```python
>>> x = y = z = 3
```

{% enddetails %}
