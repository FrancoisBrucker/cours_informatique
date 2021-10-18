---
layout: page
title:  "Projet numérologie : partie 3 : intégration"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %}) / [partie 3]({% link cours/web/projets/numerologie/partie-3-donnees/index.md %}) / [intégration]({% link cours/web/projets/numerologie/partie-3-donnees/2-integration.md %})
{: .chemin}

Création de la base de donnée associée au projet

## base en lecture seule

On va commencer par créer une base de donnée en lecture pour associer à chaque chiffre sa signification (scientifique).

### modèle

Le modèle va être identique à notre modèle jouet de la partie précédente. Modifions *"numerologie/db.js"* pour qu'il corresponde à notre nouveau modèle :

```js
const { Sequelize, DataTypes } = require('sequelize');
path = require('path')

const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: path.join(__dirname, 'db.sqlite')
});

const Signification = sequelize.define('Signification', {
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

module.exports = {
    sequelize: sequelize,
    model: {
        Signification: Signification,
    }
}
```

### initialisation

On initialise la base dans le fichier *"numerologie/db-init.js"* :

```js
const db = require("./db")

async function initDB() {
    await db.sequelize.sync({force: true})
    
    await db.model.MonModele.create({
        message: "Une main de fer dans un gant de velours... Votre caractère bien trempé vous cause parfois du tort, mais pas question de vous adoucir : vous êtes comme vous êtes, que ça plaise ou non ! Au moins, vous avez le mérite de jouer cartes sur table. Vos amis savent qu'ils peuvent compter sur votre loyauté.",
        nombre: 1,
    })

    await db.model.MonModele.create({
        message: "Au premier abord, on vous juge froide, distante. Mais c'est mal vous connaître car sous votre carapace glaciale, vous êtes ultrasensible ! Le sarcasme et l'ironie vous protègent des déceptions... Combien de fois avez-vous accordé votre confiance à des gens qui ne la méritaient pas ?",
        nombre: 2,
    })

    await db.model.MonModele.create({
        message: "Vous avez l'âme d'une artiste ! Dessin, chant, danse... Vous vous épanouissez dans les activités créatives, et vous avez une imagination débordante.",
        nombre: 3,
    })

    await db.model.MonModele.create({
        message: "La spontanéité, ce n'est pas votre truc. Dans votre vie, tout doit être rangé, organisé, planifié, sinon c'est la panique ! Au travail, les responsabilités vous font peur : vous préférez vous mettre au service d'un supérieur plutôt que de prendre les commandes. Votre prudence naturelle vous pousse à ne pas vous aventurer en terrain inconnu...",
        nombre: 4,
    })

    await db.model.MonModele.create({
        message: "Le changement, l'imprévu, la nouveauté, vous adorez ! Ultra curieuse, vous êtes bien décidée à tout essayer, et les expériences extrêmes ne vous font pas peur.",
        nombre: 5,
    })

    await db.model.MonModele.create({
        message: "Vous attendez le prince charmant !",
        nombre: 6,
    })

    await db.model.MonModele.create({
        message: "Sous votre petit air mystérieux, vous cachez des capacités d'observation et d'analyse incroyables. D'ailleurs, lorsque vous leur donnez des conseils, vos proches les suivent à la lettre !",
        nombre: 7,
    })

    await db.model.MonModele.create({
        message: "Des projets, vous en avez toujours en pagaille ! Visionnaire, vous avez l'âme d'un chef : vous commandez, et les autres vous obéissent sans discuter. Et à l'arrivée, on reconnaît vos mérites.",
        nombre: 8,
    })

    await db.model.MonModele.create({
        message: "Vous rêvez d'un monde paisible et harmonieux... L'idéaliste de la famille, c'est vous ! Vous êtes vulnérable face au mensonge et à la trahison. Pourtant, lorsque les choses se corsent, vous êtes capable de vous démener pour résoudre les problèmes au plus vite. Pas question de rester passive face aux situations difficiles !",
        nombre: 9,
    })

}

initDB()
    .then(() => {
        console.log("base initalisée")
    })
```

## on jardine

### suppression des vieux fichiers

Nous n'avons plus besoin des vieux fichiers de tests : *"numerologie/ma_db_init.js"*, *"numerologie/ma_db_test.js"* et *"numerologie/ma_db_utilisation.js"*

### script init

On a coutume de mettre les différents scripts utiles dans la partie `script` du fichier *"package.json"*. Ajoutons donc un script d'initialisation :

```json
...

  "scripts": {
    "init": "node db-init.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },

...
```

On pourra exécuter ce script (juste une commande pour l'instant) en tapant la commande :

```shell
npm run init
```

Ajoutons également les commandesà faire dans le fichier *"numerologie/readme.md"* :

```markdown
# numerologie

Voyez la vie en base 10 en associant un chiffre à votre prénom.

## initialisation

`npm run init`
```

## utilisation de la base

Nous allons donner le message associé au numéro en plus du reste.

### côté serveur

Avec le numéro calculé, on cherche dans la base [e premier élément ayant ce numéro (méthode [findOne](https://sequelize.org/master/manual/model-querying-finders.html#-code-findone--code-)) et on le renvoie dans le json de résultat :

```js
// ...

const db = require("./db")

// ...

app.get(encodeURI('/prénom'), (req, res) => {
    console.log(req.query)
    prenom = req.query["valeur"]
    chiffre = numerologie.chiffre(prenom) 
    db.model.Signification.findOne({
        where: {
            nombre: chiffre
        }
    }).then((data) => {
        res.json({
            prénom: prenom,
            chiffre: chiffre, 
            message: data.message
        })
    })
})

// ...
```

Notez que l'accès en base est asynchrone, il faut donc attendre le résultat (avec le `then` des promise) avant de finir la requête.

### côté client

On va créer un div et afficher le message reçu. Fichier *"numerologie/static/index.html"* :

```html
<!-- ... -->

<div id="message"></div>

<script>
document.querySelector("#form-button").addEventListener("click", (event) => {
    prenom = document.querySelector("#form-input").value;
    if (prenom) {
        fetch('/prénom/?valeur=' + prenom)
            .then(response => response.json())
            .then(data => {
                document.querySelector("#chiffre").textContent = data.chiffre
                document.querySelector("#message").textContent = data.message
                console.log(data)
            })
    } else {
        document.querySelector("#chiffre").textContent = "?"
    }

    event.preventDefault();
})
</script>

<!-- ... -->

```

## base des correspondances recherchées

Ajoutons un autre modèle qui stocke les prénoms recherchés. On ne va cependant stocker qu'une seule fois le prénom.

### modèle prénom

On modifie *"numerologie/db.js"* pour inclure le nouveau modèle :

```js
const { Sequelize, DataTypes } = require('sequelize');
path = require('path')

const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: path.join(__dirname, 'db.sqlite')
});

const Signification = sequelize.define('Signification', {
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

const Prenoms = sequelize.define('Prenoms', {
    prenom: {
        type: DataTypes.STRING,
        allowNull: false
    },
}, {
    // Other model options go here
});

module.exports = {
    sequelize: sequelize,
    model: {
        Signification: Signification,
        Prenoms: Prenoms,
    }
}
```

Puis on recrée notre base de données avec la commande :

```shell
npm run init
```

### ajout dans la route

Il nous reste plus qu'à ajouter, si nécessaire, le prénom dans la base. On modifie la route dans *"numerologie/index.js"* :

```js
// ...

app.get(encodeURI('/prénom'), (req, res) => {
    console.log(req.query)
    prenom = req.query["valeur"]
    chiffre = numerologie.chiffre(prenom) 
    db.model.Prenoms.findOne({
        where: {
            prenom: prenom
        }
    }).then((data) => {
        if (data === null ) {
            db.model.Prenoms.create({
                prenom: prenom
            })
        }
        console.log(data)
    })
    db.model.Signification.findOne({
        where: {
            nombre: chiffre
        }
    }).then((data) => {
        res.json({
            prénom: prenom,
            chiffre: chiffre, 
            message: data.message
        })
    })
})

//...
```

On commence par tenter de chercher le prénom dans la base. S'il n'y est pas (le retour est `null`), on sauve le prénom.
Les deux recherches sont asynchrones et indépendantes.

> `==` et `===` [sont différents](https://developer.mozilla.org/fr/docs/Web/JavaScript/Equality_comparisons_and_sameness) en javascript.

## séparation des modèles et des routes

### modèles

> tbd : ajoute un dossier models
{: .note}

### api
