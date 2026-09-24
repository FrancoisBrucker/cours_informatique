---
layout: layout/post.njk

title: Perfectionnement
tags: ["code", "go"]


eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Méthodes de développement

Dernière partie en python avant d'apprendre un nouveau langage. On montre comment développer du code au quotidien :

{% aller %}
[méthodes de développement](méthode-développement){.interne}
{% endaller %}

## Coder avec la mémoire

> TBD 
>
> le go
>
> - prérequis : git
> - outils de la partie A : 
>   - dépendances
>   - débogueur
> - pointeurs + ramasse miette 
> - programmation parallèle
> - profilage de code ?
> - interfaces
> - [mémoire](./données-mémoire/){.interne}
