---
layout: page
title:  "Selenium"
category: cours
tags: combat web
authors: 
  - "Jiang Yi Mei"
  - "Laurent Léo"
---

## User Stories et Tests Fonctionnels

Le concept de User Story rejoint celui d'expérience utilisateur.  En effet il s’agit de comment on imagine que l’utilisateur va utiliser le produit, quel est le chemin qu’il va parcourir, surtout quel est le chemin qu’on veut qu’il parcoure. Définir une user story permet également de définir comment sera utilisé le site qu’on va écrire. 

Pour tester notre code, on a déjà vu les [tests unitaires] qui permettent de vérifier que des petites portions du code fonctionnent correctement. 
Ici, on souhaite tester le comportement du site en fonction du parcours d'un utilisateur. 
On doit donc réaliser des tests fonctionnels: On veut observer le résultat d'une séquence d'opérations complexes.

Pour cela, on va utiliser [Selenium](https://www.selenium.dev), un outil qui permet d’automatiser un navigateur web. On peut l’utiliser pour simuler un utilisateur, et donc vérifier que le site fonctionne comme il devrait d’un point de vue utilisateur. 
C’est un outil très générique puisqu’il supporte de nombreux navigateurs, il est utilisable avec de nombreux langages également. 

## Installation de Selenium

Selenium est écrit en Java, avant de l’utiliser assurez-vous d’avoir Java installé sur votre machine. Vous pouvez le faire en passant par l’installer [sdkman](https://sdkman.io).

Pour bien prendre en main selenium, faisons quelques tests\
[Doc de Selenium](https://www.selenium.dev/documentation/en/).

## Le WebDriver



## Trouver un Élément Web

Pour trouver un élément sur une page web, on utilise `findElement`.

Cette fonction renvoie un objet WebElement qui représente un noeud de l'arbre DOM,
en prenant en argument un contexte de recherche.
Par exemple, la ligne suivante permet de trouver l'élément dont l'id est "introduction", 
et de stocker cet objet dans la variable intro :
~~~js
const intro = driver.findElement(By.id("introduction")); 
~~~

Ensuite, si on veut trouver un élément contenu dans l'objet intro (par exemple l'image d'id "img-intro"), on écrit :
~~~js
const imgIntro = intro.findElement(By.id("img-intro")); 
~~~

On peut rechercher un Élément en fonction de divers sélecteurs grâce à `By`. En voici quelques-uns:
~~~js
// dont le nom est "a" (un lien):
const element = driver.findElement(By.name("a"));
// dont l'id est "truc":
const element = driver.findElement(By.id("truc"));
// possédant a minima les attributs css "#machin" et "bidule":
const element = driver.findElement(By.css("#machin bidule"));
~~~

De manière générale, il est conseillé de rechercher des éléments par leur id unique s'il existe,
ou par leurs sélecteurs CSS.
Cela évite de parcourir l'arbre DOM avec plusieurs recherches, ce qui prend plus de temps.

On peut aussi rechercher un élément en fonction de sa position par rapport à un autre élément:
~~~js
// Trouve un bouton en dessous de intro
const intro = driver.findElement(By.id("introduction"));
const button = await driver.findElement(withTagName("button")
                                        .below("intro"));
~~~
On utilise `withTagName` qui remplace `By.name`.
On peut rechercher:
- au dessus avec `.above`
- en dessous avec `.below`
- à gauche avec `.toLeftOf`
- à droite avec `.toRightOf`
- à moins de 50px avec `.near`

On peut utiliser plusieurs de ces sélecteurs en même temps :

~~~js
const button = await driver.findElement(withTagName("button")
                                        .above(By.id("introduction"))
                                        .toRightOf(By.cssSelector("#menu")));
~~~

## Réaliser des actions sur la page





## Attendre la réponse du navigateur



## Quelques commandes utiles



## Petite recherche sur Google



## CheatSheet

