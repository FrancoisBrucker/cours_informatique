---
layout: layout/post.njk

title: TLS

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


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
