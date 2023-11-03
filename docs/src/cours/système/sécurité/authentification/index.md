---
layout: layout/post.njk

title: Authentification


eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD

- asymétrique
- signature
- attaque man in the middle (tls)

> TBD : pourquoi asymétrique pas utilisé pour confidentialité ? A cause du temps que ça prend.
