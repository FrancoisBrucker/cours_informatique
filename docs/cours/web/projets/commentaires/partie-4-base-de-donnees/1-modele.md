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
  message: {
    type: DataTypes.STRING,
    allowNull: false
  },
}, {
  // Other model options go here
});

```

On demande qu'un message soit 3 chaînes de caractères non vide. Notez qu'on a pas donné de clé primaire : dans ce cas sequelize en crée une qui s'appelle `id` pour nous.

## création de la base

Nous n'avons pour l'instant que créer le modèle, il n'existe pas encore dans la base. Comme notre modèle est en mémoire, on va faire en sorte de recréer la base en changeant tou sles modèles que nous avons défini (ici un seul). Ceci se fait avec la ligne :

```js
await sequelize.sync({ force: true });
```

Le mot clé `await` précise que l'on attend que la commande soit finie avant de passer à la ligne suivante. La commande est asynchrone par défaut, mais on ne veut pas commencer à faire des choses avec la base de donnée avant qu'elle ait été complètement créée.

On ne peut cependant pas utiliser `await` comme ça, il doit être dans une fonction de type `async` (asynchrone), ce que n'est pas notre programme par défaut. On utilise du coup le truc suivant :

```js
(async () => {
    await sequelize.sync({ force: true });
    // Code here
  })();
```

On exécute notre code dans une fonction asynchrone sans paramètre qui est exécutée juste après avoir été définie.

> Le javascript est formidable, non ?

## fichier de test

Avant d'incorporer la base de donnée dans le code du serveur, on va déjà l'utiliser dans un fichier séparé, histoire de voir si tout se passe comme prévu.

Créez un fichier *"db.test.js"* dans *"commentaires"* et on pourra y mettre le code suivant pour voir comment tout ça peut fonctionne :

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
    message: {
      type: DataTypes.STRING,
      allowNull: false
    },
  }, {
    // Other model options go here
  });
  
  (async () => {
    await sequelize.sync({ force: true });
    // Code here
  })();
```

En exécutant ce code on voit (en SQL, dialecte parlé par sqlite qui est notre base de donnée) ce que fait sequelize. Le résultat de la commande `node db.test.js` donne :

```text
Executing (default): DROP TABLE IF EXISTS `Users`;
Executing (default): DROP TABLE IF EXISTS `Users`;
Executing (default): CREATE TABLE IF NOT EXISTS `Users` (`id` INTEGER PRIMARY KEY AUTOINCREMENT, `pseudo` VARCHAR(255) NOT NULL, `titre` VARCHAR(255) NOT NULL, `message` VARCHAR(255) NOT NULL, `createdAt` DATETIME NOT NULL, `updatedAt` DATETIME NOT NULL);
Executing (default): PRAGMA INDEX_LIST(`Users`)
```

On supprime toute la base puis on recrée notre modèle `Message`.

## crud

Pour l'accès à nos données, on utilise le formalisme [CRUD](https://fr.wikipedia.org/wiki/CRUD), c'est à dire que l'on veut avoir des url qui nous permettent de :

* **C**reate : créer un message
* **R**ead : lire un message
* **U**pdate : mettre à jour un message
* **D**elete : supprimer un message

> Nous utiliserons l'id qui est ajouté par défaut à chaque message pour spécifier directement  un message.

Avant de créer les routes, concentrons nous sur les façons de faire ça en sequelize.

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

Le message est poussé en base. Son `id` est visible : `console.log(message.id)`. Si c'est le premier élément que vous créez, son `id` sera de 1, et si vous en créez d'autres, l'`id` va augmenter. C'est la clé primaire de notre modèle.

Testons ça en modifiant notre fonction `async` de `test.db.js` :

```js
(async () => {
    await sequelize.sync({ force: true });
    // Code here
    pseudo = "François"
    titre = "un coup de gueule"
    corps = "il faut permettre aux étudiants de de faire plus d'informatique !"

    message = await Message.create({
        pseudo: pseudo,
        titre: titre,
        message: corps
    })
    console.log(message.id)
    
    messages = await Message.findAll({});
    console.log(messages);
})();
```

On crée un message, on note son id puis on cherche tous les messages de la base et on les affiche (notez le `await` dans la dernière ligne pour être sur que o'n a tout chargé avant de l'afficher).

### read

> <https://sequelize.org/master/manual/model-querying-finders.html#-code-findbypk--code->

On va lire une instance en connaissant sa clé primaire.

```js
message = await Message.findByPk(1)
```

Si l'on donne une clé primaire inexistante, on récupère l'objet `null`.

### update

> <https://sequelize.org/master/manual/model-instances.html#updating-an-instance>

On met à jour un objet en connaissant sa clé primaire et les attributs à changer.

```js
message = await Message.findByPk(1);
message.titre = "un pavé dans la marre"

message.save()
```

### delete

> <https://sequelize.org/master/manual/model-instances.html#deleting-an-instance>

```js
message = await Message.findByPk(1);
message.titre = "un pavé dans la marre"

await message.destroy();
```

## requêtes

Nous allons aussi avoir besoin de 2 routes spéciales, pour la page **lire.html** :

* une route qui rend une liste de tous les messages
* une route qui rend une liste de tous les messages pour un pseudo donné.

### tous les messages

On a déjà utilisé cette requête, c'est `Message.findAll({}))`.

### les messages d'un pseudo

Il suffit de donner des contraintes à la requête `findAll` grâce un `where` sqlien :

```js
messages = await Message.findAll({
        where: {
            pseudo: "François"
        }
    })
console.log(messages)
```

### requêtes possible dans sequelize

Les requêtes possible dans sequelize sont très puissantes. Regardez du côté de la [documentation sur les requêtes basiques](https://sequelize.org/master/manual/model-querying-basics.html), c'est facile à utiliser et puissant.

Si vous êtes en mal de SQL, vous pouvez bien sur aussi utliser les [reqêtes SQL](https://sequelize.org/master/manual/raw-queries.html) standards.

## base de donnée en dur

> <https://sequelize.org/master/manual/getting-started.html#connecting-to-a-database>

Pour ne pas avoir une base de donnée en mémoire (ce qui est bien pour des tests par exemple, mais en prod on aimerait ne pas tout perdre à chaque fois qu'un relance le serveur).

Si l'on veut utiliser une base de données sqlite en dur on peut alors :

```js
path = require('path')

const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: path.join(__dirname, 'db.sqlite')
});
```

Si vous remplacez la ligne `await sequelize.sync({ force: true });` par `await sequelize.sync();`, la base est juste synchronisée (on ajoute les modèles inexistant) et non remise à plat. Ceci vous permet d'avoir une base qui va grandir au fil du temps.

## fichier

Le fichier *3commentaires/db.test.js"* ressemble à la fin de ces tests à ça :

```js
const { Sequelize, DataTypes } = require('sequelize');
// const sequelize = new Sequelize('sqlite::memory:');

path = require('path')

const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: path.join(__dirname, 'db.sqlite')
});

const Message = sequelize.define('User', {
    pseudo: {
        type: DataTypes.STRING,
        allowNull: false
    },
    titre: {
        type: DataTypes.STRING,
        allowNull: false
    },
    message: {
        type: DataTypes.STRING,
        allowNull: false
    },
}, {
    // Other model options go here
});

(async () => {
    // await sequelize.sync({ force: true });
    await sequelize.sync();
    
    // Code here
    pseudo = "François"
    titre = "un coup de gueule"
    corps = "il faut permettre aux étudiants de de faire plus d'informatique !"

    message = await Message.create({
        pseudo: pseudo,
        titre: titre,
        message: corps
    })
    console.log(message.id)

    console.log(await Message.findAll({}));
    console.log(await Message.findByPk(1));

    message = await Message.findByPk(1);
    message.titre = "un pavé dans la marre"

    message.save()

    console.log(await Message.findByPk(1));

    messages = await Message.findAll({
        where: {
            pseudo: "François"
        }
    })
    console.log(messages)

    console.log("------")
    console.log(messages)

})();
```
