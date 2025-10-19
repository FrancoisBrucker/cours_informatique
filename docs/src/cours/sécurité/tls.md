---
layout: layout/post.njk

title: TLS

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD verbose d'une communication tsl 1.3

> <https://en.wikipedia.org/wiki/Terrapin_attack>

## Key derivation function

> TBD si autre message.

{% lien %}

- [Définition](https://en.wikipedia.org/wiki/Key_derivation_function)
- [Usage](https://blog.trailofbits.com/2025/01/28/best-practices-for-key-derivation/)

{% endlien %}

Les protocole vont avoir besoin de tout un tas de clés différentes. Une pour chaque message à transmettre et pour chaque messages. La façon la plus simple, si on a un PRF sous la main est de :

- posséder une clé primaire appelée $SK$ (_source key_)
- une constante $CTX$, application dépendante pour éviter que plusieurs applications différentes utilisant la même clé primaires de se trouvent avec les mêmes clés

Puis il suffit d'étier le process à chaque fois que l'in veut une clé avec : $F(\text{SK}, \text{CTX} || i)$, où $i$ est un compteur.

> TBD rekeying. Attention au passé <https://blog.cr.yp.to/20170723-random.html> car on ne génère qu'un bout.
> TBD ? <https://crypto.stackexchange.com/questions/53295/using-chacha20-as-a-prng-with-a-variable-length-seed>

### hash based KDF

- <https://en.wikipedia.org/wiki/PBKDF2>

- <https://blog.boot.dev/cryptography/key-derivation-functions/>
- <https://www.youtube.com/watch?v=gTaOccTY9bc>

<https://www.cryptolux.org/index.php/Argon2>
<https://master-spring-ter.medium.com/from-basics-to-expert-a-deep-dive-into-argon2-password-hashing-95d17ba3b10f>

```shell
❯ echo -n "je te hash" | argon2 "des grains de sel" -l 50
Type:           Argon2i
Iterations:     3
Memory:         4096 KiB
Parallelism:    1
Hash:           62ac773d564f583c593e6091c72eeb48766fc1d1e314afdce0bc175328e98afbca29a5078035152cdac35d2720d9cc6cb4e3
Encoded:        $argon2i$v=19$m=4096,t=3,p=1$ZGVzIGdyYWlucyBkZSBzZWw$Yqx3PVZPWDxZPmCRxy7rSHZvwdHjFK/c4LwXUyjpivvKKaUHgDUVLNrDXScg2cxstOM
0.014 seconds
Verification ok

```

{% lien %}
[TLS](https://www.youtube.com/watch?v=0TLDTodL7Lc)
{% endlien %}

pare les attaques :

- [man in the middle attack](https://fr.wikipedia.org/wiki/Attaque_de_l'homme_du_milieu) : authentification
- [replay attack](https://fr.wikipedia.org/wiki/Attaque_par_rejeu) : un NONCE identifie chaque session
- [downgrade attack](https://fr.wikipedia.org/wiki/Attaque_par_repli) : refuse les protocoles non sécurisés.

1. être sûr de à qui on parle (évite attaque man un the middle)
2. échange de la clé maître et du mode de chiffrement
3. échange des messages par chiffrement symétrique

Le protocole TLS se place entre la couche TCP et l'application. 

## TLS Handshake

{% lien %}

- [TLS handshake](https://www.youtube.com/watch?v=86cQJ0MMses)
- [TLS handshake détails](https://cabulous.medium.com/tls-1-2-andtls-1-3-handshake-walkthrough-4cfd0a798164)

{% endlien %}

La mise en route du protocole, le handshake est très rapide. Initiation d'un communication entre Alice et Bob :

> TBD [Protocole utilisés](https://ciphersuite.info/cs/)

1. Alice envoie un message d'authentification
2. Bob envoie un message d'authentification
3. Alice annonce les protocoles qu'elle peut utiliser pour l'AEAD
4. Bob lui répond le protocole qui'il choisit
5. Alice envoie sa partie du secret
6. bob envoie sa partie du secret

La communication peut ensuite commencer en utilisant une clé dérivée

Avec TLS 1.3, les 6 étapes ci-dessus se font en 1 seul aller/retour. Alice envoie tout ce qui est nécessaire à Bob en une fois et Bob lui répond toutes ses informations en un message.

{% lien %}
[ANSSI : recommandations de sécurité relatives à tls](https://www.ssi.gouv.fr/uploads/2020/03/anssi-guide-recommandations_de_securite_relatives_a_tls-v1.2.pdf)
{% endlien %}

## gestion des clés symétrique

> TBD : clés :
>
> - <https://crypto.stackexchange.com/questions/27131/differences-between-the-terms-pre-master-secret-master-secret-private-key>
> - [durée de vie de la clé TLS](https://security.stackexchange.com/questions/55454/how-long-does-an-https-symmetric-key-last)
