---
layout: page
title:  "Algorithme, code et théorie : algorithmie / algorithmes"
category: cours
---

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [algorithme]({% link cours/algorithme-code-theorie/algorithme/index.md %}) / [algorithmes]({% link cours/algorithme-code-theorie/algorithme/algorithmes.md %})
{.chemin}

Pseudo-code, calcul et code sont les trois faces d'une même pièce nommée algorithme. Nous allons voir les implications de ces trois termes, mais commençons par définir un algorithme.

> Une super introduction aux algorithmes : <https://www.arte.tv/fr/videos/094414-012-A/declics/>

On doit le mot algorithme à [Ada Lovelace](https://fr.wikipedia.org/wiki/Ada_Lovelace) (1815-1852) qui est le(a) premier(e) informaticien(ne) de l'histoire. Elle a donné ce nom en hommage à un savant persan du IXème siècle (né vers 780 et mort en 850 à Bagdad) nommé [Al-Khwârizmî](https://fr.wikipedia.org/wiki/Al-Khw%C3%A2rizm%C3%AE) qui a publié le premier manuel d'algèbre connu à ce jour.

## algorithme ? {#algorithme}

Définition du 'Petit Robert'  d'un **algorithme** :

> ensemble des règles opératoires propres à un *calcul*
{.note}

Qu'est-ce que ça veut dire ?

* **algorithme** : ensemble des règles opératoires propres à un **calcul**
* **calcul** : enchaînement des instructions nécessaires à l'accomplissement d'une **tâche**
* **tâche** : ...

On a utilisé un algorithme pour comprendre ce qu'est un algorithme :

* *Nom* : définition_petit_robert
  * *paramètres* : un *mot_à_définir*
  * *sortie* : aucune
  * *description* : comprendre la définition d'un mot dans le 'Petit Robert'
* *corps de l'algorithme* :
  1. étant donné la définition nommée *définition* de *mot_à_définir* dans le 'Petit Robert'
  2. afficher *définition* à l'écran.
  3. pour chaque *mot* non compris dans *définition* :
     1. *définition_petit_robert(mot)*

C'est un algorithme tout à fait valable. Ce n'est pas du python, mais c'est :

* compréhensible
* chaque instruction (lire une définition, afficher à l'écran, ...) peut être caractérisée par un petit texte en français
* notre algorithme s'arrête bien à un moment (au pire une fois que l'on a passé en revu tous les mots du dictionnaire)

Règles de construction de l'algorithme utilisé :

* **des** paramètres en entrée mais **une** sortie (qui peut être une structure composée comme une liste ou un dictionnaire).
* le **retour** d'un algorithme est la dernière instruction qu'il fait, en rendant la sortie (ici, il ne rend rien)
* une description de ce qu'il fait
* L'exécution d'un algorithme est signifié par son nom suivie de parenthèses contenant ses paramètres
* afficher à l'écran n'est **PAS** un retour de fonction/méthode/algorithme.

Donald Knuth (1938-) liste, comme prérequis d'un algorithme, [cinq propriétés](https://fr.wikipedia.org/wiki/Algorithme) :

* **finitude** : *« Un algorithme doit toujours se terminer après un nombre fini d’étapes. »*
* **définition précise** : *« Chaque étape d'un algorithme doit être définie précisément, les actions à transposer doivent être spécifiées rigoureusement et sans ambiguïté pour chaque cas. »*
* **entrées** : *« […] des quantités qui lui sont données avant qu'un algorithme ne commence. Ces entrées sont prises dans un ensemble d'objets spécifié. »*
* **sortie** : *« […] des quantités ayant une relation spécifiée avec les entrées. »*
* **rendement** : *« […] toutes les opérations que l'algorithme doit accomplir doivent être suffisamment basiques pour pouvoir être en principe réalisées dans une durée finie par un homme utilisant un papier et un crayon. »*

On peut en déduire la **définition** suivante :

> Un **algorithme** est une succession d'instructions simples et clairement définies. A partir d'entrées, il produit une sortie en un nombre fini d'instructions.
{.note}

Ou, de façon équivalente :

> Les **4 propriétés générales** qui définissent un algorithme :
>
>1. un algorithme est constitué d'un ensemble fini d'instructions, décrites avec un nombre fini de symboles
>2. si l'algorithme produit un résultat cela doit être fait après un nombre fini d'étapes (une étape étant l'application d'une instruction) successives.
>3. un humain doit pouvoir suivre chaque étape avec un papier et un crayon
>4. exécuter une instruction ne doit pas nécessiter d'intelligence (à part celle pour comprendre l'instruction)
>
{.note}

Un algorithme est donc constitué de trois parties :

* une liste d'instructions possibles
* le nombre d'instructions nécessaires pour s'exécuter (ce qu'on appelle **complexité**)
* une caractérisation de la sortie

## algorithmes ! {#algorithmes-trois-voies}

La définition très générale d'un algorithme se décline usuellement sous trois formes :

1. [pseudo-code]({% link cours/algorithme-code-theorie/algorithme/pseudo-code.md %}) : l'écriture (sans ordinateur) d'algorithmes en utilisant un nombre restreint d'instructions précisément définies. Un pseudo-code n'est pas directement fait pour être exécuté par un ordinateur, même si l'on peut utiliser un langage de programmation pour décrire notre code. Le but ici est de résoudre un problème donné avec un algorithme utilisant le moins d'instructions possibles.
2. [fonctions]({% link cours/algorithme-code-theorie/theorie/fonctions.md %}). Un algorithme est vu comme une fonction qui calcule un nombre. Le but est ici de comprendre ce que peuvent faire les algorithmes, quels sont les problèmes qu'ils peuvent résoudre.
3. [coder]({% link cours/algorithme-code-theorie/code/coder.md %}) : l'écriture d'un programme pouvant s'exécuter sur un ordinateur. Le but sera ici de faire en sorte de vérifier que le code correspond bien au pseudo-code et — surtout — de maintenir son fonctionnement au court du temps.

Ces trois formes ont des buts différents, mais on ne peut exceller dans l'une sans connaitre les autres. Tout algorithmicien doit avoir de bonnes connaissances théoriques sur ce que peut calculer  un ordinateur et — tôt ou tard — il devra programmer ses algorithmes ; tout développeur doit avoir des connaissances fortes en algorithmie pour pouvoir écrire du code performant.

## étude

Quelque-soit la forme que prendra vos algorithmes (pseudo-code, code ou calcul), il faudra **toujours** vérifier qu'il fait bien ce qu'on attend de lui. Ainsi :

> Pour chaque algorithme il faudra :
>
> 1. vérifier le fonctionnement de l'algorithme sur de petits exemples que l'on peut tester à la main
> 2. prouver l'algorithme :
>    * preuve que l'algorithme termine
>    * preuve qu'il résout le problème demandé
> 3. évaluer ses performances en calculant sa complexité, c'est à dire le nombre d'instructions qu'il a effectué avant de se terminer
>
{.note}
