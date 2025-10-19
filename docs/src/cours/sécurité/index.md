---
layout: layout/post.njk

title: Sécurité
tags: ['cours', 'sécurité', 'cryptographie']
authors:
    - "François Brucker"
resume: "Cours de sécurité. On y verra essentiellement les fondements cryptographiques."

eleventyComputed:
    eleventyNavigation:
        key: "{{ page.url }}"
        title: "{{ title | safe }}"
        parent: "{{ '../' | siteUrl(page.url) }}"
---

Embryon de cours de sécurité. On y verra essentiellement les fondements cryptographiques de la sécurité.

<!-- TBD

> TBD montrer avec openssh comment le faire (voir serious cryptography)
> TBD xor : <https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/xor/>
> TBD échange de messages avec key generation algorithm : <https://www.youtube.com/watch?v=7uEeE3TUqmU> double ratchet algorithm (<https://www.youtube.com/watch?v=9sO2qdTci-s>). Puis à plusieurs (suite du channel) MLS protocol <https://www.youtube.com/watch?v=FESp2LHd42U>

> Trop compliqué. A simplifier pour laisser les preuve et le reste pour les plus intéressés et ne garder que les principes et une preuve max par partie. 
> Ajourer des TPs.
> 
-->

## Cryptographie

{% aller %}

[Cryptographie](./cryptographie){.interne}

{% endaller %}

## Communication

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

## OpenPGP

{% aller %}

[OpenPGP](./openPGP){.interne}

{% endaller %}
