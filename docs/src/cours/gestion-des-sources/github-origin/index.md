---
layout: layout/post.njk
title: Github

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Pour pratiquer la gestion des sources, nous allons utiliser <https://github.com/> comme sauvegarde origine. Le site fonctionne avec logiciel de gestion de sources [git](https://fr.wikipedia.org/wiki/Git). Il en existe d'autres, comme <https://gitlab.com/> par exemple.

{% info %}
L'[aide de github](https://docs.github.com/en/get-started) est très bien faite (la traduction en français est cependant automatique, donc souvent approximative), n'hésitez pas à y jeter un coup d'œil.
{% endinfo %}

## <span id="compte-github"></span> Création du compte github

{% aller %}
[Se créer un compte github](./compte-github){.interne}
{% endaller %}

## <span id="tuto-github"></span> Utilisation de github

On va utiliser l'interface de github pour mettre en œuvre les principales fonctionnalités d'un système de gestion des sources :

- faire des commit
- gérer des branches
- fusionner des branches en résolvant des conflits
- voir l'historique du projet
- comment ajouter des membres à un projet

{% aller %}
[Comment créer un projet uniquement avec github](./projet-github){.interne}
{% endaller %}

## Pull requests

Por mettre à jour notre projet, nous avons effectué [une **_pull request_**](../bonnes-pratiques/#pull-request){.interne}. Cette façon d'ajouter des commits à la sauvegarde est une spécificité de github (et gitlab). Lorsque nous utiliserons git en ligne de commande, on mettra la sauvegarde directement à jour.

## Github actions

> TBD :
>
> - permet de mettre en place du CI/CD : <https://www.youtube.com/watch?v=scEDHsr3APg>
> - github actions <https://www.youtube.com/watch?v=p3W2XCD3smk>
