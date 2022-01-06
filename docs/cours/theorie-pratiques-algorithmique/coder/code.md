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

Ces règles sont appelées des **coding mantra**. Comme toutes les règles, il ne faut pas apprendre ce qu'elle dit, mais pourquoi elle le dit. Par exemple : on ne doit pas passer du temps à chaque lecture pour comprendre ce que fait un bout de code, comment il est organisé ou encore se questionner pour savoir s'il fonctionne : il faut pouvoir aller rapidement là où l'on veut modifier son code et comprendre aisément comment le modifier.

Nous allons maintenant lister les bonnes pratiques fondamentales à posséder lorsque l'on code.

> Les différentes méthodes et mantra que l'on va voir sont issues de l'[XP](https://fr.wikipedia.org/wiki/Extreme_programming), qui date des années 2000 mais dont on à l'impression qu'elle a été écrite hier (voir demain tellement elle est encore novatrice).

## noms explicites et découpage fonctionnel

* des noms de variables **explicites**
* on préfèrera de **petites fonctions/méthodes** avec noms explicites à de nombreuses lignes de code

Ceci permet de lire le code comme on lirait un texte, ce qui permet de rapidement comprendre ce qu'il fait, juste en le lisant. Les petites fonctions sont de plus facilement modifiables et testables.

Le découpage fonctionnel de votre code permet d'éviter la duplication de code, qui est un mal absolu en code. Si l'on copie/colle du code et qu'il y a un bug ou qu'on veut modifier le fonctionnement de ce code, il faudra se rappeler de tous les endroits où le code a été copié, ce qui est impossible ! De plus, cela rend votre code peu lisible.

> **Coding antra :** [DRY](https://fr.wikipedia.org/wiki/Ne_vous_r%C3%A9p%C3%A9tez_pas)
{: .note}

On saura que le code est ok lorsqu'il ne nécessitera **pas** de commentaires pour être compris. Ils sont en effet remplacé par des noms de variables explicites et les noms de fonctions qui doivent expliquer ce qu'elles font.

> **Coding mantra :** [NO COMMENTS !](https://www.developpez.com/actu/150066/Programmation-quand-faut-il-commenter-son-code-Google-s-invite-dans-le-debat-et-montre-que-les-commentaires-peuvent-tres-souvent-etre-evites/)
{: .note}

En plus d'être inutile :

* **les commentaires sont souvent des mensonges** : comme le commentaire n'est pas du code, lorsque l'on modifie le code on *oublie* de changer le commentaire. Au bout d'un moment le commentaire n'est donc plus en relation avec le code : au lieu d'aider à comprendre, il confuse : un commentaire est donc tôt ou tard un mensonge.
* **ils cachent la difficulté**. S'il y a plein de commentaire, on ne les lira plus. Un commentaire se doit d'être rare. S'il est là c'est que l'on a pas vraiment pu faire autrement. Vous n'en aurez pas besoin dans 99% des cas...

Attention cependant, commentaires != documentation :

* Si votre code est destiné à être utilisé uniquement par vous ou votre équipe, on n'a pas besoin de le documenter. Son organisation et son écriture doit se suffire à lui-même.
* si votre code va être utilisé par des inconnus (lorsque vous créez une [bibliothèque](https://fr.wikipedia.org/wiki/Biblioth%C3%A8que_logicielle) par exemple), les fonctions publiques doivent être documentées. Un utilisateur doit pouvoir utiliser votre code sans effort.

Lorsque l'on utilise une [API](https://fr.wikipedia.org/wiki/Interface_de_programmation), on a en effet jamais accès aux corps des méthodes, mais juste à leurs noms : : on a besoin de savoir comment elle fonctionne sans en connaitre le corps :

> Toutes les méthodes destinées à être utilisées par des clients/utilisateurs différents de l'équipe de développement doivent être documentées.
{: .note}

## lisibilité

Un code est fait pour être relu et amélioré. On doit donc privilégier la lecture à son écriture. Pour que votre équipe ou vous même puissiez le relire plus tard sans faire d'effort de compréhension.

>**Ecrire du code n'est pas un concours d'érudition.**

Ecriture claire du code : si on a le choix entre écrire du code utilisant des subtilités mais difficile à comprendre ou du code plus basique mais lisible on choisira **TOUJOURS** le code lisible.

> **Coding mantra :** [KISS](https://fr.wikipedia.org/wiki/Principe_KISS)
{: .note}

Si le fond doit être simple, la forme du code est importante aussi. Il se doit d'être agréable à lire et homogène. L'équipe de développement doit se mettre d'accord sur un [coding style](https://fr.wikipedia.org/wiki/Style_de_programmation). Par défaut on utilise le standard du langage. En python, c'est la  [PEP8](https://www.python.org/dev/peps/pep-0008/)

> Utilisez un style de programmation homogène pour faciliter la lecture de code. Si possible, automatisez ce processus avec un outil automatique de formatage de code.
{: .code}

## efficacité

On ne dois jamais coder de choses inutiles : tout bout de code doit être utilisé au moment où il est écrit. On ne codera jamais de fonctionnalités qui vont être utiles plus tard (car "plus tard" le code ne sera plus le même et l'intégration de la fonctionnalité ne sera pas immédiate et, vraisemblablement, les besoins auront changés et l'instant "plus tard" n'arrivera jamais) et tout code qui n'est plus utile est immédiatement supprimé (pour les mêmes raisons).

> **Coding mantra :** [YAGNI](https://fr.wikipedia.org/wiki/YAGNI)

## tests

Pour s'assurer que notre code fait bien ce qu'il est sensé faire, on effectuera des **tests**. C'est le pendant code de la preuve d'un algorithme.

Comme on passe son temps à modifier son code, il est nécessaire de conserver ses tests pour pouvoir les exécuter très souvent et vérifier que son code continue de fonctionner.

Lorsque l'on ajoute des fonctionnalités au code ou que l'on corrige un bug, on écrit un test qui vérifie la fonctionnalité ou qui montre que le bug n'existe pas/plus. Ainsi, puisque les tests sont conservées, ce bug ne pourra plus jamais réapparaître et cette fonctionnalité ne pourra plus disparaître.

> Coding mantra :** [TDD](https://artificials.ch/test-driven-development-mantra/)
{: .note}

Nous n'utiliserons pas ici au début le mantra TDD dans son intégralité puisque l'on se permettra d'écrire les tests après avoir codé la fonctionnalité et pas avant. Mais, l'expérience venant, faites l'expérience de coder vos tests avant la fonction, c'est très utile car cela permet d'utiliser sa fonction avant de la coder, ce qui souvent change la façon dont on voulait coder la fonction initialement.

Les tests sont autant de cas d'utilisation de vos programmes qui montrent qu'il fonctionne et comment il fonctionne. Il permettent de montrer les différentes fonctionnalités de votre code :

> **La fonctionnalité est plus importante que le code** : Le code va changer, les fonctionnalités doivent rester.
{: .note}

Enfin, le code et ses tests doivent être fait par la **même personne** et au **même moment**. Il ne faut pas attendre d'avoir codé plusieurs fonctions avant de faire ses tests. Vous n'êtes en effet pas sur que votre 1ère fonction codée fonctionne avant d'avoir fait des tests. De là, il est possible qu'un bug dans cette première fonction affecte le code de votre seconde fonction... Lorsque vous ferez vos tests vous serez alors obligé de re-coder toutes vos fonctions ce qui ne serait pas arrivé si vous aviez testé toutes vos fonction une par une et au moment de les coder.

## structure d'un programme

Tout ce qu'on vient de voir structure un projet informatique en trois entités : 

* le **programme principal** (aussi appelé **main**) qui est ce qui sera exécuté
* le **code** qui regroupe l'ensemble des fonctions utilisée par le programme principal
* les **tests** qui *certifient* que le code fonctionne.

Ces trois entités sont d'égale importance et sont **toujours** codées en même temps.

Exemples :

* pour rajouter une fonctionnalité au programme principal, on ajoute du code qui doit lui-même être testé pour vérifier qu'il fonctionne.
* pour corrigé un bug du programme principal, on modifie du code et on ajoute des tests qui montrent que le bug n'existe plus.
