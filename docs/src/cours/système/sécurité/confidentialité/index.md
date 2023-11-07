---
layout: layout/post.njk

title: Confidentialité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


```
         k               k
         |               | 
         v               v
       _____           _____
       | v |           | v |
       |   |           |   |
 m --> | E | --> c --> | D | --> m
       -----           -----
```

Deux types d'attaques :

- brute-force : énumération des clés
- connaissances supplémentaires :
  - *a priori* sur $m$ si l'attaque est chiffre seul
  - acquises si on peut avoir ou produire des couples (message, chiffre)

On considère **en 2024** que si le [nombre de clés est supérieur $2^{128}$](https://en.wikipedia.org/wiki/Key_size#Brute-force_attack), l'approche brute-force n'est pas profitable car il faudrait un temps de déchiffrage supérieure à la durée de vie du message. Si l'on utilise des connaissances supplémentaires, il est possible de faire baisser ce nombre drastiquement.

{% lien %}
[recommendations ANSSI taille de clés](https://www.ssi.gouv.fr/administration/guide/mecanismes-cryptographiques/)
{% endlien %}

## Codes historiques

{% aller %}
[Codes historiques](codes-historiques){.interne}
{% endaller %}

## Qu-est ce que la confidentialité ?

{% aller %}
[Définitions de la confidentialité](définitions){.interne}
{% endaller %}

## Types de code

### Stream

{% aller %}
[chiffrement en flux](chiffre-flux){.interne}
{% endaller %}

### Bloc

{% aller %}
[chiffrement par bloc](chiffre-bloc){.interne}
{% endaller %}

### Attention aux implémentations

#### Side channel Attack

- [exemples de side channel attack](https://www.youtube.com/watch?v=GPwNFrpd1KU)
- [side channel attack](https://fr.wikipedia.org/wiki/Attaque_par_canal_auxiliaire)
- [Attaques sur Machines embarquées](https://www.ssi.gouv.fr/agence/publication/combined-fault-and-side-channel-attack-on-protected-implementations-of-aes/)

Il faut que l'algorithme :

1. fasse tout le temps la même chose
2. consomme la même énergie
3. ...

Bref, n'implémentez pas vous même les algorithmes, prenez des implémentations éprouvées.

## Partager le secret

Le message ne doit pouvoir être lu que par son destinataire.

{% aller %}
[Partager la clé](partager-secret){.interne}
{% endaller %}

## Générer des clés

### Trouver la clé

Il faut utiliser des générateur avec entropie. Il n'est pas utile de retrouver le nombre ensuite.

> TBD /dev/random ou /dev/urandom

### Clé maître

Les protocole vont avoir besoin de tout un tas de clés différentes. Une pour chaque message à transmettre et pour chaque message, on a souvent besoin d'un [nonce](https://en.wikipedia.org/wiki/Cryptographic_nonce).

On utilise une clé maître puis elle se dérive en plusieurs autres clés qu'elle génère.

> TBD expliquer pour de vrai.
