---
layout: layout/post.njk

title: Sécurité
tags: ['cours', 'sécurité', 'cryptographie']
authors:
    - "François Brucker"

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Embryon de cours de sécurité. On y verra essentiellement les fondements gryptographique de la sécurité.

<!-- fin résumé -->

> TBD montrer avec openssh comment le faire (voir serious cryptography)

## Cryptographie

{% aller %}

[Cryptographie](./cryptographie){.interne}

{% endaller %}



## Communication

### OpenPGP

{% aller %}

[OpenPGP](./openpgp){.interne}

{% endaller %}

### TLS

Le protocole derrière toute communication sécurisée

{% aller %}
[Transport Layer Security](./tls){.interne}
{% endaller %}

### https

{% lien %}
[https](https://www.youtube.com/watch?v=OU-e_Qz-v4U&list=PLql0J2JIDXdOREGUibCXlsevKDK4o8EzN)
{% endlien %}

[Certificats X.509](https://fr.wikipedia.org/wiki/X.509) :

1. certifiant (*issuer*) :
   1. nom
   2. adresse
2. possesseur du certificat (*subject*) :
   1. nom
   2. adresse
   3. clé publique
3. plage de validités du certificat (de quand à quand)
4. signature du certifiant : un hash du certificat chiffré avec sa clé privée

Lorsque l'on reçoit la signature :

1. hash le certificat
2. déchiffre la signature du certificat avec la clé publique du certifiant
3. si les hash coincident c'est bon

Qui certifie :

1. root authority délivre des certificat aux intermediate authority
2. les intermediate authority certifient :
   1. d'autres intermediate authority
   2. des serveur directement

C'est une chaîne de confiance. Lorsqu'un serveur se connecte on lui présente son certificat. On peut alors remonter la chaîne de confiance, en allant sur le site web du certifiant pour examiner le certifiant du certifiant, jusqu'à root si nécessaire.

## Arithmétique

{% aller %}
[Arithmétique](./arithmétique){.interne}
{% endaller %}

{% lien %}

[arithmétique pour la cryptographie](https://www.youtube.com/watch?v=oRM-gNrbcgE&list=PL024XGD7WCIEii2U_HKeprCTJA4xb-uJ6&index=1)

{% endlien %}
