---
layout: layout/post.njk 
title: "Programmation évènementielle"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"


---


La [programmation événementielle](https://fr.wikipedia.org/wiki/Programmation_%C3%A9v%C3%A9nementielle) est un paradigme de programmation très utiliser dans les interfaces graphiques et le web. Cette méthode consiste à réagir à des événements issus du programme ou de la page web comme de cliquer sur un bouton, appuyer sur une touche, etc.

Le principe est le suivant :

1. on inscrit une fonction $f$ à un type d'événement $e$
2. lorsque l'événement $e$ arrive, la fonction $f(e)$  est exécutée

## Environnement python

Nous allons mettre à profit ce que nous venons d'apprendre sur [la gestion des dépendances](../gestion-dépendances/){.interne} et mettre en place un environnement pour utiliser la bibliothèque <https://pyglet.org/> :

{% aller %}
[Créer un environnement virtuel](environnement-virtuel){.interne}
{% endaller %}


> TBD créer un environnement pour pyglet + test de programme.

## Principes

{% aller %}
[Principes](principes){.interne}
{% endaller %}

## Projet

{% aller %}
[Projet : Arkanoid](projet-arkanoid){.interne}
{% endaller %}
