---
layout: page
title:  "Projet numérologie : partie 1 / niveau 2 / intégration html et js"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %}) / [partie 1]({% link cours/web/projets/numerologie/partie-1-front/index.md %}) / [niveau 2]({% link cours/web/projets/numerologie/partie-1-front/niveau-2/index.md %}) / [html et css]({% link cours/web/projets/numerologie/partie-1-front/niveau-2/4-integration_html_js.md %})
{: .chemin}

On va lier le code javascript de la la [partie 2]({% link cours/web/projets/numerologie/partie-1-front/niveau-2/2-code_js.md %}) et le html/css de la [partie 3]({% link cours/web/projets/numerologie/partie-1-front/niveau-2/3-html_css.md %}).

## todos

* [X] associer un chiffre à un nom
  * [X] ~~numéro unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
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
  * [X] ~~numéro unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [X] ~~ajouter du style dans le html~~
* [X] ~~inclure une bibliothèque css~~
* [X] ~~police de caractère spéciale pour le chiffre~~
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [X] récupérer l'input en appuyant sur le `button`
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

## Tache 1 : cliquer sur le bouton

On procède comme pour le [niveau 1]({% link cours/web/projets/numerologie/partie-1-front/niveau-1/4-integration_html_js.md %}#tache-1).

* [X] associer un chiffre à un nom
  * [X] ~~numéro unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [X] ~~ajouter du style dans le html~~
* [X] ~~inclure une bibliothèque css~~
* [X] ~~police de caractère spéciale pour le chiffre~~
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [X] ~~récupérer l'input en appuyant sur le `button`~~
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

Que faire avec la valeur du champ `<input>` ? Ben lui associer le chiffre numérologique pardi. Sauf qu'on ne l'a pas mis dans notre todo liste.... Ajoutons le :

* [X] associer un chiffre à un nom
  * [X] ~~numéro unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [X] ~~ajouter du style dans le html~~
* [X] ~~inclure une bibliothèque css~~
* [X] ~~police de caractère spéciale pour le chiffre~~
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [X] ~~récupérer l'input en appuyant sur le `button`~~
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter
* [ ] utiliser le code numerologie.js dans le html

Puis occupons nous en, car c'est nécessaire à la suite.

## Tâche 2 : chargement et utilisation de fichier javascript {#tache-2}

* [X] associer un chiffre à un nom
  * [X] ~~numéro unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [X] ~~ajouter du style dans le html~~
* [X] ~~inclure une bibliothèque css~~
* [X] ~~police de caractère spéciale pour le chiffre~~
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [X] ~~récupérer l'input en appuyant sur le `button`~~
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter
* [X] utiliser le code numerologie.js dans le html

On procède comme pour le [niveau 1]({% link cours/web/projets/numerologie/partie-1-front/niveau-1/4-integration_html_js.md %}#tache-2).

## Tâche 3 : modification du html {#tache-3}

* [X] associer un chiffre à un nom
  * [X] ~~numéro unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [X] ~~ajouter du style dans le html~~
* [X] ~~inclure une bibliothèque css~~
* [X] ~~police de caractère spéciale pour le chiffre~~
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [X] ~~récupérer l'input en appuyant sur le `button`~~
* [X] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter
* [X] ~~utiliser le code numerologie.js dans le html~~

On procède comme pour le [niveau 1]({% link cours/web/projets/numerologie/partie-1-front/niveau-1/4-integration_html_js.md %}#tache-3).

## Tâche 3.5 : la touche entrée

Il ne nous reste plus que 2 items :

* [X] associer un chiffre à un nom
  * [X] ~~numéro unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [X] ~~ajouter du style dans le html~~
* [X] ~~inclure une bibliothèque css~~
* [X] ~~police de caractère spéciale pour le chiffre~~
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [X] ~~récupérer l'input en appuyant sur le `button`~~
* [X] ~~modifier l'arbre DOM avec du texte~~
* [ ] récupérer un info de l'url et la traiter
* [X] ~~utiliser le code numerologie.js dans le html~~

Le plus simple semble encore de gérer la touche entrée puisque l'autre item nécessite un serveur web. 

Avant de googler comment gérer le fait de taper sur une touche (c'est possible), regardons ce que ça donne sur notre page actuelle. Et là, miracle ! Ca marche tout seul. En voilà un item rondement géré :-)

* [X] associer un chiffre à un nom
  * [X] ~~numéro unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [X] ~~ajouter du style dans le html~~
* [X] ~~inclure une bibliothèque css~~
* [X] ~~police de caractère spéciale pour le chiffre~~
* [X] ~~récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée~~
* [X] ~~récupérer l'input en appuyant sur le `button`~~
* [X] ~~modifier l'arbre DOM avec du texte~~
* [ ] récupérer un info de l'url et la traiter
* [X] ~~utiliser le code numerologie.js dans le html~~

## todos finaux

On arrête notre session ici. La prochaine session sera consacrée au serveur, on recommencera une nouvelle todo liste, où l'on remettre notre item non fait. Pour l'instant on a : 

* [X] associer un chiffre à un nom
  * [X] ~~numéro unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [X] ~~ajouter du style dans le html~~
* [X] ~~inclure une bibliothèque css~~
* [X] ~~police de caractère spéciale pour le chiffre~~
* [X] ~~récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée~~
* [X] ~~récupérer l'input en appuyant sur le `button`~~
* [X] ~~modifier l'arbre DOM avec du texte~~
* [X] ~~utiliser le code numerologie.js dans le html~~
