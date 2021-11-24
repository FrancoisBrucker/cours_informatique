---
layout: page
title:  "Bases de python"
authors: 
    - Augustin Agbo-Kpati
    - François Brucker
    - Pascal Préa
---

> [développement]({% link cours/developpement/index.md %}) / [bases de python]({% link cours/developpement/bases-python/index.md %})
{: .chemin}

Un court cours sur les bases de python. On montrera les types de bases et diverses possibilités du langages. Le niveau est basique et va préparer le cours de développement objet. On présuppose juste que vous ne soyez pas débutant complet en informatique.

## interpréteur

L'installation des plugins vscode pour python vous a fait écrire votre 1er programme python. Tout programme python est exécuté par l'interpréteur, c'est le cœur de python. Tout programme python est exécuté de la même manière :

1. on entre une ligne de code dans l'interpréteur
2. l'interpréteur exécute cette ligne dans son *espace de noms global* (*global namespace*)
3. une fois la ligne exécutée, l'interpréteur redonne la main à l'utilisateur
4. retour à la l'étape 1.

Un *espace de noms* est un endroit où seront stockées les différentes variables par exemple. C'est tout ce dont il faut se souvenir pour les futures lignes de code. A chaque fois que l'on exécute l'interpréteur, un nouvel *espace de noms global* est crée et une fois que l'on stoppe l'interpréteur, cet *espace* est détruit.

> Le fait qu'un espace de nom existe est crucial pour pouvoir utiliser des variables et le fait qu'il soit créé au début du programme (au lancement de l'interpréteur) détruit une fois le programme terminée (une fois que l'interpréteur s'arrête) permet d'assurer qu'un programme donnera toujours le même résultat (si l'espace de noms était toujours le même il resterait des variables d'un ancien programme dans un nouveau...).

Les namespaces ne font que stocker des noms, ils peuvent donc être créés et détruits sans détruire des objets. Seul un objet qui n'est référencé dans aucun namespace est effacé car on ne peut plus y accéder.

## objets de python

[La partie objets types et types d'objets]({% link cours/developpement/bases-python/objets-types.md %}) vous dira tout sur les objets courant que vous manipulerez en python.

## variables

[variable et espace de noms]({% link cours/developpement/bases-python/variables.md %}) vous montrera le principe de l'affectation des variables en python.

## conteneur

Les objets peuvent être stockés dans des structures nommées conteneur, comme la [structure de liste]({% link cours/developpement/bases-python/listes.md %}) par exemple : un conteneur est ainsi un objet qui en contient d'autres.

## opérations sur les objets

On peut facilement faire des [opérations sur les objets]({% link cours/developpement/bases-python/operations.md %}).

## blocs de code

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

Ces différents blocs sont pratiques car ils vont nous permettre :

* d'**exécuter un certain nombre de fois un bloc donné** grâce aux [boucles]({% link cours/developpement/bases-python/boucles.md %}).
* d'**exécuter si une condition est vraie** grâce aux [conditions]({% link cours/developpement/bases-python/conditions.md %})

Si un bloc de code est exécuté plusieurs fois à l'identique, on aimerait aussi pouvoir nommer ce groupe pour **pouvoir le réutiliser juste en appelant son nom**, ce sont les [fonctions]({% link cours/developpement/bases-python/fonctions.md %})

## modules

les [modules python]({% link cours/developpement/bases-python/modules.md %}) permettent de se faciliter la vie dans l'écriture des programmes grâces aux méthodes qu'ils définissent.

## notation `.`

On l'a vue pour les méthodes et les modules. De façon générale la notation `A.B` : se lit ainsi on cherche le nom `B` dans l'espace de nom `A`.

> une méthode n'est rien d'autre qu'un nom appelable dans l'espace de nom de l'objet à gauche du point
