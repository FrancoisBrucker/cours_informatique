---
layout: layout/post.njk

title: Chiffrement par bloc

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD *bloc cicher*

1. un bloc
2. plusieurs blocs (on les transforme en code stream)

> TBD : PRP -> block

> TBD : nonce

sécurité du bloc = taille de la clé ou moitié d la taille du bloc (attaque par anniversaire si pas de counter mode)

> [tuto encryption](https://www.youtube.com/watch?v=oVCCXZfpu-w)

- [SP network](https://www.youtube.com/watch?v=DLjzI5dX8jc)
- [key schedule](https://braincoke.fr/blog/2020/08/the-aes-key-schedule-explained/#key-expansion)
- [inverse](https://tratliff.webspace.wheatoncollege.edu/2016_Fall/math202/inclass/sep21_inclass.pdf)
