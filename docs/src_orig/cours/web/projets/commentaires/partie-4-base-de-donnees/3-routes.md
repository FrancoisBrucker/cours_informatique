---
layout: page
title:  "Projet commentaires : partie 4 / routes"
category: cours
author: "François Brucker"
---

> [commentaires]({% link cours/web/projets/commentaires/index.md %}) / [partie 4]({% link cours/web/projets/commentaires/partie-4-base-de-donnees/index.md %}) / [routes]({% link cours/web/projets/commentaires/partie-4-base-de-donnees/3-routes.md %})
{.chemin}

On crée les routes permettant d'accéder aux données dans notre serveur.

## import de la base

On ajoute en début de fichier *"commentaires/server.js"* l'import de notre base : `const db = require("./db")`. A partir de là, on pourra accéder à la base par le modèle (`db.models.Message`) ou via sequelize (`db.sequelize`).

## routes

On va implémenter une partie des routes CRUD, nous n'aurons en effet besoin que des méthodes **C**reate et **R**ead.

Pour séparer la gestion des données des autres route, on va faire commencer toutes les routes par `/api/`.

### create

Une requête POST qui récupère un json permettant de créer une donnée qu'on met en base :

```js
app.post("/api/create/", (req, res) => {

    db.models.Message.create({
        pseudo: req.body.pseudo,
        titre: req.body.titre,
        message: req.body.message
    }).then((message) => {
        res.json(message)
    }).catch((err) => {
        console.log(err)
    })
})
```

On a pas utiliser de `await` ici. Qu'une requête soit asynchrone côté serveur, c'est très bien.

Cette route va remplacer la route POST `/donne` que nous avions précédemment créée et qui ne sert plus.  Du coup, le fetch de *"commentaires/static/donne.html"* devient :

```js
fetch("/api/create", {
    'method': "POST",
    'headers': {
        'Content-Type': 'application/json'
    },
    'body': JSON.stringify(data)
})
```

### read

On va utiliser une route avec des options. Si l'on utilise :

* la route `/api/read/` : on rendra une liste de tous les message
* la route `/api/read/?pseudo="mon pseudo"` : on rendra une liste de tous les messages d'un pseudo donné.

#### lire tous les messages

Ceci va nous permettre de gérer la page *"commentaires/static/lire.html"*.

Commençons par rendre tous les commentaires avec notre méthode read :

```js
app.get("api/read", (req, res) => {
    db.models.Message.findall({
    }).then((message) => {
        res.json(message)
    }).catch((err) => {
        res.end("error")
        console.log(err)
    })
})
```

Que l'on va utiliser dans *"commentaires/static/lire.html"* pour lister tous les messages : 

```html
<!doctype html>
<html lang="fr">

<head>
    <meta charset="utf-8">
    <title>Lire un avis</title>

    <link href="./node_modules/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="./node_modules/bootstrap//dist/js/bootstrap.bundle.min.js"></script>

    <style>
        .main {
            margin-top: 100px;
            margin-bottom: 50px;
        }

        nav .marge {
            margin-right: 20px;
            margin-left: 20px;
        }
    </style>
</head>

<body>
    <header>
        <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
            <a class="marge navbar-brand" href="./index.html">Maison</a>
            <form class="navbar form-inline ms-auto row">
                <input class="form-control col" type="text" placeholder="Search" aria-label="Search">
                <button class="marge col-3 btn btn-outline-success" type="submit">Search</button>
            </form>
        </nav>
    </header>

    <div class="main container-fluid" id="main">
        <div>
            <p>Chargement des commentaires...</p>
        </div>
        <!-- <div class="card">
            <div class="card-body">
                <h5 class="card-title">titre du commentaire</h5>
                <h6 class="card-subtitle mb-2 text-muted">pseudo</h6>
                <p class="card-text">Contenu du commentaire.</p>
            </div>
        </div> -->
    </div>

    <footer class="footer fixed-bottom text-center bg-dark">
        <p class="text-white">Le site qui permet de donner son avis.</p>
    </footer>
    <script>
        main = document.querySelector("#main")
        fetch("/api/read")
            .then(response => response.json())
            .then(data => {
                // console.log(data)
                for (const message of data) {
                    // console.log(message)

                    card = document.createElement("div")
                    card.classList.add("card")
                    cardBody = document.createElement("div")
                    cardBody.classList.add("card-body")
                    card.appendChild(cardBody)

                    element = document.createElement("h5")
                    element.classList.add("card-title")
                    element.innerText = message.titre
                    cardBody.appendChild(element)

                    element = document.createElement("h6")
                    element.classList.add("card-subtitle", "mb-2", "text-muted")
                    element.innerText = message.pseudo
                    cardBody.appendChild(element)

                    element = document.createElement("p")
                    element.classList.add("card-text")
                    element.innerText = message.message
                    cardBody.appendChild(element)


                    main.appendChild(card)
                }
            })

    </script>
</body>

</html>
```

#### lire certains messages

Les query vont nous permettre de particulariser les lectures. Commençons par modifier la requête dans *"commentaires/server.js"* :

```js
app.get("/api/read/", (req, res) => {
    if ("pseudo" in req.query) {
        db.models.Message.findAll({
            "where": {
                "pseudo": req.query.pseudo
            }
        }).then((message) => {
            res.json(message)
        }).catch((err) => {
            res.end("error")
            console.log(err)
        })
    
    } else {
        db.models.Message.findAll({
        }).then((message) => {
            res.json(message)
        }).catch((err) => {
            res.end("error")
            console.log(err)
        })    
    }
})
```

On fait maintenant la différence entre une requête sans paramètre (qui lit renvoie tous les messages) et une requête avec un paramètre (pour l'instant uniquement le pseudo) qui renvoie les message d'un pseudo donné.

Modifions *"commentaires/static/lire.html"* pour finir cette partie en :

* ajoutant un petit script qui gère les cookie et pré-remplis le champ recherche
* lie le bouton à la requête

```html
<!doctype html>
<html lang="fr">

<head>
    <meta charset="utf-8">
    <title>Lire un avis</title>

    <link href="./node_modules/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="./node_modules/bootstrap//dist/js/bootstrap.bundle.min.js"></script>

    <style>
        .main {
            margin-top: 100px;
            margin-bottom: 50px;
        }

        nav .marge {
            margin-right: 20px;
            margin-left: 20px;
        }
    </style>
</head>

<body>
    <header>
        <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
            <a class="marge navbar-brand" href="./index.html">Maison</a>
            <form class="navbar form-inline ms-auto row">
                <input id="pseudo" class="form-control col" type="text" placeholder="Search" aria-label="Search">
                <button id="bouton_envoi" class="marge col-3 btn btn-outline-success" type="submit">Search</button>
            </form>
        </nav>
    </header>

    <div class="main container-fluid" id="main">
        <div>
            <p>Chargement des commentaires...</p>
        </div>
        <!-- <div class="card">
            <div class="card-body">
                <h5 class="card-title">titre du commentaire</h5>
                <h6 class="card-subtitle mb-2 text-muted">pseudo</h6>
                <p class="card-text">Contenu du commentaire.</p>
            </div>
        </div> -->
    </div>

    <footer class="footer fixed-bottom text-center bg-dark">
        <p class="text-white">Le site qui permet de donner son avis.</p>
    </footer>
    <script>
        main = document.querySelector("#main")
        fetch("/api/read")
            .then(response => response.json())
            .then(data => {
                // console.log(data)
                for (const message of data) {
                    // console.log(message)

                    card = document.createElement("div")
                    card.classList.add("card")
                    cardBody = document.createElement("div")
                    cardBody.classList.add("card-body")
                    card.appendChild(cardBody)

                    element = document.createElement("h5")
                    element.classList.add("card-title")
                    element.innerText = message.titre
                    cardBody.appendChild(element)

                    element = document.createElement("h6")
                    element.classList.add("card-subtitle", "mb-2", "text-muted")
                    element.innerText = message.pseudo
                    cardBody.appendChild(element)

                    element = document.createElement("p")
                    element.classList.add("card-text")
                    element.innerText = message.message
                    cardBody.appendChild(element)


                    main.appendChild(card)
                }
            })
    </script>
        <script>
            function getCookie(name) {
                var cookie, c;
                cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    c = cookies[i].split('=');
                    if (c[0] == name) {
                        return c[1];
                    }
                }
                return "";
            }
            
            document.querySelector("#pseudo").value = decodeURI(getCookie("pseudo"))
        </script>
    <script>
        main = document.querySelector("#main")
        document.querySelector("#bouton_envoi").addEventListener("click", (event) => {
            pseudo = document.querySelector("#pseudo").value
            if (!pseudo) {
                url = "/api/read/"
                console.log("prout")
            } else {
                url = "/api/read/?pseudo=" + pseudo
            }
            
            fetch(url)
            .then(response => response.json())
            .then(data => {
                // console.log(data)
                main.textContent = "";
                for (const message of data) {
                    // console.log(message)
                    
                    card = document.createElement("div")
                    card.classList.add("card")
                    cardBody = document.createElement("div")
                    cardBody.classList.add("card-body")
                    card.appendChild(cardBody)

                    element = document.createElement("h5")
                    element.classList.add("card-title")
                    element.innerText = message.titre
                    cardBody.appendChild(element)

                    element = document.createElement("h6")
                    element.classList.add("card-subtitle", "mb-2", "text-muted")
                    element.innerText = message.pseudo
                    cardBody.appendChild(element)

                    element = document.createElement("p")
                    element.classList.add("card-text")
                    element.innerText = message.message
                    cardBody.appendChild(element)


                    main.appendChild(card)
                }
            })
            event.preventDefault()
        })
    </script>
</body>

</html>
```