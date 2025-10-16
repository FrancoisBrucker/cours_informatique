---
layout: layout/post.njk

title: Codes actuels

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD attaques : <https://sparkle-lwc.github.io/security>

Comme l'existence d'une PRP n'étant pas prouvée, il faut prendre toute proposition de chiffrement avec pincette. Il n'est pas improbable que l'on découvre des failles de sécurité et qu'il faille changer de méthode de chiffrement (c'est arrivé et ça arrivera encore) ou qu'il faille augmenter la taille de la clé pour maintenir la confidentialité que ce soit par le développement de nouveaux ordinateur de nouvelles attaques (c'est arrivé et ça arrivera encore).

S'il faut retenir une chose c'est :

{% note %}
Utilisez des bibliothèques de chiffrement développés par des professionnels reconnus comme [openssl](https://fr.wikipedia.org/wiki/OpenSSL).
{% endnote %}

### Nécessité de la non linéarité

Pour éviter une attaque classique, nommée [cryptanalyse linéaire](https://fr.wikipedia.org/wiki/Cryptanalyse_lin%C3%A9aire), tous les PRP vont avoir à la fois des transformations linéaires $\oplus$, décalage ou circulation de bits ainsi que des choses non linéaire, souvent encapsulé dans des matrices de transformation appelées [S-box](https://fr.wikipedia.org/wiki/S-Box). Il faut bien sûr que ces opérations soient choisies avec soin pour éviter tout biais, la moindre linéarité cachée pouvant être facilement utilisée comme attaque.

{% info %}
Le chiffrement DES, proposé par la NSA, proposait des [S-box](https://fr.wikipedia.org/wiki/S-Box) obscures qui ont toujours laissé des doutes quant à la sincérité de ses non-linéarités.
{% endinfo %}

La cryptanalyse linéaire va chercher des corrélations linéaires entre le message $m$, le chiffre $c$ et la clé $k$, c'est à dire si :

<div>
$$
Pr[(\oplus_{i \in I} m_i) \oplus (\oplus_{j \in J} c_j) = (\oplus_{l \in L} k_l)] \leq 1/2 + \epsilon
$$
</div>

Si $\epsilon$ est non négligeable, on peut en déduire un algorithme qui va exécuter $1/\epsilon$ fois cette relation et trouver avec une grande probabilité cette corrélation, et donc l'information nécessaire à sa cryptanalyse.

> TBD calcul probabilité avec une binomiale $Pr[B(n, p) \geq 1]$.

Chaque méthode de chiffrement intègre ainsi en son sein des transformations non linéaires permettant de casser ce genre d'attaque.

### Chacha20

{% aller %}
[Algorithme chacha20](chacha20){.interne}
{% endaller %}

### AES

{% aller %}
[Algorithme AES](aes){.interne}
{% endaller %}
