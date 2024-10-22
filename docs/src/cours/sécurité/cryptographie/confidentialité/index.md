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
        ---             ---
       | v |           | v |
       |   |           |   |
 m --> | E | --> c --> | D | --> m
        ---             --- 
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

## Types de code

Il existe historiquement deux types de codes même si les différences commencent à s'estomper entres eux :

- les codes en flux qui vont se comporter comme le code de Vernam
- les code en bloc qui vont découper le message en blocs et chiffrer chacun d'entre eux avec un permutation.

### Non linéarité

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

### Stream cipher

{% aller %}
[Chiffrement en flux](chiffre-flux){.interne}
{% endaller %}

{% aller %}
[Algorithme chacha20](chacha20){.interne}
{% endaller %}

### Bloc cipher

> TBD : pas encore fait

{% aller %}
[chiffrement par bloc](chiffre-bloc){.interne}
{% endaller %}
{% aller %}
[Algorithme AES](aes){.interne}
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
