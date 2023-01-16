---
layout: layout/post.njk 
title:  "Projet commentaires : partie 5 : structure"
category: cours
author: "François Brucker"
---

> [commentaires]({% link cours/web/projets/commentaires/index.md %}) / [partie 5]({% link cours/web/projets/commentaires/partie-5-structures/index.md %})
{.chemin}

## structure du projet

```text
.
├── ./db.js
├── ./db.sqlite
├── ./db.test.js
├── ./models
│   └── ./models/message.js
├── ./node_modules
├── ./package-lock.json
├── ./package.json
├── ./server.js
└── ./static
    ├── ./static/donner.html
    ├── ./static/index.html
    ├── ./static/lire.html
    ├── ./static/node_modules
    ├── ./static/package-lock.json
    └── ./static/package.json
```

## fichiers

### db.js

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

### db.test.js

```js
const { Sequelize, DataTypes } = require('sequelize');
// const sequelize = new Sequelize('sqlite::memory:');

path = require('path')

const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: path.join(__dirname, 'db.sqlite')
});

const Message = sequelize.define('Message', {
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

### /models/message.js

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

### package.json

```json
{
  "name": "commentaires",
  "version": "1.0.0",
  "description": "donnez votre avis",
  "main": "server.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "node server.js"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "cookie-parser": "^1.4.5",
    "express": "^4.17.1",
    "sequelize": "^6.6.5",
    "sqlite3": "^5.0.2"
  }
}

```

### server.js

```js
const path = require('path')

const express = require('express')
const cookieParser = require('cookie-parser')

const db = require('./db')

const app = express()


const hostname = '127.0.0.1';
const port = 3000;

app.use(cookieParser())
// app.use(express.json())

// app.use((req, res, next) => {
//     console.log(req.cookies)
//     next()
// })

app.use("/static", express.static(path.join(__dirname, '/static')))

app.get('/', (req, res) => {
    res.redirect(301, '/static/index.html')
})

app.get("/cookie/", (req, res) => {
    console.log(req.query)
    for (const property in req.query) {
        // console.log(`${property}: ${req.query[property]}`);

        res.cookie(property, req.query[property])
        res.end("cookie updated")   
      }
})

app.use(express.json())

app.post("/api/create/", (req, res) => {
    db.models.Message.create({
        pseudo: req.body.pseudo,
        titre: req.body.titre,
        message: req.body.message
    }).then((message) => {
        res.json(message)
    }).catch((err) => {
        res.end("error")
        console.log(err)
    })
})

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

app.use(function (req, res) {
    console.log("et c'est le 404 : " + req.url);

    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/html');

    res.end("<html><head><title>404</title></head><body><h1>Et c'est le 404.</h1><p> ressource non trouvée</p></body></html>");

})

app.listen(port, hostname);
console.log(`Server running at http://${hostname}:${port}/`);
```

### static/donner.html

```html
<!doctype html>
<html lang="fr">

<head>
    <meta charset="utf-8">
    <title>Donner son avis</title>

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
        </nav>
    </header>

    <div class="main container-fluid row">
        <div class="col"></div>
        <form id="form_avis" class="was-validated col-6">
            <div class="mb-3">
                <label for="pseudo" class="form-label">Pseudo</label>
                <input class="form-control" id="pseudo" required>
            </div>
            <div class="mb-3">
                <label for="titre" class="form-label">Titre</label>
                <input class="form-control" id="titre" required>
            </div>
            <div class="mb-3">
                <label for="message" class="form-label">Message</label>
                <textarea class="form-control" rows="7" id="message" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary" id="bouton_envoi">Envoyer</button>
        </form>
        <div class="col"></div>
    </div>

    <footer class="footer fixed-bottom text-center bg-dark">
        <p class="text-white">Le site qui permet de donner son avis.</p>
    </footer>

    <script>
        document.querySelector("#bouton_envoi").addEventListener("click", (event) => {
            if (!document.querySelector("#form_avis").checkValidity()) {
                console.log("formulaire non envoyé")
                event.preventDefault()

                return
            }
            data = {
                "pseudo": document.querySelector("#pseudo").value,
                "titre": document.querySelector("#titre").value,
                "message": document.querySelector("#message").value
            }
            fetch("/cookie/?pseudo=" + data.pseudo)

            fetch("/api/create", {
                'method': "POST",
                'headers': {
                    'Content-Type': 'application/json'
                },
                'body': JSON.stringify(data)
            })

            console.log(JSON.stringify(data, null, 2))
            event.preventDefault()
            location.reload()
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
</body>

</html>
```

### static/index.html

```html
<!doctype html>
<html lang="fr">

<head>
    <meta charset="utf-8">
    <title>Commentaires</title>

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

        .choix {
            padding: 50px;
        }

        .bas {
            margin-top: 100px;
        }
    </style>
</head>

<body>
    <header>
        <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
            <a class="marge navbar-brand" href="#">Maison</a>
        </nav>
    </header>

    <div class="main container-fluid text-center">
        <div class="row">
            <h1 class="display-1">Votre avis [n|v]ous intéresse</h1>
        </div>
        <div class="bas row align-items-center gx-6">
            <div class="col">
                <div class="choix border bg-light">
                    <p>donnez votre avis</p>
                    <p><a class="btn btn-primary" href="./donner.html" role="button">DONNER !</a></p>
                </div>
            </div>
            <div class="col">
                <div class="choix border bg-light">
                    <p>lisez des avis</p>
                    <p><a class="btn btn-danger" href="./lire.html" role="button">LIRE !</a></p>
                </div>
            </div>
        </div>

    </div>

    <footer class="footer fixed-bottom text-center bg-dark">
        <p class="text-white">Le site qui permet de donner son avis.</p>
    </footer>
</body>

</html>
```

### static/lire.html

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

### static/package.json

```json
{
  "name": "static",
  "version": "1.0.0",
  "description": "partie statique du site",
  "main": "index.html",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "bootstrap": "^5.1.1"
  }
}
```
