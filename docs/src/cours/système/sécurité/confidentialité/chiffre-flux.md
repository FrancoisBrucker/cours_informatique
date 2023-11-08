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

Générer des nombres purement aléatoire est impossible pour un algorithme. Il faut donc trouver une façon de simuler ce hasard, ou tout du ;oins de garantir qu'un algorithme efficace ne puisse voir la supercherie.'

> TBD : [prg et $p \neq np$](https://crypto.stackexchange.com/questions/16020/prg-existance-and-p-versus-np)

### Distinguable

On définit la ***distinguabilité*** par un jeu à un paramètre $F: A \rightarrow B$

```
      testeur                             adversaire A
 b  -----------            x1            -------------
--->|   H     |<-------------------------|           | 
    |         |                          |           |
    |         | F(x1) si b=1 H(x1) sinon |           |
    |         |------------------------->|           |
    |         |                          |           |
    |         |          ....            |           |
    |         |                          |           |
    |         |           xq             |           |
    |         |<-------------------------|           |
    |         | F(xq) si b=1 H(xq) sinon |           | A(F, b) = b'
    |         |------------------------->|           |------------>
    -----------                          -------------
```

A l'initialisation :

- un bit $b$ est choisi uniformément
- le testeur choisit une fonction $H$ uniformément parmi toutes les fonctions de $A$ dans $B$.

Le testeur va rendre la fonction à tester si $b=1$ et une fonction aléatoire prise à l'initialisation sinon.

Après $q$ requêtes successives, l'adversaire $A$ doit choisir si les $q$ mots fournis viennent de $F$ ou de $H$ (une fonction quelconque). L'avantage dans ce jeu est $\epsilon$ où la probabilité de gagner au jeu est inférieure à ($b=b'$) $1/2 + \epsilon$.

{% note "**Définition**" %}
$A$ est un ***distingueur*** si c'est un algorithme efficace adversaire du jeu de la distinguabilité.

Son avantage est :

<div>
$$
\vert Pr[A(F, 1) == 1] - Pr[A(F, 0) == 1] \vert
$$
</div>

{% endnote %}

Notez que le fait que l'on utilise des algorithme efficaces implique que $q$ ne peut être que polynomial.

### PRG

{% note "**Définition**" %}
Un **générateur de nombres pseudo-aléatoire sécurisé** (*secure PRG, secure pseudo random generator*) doit avoir les propriétés suivantes :

- $G: \\{0, 1\\}^s \rightarrow \\{0, 1\\}^n$, avec $s <<n$
- algorithme efficace (ie polynomial)
- tout distingueur efficace $D$ de $G$ est tel que son avantage est négligeable.
{% endnote %}
{% info %}
Le paramètre de $G$ est appelé *seed*
{% endinfo %}

La notion de de distingueur explicite le fait qu'il est impossible de distinguer $G$ de toute autre fonction choisie de façon efficace, et ce quelque soit la *seed* choisie.

{% exercice %}
Le générateur avec un biais négligeable de la partie précédente est bien un PRG sécurisé.
{% endexercice %}
{% details "preuve" %}
> TBD
{% enddetails %}

En règle générale, en cryptographie, utilisez des générateurs fait pour cela. Ils sont plus lent mais sont non prédictible : simuler (le monde physique) est différent de protéger.

### Existence

L'existence de générateur de nombre pseudo-aléatoire sécurisé n'est pas prouvée. Ils dépendent de l'existence de fonction pseudo-aléatoire sécurisées.

{% note "**Définition**" %}
Une **fonction pseudo-aléatoire sécurisé** (*secure PRF, pseudo random function*) doit avoir les propriétés suivantes :

- $F: \\{0, 1\\}^s \times \\{0, 1\\}^n \rightarrow \\{0, 1\\}^n$, avec $s <<n$
- algorithme efficace (ie polynomial)
- Tout distingueur efficace ne peut avoir qu'un avantage $F(k, \cdot)$ doit être non distinguable de $F': \\{0, 1\\}^n \rightarrow \\{0, 1\\}^n$ une fonction quelconque pour tout distingueur efficace.
{% endnote %}

{% exercice %}
Montrez que la fonction constante $F(k,x) = \mathbb{0}$ n'est pas sécurisée.
{% endexercice %}
{% details "preuve" %}
> TBD
{% enddetails %}

On est pas sûr de l'existence de secure PRF. Elles sont conditionnées à l'existence de [fonctions à sens unique](https://en.wikipedia.org/wiki/One-way_function), dont on pense très fort qu'elles existent.

Mais si ces fonctions existent, alors il existe des secure PRG :

{% note "**Proposition**" %}
Si $F: \\{0, 1\\}^s \times \\{0, 1\\}^n \rightarrow \\{0, 1\\}^n$ est une secure PRF, alors $G(k) = F(k, x)$ est un secure PRG pour tout $x$.
{% endnote %}

{% details "preuve" %}
Si $H$ est une fonction quelconque de $\\{0, 1\\}^n$ dans $\\{0, 1\\}^n$ alors la probabilité que $H(x) = F(k, x)$ vaut $1/2^n$ (il faut que les valeurs coïncident bit à bit).

De là, si $G(k)$ n'est pas un secure PRG, il existe un algorithme efficace $A$ ayant un avantage non négligeable.

On peut utiliser cet algorithme dans la reconnaissance de $F$ comme un secure PRF en ne demandant que la valeur en $x$ et reconnaître F avec le même avantage non négligeable : $F$ n'est pas un secure PRF ce qui contredit notre hypothèse.
{% enddetails %}

Toutes les fonctions utilisées en pratiques sont donc non prouvées être des  générateurs de nombre pseudo-aléatoire.

## Attaque

Notez d'un générateur de nombre done des résultats loin d'être aléatoires.

En effet :

- le nombre de chaînes atteignable depuis sa seed : $2^s$
- le nombre de chaînes possible : $2^{n} > 2^s$

Le distingeur $D$ **non efficace** qui consiste à générer toutes les chaînes atteignable depuis $G$ et à rendre 1 si la chaîne est productible par $G$ on a :

- $Pr[D(G, 1) = 1] = 1$
- $Pr[D(G, 0) = 1] = 2^s/2^n = 1/2^{n-s}$

Son avantage est donc $1-1/2^{n-s}$ qui peut être énorme si $n>>s$

Cette attaque brute force nous donne une borne min acceptable pour une attaque : il faut que $s$ soit assez grand pour que générer toute les solutions soient non efficace.

## Construction d'un code par flux avec un PRG

{% note "**Proposition**" %}
Si $G: \\{0, 1\\}^s \rightarrow \\{0, 1\\}^n$, avec $s <<n$ est un secure PRG, alors :

- $E(k, m) = G(k) \oplus m$
- $D(k, m) = E(k, m)$

est méthode de chiffrement sémantiquement sécurisée.
{% endnote %}
{% details "preuve" %}
Si la méthode n'est pas sémantiquement sécurisée, il deux mots $m_0$ et $m_1$ et un algorithme A ayant un avantage non négligeable pour reconnaître $G(k) \oplus m_0$ de $G(k) \oplus m_1$.

On peut alors utiliser l'algorithme qui prend en entrée un mot de $\\{0, 1\\}^n$ et qui rend $A(y \oplus m_0)$. Il rendra avec le même avantage que $A$ la distinction entre $y \oplus m_0$ et $G(k) \oplus m_0$. Comme l'avantage est non négligeable on en déduit que $G(k)$ n'est pas un secure PRG ce qui est impossible.

{% enddetails %}

## Construction pratique

### Taille fixe

Un PRF est comme un PRG $F(k, r)$ mais il faut stocker r de façon non crypté. Ce n'est cependant pas grave.

{% note "**Proposition**" %}
Si $F: \\{0, 1\\}^s \times \\{0, 1\\}^n \rightarrow \\{0, 1\\}^n$$ est une secure PRF, alors :

- $E(k, m) = r || (F(k, r) \oplus m)$
- $D(k, m) = F(k, m[:n]) \oplus mm[n:]$

{% endnote %}
{% details "preuve" %}
> TBD : construction 3.25 Introduction to modern cryptography
{% enddetails %}

### Taille variable

> TBD : besoin d'un nonce
> TBD non linéarité très important sinon attaque possible
> on évite l'utilisation de la même clés en utilisant une nonce et
> F(k, 0 ) || F(k, 1 ) || F(k, 2) qui est un secure prg.
> TBD : preuve.

Un PRF concaténé est comme un PRG concaténé

1. F(k, ) : PRF
2. ri = F(k, NONCE + i)
3. mi + ri

> BD theorem 3.30 introduction to cryptography

### Chacha

Chacha est un PRP masi ça marche aussi

> TBD 1. def PRP
> PRP alors aussi PRF proposition 3.29 (trouver un point fixe est rare, donc pas efficace)

On règle le problème précédent en découpant le message en bloc et en générant $n$ bit par $n$ bits.

Mais il faut faire ça bien pour garde la sécurité. Rappelez vous que le OTP ne fonctionne que si c'est One Time.

{% lien %}

Chacha :

- [fonctionnement et origine](https://en.wikipedia.org/wiki/Salsa20#ChaCha_variant)
- [design](https://loup-vaillant.fr/tutorials/chacha20-design)
- [spec et implémentations](https://cr.yp.to/chacha.html)
- [RFC](https://datatracker.ietf.org/doc/html/rfc8439)

{% endlien %}

## PRG et *prédictabilité*

{% note %}
Une suite $g(k,1), \dots g(k, m + 1)$ est non prédictible si tout algorithme efficace ne peut peut prédire $g(k, m + 1)$ sachant $g(k, 1), \dots, g(k, m)$ qu'avec un avantage négligeable.
{% endnote %}

Le générateur de nombre pseudo-aléatoire tel que $x_i = a \cdot x_{i-1} + b \mod p$ ne l'est pas, malgré le fait qu'il possède de belle propriétés statistiques si $p$ est premier. Pour qu'un générateur de nombre puisse être utilisé de façon cryptographe, on s'intéresse moins à ses propriété d'uniformité qu'à sa non prédictibilité.

Non prédictible est équivalent à non distinguable.

{% note "**Proposition**" %}
Un PRG sécurisé est non prédictible.
{% endnote %}
{% details "preuve" %}

Supposons qu'un secure PRG soit prédictible. Il existe alors un algorithme efficace A qui possède un avantage non négligeable pour déterminer le $m+1$ ème bit à partir des $m$ premiers.

On peut utiliser cet algorithme pour déterminer si $G$ est un PRG sécurisé : on ne considère que les $m+1$ premiers bits et on rend la valeur donnée par l'algorithme $A$. L'avantage est le même et est non négligeable.

{% enddetails %}

{% note "**Théorème (Yao, 1982)**" %}
Un PRG non prédictible est sécurisé.
{% endnote %}
{% details "preuve" %}
Soit $G$ un générateur non prédictible, et R un générateur aléatoire.

Supposons qu'il existe $i$ tel que que le générateur $G(k) [:i]\\; ||\\; R[i:]$ soit non sécurisé. Prenons $i$ le plus petit et soit A l'algorithme efficace qui réalise cet avantage.

Cet algorithme nous permettra de discerner $G(k) [:i-1]\\; ||\\; R[i-1:]$ de $G(k) [:i]\\; ||\\; R[i:]$ avec le même avantage et donc de prédire $G(k) [i]$ à partir de $G(k) [:i-1]$ avec encore une fois le même avantage. Ceci n'est pas possible puisque $G$ est non prédictible.

le générateur $G(k) [:i]\\; ||\\; R[i:]$ est donc sécurisé pour tout $i$ donc également pour $i=n$.

{% enddetails %}
{% info %}

- on note `||` l'opérateur de concaténation
- `m[:n]` correspond aux n-1 premiers bits de $m$
- `m[n:]` correspond à $m$ privé de ses $n-1$ premiers bits

{% endinfo %}

{% lien %}
[Article originel de Yao, 1982](https://www.di.ens.fr/users/phan/
secuproofs/yao82.pdf)
{% endlien %}

## Registre à décalage

{% aller %}

[Registre à décalage](https://fr.wikipedia.org/wiki/Registre_%C3%A0_d%C3%A9calage_%C3%A0_r%C3%A9troaction_lin%C3%A9aire)

{% endaller %}

> TBD

> TBD : soucis est que l'on doit tout faire pour déchiffrer. On ne peut pas faire d'avance rapide et se placer au milieu du film par exemple.
