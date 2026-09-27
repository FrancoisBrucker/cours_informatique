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
> aussi cache et bus pour les transferts. On doit pouvoir controler le tout.
> qu'est un entier python sous cette nomenclature ? Un tableau d'int64 
> sauf que longueur au max int64. Si on veut plus = liste chaînée int64 = taille et si taille = max, le prochain int64 est l'adresse du suivant.
