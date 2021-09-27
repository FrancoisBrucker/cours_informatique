---
layout: page
title:  "Projet commentaires : partie 1 / front"
category: cours
author: "François Brucker"
---

> [commentaires]({% link cours/web/projets/commentaires/index.md %}) / [partie 1]({% link cours/web/projets/commentaires/partie-1-site/index.md %}) / [front]({% link cours/web/projets/commentaires/partie-1-site/2-front.md %})
{: .chemin}

On va créer le site front en utilisant (un peu) la bibliothèque front [bootstrap](https://getbootstrap.com/).

## bootstrap

Il existe de nombreux tutos de bootstrap, en particulier la [documentation officielle](https://getbootstrap.com/docs/5.1/getting-started/introduction/), ou encore celle du [W3school](https://www.w3schools.com/bootstrap5/index.php).

Pour l'installer, ajoutons le à nos prés-requis du site **front**. On tape dans la commande suivante dans *"commentaires/static"* : `npm add --save bootstrap`

Si l'on regarde le contenu du package *"commentaires/static/bootstrap"* on trouve les dossiers suivant :

```text
.
├── dist
│   ├── css
│   └── js
├── js
│   ├── dist
│   │   └── dom
│   └── src
│       ├── dom
│       └── util
└── scss
    ├── forms
    ├── helpers
    ├── mixins
    ├── utilities
    └── vendor
```

Nous n'allons avoir besoin que du dossier *"dist"* qui contient la version *compilée* de bootstrap.

> le javascript est assemblé en fichier utilisable par le front, et le css est le résultat de la compilation du [scss](https://sass-lang.com/)).

Si l'on regarde le dossier *"commentaires/static/bootstrap/dist/css"* on trouve tout un tas de fichier qui se ressemblent. Par exemple pour `bootstrap.css` :

* `bootstrap.css`
* `bootstrap.min.css`

Ces deux fichiers sont presque identiques. Le premier est visible par des humains et le second est le même fichier mais sans les retour à la ligne et les indentations ce qui le rend plus petit : 200ko environ vs 160ko. C'est celui-ci que nous inclurons dans nos pages.

Il se passe la même chose pour `bootstrp.js` et `bootstrap.min.js` dans le dossier *"commentaires/static/bootstrap/dist/js"* mais la différence est plus importante : 150ko vs 60ko.

## fichiers

on va faire trois pages :

* *"index.html"* qui va permettre d'aller soit vers *"donner.html"* soit vers *"lire.html"*
* *"donner.html"* qui va permettre à l'utilisateur de donner son avis
* *"lire.html"* qui va permettre à l'utilisateur de lire les avis déjà donné et de les noter.

On fait une mise en forme avec bootstrap simple, élégante et de bon goût. Une barre de navigation nous permet de revenir à *"index.html"* et le footer 

### *"index.html"*

Commençons par le fichier *"index.html"* :

```html
<!doctype html>
<html lang="fr">

<head>
    <meta charset="utf-8">
    <title>Commentaires</title>

    <link href="./node_modules/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="./node_modules/bootstrap//dist/js/bootstrap.bundle.min.js"></script>

    <style>
        .main {
            margin-top: 100px;
            margin-bottom: 50px;
        }
        nav .marge {
            margin-right: 20px;
            margin-left: 20px;
        }

        .choix {
            padding: 50px;
        }

        .bas {
            margin-top: 100px;
        }
    </style>
</head>

<body>
    <header>
        <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
            <a class="marge navbar-brand" href="#">Maison</a>
        </nav>
    </header>

    <div class="main container-fluid text-center ">
        <div class="row">
            <h1 class="display-1">Votre avis [n|v]ous intéresse</h1>
        </div>
        <div class="bas row align-items-center gx-6">
            <div class="col">
                <div class="choix border bg-light">
                    <p>donnez votre avis</p>
                    <p><a class="btn btn-primary" href="./donner.html" role="button">DONNER !</a></p>
                </div>
            </div>
            <div class="col">
                <div class="choix border bg-light">
                    <p>lisez des avis</p>
                    <p><a class="btn btn-danger" href="./lire.html" role="button">LIRE !</a></p>
                </div>
            </div>
        </div>

    </div>

    <footer class="footer fixed-bottom text-center bg-dark">
        <p class="text-white">Le site qui permet de donner son avis.</p>
    </footer>
</body>

</html>
```

### *"donner.html"*

```html
<!doctype html>
<html lang="fr">

<head>
    <meta charset="utf-8">
    <title>Donner son avis</title>

    <link href="./node_modules/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="./node_modules/bootstrap//dist/js/bootstrap.bundle.min.js"></script>

    <style>
        .main {
            margin-top: 100px;
            margin-bottom: 50px;
        }
        nav .marge {
            margin-right: 20px;
            margin-left: 20px;
        }
    </style>
</head>

<body>
    <header>
        <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
            <a class="marge navbar-brand" href="./index.html">Maison</a>
        </nav>
    </header>

    <div class="main container-fluid row">
        <div class="col"></div>
        <form class="col-6">
            <div class="mb-3">
              <label for="pseudo" class="form-label">Pseudo</label>
              <input class="form-control">
            </div>
            <div class="mb-3">
              <label for="titre" class="form-label">Titre</label>
              <input type="password" class="form-control">
            </div>            
            <div class="mb-3">
                <label for="message" class="form-label">Message</label>
                <textarea class="form-control" rows="7"></textarea>
              </div>
              <button type="submit" class="btn btn-primary">Envoyer</button>
          </form>
          <div class="col"></div>
    </div>

    <footer class="footer fixed-bottom text-center bg-dark">
        <p class="text-white">Le site qui permet de donner son avis.</p>
    </footer>
</body>

</html>
```

### *"lire.html"*

```html
<!doctype html>
<html lang="fr">

<head>
    <meta charset="utf-8">
    <title>Lire un avis</title>

    <link href="./node_modules/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="./node_modules/bootstrap//dist/js/bootstrap.bundle.min.js"></script>

    <style>
        .main {
            margin-top: 100px;
            margin-bottom: 50px;
        }
        nav .marge {
            margin-right: 20px;
            margin-left: 20px;
        }
    </style>
</head>

<body>
    <header>
        <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
                <a class="marge navbar-brand" href="./index.html">Maison</a>
                <form class="navbar form-inline ms-auto row">
                    <input class="form-control col" type="text" placeholder="Search" aria-label="Search">
                    <button class="marge col-3 btn btn-outline-success" type="submit">Search</button>
                </form>
        </nav>
    </header>

    <div class="main container-fluid">
        <div class="card">
            <div class="card-body">
              <h5 class="card-title">titre du commentaire</h5>
              <h6 class="card-subtitle mb-2 text-muted">pseudo</h6>
              <p class="card-text">Contenu du commentaire.</p>
            </div>
          </div>
    </div>

    <footer class="footer fixed-bottom text-center bg-dark">
        <p class="text-white">Le site qui permet de donner son avis.</p>
    </footer>
</body>

</html>
```
