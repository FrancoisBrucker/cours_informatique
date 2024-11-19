---
layout: layout/post.njk

title: "Projet numérologie : partie 2 / javascript serveur"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

On crée notre première route écrite en javascript et on récupère le résultat dans le front.

<!-- fin résumé -->

> TBD : à refaire sans json. Uniquement avec du texte.

Le projet ressemble maintenant à ça, en excluant le dossier `node_modules`{.fichier} :

```
.
├── index.js
├── package-lock.json
├── package.json
└── static
    ├── index.html
    ├── main.css
    └── numérologie.js
```

Nous échangerons dans cette partie des données entre le client (le navigateur) et le serveur (en node). Nous passerons ces objets dans le format [json](https://www.json.org/json-fr.html) qui est — en gros — un moyen de transformer des dictionnaires javascript en texte en vue de les transférer (ce qu'on fera) ou de les stocker au format texte.

Dans cette partie, retenez donc juste que l'on transfère (via le format json) des dictionnaires depuis le serveur vers le client.

## Route avec paramètres

Pour passer les données au serveur, nous allons utiliser les [routes avec query du cours]({{ "/cours/web/serveur-web/routes-paramètres" | url }}#query). Pour notre projet, on veut qu'une fois que l'utilisateur a rempli le formulaire il appuie sur le bouton d'envoi qui demande au serveur le numéro associé au prénom. Une fois que l'on a reçu la réponse du serveur on met à jour la page.

Commençons par traiter le plus simple, la réponse du serveur. Il doit répondre à la requête avec paramètres (<http://127.0.0.1:3000/chaine/François> ou <http://localhost:3000/prenom?valeur=françois> selon la méthode choisie) par un dictionnaire contenant les réponses :

```json
{
  prénom: "François",
  chiffre: 8,
}
```

On va procéder en 2 temps. On commence par créer la route, puis on va y intégrer la logique de conversion

### Route

Ce dictionnaire est envoyé au client sous la forme d'un objet objet [json](https://developer.mozilla.org/fr/docs/Learn/JavaScript/Objects/JSON). Avant de donner une véritable valeur en utilisant `numérologie.js`{.fichier} occupons nous d'envoyer notre dictionnaire au format json. Nous avons chois d'utiliser la méthode avec query :

```javascript
// ...

app.get('/prenom', (req, res) => {
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

### Logique de conversion

Pour associer un numéro spécifique à chaque prénom, on reprend le fichier `static/numérologie.js`{.fichier} qu'il faut pouvoir intégrer au serveur. Pour cela, on va commencer par le placer dans un dossier particulier : `numérologie/back/numérologie.js`{.fichier} puis il faut le modifier pour le transformer en module ES6 :

```javascript

function nombre(chaîne) {
    let somme = 0
    for (let i=0; i < chaîne.length; i++) {
        somme += function nombre(chaîne) {
.charCodeAt(i)
    }
    return somme
}

function somme(nombre) {
    let somme = 0
    let chaîne = String(nombre)
    for (let i=0; i < chaîne.length ; i++) {
        somme += parseInt(chaîne.charAt(i))
    }
    return somme
}

function chiffreAssocie(chaîne) {
    let valeur = nombre(chaîne)

    while (valeur > 9) {
        valeur = somme(valeur)
    }
    return valeur
}

export default {
  chiffre: chiffreAssocie,
}
```

A à la fin du module, on décrit ce que l'on veut exporter. Ici un dictionnaire qui va associer la fonction `chiffreAssocie`{.language-} au nom `chiffre`{.language-}

{% lien %}
[Documentation sur les modules](https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Modules)
{% endlien %}

Lorsque l'on `import toto from './titi.js'`{.language-}, on rend l'objet `export default`{.language-} du fichier `titi.js`{.fichier} et on l'appelle `toto`{.language-}. Pour `numérologie.js`{.fichier}, j'exporte un objet qui a un attribut `chiffre`{.language-} associé à la fonction chiffreAssocie.

On peut alors l'utiliser comme ça dans `serveur.js`{.fichier} :

```javascript
// ...

import numérologie from './back/numérologie.js'; //import

// ...

app.get('/prenom', (req, res) => {
    console.log(req.query)
    prenom = req.query["valeur"]
    chiffre = numérologie.chiffre(prenom) //utilisation

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

## Réception des données par le client

Pour récupérer les données côté client, il faut que l'on envoie une requête avec la query lorsque l'on clique sur le bouton et que l'on attende la réponse du serveur avant de changer la valeur dans le paragraphe.

Ceci peut se faire simplement avec un petit bout de javascript côté client, en utilisant la fonction [fetch](https://developer.mozilla.org/fr/docs/Web/API/Fetch_API/Using_Fetch), très pratique, qui permet de récupérer des choses sur internet avec des [promesses](https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Using_promises) :

```javascript
document.querySelector("#form-button").addEventListener("click", (event) => {
    let prenom = document.querySelector("#form-input").value;
    if (prenom) {
        fetch('/prenom/?valeur=' + prenom)
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
   2. avec le json (le second `.then`{.language-}) on peut facilement accéder aux données pour changer le chiffre.

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
            let prenom = document.querySelector("#form-input").value;
            if (prenom) {
                fetch('/prenom/?valeur=' + prenom)
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

## Url et utf8

Vous avez sûrement remarqué que nos routes ne sont pas du vrai français :

1. <http://localhost:3000/chaine/françois> à la place de <http://localhost:3000/chaîne/françois>
2. <http://localhost:3000/prenom?valeur=françois> à la place de <http://localhost:3000/prénom?valeur=françois>

Ceci est du au fait que lorsque l'on tape des urls en utf8, celles ci sont encodés en transformant les caractères non ASCII par des nombres précédés d'un `%`{.language-} : c'est [l'encodage %](https://fr.wikipedia.org/wiki/Encodage-pourcent).

On le voit dans le log console de la requête <http://127.0.0.1:3000/chaine/François> qui est  `Time: 19/09/2021 20:29:08 ; url : /chaine/Fran%C3%A7ois` : le `ç` a été transformé en `%C3%A7`.

Les paramètres (`françois`{.language-} dans le premier cas et `valeur=françois`{.language-} dans le second) sont automatiquement transformés en utf8 par node, mais **pas** l'url de la route :

{% attention %}
Une route qui aura comme base : `'/chaîne/:prenom'`{.language-} donnera tout le temps un 404. C'est la route `cha%C3%AEne/:prenom`{.language-} qui sera reconnue.
{% endattention %}

Pour ne pas à avoir à se rappeler des encodages, on pourra utiliser les fonction [encodeURI()](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/encodeURI) et [decodeURI](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/decodeURI) pour simplifier l'écriture d'url en utf8. Ainsi, dans notre cas, on aurait pu écrire :

```javascript
// ...

app.get(encodeURI(/chaîne/) + ':prenom', (req, res) => {
    console.log(req.params)
    res.end()
})

// ...
```

ou :

```javascript
// ...

app.get(encodeURI('/prenom'), (req, res) => {
    console.log(req.query)
    res.end()
})

// ...
```

pour écrire nos urls sans faute de Français.
