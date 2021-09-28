---
layout: page
title:  "Projet commentaires : partie 2 / envoyer les données"
category: cours
author: "François Brucker"
---

> [commentaires]({% link cours/web/projets/commentaires/index.md %}) / [partie 2]({% link cours/web/projets/commentaires/partie-2-requetes-post/index.md %}) / [envoyer les données]({% link cours/web/projets/commentaires/partie-2-requetes-post/2-post-envoi.md %})
{: .chemin}

Envoyer des données au serveur depuis le navigateur.

## requêtes post

Pour l'instant on a toujours utilisé des requêtes GET pour parler au serveur. Ces requêtes ne nécessitent que l'url. Les requêtes POST quant à elles permettent d'envoyer des données au serveur. C'est le cas pour notre formulaire.

> les différences entre les requêtes GET et POST sont surtout des conventions. Vous pouvez très bien envoyer des données avec une requête GET mais ça rend le code moins lisible.

## fetch en POST

On a déjà utilisé [fetch](https://developer.mozilla.org/fr/docs/Web/API/Fetch_API/Using_Fetch) pour envoyer des requêtes GT au serveur depuis le navigateur. Nous allons faire pareil ici, mais avec une requête POST.

On modifie le script de *"commentaires/static/donner.html"* pour qu'il envoie les données au serveur en utilisant fetch :

```html
<script>
    document.querySelector("#bouton_envoi").addEventListener("click", (event) => {
        data = {
            "pseudo": document.querySelector("#pseudo").value,
            "titre": document.querySelector("#titre").value,
            "message": document.querySelector("#message").value
        }
        fetch("/donne", {
            'method': "POST",
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': JSON.stringify(data)
        })

        console.log(JSON.stringify(data, null, 2))
        event.preventDefault()
    })
</script>
```

On a paramètre la requête `fetch` grâce au deuxième paramètre, qui est un objet :

* on spécifie que la requête va être de type post
* on dit qu'on va envoyer du json
* on envoye du json dans le corps de la requête

Lorsque l'on test la requête on voit (dans la console du navigateur) que le serveur reçoit la requête mais rend un 404. Ceci est normal puisque nous ne gérons pas encore la route côté serveur.

## on fignole

On va ajouter un minimum de contrôle sur le formulaire, histroie de ne pas envoyerde données vide au serveur. On utilise por cela les [validation de formulaire de bootstrap](https://getbootstrap.com/docs/5.1/forms/validation/) et un peu de javascript. Ce qui donne le code final suivant de *"commentaires/static/donner.html"* :

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
        <form id="form_avis" class="was-validated col-6">
            <div class="mb-3">
                <label for="pseudo" class="form-label">Pseudo</label>
                <input class="form-control" id="pseudo" required>
            </div>
            <div class="mb-3">
                <label for="titre" class="form-label">Titre</label>
                <input class="form-control" id="titre" required>
            </div>
            <div class="mb-3">
                <label for="message" class="form-label">Message</label>
                <textarea class="form-control" rows="7" id="message" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary" id="bouton_envoi">Envoyer</button>
        </form>
        <div class="col"></div>
    </div>

    <footer class="footer fixed-bottom text-center bg-dark">
        <p class="text-white">Le site qui permet de donner son avis.</p>
    </footer>

    <script>
        document.querySelector("#bouton_envoi").addEventListener("click", (event) => {
            if (!document.querySelector("#form_avis").checkValidity()) {
                console.log("formulaire non envoyé")
                event.preventDefault()
                event.stopPropagation()

                return
            }
            data = {
                "pseudo": document.querySelector("#pseudo").value,
                "titre": document.querySelector("#titre").value,
                "message": document.querySelector("#message").value
            }
            fetch("/donne", {
                'method': "POST",
                'headers': {
                    'Content-Type': 'application/json'
                },
                'body': JSON.stringify(data)
            })

            console.log(JSON.stringify(data, null, 2))
            event.preventDefault()
        })
    </script>
</body>

</html>
```

On a pas fait grand chose au final, c'est bootstrap qui fait la majeure partie du boulot :

* ajout d'une classe `was-validated` au formulaire
* on ajoute que nos champs sont `required`
* le javascript qui diffère selon que le formulaire est valide ou non
