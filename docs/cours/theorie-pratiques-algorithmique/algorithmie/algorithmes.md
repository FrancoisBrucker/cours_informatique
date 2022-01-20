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
* une vérification.

On voit en creux que des notions de **vérification** (caractériser la sortie) et de  () apparaissent également.

## algorithmes ! {#algorithmes-trois-voies}

La définition très générale d'un algorithme se décline usuellement sous trois formes :

1. [pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %}) : l'écriture (sans ordinateur) d'algorithmes en utilisant un nombre restreint d'actions que l'on définira précisément. Un pseudo-code n'est pas directement fait pour être exécuté par un ordinateur, même si l'on peut utiliser un langage de programmation pour décrire notre code. Le but ici est de résoudre un problème donné avec un algorithme de complexité la plus faible possible.
2. [calcul]({% link cours/theorie-pratiques-algorithmique/theorie/calcul.md %}). Un algorihtme est vu comme une fonction qui calcule un nombre. Le but est ici de comprendre ce que peuvent faire les algorithmes, quels sont les problèmes qu'ils peuvent résoudre.
3. [code]({% link cours/theorie-pratiques-algorithmique/coder/code.md %}) : l'écriture d'un programme pouvant s'exécuter sur un ordinateur. Le but sera ici de faire en sorte de vérifier que le code correspond bien au pseudo-code et — surtout — de maintenir son fonctionnement au court du temps.

Ces trois formes ont des buts diférents, mais on ne peut exceller dans l'une sans connaitre les autres. Tout algorithmicien doit avoir de bonnes connaissances théoriques sur ce que peut calculer  un ordinateur et — tôt ou tard — il devra programmer ses algorithmes; tout développeur doit avoir des connaissances fortes en algorithmie pour pouvoir écrire du code performant.

## étude

Quelque-soit la forme que prendra vos algorithmes (pseudo-code, programme ou fonction), il faudra toujours vérifier qu'il fait bien ce qu'on attend de lui. Ainsi :

> Pour chaque algorithme il faudra :
>
> 1. vérifier le fonctionnement de l'algorithme sur de petits exemples que l'on peut tester à la main
> 2. prouver l'algorithme :
>   * preuve que l'algorithme termine
>   * preuve qu'il résout le problème demandé
> 3. évaluer ses performances en calculant sa complexité
>
{: .note}

