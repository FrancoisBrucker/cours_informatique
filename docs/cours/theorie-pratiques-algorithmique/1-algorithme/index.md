---
layout: page
title:  "Algorithme"
category: cours
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [algorithme]({% link cours/theorie-pratiques-algorithmique/1-algorithme/index.md %})
{: .chemin}

* algorithmie : pseudo-code
* théorie : calcul
* développement : code

Pseudo-code, calcul et code sont les trois faces d'une même pièce nommée algorithme. Nous allons voir les implications de ces trois termes, mais commençons par définir un algorithme.

## algorithme ? {#algorithme}

Définition du 'Petit Robert'  d'un **algorithme** :

> ensemble des règles opératoires propres à un *calcul*
{: .note}

Qu'est-ce que ça veut dire ?

* **algorithme** : ensemble des règles opératoires propres à un **calcul**
* **calcul** : enchaînement des actions nécessaires à l'accomplissement d'une **tâche**
* **tâche** : ...

On a utilisé un algorithme pour comprendre ce qu'est un algorithme :

* *Nom* : définition_petit_robert
  * *paramètres* : un *mot_à_définir*
  * *sortie* : aucune
  * *description* : comprendre la définition d'un mot dans le 'Petit Robert'
* *corps de l'algorithme* :
  1. étant donné la définition nommée *définition* de *mot_à_définir* dans le 'Petit Robert'
  2. afficher *définition* à l'écran.
  3. pour chaque *mot* non compris dans *définition_mot* :
     1. *définition_petit_robert(mot)*

Nota Bene :

* afficher à l'écran n'est **PAS** un retour de fonction/méthode/algorithme.
* différence entre nom d'algorithme et exécution de fonction/méthode/algorithme avec des parenthèses
* **des** paramètres en entrée mais **une** sortie (qui peut être une structure composée comme une liste ou un dictionnaire)

Donald Knuth (1938-) liste, comme prérequis d'un algorithme, [cinq propriétés](https://fr.wikipedia.org/wiki/Algorithme) :

* finitude : *« Un algorithme doit toujours se terminer après un nombre fini d’étapes. »*
* définition précise : *« Chaque étape d'un algorithme doit être définie précisément, les actions à transposer doivent être spécifiées rigoureusement et sans ambiguïté pour chaque cas. »*
* entrées : *« […] des quantités qui lui sont données avant qu'un algorithme ne commence. Ces entrées sont prises dans un ensemble d'objets spécifié. »*
* sortie : *« […] des quantités ayant une relation spécifiée avec les entrées. »*
* rendement : *« […] toutes les opérations que l'algorithme doit accomplir doivent être suffisamment basiques pour pouvoir être en principe réalisées dans une durée finie par un homme utilisant un papier et un crayon. »*

On pourrait en déduire la définition suivante :

> Un algorithme est une succession d'actions simples et clairement définies. A partir d'entrées, il produit une sortie en un nombre fini d'actions.
{: .note}

On voit en creux que des notions de **vérification** (caractériser la sortie) et de **complexité** (nombre d'opérations nécessaires à son fonctionnement) apparaissent également.

## plan

La suite de cette partie va être consacrée à préciser les notions d'actions (qu'ai-je le droit d'utiliser ?), de calcul (que fait un algorithme) et de code (comment exécuter sur un ordinateur un algorithme).

1. [pseudo-code]({% link cours/theorie-pratiques-algorithmique/1-algorithme/pseudo-code.md %})
2. [calculs]({% link cours/theorie-pratiques-algorithmique/1-algorithme/calcul.md %})
3. [code]({% link cours/theorie-pratiques-algorithmique/1-algorithme/code.md %})
