---
layout: page
title:  "Algorithme : machine de Turing calculs ?"
category: cours
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [théorie]({% link cours/theorie-pratiques-algorithmique/theorie/index.md %}) / [calculabilité]({% link cours/theorie-pratiques-algorithmique/theorie/calculabilite.md %})
>
> prérequis :
>
> * [machine de turing]({% link cours/theorie-pratiques-algorithmique/theorie/machine-turing.md %})
> * [complexité d'un problème]({% link cours/theorie-pratiques-algorithmique/algorithmie/complexite-probleme.md %})
{: .chemin}

La machine de Turing est un modèle permettant de rendre compte d'un algorithme. Soit $M$ une machine de turing. A partir d'un mot $E$ sur le ruban, la machine va soit :

* ne pas s'arrêter (elle n'arrivera jamais sur un état final)
* s'arrêter avec l'état $q$ et le mot $S$ inscrit sur le ruban au bout d'un nombre fini d'opérations.

Connaitre l'algorithme de la machine correspond ainsi à **deux** problèmes :

1. connaitre les mots d'entrée qui vont faire stopper la machine : c'est la *décidabilité*
2. connaitre la sortie de la machine pour un mot d'entrée qui la fait s'arrêter : c'est la *calculabilité*

Aucun de ces deux problèmes n'est simple.

## décidabilité

Formalisons le problème :

> Soit $M$ une machine de Turing sur un alphabet d'entrée $\Sigma$. L'ensemble des mots de $\Sigma$ acceptés par $M$ est noté $\mathcal{L}(M)$.
> ne ensemble de mots $L$ d'un alphabet $\Sigma$ est **reconnaissable** s'il existe une machine de Turing $M$ d'alphabet d'entrée $\Sigma$ tel que $L = $\mathcal{L}(M)$
{: .note}


> la notion de rejet ?
{: .note}


> U Soit $M$ une machine de Turing sur un alphabet d'entrée $\Sigma$. L'ensemble des mots de $\Sigma$ acceptés par $M$ est noté $\mathcal{L}(M)$.
{: .note}

> Etant donné un ensemble $\Gamma$ appelé *alphabet*, un **mot** est une suite finie  et un ensemble de mots $L$ de 
décidable = reconu et s'arrête sur oui ou non.
ex : syracuse

## calculabilité 

### fonctions calculables



### nombres calculables


<https://en.wikipedia.org/wiki/Computable_number>

* que peut-on calculer ? 
* de pseudo code à calcul de f(N) -> N

pour l'instant tous les pseudo-code qu'on a écrit s'arrêtent tout le temps. Mais celui là ? syracuse. On ne sais pas.

## arrêt de la machine



des actions sussessivent qui ment au résultat : ce n'est pas immédiat ! Et on ne sais pas si ça s'arrête.

passer d'un pseudo code à la machine. entier/réels/chaine de caractères. Permet de voir théoriquement ce qu'on peut faire.


## logique, démonstrations mathématiques et calculabilité

<https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Rice>
<https://en.wikipedia.org/wiki/List_of_undecidable_problems>

démonstation = pseudo-code

## Ackermann

Souvent, savoir si un algorithme va finir est trivial. Mais qu'en est-il de la [fonction d'Ackermann](https://fr.wikipedia.org/wiki/Fonction_d%27Ackermann), très importante en informatique théorique ?

En gros, c'est une fonction qui ne peut être décrite que par un algorithme. Il n'existe pas de fonction qui la calcule. Elle se définit de la manière suivante, pour tous entiers m et n positifs :

* A(m, n) = n + 1 si m = 0 
* A(m - 1, 1) si n = 0
* A(m - 1, A(m, n - 1)) sinon.

Cette fonction s'arrête bien un jour.



Pour chaque appel récursif de la fonction d'ackerman, soit m, soit $n$ est strictement plus petit dans la fonction appelée que dans la fonction appelante. On arrivera donc toujours à $m = 0$ qui stoppera la récursion ou $n = 0$ qui fera baisser la valeur de $m$.
 

Pour calculer Ack(2, 3) par exemple, on a les récurrences suivantes :

* Ack(2, 3) = Ack(1, Ack(2, 2))
* Ack(2, 2) = Ack(1, Ack(2, 1))
* Ack(2, 1) = Ack(1, Ack(2, 0))
* Ack(2, 0) = Ack(1, 1)
* Ack(1, 1) = Ack(0, Ack(1, 0))
* Ack(1, 0) = Ack(0, 1) = 2
* puis on remonte d'un cran et les récursions recommencent...


Au final on trouve Ack(2, 3) = 9. La fonction croît très très vite. Par exemple Ack(5, 0) = Ack (4, 1) = 65533 et Ack(4, 2) = $2^{65536} - 3$.

Complexité : nombre d'opération au moins supérieure à son résultat puisque que l'on ne fait qu'ajouter 1 à n comme calcul et les valeurs de n sont modifiées de +1 ou -1.


## refs

<https://plato.stanford.edu/entries/church-turing/>
<http://pageperso.lif.univ-mrs.fr/~kevin.perrot/documents/2016/calculabilite/Cours_16.pdf>
<https://www.cs.odu.edu/~zeil/cs390/latest/Public/turing-complete/index.html>