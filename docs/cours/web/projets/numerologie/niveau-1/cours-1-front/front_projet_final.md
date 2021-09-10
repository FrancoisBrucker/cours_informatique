---
layout: page
title:  "Projet numérologie : niveau 1 - cours 1/projet final"
category: cours
author: "François Brucker"
---


## structure du projet

### dossiers

* dossier : *"numerologie-niveau-1"* :
    * fichier : *"numerologie.js"*
    * fichier : *"index.html"*
    * fichier : *"main.css"*
    * dossier : *"user stories"*
      * fichier : *"connaitre-son-numero.md"*
      * fichier : *"todo.md"*
    * dossier : *"tests"*
      * fichier : *"tests_numerologie.js"*

### todos

- [X] associer un chiffre à un nom
    - [X] ~~numéro unicode/utf8 d'un caractère~~
    - [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
    - [X] ~~sommer les chiffre d'un nombre~~
    - [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
- [X] ~~créer un champ texte dans un fichier html~~
- [X] ~~ajouter du style dans le html.~~
- [X] ~~inclure une bibliothèque css~~
- [X] ~~récupérer l'input en appuyant sur le button.~~
- [X] ~~utiliser le code numerologie.js dans le html~~
- [X] ~~modifier l'arbre DOM avec du texte.~~
- [ ] récupérer un info de l'url et la traiter
- [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée


## fichiers 

### *"numerologie-niveau-1/index.html"*

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
                <input type="text" id="input-form" />

                <button type="submit" id="button-form" class="pure-button pure-button-primary">Envoi</button>
            </form>
            <div class="pure-g">
                <div class="pure-u-1-3"></div>
                <div class="pure-u-1-3"><p id="chiffre-valeur">?</p></div>
                <div class="pure-u-1-3"></div>
            </div>
        </div>

        <script src="numerologie.js"></script>
        <script>
            document.querySelector("#button-form").addEventListener("click", (event) => {
                chaine = document.querySelector("#input-form").value
                if (chaine) {
                    document.querySelector("#chiffre-valeur").textContent = chiffreAssocie(chaine)
                } else {
                    document.querySelector("#chiffre-valeur").textContent = '?'
                }
                event.preventDefault()
            })
        </script>
    </body>
</html>
```

### *"numerologie-niveau-1/main.css"*

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

### *"numerologie-niveau-1/numerologie.js"*

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

### *"numerologie-niveau-1/user stories/connaitre-son-numero.md"*

```markdown
# connaître son numéro

## page générale

1. je rentre mon nom dans un champ texte : François puis j'appuie sur la touche entrée.
2. En dessous du champ texte, on affiche alors Bonjour François, votre numéro est le X

X est écrit en gros au milieu de la page.

## page du numéro

<http://localhost/prénom/XXXX>

doit rendre le numéro associé à XXXX
```

### *"numerologie-niveau-1/user stories/todo.md"*

```markdown

- [X] associer un chiffre à un nom
    - [X] ~~numéro unicode/utf8 d'un caractère~~
    - [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
    - [X] ~~sommer les chiffre d'un nombre~~
    - [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
- [X] ~~créer un champ texte dans un fichier html~~
- [X] ~~ajouter du style dans le html.~~
- [X] ~~inclure une bibliothèque css~~
- [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
- [X] ~~récupérer l'input en appuyant sur le button.~~
- [X] ~~utiliser le code numerologie.js dans le html~~
- [X] ~~modifier l'arbre DOM avec du texte.~~
- [ ] récupérer un info de l'url et la traiter
```
