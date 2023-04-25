---
layout: layout/post.njk
title: "Projet numérologie / partie 1 : front / niveau 2 / html & css"

authors:
    - "François Brucker"


eleventyNavigation:
  key: "Projet numérologie / partie 1 : front / niveau 2 / html & css"
  parent: "Projet numérologie / partie 1 : front / niveau 2"
---

<!-- début résumé -->

Html et css

<!-- fin résumé -->

## Todos

Ce que je préfère lorsque je travaille avec des todos, c'est que lorsque je recommence une nouvelle session de travail, je peux me rappeler ce que j'ai fait en regardant le fichier de todos, ce qui me me permet d'être directement *dans le bain* :

* [X] associer un chiffre à un nom
  * [X] ~~numéro Unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaîne de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [ ] créer un champ texte dans un fichier html
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

{% info %}
Lorsque l'on fini une une grande session de travail, il ne faut pas avoir d'item en court (ce qui est le cas ici). On peut commencer quelque chose de neuf en ayant un souvenir de ce qui a déjà été accompli.
{% endinfo %}

## Tache 1 : site, première mouture

On va commencer par coder la structure du projet, c'est à dire faire l'html :

* [X] associer un chiffre à un nom
  * [X] ~~numéro Unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaîne de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] créer un champ texte dans un fichier html
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

Pour créer le fichier html, il faut s'appuyer sur les users stories pour être sur que notre site correspond bien aux attentes :

* un champ texte pour rentrer son prénom
* un chiffre associé au prénom

{% note %}
Avec ces directives on peut procéder comme [au niveau 1](../../niveau-1/3-html_css#tache-1){.interne}
{% endnote %}

## Ajout de todos

Comme c'est moche et qu'on est des esthètes, on va ajouter des choses au todo pour améliorer rendu. On va ajouter notre propre style pour les choses basiques (marges par exemples) et utiliser une bibliothèque css pour avoir une charte graphique homogène :

* [X] associer un chiffre à un nom
  * [X] ~~numéro Unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaîne de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [ ] ajouter du style dans le html
* [ ] inclure une bibliothèque css
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

{% note %}
Il est tout à fait naturel d'ajouter/supprimer et modifier des todos de notre liste. Il est en effet **impossible** de tout prévoir quant à ce qu'il faudra coder ou les fonctionnalités qu'il faut ajouter. Avoir un *cahier des charges* exhaustif est impossible en début de projet.
{% endnote %}

## Tache 2 : style personnel

* [X] associer un chiffre à un nom
  * [X] ~~numéro Unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaîne de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [X] ajouter du style dans le html
* [ ] inclure une bibliothèque css
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

{% note %}
On va procéder comme [au niveau 1](../../niveau-1/3-html_css#tache-2){.interne}
{% endnote %}

## Tache 3 : bibliothèque css

* [X] associer un chiffre à un nom
  * [X] ~~numéro Unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaîne de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [X] ~~ajouter du style dans le html~~
* [X] inclure une bibliothèque css
* [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
* [ ] modifier l'arbre DOM avec du texte
* [ ] récupérer un info de l'url et la traiter

{% note %}
On va procéder comme [au niveau 1](../../niveau-1/3-html_css#tache-3){.interne}.
{% endnote %}

## Tache 3.5 : mais que fait la police ?

Notre user story dit que la police de caractère du chiffre doit être *rigolote*. Ajoutons un item à notre todo list et occupons nous en de suite :

* [X] associer un chiffre à un nom
  * [X] ~~numéro Unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaîne de caractères~~
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

Ce lien télécharge la font et ses styles. On peut **ensuite** les utiliser dans nos css. Par exemple en changeant la police des paragraphes dans le fichier `numérologie/main.css`{.fichier} :

```css
/* ...  */

p {
    font-size: 100px;
    font-family: 'Lobster', cursive;
}

/* ... */
```

{% info %}
Remarquez comme la marque des [commentaires en css](https://developer.mozilla.org/fr/docs/Web/CSS/Comments) est différentes de ceux en javascript. UN peut de patience, nous verrons comment sont les commentaires html dans la prochaine partie...
{% endinfo %}

## Todos finaux

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

Tout est prêt pour combiner le javascript et le html.
