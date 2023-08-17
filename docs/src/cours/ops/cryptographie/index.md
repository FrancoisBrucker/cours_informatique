---
layout: layout/post.njk

title: Cryptographie

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


## Codes

crypter et décrypter des messages. Deux grandes familles :

* code symétriques où la même clé permet de crypter et décrypter le message
* code asymétriques où deux clés (publique et privée) sont utilisés :
  * la clé publique, donnée à tout le monde qui permet :
    * de crypter un message pouvant être décrypté par la clé privé
    * de décrypter un message crypté par la clé privé
  * la clé privée secrète permet :
    * de crypter un message qui pourra être décryptée par la clé publique
    * de décrypter un message crypté par la clé publique

{% aller %}
[Codes](./codes){.interne}
{% endaller %}

## Usage

### Codes symétriques

rapide et efficace si la clé est grande mais la clé doit être partagée par le codeur et le décodeur.

### Codes asymétriques

Échange de (petits) secrets

<https://fr.wikipedia.org/wiki/Cryptographie_asym%C3%A9trique>

### Méthode hybride

RSA peut encrypter un nombre plus petit que $n$. On pourrait décomposer un message plus gros en paquets de $T$ bits avec $2^T < n$ mais ce n'est quasi-jamais fait car le codage/décodage est algorithmiquement long.

On utilise des techniques [PGP](https://fr.wikipedia.org/wiki/Pretty_Good_Privacy) pour cela.

{% lien %}
Encoder un fichier avec RSA et un code symétrique :

<https://kulkarniamit.github.io/whatwhyhow/howto/encrypt-decrypt-file-using-rsa-public-private-keys.html>
{% endlien %}

## Signature électronique

<https://fr.wikipedia.org/wiki/Certificat_%C3%A9lectronique>

## Tiers de confiance et keyring

attaque du man in the middle.

<https://wiki.archlinux.org/title/Pacman/Package_signing>

* keyring ubuntu : <https://www.malekal.com/comment-ajouter-des-cles-de-signature-a-apt-sur-debian-ubuntu-mint/>
* exemple vscode : <https://code.visualstudio.com/docs/setup/linux>