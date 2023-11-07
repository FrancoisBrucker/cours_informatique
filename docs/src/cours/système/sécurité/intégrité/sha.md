---
layout: layout/post.njk

title: SHA

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


> TBD standard

> montrer que c'est bien fait via un PRP.

Plusieurs méthode de hash cryptographique existent. On peut en citer deux, issues de sha :

- [sha-1](https://fr.wikipedia.org/wiki/SHA-1) utilisé par git mais plus trop de façon cryptographique
- SHA256 (protocole [sha-2](https://fr.wikipedia.org/wiki/SHA-2))

{% info %}
On recommande actuellement d'utiliser l'algorithme SHA256 ou SHA512 pour un usage cryptographique.
{% endinfo %}

Ils sont directement utilisable :

- [sous mac](https://fre.applersg.com/check-sha1-checksum-mac-os-x) et [linux](https://www.lojiciels.com/quest-ce-que-shasum-sous-linux/) avec le programme `shasum`
- [sous windows](https://lecrabeinfo.net/verifier-integrite-calculer-empreinte-checksum-md5-sha1-sha256-fichier-windows.html) avec la commande [Get-FileHash](module) sous powershell.


[SHA-x](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms)

[sha](https://www.youtube.com/watch?v=DMtFhACPnTY)

[SHA-x](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms)

- SHA-1 : checksum (git ?). Attention, <https://security.googleblog.com/2017/02/announcing-first-sha1-collision.html>. [Gitlab passe à sha-256](https://about.gitlab.com/blog/2023/08/28/sha256-support-in-gitaly/) pour ses hash
- SHA-256/512 : empreinte (crypto ?)
