---
layout: page
title:  "Projet numérologie : niveau 2/partie 1/html et css"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %})/[niveau 2]({% link cours/web/projets/numerologie/niveau-2/index.md %})/[partie 1]({% link cours/web/projets/numerologie/niveau-2/partie-1-front/index.md %})/[html et css]({% link cours/web/projets/numerologie/niveau-2/partie-1-front/3-html_css.md %})
{: .chemin}

## todos

Ce que je préfère lorsque je travaille avec des todos, c'est que lorsque je recommence une nouvelle session de travail, je peux me rappeler ce que j'ai fait en regardant le fichier de todos, ce qui me me permet d'être directement *dans le bain* :

* [X] associer un chiffre à un nom
  * [X] ~~numéro unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [ ] créer un champ texte dans un fichier html
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

> Lorsque l'on fini une une grande session de travail, il ne faut pas avoir d'item en court (ce qui est le cas ici). On peut commencer quelque chose de neuf en ayant un souvenir de ce qui a déjà été accompli.

## Tache 1 : site, première mouture

On va commencer par coder la structure du projet, c'est à dire faire l'html :

* [X] associer un chiffre à un nom
  * [X] ~~numéro unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] créer un champ texte dans un fichier html
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

Pour créer le fichier html, il faut s'appuyer sur les users stories pour être sur que notre site correspond bien aux attentes :

* un champ texte pour rentrer son prénom
* un chiffre associé au prénom

Avec ces directives on peut procéder comme [au niveau 1]({% link cours/web/projets/numerologie/niveau-1/partie-1-front/3-html_css.md %}#tache-1)

## ajout de todos

Comme c'est moche et qu'on est des esthètes, on va ajouter des choses au todo pour améliorer rendu. On va ajouter notre propre style pour les choses basiques (marges par exemples) et utiliser une bibliothèque css pour avoir une charte graphique homogène :

* [X] associer un chiffre à un nom
  * [X] ~~numéro unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [ ] ajouter du style dans le html
* [ ] inclure une bibliothèque css
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

> Il est tout à fait naturel d'ajouter/supprimer et modifier des todos de notre liste. Il est en effet **impossible** de tout prévoir quant à ce qu'il faudra coder ou les fonctionnalités qu'il faut ajouter. Avoir un *cahier des charges* exhaustif est impossible en début de projet.

## Tache 2 : style personnel

* [X] associer un chiffre à un nom
  * [X] ~~numéro unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [X] ajouter du style dans le html
* [ ] inclure une bibliothèque css
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

On va procéder comme [au niveau 1]({% link cours/web/projets/numerologie/niveau-1/partie-1-front/3-html_css.md %}#tache-2)

## Tache 3 : bibliothèque css

* [X] associer un chiffre à un nom
  * [X] ~~numéro unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [X] ~~ajouter du style dans le html~~
* [X] inclure une bibliothèque css
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

On va procéder comme [au niveau 1]({% link cours/web/projets/numerologie/niveau-1/partie-1-front/3-html_css.md %}#tache-3).

## Tache 3.5 : mais que fait la police ?

Notre user story dit que la police de caractère du chiffre doit être *rigolote*. Ajoutons un item à notre todo list et occupons nous en de suite :

* [X] associer un chiffre à un nom
  * [X] ~~numéro unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [X] ~~ajouter du style dans le html~~
* [X] ~~inclure une bibliothèque css~~
* [X] police de caractère spéciale pour le chiffre
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

Si on est pas riche à millions pour acheter une font propriétaire, choisir une fonte spéciale peut se faire facilement grâce à : <https://fonts.google.com/>.

Cela fonctionne de façon assez finaude. Une fois la font choisie et ses styles choisis, google nous donne un lien à mettre dans notre balise head. Ici :

```html
<link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet">
```

Ce lien télécharge la font et ses styles. On peut **ensuite** les utiliser dans nos css. Par exemple en changeant la police des paragraphes dans le fichier *"numerologie/main.css"* :

```css
/* ...  */

p {
    font-size: 100px;
    font-family: 'Lobster', cursive;
}

/* ... */
```

> Remarquez comme la marque des [commentaires en css](https://developer.mozilla.org/fr/docs/Web/CSS/Comments) est différentes de ceux en javascript. UN peut de patience, nous verrons comment sont les commentaires html dans la prochaine partie...

## todos finaux

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

Tout est prêt pour combiner le javascript et le html.
