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
