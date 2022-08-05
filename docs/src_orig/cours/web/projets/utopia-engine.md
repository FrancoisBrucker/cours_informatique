---
layout: page
title:  "Projet MD2 - Utopia Engine"
category: Projets
tags: projet utopia engine
author:
- "François Jiang"
---

Ce projet s'inscrit dans le cours de *Méthode de Développement* de l'option 3A **Digital.e**. Le code source est sur [GitHub](https://github.com/MCF-ECM/utopia-engine-node) et est déployé sur [ovh1](http://node.melisse.ovh1.ec-m.fr/).

## Présentation du projet
### Histoire
![Utopia Engine](https://cf.geekdo-images.com/HTsjNQHQQMf029lmvlOFqA__itemrep/img/BX4Bcn68QCWJHaEIrCG5mTioiCE=/fit-in/246x300/filters:strip_icc()/pic1827127.jpg)

Vous jouez le rôle d'un vieil artificier nommé Isodoros qui tente de reconstruire l'*Utopia Engine*, un appareil légendaire datant d'un passé lointain et peut-être le seul espoir d'éviter la fin du monde qui approche rapidement. Vous devez récupérer les six pièces de la machine dans six régions dangereuses et assembler l'*Utopia Engine* avant la fin du monde. Le jeu utilise une mécanique de dés simple pour simuler la recherche dans les régions sauvages, l'activation et l'assemblage d'artefacts puissants, et le combat avec les armes des artefacts.

*Résumé traduit depuis [BoardGameGeek](https://boardgamegeek.com/boardgame/75223/utopia-engine).*

### Dépendences
Dépendences [Node.js](https://nodejs.org/fr) :
* [Express](https://expressjs.com/fr/) (version 4.17.1) : *Express* est un *framework* permettant de construire simplement un server *Node.js*.

Dépendences [React](https://fr.reactjs.org/) :
* [React](https://fr.reactjs.org/) (version 17.0.2) : *React* est une bibliothèque *JavaScript* pour créer des interfaces utilisateurs. Grâce à un riche écosystème de bibliothèques dédiées, React peut être utilisée comme un puissant *framework frontend*, comme [Vue.js](https://fr.vuejs.org/).
* [React Router Dom](https://www.npmjs.com/package/react-router-dom) (version 5.3.0) : *React Router Dom* est une bibliothèque *JavaScript* pour la gestion des routes sur les projets *React*.
* [Redux](https://redux.js.org/) (version 4.1.1) : *Redux* est une bibliothèque *JavaScript* pour générer les états (variables globales) d'applications *front*.

### Installer le projet
Pour installer le projet, il faut :
* cloner le projet
~~~ shell
$ git clone --recurse-submodules https://github.com/MCF-ECM/utopia-engine-node
~~~
>L'option *--recurse-submodules* permet de cloner avec les sous-modules.

* installer les dépendences (pour le server *Node.js* à la racine et la partie *React* dans le dossier react) :
~~~ shell
$ npm install
~~~

### Lancer le projet
Pour lancer le projet en local, il faut :
* build le projet *React* avec la commande (dans le dossier react) :
~~~ shell
$ npm build
~~~
> Build un projet *React* permet d'obtenir un dossier avec le projet sous forme d'un site statique.

* lancer le server *Node.js* avec la commande (à la racine):
~~~ shell
$ npm start
~~~

## Mécanique de jeu
### Recherche des Artéfacts
Pour partir à la recherche des artéfacts composant l'*Utopia Engine*, il suffit de cliquer sur les pins présent sur la carte (à gauche sur la page d'acceuil).

Une recherche se déroule de la façon suivant :
* lancer deux dés;
* affecter les valeurs des dés dans le tableau;
* soustraire à la ligne du haut celle du bas.

Le but est d'obtenir le plus petit nombre positif. Le résultat de la recherche dépend de ce nombre et est présenté dans le tabeau ci-dessous.

| Valeur de la différence|  Résultat de la recherche      |
| :--------------------: |:-----------------------------: |
| 0     				 | un artéfact activé         	  |
| 1 à 10       			 | un artéfact inactivé           |
| 10 à 99     			 | un composant        			  |
| 100 à 555 ou -555 à -1 | une rencontre avec un monstre  |

### Combats
Les combats se font contre des monstres. Les monstres ont un niveau dépendant du résulat de la recherche. La correspondance se retrouve dans le tableau ci-dessous.

| Valeur de la différence  		   | Niveau du monstre   | Dégat du monstre    | Fuite du monstre    |
| :------------------------------: |:------------------: |:------------------: |:------------------: |
| 100 à 199 ou -1 à -100  		   | 1        	  		 | 1 				   | 5 ou 6 			 |
| 200 à 299 ou -101 à -200 		   | 2           		 | 1 				   | 6					 |
| 300 à 399 ou -201 à -300		   | 3       			 | 1 ou 2 			   | 6					 |
| 400 à 499 ou -301 à -400		   | 4 					 | 1 à 3 			   | 6					 |
| 500 à 555 ou -401 à -555 		   | 5  				 | 1 à 4 			   | 6					 |

Un tour se déroule avec le lancer de deux dés. Si un des dés se trouve dans la plage de *Dégat du monstre*, alors un point de vie est perdu. Si un des dés se trouve dans la plage de *Fuite du monstre*, alors le monstre fuit. En cas de dégat et de fuite, le monstre réaliser le dégat avant sa fuite.

Si les points de vie tombent à zéro, alors le joueur s'évanouit et le monstre part. Le joueur se repose alors pour regagner ses points de vie.
Si les points de vie deviennent négatives, alors le joueur meurt et la partie est perdu.

### Activations des Artéfacts
Le but du jeu à ce stade étant d'activé les six artéfacts formant l'*Utopia Engine*, il faut activer les artéfacts inactifs. Pour se faire, depuis l'acceuil, il suffit de cliquer sur les artéfacts inactifs pour se rendre sur la page d'activation des artéfacts.

L'activation d'un artéfact nécessite quatres points de charge. Pour obtenir des points de charge, il faut lancer les deux dés et les affecter de telle sorte que la différence d'une cellule supérieure avec celle juste en dessous.
* Si cette différence est 5 alors deux points de charge est obtenu.
* Si cette différence est 4 alors un point de charge est obtenu.
* Si cette différence est null, alors les cellules correspondantes se vident.
* Si cette différence est négative un point de vie est perdu.