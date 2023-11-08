---
layout: layout/post.njk

title: Chacha20

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Chacha est un PRP masi ça marche aussi

> TBD 1. def PRP
> PRP alors aussi PRF proposition 3.29 (trouver un point fixe est rare, donc pas efficace)

On règle le problème précédent en découpant le message en bloc et en générant $n$ bit par $n$ bits.

Chacha est organisé en round qui vont éloigner l'élément de la clé. Le but est de rendre le retour difficile dans l'absolu mais aisé si on connaît le chemin.

Mais il faut faire ça bien pour garde la sécurité. Rappelez vous que le OTP ne fonctionne que si c'est One Time.

contre side channel attack : chaque round fait la même chose.
{% lien %}

Chacha :

- [fonctionnement et origine](https://en.wikipedia.org/wiki/Salsa20#ChaCha_variant). Attention maintenant le nonce est sur 3 byte, Les constantes sont là pour l'init si message vide

- [design](https://loup-vaillant.fr/tutorials/chacha20-design)
- [spec et implémentations](https://cr.yp.to/chacha.html)
- [RFC](https://datatracker.ietf.org/doc/html/rfc8439)

{% endlien %}

