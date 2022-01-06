---
layout: page
title:  "Théorie et pratiques algorithmique : algorithmie / algorithmes"
category: cours
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [algorithme]({% link cours/theorie-pratiques-algorithmique/algorithmie/index.md %}) / [algorithmes]({% link cours/theorie-pratiques-algorithmique/algorithmie/algorithmes.md %})
{: .chemin}

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

Un algorithme est donc constitué de trois parties :

* une liste d'actions possibles
* le nombre d'actions nécessaires pour s'exécuter (ce qu'on appelle **complexité**)
* une vérification
On voit en creux que des notions de **vérification** (caractériser la sortie) et de  () apparaissent également.

## algorithmes ! {#algorithmes-trois-voies}

La définition très générale d'un algorithme est déclinée selon trois voies :

1. L'écriture (sans ordinateur) d'algorithmes en utilisant un nombre restreint d'actions que l'on définira précisément. On appelle cette forme d'algorithme [pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}) car ils ne sont pas directement fait pour être exécutés par un ordinateur. Le but ici est de résoudre un problème donné avec un algorithme de complexité la plus faible possible. C'est **l'algorithmie**
2. [Que calcule un algorithme ?]({% link cours/theorie-pratiques-algorithmique/theorie/calcul.md %}). Cette partie s'attache à comprendre ce qu'est un algorithme de façon théorique et des problèmes qu'ils peuvent **théoriquement** résoudre.
3. [Comment exécuter (coder) un algorithme]({% link cours/theorie-pratiques-algorithmique/coder/code.md %}) sur un ordinateur et maintenir son fonctionnement au court du temps.

Les visions trois vision ci-dessus ont des points communs mais également des différences car leur but est différent. Un "honnête informaticien" doit avoir des bases dans ces trois disciplines car l'informatique en tant que science regroupe ces trois champs.
