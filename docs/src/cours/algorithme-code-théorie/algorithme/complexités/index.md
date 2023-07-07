---
layout: layout/post.njk 
title: Complexités

eleventyNavigation:
    order: 1

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Différents types de complexités

<!-- fin résumé -->

> TBD : mettre $\mathcal{O}$ (parler de $\Omega$) et ajouter $\Theta$  dans un truc à part pour expliquer pourquoi c'est central en informatique (Turing aussi). Avec hiérarchie des complexité Polynomial vs exponentiel (faire tous les cas).

<div class="interne">
{{ collections.all | eleventyNavigation(eleventyNavigation.key) | eleventyNavigationToHtml() | safe }}
</div>
