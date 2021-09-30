---
layout: page
title:  "Projet commentaires : partie 4 / intégration"
category: cours
author: "François Brucker"
---

> [commentaires]({% link cours/web/projets/commentaires/index.md %}) / [partie 4]({% link cours/web/projets/commentaires/partie-4-base-de-donnees/index.md %}) / [intégration]({% link cours/web/projets/commentaires/partie-4-base-de-donnees/2-db-config.md %})
{: .chemin}

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

Comme les require ne sont lu qu'une seule fois, on est assuré de n'avoir qu'une seule base de donnée, même si le module est importé plusieurs fois.

## modèles

La base de donnée c'est bien, mais il manque tous les modèles que nous avons crées.

Pour cela, l'usage est de créer un dossier *"models"* où l'on stoque nos modèles. Donc créez un dossier *"commentaires/models"* et placez-y le fichier du model *"message.js"* :

```js
modele.exports = {
    
}
```