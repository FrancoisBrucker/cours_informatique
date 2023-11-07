---
layout: layout/post.njk

title: Intégrité de la transmission

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

ajouter le hash à chaque bloc. Pas la peine d'utiliser sha à ce moment.

> AEAD : p148 serious cryptography

## Chacha20-coly1309

## AES-GCM

[aes gcm](https://www.youtube.com/watch?v=g_eY7JXOc8U)
[galois counter mode v2](https://www.youtube.com/watch?v=R2SodepLWLg&t=0s)
