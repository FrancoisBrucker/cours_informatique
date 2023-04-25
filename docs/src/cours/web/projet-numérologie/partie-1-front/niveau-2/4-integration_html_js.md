---
layout: layout/post.njk
title: "Projet numérologie / partie 1 : front / niveau 2 / intégration html & js"

authors:
    - "François Brucker"


eleventyNavigation:
  key: "Projet numérologie / partie 1 : front / niveau 2 / intégration html & js"
  parent: "Projet numérologie / partie 1 : front / niveau 2"
---

<!-- début résumé -->

Intégration Html et javascript.

<!-- fin résumé -->

## Todos

* [X] associer un chiffre à un nom
  * [X] ~~numéro Unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaîne de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [X] ~~ajouter du style dans le html~~
* [X] ~~inclure une bibliothèque css~~
* [X] ~~police de caractère spéciale pour le chiffre~~
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

Jouer avec la touche entrée, est peut-être un peu compliqué. On va donc ajouter un todo (qu'on va faire de suite) qui consistera à récupérer le texte de l'*input* lorsque l'on appuie sur le bouton.

* [X] associer un chiffre à un nom
  * [X] ~~numéro Unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaîne de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [X] ~~ajouter du style dans le html~~
* [X] ~~inclure une bibliothèque css~~
* [X] ~~police de caractère spéciale pour le chiffre~~
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [X] récupérer l'input en appuyant sur le `button`{.language-}
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

## Tache 1 : cliquer sur le bouton

{% note %}
On procède comme pour le [niveau 1](../../niveau-1/4-integration_html_js#tache-1){.interne}.
{% endnote %}

* [X] associer un chiffre à un nom
  * [X] ~~numéro Unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaîne de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [X] ~~ajouter du style dans le html~~
* [X] ~~inclure une bibliothèque css~~
* [X] ~~police de caractère spéciale pour le chiffre~~
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [X] ~~récupérer l'input en appuyant sur le `button`{.language-}~~
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

Que faire avec la valeur du champ `<input>`{.language-} ? Ben lui associer le chiffre numérologique pardi. Sauf qu'on ne l'a pas mis dans notre todo liste.... Ajoutons le :

* [X] associer un chiffre à un nom
  * [X] ~~numéro Unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaîne de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [X] ~~ajouter du style dans le html~~
* [X] ~~inclure une bibliothèque css~~
* [X] ~~police de caractère spéciale pour le chiffre~~
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [X] ~~récupérer l'input en appuyant sur le `button`{.language-}~~
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter
* [ ] utiliser le code `numérologie.js`{.fichier} dans le html

Puis occupons nous en, car c'est nécessaire à la suite.

## <span id="tache-2"></span> Tâche 2 : chargement et utilisation de fichier javascript

* [X] associer un chiffre à un nom
  * [X] ~~numéro Unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaîne de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [X] ~~ajouter du style dans le html~~
* [X] ~~inclure une bibliothèque css~~
* [X] ~~police de caractère spéciale pour le chiffre~~
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [X] ~~récupérer l'input en appuyant sur le `button`{.language-}~~
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter
* [X] utiliser le code `numérologie.js`{.fichier} dans le html

{% note %}
On procède comme pour le [niveau 1](../../niveau-1/4-integration_html_js#tache-2){.interne}.
{% endnote %}

## <span id="tache-3"></span> Tâche 3 : modification du html

* [X] associer un chiffre à un nom
  * [X] ~~numéro Unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaîne de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [X] ~~ajouter du style dans le html~~
* [X] ~~inclure une bibliothèque css~~
* [X] ~~police de caractère spéciale pour le chiffre~~
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [X] ~~récupérer l'input en appuyant sur le `button`{.language-}~~
* [X] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter
* [X] ~~utiliser le code `numérologie.js`{.fichier} dans le html~~

{% note %}
On procède comme pour le [niveau 1](../../niveau-1/4-integration_html_js#tache-3){.interne}.
{% endnote %}

## Tâche 3.5 : la touche entrée

Il ne nous reste plus que 2 items :

* [X] associer un chiffre à un nom
  * [X] ~~numéro Unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaîne de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [X] ~~ajouter du style dans le html~~
* [X] ~~inclure une bibliothèque css~~
* [X] ~~police de caractère spéciale pour le chiffre~~
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [X] ~~récupérer l'input en appuyant sur le `button`{.language-}~~
* [X] ~~modifier l'arbre DOM avec du texte~~
* [ ] récupérer un info de l'url et la traiter
* [X] ~~utiliser le code `numérologie.js`{.fichier} dans le html~~

Le plus simple semble encore de gérer la touche entrée puisque l'autre item nécessite un serveur web.

Avant de gougeuler comment gérer le fait de taper sur une touche (c'est possible), regardons ce que ça donne sur notre page actuelle. Et là, miracle ! Ca marche tout seul. En voilà un item rondement géré :-)

* [X] associer un chiffre à un nom
  * [X] ~~numéro Unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaîne de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [X] ~~ajouter du style dans le html~~
* [X] ~~inclure une bibliothèque css~~
* [X] ~~police de caractère spéciale pour le chiffre~~
* [X] ~~récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée~~
* [X] ~~récupérer l'input en appuyant sur le `button`{.language-}~~
* [X] ~~modifier l'arbre DOM avec du texte~~
* [ ] récupérer un info de l'url et la traiter
* [X] ~~utiliser le code `numérologie.js`{.fichier} dans le html~~

## Todos finaux

On arrête notre session ici. La prochaine session sera consacrée au serveur, on recommencera une nouvelle todo liste, où l'on remettre notre item non fait. Pour l'instant on a :

* [X] associer un chiffre à un nom
  * [X] ~~numéro Unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaîne de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [X] ~~ajouter du style dans le html~~
* [X] ~~inclure une bibliothèque css~~
* [X] ~~police de caractère spéciale pour le chiffre~~
* [X] ~~récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée~~
* [X] ~~récupérer l'input en appuyant sur le `button`{.language-}~~
* [X] ~~modifier l'arbre DOM avec du texte~~
* [X] ~~utiliser le code `numérologie.js`{.fichier} dans le html~~
