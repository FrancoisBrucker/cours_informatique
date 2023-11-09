---
layout: layout/post.njk

title: Hash cryptographiques

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}

- [Hash cryptographique](https://fr.wikipedia.org/wiki/Fonction_de_hachage_cryptographique)
- [Hash propriétés et autres](https://membres-ljk.imag.fr/Bruno.Grenet/IntroCrypto/4.HashFunctions.pdf)

{% endlien %}

Une fonction de hash cryptographique doit être conçue pour éviter les collision, c'est à dire qu'en connaissant $a$ il est très difficile de trouver $b \neq a$ tel que $f(b) = f(a)$

{% note "**Définition**" %}
Une fonction $H: \\{0, 1\\}^\star \rightarrow \\{0, 1\\}^n$ est une fonction de ***hash cryptographique*** si elle est résistante aux collision.

Tout algorithme efficace ne peut rendre un couple $(x, x')$ tel que $H(x) = H(x')$ qu'avec un avantage négligeable.
{% endnote %}

On peut relâcher la condition de résistance à la collision en :

1. ***résistant à la seconde pré-image*** : étant donné $x$, il est difficile de trouver $x'$ tel que $H(x) = H(x')$

2. ***résistant à la pré-image*** : étant donné $y$, il est difficile de trouver $x$ tel que $H(x) = y$

La première condition étant plus restrictive que la condition 2.

## Attaque

### Attaque des anniversaires

L'attaque générique des anniversaire est l'attaque brute force associée aux fonctions de hash cryptographique.

Grace aux paradoxe des anniversaires, on sait qu'il suffit de $2^{n/2}$ mots de $\\{0, 1\\}^n$ plur avoir une probabilité supérieure à 1/2 d'avoir deux éléments $x$ et $x'$ tels que $H(x)c = H(x')$.

Il n'est pas nécessaire de stocker tous les mots en mémoire, on peut montrer qu'il suffit de :

{% note "**Algorithme attaque anniversaire**" %}

1. prendre $x_1$ et $y_1$ deux mots aléatoires de $\\{0, 1\\}^n$
2. créer itérativement $x_i = H(x_{i−1})$ et $y_i = H(H(y_{i−1}))$ jusqu'à ce que $x_m = y_m$
3. on a alors $H(x_{m−1}) = H(H(y_{m−1}))$ si $x_{m-1} \neq H(y_{m−1})$ (ce qui est très probable)

Il faut, comme l'attaque brute force du dictionnaire de l'ordre de $\mathcal{O}(2^{n/2})$ opération avant de trouver une collision

{% endnote %}
{% details "preuve" %}
L'ensemble d'arrivée de $H$ étant fini, il va exister, pour tout $x$, un entier $p$ tels que $H^p(x) = x$. De là $H^{2p}(x) = H^p(x)$ et comme $x_i = H^i(x_1)$ et $y_i = H^{2i}(x_1)$, lorsque $i=p$ on aura trouvé le point fixe.
{% enddetails %}

Notez que si l'attaque ds anniversaire ne donne pas de garantie sur les deux mots que l'on trouve, il est très facile de modifier 2 documents différents de façon aléatoire (ajouter des espaces/entrée, backspace, ...) un très grand nombre de fois, ce qui va garantir de tomber sur une collision tout en ayant deux texte se ressemblant.

{% info %}
Se rappeler de toujours modifier un peu un document que l'on signe, histoire que l'attaquant doive tout refaire.
{% endinfo %}

### Differential Analysis

{% lien %}

[differential analysis](https://en.wikipedia.org/wiki/Differential_cryptanalysis)

{% endlien %}

> TBD : à étoffer

## Construction

### A longueur fixée

{% lien %}
[Construction Davies–Meyer](https://fr.wikipedia.org/wiki/Construction_de_Davies-Meyer)
{% endlien %}

On utilise la construction Davies–Meyer qui permet de transformer un PRP $P : \\{0, 1\\}^s \times \\{0, 1\\}^n \rightqrrow \\{0, 1\\}^n$ ($P(k, x)$ est une permutation aléatoire de $x$) en hash à taille fixe.

On fait rentrer le message là où normalement arrive la clé. Et un utilisant une constante IV (initial value) à la place de la où habituellement se place un message.

<div>
$$
H(m) = P(m, IV)
$$
</div>

Ce qui donne schéma :

```
         m |
           |
       ---------
IV ----|   v   |--- XOR ---
    |  |       |     |
    |  ---------     |
    |                |
    ------------------               
```

{% note "**Théorème**" %}

Si le bloc est une PRP, alors la résistance à la collision est maximale.
{% endnote %}
{% details "preuve" %}
> TBD : preuve avec <https://crypto.stackexchange.com/questions/8023/why-are-the-davies-meyer-and-miyaguchi-preneel-constructions-secure>

{% enddetails %}
{% info %}
[article de la preuve](<https://www.cs.ucdavis.edu/~rogaway/papers/hash.pdf>)
{% endinfo %}

> TBD : [pseudo-random function et permutation pareil sous le paradoxe anniversaire](https://crypto.stackexchange.com/questions/75304/what-is-the-difference-between-pseudorandom-permutation-pseudorandom-function-bl)

### A longueur variable

{% lien %}

- [Construction de Merkel Damgard](https://fr.wikipedia.org/wiki/Construction_de_Merkle-Damg%C3%A5rd)
- [Merkel Damgard preuve](https://www.youtube.com/watch?v=s7arHByjSOw)

{% endlien %}

```
        m1 |                           mi |                
           |                              |                
       --------- H1                   --------- Hi           
IV ----|   v   |--- XOR --- ... ------|   v   |--- XOR --- .... Hm
    |  |       |     |             |  |       |     |     
    |  ---------     |             |  ---------     |      
    |                |             |                |      
    ------------------             ------------------           
```

On ajoute le padding à la fin qui consiste en `10....0 || taille du message`. Si le message est déjà de la bonne taille on ajoute un bloc ne contenant que le padding.

{% note "**Théorème**" %}
Si le bloc est résistant à la collision, la construction l'est.
{% endnote %}
{% details "preuve" %}
Supposons qu'il y ait une collision :

On a alors $H_n$ = $H'_{n'}$ ce qui implique $F(H_{m-1}, m_n || \text{pad}) = F(H'_{m'-1}, m'_{n'} || \text{pad}')$.

De là si $m_n || \text{pad} \neq m'_{n'} || \text{pad}$ on a découvert une collision interne ce qui est improbable. Donc $m_n || \text{pad} = m'_{n'} || \text{pad}'$.

Alors :

1. $\text{pad} = \text{pad}'$ ce qui implique que les deux messages ont la même taille
2. $m_n = m'_n$ : les messages ont la même fin

On conclut la preuve en remarquant que si $H_{m-1} \neq H'_{m-1}$ on a une collision ce qui est improbable donc $H_{m-1}$ = $H'_{m -1}$ et on peut faire une preuve par récurrence.

{% enddetails %}

Les fonctions de hash très utilisés que sont les SHA-1 et SHA-2 sont basées sur ce principe.

{% info %}
SHA-3 est basé sur une autre construction : les [sponge function](https://en.wikipedia.org/wiki/Sponge_function)
{% endinfo %}

## Usage

### Intégrité non sécurisée

> TBD encrpyt then : hash M || H(m)

Bien arrivé si le hash du message arrivé correspond au hash concaténé. Couple $(S, V)$ signe et vérifie :

- $S(m) = H(m)$
- $V(m, h) = H(m) == h$

Mais peut- être changé par un attaquant. DOnc uniquement preuve de transmission correct d'un message.

### Stockage sécurisé

Les mots de passe d'un système son normalement stockés sous la forme d'un hash, auquel on ajoute un *sel* aléatoire. Voir par exemple [ce post de blog](https://patouche.github.io/2015/03/21/stocker-des-mots-de-passe/) qui vous explique un peu comment tout ça fonctionne.

> TBD : ajout de salt : taille du sel ?

on stocke : utilisateur, SALT || H(SALT || m)

### Clés

La non collision permet de stocker les sha plutôt que les valeurs exactes

> TBD git utilise SHA-1. Il n'a besoin que de la non collision
