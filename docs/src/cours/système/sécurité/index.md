---
layout: layout/post.njk

title: Sécurité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD reprendre partie dictionnaire pour checksum
> TBD SSH : <https://www.linkedin.com/pulse/understanding-ssh-encryption-connection-process-robert-althof>
> ,https://bash-prompt.net/guides/bash-ssh-ciphers/
> TBD pgp
>
> bien parler/ comprendre ce qu'est l'agent
> les clé cryptées, passphrase, etc.

- checksum
- [cryptographie](./cryptographie){.interne}
- signature électronique
- [ssh](./ssh){.interne}
