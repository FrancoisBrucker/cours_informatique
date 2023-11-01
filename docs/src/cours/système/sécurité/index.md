---
layout: layout/post.njk

title: Sécurité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

En cryptographie, **très difficile** signifie que le temps pour le faire doit être supérieure à la durée de vie (l'utilité) du message.

> TBD reprendre partie dictionnaire pour checksum
> TBD SSH : <https://www.linkedin.com/pulse/understanding-ssh-encryption-connection-process-robert-althof>
> ,https://bash-prompt.net/guides/bash-ssh-ciphers/
> TBD pgp
>
> bien parler/ comprendre ce qu'est l'agent
> les clé cryptées, passphrase, etc.

- crypto dépend beaucoup :
  - division euclidienne et le modulo pour contrôler les sorties
  - la primalité pour garantir la bijectivité
  - [corps finis](https://en.wikipedia.org/wiki/Finite_field_arithmetic) est l'objet qui fait marcher le tout. Surtout pour les binaires ou addition = soustraction = XOR

- S-Box : non linéaire. ce qui homogénéise les bits. Basé sur des considérations arithmétiques (groupes finis) pour que ce soit : 
  - non questionnable (exoste-t-il une backdor ?)
  - statistiquement "prouvable"
- division euclidienne donne Bezout et donne inversion avec les éléments indivisibles
- 
- RSA : bien choisir ses clés. Sinon multiplication de Fermat
- checksum/hash
- [cryptographie](./cryptographie){.interne}
- signature électronique
- [ssh](./ssh){.interne}
- aes-128 symétrique aujourd'hui <https://www.youtube.com/watch?v=VYech-c5Dic>
- [SP network](https://www.youtube.com/watch?v=DLjzI5dX8jc)
- [aes explication](https://www.di.ens.fr/~fouque/mpri/des-aes.pdf)
- [arithmétique](https://stackoverflow.com/questions/70261458/how-to-perform-addition-and-multiplication-in-f-28)
> TBD [cryptanalyse](https://fr.wikipedia.org/wiki/Cryptanalyse) vs codage/décodage
>
> > TBD [ssh paquets](https://www.youtube.com/watch?v=ORcvSkgdA58)
>
> [sha](https://www.youtube.com/watch?v=DMtFhACPnTY
ssh :

- [casser RSA](https://www.youtube.com/watch?v=-ShwJqAalOk)

- <https://info.support.huawei.com/info-finder/encyclopedia/en/SSH.html>
- [ddep dive](https://tusharf5.com/posts/ssh-deep-dive/)
- [known host](https://www.redhat.com/sysadmin/ssh-secure-communication)

## AES

- [key schedule](https://braincoke.fr/blog/2020/08/the-aes-key-schedule-explained/#key-expansion)
- [inverse](https://tratliff.webspace.wheatoncollege.edu/2016_Fall/math202/inclass/sep21_inclass.pdf)
- [spec](https://csrc.nist.gov/csrc/media/projects/cryptographic-standards-and-guidelines/documents/aes-development/rijndael-ammended.pdf#page=1)
- [python mult et inv](https://stackoverflow.com/questions/70261458/how-to-perform-addition-and-multiplication-in-f-28)

- <https://www.emse.fr/~dutertre/documents/synth_AES128.pdf>
- [aes wikipedia](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
- [aes explication français](https://www.utc.fr/~wschon/sr06/txPHP/aes/AesAlgo/AesAlgo.php)

## SHA

[SHA-x](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms)

- SHA-1 : checksum (git ?). Attention, <https://security.googleblog.com/2017/02/announcing-first-sha1-collision.html>. [Gitlab passe à sha-256](https://about.gitlab.com/blog/2023/08/28/sha256-support-in-gitaly/) pour ses hash
- SHA-256/512 : empreinte (crypto ?)

## hash

[hash et sécurité](https://www.youtube.com/watch?v=b4b8ktEV4Bg)

checksum vs empreinte
ajout de salt : taille du sel ?

## aléatoire ?

- génération de nombres premiers ?
- celui de python
- différence entre
  - aléatoire physique
  - aléatoire cryptographique
- entropie ?

[TLS](https://www.youtube.com/watch?v=0TLDTodL7Lc)

[proba discrete](https://en.wikibooks.org/wiki/High_School_Mathematics_Extensions/Discrete_Probability)
[information theory](https://www.youtube.com/watch?v=b6VdGHSV6qg)

[shannon perfect secrecy preuve](https://www3.cs.stonybrook.edu/~omkant/L02-short.pdf)

[aes gcm](https://www.youtube.com/watch?v=g_eY7JXOc8U)
[galois counter mode v2](https://www.youtube.com/watch?v=R2SodepLWLg&t=0s)
[fonction négligeable](https://en.wikipedia.org/wiki/Negligible_function)

[chacha](https://loup-vaillant.fr/tutorials/chacha20-design)
[chacha code](https://www.cryptopp.com/wiki/ChaCha20)
[chacha intro](https://www.youtube.com/watch?v=UeIpq-C-GSA)
[chacha spec](https://cr.yp.to/chacha.html)
[chacha rfc](https://datatracker.ietf.org/doc/html/rfc8439)

[proof in cryptography](https://www.youtube.com/watch?v=Js9dCUFjAhc&list=PL9mNSKC0i-d8VKahrLPoEbUJgo9BwfMQ5&index=1)

[yao 82 preuve](https://crypto.stackexchange.com/questions/18043/an-unpredictable-prg-is-secure-theorem-yao82)

[semantically secure](https://en.wikipedia.org/wiki/Semantic_security)
[prg et p neq np](https://crypto.stackexchange.com/questions/16020/prg-existance-and-p-versus-np)

[pseudo-random function et permutation pareil sous le paradoxe anniversaire](https://crypto.stackexchange.com/questions/75304/what-is-the-difference-between-pseudorandom-permutation-pseudorandom-function-bl)

[aes key schedule](https://en.wikipedia.org/wiki/AES_key_schedule)

Code block ou stream, pas vraiment important. C'est symétrique ou pas qui l'est. Parler du coup de chacha qui est plus simple ?

Juste parler de non-linéarité.

[preuve compteur semantically secure](https://crypto.stackexchange.com/questions/88753/question-on-the-cpa-security-proof-of-the-ctr-mode)

[hmac vs poly1305](https://crypto.stackexchange.com/questions/56429/which-algorithm-has-better-performance-hmac-umac-and-poly1305)
[tls AEAD 1.3 chacha poly](https://www.youtube.com/watch?v=S1Awy242Vf8)

faire :

1. problème
2. réponse avec type attaque
