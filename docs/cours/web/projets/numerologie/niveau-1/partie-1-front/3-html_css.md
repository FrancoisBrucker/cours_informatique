---
layout: page
title:  "Projet numérologie : niveau 1/partie 1/html et css"
category: cours
author: "François Brucker"
---

> [numérologie]({% link cours/web/projets/numerologie/index.md %})/[niveau 1]({% link cours/web/projets/numerologie/niveau-1/index.md %})/[partie 1]({% link cours/web/projets/numerologie/niveau-1/partie-1-front/index.md %})/[html et css]({% link cours/web/projets/numerologie/niveau-1/partie-1-front/3-html_css.md %})
{: .chemin}

Codage de la page web.

Il n'est pas nécessaire d'avoir de connaissances en html/css, puisque tout vous sera donné à copier/coller. En revanche, une fois ce projet fait, il sera bon que vous suiviez les tutoriaux de l'[introduction du cours de web]({% link cours/web/index.md %}#introduction)

## Tâche 1 : squelette de la page html {#tache-1}

Créez un fichier *"numerologie/index.html"* :

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

Petite analyse de ce qu'est un fichier html :

* des balises l'une ouvrante et l'autre fermante (le même nom avec un `/` avant, comme html) pour une balise donnée.
* Tout ce qui est à l'intérieur d'une balise sont ses *enfants*. Le l'léménet le plus *ancien*, aussi appelé *racine* est la balise `<html></html>`, Cette structure crée ce que l'on appelle [l'arbre DOM](https://la-cascade.io/le-dom-cest-quoi-exactement/).
* certaines balises sont *auto-fermante* (elles ne nécessitent pas de balise fermante), comme `<input />` par exemple (la balise est fermée avec le `/` après l'ouverture).
* on appelle attribut de la balise ce qui est à l'intérieur de la balise ouvrante, la structure d'un attribut est `nom="valeur"` (les `"` sont obligatoires pour délimiter les valeurs des attributs.

Les nom des balises sont importantes, elles définissent leurs fonctions. Par exemple :
* la balise `doctype` nous indique ce qu'est ce fichier. Ici, c'est de l'html.
* une balise `<html></html>` qui contient 2 toujours uniquement enfants :
  * `<head></head>` qui contient des informations générale de la page
  * `<body></body>` qui est le corps de la page et contiendra par là toutes les informations à afficher.

> Glisser/déposez le fichier *"numerologie/index.html"* depuis l'explorateur de fichier vers une fenêtre chrome pour que chrome interprète votre fichier (vous pouvez aussi taper *ctrl+o* souq windows ou *menu Fichier > ouvrir le fichier* sous mac).
{: .note}

Bon c'est un peu nul mais on voit bien les différentes *balises* html :

* le titre (c'est sur l'onglet du fichier) : c'est la balise `<title></title>`
* le formulaire : c'est la balise `<form></form>`. Remarquez qu'il y 3 *enfants* à ce formulaire : 
  * `<label></label>` qui est un label,
  * `<input></input>` qui est l'endroit où on peut écrire des choses
  * `<button></buton>` qui est le bouton pour envoyer les données.
* un paragraphe, balise `<p></p>`, qui contient un chiffre bidon, ici 7.

> La plupart des balises peuvent être en plusieurs exemplaires, comme plusieurs paragraphes `<p></p>` ou plusieurs formulaires `<form></form>`. En revanche, il ne doit y avoir qu'une seule balise `<html></html>`, `<head></head>` et `<body></body>`.

## Tâche 2 : css {#tache-2}

Le [css](https://developer.mozilla.org/fr/docs/Learn/CSS/First_steps) est un langage déclaratif permettant d'associer un style à une balise. Donnons un peu de style à notre page html.

> Notez que la page, même moche a déjà du style. Le paragraphe par exemple n'est pas collé au formulaire et le texte a une police de caractère. Toutes ces styles par défaut sont donné parle navigateur.

### style dans la page html

Modifions notre fichier html pour y inclure du style, grâce à la balise `<style></style>`, que l'on met usuellement dans la balise `<head></head>` :

Ajoutons le style au fichier *"numerologie/index.html"* :

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
              <input type="text"/>

              <button type="submit">Envoi</button>
          </form>
          <p>7</p>
        </div>
    </body>
</html>
```

Actualiser votre page en cliquant sur la flèche en rond à gauche de la barre d'url (ou *ctrl+R* sous windows ou *cmd+r* sous mac). Tout doit avoir changé !

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

Les possibilités de style sont [très nombreuses](https://developer.mozilla.org/fr/docs/Web/CSS/Reference). 

### feuille de style séparée du html

On a souvent coutume de placer le fichier css dans un fichier à côté pour pas qu'il *pollue* le fichier html. En effet, ces petites bêtes là deviennent vite très grosses.

Créez un fichier *"numerologie/main.css"* :

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

Et on modifie le fichier *"numerologie/index.html"* pour qu'il puisse lire le fichier de style grâce à la balise [`<link />`](https://developer.mozilla.org/fr/docs/Web/HTML/Element/link):

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

La balise `<link>` qui va chercher le fichier css. L'emplacement du fichier est décrit de [façon relative]({% post_url tutos/systeme/2021-08-24-fichiers-navigation %}#block-.-..), par rapport à l'emplacement du fichier html sur le disque dur. Ici c'est simple c'est dans le même dossier.

## Tâche 3 : bibliothèque css {#tache-3}

On ne va pas loin si on fait uniquement son propre css. L'usage veut que l'on utilise des bibliothèques css. il en existe plein. Nous allons ici utiliser une bibliothèque minimale : <https://purecss.io/>

Sur son site, on voit commet l'utiliser : il suffit de la récupérer via une balise link. Notez qu'ici le lien n'est pas sur notre disque dur mais sur le réseau puisque c'est une [url]({% link cours/web/tuto_url.md %}) qui est utilisée.

> normalement, une bibliothèque css va définir plein de classes que l'on pourra utiliser pour ses pages. Elles vont servir à mettre de jolies couleurs ou à organiser les pages (le *layout*).

Re-modifions le fichier *"numerologie/index.html"* pour y inclure un lien vers la bibliothèque :

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

Une fois <https://purecss.io/> chargé, on peut utiliser les classes qu'elle a définie (qui commencent toutes par `pure-`). On a utilisé le layout en [grids](https://purecss.io/grids/) et des modifications du formulaire et du boutton.

>Notez que l'on met **toujours** ses propres css à la fin, car les propriétés sont appliquées dans l'ordre où elles sont lues, les nôtres seront donc toujours appliquées, car en dernier.
