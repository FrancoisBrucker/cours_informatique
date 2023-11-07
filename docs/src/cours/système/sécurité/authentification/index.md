---
layout: layout/post.njk

title: Authentification


eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


> autre signature possib le : Elgamal signature.
> 
> TBD tiers et réseau de confiance

> TBD : attaque RSA si on passe (S, E(S)). Il faut faire autrement et que Alice ait une idée de S

- asymétrique
- signature
- attaque man in the middle (tls)
- signature électronique

> TBD : pourquoi asymétrique pas utilisé pour confidentialité ? A cause du temps que ça prend (1000 fois plus ?).

> TBD : checksum vs empreinte
ajout de salt : taille du sel ?
[hash et sécurité](https://www.youtube.com/watch?v=b4b8ktEV4Bg)

- RSA : bien choisir ses clés. Sinon multiplication de Fermat

## Codes asymétriques

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

## <span id="signature"></span>Signature électronique

{% lien %}
<https://fr.wikipedia.org/wiki/Certificat_%C3%A9lectronique>
{% endlien %}

- document à certifier
- condensat (ou [somme de contrôle/checksum](https://fr.wikipedia.org/wiki/Somme_de_contr%C3%B4le)) est un hash du contenu du document.

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
   - si les condensats sont identiques le fichier est dans l'état donné par le créateur
   - si les condensats sont différents le fichier a été modifié

## Tiers de confiance et keyring

> TBD : attaque du man in the middle.

- Tiers de confiance : certificat (pour le https, boot sécurisé)
- Keyring : ensemble de clés publique de confiance (pour l'installation de packages de mainteneur connu par exemple)

<https://wiki.archlinux.org/title/Pacman/Package_signing>

- keyring ubuntu : <https://www.malekal.com/comment-ajouter-des-cles-de-signature-a-apt-sur-debian-ubuntu-mint/>
- exemple vscode : <https://code.visualstudio.com/docs/setup/linux>
