---
layout: layout/post.njk

title: "Serveur Web"
authors:
    - "François Brucker"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Création des premiers serveurs web.

1. [serveur web minimal](./minimal)
2. [gestion des routes](./routes)
3. [serveur web avec express](./express)
4. [routes spéciales](./routes-paramètres)
