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
1. [Index et diffs](./besoins-index){.interne}
2. [projets commits](./github-projet-commits){.interne}
{% endaller %}

## Branches

{% aller %}
1. [Branches](./besoins-branches){.interne}
2. [projets branches](./github-projet-branches){.interne}
{% endaller %}

## Merge et rebase

{% aller %}
1. [Fusion de branches](./besoins-merge-rebase){.interne}
2. [projets fusion de branches](./github-projet-merge-rebase){.interne}
{% endaller %}

