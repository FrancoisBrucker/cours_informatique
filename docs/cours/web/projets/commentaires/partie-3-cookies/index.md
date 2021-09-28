---
layout: page
title:  "Projet commentaires : partie 3"
category: cours
author: "François Brucker"
---

> [commentaires]({% link cours/web/projets/commentaires/index.md %}) / [partie 3]({% link cours/web/projets/commentaires/partie-3-cookies/index.md %})
{: .chemin}

On ajoute un cookie pour stocker des données côté front, pour l'instant notre pseudo.

## cookies

Un [cookie](https://fr.wikipedia.org/wiki/Cookie_(informatique)) est un objet chez le client. Il a un nom, une durée de vie et contient des informations.

Un cookie est associé à un serveur : le serveur donne un cookie au navigateur qui le lui renvoie à chaque requête.

C'est un moyen simple de créer de la persistance de données entre un navigateur et un serveur.

## voir les cookies

Vous pouvez utilisez les [outils de developpement]({% link cours/web/tuto_outils_dev.md %}), onglet application pour voir les différentes manières de stocker de l'information côté front, dont les cookies.

Vous pouvez aussi y accéder directement en javascript par l'objet [document.cookie](https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie) qui contient le cookie du serveur qui sert la page courante.

## créer des cookie dans express

Pour avoir accès aux cookies, il faut utiliser [cookie-parser](http://expressjs.com/en/resources/middleware/cookie-parser.html).

On commence par l'installer : :command:`npm install --save cookie-parser` puis on l'utilise dans *"commentaires/server.js"* avec un *"middleware"* qui ajoute l'attribut `cooke` à toutes les requêtes qui passent par lui :

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

Pour l'instant, le cookie ne disparait pas. Il va donc conserver indéfiniment le cookie (jusqu'à la fermeture de la fenêtre ou du navigateur souvent). Vous pouvez créer des cookie avec une durée de vie en utilisant l'option `maxAge` : `res.cookie("pseudo", req.body.pseudo, {"maxAge": 3000})`.

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

Le cookie disparaitra s'il n'y a pas de requête au serveur pendant 3s.

## utiliser des cookies

Une fois que le cookie est mis, il est utilisable côté front. En revanche, ce n'est pas un objet javascript mais une chaine de caractère...

Il faut donc analyser la chaine pour retrouver ses petits. IL existe plusieurs façon de faire, nous avons choisi de suivre [ce tutorial](https://howchoo.com/javascript/how-to-manage-cookies-in-javascript) en reprenant leur méthdoe `getCookie`.

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
    document.querySelector("#pseudo").value = getCookie("pseudo")
</script>
```

## resources

* <https://developer.mozilla.org/fr/docs/Web/HTTP/Cookies>
* <https://www.javascripttutorial.net/web-apis/javascript-cookies/>

## cookie signés

Pour passer des informations secrètes (une session par exemple).

> TBD
> <https://stackoverflow.com/questions/52285591/signing-cookies-in-express>

