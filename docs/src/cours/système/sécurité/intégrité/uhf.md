---
layout: layout/post.njk

title: Universal Hash Function

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD AEAD

On utilise l'intégrité directement dans la transmission, ce qui permet d'utiliser des technique de MAC plus simple.

## Universal Hash Function

Si on garantit que la cé n'est utilisée qu'une seule fois, on peut utiliser des MAC
comme les one time pad, clé unique.

{% lien %}
[Universal hash function](https://eng.libretexts.org/Under_Construction/Book%3A_The_Joy_of_Cryptography_(Rosulek)/13%3A_Authenticated_Encryption_and_AEAD/13.03%3A_Carter-Wegman_MACs)
{% endlien %}

## AEAD

> p148 serious cryptography

ajouter le hash à chaque bloc. Pas la peine d'utiliser sha à ce moment.

## Chacha20-poly1309

> TBD : <https://en.wikipedia.org/wiki/ChaCha20-Poly1305>
[poly1305](https://en.wikipedia.org/wiki/Poly1305)

## AES-GCM

> TBD : <https://en.wikipedia.org/wiki/Galois/Counter_Mode>

[AES GCM](https://www.youtube.com/watch?v=g_eY7JXOc8U)

[galois counter mode v2](https://www.youtube.com/watch?v=R2SodepLWLg&t=0s)

[tuto aes-gcm](https://www.youtube.com/watch?v=Q4EmXJTwcdo)
[galois counter mode of operation ref](https://csrc.nist.rip/groups/ST/toolkit/BCM/documents/proposedmodes/gcm/gcm-spec.pdf)

[perfect hashing](https://www.youtube.com/watch?v=z0lJ2k0sl1g)