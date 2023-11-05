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

{% note "**Définition**" %}
Un **générateur de nombres pseudo-aléatoire sécurisé** (*secure PRG, secure pseudo random generator*) doit avoir les propriétés suivantes :

- $G: \\{0, 1\\}^s \rightarrow \\{0, 1\\}^n$, avec $s <<n$
- algorithme efficace (ie polynomial)
- sa sortie soit ***non distinguable d'une suite aléatoire***.
{% endnote %}
{% info %}
Le paramètre de $G$ est appelé *seed*
{% endinfo %}

On définit la ***non-distinguabilité*** par un jeu :

```
      testeur            adversaire
    -----------         ------------
 b  |  k, S   |         |          | rép(b) = b'
--->|         |         |          | ------------>
    |         |  G(k)   |          |
    | si b=0 -|-------->|          |
    |         |         |          |
    |         |   S     |          |
    | si b=1 -|-------->|          |
    -----------         ------------
```

A l'initialisation, le testeur choisit :

- une seed $k$
- un mot $S$ uniformément parmi toutes les mots de $\\{0, 1\\}^n$

L'adversaire doit choisir si le mot fournit vient de $G$ (notre PRG) ou est le mot aléatoire $S$ (une réelle suite aléatoire).

$G$ est non distinguable de $S$ si tout algorithme efficace jouant au jeu ne peut obtenir qu'un avantage négligeable.

{% exercice %}
Le générateur avec un biais négligeable de la partie précédente est bien un PRG sécurisé.
{% endexercice %}
{% details "preuve" %}
> TBD
{% enddetails %}

En règle générale, en cryptographie, utiliser des générateurs fait pour cela. Ils sont plus lent mais sont non prédictible : simuler (le monde physique) est différent de protéger.

### Existence

L'existence de générateur de nombre pseudo-aléatoire sécurisé n'est pas prouvée. Ils dépendent de l'existence de fonction pseudo-aléatoire sécurisées.

{% note "**Définition**" %}
Une **fonction pseudo-aléatoire sécurisé** (*secure PRF, pseudo random function*) doit avoir les propriétés suivantes :

- $F: \\{0, 1\\}^s \times \\{0, 1\\}^n \rightarrow \\{0, 1\\}^n$, avec $s <<n$
- algorithme efficace (ie polynomial)
- $F(k, \cdot)$ doit être non distinguable de $F': \\{0, 1\\}^n \rightarrow \\{0, 1\\}^n$ une fonction quelconque.
{% endnote %}

Comme toujours on définit la ***non-distinguabilité*** par un jeu :

```
      testeur                            adversaire
    -----------       x1, ..., xm       ------------
 b  |  k, H   | <-----------------------|          | rép(b) = b'
--->|         |                         |          | ------------>
    |         | F(k, x1), ..., f(k, xm) |          |
    | si b=0 -|------------------------>|          |
    |         |                         |          |
    |         |  H(x1), ..., H(xm)      |          |
    | si b=1 -|------------------------>|          |
    -----------                         ------------
```

A l'initialisation, le testeur choisit :

- une seed $k$
- un function $H$ uniformément parmi toutes les fonctions de $\\{0, 1\\}^n$ dans $\\{0, 1\\}^n$.

L'adversaire doit choisir si les $n$ mots fournit viennent de $F$ (notre PRF) ou de $H$ (une fonction quelconque).

$F$ est non distinguable de $H$ si tout algorithme efficace jouant au jeu ne peut obtenir qu'un avantage négligeable.

Notez que le fait que l'on utilise des algorithme efficaces, $m$ ne peut être que polynomial en $n$.

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

### Non prédictible

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

## Algorithme de chiffrement par flux

Schéma général du chiffrement par flux

### PRG

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

{% note "**Proposition**" %}
Si $F: \\{0, 1\\}^s \times \\{0, 1\\}^n \rightarrow \\{0, 1\\}^n$$ est une secure PRF, alors :

- $E(k, m) = r || (F(k, r) \oplus m)$
- $D(k, m) = F(k, m[:n]) \oplus mm[n:]$

{% endnote %}
{% details "preuve" %}
> TBD : construction 3.25 Introduction to modern cryptography
{% enddetails %}

## Exemples

Exemple ancien et nouveau

### Registre à décalage

{% aller %}

[Registre à décalage](https://fr.wikipedia.org/wiki/Registre_%C3%A0_d%C3%A9calage_%C3%A0_r%C3%A9troaction_lin%C3%A9aire)

{% endaller %}

> TBD

> TBD : soucis est que l'on doit tout faire pour déchiffrer. On ne peut pas faire d'avance rapide et se placer au milieu du film par exemple.

### Chacha

On règle le problème précédent en découpant le message en bloc et en générant $n$ bit par $n$ bits.

Mais il faut faire ça bien pour garde la sécurité. Rappelez vous que le OTP ne fonctionne que si c'est One Time.

{% lien %}

Chacha :

- [fonctionnement et origine](https://en.wikipedia.org/wiki/Salsa20#ChaCha_variant)
- [design](https://loup-vaillant.fr/tutorials/chacha20-design)
- [spec et implémentations](https://cr.yp.to/chacha.html)
- [RFC](https://datatracker.ietf.org/doc/html/rfc8439)

{% endlien %}

> TBD : besoin d'un nonce
> TBD non linéarité très important sinon attaque possible
> on évite l'utilisation de la même clés en utilisant une nonce et
> F(k, 0 ) || F(k, 1 ) || F(k, 2) qui est un secure prg.

> TBD : en vrai chacha est un code par bloc puis rabouter entre eux.
> Mais c'est bien fait. Démo que si on utilise plusieurs la clé soucis mais pas si randomisé
