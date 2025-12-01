---
layout: layout/post.njk

title: Interagir avec le réseau

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


## Principes

{% aller %}
[Principes](./principe){.interne}
{% endaller %}

## URL

{% aller %}
[Anatomie d'une URL](./anatomie-url/){.interne}
{% endaller %}

## Serveur web local

> TBD tout ce qu'on a vu fonctionne sur la même machine. localhost

> TBD avec python et http pour un serveur bête en localhost.
