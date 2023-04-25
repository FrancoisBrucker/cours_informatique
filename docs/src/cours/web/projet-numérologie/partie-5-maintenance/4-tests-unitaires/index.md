---
layout: layout/post.njk

title: "Projet numérologie : partie 5 / tests unitaires"

eleventyNavigation:
  key: "Projet numérologie : partie 5 / tests unitaires"
  parent: "Projet numérologie / partie 5 maintenance"
---

<!-- début résumé -->

Nous allons ajouter des tests unitaires à notre projet.

<!-- fin résumé -->

## Plan

Nous allons voir plusieurs aspects des tests :

1. [tests js avec jest](./js-jest){.interne}
2. [routes](./tests-routes){.interne}
3. [test de bases de données](./tests-db){.interne}

## Motivation

{% note %}
Un projet sans test est un projet qui ne fonctionne pas.
{% endnote %}

Lorsque l'on écrit un programme, on a l'habitude de vérifier qu'il fonctionne et lorsque l'on fait du web, on lance un navigateur pour vérifier visuellement que c'est *ok*. Voir, on vous l'a certainement répété, on met des commentaires pour *expliquer* le code.

Cette pratique est inefficace, voir dangereuse. Et ce pour plusieurs raisons :

* elle est longue à mettre en place : il faut penser quoi tester, vérifier visuellement que le test passe ou rate, et créer des petits programmes pour tester une fonctionnalité ou naviguer dans l'application jusqu'à trouver l'endroit que l'on veut tester
* on ne test pas tout : à chaque modification on ne teste que ce qu'on vient juste de coder et on oublie que notre nouveau code peut *casser* du code déjà existant.
* on écrit des mensonges : les commentaires sont écrit une fois puis on a la flemme de les mettre à jour lorsque l'on modifie le code. Ils deviennent donc des mensonges.

La règle d'airain en développement et dans la vie est que l'on ne va pas faire ce qui long et chiant. On ne peut donc maintenir ces pratiques, puisque tôt ou tard on va l'abandonner et ne plus trop tester notre code.

En revanche, on trouvera facilement des excuses pour expliquer pourquoi on ne teste pas :

{% note "**aucune de ces excuses ne sont valables**" %}
 <https://softwareengineering.stackexchange.com/questions/322256/time-difference-between-developing-with-unit-tests-vs-no-tests>
{% endnote %}

On doit donc :

* garder les tests que l'on écrit pour pouvoir les relancer
* supprimer les commentaires et :
  * bien nommer ses variables : elles doivent être explicite (`compteur`{.language-} plutôt que `i`{.language-} par exemple)
  * faire de toutes petites fonctions : on doit pouvoir lire votre code comme une histoire
* chaque tests doit :
  * automatiquement nous dire s'il rate et pourquoi
  * passer rapidement s'il réussi

Enfin, une fois qu'on a mis tout ça en place nos test doivent suivre la règle [FIRST](<https://medium.com/@chapuyj/5-principes-pour-guider-l-ecriture-des-tests-unitaires-be25cda2652>) pour être maintenable et aider au code :

* rapides : on doit pouvoir exécuter tous les tests rapidement
* isolé : on ne doit pas chaîner les tests, si un test dépend d'un autre si l'un rate on ne sais pas si c'est la faute de l'autre ou pas
* répétable : chaque test doit donner la même réponse à chaque fois qu'on le lance (**attentions** aux tests de bases de données par exemple : on fait une base de test)
* indépendant : chaque test teste une chose. (corollaire : Une chose ne doit pas être testé 2 fois)
* rapide : on doit pouvoir écrire un test rapidement et à tout moment

## Test unitaires

Il existe plusieurs types de tests, chacun répondant à une problématique donnée. Les tests unitaires sont des tests qui vérifient (en isolation) le bon fonctionnement d'une méthode, d'un algorithme. Ils sont écrits par le développeur de la méthode lui-même leur but initial est de vérifier que la méthode donne bien ce qu'il faut, et il faut faire autant de test que nécessaire pour se persuader que la fonction méthode

### Que tester

Il n'y a pas de bonne réponse à : quoi tester ? Et quand s'arrêter ? Il faut faire juste assez de test pour se persuader que ce qu'on a écrit est correct

### Quand tester

Juste Après avoir écrit sa fonction/méthode ! Voir même on l'écrit juste avant de coder si on suit le [TDD](https://fr.wikipedia.org/wiki/Test_driven_development) (ce qui est bien et vous fera énormément progresser !)

Si on attend trop longtemps :

* on ne se rappelle plus ce qu'on a codé
* on a pu introduire d'autres bug à d'autres endroits du code qui fond que le test de la méthode rate
* il est extrêmement difficile d'ajouter des tests à un programme déjà écrit il y a trop de dépendance et on à vraiment l'impression que cela ne finira jamais.
