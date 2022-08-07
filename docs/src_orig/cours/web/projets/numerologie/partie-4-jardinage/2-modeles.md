---
layout: page
title:  "Projet numérologie : partie 4 / modèles"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %}) / [partie 4]({% link cours/web/projets/numerologie/partie-4-jardinage/index.md %}) / [modèles]({% link cours/web/projets/numerologie/partie-4-jardinage/2-modeles.md %})
{.chemin}

Le principe qui nous a fait séparer nos routes nous fait également séparer les modèles.

## injection de dépendance

La différence par rapport aux routes est que l'on a besoin de la base de donnée (`sequelize`) pour définir le modèle. La solution élégant à ce problème est d'utiliser [l'njection de dépendance](https://fr.wikipedia.org/wiki/Injection_de_d%C3%A9pendances) : on va donner notre base à l'import du modèle.

Ceci peut se faire simplement en javascript en important une fonction et non plus des objets.

Avant de montrer le code des modèles, créons un dossier *"numerologie/models"* qui va contenir nos modèles.

### modèle Signification

Le modèle `Signification` est alors crée dans le fichier *"numerologie/models/signification.js"* :

```js
const { DataTypes } = require('sequelize');

module.exports = (sequelize) => {

    return sequelize.define('Signification', {
        message: {
            type: DataTypes.STRING,
            allowNull: false
        },
        nombre: {
            type: DataTypes.INTEGER,
            allowNull: false
        },
    }, {
        // Other model options go here
    });

}

```

Dans la définition du modèle, on ajuste besoin de l'objet `DataTypes` du module sequelize et non de la base de donnée.

Cette fonction exportée devra être utilisée dans le fichier `db.js` qui liera la base de donnée aux modèles.

### modèle Prénoms

Le modèle `Prenoms` est alors crée dans le fichier *"numerologie/models/prenoms.js"* :

```js
const { DataTypes } = require('sequelize');

module.exports = (sequelize) => {

    return sequelize.define('Prenoms', {
        prenom: {
            type: DataTypes.STRING,
            allowNull: false
        },
    }, {
        // Other model options go here
    });
    
}
```

## base de donnée

Les modèles crées vont être importé puis exécutés dans notre fichier *"numerologie/db.js"* remanié :

```js
const { Sequelize, DataTypes } = require('sequelize');
path = require('path')

const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: path.join(__dirname, 'db.sqlite')
});

signification = require("./models/signification")
prenoms = require("./models/prenoms")

module.exports = {
    sequelize: sequelize,
    model: {
        Signification: signification(sequelize),
        Prenoms: prenoms(sequelize),
    }
}
```

Voyez comment le modèle est tout d'abord chargé (`signification = require("./models/signification")`) puis exécuté à l'export (`Signification: signification(sequelize)`) en utilisant la base de donnée en injection de dépendance.
