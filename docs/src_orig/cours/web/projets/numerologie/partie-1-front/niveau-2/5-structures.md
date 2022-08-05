---
layout: page
title:  "Projet numérologie : partie 1 / niveau 2 / structures"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %}) / [partie 1]({% link cours/web/projets/numerologie/partie-1-front/index.md %}) / [niveau 2]({% link cours/web/projets/numerologie/partie-1-front/niveau-2/index.md %}) / [structures]({% link cours/web/projets/numerologie/partie-1-front/niveau-2/5-structures.md %})
{: .chemin}

## structure du projet

* dossier : *"numerologie"* :  
  * fichier : *"mes_tests.js"*
  * fichier : *"numerologie.js"*
  * fichier : *"index.html"*
  * fichier : *"main.css"*
  * dossier : *"user-stories"*
    * fichier : *"connaitre-son-numero.md"*
    * fichier : *"url-numero.md"*
  * dossier : *"todo"*
    * fichier : *"todos.md"*
  * dossier : *"tests"*
    * fichier : *"tests_numerologie"*

## fichiers

### *"numerologie/mes_tests.js"*

```javascript
nom = "monde"

console.log("bonjour " + nom + " !")
```

### *"numerologie/numerologie.js"*

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
```

### *"numerologie/index.html"*

```html
<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Numérologie</title>
        
        <link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet">
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
    </body>
</html>
```

### *"numerologie/main.css"*

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
    font-family: 'Lobster', cursive;
}
```

### *"numerologie/user-stories/connaitre-son-numero.md"*

```markdown
 connaître son numéro

## page générale

1. je rentre mon nom dans un champ texte : François puis j'appuie sur la touche entrée.
2. En dessous du champ texte, on affiche alors Bonjour François, votre numéro est le X

## style 

X est écrit en gros au milieu de la page. Avec, si possible une fonte rigolote.
```

### *"numerologie/user-stories/url-numero.md"*

```markdown
# url du numéro

<http://localhost/prénom/XXXX>

Le retour de cette url doit être le numéro associé au prénom : XXXX
```

### *"numerologie/todo/todos.md"*

```markdown
# Todos

On mettra un 'X' dans la checkbox pour l'item courant
on ~~barrera~~ lorsque cette item sera réalisé

* [X] associer un chiffre à un nom
  * [X] ~~numéro unicode/utf8 d'un caractère~~
  * [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
  * [X] ~~sommer les chiffre d'un nombre~~
  * [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
* [X] ~~créer un champ texte dans un fichier html~~
* [X] ~~ajouter du style dans le html~~
* [X] ~~inclure une bibliothèque css~~
* [X] ~~police de caractère spéciale pour le chiffre~~
* [X] ~~récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée~~
* [X] ~~récupérer l'input en appuyant sur le `button`~~
* [X] ~~modifier l'arbre DOM avec du texte~~
* [X] ~~utiliser le code numerologie.js dans le html~~
```

### *"numerologie/tests/tests_numerologie.js"*

```javascript
fs = require('fs')

eval(fs.readFileSync("../numerologie.js", {encoding:'utf8'}))

// test de nombre(chaine)
console.log("test de nombre(chaine)")

// est-ce 2x plus ?
console.log(nombre("cou"))
console.log(nombre("coucou"))

// chaque caractère :la somme est-elle correcte ?
for (c of "cou") { 
    console.log(c + " : " + nombre(c))
}
// fin de test de nombre(chaine)

// test de somme(nombre)
console.log("test de somme(nombre)")

console.log(somme(132))

// avec un chiffre : charAt != charCodeAt
console.log(somme(4))
console.log("4".charCodeAt(0))
console.log("4".charAt(0))

// conversion chaine de caracteres et nombre
console.log(typeof "4".charAt(0))
console.log(parseInt("4".charAt(0)))
console.log(typeof parseInt("4".charAt(0)))
// fin de test de somme(nombre)

// test de chiffreAssocie(chaine)
console.log("test de chiffreAssocie(chaine)")

//test valeur somme des chiffres
console.log(nombre("coucou"))
console.log(chiffreAssocie("coucou"))
// fin de test de chiffreAssocie(chaine)
```
