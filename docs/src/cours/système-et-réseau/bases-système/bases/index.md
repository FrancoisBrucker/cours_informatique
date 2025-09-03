---
layout: layout/post.njk

title: Connaissances minimales

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On suppose ici que vous savez minimalement interagir avec votre système d'exploitation en exécutant des applications via un menu ou l'explorateur de fichiers.

## But

{% aller %}
[But et principes d'un système](but){.interne}
{% endaller %}

## Interactions

{% aller %}
[Interagir avec le système](interactions){.interne}
{% endaller %}
