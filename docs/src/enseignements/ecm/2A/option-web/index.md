---
layout: layout/post.njk
templateEngineOverride: njk, md

title: "Web front/back"
tags: ["enseignement", "ECM"]

eleventyNavigation:
  order: 2

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Web front et back (avec node).

<!-- fin résumé -->

## Programme

{% aller %}
[Cours de web](/cours/web){.interne}
{% endaller %}

## cours 1 : html (2h)

A faire : une page avec son animal favori. Cette page doit contenir :

1. deux images de celui-ci :
   - une depuis internet
   - une depuis votre disque dur appelée avec une adresse relative
2. le lien Wikipédia
3. deux paragraphes de pourquoi c'est votre animal favori

Cette page doit être validée par le W3C

{% faire "À faire" %}
Mettre sa page sur sa page web.
{% endfaire %}

## cours 2 : css (2h)

CSS. Ajouter de la couleur et du style à votre page. En particulier :

- gérer les marges de vos paragraphes
- faites en sorte que les images soient centrées
- gérer les pseudo-attributs des liens

Pour vous aider : [un rapport de stage de l'année dernière](Rapport_stage_L1_Arnaud_SERRES.pdf)

{% faire %}
Ajouter le css sur sa page web.
{% endfaire %}

{% note "Exposé" %}

{% endnote %}

## cours 3 : bootstrap (2h)

Installation :

- cdn
- à la main
- node

La page des animaux à bootstraper :

- mise en page
- image et card
- ...

## cours 4 : js (2h)

Bases de javascript

## cours 5&6 : projet front

### cours 5 : Sujet

Choisir un sujet et coder les pages

{% lien %}
[règles du décathlon](https://www.ludism.fr/regles_files/fr/DECATHLONfr.pdf)
{% endlien %}

### cours 6

Lier les pages dans un projet front et un serveur web de fichiers statiques.

{% aller %}
[Site statique](/cours/web/projet-front/){.interne}
{% endaller %}

## cours 7

Presentation des projets.

## Cours 8&9 : backend

{% aller %}
[Site statique](/cours/web/serveur-web/){.interne}
{% endaller %}

## Projet final

Il doit avoir :

- une partie back
- une partie front
- des données
