---
layout: layout/post.njk

title: Principes de python

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

## Modules

Les [modules](https://docs.python.org/fr/3/tutorial/modules.html) pythons sont des espaces de noms regroupant diverses fonctions pouvant être utilisées une fois _chargé_.

{% aller %}
[Modules](modules){.interne}
{% endaller %}
