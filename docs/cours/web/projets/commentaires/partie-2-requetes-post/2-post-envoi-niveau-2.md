---
layout: page
title:  "Projet commentaires : partie 2 / envoyer les donées"
category: cours
author: "François Brucker"
---

> [commentaires]({% link cours/web/projets/commentaires/index.md %}) / [partie 2]({% link cours/web/projets/commentaires/partie-2-requetes-post/index.md %}) / [envoyer les données]({% link cours/web/projets/commentaires/partie-2-requetes-post/2-post-envoi.md %})
{: .chemin}

> TBD 
> * cors : pas bon sans serveur.
> 
## gérer les erreurs

On va ajouter une méthode `then` pour récupérer la réponse du serveur :

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
                .then((response) => {
                    console.log("réponse serveur :");
                    console.log(response)
                })

            console.log(JSON.stringify(data, null, 2))
            event.preventDefault()
        })
    </script>
```

En faisant notre essai on voir que l'objet rendu contient un attribut `status` qui vaut 404. Et un attribut `ok` qui vaut `false`.

Le [pattern classique](https://dev.to/anchobies/when-that-s-not-so-fetch-error-handling-with-fetch-4cce) est alors de lever une exception qui sera ensuite récupérée dans la méthode `catch` :

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
                .then((response) => {
                    if (!response.ok) {
                        throw Error({
                            'ok': response.ok,
                            'status': response.status,
                            'statusText': response.statusText
                        })
                    } else {
                        console.log("réponse serveur :");
                        console.log(response)
                        console.log(response.status)
                    }
                })
                .catch(error => console.log(error))

            console.log(JSON.stringify(data, null, 2))
            event.preventDefault()
        })
    </script>
```

> Par défaut, la méthode `catch` n'est appelée que si la commande `fetch` a eu un soucis (et lève une erreur de type `TypeError`), pas lorsque le serveur en a eu un.

## cors

Lorsque vous essayez de faire des requêtes `fetch` entre différents serveur (ou lorsque vous exécutez un fichier html avec le protcole `file` et que vous tentez de faire un faire sur un serveur distant), le navigateur va vous interdire de le faire car c'est une faille de sécurité.

<https://developer.mozilla.org/fr/docs/Web/HTTP/CORS>


> TBD
> on envoie que si le titre est non vide : ajouter bootstrap verification
> après envoie on supprime le titre et le message pour eviter les soucis de double post
> cors ?