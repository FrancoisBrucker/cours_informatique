---
layout: layout/post.njk

title: Key derivation

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

- key stretching
- key derivation

> TBD déplacer de tls ici.
> argon2, <https://en.wikipedia.org/wiki/PBKDF2>


> TBD verbose d'une communication tsl 1.3

> <https://en.wikipedia.org/wiki/Terrapin_attack>

{% lien %}
<https://www.youtube.com/watch?v=diBR4Jcscvs>
{% endlien %}

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

