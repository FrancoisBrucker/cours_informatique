---
layout: page
title:  "Théorie et pratiques algorithmique : coder"
category: cours
---

> [Théorie et pratiques algorithmique]({% link cours/theorie-pratiques-algorithmique/index.md %}) / [coder]({% link cours/theorie-pratiques-algorithmique/coder/index.md %}) / [code]({% link cours/theorie-pratiques-algorithmique/coder/code.md %})
>
> **prérequis :**
>
>* [algorithmie/pseudo-code]({% link cours/theorie-pratiques-algorithmique/algorithmie/pseudo-code.md %})
{: .chemin}

*Coder* c'est passer d'un algorithme *papier* (pseudo-code ou idées) à un programme informatique, appelé **code**. Par extension, on inclura dans cette partie la modification d'un code existant. Le **but** d'un code est d'être exécuté par un ordinateur pour réaliser une tâche.

Pour permettre son exécution, le code est écrit dans un [langage de programmation](https://fr.wikipedia.org/wiki/Langage_de_programmation). Celui-ci dépend **dépend de la tâche à réaliser** : [le code est un outil](https://www.jesuisundev.com/la-religion-chez-les-developpeureuses-informatiques/) il faut utiliser celui qui est le plus adapté au résultat voulu.

> Nous utiliserons ici le [python](https://www.python.org/) car notre but est ici de coder des algorithmes classiques et python est très proche d'un pseudo-code.

Modifier du code est ce vous ferez le plus souvent : on passe son temps à modifier du code plutôt que d'implémenter des algorithmes (c'est ce que l'on appelle le [refactoring](https://fr.wikipedia.org/wiki/R%C3%A9usinage_de_code)).

Il en découle que :

> **Vous allez passer plus de temps à lire du code qu'à en écrire.**
{: .note}

Comme il faut que : *ce qui se fait souvent doit se faire rapidement*, on utilisera une série de règles pour lire aisément son code et — surtout — se faire comprendre aisément de ses partenaires.

> Ces règles sont appelées des **coding mantra**. Comme toutes les règles, il ne faut pas apprendre ce qu'elle dit, mais pourquoi elle le dit.

Lorsque l'on code, on ne doit pas passer cinq minutes à chaque lecture pour comprendre ce que fait un bout de code, comment il est organisé ou encore se questionner pour savoir s'il fonctionne : il faut pouvoir aller rapidement là où l'on veut modifier son code et comprendre aisément comment le modifier.

> Le mantra associé est le [KISS](https://fr.wikipedia.org/wiki/Principe_KISS). Il en découle trois pratiques :
>
> * noms explicites et découpage fonctionnel
> * lisibilité: coding style
> * tests
{: .note}

> TBD : 
>
>Pour que l'algorithme soit implémentable pour de vrai, il est nécessaire que sa description soit facilement transposable d'une langue à un langage de programmation.
>
>
>
>
>attention : les réels n'existent pas en vrai !




#### noms explicites et découpage fonctionnel

* des noms de variables **explicites** 
* on préfèrera des **petites fonctions/méthodes** avec noms explicites à de nombreuses lignes de code


On ne mettra **PAS** de commentaires partout ! 

* souvent on modifie le code et pas le commentaire, au bout d'un moment le commentaire n'est donc plus en relation avec le code : au lieu d'aider à comprendre, il confuse : **un commentaire est donc tôt ou tard un mensonge**
* s'il y a plein de commentaire, on ne les lira plus. Un commentaire se doit d'être rare. S'il est là c'est que l'on a pas pu faire autrement, vous n'en aure pas besoin den 99% des cas...

Une structuration adaptée et des bons noms permettent de se [passer de commentaires](https://www.developpez.com/actu/150066/Programmation-quand-faut-il-commenter-son-code-Google-s-invite-dans-le-debat-et-montre-que-les-commentaires-peuvent-tres-souvent-etre-evites/)

>**Attention** : commentaire != documentation (recopiez le 10 000 fois)

* Si votre code est destiné à être utilisé uniquement par vous ou votre équipe, on n'a pas besoin de le documenter. Son organisation et son écriture doit se suffire à lui-même.
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
