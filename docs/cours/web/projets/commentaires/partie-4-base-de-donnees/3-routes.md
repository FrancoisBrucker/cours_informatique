---
layout: page
title:  "Projet commentaires : partie 4 / routes"
category: cours
author: "François Brucker"
---

> [commentaires]({% link cours/web/projets/commentaires/index.md %}) / [partie 4]({% link cours/web/projets/commentaires/partie-4-base-de-donnees/index.md %}) / [routes]({% link cours/web/projets/commentaires/partie-4-base-de-donnees/3-routes.md %})
{: .chemin}

On crée les routes permettant d'accéder aux données dans notre serveur.

## routes

On va implémenter toute les routes CRUD. Pour séparer la gestion des données des autres route, on va faire commencer toutes les routes par `/api/`.

Pour tester les routes, vous allez installer le plugin [RESTer](https://github.com/frigus02/RESTer) sur votre chrome.

### create

Une requête POST qui récupère un json permettant de créer une donnée qu'on met en base :

```js
api.post(/api/create/, (req, res) => {

})



## gestion des routes avec express

> TBD
> on utilise then et plus await. Usage normal des promise
{: .note}
