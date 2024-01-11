---
layout: layout/post.njk 
title: Fonctions et méthodes

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les fonctions et les méthodes sont des moyens d'effectuer des opérations sur les objets ou de créer de nouveaux objets. La puissance d'un langage de programmation vient aussi du fait ds nombreuses fonctions et méthodes mises à la dispositions de ses utilisateurs.

{% info %}
Utilisez la console de <https://console.basthon.fr/> pour exécuter les divers exemples et exercices
{% endinfo %}

## Fonctions

Une fonction est un type d'objet pouvant être exécuté. Par exemple la fonction `print`{.language-}.

C'est un objet :

```python
>>> type(print)
<class 'builtin_function_or_method'>
```

On *exécute* l'objet en faisant suivre son nom de parenthèses :

```python
>>> print()

```

L'exécution de la fonction `print`{.language-} à produit un retour à la ligne.

{% note %}
De nombreuses fonctions peuvent être exécutées avec des *paramètres* qui sont placées les un à la suite des autres entre les parenthèses et séparés par des virgules :

```python
nom_de_la_fonction(paramètre1, paramètre2, ..., paramètre_n)
```

{% endnote %}

Prenons par exemple la fonction print de python :

```python
>>> print("coucou", "les gens", "!")
coucou les gens !
```

L'exécution de la fonction `print`{.language-} avec les trois paramètres `"coucou"`{.language-}, `"les gens"`{.language-} et `"!"`{.language-} affichera à l'écran les 3 paramètres espacé d'un caractère (séparé par un caractère espace " ") puis ira à la ligne.

Toutes les fonctions de python sont documentées. On peut y accéder :

* via le site de python. L'aide de la fonction `print`{.language-} est là : <https://docs.python.org/fr/3/library/functions.html#print>
* en console en utilisant la fonction `help`{.language-} : `help(print)`{.language-} donne l'aide de `print`{.language-}

{% exercice %}
Affichez l'aide de la fonction print dans la console.
{% endexercice %}
{% details "solution" %}

```python
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

```

{% info %}
Si votre fenêtre est trop petite, l'affichage peut être différent.
{% endinfo %}

{% enddetails %}

### Paramètres d'une fonction

En regardant l'aide de la fonction `print`{.language-}, on remarque que les premiers paramètres sont sans noms (value, ...) puis les paramètres ont des noms (`sep`{.language-}, `end`{.language-}, `file`{.language-}, `flush`{.language-}) suivi d'une valeur. Ce sont des paramètres qui ont une valeur par défaut (par défaut `sep` vaut `" "`{.language-}).

{% note %}
Les paramètres sans valeurs par défaut sont **obligatoires** lorsque l'on appelle une fonction, les paramètres ayant une valeur par défaut sont **optionnels**.
{% endnote %}

On cependant bien sur utiliser, en le nommant, un paramètre ayant une valeur par défaut :

```python
>>> print("coucou", "les gens", "!", sep="***")
coucou***les gens***!
```

#### Ordre des paramètres

{% note %}
Les paramètres d'une fonctions doivent être mis dans cet ordre :

1. **tous** les paramètres sans valeurs par défaut dans l'ordre de la définition
2. **puis** les paramètres optionnels utilisés sans nom, dans l'ordre de leurs définitions
3. **puis** les paramètres optionnels utilisés avec leur nom (`nom=valeur`{.language-}) que l'on peut les mettre dans n'importe quel ordre.
{% endnote %}

{% info %}
La fonction print n'a pas de nombre déterminé de paramètres sans valeurs par défaut (il y a un `...`), la règle 2 ne s'applique donc pas pour print.
{% endinfo %}

Expérimentons ça sur un exercice.

{% exercice %}
La classe `int`{.language-} a pour définition `int(x, base=10)`{.language-} si `x`{.language-} est une chaîne de caractère.

Peut-on écrire :

1. `int("12")`{.language-} ?
2. `int(base=2)`{.language-} ?
3. `int("12", base=8)`{.language-} ?
4. `int("12", 8)`{.language-} ?
5. `int(base=8, "12")`{.language-} ?

{% endexercice %}
{% details "solution" %}

1. oui
2. non, la règle 1 n'est pas satisfaite
3. oui
4. oui
5. non, la règle 2 (et 1) n'est pas satisfaite

{% enddetails %}

#### Paramètres entre crochets dans une définition

On pourra parfois voir des paramètres entre crochet dans la définition de fonction. Par exemple : `complex([real[, imag]])`{.language-} ([documentation de la classe `complex`{.language-}](https://docs.python.org/fr/3/library/functions.html#complex)).

C'est **un raccourci d'écriture**, ce n'est pas une structure python. Cela signifie que l'on peut écrire la définition avec ou sans les crochets. Ceci permet d'écrire plusieurs définitions possible en une seule fois. Ainsi la définition `complex([real[, imag]])`{.language-} correspond à trois écritures possibles :

1. crochets extérieurs absents : `complex()`{.language-}

    ```python
    >>> complex()
    0j
    ```

    On vient de créer le complexe nul.
2. crochets extérieurs présents : `complex(real[, imag])`{.language-}. On a à nouveau deux choix :
   1. crochets absents :  `complex(real)`{.language-}

      ```python
      >>> complex(1)
      (1+0j)
      ```

   2. crochets présents : `complex(real, imag)`{.language-}

        ```python
        >>> complex(1, 2)
        (1+2j)
        ```

### Fonctions usuelles

{% lien "**Documentation**" %}
<https://docs.python.org/fr/3/library/functions.html>
{% endlien %}

Certaines sont plus utiles que d'autres. Nous allons en citer certaines, parmi les plus utilisées.

#### <span id="print"></span> Fonction `print`{.language-}

{% lien "**Documentation**" %}
<https://docs.python.org/fr/3/library/functions.html#print>
{% endlien %}

Affiche à l'écran ses paramètres.

#### Fonction `type`{.language-}

{% lien "**Documentation**" %}
<https://docs.python.org/fr/3/library/functions.html#type>
{% endlien %}

Donne le type d'un objet.

{% info %}
On l'a utilisée dans la partie [objets types et types d'objets](../principes/objets-types){.interne}.
{% endinfo %}

#### <span id="len"></span> Fonction `len`{.language-}

{% lien "**Documentation**" %}
<https://docs.python.org/fr/3/library/functions.html#len>
{% endlien %}

Rend le nombre d'éléments d'une chaîne de caractères (et plus généralement d'[un conteneur](../structurer-son-code/conteneurs){.interne} que l'on verra plus tard).

{% exercice %}
Quel est le nombre de caractères du mot "anticonstitutionnellement" ?
{% endexercice %}
{% details "solution" %}

```python
>>> len("anticonstitutionnellement")
25
```

{% enddetails %}

### Nom d'une classe comme fonction

`int`{.language-}, `float`{.language-},  `complex`{.language-}, `str`{.language-} et `bool`{.language-} permettent de créer des objets du nom du type.

On a déjà vu cette possibilité dans la partie [objets types et types d'objets](../principes/objets-types){.interne}, c'est très utile pour changer un objet de classe. Mais utilisons ce qu'on a vu maintenant pour aller plus loin :

{% exercice %}
En utilisant [`int()`{.language-}](https://docs.python.org/fr/3/library/functions.html#int) qui crée des entiers, trouvez la représentation décimale du nombre binaire : 1001100011
{% endexercice %}
{% details "solution" %}

On utilise le paramètre base de la classe `int`{.language-} :

```python
>>> int("1001100011", base=2)
611
```

{% enddetails %}

Allez, un dernier pour la route :

{% exercice %}
En utilisant le fait que la fonction `len(chaîne_de_caractères)`{.language-} donne le nombre de caractères de la chaîne (par exemple `len("abc")`{.language-} rend `3`{.language-}), et que l'exposant eb python s'écrit `**`{.language-} (par exemple `2**8`{.language-} rend `256`{.language-}) donnez le nombre de chiffre du 27ème [nombre de Mersenne premier](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier).
{% endexercice %}
{% details "solution" %}

```python
>>> len(str(2 ** 44497 - 1))
13395
```

{% enddetails %}

#### <span id="input"></span> Fonction `input`{.language-}

{% lien "**Documentation**" %}
<https://docs.python.org/fr/3/library/functions.html#input>
{% endlien %}

Permet de demander une chaîne de caractère à un utilisateur. Par exemple :

```python
>>> x = input()
23
>>> x
'23'
```

On demande à l'utilisateur de taper quelque chose puis d'appuyer sur la touche entrée. Ce qu'à taper l'utilisateur est rendu sous la forme d'une **chaîne de caractère**.

{% attention %}
Tout ce qui vient de l'utilisateur est une **chaîne de caractère**. Si l'on veut que ce soit un nombre par exemple, il faut le convertir. Comme par exemple : `i = int(input())`{.language-} qui converti en entier le résultat de la fonction `input`{.language-}.
{% endattention %}

## <span id="méthodes"></span> Méthodes

Les méthodes sont un autre moyen d'agir sur un objet. On les utilise de cette façon :

```python
objet.méthode(paramètre 1, paramètre 2, ..., paramètre n)
```

On applique `méthode`{.language-} à `objet`{.language-} en utilisant les paramètres de la méthode.

{% note "Utilisation des méthodes d'une classe" %}
Supposons que l'on ait un objet de nom `objet`{.language-} et une méthode nommée `méthode`{.language-} associée au type de l'objet de nom  `objet`{.language-}.

L'instruction `objet.méthode()`{.language-} exécutera la méthode `méthode`{.language-} pour l'objet `objet`{.language-}. Si la méthode nécessite des paramètres, ils seront placés à l'intérieur de la parenthèse, séparés par des virgules. Par exemple `objet.méthode(paramètre_1, paramètre_2)`{.language-}.
{% endnote %}

{% attention %}
Une méthode ne s'utilise **jamais** seule. Elle s'applique à ce qu'il y a à gauche d'elle.
{% endattention %}

Prenez le temps de regarder les différentes méthodes des classes de base de python. Souvent elle vous permettent de faire rapidement une opération compliquée. C'est en particulier vrai pour les chaînes de caractères et les listes.

### Méthodes des chaînes de caractères

Chaque classe vient avec des méthodes. Si les nombre et booléens ont peu de méthodes, les chaines de caractères par exemple en ont [tout un tas](https://docs.python.org/fr/3/library/stdtypes.html#string-methods).

Essayons de les apprendre avec ces petits exercices :

{% exercice %}
Transformez le 27ème [nombre de Mersenne](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier) en une chaîne de caractère
{% endexercice %}
{% details "solution" %}

```python
>>> x = str(2 ** 44497 - 1)
```

{% enddetails %}

{% exercice %}
En utilisant la méthode [`count`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.count), comptez le nombre de 0 du 27ème [nombre de Mersenne premier](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier).
{% endexercice %}
{% details "solution" %}

Dans un interpréteur :

```python
>>> x.count("0")
1332
```

{% enddetails %}

{% exercice %}
En utilisant la méthode [`replace`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.replace), changez les 2 en 7 dans le 27ème [nombre de Mersenne premier](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier).
{% endexercice %}
{% details "solution" %}

Dans un interpréteur :

```python
>>> y = int(x.replace("2", "7"))
```

{% enddetails %}

{% exercice %}
Avec le mot "choucroute garnie" et les méthodes [`count`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.count), [`index`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.index) et [`rindex`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#str.rindex) :

* combien y a-t-il de "ou" ?
* quel est l'indice du premier "e" ?
* quel est l'indice du dernier "e" ?

{% endexercice %}
{% details "solution" %}

```python
>>> mot.count("ou")
2
>>> mot.index("e")
9
>>> mot.rindex("e")
16
```

{% enddetails %}

On peut chaîner les méthodes, la sortie d'une méthode devenant l'entrée de la prochaine. Par exemple, avec 2 méthodes :

```python
objet.méthode_1().méthode_2()
```

Signifie que méthode2() est appliquée à l'objet résultat de `objet.méthode_1()`{.language-}

Et avec $n$ méthodes :

```python
objet.méthode_1().méthode_2(). ... .méthode_n()
```

Signifie que `méthode_n()`{.language-} est appliquée au résultat de `objet.méthode_1(). ... .méthode_n-1()`{.language-}

{% exercice %}
Que fait :

```python
str(2 ** 44497 - 1).replace("2","x").replace("7","2").replace("x","7")
```

{% endexercice %}
{% details "solution" %}

Il est aisé de comprendre ce que ça fait en procédant de droite à gauche :

1. `replace("x","7")`{.language-} est appliqué à ce qui est à sa gauche donc `str(2 ** 44497 - 1).replace("2","x").replace("7","2")`{.language-}
2. `replace("7","2")`{.language-} est appliqué à ce qui est à sa gauche donc `str(2 ** 44497 - 1).replace("2","x")`{.language-}
3. `replace("2","x")`{.language-} est appliqué à ce qui est à sa gauche donc `str(2 ** 44497 - 1)`{.language-}

En remontant les opérations précédentes :

1. le résultat de `str(2 ** 44497 - 1)`{.language-}  sera une chaîne de caractère représentant le 27ème nombre premier de Mersenne
2. `str(2 ** 44497 - 1).replace("2","x")`{.language-} on a remplacé les 2 par des "x" dans la chaîne précédente
3. `str(2 ** 44497 - 1).replace("2","x").replace("7","2")`{.language-} on a remplacé les 7 par des 2 de la chaîne précédente
4. `str(2 ** 44497 - 1).replace("2","x").replace("7","2").replace("x","7")`{.language-} on a remplacé les "x" par des 2 dans la chaîne précédente

On a donc au final échangé les 2 et les 7 du 27ème nombre premier de Mersenne

{% enddetails %}

## Fonctions vs. méthodes

Ne confondez pas fonctions et méthodes. Une fonction s'exécute toute seule alors qu'une méthode a besoin d'un objet sur lequel elle s'applique (celui avant le `.`{.language-}). Vous pouvez voir ça comme un 1er paramètre indispensable à l'exécution d'une méthode. Considérez le programme suivant :

```python
>>> ma_chaîne = "coucou !"
>>> en_majuscules = ma_chaîne.upper()
>>> print(en_majuscules)
COUCOU !
```

La première ligne crée une chaîne de caractères. La seconde instruction est une *méthode* (`upper`{.language-}) qui s'applique à l'objet de nom `ma_chaîne`{.language-} et qui n'a pas de paramètre.

{% info %}
On peut voir les méthodes comme des fonctions définies dans l'espace de nom de l'objet.
{% endinfo %}

## Attributs d'une classe

C'est plus rare, mais certaines classes possèdent  des également des *attributs* en plus des méthodes. Ce sont des valeurs associées à l'objet.

Par exemple les objets de la classe `complex`{.language-} qui possède les attributs `real`{.language-} et `imag`{.language-} pour rendre la partie réelle et imaginaire d'un complexe.

```python
>>> (1+2j).real
1.0
>>> (1+2j).imag
2.0
```
