---
layout: layout/post.njk 
title:  "Utiliser une base de données PostgreSQL avec Sequelize et NodeJS"
category: tutorial
tags: tuto postgresql sequelize nodejs données
authors:
- "Mickaël Rolland"
- "Nathanaël Soulat"
---

## Présentation de Sequelize

Sequelize est un [ORM](https://stackoverflow.com/questions/1279613/what-is-an-orm-how-does-it-work-and-how-should-i-use-one) conçu pour les applications NodeJS utilisant PostgreSQL, MySQL, MariaDB, SQLite ou Microsoft SQL Server.

L'avantage d'utiliser un ORM est d'éviter d'avoir à écrire des requêtes SQL natives, ce qui se présenterait sous la forme de

~~~ js
myDB.execute("SELECT id, stats, nom FROM players");
~~~

et qui aurait l'inconvénient d'être du code non-scalable. En effet, si jamais le modèle correspondant à players venait à changer ("nom" devient "name" par exemple), il faudrait manuellement changer toutes les requêtes où on utilisait "nom".

Utiliser un ORM permet de remédier à ça. C'est l'ORM lui-même qui va se charger de transcrire les requêtes SQL.

## Ajouter sa propre DB PostgreSQL

Nous allons dans un premier temps installer PostgreSQL sur notre machine (le tuto a été réalisé avec un PC sous Windows, libre à vous d'ajouter des variantes pour Linux et MacOS).
Puis nous ferons une simple API liée à une ressource nommée ``Player``.
Ensuite, nous verrons comment mettre en fonctionnement ce code sur l'OVH en utilisant la base de données PostgreSQL de ce dernier (l'OVH dispose déjà d'une base de données PostgreSQL donc il n'y a pas besoin de la créer).

Pour ceux utilisant Windows, vous pouvez installer [l'assistant d'installation de PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads). Celui-ci vous permettra d'installer directement **PostgreSQL Server**, **pgAdmin 4** (interface graphique de monitoring), et **Command Line Tools**.

Sinon vous pouvez suivre le [tutoriel officiel](https://www.postgresql.org/docs/current/tutorial-install.html) pour installer PostgreSQL et si tous les requirements semblent bon, vous pouvez installer PostgreSQL en commençant par [télécharger le fichier source](https://www.postgresql.org/download/) (en suivant les indications de PostgreSQL).

Lors de ces installations, retenez bien votre mot de passe et l'utilisateur pour se connecter à votre base de données PostgreSQL !

Après avoir installé PostgreSQL Server et pgAdmin 4, créons une Database dans notre PostgreSQL.
Pour cela, ouvrez pgAdmin 4, entrez votre mot de passe choisi précédemment.

Vous devriez avoir PostgreSQL 14 dans Servers (cf ci-dessous).
![image](https://user-images.githubusercontent.com/75546258/138589692-1fdf857c-32e2-4dc1-9c41-743af733a5a0.png)

Dans `PostgreSQL 14`, il y a normalement `Database` qui contient une base de données nommée `postgres`. Nous allons en créer une autre, pour s'entrainer. Faites un click droit sur `Database` puis `Create` puis `Database...`.

Il reste simplement à nommer notre base de données. Laissons `postgres` comme `Owner` (c'est le user par défaut et celui que vous utilisez actuellement *normalement*).

![image](https://user-images.githubusercontent.com/75546258/138589821-e96aba23-ef40-47b2-9e4d-3b97e476666b.png)

Cliquez sur `Save` et voilà votre base de données est créée !

Dans votre Database puis `Schemas`, vous pouvez trouver les `Tables`. Il n'y en a pour le moment aucune. Nous laisserons l'ORM les créer pour nous par la suite!
![image](https://user-images.githubusercontent.com/75546258/138589922-a38c4ced-71b2-481e-80fb-5c783a0029aa.png)

## Setup

Avant de commencer cette partie du tutoriel, assurez-vous d'avoir bien installé `express`.

Installation des modules utiles dans ton invite de commande préférée :

~~~ bash
npm install sequelize pg pg-hstore --save
~~~

> `pg` pour PostgreSQL et `pg-hstore` pour convertir les données dans le format hstore de PostgreSQL.

## Adapter son server Backend

Ici, nous séparons le front-end et le back-end, donc pas de HTML/CSS dans ce tutoriel, notre back-end ne renverra que du JSON. C'est au front-end d'appeler les routes du back-end pour récupérer le JSON et d'afficher comme souhaité toutes les informations obtenues.

> A la fin, votre dossier d'application devra ressembler à ça:

~~~ txt
C:\Users\Moi\Tuto\src
├── config
|  ├── .gitignore
|  ├── config.json
|  ├── config.model.json
|  └── db.config.js
├── controllers
|  └── player.controller.js
├── models
|  ├── index.js
|  └── player.model.js
├── node_modules
├── package-lock.json
├── package.json
├── README.md
├── routes
|  └── player.routes.js
└── server.js
~~~

## Configurer PostgreSQL et Sequelize

Créons un dossier `config` dans lequel on va mettre des fichiers de configuration. Dans ce dossier, créons un fichier `config.json`. Celui-ci est propre à l'utilisateur, c'est-à-dire qu'il ne faut pas le *push* sur GitHub, puisqu'il contient des configurations spécifiques à l'ordinateur utilisé.
Mais pour garder une cohérence entre tous les `config.json` des différents utilisateurs (par exemple ma machine perso, l'ovh, etc...) on va aussi mettre un fichier `config.model.json` qui contiendra des "fausses" valeurs (ou par défaut). Ce fichier sera alors à *push*, ainsi, chaque utilisateur devra copier ce ``config.model.json`` lors du setup de l'application sur sa machine, en remplaçant les fausses valeurs par celles correspondant à son propre ordinateur. Il devra enregistrer ce fichier en tant que ``config.json``.

Ainsi dans notre ``config.model.json`` on va mettre :

~~~ js
{
  "DATABASE": {
    "DB": "myDB",
    "USER": "user",
    "PASSWORD": "password"
  },
  "SERVER": {
    "HOST": "localhost",
    "PORT": 8080
  }
}
~~~

Et dans votre `config.json` vous mettez la même chose mais avec les bonnes valeurs (*ie* le nom de la database que vous avez créée précédement, votre *user* et *password* qui vont avec, ainsi que le hostname que vous souhaitez (vous pouvez laisser `localhost` ou mettre `127.0.0.1`) et le port souhaité).

Voici à quoi ressemble mon `config.json`:

~~~ js
{
  "DATABASE": {
    "DB": "tutoPlayer",
    "USER": "postgres",
    "PASSWORD": "LEAK"
  },
  "SERVER": {
    "HOST": "localhost",
    "PORT": 8080
  }
}
~~~

Ajoutez un ``.gitignore`` dans le dossier `Config` et mettez-y `config.json` pour ne pas *commit* votre fichier de config perso. C'est important de ne pas **leak** vos identifiants de connexion !

Toujours dans votre dossier config, vous allez ajouter un fichier
`db.config.js` qui contient les lignes ci-dessous :

~~~ js
const DBCONFIG = require("./config.json").DATABASE;

module.exports = {
    user: DBCONFIG.USER,
    password: DBCONFIG.PASSWORD,
    DB: DBCONFIG.DB,
    dialect: "postgres"
};
~~~

``user``, ``password``, ``DB`` et ``dialect`` sont requis pour créer la connexion avec la base de données PostgreSQL.

Créons un dossier `models` qui contiendra les modèles correspondant aux tables contenues dans notre base de données.

Commençons par ajouter le fichier `index.js` dans ce dossier ``models`` :

~~~ js
const dbConfig = require("../config/db.config.js");

const Sequelize = require("sequelize");
const sequelize = new Sequelize(
    dbConfig.DB,
    dbConfig.USER,
    dbConfig.PASSWORD,
    {
      dialect: dbConfig.dialect,
      operatorsAliases: 0 // 0 for false
    });

const db = {};

db.Sequelize = Sequelize;
db.sequelize = sequelize;

module.exports = db;
~~~

Ce fichier utilise les configurations déclarées dans notre fichier ``db.config.js``. Pour en savoir plus sur la configuration de Sequelize voir [ici](https://sequelize.org/master/class/lib/sequelize.js~Sequelize.html#instance-constructor-constructor).

Il ne reste plus qu'à utiliser ce module en ajoutant les lignes suivantes dans le ``server.js`` (ce fichier est parfois appelé ``index.js``) qui se trouve à la root de notre application :

~~~ js
const db = require("./models");
db.sequelize.sync();
~~~

Cette dernière ligne permet de lancer la synchronisation avec la DB lors du lancement du serveur.

Profitez-en pour récupérer les valeurs de votre configuration perso pour le hostname et le port. Voici à quoi ressemble mon ``server.js`` à ce moment du tuto :

~~~ js
const express = require("express");

const app = express()

const serverConfig = require("./config/config.json").SERVER;
const HOSTNAME = serverConfig.HOST;
const PORT = serverConfig.PORT;

const db = require("./models");
db.sequelize.sync();

app.use(function (req, res, next) {
    date = new Date(Date.now())
    console.log('Time:', date.toLocaleDateString(), date.toLocaleTimeString(), "; url :", req.url);
    next(); // sans cette ligne on ne pourra pas poursuivre.
})

// simple route
app.get("/", (req, res) => {
    res.statusCode = 200;
    res.json({
        status: 200,
        message: "Welcome to the backend."
    });
});

app.use(function (req, res) {
    console.log("et c'est le 404 : " + req.url);

    res.statusCode = 404;
    res.setHeader('Content-Type', 'application/json');

    res.json({
        status: 404,
        message: "Request not found"
    })
})

app.listen(PORT, HOSTNAME, () => {
    console.log(`Server is running at http://${HOSTNAME}:${PORT}.`);
});
~~~

Vous pourrez remarquer que j'ai un peu pris de l'avance et que mon serveur renvoie des JSON plutôt que du HTML.

## Ajouter un modèle

Pour le moment, notre database est vide.
Ajoutons dans le dossier ``models`` un fichier ``player.model.js`` contenant ceci :

~~~ js
module.exports = (sequelize, Sequelize) => {
  const Player = sequelize.define("player", {
    name: {
      type: Sequelize.STRING
    },
    birthDate: {
      type: Sequelize.DATEONLY
    },
    isPremium: {
      type: Sequelize.BOOLEAN
    }
  });

  return Player;
};
~~~

En plus des colonnes `name`, `birthDate` et `isPremium`, les colonnes `id`, `createdAt` et `updatedAt` sont générées automatiquement dans notre base de données.

Afin que Sequelize prenne en compte ce modèle, on ajoute cette ligne dans `models/index.js` juste après la déclaration de `db.Sequelize` et `db.sequelize` :

~~~ js
db.players = require("./player.model.js")(sequelize, Sequelize);
~~~

Cela permet à Sequelize d'ajouter la table des Players dans la base de données (dès qu'on lance le serveur, Sequelize va vérifier si la table des Players existe, si ce n'est pas le cas, elle va la créer). Voilà comment notre ORM nous permet simplement de créer des tables SQL !

## Les fonctions CRUD

L'avantage avec Sequelize c'est qu'il n'y a pas besoin d'écrire les requêtes SQL, c'est lui qui s'en charge.

Notre objet ``Player`` possède par défaut déjà les méthodes suivantes :

- ``Player.create(object)`` où ``object`` est un JSON/dictionnaire avec les colonnes en clés.
- ``Player.findByPk(id)`` pour récuper un Player par son Id
- ``Player.findAll()`` pour récuperer tous les Players
- ``Player.update(data, where: {id: id})`` pour mettre à jour un Player ayant un certain Id
- ``Player.destroy(where: {id: id})`` pour supprimer un Player ayant un certain Id
- ``Player.destroy(where: {})`` pour supprimer tous les Players
- ``Player.findAll({ where: { isPremium: ...} })`` pour récupérer les Players suivant certains critères.

Ces méthodes seront utilisées dans le Controller.

## Faire des POST

Avant de créer le Controller, on va adapter notre ``server.js``.

Comme expliqué [ici](https://stackoverflow.com/questions/23259168/what-are-express-json-and-express-urlencoded), `express` a des *Middlewares* (des méthodes appelées lors de la réception d'une requête, et avant la réponse à la requête, qui permettent notamment des vérifications de connexion, de sécurité, etc...) afin que notre serveur back-end soit configuré pour recevoir du JSON. Il faut ajouter cette ligne dans le ``server.js`` (juste après ``const app = express()`` par exemple) :

~~~ js
// parse requests of content-type - application/json
app.use(express.json());

// parse requests of content-type - application/x-www-form-urlencoded
app.use(express.urlencoded({ extended: true }));
~~~

La deuxième commande nous permet de configurer la réception de content-type pour le type *x-www-form-urlencoded* ce qui correspond aux requêtes avec des list de paire *name/value* dans l'url.

> Par exemple si on souhaite récupérer les livres en anglais de genre science : ``GET https://exemple.com/api/livres/langue=anglais&genre=science``. Ici les paires *name/value* sont *langue/anglais* et *genre/science*.

## Le Controller

Créons un dossier ``controllers`` qui contiendra le fichier ``player.controller.js`` défini ci-après :

~~~ js
const db = require("../models");
const Player = db.players;
const Op = db.Sequelize.Op;

// Creation
exports.create = (req, res) => {
  // Validate request
  if (!req.body.title) {
    res.status(400).send({
      message: "Content can not be empty!"
    });
    return;
  }

  // Créer un Player (les colonnes id, createdAt et updatedAt sont gérées automatiquement)
  const player = {
    name: req.body.name,
    birthDate: req.body.birthDate,
    isPremium: req.body.isPremium ? req.body.isPremium : false
  };

  // Save Player in the database
  Player.create(player)
    .then(data => {
      res.send(data);
    })
    .catch(err => {
      res.status(500).send({
        message:
          err.message || "Some error occurred while creating the Player."
      });
    });
};

// Recherche de tous les Players (ou ceux qui un 'name' particulier)
exports.findAll = (req, res) => {
  const name = req.query.name;
  var condition = name ? { name: { [Op.iLike]: `%${name}%` } } : null;

  Player.findAll({ where: condition })
    .then(data => {
      res.send(data);
    })
    .catch(err => {
      res.status(500).send({
        message:
          err.message || "Some error occurred while retrieving players."
      });
    });
};

// Recherche du Player par Id
exports.findOne = (req, res) => {
  const id = req.params.id;

  Player.findByPk(id)
    .then(data => {
      if (data) {
        res.send(data);
      } else {
        res.status(404).send({
          message: `Cannot find Player with id=${id}.`
        });
      }
    })
    .catch(err => {
      res.status(500).send({
        message: "Error retrieving Player with id=" + id
      });
    });
};

// Mise à jour d'un Player
exports.update = (req, res) => {
  const id = req.params.id;

  Player.update(req.body, {
    where: { id: id }
  })
    .then(num => {
      if (num == 1) {
        res.send({
          message: "Player was updated successfully."
        });
      } else {
        res.send({
          message: `Cannot update Player with id=${id}. Maybe Player was not found or req.body is empty!`
        });
      }
    })
    .catch(err => {
      res.status(500).send({
        message: "Error updating Player with id=" + id
      });
    });
};

// Supprimer un Player
exports.delete = (req, res) => {
  const id = req.params.id;

  Player.destroy({
    where: { id: id }
  })
    .then(num => {
      if (num == 1) {
        res.send({
          message: "Player was deleted successfully!"
        });
      } else {
        res.send({
          message: `Cannot delete Player with id=${id}. Maybe Player was not found!`
        });
      }
    })
    .catch(err => {
      res.status(500).send({
        message: "Could not delete Player with id=" + id
      });
    });
};

// Suppression de tous les Players
exports.deleteAll = (req, res) => {
  Player.destroy({
    where: {},
    truncate: false
  })
    .then(nums => {
      res.send({ message: `${nums} Players were deleted successfully!` });
    })
    .catch(err => {
      res.status(500).send({
        message:
          err.message || "Some error occurred while removing all players."
      });
    });
};

// Rechercher selon certaines conditions
exports.findAllPremium = (req, res) => {
  Player.findAll({ where: { isPremium: true } })
    .then(data => {
      res.send(data);
    })
    .catch(err => {
      res.status(500).send({
        message:
          err.message || "Some error occurred while retrieving players."
      });
    });
};
~~~

Ici le Controller ne permet pas de récupérer les requêtes de content-type ``application/x-www-form-urlencoded`` mais vous pouvez vous amuser à le faire !

## Les routes

Maintenant que le Controller est défini, il suffit de définir les différentes routes (endpoints) pour accéder aux fonctions du Controller.

Créons un dossier ``routes`` contenant le fichier ``player.routes.js`` défini ci-après :

~~~ js
module.exports = app => {
  const players = require("../controllers/players.controller.js");

  var router = require("express").Router();

  // Créer un nouveau Player
  router.post("/", players.create);

  // Récupère tous les Players
  router.get("/", players.findAll);

  // Récupère tous les Players premium
  router.get("/premium", players.findAllPremium);

  // Récupère un certain Player
  router.get("/:id", players.findOne);

  // Met à jour un certain Player
  router.put("/:id", players.update);

  // Supprime un player d'un certain Id
  router.delete("/:id", players.delete);

  // Supprime tous les Players
  router.delete("/", players.deleteAll);

  app.use('/api/players', router);
};
~~~

On vient de définir les routes suivantes :

- ``/api/players``: GET, POST, DELETE
- ``/api/players/:id`` : GET, PUT, DELETE
- ``/api/players/premium`` : GET

Il reste à ajouter ces routes dans le ``server.js``. Pour ce faire, ajoutons cette ligne juste avant le `app.listen()` :

~~~ js
require("./routes/player.routes")(app);
~~~

## La fin (et le début)

Votre projet devrait ressembler à ça:

~~~ txt
C:\Users\Moi\Tuto\src
├── config
|  ├── config.json
|  ├── config.model.json
|  └── db.config.js
├── controllers
|  └── player.controller.js
├── models
|  ├── index.js
|  └── player.model.js
├── node_modules
├── package-lock.json
├── package.json
├── README.md
├── routes
|  └── player.routes.js
└── server.js
~~~

C'est le moment du test !
Lancer le serveur avec `node server.js`.

En utilisant Postman (ou Insomnia, ou l'inspecteur de votre navigateur si vous être très à l'aise avec), vous pouvez alors tester les GET/POST/DELETE définis précédemment et vérifier (au moyen des GET ou en allant regarder directement dans la base de données PostgreSQL) si ça a bien fonctionné !

## Sur l'OVH

Connectez-vous à votre plante aromatique via ssh.

Mettez votre code sur l'OVH  dans votre dossier ``node`` (en utilisant ``scp`` ou par un ``git clone`` si vous avez votre code sur GitHub).

Et faites un ``npm ci`` dans votre dossier où se trouve le `package-lock.json`.

Allez dans le dossier parent du dossier ``node``, vous devriez y trouver un fichier nommé ``database_readme.txt``. Ouvrez-le (`cat database_readme.txt`), retenez le nom du `user` (ça devrait être votre plante aromatique) et copiez le mot de passe. Ces identifiants de connexion vous permettent de vous connecter à la base de données (du PostgreSQL de l'OVH), ayant comme nom votre plante aromatique (au lieu de `tutoPlayer`, ce sera par exemple `romarin`).

Il vous reste juste à modifier votre fichier config.json (ou config.model.json qu'il vous faut renommer en config.json) en y mettant ces valeurs pour `USER`, ``DB`` (votre plante aromatique aussi) et `PASSWORD`. Vous pouvez faire par exemple (en ayant préalablement copié le password et en vous plaçant dans le dossier config) :

~~~ bash
cp config.model.json config.json
nano config.json
~~~

> ``cp fichier_source fichier_dest`` permet de créer une copie d'un fichier source (la copie aura pour nom fichier_dest).

Et si maintenant par curiosité vous souhaitez naviguer au sein de cette mystérieuse base de données PostgreSQL de l'OVH voici comment faire:

Où que vous soyez, tapez cette ligne de commande:

~~~ bash
psql
~~~

Cela vous permet d'accéder au shell de PostgreSQL. Si vous avez un `maPlante=>` à la place de l'habituel `maPlante@ovh1:~/node` c'est que vous êtes bien entrés dans le shell psql. Toutes les commandes suivantes seront réalisées au sein du shell psql (écrivez les commandes à la suite de  ``votrePlante=>``).
On peut afficher toutes les databases existantes sur l'ovh avec:

~~~ bash
\l
~~~

Cela vous ouvre un gros tableau dans vim. Il devrait y avoir la votre (celle qui était désignée par votre plante dans `database_readme.txt`). Pour sortir de ce tableau (qui est ouvert dans Vim) tapez `q` ou `:q`.
Connectons nous à notre database en question (remplacez `maPlante` par votre USER) :

~~~ bash
\c maPlante
~~~

Cela vous affiche un message comme quoi vous êtes bien connectés à la base en question.
Maintenant que vous êtes connectés à votre base de données, vous pouvez afficher toutes vos tables :

~~~ bash
\dt
~~~

Et même réaliser des requêtes SQL comme (si vous avez une table nommée `players`) :

~~~ SQL
SELECT * FROM players;
~~~

> Attention, ne pas oublier le point-virgule !

Et finalement pour quitter psql:

~~~ bash
\q
~~~

### Liens utiles

- [Tutoriel original](https://www.bezkoder.com/node-express-sequelize-postgresql/#Setup_Express_web_server)
- [Utiliser psql sur Linux pour parcourir la base de données PostgreSQL](https://www.postgresql.org/docs/9.2/app-psql.html)
