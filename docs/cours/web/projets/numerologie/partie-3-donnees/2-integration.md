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
    
    await db.model.Signification.create({
        message: "Une main de fer dans un gant de velours... Votre caractère bien trempé vous cause parfois du tort, mais pas question de vous adoucir : vous êtes comme vous êtes, que ça plaise ou non ! Au moins, vous avez le mérite de jouer cartes sur table. Vos amis savent qu'ils peuvent compter sur votre loyauté.",
        nombre: 1,
    })

    await db.model.Signification.create({
        message: "Au premier abord, on vous juge froide, distante. Mais c'est mal vous connaître car sous votre carapace glaciale, vous êtes ultrasensible ! Le sarcasme et l'ironie vous protègent des déceptions... Combien de fois avez-vous accordé votre confiance à des gens qui ne la méritaient pas ?",
        nombre: 2,
    })

    await db.model.Signification.create({
        message: "Vous avez l'âme d'une artiste ! Dessin, chant, danse... Vous vous épanouissez dans les activités créatives, et vous avez une imagination débordante.",
        nombre: 3,
    })

    await db.model.Signification.create({
        message: "La spontanéité, ce n'est pas votre truc. Dans votre vie, tout doit être rangé, organisé, planifié, sinon c'est la panique ! Au travail, les responsabilités vous font peur : vous préférez vous mettre au service d'un supérieur plutôt que de prendre les commandes. Votre prudence naturelle vous pousse à ne pas vous aventurer en terrain inconnu...",
        nombre: 4,
    })

    await db.model.Signification.create({
        message: "Le changement, l'imprévu, la nouveauté, vous adorez ! Ultra curieuse, vous êtes bien décidée à tout essayer, et les expériences extrêmes ne vous font pas peur.",
        nombre: 5,
    })

    await db.model.Signification.create({
        message: "Vous attendez le prince charmant !",
        nombre: 6,
    })

    await db.model.Signification.create({
        message: "Sous votre petit air mystérieux, vous cachez des capacités d'observation et d'analyse incroyables. D'ailleurs, lorsque vous leur donnez des conseils, vos proches les suivent à la lettre !",
        nombre: 7,
    })

    await db.model.Signification.create({
        message: "Des projets, vous en avez toujours en pagaille ! Visionnaire, vous avez l'âme d'un chef : vous commandez, et les autres vous obéissent sans discuter. Et à l'arrivée, on reconnaît vos mérites.",
        nombre: 8,
    })

    await db.model.Signification.create({
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

Avec le numéro calculé, on cherche dans la base [e premier élément ayant ce numéro (méthode [findOne](https://sequelize.org/master/manual/model-querying-finders.html#-code-findone--code-)) et on le renvoie dans le json de résultat. On modifie le fichier *"numerologie/index.js"* pour celà :

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

### création des éléments de la base

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

### lire les prénoms

Pour voir les différents prénoms de la base, il faut que l'on implémente la méthode **R**ead pour notre modèle `Prenoms` (**C**reate est intégré à la route GET `/Prénom`, **U**pdate et **D**elete sont pour l'instant inutiles).

L'usage veut que l'accès aux données soient rangé dans une route qui commence par `/api`. Dans notre cas, on utiliser la route :
GET `/api/prenoms/read/` pour lire tous nos prénoms. Ajoutons cette route à *"numerologie/index.js"* :

```js
// ...

app.get('/api/prenoms/read', (req, res) => {
    db.model.Prenoms.findAll()
        .then((data) => {
            var liste = []
            for (element of data) {
                liste.push({
                    prenom: element.prenom,
                    chiffre: numerologie.chiffre(element.prenom)
                })
            }
            res.json(liste)
        })
})

//...
```

Testez cette route après avec l'url <http://127.0.0.1:3000/api/prenoms/read> avoir ajouté (avec la page de départ) quelques prénoms à la base.

### représenter les prénoms

On peut maintenant finir cette partie en ajoutant une page html *"numerologie/static/prenoms.html"* qui liste tous les prénoms de la base :

```html
<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Les prénoms recherchés</title>
        
        <link rel="stylesheet" href="https://unpkg.com/purecss@2.0.6/build/pure-min.css" integrity="sha384-Uu6IeWbM+gzNVXJcM9XV3SohHtmWE+3VGi496jvgX1jyvDTXfdK+rfZc8C1Aehk5" crossorigin="anonymous">
        
        <link href="main.css" rel="stylesheet">

    </head>
    <body>
        <div id="main">
            <p>Chargement des prénoms...</p>
        </div>
        
        <script>
        main = document.querySelector("#main")
        fetch("/api/prenoms/read")
            .then(response => response.json())
            .then(data => {
                main.innerHTML = ""
                if (data.length == 0) {
                    element = document.createElement("p")
                    element.innerText = "pas de prénoms sauvés dans la base."                    
                    main.appendChild(element)

                    return;
                }
                list = document.createElement("ul")
                main.appendChild(list)
                for (prenom of data) {                    
                    element = document.createElement("li")
                    element.innerText = prenom.prenom
                    list.appendChild(element)
                }
            })
        </script>
    </body>
</html>
```

Cette page affiche un texte par défaut (`<p>Chargement des prénoms...</p>`) qui est remplacé après lecture des prénoms de la base. On distingue 2 cas : la base est vide (et on le signale) ou la base contient des prénoms et on les affiche.

Notez comment on a fait pour :

* supprimer tous les enfant d'un élément de l'arbre DOM : `main.innerHTML = ""`
* créer des éléments : `element = document.createElement("p")`
* ajouter des enfants à un élément : `main.appendChild(element)`

Testez cette page (<http://127.0.0.1:3000/static/prenoms.html>) sur une base vide (juste après un `npm run init`) et sur une base avec des prénoms de stockés.
