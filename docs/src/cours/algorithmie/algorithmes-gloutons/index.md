---
layout: layout/post.njk
title: Algorithmes gloutons

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les algorithmes gloutons sont au coeur de nombreux algorithmes. Leur design est simple mais profond. Il combine ainsi souvent de bonnes propriétés théoriques et pratiques.

## Principe

{% aller %}
[Principe](./principe){.interne}
{% endaller %}

## Exemples

### Projet sac à dos

{% aller %}
[Sac à dos](./sac-à-dos){.interne}
{% endaller %}
### Projet chemins et des cycles

{% aller %}
[Chemins et cycles](./chemins-cycles){.interne}
{% endaller %}
