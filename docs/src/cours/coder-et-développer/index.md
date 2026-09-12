---
layout: layout/post.njk

title: Coder et développer
tags: ["cours", "code"]
authors:
  - François Brucker

resume: "Ce cours est dédié au code informatique. Comment l'écrire, le tester et l'exécuter."

date: 2026-01-01

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Ce cours est en 3 parties :

- Apprendre : qui donne tout ce qu'[un honnête-homme](https://fr.wikipedia.org/wiki/Honn%C3%AAte_homme) doit savoir en informatique
- Se perfectionner : connaissances utiles aux personne voulant coder au quotidien
- Se spécialiser : pour aller plus loin

On utilisera un langage d'application pour chaque partie :

- Apprendre et [python](https://www.python.org/)
- Perfectionnement et [go](https://go.dev/)
- Spécialisation et [rust](https://rust-lang.org/fr/)

## Partie A : Apprendre

{% aller %}
[Apprendre à coder en python et développer de (petits) projets informatique](apprendre-programmation){.interne}
{% endaller %}


## Partie B : Se perfectionner

{% aller %}
[Apprendre à coder en go et développer des projets _au long cours_ en informatique](Perfectionnement){.interne}
{% endaller %}


## Partie C : Se spécialiser

{% aller %}
[Spécialisation](Spécialisation){.interne}
{% endaller %}

