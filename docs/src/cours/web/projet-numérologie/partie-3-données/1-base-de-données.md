---
layout: layout/post.njk

title: "Projet numérologie : partie 3 / base de données"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Ajout d'une base de données SQlite au serveur

<!-- fin résumé -->

On va utiliser l'ORM sequelize en conjonction avec une base SQlite. Donc commençons par ajouter les 2 modules à notre projet :

```
npm add --save sqlite3 sequelize
```

## Base en lecture seule

On va commencer par créer une base de donnée en lecture seule pour associer à chaque chiffre sa signification (scientifique).

### Modèle

Le modèle va être identique au [modèle du cours]({{"/cours/web/base-données" | url}}).

{% faire %}
Créez le fichier `numérologie/db.js`{.fichier} et copiez/collez y le code suivant, qui crée le modèle :
{% endfaire %}

```js
import { Sequelize, DataTypes } from 'sequelize';

import { fileURLToPath } from 'url';
import path from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);


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

export default {
    sequelize: sequelize,
    model: {
        Signification: Signification,
    }
}
```

### Initialisation

On crée un fichier pour stocker les données initiales dans la base.

{% faire %}
Créez le fichier `numérologie/db.init.js`{.fichier} et copiez/collez y le code suivant :
{% endfaire %}

```js
import db from "./db.js";

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
        console.log("base initialisée")
    })
```

### Script d'initialisation de la base

On a coutume de mettre les différents scripts utiles dans la partie `script` du fichier `package.json`{.fichier}.

{% faire %}
Ajoutez un script d'initialisation au fichier `package.json`{.fichier}. Copiez/collez y le code suivant au bon endroit :
{% endfaire %}

```json
...

  "scripts": {
    "init": "node db.init.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },

...
```

On pourra ensuite exécuter ce script (juste une commande pour l'instant) en tapant la commande :

```
npm run init
```

Ajoutons également une liste des différentes commandes possibles dans un fichier de documentation.

{% faire %}
Créez un fichier `numérologie/readme.md`{.fichier} où vous placerez les lignes suivantes :
{% endfaire %}

```markdown
# Numérologie

Voyez la vie en base 10 en associant un chiffre à votre prénom.

## initialisation

`npm run init`
```

{% note %}
Il est important de toujours avoir une documentation à jour. Faites l'effort d'ajouter immédiatement la documentation à tout script qui a pour but d'être utilisé par un utilisateur qui n'est pas forcément le développeur.
{% endnote %}

## Utilisation de la base

Nous allons donner le message associé au numéro en plus du reste.

### Côté serveur

Avec le numéro calculé, on cherche dans la base [e premier élément ayant ce numéro (méthode [findOne](https://sequelize.org/master/manual/model-querying-finders.html#-code-findone--code-)) et on le renvoie dans le json de résultat. On modifie le fichier `numérologie/index.js`{.fichier} pour cela :

```js
// ...

import db from "./db.js"

// ...

app.get(encodeURI('/prénom'), (req, res) => {
    console.log(req.query)
    let prénom = req.query["valeur"]
    let chiffre = numérologie.chiffre(prénom) 
    db.model.Signification.findOne({
        where: {
            nombre: chiffre
        }
    }).then((data) => {
        res.json({
            prénom: prénom,
            chiffre: chiffre, 
            message: data.message
        })
    })
})

// ...
```

Notez que l'accès en base est asynchrone, il faut donc attendre le résultat (avec le `then`{.language-} des promesses) avant de finir la requête.

### Côté client

On va créer un div qui va afficher le message reçu en plus du chiffre (pour l'instant le front ne récupère que le chiffre associé). Il faut donc modifier le fichier `numérologie/static/index.html`{.fichier} :

```html
<!-- ... -->

    <body>
        <div class="main">
            <form class="pure-form">
                <label>Prénom :</label>
                <input type="text" id="form-input"/>
            
                <button type="submit" id="form-button" class="pure-button pure-button-primary">Envoi</button>
            </form>
            <div class="pure-g">
                <div class="pure-u-1-3"></div>
                <div class="pure-u-1-3"><p id="chiffre">7</p></div>
                <div class="pure-u-1-3"></div>
            </div>

        </div>
        <div id="message"></div>

        <script>
            function on_click() {
                let prénom = document.querySelector("#form-input").value;
                if (prénom) {
                    fetch('/prénom/?valeur=' + prénom)
                        .then(response => response.json())
                        .then(data => {
                            document.querySelector("#chiffre").textContent = data.chiffre
                            document.querySelector("#message").textContent = data.message

                            console.log(data)
                        })
                } else {
                    document.querySelector("#chiffre").textContent = "?"
                }

            }
            document.querySelector("#form-button").addEventListener("click", (event) => {
                on_click()
                event.preventDefault();
            })
        </script>
    </body>

<!-- ... -->

```

## Base en écriture

Ajoutons un autre modèle qui stocke les prénoms recherchés. On ne va cependant stocker qu'une seule fois le prénom.

### Modèle prénom

On modifie `numérologie/db.js`{.fichier} pour qu'il inclut le nouveau modèle :

```js
// ...

const Prénoms = sequelize.define('Prénoms', {
    prénom: {
        type: DataTypes.STRING,
        allowNull: false
    },
}, {
    // Other model options go here
});

// ...

export default {
    sequelize: sequelize,
    model: {
        Signification: Signification,
        Prénoms: Prénoms,
    }
}
```

Puis on recrée notre base de données avec la commande :

```
npm run init
```

### Création des éléments de la base

Il nous reste plus qu'à ajouter, si nécessaire, le prénom dans la base. On modifie la route dans `numérologie/index.js`{.fichier} :

```js
// ...

app.get(encodeURI('/prénom'), (req, res) => {
    console.log(req.query)
    let prénom = req.query["valeur"]
    let chiffre = numérologie.chiffre(prénom) 
    db.model.Prénoms.findOne({
        where: {
            prénom: prénom
        }
    }).then((data) => {
        if (data === null ) {
            db.model.Prénoms.create({
                prénom: prénom
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
            prénom: prénom,
            chiffre: chiffre, 
            message: data.message
        })
    })
})

//...
```

Le code précédent commence par tenter de chercher le prénom dans la base. S'il n'y est pas (le retour de la requête est `null`{.language-}), on sauve le prénom.
Les deux recherches sont asynchrones et indépendantes.

{% info %}
Les deux opérateurs `==` et `===` [sont différents](https://developer.mozilla.org/fr/docs/Web/JavaScript/Equality_comparisons_and_sameness) en javascript.
{% endinfo %}

### Lecture des prénoms

Pour voir les différents prénoms de la base, il faut que l'on implémente la méthode **R**ead pour notre modèle `Prénoms` (**C**reate est intégré à la route GET `/prénom`, **U**pdate et **D**elete sont pour l'instant inutiles).

L'usage veut que l'accès aux données soient rangé dans une route qui commence par `/api`. Dans notre cas, on utiliser la route :
GET `/api/prénoms/read/` pour lire tous nos prénoms. Ajoutons cette route à `numérologie/index.js`{.fichier} (que l'on place **avant** la gestion des 404...) :

```js
// ...

app.get(encodeURI('/api/prénoms/read'), (req, res) => {
    db.model.Prénoms.findAll()
        .then((data) => {
            var liste = []
            for (element of data) {
                liste.push({
                    prénom: element.prénom,
                    chiffre: numérologie.chiffre(element.prénom)
                })
            }
            res.json(liste)
        })
})

//...
```

{% faire %}

Testez cette route après avec l'url <http://127.0.0.1:3000/api/prenoms/read> avoir ajouté (avec la page de départ) quelques prénoms à la base de données.
{% endfaire %}

### Représenter les prénoms

On peut maintenant finir cette partie en ajoutant une page html `numérologie/static/prénoms.html`{.fichier} qui liste tous les prénoms de la base :

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
        let main = document.querySelector("#main")
        fetch("/api/prénoms/read")
            .then(response => response.json())
            .then(data => {
                main.innerHTML = ""
                if (data.length == 0) {
                    element = document.createElement("p")
                    element.innerText = "pas de prénoms sauvés dans la base."                    
                    main.appendChild(element)

                    return;
                }
                let list = document.createElement("ul")
                main.appendChild(list)
                for (prénom of data) {                    
                    element = document.createElement("li")
                    element.innerText = prénom.prénom
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

{% faire %}

Testez cette page (<http://127.0.0.1:3000/static/prénoms.html>) sur une base vide (juste après un `npm run init`) et sur une base avec des prénoms de stockés.

{% endfaire %}
