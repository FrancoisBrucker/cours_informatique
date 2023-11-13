---
layout: layout/post.njk

title: GPG

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

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

## Avec gnupg

{% lien %}
[GnuPG](https://www.gnupg.org/)
{% endlien %}



[GPG](https://www.youtube.com/watch?v=DRt-SE9eZwk)

[gpg sign](https://dev.to/gers2017/how-to-sign-your-commits-with-gpg-or-ssh-keys-2cgi)

<https://opensource.com/article/19/4/gpg-subkeys-ssh>
<https://security.stackexchange.com/questions/82216/how-to-change-default-cipher-in-gnupg-on-both-linux-and-windows>

## Avec openssh

{% lien %}
Créer un fichier pgp :

1. chiffre <https://kulkarniamit.github.io/whatwhyhow/howto/encrypt-decrypt-file-using-rsa-public-private-keys.html>
2. signature <https://www.agwa.name/blog/post/ssh_signatures>
{% endlien %}
