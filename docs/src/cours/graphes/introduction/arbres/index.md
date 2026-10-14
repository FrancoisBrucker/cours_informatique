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

[Définitions](définitions)

{% endaller %}

{% aller %}

[Compter les arbres](./compter-arbres)

{% endaller %}

## Problème de l'arbre couvrant

{% aller %}

[Arbres couvrants](arbres-couvrants)

{% endaller %}
