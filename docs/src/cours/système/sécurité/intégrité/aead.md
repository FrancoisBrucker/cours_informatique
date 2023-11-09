---
layout: layout/post.njk

title: AEAD

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD AEAD

On utilise l'intégrité directement dans la transmission, ce qui permet d'utiliser des technique de MAC plus simple.

On s'autorise l'ajout de données externes (les données associées) qui n'ont pas besoin (ou dont on a pas envie que) qu'elles soient chiffrées, comme les headers du protocole, mais dont on veut garantir l'intégrité.

On utilise pour cela le méthode du *encrpyt then MAC* mais en y ajoutant les *données ajoutées*. Le message envoyée est alors :

```
F(k, m) || S(k', AD || F(k, m))
```

La clé utilisée pour la signature est souvent différente de la clé utilisée pour signer. Ces deux clés sont souvent des clés dérivées.

## Chacha20-poly1309

> TBD : <https://en.wikipedia.org/wiki/ChaCha20-Poly1305>

## AES-GCM

> TBD : <https://en.wikipedia.org/wiki/Galois/Counter_Mode>

[AES GCM](https://www.youtube.com/watch?v=g_eY7JXOc8U)

[galois counter mode v2](https://www.youtube.com/watch?v=R2SodepLWLg&t=0s)

[tuto aes-gcm](https://www.youtube.com/watch?v=Q4EmXJTwcdo)
[galois counter mode of operation ref](https://csrc.nist.rip/groups/ST/toolkit/BCM/documents/proposedmodes/gcm/gcm-spec.pdf)
