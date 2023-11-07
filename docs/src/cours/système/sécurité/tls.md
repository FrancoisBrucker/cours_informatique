---
layout: layout/post.njk

title: TLS

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


1. être sur de à qui on parle (évite attaque man un the middle)
2. échange de la clé maître et du mode de chiffrement
3. échange des messages

<https://crypto.stackexchange.com/questions/27131/differences-between-the-terms-pre-master-secret-master-secret-private-key>

> TBD AEAD

> TBD attack au pad.

[TLS](https://www.youtube.com/watch?v=0TLDTodL7Lc)
[durée de vie de la clé TLS](https://security.stackexchange.com/questions/55454/how-long-does-an-https-symmetric-key-last)

[ANSSI : recommandations de sécurité relatives à tls](https://www.ssi.gouv.fr/uploads/2020/03/anssi-guide-recommandations_de_securite_relatives_a_tls-v1.2.pdf)

[https](https://www.youtube.com/watch?v=OU-e_Qz-v4U&list=PLql0J2JIDXdOREGUibCXlsevKDK4o8EzN)

[tls handshake](https://www.youtube.com/watch?v=86cQJ0MMses)

[tls AEAD 1.3 chacha poly](https://www.youtube.com/watch?v=S1Awy242Vf8)

<https://fr.wikipedia.org/wiki/Transport_Layer_Security>