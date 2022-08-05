---
layout: page
title:  "corrigé Test 1 : code"
category: cours
tags: informatique cours 
---

## barème

* syracuse + test : 2pt
* suite + test : 2pt
* main.py : 1pt

## erreurs fréquemment rencontrées

### tests indépendants

Une fonction de test doit être indépendante du reste du code.
De là :

```python
x = 1

def test_syracuse():
    assert syracuse(x) == 1
```

N'est pas correcte. On préférera être explicite :

```python
def test_syracuse():
    assert syracuse(1) == 1
```

### noms des tests

Un test à sa son utilité. Son nom doit dire à quoi il sert. Ainsi `test_1` n'est **PAS** un bon nom de test. On pourra avoir la convention de nommage suivante : `test_nom_quoi` où `nom` est le nom de la fonction que l'on teste et `quoi`ce que l'on teste.

exemple :

```python
from syracuse import syracuse

def test_syracuse_pair():
    assert syracuse(2) == 1
```

### vos tests/main doivent se lancer

Un programme doit **TOUJOURS** marcher. Lorsque l'on exécute un _"main.py"_ où que l'on lance les tests avec la commande `pytest` ils doivent se lancer. Cela ne veut pas dire que les tests soient tous vert, vous pouvez avoir un tests rouge ce qui signifie que vous êtes entrain de travailler sur cette fonctionnalité et qu'elle ne fonctionne pas encore, mais ils doivent se lancer.

Ainsi :

* vérifiez que vos imports soient corrects
* vérifiez que si vous exécutez votre programme principal il se lance
* vérifiez que vous pouvez exécutez vos tests et que vos tests se lancent (qu'ils soient vert ou rouge)

Si on ne peut pas exécuter votre fichier main ou que vos tests ne se lancent pas parce que vous vous êtres trompé dans un import ou que vous avez des erreurs de syntaxe, votre note chute drastiquement.

Dernière remarque : vos tests doivent tester des choses... Mettre des fonctions de tests sans qu'ils soient utile (genre `assert 1 == 1`) est également rédhibitoire.

### entrée utilisateurs et conversion de types

Après un input vous aurez **toujours** une chaîne de caractère. Il faut la convertir dans ce que va demander vos fonctions, ici des entiers.

Ne faites **PAS** de conversion de type dans vos fonctions. Si elles demandent des entrées entiers supposez que c'est le cas (par de `int(x) % 2` par exemple dans la fonction `syracuse`). Tôt ou tard ce genre chose va vous sauter à la figure car un jour vous votre programme va planter sans que vous compreniez pourquoi ni où est le soucis.

## _"syracuse.py"_

```python
def syracuse(x):
    if x % 2 == 0:
        return x / 2
    else:
        return 3 * x + 1


def suite(u_0):
    sortie = [u_0]
    
    u_n = u_0
    while u_n != 1:
        u_n = syracuse(u_n)
        sortie.append(u_n)
    
    return sortie

```

## _"test_syracuse.py"_

```python
from syracuse import syracuse, suite

def test_syracuse_pair():
    assert syracuse(2) == 1


def test_syracuse_impair():
    assert syracuse(1) == 4


def test_suite_u_0_1():
    assert suite(1) == [1]


def test_suite_u_0_5():
    assert suite(5) == [5, 16, 8, 4, 2, 1]

```

## _"main.py"_

```python
from syracuse import suite

sortie_utilisateur = input("Donnez un entier : ")

u_0 = int(sortie_utilisateur)

print("suite de syracuse associée : ", suite(u_0))

```
