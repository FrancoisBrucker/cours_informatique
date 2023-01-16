---
layout: layout/post.njk 
title:  "Projet commentaires : partie 4 / intégration"
category: cours
author: "François Brucker"
---

> [commentaires]({% link cours/web/projets/commentaires/index.md %}) / [partie 4]({% link cours/web/projets/commentaires/partie-4-base-de-donnees/index.md %}) / [intégration]({% link cours/web/projets/commentaires/partie-4-base-de-donnees/2-db-config.md %})
{.chemin}

On incorpore la base de donnée et les modèles sequelize dans notre serveur.

## intégration de la base de donnée

On pourrait mettre le code en vrac dans server.js, mais ce n'est pas vraiment une bonne pratique. On va créer dans notre projet plusieurs fichiers relatif à la base.

On va créer un module *"commentaires/db.js"* dont le but sera de rendre un objet permettant de gérer la base de donnée :

```js
const { Sequelize, DataTypes } = require('sequelize');
const sequelize = new Sequelize('sqlite::memory:');

module.exports = {
    sequeleize: sequelize 
}
```

Dans un projet node, si l'on importe plusieurs fois le même module, on ne lira le fichier que la prmière fois. La seconde fois, node ne renverra uniquement que le `module.exports`. On peut donc exécuter du code, ici faire le lien avec notre base de donnée sans soucis, il ne sera exécuté qu'une fois.

On peut maintenant ajouter l'import dans *"commentaires/server.js"* :

```js
// ...

db = require('./db')

// ...
```

> Notez que comme c'est un import à nous, le chemin est relatif (`./`).

## modèles

La base de données c'est bien, mais il manque tous les modèles que nous avons crées.

Pour cela, l'usage est de créer un dossier *"models"* où l'on stocke nos modèles. Donc créons un dossier *"commentaires/models"* et placez-y le fichier du model *"message.js"* :

```js
const { DataTypes } = require('sequelize');

module.exports = (sequelize) => {
    return sequelize.define('Message', {
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
}
```

La création du modèle nécessitant la base de données, il faut que l'on connaisse la base lorsque l'on crée le domèle. L'astuce ici est de rendre une fonction. Ce qui nous permettra d'importer notre modèle dans *"db.js"* en utilisant la base de données crée. De là, le fichier *"db.js"* :

```js
const { Sequelize, DataTypes } = require('sequelize');
const sequelize = new Sequelize('sqlite::memory:');

const message = require('./models/message')
const Message = message(sequelize)

module.exports = {
    sequelize: sequelize, 
    models: {
        Message: Message
    }
}
```

C'est technique s'appelle [injection de dépendances](https://www.freecodecamp.org/news/a-quick-intro-to-dependency-injection-what-it-is-and-when-to-use-it-7578c84fa88f/) : on donne ses dépendances à l'objet lors de l'exécution et c'est très très puissant pour découpler les dépendances entre objets.

> On aurait pu écrire les 2 lignes de l'injection de dépendances en une seule : `const Message = require('./models/message')(sequelize)`

Enfin, on joute une synchronisation de la base après avoir chargé nos modèles. Cette synchronisation n'est obligatoire que si la base ne connait pas le modèle chargé. Pour plus de sureté, on le l'exécuter tout le temps :

```js
const { Sequelize, DataTypes } = require('sequelize');
const sequelize = new Sequelize('sqlite::memory:');

const message = require('./models/message')
const Message = message(sequelize);

(async () => {
    // await sequelize.sync({ force: true });
    await sequelize.sync();
})()


module.exports = {
    sequelize: sequelize, 
    models: {
        Message: Message
    }
}
```

> Il faut mettre le `;` avant de commencer une instruction par une parenthèse, sinon javascript ne sait pas si c'est la suite de l'inscruction précédente ou une nouvelle instruction.

On a utilisé le truc de la fonction `async` pour attendre la fin d'une fonction asynchrone. C'est important ici car on **doit** fini la synchronisation de la base avant de finir l'importation.

Vous pouvez tester en remplaçant la fonction `async` par  le code suivant :

```js
(async () => {
    // await sequelize.sync({ force: true });
    await sequelize.sync();
    console.log("je suis là")
})()
```

>Si vous enlevez le mot `await`, le texte `"je suis là"` sera affiché avant le résultat de la fonction de synchronisation. Si à la place du `console.log` on avait tenté d'utiliser la base de données, on aurait eu une erreur.
{.attention}

## modèle de base de données

On a donc un module qui sera importé à chaque fois qu'on a besoin d'accéder notre base de données : le fichier *"commentaires/db.js"*. Ce fichier va inclure tous les modèles de notre base puis faire une synchronisation avec la base. Ceci ne sera fait qu'au premier import, lors des prochains import seule `module.exports` sera rendu, le reste du code ne sera même pas exécuté.

Au final, pour la suite de nos développements, on va utiliser une base de donnée sqlite, histoire de ne pas avoir à remettre des données à chaque fois que l'on relance le serveur (ce qui va arriver souvent en phase de développement...). On a alors le fichier *"commentaires/db.js"* suivant :

```js
const { Sequelize, DataTypes } = require('sequelize');
//const sequelize = new Sequelize('sqlite::memory:');

path = require('path')

const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: path.join(__dirname, 'db.sqlite')
});

const message = require('./models/message')
const Message = message(sequelize);

(async () => {
    // await sequelize.sync({ force: true });
    await sequelize.sync();
})()


module.exports = {
    sequelize: sequelize, 
    models: {
        Message: Message
    }
}
```
