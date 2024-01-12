---
layout: layout/post.njk 
title: Coder

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


*Coder* c'est passer d'un algorithme *papier* (pseudo-code ou idées) à un programme informatique, appelé **code**. Par extension, on inclura dans cette partie la modification d'un code existant. Le **but** d'un code est d'être exécuté par un ordinateur pour réaliser une tâche.

Pour permettre son exécution, le code est écrit dans un [langage de programmation](https://fr.wikipedia.org/wiki/Langage_de_programmation). Celui-ci **dépend de la tâche à réaliser** : le code est un outil il faut utiliser celui qui est le plus adapté au résultat voulu.

{% info %}
Nous utilisons ici [le python](https://www.python.org/) car notre but est ici :

- de coder des algorithmes classiques et python est très proche du pseudo-code.
- d'apprendre les bonnes pratiques de développement et python est un langage qui permet de les apprendre simplement

Enfin, python est un langage très utilisé dans le monde, que ce soit par des informaticiens ou part des personnes devant utiliser du code informatiques au quotidien (scientifiques, ingénieurs en tous genres, data scientists, etc).
{% endinfo %}

Modifier du code est ce vous ferez le plus souvent : on passe son temps à modifier du code plutôt que d'implémenter des algorithmes (c'est ce que l'on appelle [le refactoring](https://fr.wikipedia.org/wiki/R%C3%A9usinage_de_code)).

Il en découle que :

{% note %}
Vous allez passer plus de temps à **lire** du code qu'à en **écrire**
{% endnote %}

Comme il faut que : *ce qui se fait souvent doit se faire rapidement*, on utilisera une série de règles pour lire aisément son code et — surtout — se faire comprendre aisément de ses partenaires.

Ces règles sont appelées des ***coding mantra***. Comme toutes les règles, il ne faut pas apprendre ce qu'elle dit, mais pourquoi elle le dit. Par exemple : on ne doit pas passer du temps à chaque lecture pour comprendre ce que fait un bout de code, comment il est organisé ou encore se questionner pour savoir s'il fonctionne : il faut pouvoir aller rapidement là où l'on veut modifier son code et comprendre aisément comment le modifier.

Nous allons maintenant lister les bonnes pratiques fondamentales à posséder lorsque l'on code.

{% note %}
Les différentes méthodes et mantra que l'on va voir sont issues de [l'*extreme programming* (XP)](https://fr.wikipedia.org/wiki/Extreme_programming), qui date des années 2000 mais dont on à l'impression qu'elle a été écrite hier (voire demain tellement elle est encore novatrice).
{% endnote %}

## Quel langage utiliser ?

Il existe de nombreux langages de programmation, allant de [l'assembleur](https://fr.wikipedia.org/wiki/Assembleur) compréhensible par les processeurs de nos ordinateurs au [python](https://fr.wikipedia.org/wiki/Python_(langage)) que tout le monde connaît, en passant par [le haskell](https://fr.wikipedia.org/wiki/Haskell), [le C](https://fr.wikipedia.org/wiki/C_(langage)) ou encore [le Rust](https://www.rust-lang.org/fr).

On trouve même des langages désignées pour être les plus simples possibles (appelés [turing tarpit](https://fr.wikipedia.org/wiki/Langage_de_programmation_exotique)) tout en étant aussi expressif que le python. Le plus célèbre d'entre eux est [le brainfuck](https://fr.wikipedia.org/wiki/Brainfuck).

{% info "**fun fact**" %}
On peut utiliser aussi certains jeu comme langage de programmation comme [factorio](https://www.factorio.com/) (l'algorithme de [tri quicksort](https://www.youtube.com/watch?v=ts5EKp9w4TU)), ou encore [minecraft](https://www.minecraft.net/) ([une calculatrice](https://www.youtube.com/watch?v=uGug-4xkw6M)).
{% endinfo %}

Tous ces langages sont ***équivalents*** : ce que l'on peut faire dans un langage peut être fait dans un autre (et réciproquement). **Mais** certains langage sont plus adaptés que d'autre pour faire certaines tâches.

Par exemple, si vous créez d'énormes programmes avec des milliers de lignes de codes, il vaut mieux utiliser un langage comme [le java](https://www.java.com/fr/) ou [le C#](https://docs.microsoft.com/fr-fr/dotnet/csharp/programming-guide/). Ou encore, si vous coder des applications web, on utilisera beaucoup [le javascript](https://developer.mozilla.org/fr/docs/Web/JavaScript).

Bref :

{% note %}
On utilise le langage qui est le plus adapté à notre problème.
{% endnote %}

Ne faites pas rentrer des carrés dans des ronds en utilisant un langage non adapté à votre problème. Vous allez perdre plus de temps qu'autre chose :

{% note %}
Un langage informatique n'est **pas** une langue. C'est facile à apprendre !
{% endnote %}

## Noms explicites et découpage fonctionnel

{% note "**Règle générale**" %}

- des noms de variables **explicites**
- on préférera de **petites fonctions/méthodes** avec un nommage explicite à de nombreuses lignes de code

{% endnote %}

Ceci permet de lire le code comme on lirait un texte, ce qui permet de rapidement comprendre ce qu'il fait, juste en le lisant. Les petites fonctions sont de plus facilement modifiables et testables.

Le découpage fonctionnel de votre code permet d'éviter la duplication de code, qui est un mal absolu en code. Si l'on copie/colle du code et qu'il y a un bug ou qu'on veut modifier le fonctionnement de celui-ci, il faudra se rappeler de tous les endroits où il a été dupliqué, ce qui est impossible ! De plus, cela rend votre code peu lisible, il bégaie.

<span id="DRY"></span>
{% note "**Coding mantra**" %}
[DRY](https://fr.wikipedia.org/wiki/Ne_vous_r%C3%A9p%C3%A9tez_pas) : *don't repeat yourself*.
{% endnote %}

Vous saurez que votre code est lisible lorsqu'il ne nécessitera **pas** de commentaires pour être compris. Ils sont en effet avantageusement remplacés par des noms de variables explicites et les noms de fonctions qui doivent expliquer ce qu'elles font.

{% note "**Coding mantra**" %}
[NO COMMENTS !](https://www.developpez.com/actu/150066/Programmation-quand-faut-il-commenter-son-code-Google-s-invite-dans-le-debat-et-montre-que-les-commentaires-peuvent-tres-souvent-etre-evites/)
{% endnote %}

En plus d'être inutile, les commentaires :

- **sont souvent des mensonges** : comme le commentaire n'est pas du code, lorsque l'on modifie le code on *oublie* de changer le commentaire. Au bout d'un moment le commentaire n'est donc plus en relation avec le code : au lieu d'aider à comprendre, il confuse : un commentaire est donc tôt ou tard un mensonge.
- **cachent la difficulté**. S'il y a plein de commentaires, on ne les lira plus. Un commentaire se doit d'être rare. S'il est là c'est que l'on n'a pas vraiment pu faire autrement. Vous n'en aurez pas besoin dans 99% des cas...

{% attention %}
**commentaires != documentation**
{% endattention %}

- Si votre code est destiné à être utilisé uniquement par vous ou votre équipe, on n'a pas besoin de le documenter. Son organisation et son écriture doit se suffire à lui-même.
- si votre code va être utilisé par des inconnus (lorsque vous créez [une bibliothèque](https://fr.wikipedia.org/wiki/Biblioth%C3%A8que_logicielle) par exemple), les fonctions publiques doivent être documentées. Un utilisateur doit pouvoir utiliser votre code sans effort et avoir à le lire pour le faire.

Lorsque l'on utilise [une API](https://fr.wikipedia.org/wiki/Interface_de_programmation), on a en effet jamais accès aux corps des méthodes, mais juste à leurs noms : on a besoin de savoir comment elles fonctionnent sans en connaître le corps :

{% note %}
Toutes les méthodes destinées à être utilisées par des clients/utilisateurs différents de l'équipe de développement doivent être documentées.
{% endnote %}

## Lisibilité

Un code est fait pour être relu et amélioré. On **doit** privilégier sa lecture à son écriture. Pour que votre équipe ou vous même puissiez le relire plus tard sans faire d'effort de compréhension.

{% note %}
Écrire du code n'est pas un concours d'érudition.
{% endnote %}

Si on a le choix entre écrire du code utilisant des subtilités algorithmiques ou du langage utilisé mais qui le rend plus difficile à comprendre sans gain réel en complexité on choisira **TOUJOURS** le code lisible ou du code plus basique mais clair.

{% note "**Coding mantra**" %}
[KISS](https://fr.wikipedia.org/wiki/Principe_KISS) : *keep it simple, stupid*.
{% endnote %}

Si le fond doit être simple, la forme du code est importante aussi. Il se doit d'être agréable à lire et homogène. L'équipe de développement doit se mettre d'accord sur [un coding style](https://fr.wikipedia.org/wiki/Style_de_programmation). Par défaut on utilise le standard du langage. En python, c'est la  [PEP8](https://www.python.org/dev/peps/pep-0008/)

{% note %}
Utilisez un style de programmation homogène pour faciliter la lecture de code. Si possible, automatisez ce processus avec un outil automatique de formatage de code.
{% endnote %}

## Efficacité

On ne doit jamais coder de choses inutiles : tout bout de code doit être utilisé au moment où il est écrit.

{% note %}
On ne codera jamais de fonctionnalités qui ne vont être utiles que plus tard.
{% endnote %}

Car *"plus tard"* le code ne sera plus le même et — le plus souvent — les besoins auront changés : votre fonctionnalités ne sera jamais utilisé... *"plus tard"* veut souvent dire *"jamais"*.
De plus, du code inutile contraint le développement : il est là, ne sert à rien, mais pas sa seule présence il empêche de modifier le code comme on veut.

En conséquence :

{% note %}
Tout code qui n'est plus/pas utile doit être immédiatement supprimé.
{% endnote %}

Le mieux étant encore de ne jamais l'écrire au départ :

<span id="YAGNI"></span>
{% note "**Coding mantra**" %}
[YAGNI](https://fr.wikipedia.org/wiki/YAGNI) : *You ain't gonna need it*.
{% endnote %}

## Tests

Pour s'assurer que notre code fait bien ce qu'il est sensé faire, on effectuera des ***tests***. C'est le pendant code de la preuve d'un algorithme.

Comme on passe son temps à modifier son code, il est nécessaire de conserver ses tests pour pouvoir les exécuter très souvent et vérifier qu'il continue de fonctionner.

Pour cela :

{% note %}
Lorsque l'on ajoute des fonctionnalités au code ou que l'on corrige un bug, on écrit un test qui vérifie la fonctionnalité ou qui montre que le bug n'existe pas/plus.

Ainsi, puisque les tests sont conservés, ce bug ne pourra plus jamais réapparaître et cette fonctionnalité ne pourra plus disparaître.
{% endnote %}

Une méthode très efficace de programmation consiste même à commencer par écrire le test, **avant** le code testé :

{% note "**Coding mantra**" %}
[TDD](https://artificials.ch/test-driven-development-mantra/) : *test driven development*.
{% endnote %}

Nous n'utiliserons pas ici le mantra TDD dans son intégralité : on se permettra d'écrire les tests après avoir codé la fonctionnalité et pas avant. Mais, l'expérience venant, faites l'essai de coder vos tests avant la fonction, cela permet d'utiliser sa fonction avant de la coder et change souvent la façon dont on voulait la coder initialement.

Les tests sont autant de cas d'utilisation de vos programmes qui montrent qu'il fonctionne et comment il fonctionne. Il permettent de montrer les différentes fonctionnalités de votre code :

{% note "**La fonctionnalité est plus importante que le code**" %}
Le code va changer, les fonctionnalités doivent rester.
{% endnote %}

Enfin, le code et ses tests doivent être fait par la **même personne** et au **même moment**. Il ne faut pas attendre d'avoir codé plusieurs fonctions avant de faire ses tests. Vous n'êtes en effet pas sûr que votre 1ère fonction codée fonctionne avant d'avoir fait des tests.

De là, il est possible qu'un bug dans cette première fonction affecte le code de votre seconde fonction... Et lorsque vous ferez enfin vos tests vous serez alors obligé de re-coder toutes vos fonctions ce qui ne serait pas arrivé si vous aviez testé toutes vos fonctions une par une et au moment de les coder.

## Structure d'un programme

Tout ce qu'on vient de voir structure un projet informatique en trois entités :

{% note %}
Un projet informatique comporte **toujours** 3 parties d'égales importances :

- le ***programme principal*** (aussi appelé **main**) qui est ce qui sera exécuté
- le ***code*** qui regroupe l'ensemble des fonctions utilisée par le programme principal
- les ***tests*** qui *certifient* que le code fonctionne.

{% endnote %}

Ces trois entités sont **toujours** codées en même temps : un code doit être testé pour être sur qu'il fonctionne et comme on ne fait pas de code inutile, il doit être utilisé.

Exemples :

- pour rajouter une fonctionnalité au programme principal, on ajoute du code qui doit lui-même être testé pour vérifier qu'il fonctionne.
- pour corriger un bug du programme principal, on modifie du code et on ajoute des tests qui montrent que le bug n'existe plus.
