---
layout: page
title:  "Projet commentaires : partie 2 / préparer les données"
category: cours
author: "François Brucker"
---

> [commentaires]({% link cours/web/projets/commentaires/index.md %}) / [partie 2]({% link cours/web/projets/commentaires/partie-2-requetes-post/index.md %}) / [préparer les données]({% link cours/web/projets/commentaires/partie-2-requetes-post/1-json.md %})
{: .chemin}

On va préparer les données à être envoyées au serveur.

## récupération des données du formulaire

On va commencer par afficher dans la console (du client) les données du formulaires lorsque l'on appuie sur le bouton sur la page *"donner.html"*.

### le bouton

On commence par lier l'appui sur le  bouton. Pour cela on identifie le bouton par un identifiant puis, dans un script javascript en front, on lie une fonction qui sera exécutée lors d'un clic.

On commence par ajouter un identifiant au bouton :

```html
<!-- ... -->
  <button type="submit" class="btn btn-primary" id="bouton_envoi">Envoyer</button>
<!-- ... -->
```

Puis juste avant la fermeture de la balise `<body></body>` on place notre script :

```html
<script>
    document.querySelector("#form-button").addEventListener("click", (event) => {
        console.log(document.querySelector("#form-input").value)
        event.preventDefault()
    })
</script>
```

On peut maintenant cliquer sur le bouton et obtenir `"clic"` dans la console.

### les données

Pour récupérer les données, il faut :

1. ajouter des identifiants aux élément html qui vont contenir les données
2. récupérer les valeurs lors du clic
3. structurer ces valeurs dans un objet et le convertir en json pour envoi.

#### identifiants

Le formulaire :

```html
<form class="col-6">
    <div class="mb-3">
        <label for="pseudo" class="form-label">Pseudo</label>
        <input class="form-control" id="pseudo">
    </div>
    <div class="mb-3">
        <label for="titre" class="form-label">Titre</label>
        <input class="form-control"  id="titre">
    </div>
    <div class="mb-3">
        <label for="message" class="form-label">Message</label>
        <textarea class="form-control" rows="7" id="message"></textarea>
    </div>
    <button type="submit" class="btn btn-primary" id="bouton_envoi">Envoyer</button>
</form>
```

#### récupération des données et envoi

on a modifié le script :

```html
    <script>
        document.querySelector("#bouton_envoi").addEventListener("click", (event) => {
            data = {
                "pseudo": document.querySelector("#pseudo").value,
                "titre": document.querySelector("#titre").value,
                "message" : document.querySelector("#message").value
            }
            console.log(JSON.stringify(data, null, 2))
            event.preventDefault()
        })
    </script>
```

> On a utilisé la documentation de [JSON.stringify](https://stackoverflow.com/questions/4810841/pretty-print-json-using-javascript) pour rendre le rendu en texte json de notre objet joli.
