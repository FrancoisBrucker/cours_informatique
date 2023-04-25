---
layout: layout/post.njk
title: "Projet numérologie / partie 1 : front / niveau 2 / code js"

authors:
    - "François Brucker"


eleventyNavigation:
  key: "Projet numérologie / partie 1 : front / niveau 2 / code js"
  parent: "Projet numérologie / partie 1 : front / niveau 2"
---

<!-- début résumé -->

Code de la *logique métier* du projet. L'idée est de montrer comment on peut progresser en codant nous même, un item en amenant un autre à coder.

<!-- fin résumé -->

## Todos initiaux

Il faut tout faire :

* [ ] associer un chiffre à un nom
* [ ] créer un champ texte dans un fichier html
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

## Choix de la première tâche

{% note %}
Quelle est la tâche la plus simple à réaliser dans nos todos ?
{% endnote %}

Le cœur du projet est d'associer un numéro à un nom, donc autant essayer de faire ça en javascript.

{% note %}
On modifie le fichier `numérologie/todos/todos.md`{.fichier} pour refléter le fait qu'on travaille sur cet item.
{% endnote %}

* [X] associer un chiffre à un nom
* [ ] créer un champ texte dans un fichier html
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

Bon c'est pas encore très détaillé. Comment faire ça ?

1. déjà un nom c'est une chaîne de caractère codée en utf-8
2. on peut prendre le numéro Unicode/utf8 de chaque caractère et les sommer
3. il faut un chiffre donc comment passer d'un nombre à un chiffre ?
4. on peut sommer les chiffre du nombre pour obtenir un autre nombre strictement plus petit ($10.x + y < x + y$) et recommencer la procédure si ce n'est pas un chiffre.

Ajoutons nos réflexions à la todo list (fichier `numérologie/todos/todos.md`{.fichier}) :

```
* [X] associer un chiffre à un nom
  * [ ] numéro Unicode/utf8 d'un caractère
  * [ ] sommer des numéro des caractères d'une chaîne de caractères
  * [ ] sommer les chiffre d'un nombre
  * [ ] sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)
* [ ] créer un champ texte dans un fichier html
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter
```

{% info %}
Au passage, vous avez vu comment on a mis des maths dans du markdown ? Lorsque vous transformerez le markdown en html, [Mathjax](https://www.mathjax.org/) rendra ces équations toutes jolies.
{% endinfo %}

Quel est l'item le plus simple à résoudre ? A mon avis c'est lui :

* [X] associer un chiffre à un nom
  * [X] numéro Unicode/utf8 d'un caractère
  * [ ] sommer des numéro des caractères d'une chaîne de caractères
  * [ ] sommer les chiffre d'un nombre
  * [ ] sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)
* [ ] créer un champ texte dans un fichier html
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

On va aller plus vite dans ce cours ensuite. Mais l(idée est toujours la suivante : dans votre listes de todos vous devez avoir un item qui vous semble le plus *facile* à résoudre. Si ce n'est pas le cas, c'est que vous items sont trop gros et qu'il faut les décomposer en unité plus fine.

{% note %}
Que signifie *le plus facile à résoudre* ? C'est un item dont l'implémentation ne nécessite qu'une seule chose à faire, et que cette chose à faire est simple.
{% endnote %}

## Tache 1 : Unicode d'un caractère

{% note %}
On utilise l'[implémentation du niveau 1](../../niveau-1/2-code_js#tache-1){.interne} pour associer un nombre à un caractère Unicode.
{% endnote %}

## Tache 2 : caractères et nombre

Ce qui nous permet de passer à l'item suivant :

* [X] associer un chiffre à un nom
  * [X] ~~numéro Unicode/utf8 d'un caractère~~
  * [X] sommer des numéro des caractères d'une chaîne de caractères
  * [ ] sommer les chiffre d'un nombre
  * [ ] sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)
* [ ] créer un champ texte dans un fichier html
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

{% note %}
Qu'on [implémente comme au niveau 1](../../niveau-1/2-code_js#tache-2){.interne}. Nos todos deviennent :
{% endnote %}

* [X] associer un chiffre à un nom
  * [X] ~~numéro Unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaîne de caractères~~
  * [ ] sommer les chiffre d'un nombre
  * [ ] sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)
* [ ] créer un champ texte dans un fichier html
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

On a bien progressé. La tâche qui semble la plus simple maintenant est de finaliser la partie consacrée à l'association d'un chiffre à un nom.

## Tache 3 : chiffres et nombre

Je choisis de faire :

* [X] associer un chiffre à un nom
  * [X] ~~numéro Unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaîne de caractères~~
  * [X] sommer les chiffre d'un nombre
  * [ ] sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)
* [ ] créer un champ texte dans un fichier html
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

{% note %}
Encore une fois on utilise l'[implémentation de niveau 1](../../niveau-1/2-code_js#tache-3){.interne}. Nous allons cependant modifier la façon dont on teste nos méthodes.
{% endnote %}

## Tache 4 : somme itérative

On peut terminer cette partie en faisant l'item :

* [X] associer un chiffre à un nom
  * [X] ~~numéro Unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaîne de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)
* [ ] créer un champ texte dans un fichier html
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

{% note %}
On procède [comme au niveau 1](../../niveau-1/2-code_js#tache-4){.interne}, en ajoutant les tests à notre tout nouveau fichier `numérologie/tests/tests_numérologie.js`{.fichier}.
{% endnote %}

## Todos finaux

* [X] associer un chiffre à un nom
  * [X] ~~numéro Unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaîne de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [ ] créer un champ texte dans un fichier html
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

La partie javascript semble terminée pour l'instant. On peut s'attaquer à ce qui semble le plus simple, la page web.
