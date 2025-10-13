---
layout: layout/post.njk

title: Algorithme Chacha20

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD :
> - <https://www.youtube.com/watch?v=G0O0VHVtNuM>
> - <https://www.youtube.com/watch?v=UeIpq-C-GSA>
> - <https://www.youtube.com/watch?v=Xw9lBsCc_Qk>
> 
> TBD : dire qu'on ne présente que le bloc principal. Ensuite il s'imbrique dans la suite du cours (taille quelconque et intégrité)

{% lien %}

- [Fonctionnement et origine](https://en.wikipedia.org/wiki/Salsa20#ChaCha_variant)
- [RFC](https://datatracker.ietf.org/doc/html/rfc8439)

{% endlien %}

## Fonctionnement

{% lien %}

- [design](https://loup-vaillant.fr/tutorials/chacha20-design)
- [spec et implémentations](https://cr.yp.to/chacha.html)

{% endlien %}

> TBD : à approfondir
> TBD : faire dessin du chiffrement.
> TBD : Faire des exemple d'utilisation.
