---
layout: layout/post.njk

title: Système
tags: ['cours', 'unix', 'système']
authors:
    - "François Brucker"

date: 2026-01-07

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

Cours de système.

## Partie I : Ordinateur, programmes et OS

{% aller %}
[Ordinateur, programmes et OS](ordinateur-programmes-OS)
{% endaller %}

## Partie II : Interagir avec le système


{% aller %}
[Interagir avec le système](interagir-avec-système)
{% endaller %}

## Partie III : Système Linux


{% aller %}
[Linux](linux)
{% endaller %}


> TBD [refactor](./a-refactor/)