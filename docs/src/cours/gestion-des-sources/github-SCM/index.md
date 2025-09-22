---
layout: layout/post.njk

title: Gérer ses sources avec github

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Travailler depuis le site <ahttps://github.com/> uniquement est très limitant. Github est le lieu où est stocké du projet, l'outil qui fait tout fonctionner est [git](https://fr.wikipedia.org/wiki/Git). Avant d'utiliser la ligne de commande qui peut être intimidante, utilisant une application développée par github qui permet d'en utiliser les fonctions les plus courantes.

{% lien %}

Il suffit d'aller sur cette page : <https://desktop.github.com/> pour télécharger puis installer l'application.

{% endlien %}

## Projet

On va reprendre le projet précédent pour créer son projet chez soit ainsi que l'origin en utilisant l'application desktop. Ceci vous permettra de savoir comment :

- faire un clone
- notion de gestion distribuée
- créer un nouveau projet
- l'index aussi nommé _stage_
- faire un rebase

{% aller %}
[Comment créer un projet avec l'application desktop](./projet-github-desktop){.interne}
{% endaller %}

## Authentification

Pour pouvoir effectuer des modifications sur l'origine (ici github) il faut pouvoir être identifié. Il existe deux façon de faire :

- via un web token
- via une clé ssh

### Web token

A priori se fait tout seul si vous utiliser l'application.

> TBD à étoffer

### Clés ssh

Méthode est utilisée de préférence lorsque l'on développe au terminal. Elle nécessite plus de connaissance que le web token mais est largement utilisée et son utilisation dépasse de loin le seul cadre de la gestion des sources.

Commencez par créer une clé :

{% aller %}
[créer et utiliser une clé ssh](/cours/système-et-réseau/ssh/){.interne}
{% endaller %}

Puis renseignez **votre clé publique** dans [votre profil github](https://github.com/settings/keys).
