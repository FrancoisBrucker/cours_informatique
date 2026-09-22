---
layout: layout/post.njk

title: Arbres

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


## Arbres

{% aller %}

[Définitions](définitions){.interne}

{% endaller %}

{% aller %}

[Compter les arbres](./compter-arbres){.interne}

{% endaller %}

## Problème de l'arbre couvrant

{% aller %}

[Arbres couvrants](arbres-couvrants){.interne}

{% endaller %}
