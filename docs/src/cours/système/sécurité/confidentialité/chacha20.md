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

{% note "**Définition**" %}
Une **permutation pseudo-aléatoire sécurisée** (*secure PRP, pseudo random permutation*) doit avoir les propriétés suivantes :

- $F: \\{0, 1\\}^s \times \\{0, 1\\}^n \rightarrow \\{0, 1\\}^n$, avec $s <<n$
- $F(k,\cdot)$ doit être une bijection pour tout $k$
- $F$ doit être implémentable par algorithme efficace.
- tout algorithme efficace ne peut avoir qu'un avantage négligeable au jeu de la reconnaissance $F(k, \cdot)$
{% endnote %}

Une PRP est une restriction des PRF aux permutation de $\\{0, 1\\}^n$. Si $n4 est grand, ce n'est cependant pas un problème, on ne peux distinguer les deux avec un avantage négligeable :

{% note "**Proposition**" %}
Une **PRP** ne peut être distinguée d'une fonction aléatoire avec un avantage non négligeable par un algorithme efficace.

{% endnote %}
{% details "preuve" %}
> TBD : proposition 3.29 (trouver un point fixe est rare, donc pas efficace). Introduction to modern cryptography
{% enddetails %}

## Fonctionnement

{% lien %}

- [design](https://loup-vaillant.fr/tutorials/chacha20-design)
- [spec et implémentations](https://cr.yp.to/chacha.html)

{% endlien %}

> TBD : à approfondir
> TBD : faire dessin deu chiffrement. Et laisser la place pour poly1305

