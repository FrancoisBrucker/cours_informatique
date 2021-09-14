---
layout: page
title:  "Projet numérologie : niveau 1 - cours 1/code html/css"
category: cours
author: "François Brucker"
---

## Prérequis

Vos avez fini la [partie précédente]({% link cours/web/projets/numerologie/niveau-1/cours-1-front/front_code_js.md %}).

>Il n'est pas nécessaire pour suivre ce projet d'avoir de grandes connaissances en html/css, puisque tout vous sera donné à copier/coller. En revanche, une fois ce projet fait, il sera bon que vous suiviez l'[introduction du cours de web]({% link cours/web/index.md %}#introduction)


## structure du projet

### dossiers

* dossier : *"numerologie-niveau-1"* :
    * fichier : *"mes_tests.js"*
    * fichier : *"numerologie.js"*
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
- [ ] créer un champ texte dans un fichier html
- [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
- [ ] modifier l'arbre DOM avec du texte.
- [ ] récupérer un info de l'url et la traiter


## site, première mouture

On va commencer par coder la structure du projet, c'est à dire faire l'html :

- [X] associer un chiffre à un nom
    - [X] ~~numéro unicode/utf8 d'un caractère~~
    - [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
    - [X] ~~sommer les chiffre d'un nombre~~
    - [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
- [X] créer un champ texte dans un fichier html
- [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
- [ ] modifier l'arbre DOM avec du texte.
- [ ] récupérer un info de l'url et la traiter

### html

Créez un fichier *"*"numerologie-niveau-1/index.html* : 


```html
<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Numérologie</title>
    </head>
    <body>
        <form>
            <label>Prénom :</label>
            <input type="text"/>

            <button type="submit">Envoi</button>
        </form>
        <p>7</p>
    </body>
</html>
```

Un fichier html a toujours :
* des balises ouvrante et fermante (le même nom avec un `/` avant, comme html). C'est comme ça qu'il est structuré, en arbre avec comme racine la balise <html> contenant tout le reste. On appelle ça l'[arbre DOM](https://la-cascade.io/le-dom-cest-quoi-exactement/).
* certaines balises sont *auto-fermante* (elles ne nécessitent pas de balise fermante), comme `<input />` par exemple (la balise est fermée avec le `/` après l'ouverture). 
* un type : ici c'est du html (c'est le doctype qui nous le dit)
* une balise <html></html> qui contient 2 enfants :
  * <head></head> qui contient des informations générale de la page
  * <body></body> qui est le corps de la page et contiendra par là toutes les informations à afficher.


On peut voir à quoi il ressemble dans chrome en l'ouvrant : *menu fichier > ouvrir le fichier*. Bon c'est un peu nul mais on voit bien les différentes *balises* html :
* le titre (c'est sur l'onglet du fichier) : c'est la balise `<title></title>`
* le formulaire : c'est la balise `<form></form>`. Remarquez qu'il y 3 *enfants* à ce formulaire : `<label></label>` qui est un label, `<input></input>` qui est l'endroit où on peut écrire des choses et `<button></buton>` qui est le bouton pour envoyer les données.
* un paragraphe `<p></p>`.

> Comme c'est moche et qu'on est des esthètes, on va ajouter des choses au todo :

- [X] associer un chiffre à un nom
    - [X] ~~numéro unicode/utf8 d'un caractère~~
    - [X] ~~sommer des numéro des caractères d'une chaine de caractères~~
    - [X] ~~sommer les chiffre d'un nombre~~
    - [X] ~~sommer itérativement jusqu'à convergence (car $10x + y > x+y$ si $x > 0$)~~
- [X] ~~créer un champ texte dans un fichier html~~
- [ ] ajouter du style dans le html.
- [ ] inclure une bibliothèque css
- [ ] récupérer en html le contenu d'un champ texte lorsque l'on appuie sur la touche entrée
- [ ] modifier l'arbre DOM avec du texte.
- [ ] récupérer un info de l'url et la traiter

## css

Le [css](https://developer.mozilla.org/fr/docs/Learn/CSS/First_steps) est un langage déclaratif permettant d'associer un style à une balise.

D'après notre user story, le chiffre doit être en gros et au milieu.

### css dans la page


Modifions notre fichier html pour y inclure du style, grâce à la balise `<style></style>`, que l'on mets usuellement dans la balise `<head></head>` : 

*"numerologie-niveau-1/index.html"* : 
```html
<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Numérologie</title>

        <style>
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
        </style>
    </head>
    <body>
        <div class="main">
          <form>
              <label>Prénom :</label>
              <input type="text" name="prenom"/>

              <button type="submit">Envoi</button>
          </form>
          <p>7</p>
        </div>
    </body>
</html>
```

On a ajouté une balise inconnue pour l'instant : la balise `<div></div>`. C'est une balise sans signification proprement dite et qui est utilisée pour structurer la page.

Vous voyez que les propriétés css se lisent bien : 
```
qui {
  quoi: comment;
}
```

`qui` peut prendre deux formes : 

* le nom d'une balise : `p`ou `body` dans l'exemple
* le nom d'une classe précédé d'un `.` : `main` dans l'exemple.

> Il n'est pas nécessaire de mettre la balise `<style></style>` dans la balise `<head></head>`, on peut
> a priori la mettre partout, mais le style ne sera connu qu'une fois lu. Donc si vous mettez du style pour un paragraphe après celui-ci, il ne sera pas reconnu.

> Comprenez comment fonctionne le style.
{: .note}

### css chargé

On a souvent coutume de placer le fichier css dans un fichier à côté pour pas qu'il *pollue* le fichier html. En effet, ces petites bêtes là deviennent vite très grosses.

Donc créez un fichier *"numerologie-niveau-1/main.css"* :

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

Et on modifie le fichier *"numerologie-niveau-1/index.html"* pour qu'il puisse lire le fichier de style :

```html
<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Numérologie</title>

        <link href="./main.css" rel="stylesheet"/>
    </head>
    <body>
        <div class="main">
          <form>
              <label>Prénom :</label>
              <input type="text"/>

              <button type="submit">Envoi</button>
          </form>
          <p>7</p>
        </div>
    </body>
</html>
```

> Voyez la balise `<link>` qui va chercher le fichier css. L'emplacement du fichier est décrit de [façon relative]({% post_url tutos/systeme/2021-08-24-fichiers-navigation %}#block-.-..), par rapport à l'emplacement du fichier html sur le disque dur. Ici c'est simple c'est dans le même dossier.

### bibliothèque css

ON ne va pas loin si on fait uniquement son propre css. L'usage veut que l'on utilise des bibliothèques css. il en existe plein. Nous allons ici utiliser une bibliothèque minimale : <https://purecss.io/>

Sur son site, on voit commet l'utiliser : il suffit de la récupérer via une balise link. Notez qu'ici le lien n'est pas sur notre disque dur mais sur le réseau puisque c'est une [url]({% link cours/web/tuto_url.md %}) qui est utilisée.

> normalement, une bibliothèque css va définir plein de classes que l'on pourra utiliser pour ses pages. Elles vont servir à mettre de jolies couleurs ou à organiser les pages (le *layout*).

Remodifions le fichier *"numerologie-niveau-1/index.html"* : 
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

> Comprenez ce que nous avons fait. On a utilisé le layout en [grids](https://purecss.io/grids/) 
> de <https://purecss.io/> et des modification de forme du button.
{: .note}

>Notez que l'on met **toujours** ses propres css à la fin, car les propriétés sont appliquées dans l'ordre où elles sont lues, les nôtres seront donc toujours appliquées, car en dernier.



### mais que fait la police ?

Allez, pour la bonne bouche on va changer la police en utilisant les <https://fonts.google.com/>.

Dans le *"numerologie-niveau-1/main.css"*, on a modifié le `p` pour qu'il utilise une autre fonte :
```css
p {
    font-size: 100px;
    font-family: 'Lobster', cursive;
}
```

Et on a chargé la fonte dans le <head></head> du html en ajoutant le lien :
```html
<link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet">
```

## et la suite ?

### todo

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

On a fini tout le html. I va nous rester à mixer html et js dans [la dernière partie de ce projet]({% link cours/web/projets/numerologie/niveau-1/cours-1-front/front_html_js.md %})