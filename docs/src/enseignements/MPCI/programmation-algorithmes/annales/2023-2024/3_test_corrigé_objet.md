---
layout: layout/post.njk

title: "Corrigé Test 3 : Programmation objet"
authors:
  - François Brucker
---

Ces questions ont pour but de vous faire un peu réfléchir sur la programmation objet.

## Barème

Une note sur 5, un point par question.

{% note "**Objectif du test**" %}

En 15 minutes il était possible de répondre aux 5 questions. L'objectif est donc d'avoir 5 pour tout le monde.
{% endnote %}

La ventilation des notes est :

|note/4   | [0, 2.5[   | [2.5, 3]  | ]3, 4]     | ]4, 5[    | 5  |
|note/20  | [0, 10[    | [10, 12]  | [13, 16]   | [17, 19]| | 20 |
|---------|------------|-----------|------------|-----------|----|
|nombre   |  6         |  12        |  16       |  7        | 4  |
|rang min | 39         | 27         | 11        | 5         | 1  |

- moyenne : 13.49/20 (3.37/4)
- écart-type : 4.26/20 (1.06/4)
- médiane : 14/20 (3.5/4)

## Bilan

Encore une fois je suis globalement content de vous (attention, je vais commencer à m'y habituer :)). Je suis aussi content de moi puisque ma correction correspond à peut prêt aux votre.

J'ai mis en commentaire de votre récapitulatif les 2 notes que vous avez eu avec la correction par vos camarades, mais votre note correspond à la mienne. Notez que dans la très grande majorité des cas, la deuxième correction correspond au niveau réel de votre copie et est souvent 1/4 de point inférieure à ma propre notation.

## Question 1

Répondez en une phrase maximum et le plus clairement possible.

### 1.1

> Quelle est la différence entre une fonction et une méthode ?

1. Création : une méthode est définie dans une classe.
2. Appel : le premier paramètre d'une méthode est l'objet à gauche du point.


### 1.2

> Quelle est la différence entre une composition et une agrégation ?

- une composition est un attribut crée par l'objet 
- une agrégation est un attribut dont l'objet n'a pas été créé par l'objet

### 1.3

> Qu'est-ce qu'un espace de nom ? À quoi cela sert-il ? Explicitez son usage dans l’appel d’une méthode.

Un espace de nom sert à associer des noms à des objets. Lors de l'appel d'une méthode (ou d'une fonction) un espace de nom est créé pour contenir les paramètres de la méthodes et ses variables. 

En programmation objet les espaces de noms courants sont :

- l'espace de nom de la classe qui contient tout ce qui est défini dans le bloc de la classe, c'est à dire essentiellement les méthodes
- l'espace de nom de chaque objet utilisable grâce à la notation pointée et qui permet de stocker les noms de ses attributs.

Lorsqu'un nom n'est pas trouvé dans l'espace de nom de l'objet, il est cherché dans l'espace de nom de la classe.

## Question 2

Le but des questions suivantes est de vérifier que vous savez :

- écrire une description UML avec des attributs, des méthodes et leurs signatures
- avoir un tout cohérent : les attributs sont utilisés par les méthodes et leurs types correspondent
- chaque classe a un constructeur
- les liens entre les classes (composition et agrégation) sont correctement déclarés


### 2.1

> Dessinez-moi un mouton en UML (il faudra qu'il ait un constructeur, au moins deux attributs et trois méthodes).

Il faut qu'il y ait :

- un diagramme UML correct avec le nom en haut, puis les attributs et enfin des méthodes
- un constructeur
- un ou plusieurs attributs (cohérents)
- une ou plusieurs méthodes

### 2.2

> Créez une classe boîte (en UML) pour ranger le Mouton dedans.  Quelle est la relation entre cette classe et la classe mouton ? On rappelle que cette boîte-là comporte trois trous pour que le mouton respire.

- Il faut que les 3 trous soient présent sous la forme d'un attribut et qu'ils ne soient pas un paramètre du constructeur
- on doit pouvoir faire rentrer/sortir un mouton de la boîte.
- le lien entre la classe Mouton et Boîte doit être de l'agrégation


