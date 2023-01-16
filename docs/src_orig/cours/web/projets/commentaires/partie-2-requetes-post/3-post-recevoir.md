---
layout: layout/post.njk 
title:  "Projet commentaires : partie 2 / recevoir les données"
category: cours
author: "François Brucker"
---

> [commentaires]({% link cours/web/projets/commentaires/index.md %}) / [partie 2]({% link cours/web/projets/commentaires/partie-2-requetes-post/index.md %}) / [recevoir les données]({% link cours/web/projets/commentaires/partie-2-requetes-post/3-post-recevoir.md %})
{.chemin}

On récupère les données POST envoyées au serveur par le front.

## gestion avec express

> Vous verrez des tutoriaux qui vous font installer `body-parser`, ils sont obsolètes. Depuis express 4.16, on peut utiliser express pour cela.
{.attention}

Comme il faut récupérer le corps de la réquête POST, on va faire passer toutes les requêtes par *middleware* qui va ajouter un attribut `body` contenant le corps de la requête.

C'est identique à ce qu'on a fait précédemment dans le projet numérologie :

```js
const express = require('express')
// ...

app.use(express.json())
```

La ligne précédente ajoute  un attribut `body` qui contient le corps de la requête au format json. Pile ce que l'on veut. On ajoute donc ce middleware juste après les requêtes statiques (qui n'en ont pas besoin).

On obtient au final le code suivant qui ajoute une route POST nommée `/donne` qui  affiche son résultat dans la console (du serveur) :

Fichier *"commentaires/server.js"* :

```js
const path = require('path')

const express = require('express')

const app = express()


const hostname = '127.0.0.1';
const port = 3000;


app.use("/static", express.static(path.join(__dirname, '/static')))

app.get('/', (req, res) => {
    res.redirect(301, '/static/index.html')
})

app.use(express.json())

app.post('/donne', (req, res) => {
    console.log(req.body)
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

## gestion du formulaire après envoi

Dans le front, pour éviter l'envoie multiple des même données (si l'utilisateur appuie frénétiquement sur le bouton), on va rendre le formulaire non envoyable après un envoi en rechargeant la page. Ceci est conforme au pattern [post/redirect/get](https://en.wikipedia.org/wiki/Post/Redirect/Get), mais côté client.

Notre script de *"commentaires/static/donner.html"* devient alors :

```html
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
            fetch("/donne", {
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
```

C'est la ligne `location.reload()` qui recharge la page, et par là *efface* toutes les données.

On peut maintenant envoyer des données depuis le front et les recevoir sur le serveur. Une fois la base de donnée configurée, le serveur pourra se *rappeler* de choses faites par le client.
