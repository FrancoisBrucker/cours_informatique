---
layout: page
title:  "Introduction : Algorithme ? Code ?"
category: cours
tags: informatique cours
author: "François Brucker"
---

## Introduction

Définition du 'Petit Robert'  d'un *algorithme* :

> ensemble des règles opératoires propres à un *calcul* 

Qu'est-ce que ça veut dire ?

* **algorithme** : ensemble des règles opératoires propres à un *calcul* 
* **calcul** : enchaînement des actions nécessaires à l'accomplissement d'une *tâche*
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
*  **des** paramètres en entrée mais **une** sortie (qui peut être une structure composée comme une liste ou un dictionnaire)


Donald Knuth (1938-) liste, comme prérequis d'un algorithme, [cinq propriétés](https://fr.wikipedia.org/wiki/Algorithme) :

* finitude : *« Un algorithme doit toujours se terminer après un nombre fini d’étapes. »*
* définition précise : *« Chaque étape d'un algorithme doit être définie précisément, les actions à transposer doivent être spécifiées rigoureusement et sans ambiguïté pour chaque cas. »*
* entrées : *« […] des quantités qui lui sont données avant qu'un algorithme ne commence. Ces entrées sont prises dans un ensemble d'objets spécifié. »*
* sortie : *« […] des quantités ayant une relation spécifiée avec les entrées. »*
* rendement : *« […] toutes les opérations que l'algorithme doit accomplir doivent être suffisamment basiques pour pouvoir être en principe réalisées dans une durée finie par un homme utilisant un papier et un crayon. »*


On voit en creux que des notions de **vérification** (preuve que l'algorithme fait bien ce qu'on pense qu'il fait) et de **complexité** (nombre d'opérations nécessaire à son fonctionnement) apparaissent.

> **algorithme != code** (recopiez le 100 fois)

Pour que l'algorithme soit implémentable pour de vrai, il est nécessaire que sa description soit facilement transposable d'une langue à un langage de programmation.

Le code va dépendre du langage, pour nous le python. Cela permet de voir si notre algorithme marche "en vrai". On utilisera les même principes, mais de façon différente. Ce sont deux face d'une même pièce. On ne peut pas faire l'un sans l'autre.


## algorithme

Pour nos algorithmes on voudra : 

* qu'ils soient lisibles,
* qu'ils soient justes,
* en connaître les performances.



### lisible

#### pseudo-code

Le but d'un algorithme papier est d'être compris. On utilisera pour l'écrire une série de règles compréhensibles par tout le monde : le pseudo-code. Ce n'est ni une langue ni un langage.

* tests et choix :
	* plus petit que, plus grand que, égal à, etc
	* si ... alors ... sinon
	* si ... alors si ... alors ... sinon
* affectations :
	* une seule opération modifiant les variables
* répétition :
	* faire ... tant que ..., 
	* tant que ... faire ..., 
	* pour tout ... faire ..., 
	* etc

Le plus souvent, on utilisera un mix de python et de français.

#### Attentions aux excès : trop détaillé

il est plus clair d’écrire ça
```
tant que x > 0:
    x = x - 1
```	

que :

```
A: 

if x <= 0 
goto B
endif

x=x-1
goto A

B:
```

#### Attentions aux excès : trop approximatif

éviter le syndrome : "tire la chevillette et la bobinette cherra"

Les opérateurs *complexes** sont des fonctions (d’autres algorithmes) qui doivent être décrits s’il ne sont pas immédiatement compréhensibles.

#### Structures et objets utilisées 

Lorsque l'on utilise des méthodes d'objets (comme une `ma_liste.index("?")`, `x in ma_chaine_de_caractères`) ou des structures compliquées (télécharger un fichier d'internet) on doit en connaître le coût : la complexité, les cas d'usage (être connecté), etc

### preuve

On **démontrera** le fonctionnement de l'algorithme en utilisant des preuves mathématiques.

### performances

On calculera la complexité de l'algorithme :
* nombre d'opérations
* place en mémoire

Ces complexités dépendent des paramètres de l'algorithme et, parfois de circonstances extérieures comme l'état du réseau par exemple.

## code

Le code est le passage d'un algorithme *papier* à un programme informatique ou la modification d'un code existant. La seconde partie étant celle que vous ferez le plus souvent : On passe son temps à modifier du code plutôt que d'implémenter des algorithme (c'est ce que l'on appelle le refactoring). 

Il en découle que **Vous allez passer plus de temps à lire du code qu'à en écrire.** 

Comme il faut que : *ce qui se fait souvent doit se faire rapidement*, on utilisera une série de règles pour lire aisément son code et se faire comprendre aisément de ses partenaires.
On ne doit pas passer 5min à chaque lecture pour comprendre ce que fait l'algorithme à son organisation ou se questionner s'il fonctionne, il faut pouvoir aller rapidement là où l'on veut modifier son code et comprendre aisément comment le modifier.

Ce principe est appelé le  [KISS](https://fr.wikipedia.org/wiki/Principe_KISS). Il en découle trois pratiques :

* noms explicites et découpage fonctionnel 
* lisibilité: coding style
* tests

#### noms explicites et découpage fonctionnel 

* des noms de variables **explicites** 
* on préfèrera des **petites fonctions/méthodes** avec noms explicites à de nombreuses lignes de code


On ne mettra **PAS** de commentaires partout ! 

* souvent on modifie le code et pas le commentaire, au bout d'un moment le commentaire n'est donc plus en relation avec le code : au lieu d'aider à comprendre, il confuse : **un commentaire est donc tôt ou tard un mensonge**
* s'il y a plein de commentaire, on ne les lira plus. Un commentaire se doit d'être rare. S'il est là c'est que l'on a pas pu faire autrement, vous n'en aure pas besoin den 99% des cas...


Une structuration adaptée et des bons noms permettent de se [passer de commentaires](https://www.developpez.com/actu/150066/Programmation-quand-faut-il-commenter-son-code-Google-s-invite-dans-le-debat-et-montre-que-les-commentaires-peuvent-tres-souvent-etre-evites/)



>**Attention** : commentaire != documentation (recopiez le 10 000 fois)

* Si votre code est déstiné à être utilisé uniquement par vous ou votre équipe, on n'a pas besoin de le documenter. Son organisation et son écriture doit se suffire à lui-même.
* si votre code va être utilisé par des inconnus (lorsque vous créez une API par exemple), les fonctions publiques doivent être documentées. Un utilisateur doit pouvoir utiliser votre code sans effort.



#### lisibilité

Un code est fait pour être relu et amélioré. On doit donc privilégier la lecture à son écriture. Pour que votre équipe ou vous puissiez le relire plus tard sans faire d'effort de compréhension. 

>**Ecrire du code n'est pas un concours d'érudition.**

* écriture claire du code : si on a le choix entre écrire du code utilisant des subtilités mais difficile à comprendre ou du code plus basique mais lisible on choisira **TOUJOURS** le code lisible.
* coding style : style commun à toute l'équipe de développement. Par défaut on utilise le standard du langage. En python, c'est la  [PEP8](https://www.python.org/dev/peps/pep-0008/) : http://sametmax.com/le-pep8-en-resume/ 

#### tests

Pour s'assurer que notre code fait bien ce qu'il est sensé faire, on effectuera des **tests**. C'est le pendant code de la preuve d'un algorithme.

Comme on passe son temps à modifier son code, il est nécessaire de conserver ses tests pour pouvoir les exéctuer très souvent et vérifier que son code continue de fonctionner.

Lorsque l'on ajoute des fonctionnalités au code ou que l'on corrige un bug, on écrit un test qui vérifie la fonctionnalité ou qui montre que le bug n'existe pas/plus. Ainsi, puisque les tests sont conservées, ce bug ne pourra plus jamais réapparaître et cette fonctionnalité ne pourra plus disparaître.

**La fonctionnalités est plus importante que le code** : Le code va changer, les fonctionnalités doivent rester.
Ce sont de plus des cas d'utilisation de vos programmes qui montrent qu'il fonctionne et comment il fonctionne.

## structure d'un programme

Un programme est composé de trois entités :

* le **programme principal** (aussi appelé **main**) qui est ce qui sera exécuté
* le **code** qui regroupe l'ensemble des fonctions utilisée par le programme principal
* les **tests** qui *certifient* que le code fonctionne.

Ces trois entités sont d'égale importance et sont **toujours** codées en même temps.

Exemples :

* pour rajouter une fonctionnalité au programme principal, on ajoute du code qui doit lui-même être testé pour vérifier qu'il fonctionne.
* pour corrigé un bug du programme principal, on modifie du code et on ajoute des tests qui montrent que le bug n'existe plus.

>**Attention** : le code et ses tests doivent être fait par la **même personne** et au **même moment** (voir avant).


