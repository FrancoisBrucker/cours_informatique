---
layout: layout/post.njk

title: Exécution Conditionnelle et répétition de blocs

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Deux types de boucles existent en python : les boucles _tant que_ (`while`{.language-}) et les boucles _pour chaque_ (`for`{.language-})

## Bloc while : boucle tant que

{% lien "**Documentation**" %}
<https://docs.python.org/fr/3/reference/compound_stmts.html#the-while-statement>
{% endlien %}

```python
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

while x > 1:
    x -= 1
    factorielle = factorielle * x

print(factorielle)
```

{% enddetails %}

## Bloc for : boucle pour chaque

{% lien "**Documentation**" %}
<https://docs.python.org/fr/3/reference/compound_stmts.html#the-for-statement>
{% endlien %}

```python
for <nom> in <itérable>:
    instruction 1
    instruction 2
    ...
    instruction n
```

Le bloc sera exécuté pour chaque élément de l'_itérable_. A chaque exécution, l'élément courant de l'itérateur sera nommé `<nom>`{.language-} Beaucoup d'objet peuvent être considérés comme itérable (nous en verrons plusieurs par la suite) et nous en connaissons déjà un : les chaînes de caractères.

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

## <span id="range"></span> Fonction range

Les boucles for sont souvent associée à la [fonction `range`{.language-}](https://docs.python.org/fr/3/library/stdtypes.html#range). Cette fonction crée un itérateur (quelque chose qui produit des nombres).

Par exemple :

```python
for x in range(10):
    print(x)
```

Affichera les 10 premiers entiers (de 0 à 9). Le résultat de `range(10)`{.language-} est un objet de type range, qui est fait pour être utilisé avec l'instruction for.

On peut utiliser la fonction `range`{.language-} de trois façons différentes qu'elle soit appelée avec un, deux ou trois paramètres :

- de `0`{.language-} à juste avant `paramètre`{.language-}. Par exemple `range(10)`{.language-} rendra un itérateur de la suite des 10 entiers allant de 0 à 9.
- de `premier paramètre`{.language-} à juste avant `deuxième paramètre`{.language-}. Par exemple `range(4, 10)`{.language-} rendra un itérateur de la suite des 6 entiers allant de 4 à 9.
- `premier paramètre`{.language-} à juste avant `deuxième paramètre`{.language-}, avec un saut de `troisième paramètre`{.language-}. Par exemple `range(10, -1, -1)`{.language-} rendra un itérateur de la suite 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0.

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
