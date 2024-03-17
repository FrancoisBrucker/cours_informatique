---
layout: layout/post.njk

title: "Corrigé Test 3 : Programmation objet"
authors:
  - François Brucker
---

Ces questions ont pour bur de vous faire un peu réfléchir sur la prgrammation objet.

## Question 1

Répondez en une phrase maximum et le plus clairement possible.

### 1.1

> Quelle est la différence entre une fonction et une méthode ?

Le premier paramètre d'une méthode est l'objet à gauche du point.

### 1.2

> Quelle est la différence entre une composition et une agrégation ?

- une composition est un attribut crée par l'objet 
- une agrégation est un attribut dont l'objet n'a pas été créé par l'objet

### 1.3

> Qu'est-ce qu'un espace de nom ? À quoi cela sert-il ? Explicitez son usage dans l’appel d’une méthode.

Un espace de nom sert à associer des noms à des objets. Lors de l'appel d'une méthode (ou d'une fonction) un espace de nom est créé pour contenir les paramètres de la méthodes et ses variables. 

Un objet possède également un espace de nom utilisable grâce à la notation pointée : `objet.nom`{.language-} cherche `nom`{.language-} dans l'espace de nom de `objet`{.language-}. La notation pointée permet à une méthode d'accéder aux attributs de son premier paramètre `self`{.language-}, qui est l'objet à gauche du point.

## Question 2

Le but des questions suivantes est de vérifier que vous savez :

- écrire une description UML avec des attributs, des méthodes et leurs signatures
- avoir un tout cohérent : les attributs sont utilisés par les méthodes et leurs types correspondent
- chaque classe a un constructeur
- les liens entre les classes (composition et agrêgation) sont correctement déclarés


### 2.1

> Dessinez-moi un mouton en UML (il faudra qu'il ait un constructeur, au moins deux attributs et trois méthodes).

### 2.2

> Créez une classe boîte (en UML) pour ranger le Mouton dedans.  Quelle est la relation entre cette classe et la classe mouton ? On rappelle que cette boîte-là comporte trois trous pour que le mouton respire.
