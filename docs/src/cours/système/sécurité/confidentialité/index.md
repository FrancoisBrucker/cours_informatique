---
layout: layout/post.njk

title: Confidentialité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le message ne doit pouvoir être lu que par son destinataire.

1. César
2. Amélioration avec Vigenère
3. OTP
4. def théorique Shannon
5. soucis
6. def pratique sécurité :
   1. complexité efficient, négligeable

- déchiffrement vs décryptage
- code symétrique
- bloc
- message (plusieurs blocs)
- Diffie-Hellman

En cryptographie, **très difficile** signifie que le temps pour le faire doit être supérieure à la durée de vie (l'utilité) du message.


> TBD test de sécurité.

> TBD : principe d'un russe, la seule chose secrete est la clé. Il faut partir du principe que les adversaires connaissent tout le reste (protocole compris)
