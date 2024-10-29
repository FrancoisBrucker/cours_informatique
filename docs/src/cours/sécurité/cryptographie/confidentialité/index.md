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
  - *a priori* sur $m$ si l'attaque est chiffre seul
  - acquises si on peut avoir ou produire des couples (message, chiffre)

On considère **en 2024** que si le [nombre de clés est supérieur $2^{128}$](https://en.wikipedia.org/wiki/Key_size#Brute-force_attack), l'approche brute-force n'est pas profitable car il faudrait un temps de déchiffrage supérieure à la durée de vie du message. Si l'on utilise des connaissances supplémentaires, il est possible de faire baisser ce nombre drastiquement.

{% lien %}
[recommendations ANSSI taille de clés](https://www.ssi.gouv.fr/administration/guide/mecanismes-cryptographiques/)
{% endlien %}

## Qu-est ce que la confidentialité ?

{% aller %}
[Définitions de la confidentialité](définitions){.interne}
{% endaller %}

Le message ne doit pouvoir être lu que par son destinataire. Comment partager la clé en secret ?

{% aller %}
[Partager la clé](partager-secret){.interne}
{% endaller %}

## Chiffrer un message de taille fixe

Les algorithmes de chiffrement classiques ne permettent pas de chiffrer des message de taille quelconque. Ils sont conçu pour chiffrer des blocs de taille fixes.

### Principe général

> TBD

> TBD preuves avec les jeux et les avantages et on le fait dans l'autre sens en revenant au truc le plus simple à la fin : PRF qui est un générateur à une clé coupée en 2.
> TBD insister sur le PRP qui est la brique de base. Dire ici qu'il y a aussi le PRF, qu'on peut utiliser comme brique de base d'un vernam, mais montrer qu'un prp marche aussi.

{% aller %}
[Chiffrer un bloc](chiffrement-bloc){.interne}
{% endaller %}

### Exemples

> TBD rappeler que leur existence n'est pas prouvée. DOnc on fait des essais et on donne l'algo. Pas grave puisque si PRF ou PRP c'est semantically secure.

> TBD Linéarité

Bien que basés sur des approches différentes, ces deux types de code ont en commun le soucis d'être robuste aux attaques classiques en particulier celles par [cryptanalyse linéaire](https://fr.wikipedia.org/wiki/Cryptanalyse_lin%C3%A9aire).

La cryptanalyse linéaire va chercher des corrélations linéaires entre le message $m$, le chiffre $c$ et la clé $k$, c'est à dire si :

<div>
$$
Pr[(\oplus_{i \in I} m_i) \oplus (\oplus_{j \in J} c_j) = (\oplus_{l \in L} k_l)] \leq 1/2 + \epsilon
$$
</div>

Si $\epsilon$ est non négligeable, on peut en déduire un algorithme qui va exécuter $1/\epsilon$ fois cette relation et trouver avec une grande probabilité cette corrélation, et donc l'information nécessaire à sa cryptanalyse.

> TBD calcul probabilité avec une binomiale $Pr[B(n, p) \geq 1]$.

Chaque méthode de chiffrement intègre ainsi en son sein des transformations non linéaires permettant de casser ce genre d'attaque. Il faut bien sûr que ces opérations soient choisies avec soin pour éviter tout biais, la moindre linéarité cachée pouvant être facilement utilisée comme attaque.

Enfin, pour que le calcul de ces non-linéarité soit aisé elles sont souvent placées dans des tables de conversions, nommées [S-box](https://fr.wikipedia.org/wiki/S-Box).

{% info %}
Le chiffrement DES, proposé par la NSA, proposait des [S-box](https://fr.wikipedia.org/wiki/S-Box) obscures qui ont toujours laissé des doutes quant à la sincérité de ses non-linéarités.
{% endinfo %}

{% aller %}
[Algorithme via générateur pseudo-aléatoire](générateur-xor){.interne}
{% endaller %}

{% aller %}
[Algorithme chacha20](chacha20){.interne}
{% endaller %}

{% aller %}
[Algorithme AES](aes){.interne}
{% endaller %}

## Chiffrer un message de taille quelconque

Il existe historiquement deux types de codes même si les différences commencent à s'estomper entres eux :

- les codes en flux qui vont se comporter comme le code de Vernam
- les code en bloc qui vont découper le message en blocs et chiffrer chacun d'entre eux avec un permutation.

{% aller %}
[Schéma général](./schéma-général){.interne}
{% endaller %}

### Bloc cipher

> TBD : pas encore fait. mettre bloc dans schéma général alternatif

{% aller %}
[chiffrement par bloc](chiffre-bloc){.interne}
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

### Trouver la clé

Il faut utiliser des générateur avec entropie. Il n'est pas utile de retrouver le nombre ensuite.

> TBD `/dev/random`{.fichier} ou `/dev/urandom`{.fichier}
> TBD : faire grossir partie [aléatoire](aléatoire){.interne}

### Key derivation function

{% lien %}
[Key derivation function](https://en.wikipedia.org/wiki/Key_derivation_function)
{% endlien %}

Les protocole vont avoir besoin de tout un tas de clés différentes. Une pour chaque message à transmettre et pour chaque messages. La façon la plus simple, si on a un PRF sous la main est de :

- posséder une clé primaire appelée $SK$ (*source key*)
- une constante $CTX$, application dépendante pour éviter que plusieurs applications différentes utilisant la même clé primaires de se trouvent avec les mêmes clés

Puis il suffit d'étier le process à chaque fois que l'in veut une clé avec : $F(\text{SK}, \text{CTX} || i)$, où $i$ est un compteur.
