---
layout: layout/post.njk

title: OpenPGP

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[OpenPGP](https://fr.wikipedia.org/wiki/OpenPGP)
{% endlien %}

RSA peut encrypter un nombre plus petit que $n$. On pourrait décomposer un message plus gros en paquets de $T$ bits avec $2^T < n$ mais ce n'est quasi-jamais fait car le codage/décodage est algorithmiquement long.

On utilise alors une technique mixte, issue de [PGP](https://fr.wikipedia.org/wiki/Pretty_Good_Privacy), pour cela.

Supposons qu'Alice veut envoyer un message $m$ à Bob. Il faut de :

1. l'authentification : Alice chiffre le hash de $m$ avec sa clé privée
2. la confidentialité :
   1. une clé $k$ est générée puis chiffrée avec la clé publique de Bob
   2. le message $m$ est compressé puis chiffré  avec la clé $k$ (avec un chiffre symétrique)

Alice envoie à Bob :

1. la signature électronique de son message (le hash de $m$ chiffré avec sa clé privée)
2. la clé $k$ chiffrée avec la clé publique de Bob
3. le message compressé puis chiffré avec la clé $k$

Bob peut alors :

1. retrouver la clé de chiffrement $k$ en utilisant sa clé privée
2. déchiffrer le message avec la clé $k$, puis le décompresser
3. vérifier que le message vient bien d'Alice en comparant :
   - le hash du message
   - le déchiffrement de la signature avec la clé publique d'Alice.

## Avec openSSL

{% aller %}
[openssl](./openssl){.interne}
{% endaller %}

## Avec GPG

{% aller %}
[gpg](./gpg){.interne}
{% endaller %}
