---
layout: layout/post.njk
title: "Projet numérologie / partie 1 : front / niveau 1 / code html&css"

authors:
    - "François Brucker"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Codage de la page web.

<!-- fin résumé -->

Il n'est pas nécessaire d'avoir de connaissances en html/css, puisque tout vous sera donné à copier/coller. En revanche, une fois ce projet fait, il sera bon que vous (re)suiviez le [cours de web]({{"/cours/web" }})

## <span id="tache-1"></span> Tâche 1 : squelette de la page html

Créez un fichier `numérologie/index.html`{.fichier} :

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

* des balises l'une ouvrante et l'autre fermante (le même nom avec un `/`{.language-} avant, comme html) pour une balise donnée.
* Tout ce qui est à l'intérieur d'une balise sont ses *enfants*. L'élément le plus *ancien*, aussi appelé *racine* est la balise `<html></html>`{.language-}, Cette structure crée ce que l'on appelle [l'arbre DOM](https://la-cascade.io/le-dom-cest-quoi-exactement/).
* certaines balises sont *auto-fermante* (elles ne nécessitent pas de balise fermante), comme `<input />`{.language-} par exemple (la balise est fermée avec le `/`{.language-} après l'ouverture).
* on appelle attribut de la balise ce qui est à l'intérieur de la balise ouvrante, la structure d'un attribut est `nom="valeur"`{.language-} (les `"`{.language-} sont obligatoires pour délimiter les valeurs des attributs.

Les nom des balises sont importantes, elles définissent leurs fonctions. Par exemple :

* la balise `doctype`{.language-} nous indique ce qu'est ce fichier. Ici, c'est de l'html.
* une balise `<html></html>`{.language-} qui contient 2 toujours uniquement enfants :
  * `<head></head>`{.language-} qui contient des informations générale de la page
  * `<body></body>`{.language-} qui est le corps de la page et contiendra par là toutes les informations à afficher.

{% faire %}
Glisser/déposez le fichier `numérologie/index.html`{.fichier} depuis l'explorateur de fichier vers une fenêtre chrome pour que chrome interprète votre fichier (vous pouvez aussi taper *ctrl+o* sous windows ou *menu Fichier > ouvrir le fichier* sous mac).
{% endfaire %}

Bon c'est un peu nul mais on voit bien les différentes *balises* html :

* le titre (c'est sur l'onglet du fichier) : c'est la balise `<title></title>`{.language-}
* le formulaire : c'est la balise `<form></form>`{.language-}. Remarquez qu'il y 3 *enfants* à ce formulaire :
  * `<label></label>`{.language-} qui est un label,
  * `<input></input>`{.language-} qui est l'endroit où on peut écrire des choses
  * `<button></button>`{.language-} qui est le bouton pour envoyer les données.
* un paragraphe, balise `<p></p>`{.language-}, qui contient un chiffre bidon, ici 7.

{% info %}
La plupart des balises peuvent être en plusieurs exemplaires, comme plusieurs paragraphes `<p></p>`{.language-} ou plusieurs formulaires `<form></form>`{.language-}. En revanche, il ne doit y avoir qu'une seule balise `<html></html>`{.language-}, `<head></head>`{.language-} et `<body></body>`{.language-}.
{% endinfo %}

## <span id="tache-2"></span> Tâche 2 : css

Le [css](https://developer.mozilla.org/fr/docs/Learn/CSS/First_steps) est un langage déclaratif permettant d'associer un style à une balise. Donnons un peu de style à notre page html.

{% info %}
Notez que la page, même moche a déjà du style. Le paragraphe par exemple n'est pas collé au formulaire et le texte a une police de caractère. Toutes ces styles par défaut sont donné parle navigateur.
{% endinfo %}

### <span id="tache-2.1"></span> Style dans la page html

Modifions notre fichier html pour y inclure du style, grâce à la balise `<style></style>`{.language-}, que l'on met usuellement dans la balise `<head></head>`{.language-} :

Ajoutons le style au fichier `numérologie/index.html`{.fichier} :

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

On a ajouté une balise inconnue pour l'instant : la balise `<div></div>`{.language-}. C'est une balise sans signification proprement dite et qui est utilisée pour structurer la page.

Vous voyez que les propriétés css se lisent bien :

```css
qui {
  quoi: comment;
}
```

`qui`{.language-} peut prendre deux formes :

* le nom d'une balise : `p`{.language-} ou `body`{.language-} dans l'exemple
* le nom d'une classe précédé d'un `.`{.language-} : `main`{.language-} dans l'exemple.

{% info %}
Il n'est pas nécessaire de mettre la balise `<style></style>`{.language-} dans la balise `<head></head>`{.language-}, on peut
a priori la mettre partout, mais le style ne sera connu qu'une fois lu. Donc si vous mettez du style pour un paragraphe après celui-ci, il ne sera pas reconnu.
{% endinfo %}

Les possibilités de style sont [très nombreuses](https://developer.mozilla.org/fr/docs/Web/CSS/Reference).

### <span id="tache-2.2"></span> Feuille de style séparée du html

On a souvent coutume de placer le fichier css dans un fichier à côté pour pas qu'il *pollue* le fichier html. En effet, ces petites bêtes là deviennent vite très grosses.

Créez un fichier `numérologie/main.css`{.fichier} :

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

Et on modifie le fichier `numérologie/index.html`{.fichier} pour qu'il puisse lire le fichier de style grâce à la balise [`<link />`{.language-}](https://developer.mozilla.org/fr/docs/Web/HTML/Element/link):

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

La balise `<link>`{.language-} qui va chercher le fichier css. L'emplacement du fichier est décrit de [façon relative]({{ "/tutoriels/fichiers-navigation"  }}#block-.-..), par rapport à l'emplacement du fichier html sur le disque dur. Ici c'est simple c'est dans le même dossier.

## <span id="tache-3"></span> Tâche 3 : bibliothèque css

On ne va pas loin si on fait uniquement son propre css. L'usage veut que l'on utilise des bibliothèques css. il en existe plein. Nous allons ici utiliser une bibliothèque minimale : <https://purecss.io/>

Sur son site, on voit commet l'utiliser : il suffit de la récupérer via une balise link. Notez qu'ici le lien n'est pas sur notre disque dur mais sur le réseau puisque c'est une [url]({{ "/cours/web/anatomie-url"  }}) qui est utilisée.

{% info %}
Normalement, une bibliothèque css va définir plein de classes que l'on pourra utiliser pour ses pages. Elles vont servir à mettre de jolies couleurs ou à organiser les pages (le *layout*).
{% endinfo %}

Re-modifions le fichier `numérologie/index.html`{.fichier} pour y inclure un lien vers la bibliothèque :

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

Une fois <https://purecss.io/> chargé, on peut utiliser les classes qu'elle a définie (qui commencent toutes par `pure-`). On a utilisé le layout en [grids](https://purecss.io/grids/) et des modifications du formulaire et du bouton.

{% info %}
Notez que l'on met **toujours** ses propres css à la fin, car les propriétés sont appliquées dans l'ordre où elles sont lues, les nôtres seront donc toujours appliquées, car en dernier.
{% endinfo %}
