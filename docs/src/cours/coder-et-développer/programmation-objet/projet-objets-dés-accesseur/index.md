---
layout: layout/post.njk
title: "Projet : Amélioration des objets dés"

eleventyNavigation:
  prerequis:
    - "../projet-objets-dés/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Dé actuel

> TBD

## Valeur par défaut

{% faire %}
Faites en sorte que l'on puisse créer des dés avec une position initiale, On doit pouvoir :

- créer un dé sans paramètre, `Dé()`{.language-}, et sa position doit être sur la position 1
- créer un dé avec un paramètre qi sera sa position par défaut `Dé(4)`{.language-} par exemple.

Modifiez tous les tests et les programmes principaux.
{% endfaire %}


## __str__

## min et max dans classe
