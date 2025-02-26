---
layout: layout/post.njk

title:  "sujet Test 2 : code"
---


## Barème

Une note sur 9 répartie comme suit :

- 3pt pour la question 1.1
- 3pt pour la question 1.2
- 2pt pour la question 2.1
- 1pt pour la question 2.2

La note sur $20$ finale est obtenue en multipliant la note sur 9 par $2.25$.

{% note "**Objectif du test**" %}

En 15 minutes :

- **un élève *normal*** doit parvenir à faire la première question correctement (ce qui garantit le 10/20), c'est à dire :
  - coder la fonction et son test
  - avoir un main fonctionnel rendant à peu prêt ce qui est demandé.
- **un bon élève** doit parvenir à réussir à faire la première question parfaitement et commencer la seconde
- **un très bon élève** à fini la question 2.1

{% endnote %}

La ventilation des notes est :

La ventilation des notes est :

|note/20  |≤8  | ]8, 10[ | [10, 12]      | ]12, 14]    | ]14, 16]  | [16, 20]    | > 20
|---------|----|------------|------------|-------------|-----------|-------------|------
|nombre   | 9  |  6         |  8         |  11         |  3        | 5           |  2
|rang min | 44 | 34         | 28         | 21          | 10        | 7           |  1

- moyenne : 11.29/20
- écart-type : 4.3/20
- médiane : 11.48/20

## Erreurs fréquemment rencontrées

### Avoir un code fonctionnel

1. Votre code **doit** fonctionner. Au pire vous commentez le code non fonctionnel et expliquez, également en commentaire, le problème.
2. un test ne doit pas faire semblant de tester... Si la fonction à tester ne marche pas, il **faut** que le test rate.
3. Les tests font partie du code : il **doit** fonctionner. Il peut échouer ou réussir, mais il doit s'executer.

En code il faut avancer petit à petit et tout doit toujours fonctionner. Plein de code qui ne fonctionne qu'à moitié vaudra toujours moins que moins de code mais fonctionnel.

**Le correcteur** ne va pas faire l'effort de corriger votre code pour qu'il fonctionne, ni le lire attentivement comme on le ferait avec un algorithme. Mais plus important encore, **vous** serez plus confiant en bâtissant sur quelque chose qui fonctionne.

Coder sans exécuter son code c'est coder les yeux bandés : cela ne peut pas fonctionner.

### Erreur de longueur

Dans la question 1.1 alterner les 2 caractères a posé des problèmes, l'erreur la plus courante  été de ne rendre que des chaines de longueur paires.

### Erreur d'affichage

L'affichage de la question 1.2  a posé de nombreux problèmes. L'erreur la plus courante, outre le fait de tout afficher sur une ligne, a éte de ne pas alterner les 0 et les 1 en début de chaîne.

## Corrigé

### Question 1

#### Code

```python
def alternante(n, a, b):
    s = ""

    for i in range(n):
        if i % 2 == 0:
            s += a
        else:
            s += b

    return s
```

#### Test

```python
from fonctions import alternante


def test_alternante():
    assert alternante(4, "0", "1") == "0101"
    assert alternante(7, "1", "z") == "1z1z1z1"
```

#### Programme principal

```python
from fonctions import alternante, croissante_alternante

n_init = int(input("Un entier (puis entrée) :"))

chaîne = alternante(n_init, "0", "1")
n = 0
while n < n_init:
    print(chaîne[n:n+5])
    n += 5
```

#### Code alternatif

```python
def alternante_bis(n, a, b):
    s = ""

    for i in range(n):
        s += a
        a, b = b, a

    return s
```

#### Programme principal alternatif

En refaisant à chaque fois une chaîne :

```python
from fonctions import alternante

n_init = int(input("Un entier (puis entrée) :"))

début = '0'
fin = '1'
n = n_init
while n > 5:
    print(alternante(5, début, fin))

    n -= 5
    début, fin = fin, début

if n > 0:
    print(alternante(n, début, fin))

```

### Question 2

#### Code

```python
def croissante_alternante(n, c):
    s = ""

    for i in range(n):
        s += str(c)

        c = c + 1
        if c > 9:
            c = 1

    return s
```

#### Test

```python
from fonctions import croissante_alternante


def test_croissante_alternante():
    assert croissante_alternante(3, 5) == "567"
    assert croissante_alternante(13, 4) == "4567891234567"
    assert croissante_alternante(19, 1) == "1234567891234567891"
```

#### Programme principal

```python
from fonctions import alternante, croissante_alternante

n_init = int(input("Un entier (puis entrée) :"))

chaîne = alternante(n_init, "0", "1")
n = 0
while n < n_init:
    print(chaîne[n:n+5])
    n += 5

chaîne = croissante_alternante(n_init, 1)
n = 0
while n < n_init:
    print(chaîne[n:n+5])
    n += 5

```

#### Code alternatif

On n'utilise un modulo (comme on n'utilise pas l'itérateur de boucle, python permet de l'exprimer en le remplaçant par `_`{.language-}) :

```python
def croissante_alternante_bis(n, c):
    s = ""

    for _ in range(n):
        s += str(c)
        c = c % 9 + 1

    return s
```

Comme on utilise le modulo on peut modifier le code pour qu'il utilise l'itérateur de la boucle, ce qui est plus _joli_ :

```python
def croissante_alternante_bis_bis(n, c):
    s = ""
    for i in range(c-1, c+ n-1):
        s += str(i % 9 + 1)

    return s
```

Et qui permet, en utilisant des list comprehension et la méthode [`join`{.language-}](https://docs.python.org/fr/3.13/library/stdtypes.html#str.join) des chaînes de caractères, de simplifier drastiquement le code en l'[unilignant](https://fr.wikipedia.org/wiki/Uniligne) :

```python
def croissante_alternante_ultime(n, c):
    return "".join([str(i % 9 + 1) for i in range(c-1, c+ n-1)])
```

#### Programme principal alternatif

En refaisant à chaque fois une chaîne :

```python
from fonctions import alternante, croissante_alternante

n_init = int(input("Un entier (puis entrée) :"))

début = '0'
fin = '1'
n = n_init
while n > 5:
    print(alternante(5, début, fin))

    n -= 5
    début, fin = fin, début

if n > 0:
    print(alternante(n, début, fin))


n = n_init
c = 1
while n > 5:
    s = croissante_alternante(5, c)
    print(s)

    c = int(s[-1]) + 1
    if c > 9:
        c = 1

    n -= 5

if n > 0:
    s = croissante_alternante(n, c)
    print(s)
```
