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
- checksum/hash/correction d'erreur
  
{% aller %}
[Hash cryptographique](./hash){.interne}
{% endaller %}

> propriété. Non-malleability 
>
[sha](https://www.youtube.com/watch?v=DMtFhACPnTY)

[SHA-x](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms)

- SHA-1 : checksum (git ?). Attention, <https://security.googleblog.com/2017/02/announcing-first-sha1-collision.html>. [Gitlab passe à sha-256](https://about.gitlab.com/blog/2023/08/28/sha256-support-in-gitaly/) pour ses hash
- SHA-256/512 : empreinte (crypto ?)


[aes gcm](https://www.youtube.com/watch?v=g_eY7JXOc8U)
[galois counter mode v2](https://www.youtube.com/watch?v=R2SodepLWLg&t=0s)
