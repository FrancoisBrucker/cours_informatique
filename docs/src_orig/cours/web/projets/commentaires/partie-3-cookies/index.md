---
layout: page
title:  "Projet commentaires : partie 3 : cookies"
category: cours
author: "François Brucker"
---

> [commentaires]({% link cours/web/projets/commentaires/index.md %}) / [partie 3]({% link cours/web/projets/commentaires/partie-3-cookies/index.md %})
{.chemin}

On ajoute un cookie pour stocker des données côté front, ici le pseudo du dernier message envoyé.

## cookies

Un [cookie](https://fr.wikipedia.org/wiki/Cookie_(informatique)) est un chaine de caractère stoquées sur le navigateur. Il a un nom, une durée de vie et contient des informations.

Un cookie est associé à un serveur : le serveur donne un cookie au navigateur qui le lui renvoie à chaque requête à ce même serveur. Il peut donc n'y avoir qu'un cookie par serveur.

C'est un moyen simple de créer de la persistance de données entre un navigateur et un serveur donné.

## voir les cookies

Vous pouvez utilisez les [outils de developpement]({% link cours/web/tuto_outils_dev.md %}), onglet application, pour voir les différentes manières de stocker de l'information côté front, dont les cookies.

Vous pouvez aussi y accéder directement en javascript par l'objet [document.cookie](https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie) qui contient le cookie du serveur qui sert la page courante.

## créer des cookie dans express

Pour avoir accès aux cookies, il faut utiliser [cookie-parser](http://expressjs.com/en/resources/middleware/cookie-parser.html).

On commence par l'installer côté back en tapant la commande `npm install --save cookie-parser` puis on l'utilise dans *"commentaires/server.js"* avec un *middleware* qui ajoute l'attribut `cookie` à toutes les requêtes qui passent par lui :

```js
// ...
const cookieParser = require('cookie-parser')

// ...
app.use(cookieParser())
```

### création du cookie

Nos allons créer un cookie dans la route '/donne'. Celui-ci va conserver le pseudo de l'utilisateur :

```js
app.post('/donne', (req, res) => {
    console.log(req.body)
    
    res.cookie("pseudo", req.body.pseudo)
    res.redirect(302, '/')
})
```

Testez le sur votre serveur. Envoyez des données au serveur puis tapez `document.cookie` dans la console du navigateur. Vous devriez voir votre cookie.

On peut ajouter un *middleware* au début des route pour voir les cookies qui transitent :

```js
app.use((req, res, next) => {
    console.log(req.cookies)
    next()
})
```

Si vous avez déjà un cookie, vous devriez le voir dans la console (du serveur).

Pour l'instant, le cookie ne disparait pas. Le navigateur va donc conserver indéfiniment le cookie (souvent indéfiniment signifie jusqu'à la fermeture de la fenêtre ou du navigateur). Vous pouvez également créer des cookies avec une durée de vie en utilisant l'option `maxAge`. Par exemple : `res.cookie("pseudo", req.body.pseudo, {"maxAge": 3000})`.

> Il existe de nombreuses options possible. Voir la doc : <https://www.npmjs.com/package/cookie#options-1>

Si vous mettez une durée de vie, on peut revitaliser le cookie à chaque requête au serveur, par exemple avec ce petit *middleware* :

```js
app.use((req, res, next) => {
    if (req.cookies.pseudo) {
        res.cookie("pseudo", req.body.pseudo, {"maxAge": 3000})
    }
    console.log(req.cookies)
    next()
})
```

Le cookie ne disparaitra alors que s'il n'y a pas de requête au serveur pendant 3s et pas juste au bout de 3s.

## utiliser des cookies

Une fois que le cookie est mis, il est utilisable côté front. En revanche, ce n'est pas un objet javascript mais une chaine de caractère...

Il faut donc analyser la chaine pour retrouver ses petits. Il existe plusieurs façon de faire, nous avons choisi de suivre [ce tutorial](https://howchoo.com/javascript/how-to-manage-cookies-in-javascript) en reprenant leur méthode `getCookie`.

On va ajouter un bout de code javascript front dans la page *"donne.html"* qui remplacera la valeur du pseudo s'il est dans le cookie :

```html
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
```

> Notez le `decodeURI` car les cookies ne sont pas directement stockés en unicode.

## on jardine

On ne devrait pas avoir une route qui fait plusieurs choses. En l'état actuel, notre notre route et crée un cookie et envoie des données au serveur. On va séparer les deux actions en deux routes distinctes.

Le `fetch` de *"commentaires/static/donne.html"* va faire les deux routes à la suite de façon asynchrone puisqu'elles ne sont pas liées :

* envoyer les données au serveur
* positionner le cookie.

### routes

commençons par créer nos routes dans *"server.js"*.

#### le cookie

```js
app.get("/cookie/", (req, res) => {
    console.log(req.query)
    for (const property in req.query) {
        // console.log(`${property}: ${req.query[property]}`);

        res.cookie(property, req.query[property])
        res.end("cookie updated")   
      }
})
```

On itère sur les valeurs de la `query` qu'on ajoute au cookie (vous vous rappelez, on a déjà utilisé une query pendant le projet numérologie).

#### requête post

La requête `/donne`  redevient alors ce qu'elle était initialement :

```js
app.post('/donne', (req, res) => {
    console.log(req.body)
    res.redirect(302, '/')
})
```

### html

Le script qui `fetch` de *"commentaires/static/donne.html"* devient alors : 

```html
<script>
    document.querySelector("#bouton_envoi").addEventListener("click", (event) => {
        if (!document.querySelector("#form_avis").checkValidity()) {
            console.log("formulaire non envoyé")
            event.preventDefault()
            event.stopPropagation()

            return
        }
        data = {
            "pseudo": document.querySelector("#pseudo").value,
            "titre": document.querySelector("#titre").value,
            "message": document.querySelector("#message").value
        }
        fetch("/cookie/?pseudo=" + data.pseudo)

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

## resources

* <https://developer.mozilla.org/fr/docs/Web/HTTP/Cookies>
* <https://www.javascripttutorial.net/web-apis/javascript-cookies/>
