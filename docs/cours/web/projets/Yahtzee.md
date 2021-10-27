---
layout: page
title:  "Yahtzee VueJS"
category: projets
tags: yahtzee postgresql express vuejs
authors:
- "Mickaël Rolland"
- "Nathanaël Soulat"
---

Ce projet s’inscrit dans le cours de Méthode de Développement de l’option 3A Digital.e. Le code source est sur [GitHub](https://github.com/nsoulat/Yahtzee) et est déployé sur ces plantes aromatiques de l'OVH : [fenouil](http://node.fenouil.ovh1.ec-m.fr/) et [girofle](http://node.girofle.ovh1.ec-m.fr/).

## Le Yahtzee

### Présentation du jeu

Le Yahtzee est un jeu de société traditionnel de hasard raisonné. 
Le but est d'enchaîner les combinaisons à l'aide de cinq dés pour remporter un maximum de points.

### Règles

Vous avez le droit à 3 lancers de dés à chaque tour. Après chaque lancer, vous pouvez garder certains dés et donc ne relancer que ceux que vous souhaitez. Vous n’êtes pas obligés de faire les 3 lancers.

Quand vous êtes satisfaits de vos lancers, ou si vous avez déjà effectué les 3 possibles, il faut choisir une des 13 combinaisons disponibles sur la grille, dans n’importe quel ordre. 
Cependant, à chaque fin de tour, vous êtes obligés d’en remplir une.

| Combinaisons   | Valeurs |
|---------|-------|
| Partie de 1 | total des faces de dés 1 |
| Partie de 2 | total des faces de dés 2 |
| Partie de 3 | total des faces de dés 3 |
| Partie de 4 | total des faces de dés 4 |
| Partie de 5 | total des faces de dés 5 |
| Partie de 6 | total des faces de dés 6 |
| Brelan (trois dés identiques) | Somme des cinq dés |
| Carré (quatre dés identiques) | Somme des cinq dés |
| Full (trois dés identiques et deux dés identiques) | 25 points |
| Petite suite (suite de 4 chiffres) | 30 points |
| Grande suite (suite de 5 chiffres) | 40 points |
| Yahtzee (cinq dés identiques) | 50 points |
| Chance | Somme des cinq dés |

Si la somme des parties est strictement supérieure à 62 points, vous obtenez un bonus de 35 points.

Le gagnant est celui qui a le plus de points.

### La particularité de notre Yahtzee

Il y a la table des meilleurs scores.

## Détails techniques

### Avec quoi il a été fait ?

![image](https://user-images.githubusercontent.com/75546258/139152006-0c3b1778-7c31-41c3-ac3d-1047c3541ee3.png)

Serveur backend avec Express (de NodeJS).
Frontend en VueJS (avec des fichiers JS en plus).
Sequelize en ORM et PostgreSQL pour la base de données.

> Si la construction du backend `Express + Sequelize + PostgreSQL` vous intéresse, vous pouvez aller voir le [tutoriel réalisé par nos soins]({% link cours/web/js/tuto_express_postregresql.md %}).

### Architecture

Nous avons fait le choix de séparer le frontend et le backend car le backend dispose d'une API REST et VueJS fonctionne très bien en tant que *single-page app*.

Voici l'architecture (simplifiée) de notre projet :

~~~ txt
/Yahtzee/
├── .github/              /* bots personnalisés GitHub
├── backend/
|  ├── config/            /* fichiers de configuration
|  ├── controllers/       /* controllers api
|  ├── models/            /* modèles en DB
|  ├── routes/            /* référencement des routes api
|  ├── .gitignore
|  ├── package.json
|  ├── package-lock.json  /* dépendances du backend
|  └── server.js          /* fichier source du backend
├── frontend/
|  ├── public/
|  ├── src/
|  |  ├── assets/         /* images et json
|  |  ├── classes/        /* class et objet JS
|  |  ├── components/     /* component Vue
|  |  ├── router/         /* référencement des routes du frontend
|  |  ├── services/       /* service pour appeler l'API du back
|  |  ├── views/          /* views Vue
|  |  ├── App.vue         /* view parente
|  |  └── main.js         /* fichier source du frontend
|  ├── .gitignore
|  ├── babel.config.js
|  ├── package.json
|  ├── package-lock.json  /* dépendances du frontend
|  └── vue.config.js
├── scripts/              /* scripts pour les npm run
├── .gitignore
├── package.json
└── README.md
~~~

### Dépendances principales front/back

Backend :

- express : framework très répandu pour la construction d'applications web.
- pg : dépendance permettant d'utiliser la base de données PostgreSQL.
- sequelize : ORM prenant en charge le dialecte PostgreSQL.

Frontend :

- vue : framework JavaScript pour la construction d'applications web monopages.
- vue-router : permet de gérer le routage sur notre application web monopage.
- moment : permet de gérer la conversion des formats de dates et d'heures.

### Installer le projet et lancer le projet

Tout en un :

~~~ shell
git clone git@github.com:nsoulat/Yahtzee.git
cd Yahtzee
npm run update
npm run build
npm run start
~~~

Explications :
Une fois que vous avez cloné le repo et êtes à la root du Yahtzee (dans le dossier Yahtzee) :

- `npm run update` permet d'installer les dépendances du backend et du frontend conformément au `package-lock.json` (la commande est équivalente à un `npm ci` dans les dossiers backend et frontend).
- `npm run build` permet de build le frontend et de placer ce build dans le dossier `frontend/dist`.
- `npm run start` permet de lancer le serveur backend. Il utilise le dossier `frontend/dist` comme dossier static.

> En cas de problèmes : se référer au [README du projet](https://github.com/nsoulat/Yahtzee#readme)
