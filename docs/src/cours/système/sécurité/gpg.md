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

On utilise des techniques [PGP](https://fr.wikipedia.org/wiki/Pretty_Good_Privacy) pour cela.

Alice veut envoyer un message $m$ à Bob :

1. authentification : Alice chiffre le hash de $m$ avec sa clé privée
2. confidentialité :
   1. une clé $k$ est générée puis chiffrée avec la clé publique de Bob
   2. le message $m$ est compressé puis chiffré avec un code symétrique et la clé $k$

On envoie à Bob :

- la signature électronique du message par Alice ($m$ chiffrée avec la clé privée d'Alice)
- la clé $k$ chiffrée avec la clé publique de Bob
- le message compressé puis chiffré

Il peut alors :

1. retrouver la clé de chiffrement $k$ en utilisant sa clé privée
2. déchiffrer le message avec la clé $k$, puis le compresser
3. vérifier que le message vient bien d'Alice en comparant le hash de $m$ avec la signature d'Alice déchiffrée avec la clé publique d'Alice

{% lien %}
Créer un fichier pgp :

<https://kulkarniamit.github.io/whatwhyhow/howto/encrypt-decrypt-file-using-rsa-public-private-keys.html>
{% endlien %}
