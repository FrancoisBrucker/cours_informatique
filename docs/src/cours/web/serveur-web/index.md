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

1. [serveur web minimal](./minimal){.interne}
2. [gestion des routes](./routes){.interne}
3. [serveur web avec express](./express){.interne}
4. [routes spéciales](./routes-paramètres){.interne}

> TBD faire fichiers à part. Refaire avec les même concepts mais plus simple. En particulier les fichiers : commencer par tout mettre en texte dans le serveur et statique uniquement avec express.
> TBD express res.json à faire
> TBD attention ajouter import dirname dans express
> TBD parler d'une requete http : header/type/body
