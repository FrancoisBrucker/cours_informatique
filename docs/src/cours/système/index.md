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
[Ordinateur, programmes et OS](ordinateur-programmes-OS){.interne}
{% endaller %}

## Partie II : Interagir avec le système


{% aller %}
[Interagir avec le système](interagir-avec-système){.interne}
{% endaller %}

## Partie III : Système Linux


{% aller %}
[Linux](linux){.interne}
{% endaller %}


> TBD [refactor](./a-refactor/){.interne}