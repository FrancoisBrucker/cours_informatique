---
layout: layout/post.njk
title: "Projet numérologie : partie 2 / structures"

authors:
    - "François Brucker"


eleventyNavigation:
  key: "Projet numérologie : partie 2 / structures"
  parent: "Projet numérologie / partie 2 serveur"
---

<!-- début résumé -->

Structure du projet à l'issue de la partie 2.

<!-- fin résumé -->

## structure du projet

```text
.
├── back
│   └── numerologie.js
├── index.js
├── package-lock.json
├── package.json
└── static
    ├── index.html
    └── main.css
```

## fichiers

### `back/numerologie.js`{.fichier}

```javascript
function nombre(chaîne) {
    var somme = 0
    for (var i=0; i < chaîne.length; i++) {
        somme += chaîne.charCodeAt(i)
    }
    return somme
}

function somme(nombre) {
    var somme = 0
    chaîne = String(nombre)
    for (var i=0; i < chaîne.length ; i++) {
        somme += parseInt(chaîne.charAt(i))
    }
    return somme
}

function chiffreAssocie(chaîne) {
    valeur = nombre(chaîne)

    while (valeur > 9) {
        valeur = somme(valeur)
    }
    return valeur
}

module.exports = {
    chiffre: chiffreAssocie,
}
```

### `index.js`{.fichier}

```javascript
const path = require('path')

const express = require('express')

const numerologie = require('./back/numerologie');

const app = express()

const hostname = '127.0.0.1';
const port = 3000;


app.use(function (req, res, next) {
    date = new Date(Date.now())
    console.log('Time:', date.toLocaleDateString(), date.toLocaleTimeString(), "; url :", req.url);
    next(); // sans cette ligne on ne pourra pas poursuivre.
})

app.use("/static", express.static(path.join(__dirname, '/static')))

app.get('/', (req, res) => {
    res.redirect(301, '/static/index.html')
})

app.get(encodeURI('/prénom'), (req, res) => {
    console.log(req.query)
    prénom = req.query["valeur"]
    chiffre = numerologie.chiffre(prénom)

    res.json({
        prénom: prénom,
        chiffre: chiffre,
    })
})

app.use(function (req, res) {
    console.log("et c'est le 404 : " + req.url);

    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/html');

    res.end("");

})

app.listen(port, hostname);
console.log(`Server running at http://${hostname}:${port}/`);
```

### `package.json`{.fichier}

```json
{
  "name": "numerologie",
  "version": "1.0.0",
  "description": "de la numérologie",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "François Brucker",
  "license": "WTFPL",
  "dependencies": {
    "express": "^4.17.1"
  }
}
```

### `static/index.html`{.fichier}

```html
<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Numérologie</title>
        
        <link rel="stylesheet" href="https://unpkg.com/purecss@2.0.6/build/pure-min.css" integrity="sha384-Uu6IeWbM+gzNVXJcM9XV3SohHtmWE+3VGi496jvgX1jyvDTXfdK+rfZc8C1Aehk5" crossorigin="anonymous">
        
        <link href="main.css" rel="stylesheet">

    </head>
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
        <script>
            function on_click() {
                prenom = document.querySelector("#form-input").value;
                if (prenom) {
                    fetch('/prénom/?valeur=' + prenom)
                        .then(response => response.json())
                        .then(data => {
                            document.querySelector("#chiffre").textContent = data.chiffre
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
</html>
```

### `static/main.css`{.fichier}

```css
html, body {
  margin: 0;
  background-color: azure;
}

.main {
    margin-top: 100px;
    margin-left: auto;
    margin-right: auto;
    width: 600px;
    text-align: center;
}

p {
    font-size: 100px;
}
```
