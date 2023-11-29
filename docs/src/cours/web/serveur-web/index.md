---
layout: layout/post.njk

title: "Serveur Web"
authors:
    - "François Brucker"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Création des premiers serveurs web dont le but est d'envoyer des données.

<!-- fin résumé -->

> TBD faire serveur avant données.
> 
> 1. node (sans fichier)
> 2. express avec static
> 3. récupérer des données avec fetch :
>  1. de son serveur
>  2. de l'internet (en exercice, et trouver le bon exemple simple)
>
> TBD supprimer les référence à tree.


1. [serveur web minimal](./minimal){.interne}
2. [gestion des routes](./routes){.interne}
3. [serveur web avec express](./express){.interne}
4. [routes spéciales](./routes-paramètres){.interne}

> TBD faire fichiers à part. Refaire avec les même concepts mais plus simple. En particulier les fichiers : commencer par tout mettre en texte dans le serveur et statique uniquement avec express.
> TBD express res.json à faire
> TBD attention ajouter import dirname dans express
> TBD parler d'une requête http : header/type/body
> TBD fetch : dire que c'est une fonction distante et donc asynchrone ; lier json / faire un await puis un then en v2 et dire que l'on essaie de faire ça en vrai

