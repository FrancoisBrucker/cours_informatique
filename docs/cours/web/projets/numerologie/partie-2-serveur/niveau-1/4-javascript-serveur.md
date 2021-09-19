---
layout: page
title:  "Projet numérologie : partie 2 / niveau 1 / javascript serveur"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %}) / [partie 2]({% link cours/web/projets/numerologie/partie-2-serveur/index.md %}) / [niveau 1]({% link cours/web/projets/numerologie/partie-2-serveur/niveau-1/index.md %}) / [javascript serveur]({% link cours/web/projets/numerologie/partie-2-serveur/niveau-1/4-javascript-serveur.md %})
{: .chemin}

On crée notre première route écrite en javascript et on récupère le résultat dans le front.

## route avec paramètre

Il existe plusieurs façon de passer des paramètres au serveur depuis le navigateur. Nous allons regarder ici la plus ancienne de ces méthodes, qui consiste à passer les paramètres directement dans l'url sous la forme de [query string](https://en.wikipedia.org/wiki/Query_string)

Dans notre cas, on aimerait que notre serveur reconnaisse les requêtes du type : <http://localhost:3000/prénom?valeur=françois>.

> si vous voulez plusieurs paramètres, il faut les séparer par des `&` comme indiqué dans [la documentation](https://en.wikipedia.org/wiki/Query_string)

Ca tombe bien express permet de le faire simplement. Ajoutez la route suivante dans le fichier *"numerologie/index.js"* :

```javascript
// ...

app.get(encodeURI('/prénom'), (req, res) => {
    console.log(req.query)
    res.end()
})

// ...
```

Une url ne peut contenir de caractère non ascii. Ces caractères sont transformés par [encodeURI()](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/encodeURI) par le client avant d'être envoyé au serveur. De là, notre requête ne doit pas attraper les urls qui commencent par `'prénom'`, mais celles commençant par `/pr%C3%A9nom` qui est son encodage. [decodeURI](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/decodeURI) est l'opération inverse.

On récupère la `query` sous la forme d'un dictionnaire directement avec `req.query`. Notez que la conversion en utf8 s'est faite toute seule pour la query.

## retour en json

Le retour de cette requête sera un objet [json](https://developer.mozilla.org/fr/docs/Learn/JavaScript/Objects/JSON). Il pourra répondre à la requête <http://localhost:3000/prénom?valeur=françois> :

```json
{
  prénom: "François",
  chiffre: 8,
}
```

Avant de donner une véritable valeur en utilisant *"numerologie.js"* occupons nous de rendre du json.

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

> Il n'y a pas de soucis avec la ligne `chiffre: chiffre`. Le 1er chiffre est un nom, le second une variable.

## intégration au html

Pour récupérer ce json dans le fichier html, il faut que l'on envoie une requête avec la query lorsque l'on clique sur le bouton et que l'on attende la réponse du serveur avant de changer la valeur dans le paragraphe.

Ceci peut se faire simplement avec un petit bout de javascript côté client, en utilisant la fonction [fetch](https://developer.mozilla.org/fr/docs/Web/API/Fetch_API/Using_Fetch), très pratique, qui permet de récupérer des choses sur internet avec des [promesses](https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Using_promises) :

```javascript
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

On a aussi supprimé l'appel au fichier *"numérologie.js"* qui est maintenant inutile.

## module javascript

Il nous reste plus qu'à transférer le fichier *"static/numerologie.js"* du côté du back.

Pour cela, on va le placer dans un dossier particulier : *"numerologie/back/numerologie.js"*.

Il faut ensuite transformer le fichier en module node, appelable par `require` :

```javascript

function nombre(chaine) {
    var somme = 0
    for (var i=0; i < chaine.length; i++) {
        somme += chaine.charCodeAt(i)
    }
    return somme
}

function somme(nombre) {
    var somme = 0
    chaine = String(nombre)
    for (var i=0; i < chaine.length ; i++) {
        somme += parseInt(chaine.charAt(i))
    }
    return somme
}

function chiffreAssocie(chaine) {
    valeur = nombre(chaine)

    while (valeur > 9) {
        valeur = somme(valeur)
    }
    return valeur
}

module.exports = {
  chiffre: chiffreAssocie,
}
```

Lorsque l'on `require` un fichier, on rend l'objet `module.exports`. Pour numérologie.js, j'exporte un objet qui a un attribut `chiffre` associé à la fonction chiffreAssocie.

On peut alors l'utiliser comme ça dans *"serveur.js"* :

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

> Les import qui sont des fichiers à nous sont décrit par leur chemin relatif, et commencent donc par `./`.

