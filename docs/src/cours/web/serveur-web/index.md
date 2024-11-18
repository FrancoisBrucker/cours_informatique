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

1. [serveur web minimal](./minimal){.interne}
2. [gestion des routes](./routes){.interne}
3. [serveur web avec express](./express){.interne}
4. [routes spéciales](./routes-paramètres){.interne}
