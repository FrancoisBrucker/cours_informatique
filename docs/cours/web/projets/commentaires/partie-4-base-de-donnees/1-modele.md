---
layout: page
title:  "Projet commentaires : partie 4 / modèle"
category: cours
author: "François Brucker"
---

> [commentaires]({% link cours/web/projets/commentaires/index.md %}) / [partie 4]({% link cours/web/projets/commentaires/partie-4-base-de-donnees/index.md %}) / [modèle]({% link cours/web/projets/commentaires/partie-4-base-de-donnees/1-modele.md %})
{: .chemin}

## sequelize

La vie est trop courte pour taper du SQL à la main. ON va utiliser [sequilize](https://sequelize.org/) qui va nous permettre de gérer tout le côté configuration de base et SQL pour nous.

En effet, selon la base, le dialecte SQL sera différent. Si l'on écrit nos requêtes à la main, il faudra toutes les changer lorsque l'on change de base, ce qui n'est pas humainement possible.

On va donc écrire nos requête dans le formalisme de sequilize qui va le traduire pour chaque base utilisée.

Commençons par installer la dépendance sequilize dans le projet, côté back. Tapez la commande suivante dans le dossier *"commentaires"* :

```shell
npm install --save sequelize
```

Notre base de donnée étant sqlite3, on installe également le driver :

```shell
npm install --save sqlite3
```

> Le driver sqlite3 est différent du logiciel sqlite3 que vous avez déjà installé (enfin, je crois).

Nous allons ici utiliser une base de donnée en mémoire. Elle sera remise à zéro à chaque fois que l'on relancera le serveur.

On initialise sequelize avec les deux lignes suivantes :

```js
const { Sequelize, DataTypes } = require('sequelize');
const sequelize = new Sequelize('sqlite::memory:');
```

La première récupère le module, la seconde crée le lien entre la base de donnée et nous.

> Si on avait eu une base de donnée physique ou un serveur de base de donnée, on aurait eu besoin de mettre nos login/mots de passe

## modèle

Nous avons envi de sauvegarder les commentaires. C'est à dire 3 chaînes de caractères. Les types possible de champ sont disponible [dans la documentation](https://sequelize.org/v5/manual/data-types.html). On va prendre les chaine les plus simple : `Sequelize.STRING` (tous nos champs devront avoir moins de 255 caractères).

Notre modèle de message est alors :

```js
const { Sequelize, DataTypes } = require('sequelize');
const sequelize = new Sequelize('sqlite::memory:');

const Message = sequelize.define('User', {
  pseudo: {
    type: DataTypes.STRING,
    allowNull: false
  },
  titre: {
    type: DataTypes.STRING,
    allowNull: false
  },
  message {
    type: DataTypes.STRING,
    allowNull: false
  },
}, {
  // Other model options go here
});

```

On demande qu'un message soit 3 chaînes de caractères non vide. Notez qu'on a pas donné de clé primaire : dans ce cas sequelize en crée une qui s'appelle `id` pour nous.

## création de la base

Nous n'avons pour l'instant que créer le modèle, il n'existe pas encore dans la base. Comme notre modèle est en mémoire, on va faire en sorte de recréer le modèle, même s'il existe déjà. Ceci se fait avec la ligne :

```js
await Message.sync({ force: true });
```

Le mot clé `await` précise que l'on attend que la commande soit finie avant de passer à la ligne suivante. La commande est asynchrone par défaut, mais on ne veut pas commencer à faire des choses avec la base de donnée avant qu'elle ait été complètement créée.

## fichier de test

Avant d'incorporer la base de donnée dans le code du serveur, on va déjà l'utiliser dans un fichier séparé, histoire de voir si tout se passe comme prévu.

Créez un fichier *"db.test.js"* 

## crud

Pour l'accès à nos données, on utilise le formalisme [CRUD](https://fr.wikipedia.org/wiki/CRUD), c'est à dire que l'on veut avoir des url qui nous permettent de :

* **C**reate : créer un message
* **R**ead : lire un message
* **U**pdate : mettre à jour un message
* **D**elete : supprimer un message

> Nous utiliserons l'id qui est ajouté par défaut à chaque message pour spécifier directement  un message.

### create

> <https://sequelize.org/master/manual/model-instances.html#creating-an-instance>

On veut créer une donnée avec sequelize en ayant le pseudo, le titre et le corps du message. On peut faire comme ça :

```sequelize
pseudo = "François"
titre = "un coup de gueule"
corps = "il faut permettre aux étudiants de de faire plus d'informatique !"

const message = await Message.create({
    pseudo: pseudo,
    titre: titre,
    message: corps
})
```

### read

### update

### delete


## routes spéciales

Nous allons aussi avoir besoin de 2 routes spéciales, pour la page **lire.html** :

* une route qui rend une liste de tous les messages
* une route qui rend une liste de tous les messages pour un pseudo donné.

