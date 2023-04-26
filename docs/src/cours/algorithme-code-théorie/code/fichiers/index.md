---
layout: layout/post.njk 
title: "Fichiers"

eleventyNavigation:
    order: 13
    prerequis:
        - "../../algorithme/structure-de-données/chaîne-de-caractères/"
        - "/tutoriels/fichiers-navigation/"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


<!-- début résumé -->

Qu'est-ce qu'un fichier et comment l'utiliser.

<!-- fin résumé -->

<div class="interne">
{{ collections.all | eleventyNavigation(eleventyNavigation.key) | eleventyNavigationToHtml() | safe }}
</div>
