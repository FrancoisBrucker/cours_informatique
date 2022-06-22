---
layout: page
title:  "Bases de python : Objets types et types d'objets"
authors: 
    - Augustin Agbo-Kpati
    - François Brucker
    - Pascal Préa
---


Dans les exemples qui suivent, nous allons ici utiliser des fonctions ou des classes sans véritablement les définir. 

Une fonction ou une classe s'utilise en mettant son nom suivi de parenthèses contenant zéro, un ou plusieurs paramètres (des objets) séparés par des virgules. 
Par exemple la commande : 

```python
print("coucou", "les gens", "!")
``` 

Qui consiste à exécuter la fonction `print` avec les trois paramètres `"coucou"`, `"les gens"` et `"!"` affichera à l'écran les 3 paramètres séparé par un espace. 


#### pour aller plus loin

> En utilisant [la classe int()](https://docs.python.org/fr/3.9/library/functions.html#int) qui crée des entiers, trouvez la représentation décimale du nombre binaire : 1001100011
{: .a-faire}
{% details solution %}

On utilise le paramètre base de la classe `int` :

```python
>>> int("1001100011", base=2)
611
```
{% enddetails %}

## Action sur les objets

Agir sur des objets en python prend deux formes (en apparence) différentes :

* les opérateurs
* les méthodes

### opérateurs

#### sur les entiers et réels

Outre les classiques opérations `+` (addition), `-` (soustraction), `/` (division) et `*` (multiplication), python possède aussi `//` division entière,  `%` reste de la division entière et `**` exposant.

> que vaut le quotient et le reste de la division entière de 4538 par 23 ?
{: .a-faire}
{% details solution %}
Dans un terminal :

```text
>>> 4538 // 23
197
>>> 4538 % 23
7
>>> (4538 // 23) * 23 + 7
4538
```

{% enddetails %}
{: .a-faire}

#### sur les chaînes de caractères


```python
>>> "x" + "y"
'xy'
>>> 3 * "x"
'xxx'
```

> Recopiez 10 fois : `"j'aime bien faire du python"`
{: .a-faire}
{% details solution %}
Si l'on sait que le caractère `\n` correspond à aller à la ligne, on peut écrire :

```python
>>> print(10 * "j'aime bien faire du python\n")
j'aime bien faire du python
j'aime bien faire du python
j'aime bien faire du python
j'aime bien faire du python
j'aime bien faire du python
j'aime bien faire du python
j'aime bien faire du python
j'aime bien faire du python
j'aime bien faire du python
j'aime bien faire du python

```

{% enddetails %}
{: .a-faire}

#### sur les booléens


#### pour aller plus loin

> En utilisant le fait que la fonction `len(chaine de caractère)` donne le nombre de caractères de la chaîne (par exemple `len("abc")` rend `3`), et que l'exposant eb python s'écrit `**` (par exemple `2**8` rend `256`) donnez le nombre de chiffre du 27ème [nombre de Mersenne premier](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier).
{: .a-faire}
{% details solution %}

```python
>>> len(str(2 ** 44497 - 1))
13395
```

{% enddetails %}

### méthodes d'une classes

Les méthodes sont moyens d'agir sur un objet. On les utilise de cette façon :

```pyhton
objet.methode(paramètre 1, paramètre 2, ..., paramètre n)
```

On applique `méthode` à `objet` en utilisant les `paramètres` de la méthode.

> Une méthode ne s'utilise **jamais** seule. Elle s'applique à ce qu'il y a à gauche d'elle.

Chaque classe vient avec des méthodes. Si les nombre et booléens ont peux de méthode, les [chaines de caractères en ont tout un tas](https://docs.python.org/3/library/stdtypes.html#string-methods).

> Combien y a-t-il de 0 dans le 27ème [nombre de Mersenne premier](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier).
{: .a-faire}
{% details solution %}

Dans un interpréteur :

```python
>>> str(2 ** 44497 - 1).count("")
1332
```

{% enddetails %}
{: .a-faire}

On peut chainer les méthodes, la sortie d'une méthode devenant l'entrée de la prochaine. Par exemple, avec 2 méthodes :

```python
objet.methode_1().methode_2()
```

Signifie que méthode2() est appliquée à l'objet résultat de `objet.methode1()`

Et avec n méthodes :

```python
objet.methode1().methode2(). ... .methode_n()
```

Signifie que `methode_n()` est appliquée au résultat de `objet.methode_1(). ... .methode_n-1()`

> Que fait :
>
> ```python
> str(2 ** 44497 - 1).replace("2","x").replace("7","2").replace("x","7")
> ```
>
{: .a-faire}
{% details solution %}
Il est aisé de comprendre ce que ça fait en procédant de droite à gauche :

1. `replace("x","7")` est appliqué à ce qui est à sa gauche donc `str(2 ** 44497 - 1).replace("2","x").replace("7","2")`
2. `replace("7","2")` est appliqué à ce qui est à sa gauche donc `str(2 ** 44497 - 1).replace("2","x")`
3. `replace("2","x")` est appliqué à ce qui est à sa gauche donc `str(2 ** 44497 - 1)`

En remontant les opérations précédentes :

1. le résultat de `str(2 ** 44497 - 1)`  sera une chaine de caractère représentant le 27ème nombre premier de Mersenne
2. `str(2 ** 44497 - 1).replace("2","x")` on a remplacé les 2 par des "x" dans la chaine précédente
3. `str(2 ** 44497 - 1).replace("2","x").replace("7","2")` on a remplacé les 7 par des 2 de la chaine précédente
4. `str(2 ** 44497 - 1).replace("2","x").replace("7","2").replace("x","7")` on a remplacé les "x" par des 2 dans la chaine précédente

On a donc au final échangé les 2 et les 7 du 27ème nombre premier de Mersenne

{% enddetails %}
{: .a-faire}

### attributs d'une classe

C'est plus rare, mais certaines classes possèdent  des également des *attributs* en plus des méthodes. Ce sont des valeurs associées à l'objet.

Par exemple les objets de la classe complex qui possède les attibuts `real` et `imag` pour rendre la partie réelle et imaginaire d'un complexe.

```pyhton
>>> (1+2j).real
1.0
>>> (1+2j).imag
2.0
```
