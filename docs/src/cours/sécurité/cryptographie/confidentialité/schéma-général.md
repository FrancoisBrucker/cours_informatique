---
layout: layout/post.njk

title: Schéma général du chiffrement

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


On montre ici le schéma général qui nous permet de créer un chiffrement sémantiquement sécurisé d'un message de taille quelconque à partir d'une brique de base permettant de chiffrer une séquence de [blocs de taille fixée](../chiffrer-un-bloc){.interne}.

{% lien %}
Il existe d'autres façons de faire. On donne ici le plus simple sécurisé de maintenant. Pour voir d'autre procédés, voir par exemples :

- [SP network](https://www.youtube.com/watch?v=DLjzI5dX8jc)
- [tuto encryption](https://www.youtube.com/watch?v=oVCCXZfpu-w)

{% endlien %}

Concaténer des blocs de messages chiffrés. On découpe le message à chiffrer $m$ en blocs $m_i$ de taille $t$ fixe que l'on traite séparément.

## Non

Il faut cependant faire **très** attention à ce que l'on fait et ne pas réutiliser les clés ! Sinon on peut très facilement déchiffrer le message comme on a vu avec le chiffre de Vernam.

```
        m1           m2                mi                ml
        |            |                 |                 |
      -----        -----             -----             -----
 k-->|     |  k-->|     |  ...  k-->|     |  ...  k-->|     |
      -----        -----             -----             -----
        |            |                 |                 |
        |            |                 |                 |
        |            |                 |                 |
       c1           c2                ci                cl
```

{% attention %}
ECB pas semantically secure : <https://crypto.stanford.edu/~dabo/courses/cs255_winter19/lectures/PRP-PRF.pdf>

{% endattention %}

> TBD prouver par le jeu de la reconnaissance que ce n'est pas sécurisé.

> TBD : on peut aussi ajouter des portions de messages forgés pour trouver la clé

## Oui

```
        1            2                 i                 l
        |            |                 |                 |
      -----        -----             -----             -----
 k-->|     |  k-->|     |  ...  k-->|     |  ...  k-->|     |
      -----        -----             -----             -----
        |            |                 |                 |
 m1--->XOR    m2--->XOR         mi--->XOR         ml--->XOR
        |            |                 |                 |
        |            |                 |                 |
       c1           c2                ci                cl
```

> TBD comme le chiffrement d'un bloc avec flux !

On peut utiliser le fait que si $F$ est une PRF (ou un PRP) alors $F(\cdot, x)$ est un PRG quelque soit $x$.

{% note "**proposition**" %}
$F: \\{0, 1\\}^s \times \\{0, 1\\}^n \rightarrow \\{0, 1\\}^n$ est une secure PRF et $m$ un message de taille $l\cdot n$ alors :

$$
E(k, m) = F(k, 1) \ \ ||\ \  \dots \ \ ||\ \  F(k, l) \oplus m
$$

est un codage par flus sécurisé.
{% endnote %}
{% info %}
L'opérateur `||` est la concaténation.
{% endinfo %}
{% details "preuve", "open" %}

> BD theorem 3.30 introduction to cryptography
{% enddetails %}

Cette construction permet également de déchiffrer rapidement le message en parallèle. Il suffit de connaître la clé $k$ et la position du bloc à déchiffrer.

## NONCE

On peut même ajouter un élément en clair $N$, appelé [NONCE](https://en.wikipedia.org/wiki/Cryptographic_nonce), dans le cryptage sans en altérer la sécurité. Le schéma général devient alors :

```
     N || 1       N || 2            N || i            N || l
        |            |                 |                 |
      -----        -----             -----             -----
 k-->|     |  k-->|     |  ...  k-->|     |  ...  k-->|     |
      -----        -----             -----             -----
        |            |                 |                 |
 m1--->XOR    m2--->XOR         mi--->XOR         ml--->XOR
        |            |                 |                 |
        |            |                 |                 |
       c1           c2                ci                cl
```

{% note "**proposition**" %}
$F: \\{0, 1\\}^s \times \\{0, 1\\}^\star \rightarrow \\{0, 1\\}^n$ est une secure PRF, $m$ un message de taille plus petite que $l\cdot n$ et $\text{NONCE}$ un mot de \\{0, 1\\}^p$ avec $p<n$ alors :

$$
E(k, m) = NONCE \ ||\  (F(k, NONCE \ ||\  1) \ ||\  (F(k, NONCE \ ||\  2) \ ||\  \dots \ ||\  F(k, NONCE \ ||\  l) \oplus m)
$$

est un codage par flux sécurisé.
{% endnote %}
{% details "preuve", "open" %}

> TBD : construction 3.25 Introduction to modern cryptography

{% enddetails %}

Remarquer que le $\text{NONCE}$ est transmis en clair, ce n'est pas grave. L'utilisation de ce $\text{NONCE}$ est courante dans les méthodes de chiffrement en flux.

Un NONCE, comme son nom l'indique est utilisé une unique fois. Il est utilisé dans de nombreux protocoles cryptographiques pour distinguer des encodages au sein de l'envoie d'un message pour éviter les [attaque par rejeu](https://fr.wikipedia.org/wiki/Attaque_par_rejeu).
