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

- aes-128 symétrique aujourd'hui <https://www.youtube.com/watch?v=VYech-c5Dic>
- [SP network](https://www.youtube.com/watch?v=DLjzI5dX8jc)
- [aes explication](https://www.di.ens.fr/~fouque/mpri/des-aes.pdf)
- [key schedule](https://braincoke.fr/blog/2020/08/the-aes-key-schedule-explained/#key-expansion)
- [inverse](https://tratliff.webspace.wheatoncollege.edu/2016_Fall/math202/inclass/sep21_inclass.pdf)
- [spec](https://csrc.nist.gov/csrc/media/projects/cryptographic-standards-and-guidelines/documents/aes-development/rijndael-ammended.pdf#page=1)
- [python mult et inv](https://stackoverflow.com/questions/70261458/how-to-perform-addition-and-multiplication-in-f-28)

- <https://www.emse.fr/~dutertre/documents/synth_AES128.pdf>
- [aes wikipedia](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
- [aes explication français](https://www.utc.fr/~wschon/sr06/txPHP/aes/AesAlgo/AesAlgo.php)

