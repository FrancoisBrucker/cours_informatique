---
layout: layout/post.njk

title: Sécurité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La thématique de la *sécurité* en informatique traite de l'échange de messages entre un expéditeur et un destinataire via un canal public tout en respectant les quatre principes suivant :

- ***confidentialité*** : le message ne doit pouvoir être lu que par son destinataire.
- ***intégrité*** : le message ne doit pas être altéré entre son envoi et sa réception
- ***authentification*** :
  - l'expéditeur doit être sur de l'identité du destinataire
  - le destinataire doit être sur de l'identité de l'expéditeur
- ***non-répudiation*** : l'expéditeur ne doit pas pouvoir nier être l'auteur du message a posteriori

La mise en œuvre de ces quatres principes va nécessiter la mise en place de ***protocoles*** : une séries d'étapes à effectuer par au moins **deux** entités (homme ou machine) en vu de réaliser une tâche.

Enfin, ces protocoles vont souvent nécessiter des algorithmes (une séries d'étapes à effectuer par **une** entité) pour être correctement mis en œuvre.

L'usage (depuis "applied cryptography" ?) est de personifier les différentes parties prenantes d'un protocole :

- Les ***joueurs*** sont les personnes voulant s'échanger un message en suivant un protocole donné :
  - Alice veut envoyer un message sécurisé à Bob
  - on ajoute Carol puis Dave si d'autres personnes sont impliquées
- Les ***adversaires*** voulant perturber le protocole. Ces adversaires sont de deux niveaux de difficulté :
  - Niveau 1 : Eve. Elle ne peut qu'observer le protocole et les échanges
  - Niveau 2 : Mallory. Il peut en plus modifier tout ce qui est public : messages et paramètres public du protocole
- Les ***tiers de confiance*** (arbitres incorruptibles), non impliquées dans l'échange du message mais nécessaires au bon fonctionnement du protocole (tous les protocoles ne nécessitent pas de tiers de confiance)

On supposera de plus toujours que le protocole, les algorithmes utilisés et leurs implémentations effectives sont connus de tous, joueurs et adversaires. La confidentialité ne devant être garantie que via un paramètre du protocole nommé ***clé***, uniquement connu des joueurs. Cette hypothèse est connue sous le nom de [le principe de Kerckhoffs](https://fr.wikipedia.org/wiki/Principe_de_Kerckhoffs).

Enfin, on considérera que les adversaires ne sont pas stupides et ont à leur disposition des outils modernes et performants.

## Cryptologie

{% lien %}
[Introduction à la cryptologie (ANSSI)](https://www.ssi.gouv.fr/particulier/bonnes-pratiques/crypto-le-webdoc/cryptologie-art-ou-science-du-secret/)
{% endlien %}

La cryptologie, ou science du secret est l'étude des protocoles de sécurités. Elle possède deux branches :

- la cryptographie qui crée les algorithmes et protocoles de sécurité
- la cryptanalyse qui attaque ces algorithmes pour tester leurs robustesse

A moins d'être un professionnel du domaine, ne créez pas votre propre protocole ni n'implémentez vous même les algorithmes de cryptographies qui les composent. Utilisez les protocoles connus via des bibliothèques reconnues, cela vous évitera de vous croire en sécurité alors que vous ne l'êtes pas (il vaut mieux pas de sécurité qu'une mauvaise sécurité).

## Confidentialité

{% aller %}
[Confidentialité](./confidentialité){.interne}
{% endaller %}

## Intégrité

{% aller %}
[Intégrité](./intégrité){.interne}
{% endaller %}

## Authentification

{% aller %}
[Authentification](./authentification){.interne}
{% endaller %}

## Communication

### tls

> TBD

### ssh

> TBD SSH : <https://www.linkedin.com/pulse/understanding-ssh-encryption-connection-process-robert-althof>
> ,https://bash-prompt.net/guides/bash-ssh-ciphers/

### gpg

> TBD

## Bibliographie

- [*Applied Cryptography, protocols algorithms and source code in C* de Bruce Schneier](https://www.amazon.fr/Applied-Cryptography-Protocols-Algorithms-Source/dp/1119096723). Un peu vieux maintenant concernant les algorithmes, mais toujours utile pour une description des protocoles (qui eux sont toujours utilisés)
- [*Serious Cryptography: A Practical Introduction to Modern Encryption*, Jean-Philippe Aumasson](https://www.amazon.fr/Serious-Cryptography-Practical-Introduction-Encryption/dp/1593278268) Très bonne introduction aux méthodes actuelles de cryptographie
- [*pgp & gpg assurer la confidentialité de ses e-mails et fichiers*](https://www.amazon.fr/PGP-GPG-confidentialit%C3%A9-mails-fichiers/dp/221212001X) pour l'utilisation de GPG
- [*A Graduate Course in Applied Cryptography* de Dan Boneh et   Victor Shoup](https://toc.cryptobook.us/) cours détaillé donné à Standford

## misc

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
[poly1305](https://en.wikipedia.org/wiki/Poly1305)

[https](https://www.youtube.com/watch?v=OU-e_Qz-v4U&list=PLql0J2JIDXdOREGUibCXlsevKDK4o8EzN)

[tls handshake](https://www.youtube.com/watch?v=86cQJ0MMses)

[hash propriété et autres](https://membres-ljk.imag.fr/Bruno.Grenet/IntroCrypto/4.HashFunctions.pdf)

[sha 3 sponge function](https://www.youtube.com/watch?v=bTOJ9An9wpE)
[sponge function thm](https://keccak.team/files/SpongeFunctions.pdf)

[sha 1 collision](https://www.youtube.com/watch?v=Zl1TZJGfvPo)
[sha choses](https://crypto.stackexchange.com/questions/25233/shacal-2-vs-aes-as-underlying-block-cipher-for-secure-hash-aka-sha-256)

PRF -> stream
PRP -> block

on peut faire un prp à partir d'un prf (Feistel) et si espace assez grand prp = prf.

- faire une partie anneau/corps z/pz
- importance d'Euclide et Euclide étendu
- complexité des algos

histoire :
- xor et ses propriétés
- attrention aux fréquences :
  - cesar, vegnere, ...
  - xor en bloc
- ne pas se répéter

- [integer factorization](https://en.wikipedia.org/wiki/Integer_factorization)
- opération binaire :
  - addition
  - soustraction (complément à deux)
  - multiplication
  - division entière
  - modulo (division, multiplication, soustraction)
  - pgcd (méthode binaire)
- Euclide étendu
- factorisation
- exponentiation modulaire
- logarithme modulaire

tout doit rester aléatoire pour ne donner aucune info. Si info, même très petite on en déduit un algo

[tuto encryption](https://www.youtube.com/watch?v=oVCCXZfpu-w)
[tuto aes-gcm](https://www.youtube.com/watch?v=Q4EmXJTwcdo)
[galois counter mode of operation ref](https://csrc.nist.rip/groups/ST/toolkit/BCM/documents/proposedmodes/gcm/gcm-spec.pdf)

TB : [AES en dessin](https://www.youtube.com/watch?v=pSCoquEJsIo)
[AEDS GCM](https://www.youtube.com/watch?v=g_eY7JXOc8U)

[blake](https://crypto.stackexchange.com/questions/75754/why-is-the-core-chacha-primitive-not-good-for-use-in-a-crcf-why-create-blake)
[blake wikipedia](https://en.wikipedia.org/wiki/BLAKE_(hash_function))

[ssh en 10min](https://www.youtube.com/watch?v=3-MDtASgSo8)
[ssh en 5 parties](https://www.youtube.com/watch?v=QGixbJ9prEc&list=PLQqbP89HgbbYIarPqOU8DdC2jC3P3L7a6)
[ssh crash course](https://www.youtube.com/watch?v=hQWRp-FdTpc)

[https](https://www.youtube.com/watch?v=OU-e_Qz-v4U&list=PLql0J2JIDXdOREGUibCXlsevKDK4o8EzN&index=1)

man in the middle attaque pour échange de clés. De l'utilité des clés public/privées

[durée de vie de la clé TLS](https://security.stackexchange.com/questions/55454/how-long-does-an-https-symmetric-key-last)
faire :

1. problème
2. de quoi on veut se protéger (attaque)
3. réponse possible


<https://fr.wikipedia.org/wiki/Transport_Layer_Security>
<https://www.ssi.gouv.fr/uploads/2020/03/anssi-guide-recommandations_de_securite_relatives_a_tls-v1.2.pdf>

Arriver à tls et se poser la question du man in the middle.

-> Du coup rsa.

On ne prend pas tout le temps rsa à cause du temps (100 fois plus long ?)

[binary gcd algorithm](https://en.wikipedia.org/wiki/Binary_GCD_algorithm)
