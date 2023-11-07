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

Il existe historiquement deux types de codes, même si les différences commencent à s'estomper entres eux. Bien que basés sur des approches différentes, ils ont en commun le soucis d'éviter les attaques classiques en particulier la [cryptanalyse linéaire](https://fr.wikipedia.org/wiki/Cryptanalyse_lin%C3%A9aire).

De à chaque méthode de chiffrement va avoir une partie de transformation non linéaire. Il faut que ces opérations soient choisies avec soin pour éviter tout biais. La moindre linéarité cachée pouvant être facilement utilisée comme attaque.

Il faut cependant que ces opérations soient clairement définies, ce qui est le cas avec les deux méthodes de chiffrement populaire : chacha20 (qui utilise l'addition) ou AES (les inverse de groupes de Galois).

{% info %}
DES proposait des[S-box](https://fr.wikipedia.org/wiki/S-Box) obscures qui ont toujours laissé des doutes quant à la sincérité de ces non-linéarités.
{% endinfo %}

### Stream cipher

{% aller %}
[chiffrement en flux](chiffre-flux){.interne}
{% endaller %}

### Bloc cipher

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

> TBD `/dev/random`{.fichier} ou `/dev/urandom`{.fichier}

### Key derivation function

{% lien %}
[Key derivation function](https://en.wikipedia.org/wiki/Key_derivation_function)
{% endlien %}

Les protocole vont avoir besoin de tout un tas de clés différentes. Une pour chaque message à transmettre et pour chaque messages. La façon la plus simple, si on a un PRF sous la main est de :

- posséder une clé primaire appelée $SK$ (*source key*)
- une constante $CTX$, application dépendante pour éviter que plusieurs applications différentes utilisant la même clé primaires de se trouvent avec les mêmes clés

Puis il suffit d'étier le process à chaque fois que l'in veut une clé avec : $F(SK, CTX || i)$, où $i$ est un compteur.
