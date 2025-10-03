---
layout: layout/post.njk

title: Chiffrement par flux

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le chiffrement par flux est une façon d'implémenter l'algorithme de Vernam en utilisant une taille de clé plus petite que le bloc à coder.

Le [PRP](../chiffrement-cloc/#PRP)  $F: \\{0, 1\\}^s \times \\{0, 1\\}^t \rightarrow \\{0, 1\\}^t$ utilisé est celui ci :

<div>
$$
F(k, m) = m \oplus g(k)
$$
</div>

Avec $G(k)$ une fonction permettant de générer $t$ bits à partir de $s$ bit (avec $s < n$, voir $s << n$).

```
  ---------
  | k bit |
  ---------
  :        \
  :         \
  :          \
  :           \
  --------------
  |G(k) à t bits|
  --------------
```

S'il est clair que $F(k, \cdot)$ $ est une permutation quelque soit $k$ (l'inverse étant la fonction elle même), nous allons allons montrer qu'elle est sémantiquement sécurisée si le générateur $G$ l'est.

## Générateur de nombre

Générer des nombres purement aléatoire est impossible pour un algorithme. Il faut donc trouver une façon de simuler ce hasard, ou tout du moins de garantir qu'un algorithme efficace ne puisse voir la supercherie.

<div id="PRG"></div>

{% note "**Définition**" %}
Un **générateur de nombres pseudo-aléatoire sécurisé** (_secure PRG, secure pseudo random generator_) doit avoir les propriétés suivantes :

- $G: \\{0, 1\\}^s \rightarrow \\{0, 1\\}^n$, avec $s <<n$
- $G$ doit être implémentable par algorithme efficace
- tout algorithme efficace ne peut avoir qu'un avantage négligeable au jeu de la reconnaissance  [jeu de la reconnaissance](../définitions/#jeu-reconnaissance) entre :

- un élément $G(k) \in \\{0, 1\\}^t$ pour $k$ uniformément choisi,
- un élément de \\{0, 1\\}^t$ uniformément choisi.

{% endnote %}
{% info %}
Le paramètre de $G$ est appelé _seed_
{% endinfo %}

La définition explicite fait qu'il est impossible de distinguer efficacement $G(k)$ d'un mot aléatoire et ce, quelque soit la _seed_ choisie.

{% note %}
En règle générale, en cryptographie, utilisez des générateurs fait pour cela. Ils sont plus lent mais sont non prédictible : simuler (le monde physique) est différent de se protéger.
{% endnote %}

### Générateur et PRP

Sémantiquement sécurisé suffit pour garantir que notre PRP est sémantiquement sécurisé :

{% note "**Proposition**" %}
Si $G: \\{0, 1\\}^s \rightarrow \\{0, 1\\}^n$, avec $s <<n$ est un secure PRG, alors :

- $E(k, m) = G(k) \oplus m$
- $D(k, m) = E(k, m)$

est une méthode de chiffrement sécurisée.
{% endnote %}
{% details "preuve", "open" %}

> TBD preuve : <https://www.youtube.com/watch?v=4vbwxPR_D2U>

Si la méthode n'est pas sémantiquement sécurisée, il existe deux mots $m_0$ et $m_1$ et un algorithme A ayant un avantage non négligeable pour reconnaître $G(k) \oplus m_0$ de $G(k) \oplus m_1$. On a alors :

<div>
$$
\begin{array}{lcl}
\text{avantage}(A) &=& |Pr[b'=1 | b=1] - Pr[b'=1 | b=0]|\\
&=&|\frac{1}{2}\sum_{X\in \{0, 1\}^n}Pr[A(G(k)\oplus m_1) = 1]\cdot Pr[X=G(k)] - Pr[A(G(k) \oplus m_0) =1]\cdot Pr[X=G(k)]|\\
&\leq&|\frac{1}{2}\sum_{X\in \{0, 1\}^n}Pr[A(G(k)\oplus m_1) = 1]\cdot Pr[X=G(k)] - Pr[A(X) = 1]\cdot (1/2)^n| +\\
&&|\frac{1}{2}\sum_{X\in \{0, 1\}^n} Pr[A(G(k) \oplus m_0) =1]\cdot Pr[X=G(k)] - Pr[A(X) = 1]\cdot (1/2)^n|\\
\end{array}
$$
</div>

On peut supposer sans perte de généralité que :

<div>
$$
\begin{array}{lcl}
\text{avantage}(A) &\leq&2\cdot|\frac{1}{2}\sum_{X\in \{0, 1\}^n}Pr[A(G(k)\oplus m_1) = 1]\cdot Pr[X=G(k)] - Pr[A(X) = 1]\cdot (1/2)^n|
\end{array}
$$
</div>

Puisque $X\oplus m_1$ est distribué de façon uniforme, on a donc aussi :

<div>
$$
\begin{array}{lcl}
\text{avantage}(A) &\leq&2\cdot|\frac{1}{2}\sum_{X\in \{0, 1\}^n}Pr[A(G(k)\oplus m_1) = 1]\cdot Pr[X=G(k)] - Pr[A(X\oplus m_1) = 1]\cdot (1/2)^n|
\end{array}
$$
</div>

On peut alors utiliser l'algorithme $A'$ qui prend en entrée un mot $y\in \\{0, 1\\}^n$ et qui rend $A'(y) = A(y \oplus m_1)$.

Son avantage vaut :

<div>
$$
\begin{array}{lcl}
\text{avantage}(A') &=& Pr[b'=1 | b=1] - Pr[b'=1 | b=0]\\
&=&\frac{1}{2}\sum_{X\in \{0, 1\}^n}|Pr[A(G(k)\oplus m_1) = 1]\cdot Pr[X=G(k)] - Pr[A(X \oplus m_1) =1]\cdot (1/2)^n|\\
\end{array}
$$
</div>

On a alors que l'avantage de $A$ ne peut être non négligeable puisque que $A'$ discrimine $G(k)$ d'une loi uniforme et est statistiquement sécurisé.

{% enddetails %}

Notez qu'un générateur de nombre donne des résultats loin d'être aléatoires.

En effet :

- le nombre de chaînes atteignable depuis sa seed : $2^s$
- le nombre de chaînes possible : $2^{t} > 2^s$

Considérons l'algorithme **non efficace** $D$ suivant :

1. il calcule $G(k)$ pour tous les $2^s$ valeurs de $k$ possible.
2. lorsque le testeur lui montre un mot $m$ de $\\{0, 1\\}^n$ il répond 1 s'il existe $k$ tel que $G(k)=m$, et 0 sinon.

Il reconnaît $D$ avec l'avantage suivant :

- $Pr[D(G) = 1 | b=1] = 1$
- $Pr[D(G) = 1 | b=0] = 2^s/2^n = 1/2^{n-s}$ qui correspond à la probabilité que $N$ soit choisit parmi les mots possibles de $G$ ($2^s$ mots de $G$ parmi les $2^n$ mots possibles)

Son avantage est donc $1-1/2^{n-s}$ qui peut être énorme si $n>>s$

Cette attaque brute force nous donne une borne min acceptable pour une attaque : il faut que $s$ soit assez grand pour que générer toute les solutions soient non efficace.

### <span id="construction-générateur"></span>Construction d'un générateur

Enfin, créer un générateur peut se faire simplement si on a à notre disposition une [PRF](../#définitions/#PRF){.interne} :

{% note "**Proposition**" %}
Si $F: \\{0, 1\\}^s \times \\{0, 1\\}^n \rightarrow \\{0, 1\\}^n$ est une secure PRF, alors $G(k) = F(k, x)$ est un secure PRG pour tout $x$.
{% endnote %}

{% details "preuve", "open" %}
Si $H$ est une fonction quelconque de $\\{0, 1\\}^n$ dans $\\{0, 1\\}^n$ alors la probabilité que $H(x) = F(k, x)$ vaut $1/2^n$ (il faut que les valeurs coïncident bit à bit).

De là, si $G(k)$ n'est pas un secure PRG, il existe un algorithme efficace $A$ ayant un avantage non négligeable le distinguant de la loi uniforme.

On peut utiliser cet algorithme dans la reconnaissance de $F$ comme un secure PRF en ne demandant que la valeur en $x$ et reconnaître F avec le même avantage non négligeable : $F$ n'est pas un secure PRF ce qui contredit notre hypothèse.
{% enddetails %}

Comme une [PRP](../#définitions/#PRP){.interne} peut être utilisée en lieu et place d'une PRF sans gagner plus qu'un avantage négligeable, on a coutume d'utiliser des méthodes de chiffrement classiques (comme chacha20 ou aes) pour créer cette méthode de chiffrement.

Notez qu'on est passé d'un générateur à un paramètre $G(k)$ à un générateur à deux paramètres $F(k, r)$ que l'on peut prendre indépendamment.

## PRG et _prédictabilité_

> TBD à comparer aux générateur de nombres pseudo-aléatoire que l'on verra ensuite en algorithmie.

{% note %}
Une suite $g(k,1), \dots g(k, m + 1)$ est non prédictible si tout algorithme efficace ne peut peut prédire $g(k, m + 1)$ sachant $g(k, 1), \dots, g(k, m)$ qu'avec un avantage négligeable.
{% endnote %}

Le générateur de nombre pseudo-aléatoire tel que $x_i = a \cdot x_{i-1} + b \bmod p$ ne l'est pas, malgré le fait qu'il possède de belle propriétés statistiques si $p$ est premier. Pour qu'un générateur de nombre puisse être utilisé de façon cryptographe, on s'intéresse moins à ses propriété d'uniformité qu'à sa non prédictibilité.

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
[Article originel de Yao, 1982](https://www.di.ens.fr/users/phan/secuproofs/yao82.pdf)
{% endlien %}
