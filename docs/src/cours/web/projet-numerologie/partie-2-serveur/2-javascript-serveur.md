---
layout: layout/post.njk
title: "Projet numérologie : partie 2 / javascript serveur"

authors:
    - "François Brucker"


eleventyNavigation:
  key: "Projet numérologie : partie 2 / javascript serveur"
  parent: "Projet numérologie / partie 2 serveur"
---

<!-- début résumé -->

On crée notre première route écrite en javascript et on récupère le résultat dans le front.

<!-- fin résumé -->

Le projet ressemble maintenant à ça, en excluant le dossier `node_modules`{.fichier} :

```text
.
├── index.js
├── package-lock.json
├── package.json
└── static
    ├── index.html
    ├── main.css
    └── numerologie.js
```

## Route avec paramètre

Il existe plusieurs façon de passer des paramètres au serveur depuis le navigateur. Nous allons en voir 2.

### Paramètres dans `req.params`

La première façon de faire est de mettre la dernière partie de l'url en paramètre.
Ajoutez la route suivante dans le fichier `numerologie/index.js`{.fichier} :

```javascript
// ...

app.get('/chaine/:prenom', (req, res) => {
    console.log(req.params)
    res.end()
})

// ...
```

Tout ce qui suit `/chaine`{.language-} dans l'url sera considéré comme notre variable `prenom`{.language-}. Ainsi la requête <http://127.0.0.1:3000/chaine/François>

```json
{ prenom: 'François' }
```

{% note %}
Le paramètre ne peut cependant pas contenir de `/`{.language-} car c'est un séparateur de parties d'url.
{% endnote %}

### Url et utf8

Lorsque vous tapez des urls en utf8, celles ci sont encodés en transformant les caractères non ASCII par des nombres précédés d'un `%`{.language-} : c'est [l'encodage %](https://fr.wikipedia.org/wiki/Encodage-pourcent).

On le voit dans le log console de la requête <http://127.0.0.1:3000/chaine/François> qui est  `Time: 19/09/2021 20:29:08 ; url : /chaine/Fran%C3%A7ois` : le `ç` a été transformé en `%C3%A7`.

Cela ne se voit cependant pas dans le code node car les paramètres sont reconvertis en chaîne Unicode pour le traitement.

{% attention %}
Ce n'est cependant pas le cas pour la requête de base, ainsi une route qui aura comme base : `'/chaîne/:prenom'`{.language-} donnera tout le temps un 404. C'est la route `cha%C3%AEne/:prenom`{.language-} qui sera reconnue.

Pour ne pas à avoir à se rappeler des encodage, on pourra utiliser les fonction [encodeURI()](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/encodeURI) et [decodeURI](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/decodeURI)
{% endattention %}

### Paramètres dans `req.query`{.language-}

Nous allons regarder ici la plus ancienne de ces méthodes, qui consiste à passer les paramètres directement dans l'url sous la forme de [query string](https://en.wikipedia.org/wiki/Query_string). C'est la façon classique de passer des paramètres à une url et c'est donc celle-ci que nous garderons ici.

Dans notre cas, on aimerait que notre serveur reconnaisse les requêtes du type : <http://localhost:3000/prénom?valeur=françois>.

{% note %}
Si vous voulez plusieurs paramètres, il faut les séparer par des `&` comme indiqué dans [la documentation](https://en.wikipedia.org/wiki/Query_string)
{% endnote %}

Express permet de le faire tout aussi simplement que précédemment. Ajoutez la route suivante dans le fichier `numerologie/index.js`{.fichier} :

```javascript
// ...

app.get(encodeURI('/prénom'), (req, res) => {
    console.log(req.query)
    res.end()
})

// ...
```

{% note %}
On a utilisé `encodeURI` pour un chemin on ascii.
{% endnote %}

On récupère la `query` sous la forme d'un dictionnaire directement avec `req.query`. Notez que la conversion en utf8 s'est faite toute seule pour la query.

## Retour en json

Le retour de cette requête sera un objet [json](https://developer.mozilla.org/fr/docs/Learn/JavaScript/Objects/JSON). Il pourra répondre à la requête <http://localhost:3000/prénom?valeur=françois> :

```json
{
  prénom: "François",
  chiffre: 8,
}
```

Avant de donner une véritable valeur en utilisant `numerologie.js`{.fichier} occupons nous de rendre du json.

```javascript
// ...

app.get(encodeURI('/prénom'), (req, res) => {
    console.log(req.query)
    prenom = req.query["valeur"]
    chiffre = 8

    res.json({
        prénom: prenom,
        chiffre: chiffre,
    })
})

// ...
```

{% note %}
Il n'y a pas de soucis avec la ligne `chiffre: chiffre`. Le 1er chiffre est un nom, le second une variable.
{% endnote %}

## Intégration au html

Pour récupérer ce json dans le fichier html, il faut que l'on envoie une requête avec la query lorsque l'on clique sur le bouton et que l'on attende la réponse du serveur avant de changer la valeur dans le paragraphe.

Ceci peut se faire simplement avec un petit bout de javascript côté client, en utilisant la fonction [fetch](https://developer.mozilla.org/fr/docs/Web/API/Fetch_API/Using_Fetch), très pratique, qui permet de récupérer des choses sur internet avec des [promesses](https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Using_promises) :

```javascript
document.querySelector("#form-button").addEventListener("click", (event) => {
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

    event.preventDefault();
})
```

Une promesse permet d'attendre que quelque chose d'asynchrone se fasse (ici le retour de notre appel serveur), puis (avec `.then`) de faire des choses. Ici :

   1. une fois que le serveur a répondu, on transforme le résultat en json
   2. avec le json (le second `.then`) on peut facilement accéder aux données pour changer le chiffre.

Ce qui donne le fichier html suivant :

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
        document.querySelector("#form-button").addEventListener("click", (event) => {
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

            event.preventDefault();
        })
        </script>
    </body>
</html>
```

On a aussi supprimé l'appel au fichier `numérologie.js`{.fichier} qui est maintenant inutile.

## Module javascript

Il nous reste plus qu'à transférer le fichier `static/numerologie.js`{.fichier} du côté du back.

Pour cela, on va le placer dans un dossier particulier : `numerologie/back/numerologie.js`{.fichier}.

Il faut ensuite transformer le fichier en module node, appelable par `require`{.language-} :

```javascript

function nombre(chaîne) {
    var somme = 0
    for (var i=0; i < chaîne.length; i++) {
        somme += function nombre(chaîne) {
.charCodeAt(i)
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

Lorsque l'on `require`{.language-} un fichier, on rend l'objet `module.exports`{.language-}. Pour `numérologie.js`{.fichier}, j'exporte un objet qui a un attribut `chiffre`{.language-} associé à la fonction chiffreAssocie.

On peut alors l'utiliser comme ça dans `serveur.js`{.fichier} :

```javascript
// ...

const numerologie = require('./back/numerologie'); //import

// ...

app.get(encodeURI('/prénom'), (req, res) => {
    console.log(req.query)
    prenom = req.query["valeur"]
    chiffre = numerologie.chiffre(prenom) //utilisation

    res.json({
        prénom: prenom,
        chiffre: chiffre, 
    })
})

// ...
```

{% note %}
Les imports qui sont des fichiers à nous sont décrit par leur chemin relatif, et commencent donc par `./`.
{% endnote %}