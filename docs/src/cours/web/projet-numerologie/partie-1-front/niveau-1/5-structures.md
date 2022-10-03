---
layout: layout/post.njk
title: "Projet numérologie / partie 1 : front / niveau 1 / structures"

authors:
    - "François Brucker"


eleventyNavigation:
  key: "Projet numérologie / partie 1 : front / niveau 1 / structures"
  parent: "Projet numérologie / partie 1 : front / niveau 1"
---

<!-- début résumé -->

Code complet après la partie 1.

<!-- fin résumé -->

## Dépôt git

<https://github.com/FrancoisBrucker/numerologie/releases/tag/partie-1-niveau-1-fin>

## Structure du projet

* dossier : `numerologie`{.fichier} :
  * fichier : `mes_tests.js`{.fichier}
  * fichier : `numerologie.js`{.fichier}
  * fichier : `index.html`{.fichier}
  * fichier : `main.css`{.fichier}

## Fichiers

### `numerologie/mes_tests.js`{.fichier}

```javascript
nom = "monde"

console.log("bonjour " + nom + " !")
```

### `numerologie/numerologie.js`{.fichier}

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

// // test de nombre(chaine)

// // est-ce 2x plus ?
// console.log(nombre("cou"))
// console.log(nombre("coucou"))

// // chaque caractère :la somme est-elle correcte ?
// for (c of "cou") { 
//     console.log(c + " : " + nombre(c))
// }
// // fin de test de nombre(chaine)

// // test de somme(nombre)
// console.log(somme(132))

// // avec un chiffre : charAt != charCodeAt
// console.log(somme(4))
// console.log("4".charCodeAt(0))
// console.log("4".charAt(0))

// // conversion chaine de caracteres et nombre
// console.log(typeof "4".charAt(0))
// console.log(parseInt("4".charAt(0)))
// console.log(typeof parseInt("4".charAt(0)))
// // fin de test de somme(nombre)

// // test de chiffreAssocie(chaine)

// //test valeur somme des chiffres
// console.log(nombre("coucou"))
// console.log(chiffreAssocie("coucou"))
// // fin de test de chiffreAssocie(chaine)
```

### `numerologie/index.html`{.fichier}

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
        <script src="./numerologie.js"></script>
        <script>
            document.querySelector("#form-button").addEventListener("click", (event) => {
                chaine = document.querySelector("#form-input").value;
                chiffre = chiffreAssocie(chaine);
                document.querySelector("#chiffre").textContent = chiffre;
                event.preventDefault();
            })
        </script>
    </body>
</html>
```

### `numerologie/main.css`{.fichier}

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
