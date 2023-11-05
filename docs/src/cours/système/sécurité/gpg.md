---
layout: layout/post.njk

title: GPG

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD
>

RSA peut encrypter un nombre plus petit que $n$. On pourrait décomposer un message plus gros en paquets de $T$ bits avec $2^T < n$ mais ce n'est quasi-jamais fait car le codage/décodage est algorithmiquement long.

On utilise des techniques [PGP](https://fr.wikipedia.org/wiki/Pretty_Good_Privacy) pour cela.

{% lien %}
Encoder un fichier avec RSA et un code symétrique :

<https://kulkarniamit.github.io/whatwhyhow/howto/encrypt-decrypt-file-using-rsa-public-private-keys.html>
{% endlien %}
