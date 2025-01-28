---
layout: layout/post.njk

title: "Erreurs courantes : Syracuse"
---

## Tests indépendants

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

## Noms des tests

Un test à sa son utilité. Son nom doit dire à quoi il sert. Ainsi `test_1`{.language-} n'est **PAS** un bon nom de test. On pourra avoir la convention de nommage suivante : `test_nom_quoi`{.language-} où `nom`{.language-} est le nom de la fonction que l'on teste et `quoi`ce que l'on teste.

exemple :

```python
from syracuse import syracuse

def test_syracuse_pair():
    assert syracuse(2) == 1
```

## Vos tests/main doivent se lancer

Un programme doit **TOUJOURS** marcher. Lorsque l'on exécute un _"main.py"_ où que l'on lance les tests avec la commande `pytest` ils doivent se lancer. Cela ne veut pas dire que les tests soient tous vert, vous pouvez avoir un tests rouge ce qui signifie que vous êtes entrain de travailler sur cette fonctionnalité et qu'elle ne fonctionne pas encore, mais ils doivent se lancer.

Ainsi :

- vérifiez que vos imports soient corrects
- vérifiez que si vous exécutez votre programme principal il se lance
- vérifiez que vous pouvez exécutez vos tests et que vos tests se lancent (qu'ils soient vert ou rouge)

Si on ne peut pas exécuter votre fichier main ou que vos tests ne se lancent pas parce que vous vous êtres trompé dans un import ou que vous avez des erreurs de syntaxe, votre note chute drastiquement.

Dernière remarque : vos tests doivent tester des choses... Mettre des fonctions de tests sans qu'ils soient utile (genre `assert 1 == 1`) est également rédhibitoire.

## Entrée utilisateurs et conversion de types

Après un input vous aurez **toujours** une chaîne de caractère. Il faut la convertir dans ce que va demander vos fonctions, ici des entiers.

Ne faites **PAS** de conversion de type dans vos fonctions. Si elles demandent des entrées entiers supposez que c'est le cas (par de `int(x) % 2` par exemple dans la fonction `syracuse`). Tôt ou tard ce genre chose va vous sauter à la figure car un jour vous votre programme va planter sans que vous compreniez pourquoi ni où est le soucis.
