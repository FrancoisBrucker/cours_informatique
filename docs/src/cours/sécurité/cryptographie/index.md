---
layout: layout/post.njk

title: Cryptographie

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


La thématique de la *sécurité* en informatique traite de l'échange de messages entre un expéditeur et un destinataire via un canal public tout en respectant les quatre principes suivant :

- ***confidentialité*** : le message ne doit pouvoir être lu que par son destinataire.
- ***intégrité*** : le message ne doit pas être altéré entre son envoi et sa réception
- ***authentification*** :
  - l'expéditeur doit être sur de l'identité du destinataire
  - le destinataire doit être sur de l'identité de l'expéditeur
- ***non-répudiation*** : l'expéditeur ne doit pas pouvoir nier être l'auteur du message a posteriori

Les expéditeurs et destinataires du messages ne sont pas forcement distincts, lors du chiffrage de données sur un disque dur par exemple. On distingue ainsi deux mode de chiffrement :

- transport : le message est chiffré avant le transport et déchiffré une fois arrivé à bon port
- stockage : le message est chiffré pour être stocké en mémoire ou sur le disque. Il est déchiffré avant d'être lu.

La mise en œuvre de ces quatres principes va nécessiter la mise en place de ***protocoles*** : une séries d'étapes à effectuer par au moins **deux** entités (homme ou machine) en vu de réaliser une tâche.

Enfin, ces protocoles vont souvent nécessiter des algorithmes (une séries d'étapes à effectuer par **une** entité) pour être correctement mis en œuvre.

L'usage (depuis "applied cryptography" ?) est de personifier les différentes parties prenantes d'un protocole :

- Les ***joueurs*** sont les personnes voulant s'échanger un message en suivant un protocole donné :
  - Alice veut envoyer un message sécurisé à Bob
  - on ajoute Carol puis Dave si d'autres personnes sont impliquées
- Les ***adversaires*** voulant perturber le protocole. Ces adversaires sont de deux niveaux de difficulté :
  - Niveau 1 : Eve. Elle ne peut qu'observer le protocole et les échanges
  - Niveau 2 : Mallory. Il peut en plus modifier tout ce qui est public : messages et paramètres public du protocole
- Les ***tiers de confiance*** (arbitres incorruptibles), non impliquées dans l'échange du message mais nécessaires au bon fonctionnement du protocole (tous les protocoles ne nécessitent pas de tiers de confiance)

On supposera de plus toujours que le protocole, les algorithmes utilisés et leurs implémentations effectives sont connus de tous, joueurs et adversaires. La confidentialité ne devant être garantie que via un paramètre du protocole nommé ***clé***, uniquement connu des joueurs. Cette hypothèse est connue sous le nom du [principe de Kerckhoffs](https://fr.wikipedia.org/wiki/Principe_de_Kerckhoffs).

Enfin, on considérera que les adversaires ne sont pas stupides et ont à leur disposition des outils modernes et performants.

## Cryptologie

{% lien %}
[Introduction à la cryptologie (ANSSI)](https://www.ssi.gouv.fr/particulier/bonnes-pratiques/crypto-le-webdoc/cryptologie-art-ou-science-du-secret/)
{% endlien %}

La cryptologie, ou science du secret est l'étude des protocoles de sécurités. Elle possède deux branches :

- la [cryptographie](https://fr.wikipedia.org/wiki/Cryptographie) qui crée les algorithmes et protocoles de sécurité
- la [cryptanalyse](https://fr.wikipedia.org/wiki/Cryptanalyse) qui attaque ces algorithmes pour tester leurs robustesse

À moins d'être un professionnel du domaine, ne créez pas votre propre protocole ni n'implémentez vous même les algorithmes de cryptographies qui les composent. Utilisez les protocoles connus via des bibliothèques reconnues, cela vous évitera de vous croire en sécurité alors que vous ne l'êtes pas (il vaut mieux pas de sécurité qu'une mauvaise sécurité).

{% lien %}
[Site de l'ANSSI](https://cyber.gouv.fr/)
{% endlien %}

### Cryptographie

Pour qu'un message $m$ puisse passer de Alice à Bob via un canal public sans qu'Eve ne puisse le lire, il faut qu'il soit ***chiffré*** (*encrypted*) par une fonction $E(m) = c$ pendant son passage dans le canal public, puis ***déchiffré*** (*decrypted*) par une autre fonction $D(c) = m$.

{% info %}
Les fonctions de chiffrements et de déchiffrements sont appelés *cipher* en anglais ; le message $m$ est appelé *plain text* et le message chiffré $c$ : *ciphertext*.
{% endinfo %}

Mais comme Eve connaît (ou peut soudoyer quelqu'un pour connaître) $E()$ et $D()$, il faut que ces fonctions possèdent un paramètre en plus : une clé $k$, connue uniquement d'Alice et Bob :

```
    Alice    |  Eve   |     Bob
-------------|--------|-------------- 
    m, k     |        |      k 
             |        |
E(k, m) = c -|-- c ---|----> c
             |        | D(k, c) = m
             |        |
espace privé | public |    privé  
```

En supposant qu'Eve ne possède pas d'autre information que le message chiffré, si elle veut prendre connaissance de $m$ sans connaître $k$, on dit ***décrypter*** $c$, il lui faut tester $E(k', m)$ pour toutes les combinaisons $k'$ de clés possibles.

La communication est alors confidentielle si le temps nécessaire pour faire tout ces essais est supérieur à la durée de validité du message chiffré.

De part la nature algorithmique de secret, la confidentialité de la transmission de $m$ via $E(k, m)$ n'est garantie que si :

- $D(k, E(k, m)) = m$
- Eve ne peut obtenir aucune information sur $k$ ou $m$ à partir de $E(k, m)$
- le temps nécessaire pour décrypter le message en utilisant toutes les clé possible est prohibitif.

Formalisons tout cela.

#### Cohérence

Dans toutes leur généralité les fonctions $E$ et $D$ sont définies :

- $E : \mathcal{K} \times \mathcal{M} \rightarrow \mathcal{C}$
- $D : \mathcal{K} \times \mathcal{C} \rightarrow \mathcal{M}$

Pour le chiffrement soit effectif, il faut qu'il soit :

- ***cohérent*** : $D(k, E(k, m)) = m$ pour tout $m \in \mathcal{M}$
- ***efficace*** (*efficient*) : $D$ et $E$ sont des algorithmes polynomiaux et s'ils sont linéaires c'est encore mieux.

On peut se restreindre, sans perte de généralité, aux messages binaires et supposer que $\mathcal{M} = \mathcal{C}$. On a alors :

- $\mathcal{K} = \\{0, 1\\}^K$
- $\mathcal{M} = \mathcal{C} = \\{0, 1\\}^L$
- $E$ et $D$ doivent être de complexité $\mathcal{O}((K+L)^d)$ avec $d$ une constante valant de préférence 1.

#### Robustesse

Il faut que le code puisse résister aux tentatives de décryptage. La résistance d'un code dépend du type d'attaque auquel il doit faire face.

Cependant, tout code doit faire en sorte qu'aucune information sur $m$ ou $k$ ne puisse être déduite à partir de $E(k, m)$. Toute information, même minuscule, peut être transformée en algorithme par un cryptanalyste et utilisé pour compromettre la sécurité du code.

### Cryptanalyse

Les tentatives de décryptage d'un message chiffré, on parle d'***attaques*** peuvent s'échelonner en 4 niveaux, selon les possibilités de l'attaquant :

1. ***chiffres uniquement*** (*Ciphertext-only attackers, COA*). L'attaquant est passif et n'a accès qu'a des textes chiffrés $c$ sans connaître les messages initiaux.
2. ***messages connus*** (*Known-plaintext attackers, KPA*). L'attaquant est passif et des message ainsi que leurs chiffrement
3. ***messages choisis*** (*Chosen-plaintext attackers, CPA*). L'attaquant est actif et peut choisir des messages à chiffrer.
4. ***chiffres choisis*** (*Chosen-ciphertext attackers, CCA*). L'attaquant est actif et peut chiffrer et déchiffrer les message. Dans ce type d'attaque, l'attaquant chercher à connaître la clé de chiffrage.

## Confidentialité

{% aller %}
[Confidentialité](./confidentialité){.interne}
{% endaller %}

{% lien %}
Rapport de stage sur les codes LSFR : [projet codes LSFR](Rapport_de_Stage_Laura_Michelutti.pdf)
{% endlien %}

## Intégrité

{% aller %}
[Intégrité](./intégrité){.interne}
{% endaller %}

## Authentification

{% aller %}
[Authentification](./authentification){.interne}
{% endaller %}

## Bibliographie

- [*Applied Cryptography, protocols algorithms and source code in C* de Bruce Schneier](https://www.amazon.fr/Applied-Cryptography-Protocols-Algorithms-Source/dp/1119096723). Un peu vieux maintenant concernant les algorithmes, mais toujours utile pour une description des protocoles (qui eux sont toujours utilisés)
- [*Serious Cryptography: A Practical Introduction to Modern Encryption*, Jean-Philippe Aumasson](https://www.amazon.fr/Serious-Cryptography-Practical-Introduction-Encryption/dp/1593278268) Très bonne introduction aux méthodes actuelles de cryptographie
- [*pgp & gpg assurer la confidentialité de ses e-mails et fichiers*](https://www.amazon.fr/PGP-GPG-confidentialit%C3%A9-mails-fichiers/dp/221212001X) pour l'utilisation de GPG
- [*A Graduate Course in Applied Cryptography* de Dan Boneh et   Victor Shoup](https://toc.cryptobook.us/) cours détaillé donné à Standford
- [ANSSI](https://www.ssi.gouv.fr/)
- [proof in cryptography](https://www.youtube.com/watch?v=Js9dCUFjAhc&list=PL9mNSKC0i-d8VKahrLPoEbUJgo9BwfMQ5&index=1)
