---
layout: layout/post.njk 

title: Blocs

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% info %}
Utilisez un notebook ou spyder pour exécuter les divers exemples et exercices
{% endinfo %}

<!-- début résumé -->

Les blocs python qui permettent de grouper un ensemble de lignes de codes ensemble. On verra les blocs `while`{.language-}, `for`{.language-} et les blocs `if/elif/else`{.language-}.

<!-- end résumé -->

Si python ne pouvait qu'exécuter ligne à ligne un code on ne pourrait pas faire grand chose. Le principe des programmes est de pouvoir grouper les instructions en bloc.

## Définition d'un bloc

En python, un bloc est toujours défini de la même manière  :

* Ce qui va identifier le bloc pour son exécution (une condition, son nombre d'exécution, son nom) et se finit par un `:`{.language-}
* Les instructions le constituant.

Pour séparer les blocs les un des autres, et savoir ce qui le définit, le langage Python utilise l'indentation (4 espaces par défaut): un bloc est donc une suite d'instructions ayant la même indentation.

```text
type de bloc:
    instruction 1
    instruction 2
    ...
    instruction n
```

Ces différents blocs sont pratiques car ils vont nous permettre :

* répéter des blocs
* d'exécuter des blocs conditionnellement

Les blocs peuvent bien sur se combiner :

```text
bloc A:
    instruction 1 du bloc A
    bloc B:
        instruction 1 du bloc B
        ...
        instruction m du bloc B
    instruction 2 du bloc A
    ...
    instruction n du bloc A
```

L'indentation permet **toujours** de s'y retrouver.

## Répétition de blocs

Deux types de boucles existent en python : les boucles *tant que* (`while`{.language-}) et les boucles *pour chaque* (`for`{.language-})

### Bloc while : boucle tant que

{% lien "**Documentation**" %}
<https://docs.python.org/3/reference/compound_stmts.html#the-while-statement>
{% endlien %}

```text
while <condition logique>:
    instruction 1
    instruction 2
    ...
    instruction n
```

Par exemple le bloc `while`{.language-} suivant :

```python
b = 6
while b > 0:
    print(b)
    b = b - 1
```

qui va afficher :

```text
6
5
4
3
2
1
```

{% exercice %}
Calculez la factorielle de 45.
{% endexercice %}
{% details "solution" %}

```python
factorielle = x = 45

while x >= 1:
    factorielle = factorielle * x
    x -= 1

print(factorielle)
```

{% enddetails %}

### Bloc for : boucle pour chaque

{% lien "**Documentation**" %}
<https://docs.python.org/3/reference/compound_stmts.html#the-for-statement>
{% endlien %}

```python
for <nom> in <itérable>:
    instruction 1
    instruction 2
    ...
    instruction n
```

Le bloc sera exécuté pour chaque élément de l'*itérable*. A chaque exécution, l'élément courant de l'itérateur sera nommé `<nom>`{.language-} Beaucoup d'objet peuvent être considérés comme itérable (nous en verrons plusieurs par la suite) et nous en connaissons déjà un : les chaînes de caractères.

L'exécution du code suivant :

```python
for c in "bonjour":
    print(c)
```

Donnera :

```python
b
o
n
j
o
u
r
```

La boucle for itère sur chaque caractère de la chaîne `"bonjour"`{.language-} et le place dans la variable nommée `c`{.language-}. La valeur de `c`{.language-} vaut donc successivement les caractères `"b"`{.language-}, `"o"`{.language-}, `"n"`{.language-}, `"j"`{.language-}, `"o"`{.language-}, `"u"`{.language-} et enfin `"r"`{.language-}.

{% note %}
Choisissez toujours des noms de variables explicatifs dans vos boucles for !

Il sera plus simple de s'y retrouver avec des noms de variables explicites qu'avec un tas de variables s'appelants `i`{.language-}, `j`{.language-}, `i2`{.language-}, `j2`{.language-}, etc.
{% endnote %}

{% exercice %}
Écrire un programme qui affiche la table de 9 :

```text
1 x 9 = 9   
2 x 9 = 18  
...   
```

{% endexercice %}
{% details "solution" %}

```python

for nombre in range(1, 11):
    print(nombre, "x 9 = ", nombre * 9)
```

{% enddetails %}

{% exercice %}
Écrire un programme qui calcule la somme des chiffres de 1 à 100.

{% endexercice %}
{% details "solution" %}

```python

somme = 0
for k in range(1, 101):
    somme += k
print(somme)
```

{% enddetails %}

### <span id="range"></span> Itérateur range

Les boucles for sont souvent associée à la fonction [`range`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#range). Cette fonction crée un itérateur (quelque chose qui produit des nombres).

Par exemple :

```python
for x in range(10):
    print(x)
```

Affichera les 10 premiers entiers (de 0 à 9). Le résultat de `range(10)`{.language-} est un objet de type range, qui est fait pour être utilisé avec l'instruction for.

On peut utiliser la fonction `range`{.language-} de trois façons différentes qu'elle soit appelée avec un, deux ou trois paramètres :

* de `0`{.language-} à juste avant `paramètre`{.language-}. Par exemple `range(10)`{.language-} rendra un itérateur de la suite des 10 entiers allant de 0 à 9.
* de `premier paramètre`{.language-} à juste avant `deuxième paramètre`{.language-}. Par exemple `range(4, 10)`{.language-} rendra un itérateur de la suite des 6 entiers allant de 4 à 9.
* `premier paramètre`{.language-} à juste avant `deuxième paramètre`{.language-}, avec un saut de `troisième paramètre`{.language-}. Par exemple `range(10, -1, -1)`{.language-} rendra un itérateur de la suite 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0.

{% exercice %}
Afficher à l'écran les 16 premiers entiers, allant de 0 à 15
{% endexercice %}
{% details 'solution' %}

```python
for i in range(16):
    print(i)

```

{% enddetails %}
{% exercice %}
Afficher à l'écran les 13 entiers, allant de 3 à 15
{% endexercice %}
{% details 'solution' %}

```python
for i in range(3, 16):
    print(i)

```

{% enddetails %}

{% exercice %}
Afficher à l'écran les multiples de 3 allant de de 3 à 15
{% endexercice %}
{% details 'solution' %}

```python
for multiple_trois in range(3, 16, 3):
    print(multiple_trois)

```

{% enddetails %}

Le troisième paramètre de la fonction range n'est pas obligatoirement positif. Ceci permet de compter à rebours :

{% exercice %}
Afficher à l'écran les entiers allant de 5 à 0, dans cet ordre.
{% endexercice %}
{% details 'solution' %}

```python
for x in range(5, -1, -1):
    print(x)

```

{% enddetails %}

## Blocs if : Exécution conditionnelle

{% lien "**Documentation**" %}
<https://docs.python.org/3/reference/compound_stmts.html#the-if-statement>
{% endlien %}

Permet d'exécuter un bloc si une condition logique est vraie :

```text
if <condition logique>:
    instruction 1
    instruction 2
    ...
    instruction n
elif <condition logique>:
    instruction 1
    instruction 2
    ...
    instruction n
else:
    instruction 1
    instruction 2
    ...
    instruction n
```

Notez qu'il peut y avoir autant de bloc `elif`{.language-} que l'on veut (même 0) et qu'il n'est pas nécessaire d'avoir de `else`{.language-}.

{% exercice %}
Demandez à l'utilisateur de rentrer un entier au clavier (en utilisant la fonction [input](../fonctions-méthodes#input)) et de répondre "C'est entre 2 et 8" si le nombre rentré est entre 2 et 8 et de répondre "ce n'est pas entre 2 et 8" sinon.
{% endexercice %}
{% details "solution" %}

```python

entier = int(input("Un entier entre 2 et 8 : "))
if 2 >= entier and entier <= 8:
    print("C'est entre 2 et 8")
else:
    print("ce n'est pas entre 2 et 8")
```

{% enddetails %}

## Exercice final

{% exercice %}
Utilisez ce que vous avez appris pour vérifier la [conjecture de Syracuse](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse) pour les 100 premiers entiers
Exemple :
{% endexercice %}
{% details "solution" %}

```python

for x in range(100):
    while x > 1:
        if x % 2  == 0:
            x /= 2
        else:
            x = 3 * x + 1
```

{% enddetails %}
