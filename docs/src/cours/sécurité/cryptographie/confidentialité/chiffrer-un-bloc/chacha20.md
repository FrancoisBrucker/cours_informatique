---
layout: layout/post.njk

title: Algorithme Chacha20

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



> TBD : tout est à faire.
> Faire des exemple d'utilisation.


{% lien %}

- [Fonctionnement et origine](https://en.wikipedia.org/wiki/Salsa20#ChaCha_variant)
- [RFC](https://datatracker.ietf.org/doc/html/rfc8439)

{% endlien %}

Chacha20 est le chiffrement en flux le plus populaire. Son chiffrement est identique au principe général :

- chiffrement d'un bloc
- aggregation des blocs entre eux.

La seule différence est que toutes les opérations de Chacha sont inversible, le générateur pseudo-aléatoire n'est donc pas créer à partir d'une PRF, mais d'une PRP.

## PRP


## Fonctionnement

{% lien %}

- [design](https://loup-vaillant.fr/tutorials/chacha20-design)
- [spec et implémentations](https://cr.yp.to/chacha.html)

{% endlien %}

> TBD : à approfondir
> TBD : faire dessin deu chiffrement. Et laisser la place pour poly1305
