---
layout: layout/post.njk

title: Intégrité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

- cryptographic hash
- AEAD

différent de code correcteur d'erreur

{% aller %}
[Hash cryptographique](./hash){.interne}
{% endaller %}
