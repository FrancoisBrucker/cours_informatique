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

## Usage

{% aller %}
[Codes](./codes){.interne}
{% endaller %}

### Codes symétriques

rapide et efficace si la clé est grande mais la clé doit être partagée par le codeur et le décodeur.

{% aller %}
[symétriques](./symétriques){.interne}
{% endaller %}

### Codes asymétriques

Échange de (petits) secrets

<https://fr.wikipedia.org/wiki/Cryptographie_asym%C3%A9trique>

> def : asymétrique : clé de chiffrement != clé de déchiffrement.
> 

> si clé de déchiffrement difficile à trouver à partir de la clé de chiffrement, la clé de chiffrement peut être connue.
>
> intérêt :

> TBD durée de vie du message
> exemple : <https://fr.wikipedia.org/wiki/Chiffrement_RSA>
Nous ajouterons égale

Le but de la  est de permettre :

<https://fr.wikipedia.org/wiki/Cryptographie_asym%C3%A9trique>

1. de transformer un message $m$ en un message $m'$ ne permettant pas de connaître $m$
2. de transformer $m'$

{% aller %}
[RSA](./RSA){.interne}
{% endaller %}

### Méthode hybride

RSA peut encrypter un nombre plus petit que $n$. On pourrait décomposer un message plus gros en paquets de $T$ bits avec $2^T < n$ mais ce n'est quasi-jamais fait car le codage/décodage est algorithmiquement long.

On utilise des techniques [PGP](https://fr.wikipedia.org/wiki/Pretty_Good_Privacy) pour cela.

{% lien %}
Encoder un fichier avec RSA et un code symétrique :

<https://kulkarniamit.github.io/whatwhyhow/howto/encrypt-decrypt-file-using-rsa-public-private-keys.html>
{% endlien %}

## Signature électronique

{% lien %}
<https://fr.wikipedia.org/wiki/Certificat_%C3%A9lectronique>
{% endlien %}

* document à certifier
* condensat (ou [somme de contrôle/checksum](https://fr.wikipedia.org/wiki/Somme_de_contr%C3%B4le)) est un hash du contenu du document.

Le document à certifier peut être un fichier ou des informations.

{% info %}
Comme fonction de hash on utilise souvent [MD5](https://fr.wikipedia.org/wiki/MD5) ou [sha-1](https://fr.wikipedia.org/wiki/SHA-1)
{% endinfo %}

Le condensat est un moyen efficace de savoir si un document a été modifié car deux documents différents auront un condensat différent (la probabilité que deux document différents aient le même condensat est infinitésimale).

En soit, le condensat permet de vérifier l'intégrité d'un fichier si on peut assurer qu'il a bien été émis par le créateur du fichier. Pour cela, le condensat est crypté avec la clé privée du créateur du fichier. Le condensat crypté est appelé ***signature***

Vérifier l'intégrité d'un fichier se fait alors en trois étapes :

1. on calcule le condensat du fichier
2. on décrypte la signature avec la clé public du créateur du fichier
3. on compare les les deux condensats :
   * si les condensats sont identiques le fichier est dans l'état donné par le créateur
   * si les condensats sont différents le fichier a été modifié

## Tiers de confiance et keyring

> TBD : attaque du man in the middle.

* Tiers de confiance : certificat (pour le https, boot sécurisé)
* Keyring : ensemble de clés publique de confiance (pour l'installation de packages de mainteneur connu par exemple)

<https://wiki.archlinux.org/title/Pacman/Package_signing>

* keyring ubuntu : <https://www.malekal.com/comment-ajouter-des-cles-de-signature-a-apt-sur-debian-ubuntu-mint/>
* exemple vscode : <https://code.visualstudio.com/docs/setup/linux>
