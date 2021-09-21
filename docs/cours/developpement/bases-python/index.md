---
layout: page
title:  "Bases de python"
author: "François Brucker"
---

[développement]({% link cours/developpement/index.md %}) / [bases de python]({% link cours/developpement/bases-python/index.md %})

Un court cours sur les bases de python. On montrera les types de bases et diverses possibilités du langages. Le niveau est basique et va préparer le cours de développement objet. On présuppose juste que vous ne soyez pas débutant complet en informatique.

## Premier programme

[Le tutoriel premier programme]({% link cours/developpement/bases-python/premier-programme.md %}) vous fera utiliser pour la première fois le langage python avec l'éditeur vscode.

## objets de python

[La partie objets types et types d'objets]({% link cours/developpement/bases-python/objets-types.md %}) vous dira tout sur les objets courant que vous manipulerez en python.

## variables

[variable et espace de noms]({% link cours/developpement/bases-python/variables.md %}) vous montrera le principe de l'affectation des variables en python.

## conteneur

Les objets peuvent être stockés dans des structures nommées conteneur, comme la [structure de liste]({% link cours/developpement/bases-python/listes.md %}) par exemple : un conteneur est ainsi un objet qui en contient d'autres.

## opérations sur les objets

On peut facilement faire des [opérations sur les objets]({% link cours/developpement/bases-python/operations.md %}).

## bloc de code

Si python ne pouvait qu'exécuter ligne à ligne un code on ne pourrait pas faire grand chose. Le principe des programmes est de pouvoir grouper les instructions en bloc.

En python, un bloc est toujours défini de la même manière  :

* Ce qui va identifier le bloc pour son exécution (une condition, son nombre d'exécution, son nom) et se finit par un `:`
* Les instructions le constituant.

Pour séparer les blocs les un des autres, et savoir ce qui le définit, le langage Python utilise l'indentation (4 espaces par défaut): un bloc est donc une suite d'instructions ayant la même indentation.

```text
type de bloc:
    instruction 1
    instruction 2
    ...
    instruction n
```

Ces différents blocs sont pratiques car ils vont nous permettre de :

* les [exécuter un certain nombre de fois]({% link cours/developpement/bases-python/boucles.md %})
* les [exécuter si une condition est vraie]({% link cours/developpement/bases-python/conditions.md %})

Si un bloc de code est exécuté plusieurs fois à l'identique, on aimerait aussi pouvoir nommer ce groupe pour voir le réutiliser juste en appelant son nom, on appelle ces groupe des [fonctions]({% link cours/developpement/bases-python/fonctions.md %})

## modules

les [modules python]({% link cours/developpement/bases-python/modules.md %}) permettent de se faciliter la vie dans l'écriture des programmes grâces aux méthodes qu'ils définissent.

utilisation de random.

Comme un sous espace
interpéteur exécution dans le terminal
ligne à ligne
