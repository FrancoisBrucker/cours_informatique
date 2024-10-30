---
layout: layout/post.njk

title: Générateur et XOR 

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


> TBD One Time Pad : on génère des nombres à partir d'une seed comme on le ferait avec un générateur normal, mais être sécurisé.

> TBD Algorithme via générateur pseudo-aléatoire


> TBD preuves avec les jeux et les avantages et on le fait dans l'autre sens en revenant au truc le plus simple à la fin : PRF qui est un générateur à une clé coupée en 2.

Nous allons utiliser ici
Le **_chiffrement par flux_** _stream cicher_ reprend directement l'idée du code de Vernam et l'adapte aux contraintes d'utilisation réelle :

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

On définit la **_reconnaissance $G: K \rightarrow U$_** par un jeu :

```
      testeur                            adversaire A
 b  -----------                         -------------
--->|   N     |                         |           |
    |   k     |   G(k) si b=1 N sinon   |           |
    |         |------------------------>|           | A(X) = b'
    |         |                         |           |------------>
    -----------                         -------------
```

A l'initialisation :

- un bit $b$ est choisi uniformément
- une valeur $k$ de $K$ est choisie uniformément
- une valeur $N$ de $U$ est choisie uniformément

{% note "**Définition**" %}
L'**_avantage_** d'un algorithme $A$ au jeu de la reconnaissance de $G$ est :

<div>
$$
\vert Pr_{k \xleftarrow{R} \mathcal{U}}[A(G(k))=1] - Pr_{X \xleftarrow{R} \mathcal{K}}[A(X)=1] \vert
$$
</div>

{% endnote %}

L'avantage montre l'écart à l'uniformité de $G$ reconnaissable et donc exploitable par un algorithme. Moins cette écart est grand, moins il est exploitable par une attaque.

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
- le nombre de chaînes possible : $2^{n} > 2^s$

Considérons l'algorithme **non efficace** $D$ suivant :

1. il calcule $G(k)$ pour tous les $2^s$ valeurs de $k$ possible.
2. lorsque le testeur lui montre un mot $m$ de $\\{0, 1\\}^n$ il répond 1 s'il existe $k$ tel que $G(k)=m$, et 0 sinon.

Il reconnaît $D$ avec l'avantage suivant :

- $Pr[D(G) = 1 | b=1] = 1$
- $Pr[D(G) = 1 | b=0] = 2^s/2^n = 1/2^{n-s}$ qui correspond à la probabilité que $N$ soit choisit parmi les mots possibles de $G$ ($2^s$ mots de $G$ parmi les $2^n$ mots possibles)

Son avantage est donc $1-1/2^{n-s}$ qui peut être énorme si $n>>s$

Cette attaque brute force nous donne une borne min acceptable pour une attaque : il faut que $s$ soit assez grand pour que générer toute les solutions soient non efficace.

### Construction d'un PRG avec un PRF

{% note "**Proposition**" %}
Si $F: \\{0, 1\\}^s \times \\{0, 1\\}^n \rightarrow \\{0, 1\\}^n$ est une secure PRF, alors $G(k) = F(k, x)$ est un secure PRG pour tout $x$.
{% endnote %}

{% details "preuve", "open" %}
Si $H$ est une fonction quelconque de $\\{0, 1\\}^n$ dans $\\{0, 1\\}^n$ alors la probabilité que $H(x) = F(k, x)$ vaut $1/2^n$ (il faut que les valeurs coïncident bit à bit).

De là, si $G(k)$ n'est pas un secure PRG, il existe un algorithme efficace $A$ ayant un avantage non négligeable le distinguant de la loi uniforme.

On peut utiliser cet algorithme dans la reconnaissance de $F$ comme un secure PRF en ne demandant que la valeur en $x$ et reconnaître F avec le même avantage non négligeable : $F$ n'est pas un secure PRF ce qui contredit notre hypothèse.
{% enddetails %}

Cette construction va être utilisée par quasi tous les codes pour créer des codages sécurisées. Notez qu'on est passé d'un générateur à un paramètre $G(k)$ à un générateur à deux paramètres $F(k, r)$ que l'on peut prendre indépendamment.


L'exemple précédent n'est pas utilisable en pratique car sans clé on ne retrouve plus l'entrée.

{% note "**Définition**" %}
Un **générateur de nombres pseudo-aléatoire sécurisé** (_secure PRG, secure pseudo random generator_) doit avoir les propriétés suivantes :

- $G: \\{0, 1\\}^s \rightarrow \\{0, 1\\}^n$, avec $s <<n$
- $G$ doit être implémentable par algorithme efficace
- tout algorithme efficace ne peut avoir qu'un avantage négligeable au jeu de la reconnaissance $G$.

{% endnote %}
{% info %}
Le paramètre de $G$ est appelé _seed_
{% endinfo %}

La définition explicite le fait qu'il est impossible de distinguer efficacement $G(k)$ d'un mot aléatoire et ce, quelque soit la _seed_ choisie.

{% note %}
En règle générale, en cryptographie, utilisez des générateurs fait pour cela. Ils sont plus lent mais sont non prédictible : simuler (le monde physique) est différent de se protéger.
{% endnote %}