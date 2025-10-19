---
layout: layout/post.njk

title: SHA Utilisation

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD : Ne faire que des exemple d'utilisation shasum


> TBD [faire du sha](https://osxdaily.com/2021/12/17/check-sha256-hash-mac/)

{% lien %}

- [sha-1](https://fr.wikipedia.org/wiki/SHA-1) utilisé par git mais plus trop de façon cryptographique
- SHA256 (protocole [sha-2](https://fr.wikipedia.org/wiki/SHA-2))

{% endlien %}

> [Gitlab passe à sha-256](https://about.gitlab.com/blog/2023/08/28/sha256-support-in-gitaly/)

> Fonctionne comme ce qu'on a vu en cours, le PRP est appelé SHACAL.

{% info %}
On recommande actuellement d'utiliser l'algorithme SHA256 ou SHA512 pour un usage cryptographique.
{% endinfo %}

Ils sont directement utilisable :

- [sous mac](https://fre.applersg.com/check-sha1-checksum-mac-os-x) et [linux](https://www.lojiciels.com/quest-ce-que-shasum-sous-linux/) avec le programme `shasum`
- [sous windows](https://lecrabeinfo.net/verifier-integrite-calculer-empreinte-checksum-md5-sha1-sha256-fichier-windows.html) avec la commande [Get-FileHash](module) sous powershell.


[sha](https://www.youtube.com/watch?v=DMtFhACPnTY)

[SHA-x](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms)
