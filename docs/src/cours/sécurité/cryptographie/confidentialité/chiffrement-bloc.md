---
layout: layout/post.njk

title: Chiffrer un message de taille fixe

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


PRF et PRP


> TBD
>
> 1. Vernam. Mais
> 2. doit avoir une clé pour déchiffrer, donc taille max. Mais
> 3. doit réutiliser la clé ? Ajouter un paramètre
> 4. on peut maintenant chiffrer et déchiffrer des message. Mais
> 5. est-ce vraiment sécurisé ? On le vérifie avec des preuves de théorie des jeux.
>

> TBD attention : ECB pas semantically secure : <https://crypto.stanford.edu/~dabo/courses/cs255_winter19/lectures/PRP-PRF.pdf>

sécurité du bloc = taille de la clé ou moitié d la taille du bloc (attaque par anniversaire si pas de counter mode)

> [tuto encryption](https://www.youtube.com/watch?v=oVCCXZfpu-w)

- [SP network](https://www.youtube.com/watch?v=DLjzI5dX8jc)
- [key schedule](https://braincoke.fr/blog/2020/08/the-aes-key-schedule-explained/#key-expansion)
- [inverse](https://tratliff.webspace.wheatoncollege.edu/2016_Fall/math202/inclass/sep21_inclass.pdf)
