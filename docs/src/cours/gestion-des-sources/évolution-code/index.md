---
layout: layout/post.njk

title: Gestion de l'évolution de son code source
tags: ["projet"]

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Comment gérer l'évolution de son code source au quotidien, sans avoir peur de modifier son code. On va utiliser l'interface de github pour mettre en œuvre les principales fonctionnalités d'un système de gestion des sources :

- faire des commit
- gérer des branches
- fusionner des branches en résolvant des conflits
- voir l'historique du projet
- comment ajouter des membres à un projet

{% info %}
L'[aide de github](https://docs.github.com/en/get-started) est très bien faite (la traduction en français est cependant automatique, donc souvent approximative), n'hésitez pas à y jeter un coup d'œil.
{% endinfo %}


## Projet Github

Nous allons illustrer toutes les parties de ce cours avec un projet entièrement sous github.

{% aller %}
[Création du projet](./github-projet-création){.interne}
{% endaller %}


## Index

{% aller %}
[Index et commits](./besoins-index){.interne}
{% endaller %}

## Branches

> TBD évolution divergentes du code
>
## Merge et rebase

> TBD synchronisation de code

## Besoins pour une gestion des sources locale


{% aller %}
[Besoins](./besoins-gestion-sources){.interne}
{% endaller %}

## Projet : gestion des sources

{% aller %}
[Projet uniquement avec github](./github-projet){.interne}
{% endaller %}

