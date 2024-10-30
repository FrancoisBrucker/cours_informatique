---
layout: layout/post.njk

title: Chiffrer un message de taille fixe

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On va analyser ici les conditions théoriques pour pouvoir chiffrer un message de taille donnée. Cette partie sera ensuite
utilisé dans la suite pour chiffrer un message de taille quelconque.

Reprenons le schéma général :

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

Avec :

- $E : \\{0, 1\\}^s \times \\{0, 1\\}^t \rightarrow \\{0, 1\\}^t$
- $D : \\{0, 1\\}^s \times \\{0, 1\\}^t \rightarrow \\{0, 1\\}^t$

Tel que : $D(k, E(k, m)) = m$ pour tout $m \in \\{0, 1\\}^t$

Pour tout $k \in \\{0, 1\\}^k$ on a :

- $f_k(x) = E(k, x)$ était une permutation de $\\{0, 1\\}^t$
- $f^{-1}_k(x) = D(k, x)$

Pour que ce genre de fonctions soient valides pour un usage cryptographique, il faut qu'elles soient [sémantiquement sécurisées](../définitions/#sémantiquement-sécurisé).

## PRP

<div id="PRP"></div>

{% note "**Définition**" %}
Soit $F: \\{0, 1\\}^s \times \\{0, 1\\}^t \rightarrow \\{0, 1\\}^t$ une fonction telle que :

- $F(k,\cdot)$ doit être une permutation de $\\{0, 1\\}^t$ pour tout $k \in \\{0, 1\\}^s$
- $F$ doit être implémentable par algorithme efficace.

$F$ est dite être une **fonction pseudo-aléatoire sécurisée** (_secure PRF, pseudo random function_) si tout algorithme efficace ne peut avoir qu'un avantage négligeable au [jeu de la reconnaissance](../définitions/#jeu-reconnaissance) entre :

- une fonction $F(k, \cdot)$ pour $k$ uniformément choisie,
- une fonction $f$ uniformément choisie parmi toutes les fonctions de $\\{0, 1\\}^t$ dans $\\{0, 1\\}^t$.

Si de plus $F$ est une permutation, elle est appelée **permutation pseudo-aléatoire sécurisée** (_secure PRP, pseudo random permutation_)  si tout algorithme efficace ne peut avoir qu'un avantage négligeable au [jeu de la reconnaissance](../définitions/#jeu-reconnaissance) entre :

- une fonction $F(k, \cdot)$ pour $k$ uniformément choisie,
- une permutation $f$ uniformément choisie parmi toutes les permutations de $\\{0, 1\\}^t$ dans $\\{0, 1\\}^t$.

{% endnote %}

Une PRP est un cas particulier de PRF, mais si $n$ est grand, elle est indistinguable d'une fonction quelconque avec un avantage non négligeable :

{% note "**Proposition**" %}
Une **PRP** ne peut être distinguée d'une fonction **PRF** qu'avec un avantage non négligeable par un algorithme efficace.

{% endnote %}
{% details "preuve", "open" %}

On considère le jeu de la reconnaissance où un algorithme efficace cherche à distinguer une fonction $F(k, \cdot)$ pour un $k$ uniformément choisi d'une fonction $f$ uniformément choisie parmi toutes les permutations de $\\{0, 1\\}^t$ dans $\\{0, 1\\}^t$.

La seule façon de distinguer une permutation d'une simple fonction est de chercher des points fixes : s'il existe $x\neq y$ tel que $f(x) = f(y)$, $f$ n'est pas une permutation. Comme les fonctions sont tirées aléatoirement, vérifier si $N$ éléments ont des images différentes a la même probabilité que savoir si $N$ éléments tirés aléatoirement sont différents. En reprenant la démonstration du [paradoxe des anniversaires](/cours/algorithmie/structure-conteneurs/fonctions-hash/#paradoxe-anniversaires){.interne}, cette probabilité vaut :

<div>
$$
\bar{p}(N, 2^t) = \prod_{i=1}^{N}(1-\frac{i-1}{2^t})
$$
</div>

Le nombre de tirages $N$ est plus petit que la complexité de l'algorithme et comme celui-ci est efficace il est borné par $K\cdot n^d$ avec $d$ et $K$ deux constantes, et $n$, le paramètre de sécurité, supérieur à $t$. De là $N << 2^t$ et :

<div>
$$
\bar{p}(N, 2^t) \leq (1-\frac{1}{2^t})^N \simeq 1-\frac{N}{2^t} \leq 1-\frac{t^d}{2^t}
$$
</div>

Le meilleur avantage possible que peut avoir un adversaire efficace au jeu de la reconnaissance est donc $1-\bar{p}(N, 2^t) \leq \frac{t^d}{2^t}$, qui est négligeable.

{% enddetails %}

La proposition précédente fait des PRP des candidats idéaux pour pour nos méthodes de chiffrement, ce sont des bijections mais vues de l'extérieur (_ie_ d'un adversaire) elles sont indistinguables de simples fonctions. Leur existence n'est cependant pas prouvée... Elles sont [équivalentes](https://en.wikipedia.org/wiki/Pseudorandom_generator_theorem#Existence_of_pseudorandom_generators) à l'existence de [fonctions à sens unique](https://en.wikipedia.org/wiki/One-way_function).

Les fonctions à sens unique sont une représentation de la difficulté computationnelle et sont à la base de nombreuse méthodes en cryptographie :

{% note "**définition**" %}
Une fonction $F : \\{0, 1\\}^n \rightarrow \\{0, 1\\}^n$ est à sens unique si :

- il existe un algorithme efficace pour calculer $F(x)$ quelque soit $x$
- Que pour tout algorithme $G$, $Pr[F(G(F(x))) = F(x)]$ soit négligeable.
  {% endnote %}

La définition stipule que $F$ soit difficile à inverser en moyenne et pas seulement dans le pire des cas comme en théorie de la complexité classique. De là, si une telle fonction existe :

- il n'existerait pas d'algorithme polynomial produisant la fonction $G(F(x)) = y$ tel que $F(y) = F(x)$
- mais il serait facile de vérifier si $F(y) = F(x)$

Et donc $P \neq NP$.

Comme on pense très fort à l'existence de problèmes dont la résolution nécessite plus qu'un algorithme polynomial pour être résolu, donc que $P \neq NP$, on croit très fort que les PRG et PRF existent.

> TBD rappeler qu'on a vu ça en algorithmie.

## En pratique

Comme l'existence d'une PRP n'est pas prouvée, il faut prendre toute proposition de chiffrement avec pincette. Il n'est pas improbable que l'on découvre des failles de sécurité et qu'il faille changer de méthode de chiffrement (c'est arrivé et ça arrivera encore) ou qu'il faille augmenter la taille de la clé pour maintenir la confidentialité que ce soit par le développement de nouveaux ordinateur de nouvelles attaques (c'est arrivé et ça arrivera encore).

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

### One tTime Pad

{% aller %}
[Algorithme via générateur pseudo-aléatoire](générateur-xor){.interne}
{% endaller %}

### Chacha20

{% aller %}
[Algorithme chacha20](chacha20){.interne}
{% endaller %}

### AES

{% aller %}
[Algorithme AES](aes){.interne}
{% endaller %}
