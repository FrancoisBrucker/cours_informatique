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
           k                   k
           |                   |
           v                   v
        -------             -------
       |       |           |       |
 m --> |   E   | --> c --> |   D   | --> m
       |       |           |       |
        -------             -------
```

Deux types d'attaques :

- brute-force : énumération des clés
- connaissances supplémentaires :
  - _a priori_ sur $m$ si l'attaque est chiffre seul
  - acquises si on peut avoir ou produire des couples (message, chiffre)

On considère actuellement que si le [nombre de clés est supérieur à $2^{128}$](https://en.wikipedia.org/wiki/Key_size#Brute-force_attack), l'approche brute-force n'est pas profitable car il faudrait un temps de déchiffrage supérieure à la durée de vie du message. Si l'on utilise des connaissances supplémentaires, il est possible de faire baisser ce nombre drastiquement.

{% lien %}
[recommendations ANSSI taille de clés](https://www.ssi.gouv.fr/administration/guide/mecanismes-cryptographiques/)
{% endlien %}

## Qu-est ce que la confidentialité ?

{% aller %}
[Partager la clé](partager-secret){.interne}
{% endaller %}

On a vu que la confidentialité du partage de la clé était basé sur la difficulté algorithmique du logarithme discret. Mais qu'un seul maillon soit faible (side channel attack) peut faire écrouler tout l'édifice. Essayons de formaliser tout ça :

{% aller %}
[Définitions de la confidentialité](définitions){.interne}
{% endaller %}

Le message ne doit pouvoir être lu que par son destinataire. Comment partager la clé en secret ?

## Chiffrer un message

Les algorithmes de chiffrement classiques ne permettent pas de chiffrer des message de taille quelconque. Ils sont conçus pour chiffrer des blocs de taille fixes.

### Chiffrer un message de taille fixe

{% aller %}
[Chiffrer un bloc](chiffrer-un-bloc){.interne}
{% endaller %}

### Chiffrer un message de taille quelconque

Il existe historiquement deux types de codes même si les différences commencent à s'estomper entres eux :

- les codes en flux qui vont se comporter comme le code de Vernam
- les code en bloc qui vont découper le message en blocs et chiffrer chacun d'entre eux avec un permutation.

{% aller %}
[Schéma général](./schéma-général){.interne}
{% endaller %}

### Attention aux implémentations

Les [side channel attacks](partager-secret/#side-channel-attack){.interne} permettent, on l'a vue, de tirer parie de l'implémentation de l'algorithme pour obtenir un avantage npn négligeable. Pour qu'aucune information ne transparaisse, il faut que l'algorithme :

1. fasse tout le temps la même chose
2. consomme la même énergie
3. ...

Bref, n'implémentez pas vous même les algorithmes, prenez des implémentations éprouvées.

{% lien %}

- [channel attack exemples](https://www.youtube.com/watch?v=GPwNFrpd1KU)
- [Attaques sur Machines embarquées](https://www.ssi.gouv.fr/agence/publication/combined-fault-and-side-channel-attack-on-protected-implementations-of-aes/)

{% endlien %}

## Générer des clés

### Générateur de nombre aléatoire cryptographique

> TBD LSFR

{% lien %}
Rapport de stage sur les codes LSFR : [projet codes LSFR](Rapport_de_Stage_Laura_Michelutti.pdf)
{% endlien %}

### Trouver la clé

Il faut utiliser des générateur avec entropie. Il n'est pas utile de retrouver le nombre ensuite.

> TBD `/dev/random`{.fichier} ou `/dev/urandom`{.fichier}
> TBD : faire grossir partie [aléatoire](aléatoire){.interne}

### Key derivation function

{% lien %}
[Key derivation function](https://en.wikipedia.org/wiki/Key_derivation_function)
{% endlien %}

Les protocole vont avoir besoin de tout un tas de clés différentes. Une pour chaque message à transmettre et pour chaque messages. La façon la plus simple, si on a un PRF sous la main est de :

- posséder une clé primaire appelée $SK$ (_source key_)
- une constante $CTX$, application dépendante pour éviter que plusieurs applications différentes utilisant la même clé primaires de se trouvent avec les mêmes clés

Puis il suffit d'étier le process à chaque fois que l'in veut une clé avec : $F(\text{SK}, \text{CTX} || i)$, où $i$ est un compteur.
