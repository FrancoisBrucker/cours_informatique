---
layout: page
title:  "Projet numérologie : niveau 1 - cours 1/intégration html/js"
category: cours
author: "François Brucker"
---

## Prérequis

Vos avez fini la [partie précédente]({% link cours/web/projets/numerologie/niveau-1/cours-1-front/front_html_css.md %}).

>Il n'est pas nécessaire pour suivre ce projet d'avoir de grandes connaissances en html/css, puisque tout vous sera donné à copier/coller. En revanche, une fois ce projet fait, il sera bon que vous suiviez l'[introduction du cours de web]({% link cours/web/index.md %}#introduction)


## structure du projet

### dossiers

* dossier : *"numerologie-niveau-1"* :
    * fichier : *"mes_tests.js"*
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
- [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
- [ ] modifier l'arbre DOM avec du texte.
- [ ] récupérer un info de l'url et la traiter


Jouer avec la touche entrée, est peut-être un peu compliqué. On va donc ajouter un todo (qu'on va faire de suite) qui consistera à récupérer le texte de l'*input* lorsque l'on appuie sur le bouton.

- [X] associer un chiffre à un nom
    - [X] ~~numéro unicode/utf8 d'un caractère~~
    - [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
    - [X] ~~sommer les chiffre d'un nombre~~
    - [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
- [X] ~~créer un champ texte dans un fichier html~~
- [X] ~~ajouter du style dans le html.~~
- [X] ~~inclure une bibliothèque css~~
- [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
- [X] récupérer l'input en appuyant sur le button.
- [ ] modifier l'arbre DOM avec du texte.
- [ ] récupérer un info de l'url et la traiter


## buttons

Le javascript en web est fait pour réagir à des évènement se produisant, comme de cliquer sur un bouton. 

On a plusieurs choses à faire :
1. trouver le bouton
2. greffer du code qui s'exécutera lorsque l'on cliquera sur le bouton
3. trouver le texte à récupérer

POur récupérer des objets de l'arbre DOM, le plus simple est de les identifier de façon unique en utilisant un `id`. 

Regardons la page *"numerologie-niveau-1/index.html"* actuelle : 
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
                <input type="text"/>

                <button type="submit" class="pure-button pure-button-primary">Envoi</button>
            </form>
            <div class="pure-g">
                <div class="pure-u-1-3"></div>
                <div class="pure-u-1-3"><p>7</p></div>
                <div class="pure-u-1-3"></div>
            </div>
        </div>
    </body>
</html>
```

### identifiants 

Ajoutons des identifiants au bouton et à l'input en utilisant l'attribut `id` : 

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
                <div class="pure-u-1-3"><p>7</p></div>
                <div class="pure-u-1-3"></div>
            </div>
        </div>
    </body>
</html>
```

### console 
Affichez le fichier html dans un navigateur chrome et ouvrez les outils de développement et placez vous dans la console (*menu afficher > options pour les développeurs > outils de développement* puis choisissez le panel *console*). La console correspond à l'interpréteur javascript de la page, on peut y voir tout ce qu'on veut par exemple tapez y :

```javascript
document.querySelector("#input-form").value
```
Et vous y découvrirez la valeur de votre input. 

> Changez la valeur de l'input et vérifiez que la ligne précédente donne un autre résultat
{: .note}

On a utilisé plusieurs choses :
* [`document.querySelector`](https://developer.mozilla.org/fr/docs/Web/API/Document/querySelector) qui permet de retrouver un élément de l'arbre DOM par son identifiant (il faut mettre un `#` devant l'identifiant)
* l'attribut `value` d'un input qui donne sa valeur.


Il faut maintenant réussir à faire ça lorsque l'on clique sur un bouton. 

### évènements

> <https://developer.mozilla.org/fr/docs/Learn/JavaScript/Building_blocks/Events>

Dès qu'il se passe quelque chose sur la page, un évènement est lancé. Ici, pour le bouton, c'est lorsque l'on clique dessus. On va donc se greffer à cet évènement : 

```javascript
document.querySelector("#button-form").addEventListener("click", (event) => {
    console.log(document.querySelector("#input-form").value)
    event.preventDefault()
})
```

Il se lit comme ça : 
1. on récupère (comme avant) le bouton. 
2. on ajoute une fonction qui fa être exécuté lors de l'évènement "click"

> La notation [`(param) => {code}` crée une fonction javascript](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Functions#utiliser_une_expression_de_fonction_fl%C3%A9ch%C3%A9e_).


Testons ça dans notre html :

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
                <div class="pure-u-1-3"><p>7</p></div>
                <div class="pure-u-1-3"></div>
            </div>
        </div>

        <script>
            document.querySelector("#button-form").addEventListener("click", (event) => {
                chaine = document.querySelector("#input-form").value;
                console.log(chaine);
                event.preventDefault();
            })
        </script>
    </body>
</html>
```

Dès que vous cliquerez sur le bouton, la valeur sera envoyée dans la console. 

> Testez le !
{: .node}

> On a ajouté une ligne, peu utilise actuellement mais qui ne fait pas d mal dans le doute,  qui empêche le comportement par défaut du clique sur un bouton (`event.preventDefault()`)

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
- [ ] modifier l'arbre DOM avec du texte.
- [ ] récupérer un info de l'url et la traiter


### association du chiffre au nom

Que faire avec la valeur du champ `<input>` ? Ben lui associer le chiffre numérologique pardi. Sauf qu'on ne l'a pas mis dans notre todo liste.... Ajoutons le et occupons-en nous :


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
- [X] utiliser le code numerologie.js dans le html
- [ ] modifier l'arbre DOM avec du texte.
- [ ] récupérer un info de l'url et la traiter


Là c'est simple : 

1. on lit notre fichier javascript dans le html
2. on utilise ensuite la fonction `chiffreAssocie` 

Faisons le : 

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
                <div class="pure-u-1-3"><p>7</p></div>
                <div class="pure-u-1-3"></div>
            </div>
        </div>

        <script src="numerologie.js"></script>
        <script>
            document.querySelector("#button-form").addEventListener("click", (event) => {
                chaine = document.querySelector("#input-form").value
                console.log(chaine)
                console.log(chiffreAssocie(chaine))
                event.preventDefault()
            })
        </script>
    </body>
</html>
```

* on charge un sript avec la balise script en mettant le chemin relatif du fichier chargé dans l'attribut `src`. Il ne faut rien mettre d'autre dans la balise script
* on a mis le code tout à la fin pour être sur que les éléments html soient visible.

### modification du html

Il nous reste à changer le chiffre. C'est aussi simple :

1. on met par défaut `?`comme valeur (pour l'instant c'est 7)
2. on ajoute un identifiant au paragraphe contenant le chiffre
3. on le modifie celui ci lorsque l'on clique sur le bouton.

Modifions le html pour avoir un identifiant et une valeur par défaut au paragraphe :

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
                console.log(chaine)
                console.log(chiffreAssocie(chaine))
                event.preventDefault()
            })
        </script>
    </body>
</html>
```

> Chargez le html actuel et ouvrez la console dans les outils de développement.
{: .note}

Pour un paragraphe, son contenu est décrit dans l'attribut `textContent`. C'est donc lui qu'il faut modifier.

> Tapez : `document.querySelector("#chiffre-valeur").textContent` dans la console puis appuyez sur la touche entrée
{: .note}

Vous devriez voir `'?'`.

> Tapez : `document.querySelector("#chiffre-valeur").textContent = 5` dans la console puis appuyez sur la touche entrée
{: .note}

L'affichage du paragraphe a changé !

> Toutes les balises html se comportent différemment (pour un input c'est l'attribut `value` pour un paragraphe c'est `textContent` qui contient la valeur...) : il faut toujours se référer à la documentation et tester dans la console avant de se lancer dans du code.

Il ne nous reste plus qu'à modifier tout ça dans notre html : 

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

## Fin

On va s'arrêter là. Comme on le voit on a pas pu traiter le cas de la touche entrée (c'estpour aller plus loin), ni le traitement de l'url qui sera pour le prochain cours.

