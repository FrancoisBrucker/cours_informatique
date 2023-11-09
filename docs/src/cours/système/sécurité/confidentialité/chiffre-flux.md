---
layout: layout/post.njk

title: Chiffrement en flux

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le ***chiffrement par flux*** *stream cicher* reprend directement l'idée du code de Vernam et l'adapte aux contraintes d'utilisation réelle :

- une clé plus petite que le message
- des algorithmes rapides

On cherche une fonction permettant de générer $n$ bits à partir de $s <<n$

```
  ---------
  | k bit |
  ---------
  :        \
  :         \
  :          \ 
  :           \
  --------------
  |G(k) à n bits|
  --------------
```

ce qui permettra d'écrire le chiffre :

<div>
$$
c = m \oplus g(k)
$$
</div>

Encore faut-il que $g$ respecte quelques propriétés permettant d'obtenir un chiffre sémantiquement sécurisé puisqu'il est impossible qu'une fonction de $\\{0, 1\\}^s$ dans $\\{0, 1\\}^n$ avec $s <n$ soit une bijection.

## Générateur de nombre

Générer des nombres purement aléatoire est impossible pour un algorithme. Il faut donc trouver une façon de simuler ce hasard, ou tout du moins de garantir qu'un algorithme efficace ne puisse voir la supercherie.

### Reconnaissance

 On définit la ***reconnaissance $G: K \rightarrow U$*** par un jeu :

```
      testeur                             adversaire A
 b  -----------                          -------------
--->|   N     |                          |           | 
    |   k     |                          |           |
    |         |    G(k) si b=1 N sinon   |           | A(G, b) = b'
    |         |------------------------->|           |------------>
    -----------                          -------------
```

A l'initialisation :

- un bit $b$ est choisi uniformément
- une valeur $k$ de $K$ est choisie uniformément
- une valeur $N$ de $U$ est choisie  uniformément

{% note "**Définition**" %}
L'***avantage*** d'un algorithme $A$ au jeu de la reconnaissance de $G$ est :

<div>
$$
\vert Pr[A(G, 1) == 1] - Pr[A(G, 0) == 1] \vert
$$
</div>

{% endnote %}

L'avantage montre l'écart à l'uniformité de $G$ reconnaissable et donc exploitable par un algorithme. Moins cette écart est grand, moins il est exploitable par une attaque.

### PRG

{% note "**Définition**" %}
Un **générateur de nombres pseudo-aléatoire sécurisé** (*secure PRG, secure pseudo random generator*) doit avoir les propriétés suivantes :

- $G: \\{0, 1\\}^s \rightarrow \\{0, 1\\}^n$, avec $s <<n$
- $G$ doit être implémentable par algorithme efficace
- tout algorithme efficace ne peut avoir qu'un avantage négligeable au jeu de la reconnaissance $G$.

{% endnote %}
{% info %}
Le paramètre de $G$ est appelé *seed*
{% endinfo %}

La définition explicite le fait qu'il est impossible de distinguer efficacement $G(k)$ d'un mot aléatoire et ce, quelque soit la *seed* choisie.

{% exercice %}
Le générateur avec un biais négligeable de la partie précédente est bien un PRG sécurisé.
{% endexercice %}
{% details "preuve" %}
> TBD
{% enddetails %}

En règle générale, en cryptographie, utilisez des générateurs fait pour cela. Ils sont plus lent mais sont non prédictible : simuler (le monde physique) est différent de protéger.

### Construction d'un code par flux avec un PRG

{% note "**Proposition**" %}
Si $G: \\{0, 1\\}^s \rightarrow \\{0, 1\\}^n$, avec $s <<n$ est un secure PRG, alors :

- $E(k, m) = G(k) \oplus m$
- $D(k, m) = E(k, m)$

est une méthode de chiffrement sécurisée.
{% endnote %}
{% details "preuve" %}
Si la méthode n'est pas sémantiquement sécurisée, il deux mots $m_0$ et $m_1$ et un algorithme A ayant un avantage non négligeable pour reconnaître $G(k) \oplus m_0$ de $G(k) \oplus m_1$.

On peut alors utiliser l'algorithme qui prend en entrée un mot de $\\{0, 1\\}^n$ et qui rend $A(y \oplus m_0)$. Il rendra avec le même avantage que $A$ la distinction entre $y \oplus m_0$ et $G(k) \oplus m_0$. Comme l'avantage est non négligeable on en déduit que $G(k)$ n'est pas un secure PRG ce qui est impossible.

{% enddetails %}

## Attaque

Notez d'un générateur de nombre donne des résultats loin d'être aléatoires.

En effet :

- le nombre de chaînes atteignable depuis sa seed : $2^s$
- le nombre de chaînes possible : $2^{n} > 2^s$

Considérons l'algorithme **non efficace** $D$ suivant :

1. il calcule $G(k)$ pour tous les $2^s$ valeurs de $k$ possible.
2. lorsque le testeur lui montre un mot $m$ de $\\{0, 1\\}^n$ il répond 1 s'il existe $k$ tel que $G(k)=m$, et 0 sinon.

Il reconnaît $D$ avec l'avantage suivant :

- $Pr[D(G, 1) = 1] = 1$
- $Pr[D(G, 0) = 1] = 2^s/2^n = 1/2^{n-s}$ qui correspond à la probabilité que $N$ soit choisit parmi les mots possibles de $G$ ($2^s$ mots de $G$ parmi les $2^n$ mots possibles)

Son avantage est donc $1-1/2^{n-s}$ qui peut être énorme si $n>>s$

Cette attaque brute force nous donne une borne min acceptable pour une attaque : il faut que $s$ soit assez grand pour que générer toute les solutions soient non efficace.

## PRF

On peut créer des PRG en utilisant des fonctions moins contraignantes, les PRF

### Définition

{% note "**Définition**" %}
Une **fonction pseudo-aléatoire sécurisée** (*secure PRF, pseudo random function*) doit avoir les propriétés suivantes :

- $F: \\{0, 1\\}^s \times \\{0, 1\\}^n \rightarrow \\{0, 1\\}^n$, avec $s <<n$
- $F$ doit être implémentable par algorithme efficace.
- tout algorithme efficace ne peut avoir qu'un avantage négligeable au jeu de la reconnaissance $F(k, \cdot)$
{% endnote %}

Pour reconnaître  une fonction, il faut un peut modifier le jeu de la reconnaissance :

On définit la ***reconnaissance de $G: K \times U \rightarrow U$*** par un jeu :

```
      testeur                                adversaire A
 b  -----------            x1               -------------
--->|   H     |<----------------------------|           | 
    |   k     |                             |           |
    |         | F(k, x1) si b=1 H(x1) sinon |           |
    |         |---------------------------->|           |
    |         |                             |           |
    |         |           ....              |           |
    |         |                             |           |
    |         |             xq              |           |
    |         |<----------------------------|           |
    |         | F(k, xq) si b=1 H(xq) sinon |           |
    |         |---------------------------->|           | A(F, b) = b'
    |         |                             |           |------------>
    -----------                             -------------
```

A l'initialisation :

- un bit $b$ est choisi uniformément
- une valeur $k$ de $K$ est choisie uniformément
- une fonction $H: U \rightarrow $U$ est choisie  uniformément

Après $q$ requêtes successives, l'adversaire $A$ doit choisir si les $q$ mots fournis viennent de $F$ ou de $H$ (une fonction quelconque).

{% note "**Définition**" %}
L'avantage d'un algorithme $A$ au jeu de la reconnaissance de $F$ est :

<div>
$$
\vert Pr[A(F, 1) == 1] - Pr[A(F, 0) == 1] \vert
$$
</div>

{% endnote %}

Notez que le fait que l'on utilise des algorithme efficaces implique que $q$ ne peut être que polynomial.

{% exercice %}
Montrez que la fonction constante $F(k,x) = \mathbb{0}$ n'est pas sécurisée.
{% endexercice %}
{% details "preuve" %}
> TBD
{% enddetails %}

### Construction d'un PRG avec un PRF

{% note "**Proposition**" %}
Si $F: \\{0, 1\\}^s \times \\{0, 1\\}^n \rightarrow \\{0, 1\\}^n$ est une secure PRF, alors $G(k) = F(k, x)$ est un secure PRG pour tout $x$.
{% endnote %}

{% details "preuve" %}
Si $H$ est une fonction quelconque de $\\{0, 1\\}^n$ dans $\\{0, 1\\}^n$ alors la probabilité que $H(x) = F(k, x)$ vaut $1/2^n$ (il faut que les valeurs coïncident bit à bit).

De là, si $G(k)$ n'est pas un secure PRG, il existe un algorithme efficace $A$ ayant un avantage non négligeable.

On peut utiliser cet algorithme dans la reconnaissance de $F$ comme un secure PRF en ne demandant que la valeur en $x$ et reconnaître F avec le même avantage non négligeable : $F$ n'est pas un secure PRF ce qui contredit notre hypothèse.
{% enddetails %}

Cette construction va être utilisée par quasi tous les codes pour créer des codages sécurisées. Notez qu'on est passé d'un générateur à un paramètre $G(k)$ à un générateur à deux paramètres $F(k, r)$ que l'on peut prendre indépendamment.

## Existence

L'existence de PRG ou de PRF n'est pas prouvée. Elles sont [équivalentes](https://en.wikipedia.org/wiki/Pseudorandom_generator_theorem#Existence_of_pseudorandom_generators) à l'existence de [fonctions à sens unique](https://en.wikipedia.org/wiki/One-way_function).

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

## Construction générale

Pour construire un code à flux il faut être capable de créer des générateurs pseudo-aléatoires de taille quelconque. Ceci peut être compliqué. On préfère découper le message à chiffrer $m$ en blocs $m_i$ de taille fixe que l'on traite séparément.

Il faut cependant faire **très** attention à ce que l'on fait et ne pas réutiliser les clés ! Sinon on peut très facilement déchiffrer le message comme on a  vu avec le chiffre de Vernam. 

On peut utiliser le fait que si $F$ est une PRF alors $F(\cdot, x)$ est un PRG quelque soit $x$.

{% note "**proposition**" %}
$F: \\{0, 1\\}^s \times \\{0, 1\\}^n \rightarrow \\{0, 1\\}^n$ est une secure PRF et $m$ un message de taille $l\cdot n$ alors :

$$
E(k, m) = F(k, 1) || \dots || F(k, l) \oplus m
$$

est un codage par flus sécurisé.
{% endnote %}
{% info %}
L'opérateur `||` est la concaténation.
{% endinfo %}
{% details "preuve" %}
> BD theorem 3.30 introduction to cryptography
{% enddetails %}

On peut même ajouter un élément en clair dans le cryptage sans en altérer la sécurité :

{% note "**proposition**" %}
$F: \\{0, 1\\}^s \times \\{0, 1\\}^n \rightarrow \\{0, 1\\}^n$ est une secure PRF, $m$ un message de taille plus petite que $l\cdot n$ et $\text{NONCE}$ un mot de \\{0, 1\\}^p$ avec $p<n$ alors :

$$
E(k, m) = NONCE || (F(k, NONCE || 1) || (F(k, NONCE || 2) || \dots || F(k, NONCE || l) \oplus m)
$$

est un codage par flux sécurisé.
{% endnote %}
{% info %}
L'opérateur `||` est la concaténation.
{% endinfo %}
{% details "preuve" %}
> TBD : construction 3.25 Introduction to modern cryptography
{% enddetails %}

Remarquer que le $\text{NONCE}$ est transmis en clair, ce n'est pas grave. L'utilisation de ce $\text{NONCE}$ est courante dans les méthodes de chiffrement en flux.

{% note "**Définition**" %}

Un [NONCE](https://en.wikipedia.org/wiki/Cryptographic_nonce) est un nombre utilisé une fois.

Il st utilisé dans de nombreux protocoles cryptographiques pour distinguer des encodages au sein de l'envoie d'un message.
{% endnote %}

Le schéma général d'un codage en flux avec compteur est alors :

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
       c1           c1                c1                c1     
```
