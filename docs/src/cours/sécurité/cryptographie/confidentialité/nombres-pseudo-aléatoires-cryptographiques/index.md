---
layout: layout/post.njk

title: Nombres pseudo-aléatoires cryptographique

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Pour qu'Alice et Bob puissent générer la clé $K$ à $t$ bits à partir de la clé partagée à $s <t$ bits aléatoire, il est nécessaire d'avoir un algorithme déterministe permettant de générer (au moins) $t$ bits à partir des $s$ bits de $k$.

```
  ---------
  | s bit |            #  k
  ---------
  :        \
  :         \
  :          \
  :           \
  --------------
  |   t bits    |      # G(k)
  --------------
```

## Définition

Pour que l'algorithme de Vernam fonctionne il faut que $K$ le plus uniforme possible, ce qui impose la définition suivante :

<div id="CPRNG"></div>

{% note "**Définition**" %}
Un **_générateur de nombres pseudo-aléatoire sécurisé_** (_cryptographic pseudo random generator **CPRNG**_) doit avoir les propriétés suivantes :

- $G: \\{0, 1\\}^s \rightarrow \\{0, 1\\}^t$, avec $s <<t$
- $G$ doit être implémentable par algorithme efficace
- tout algorithme efficace ne peut avoir qu'un avantage négligeable au jeu de la reconnaissance [jeu de la reconnaissance](../définition-sécurité/#jeu-reconnaissance) entre :

- la variable aléatoire $G(k \xleftarrow{U} \\{0, 1\\}^s)$ prenant ses valeurs dans $\\{0, 1\\}^t$
- la variable aléatoire $x \xleftarrow{U} \\{0, 1\\}^t$

{% endnote %}
{% info %}
Le paramètre de $G$ est appelé _seed_
{% endinfo %}

Notez que cette condition est différente de celle des [PRNG](/cours/misc/aléatoire/nombres-pseudo-aléatoires/){.interne} qui ne supposent que l'uniformité statistique pour $k$ fixé (passent une batterie de tests statistiques).

Avec $G(k)$ une fonction permettant de générer $t$ bits à partir de $s$ bit (avec $s < n$, voir $s << n$).

La définition explicite fait qu'il est impossible de distinguer efficacement $G(k)$ d'un mot aléatoire et ce, quelque soit la _seed_ choisie.

{% attention "**À retenir**" %}
En cryptographie utilisez des générateurs fait pour cela. Ils sont plus lent mais sont non prédictible : simuler (le monde physique) est différent de se protéger.
{% endattention %}

Notez qu'un générateur de nombres pseudo-aléatoire sécurisé donne des résultats loin d'être aléatoire, en particulier distribution de sa sortie n'est **pas** uniforme :

- le nombre de chaînes atteignable depuis sa seed : $2^s$
- le nombre de chaînes possible : $2^{t} > 2^s$

Ne nombreuses chaînes ($2^{t-s}$) ne sont atteignables avec notre générateur. L'algorithme **non efficace** $D$ suivant va avoir un avantage non négligeable pour distinguer une sortie de $G$ d'une suite aléatoire :

1. il calcule $G(k)$ pour tous les $2^s$ valeurs de $k$ possible.
2. lorsque le testeur lui montre un mot $m$ de $\\{0, 1\\}^n$ il répond 1 s'il existe $k$ tel que $G(k)=m$, et 0 sinon.

Il reconnaît $G$ avec l'avantage suivant :

- $Pr[D(x) = 1 | b=1] = Pr[D(G(k)) = 1] = 1$
- $Pr[D(x) = 1 | b=0] = Pr[D(u) = 1] = 2^s/2^t = 1/2^{t-s}$ qui correspond à la probabilité que $u \xleftarrow{U} \\{0, 1\\}^t$ soit choisit parmi les mots possibles de $G$ ($2^s$ mots de $G$ parmi les $2^t$ mots possibles)

Son avantage est donc $1-1/2^{t-s}$ qui peut être énorme si $t>>s$

Cette attaque brute force nous donne une borne min acceptable pour une attaque : il faut que $s$ soit assez grand pour que générer toute les solutions soient non efficace.
Notez que ceci ne contredit pas la définition puisque l'adversaire n'est pas efficace.

## Non prédictabilité

Si l'on utilise notre générateur pour une transmission avec un chiffre de Vernam il est nécessaire que l'on ne puisse pas déterminer la fin de $G(k)$ en ayant son début. En effet, si un attaquant peut envoyer des messages à chiffrer, ou au moins une partie du message, il peut envoyer des 0 :

```
  kkkkkkk
⊕ 0000000
----------
  kkkkkkk
```

Pour trouver une partie de la clé. Si à partir de là on peut prédire la suite toute la sécurité en serait compromise.

Heureusement pour nous, non-prédictabilité et générateur de nombres pseudo-aléatoire sécurisé sont deux notions équivalentes.

{% note "**Définition**" %}
Une suite $({x^k_i})\_{i\geq 0}$ avec $k \in \\{0, 1\\}^s$ est **_non prédictible_** si tout algorithme efficace ne peut peut prédire $x^k_{m+1}$ sachant $x^k_1, \dots x^k_{m}$ qu'avec un avantage négligeable.
{% endnote %}

Ceci disqualifie d'emblée tous les générateurs pseudo-aléatoire de type $x^k_{i+1} = a \cdot x^k_{i} + b \bmod p$, puisque connaître $x^k_i$ permet de connaître tout $x^k_j$ avec $j> i$. Ceci est la principale différence entre un générateur pseudo-aléatoire et un générateur cryptographique : le premier veut obtenir une suite uniforme (ce que fait le générateur avec un modulo si $p$ est premier) alors que le second cherche à ne pas être prédictible.

Commençons par montrer qu'un générateur de nombres pseudo-aléatoire sécurisé est non prédictible :

{% note "**Proposition**" %}
Un générateur de nombres pseudo-aléatoire sécurisé $G$ produit une suite $G(k)$ de $\\{0, 1\\}^t$ non prédictible.
{% endnote %}
{% details "preuve", "open" %}

Supposons qu'un générateur de nombres pseudo-aléatoire sécurisé $G$ soit prédictible. Il existe alors un algorithme efficace $A$ qui possède un avantage non négligeable pour déterminer le $m+1$ ème bit de la suite à partir des $m$ premiers.

On peut utiliser cet algorithme pour déterminer si $G$ est un générateur de nombres pseudo-aléatoire sécurisé : on ne considère que les $m+1$ premiers bits et on rend la valeur donnée par l'algorithme $A$. L'avantage est le même et est non négligeable.

{% enddetails %}

La réciproque est plus compliquée, mais montre que les deux notions sont équivalentes :

<span id="théorème-yao"></span>

{% note "**Théorème (Yao, 1982)**" %}
Une suite non prédictible est un générateur de nombres pseudo-aléatoire sécurisé.
{% endnote %}
{% details "preuve", "open" %}

Soit $(x^k)_{1\leq i \leq t}$ une suite non prédictible et $u \xleftarrow{U} \\{0, 1\\}^t$ une variable aléatoire uniforme sur $\\{0, 1\\}^t$.

On construit la variable aléatoire $Y_i(k)$ sur $\\{0, 1\\}^t$ telle que :

- les $i$ premiers éléments de $Y_i(k)$ soient les $i$ premiers éléments de ${(x^k)}_{1\leq i \leq t}$
- les $t-i$ derniers éléments de $Y_i$ soient les $t-i$ derniers éléments d'une réalisation de $u \xleftarrow{U} \\{0, 1\\}^t$

Supposons qu'il existe $i$ tel que l'on puisse reconnaître $Y_i(k)$ de $Y_{i+1}(k)$ avec un avantage non négligeable. Prenons alors $i$ le plus petit possible et $A$ un algorithme efficace qui le reconnaît avec un avantage non négligeable. On a alors, avec $b$ une variable uniforme. :

<div>
$$
\begin{array}{lcl}
\epsilon(A) &=& \vert \Pr[A(Y_i(k)) = 1] - \Pr[A(Y_{i+1}(k)) = 1] \vert \\
&=& \vert \Pr[A({x^k}_1\dots{x^k}_ibu_{n-i+1}\dots u_n) = 1] - \Pr[A({x^k}_{1}\dots{x^k}_{i+1}u_{n-i}\dots u_n) = 1] \vert \\
\end{array}
$$
</div>

L'égalité précédente montre que l'algorithme qui rend $b$ tel que $A(x_1^k\dots x^k_ibu_{n-i+1}\dots u_n) = 1$ reconnaît $x^k_{i+1}$ sachant $x^k_1\dots x^k_i$ avec une probabilité $(1 + \epsilon(A))/2$ qui est non négligeable et $(x^k)_{1\leq i \leq t}$ est prédictible ce qui est contredit notre hypothèse.

On en conclut que pour tout $i$ $Y_i(k)$ est indiscernable de $Y_{i+1}(k)$, en particulier pour $i= t$ où l'on en conclut que $Y$ est indiscernable de $u \xleftarrow{U} \\{0, 1\\}^t$, ce qui conclut la preuve.

{% enddetails %}
{% lien %}
[Article originel de Yao, 1982](https://www.di.ens.fr/users/phan/secuproofs/yao82.pdf)
{% endlien %}

## Existence

{% lien %}
[Existence de générateur de nombres pseudo aléatoire cryptographique](https://en.wikipedia.org/wiki/Pseudorandom_generator_theorem#Existence_of_pseudorandom_generators)
{% endlien %}

L'existence de générateur de nombres pseudo-aléatoire sécurisé n'est pas garantie, mais est fortement soupçonnée comme on vale voir.

### <span id="construction-incrémentale"></span> Incrémentale

Commençons par voir qu'il suffit d'avoir un générateur de nombres pseudo-aléatoire sécurisé $G: \\{0, 1\\}^s \rightarrow \\{0, 1\\}^{s+1}$ pour construire un autre générateur de nombres pseudo-aléatoire sécurisé $G_m: \\{0, 1\\}^s \rightarrow \\{0, 1\\}^{m}$ pour tout $m\leq 1$.

<span id="chiffre-CPRNG-incrémental"></span>

{% note "**Proposition**" %}
Si $G: \\{0, 1\\}^s \rightarrow \\{0, 1\\}^{s+1}$ est un générateur de nombres pseudo-aléatoire sécurisé, alors la fonction $G_m: \\{0, 1\\}^s \rightarrow \\{0, 1\\}^{m}$ suivante est également n générateur de nombres pseudo-aléatoire sécurisé pour tout $m = \mathcal{O}(s^d)$ et $d$ une constante.

Avec $(x^i)\_{1\leq i \leq m}$ la suite finie définie telle que :

<div>
$$
\begin{cases}
x^1 = G(k)\\
x^i = G(x^{i-1}[:-1])\\
\end{cases}
$$
</div>

Et $G_m(k) = x^1[-1]\dots x^i[-1] \dots x^m[-1]$

{% endnote %}
{% details "preuve", "open" %}

Tout d'abord il est clair que $G_m$ est efficace pour tout $m = \mathcal{O}(s^d)$ si $G$ l'est. Soit $A$ un algorithme efficace permettant de prédire $x^m[-1]$ à partir des $x^1[-1], \dots, x^{m-1}[-1]$ avec un avantage $\epsilon(A)$.

Supposons maintenant que $G_m$ n'est pas un générateur de nombres pseudo-aléatoire sécurisé : il existe un algorithme $A$ efficace qui différencie $G_m(k \xleftarrow{U} \\{0, 1\\}^s)$ de $u \xleftarrow{U} \\{0, 1\\}^t$ avec un avantage non négligeable.

On peut maintenant créer une variable aléatoire $H_i = u \xleftarrow{U} \\{0, 1\\}^i \\;\\|\\; G_{m-i}(k \xleftarrow{U} \\{0, 1\\}^s)$ pour $0\leq i \leq m$.

L'avantage de $A$ s'écrit alors :

<div>
$$
\begin{array}{lcl}
\epsilon(A) &=& \vert \Pr[A(H_0) = 1] - \Pr[A(H_m) = 1] \vert \\
&=&  \vert \sum_{0\leq i < m} (\Pr[A(H_i) = 1] - \Pr[A(H_{i+1}) = 1]) \vert \\
&\leq&  \sum_{0\leq i < m} \vert (\Pr[A(H_i) = 1] - \Pr[A(H_{i+1}) = 1]) \vert \\
\end{array}
$$
</div>

On en conclut qu'en prenant $i^\star$ qui réalise le maximum de $\vert (\Pr[A(H_i) = 1] - \Pr[A(H_{i+1}) = 1]) \vert$ on a $\epsilon(A)/m \leq \vert (\Pr[A(H_{i^\star}) = 1] - \Pr[A(H_{i^\star+1}) = 1]) \vert$. L'algorithme $A$ distingue donc $H_{i^\star}$ de $H_{i^\star + 1}$ avec un avantage d'au moins $\epsilon(A)/m$ qui est non négligeable puisque $m = \mathcal{O}(s^d)$.

Soit alors l'algorithme $A'$ qui prend en paramètre un élément $x$ de $\\{0, 1\\}^s$ qui construit $H'\_{i^\star} = u \xleftarrow{U} \\{0, 1\\}^{i^\star} \\;\\|\\; G'\_{m-i^\star}(k \xleftarrow{U} \\{0, 1\\}^s)$ avec $G'$ construit comme $G$ mais avec $x^1 = x$ puis rend $A(H'_{i^\star})$ différencie $G(k \xleftarrow{U} \\{0, 1\\}^s)$ de $u \xleftarrow{U} \\{0, 1\\}^{s+1}$ avec le même avantage non négligeable que $A$ ce qui est impossible.

{% enddetails %}
{% info %}
L'opérateur $\\;\\|\\;$  est la concaténation de chaîne.
{% endinfo %}

Le contraire est bien sur évident :

{% note "**Proposition**" %}
Si $G: \\{0, 1\\}^s \rightarrow \\{0, 1\\}^{t}$ est un générateur de nombres pseudo-aléatoire sécurisé avec $t > s$ alors $G(x)[-1]$ est également un un générateur de nombres pseudo-aléatoire sécurisé.
{% endnote %}
{% details "preuve", "open" %}

S'il existait un algorithme avec un avantage non négligeable pour discriminer la restriction de la loi uniforme, il permettrait de discriminer $G$ avec le même avantage.

{% enddetails %}

### Fonctions à sens unique

Terminons cette partie en montrant que l'existence de générateur de nombres pseudo-aléatoire sécurisé est lié à l'existence de fonctions à sens unique.

{% note "**Proposition**" %}
S'il existe des générateurs de nombres pseudo-aléatoire sécurisés alors il existe des fonctions à sens unique
{% endnote %}
{% details "preuve", "open" %}

Soit $G: \\{0, 1\\}^s \rightarrow \\{0, 1\\}^{2s}$, un générateur de nombres pseudo-aléatoire sécurisé. [La partie précédente](./#construction-incrémentale){.interne} montre que cela existe.

Soit maintenant la fonction $f: \\{0, 1\\}^s \rightarrow \\{0, 1\\}^{s}$ telle que $f(x) = G(x)[:s]$.

On suppose que $f$ n'est pas à sens unique et on exhibe un algorithme $A$ efficace telle que :

<div>
$$
\Pr_{x \xleftarrow{U} \{0, 1\}^s}[f(A(f(x))) = f(x)] \geq \epsilon
$$
</div>

Avec $\epsilon$ non négligeable.

Soit alors l'algorithme $A'$ efficace qui, à partir d'une entrée $y$ de $2s$ bits rend : $1$ si G(A(y[:s])) = y$ et $0$ sinon. Cet algorithme reconnaît $G$ avec un avantage de :

<div>
$$
\vert \Pr_{x \xleftarrow{U} \{0, 1\}^{s}}[A'(G(x)) = 1] - \Pr_{x \xleftarrow{U} \{0, 1\}^{2s}}[A'(u) = 1] \vert
$$
</div>

On a alors :

- $Pr_{x \xleftarrow{U} \{0, 1\}^{s}}[A'(G(x)) = 1] \geq \epsilon$ puisque l'on utilise $A$
- $\Pr_{x \xleftarrow{U} \{0, 1\}^{2s}}[A'(u) = 1] \leq 1/2^s$ puisqu'il n'y a que $1/2^s$ chance que $u$ correspondent à une image de $G$.

Et l'avantage de $A'$ vaut $\epsilon-1/2^s$ qui est non négligeable ce qui est impossible puisque par hypothèse $G$ est un générateurs de nombres pseudo-aléatoire sécurisés.

{% enddetails %}

## Construction

On a vu que l'on ne connaît aucun générateur de nombres pseudo-aléatoire sécurisés. Les moyens actuels de construire ce que l'on pense être une bonne solution passe par des moyens détournés que nous allons maintenant voir.

L'idée est d'utiliser des permutations de $\\{0, 1\\}^t$ qui sont faciles à implémenter et dont la robustesse semble avérée. Mais avant de donner un exemple de permutation montrons que cette construction est valide.

Nous allons procéder en deux temps :

1. monter que l'on peut utiliser des fonctions pour approximer des générateurs pseudo-aléatoires
2. monter que l'on peut utiliser des permutations pour approximer des fonctions
3. donner un exemple de permutation

### Fonctions et générateurs pseudo-aléatoires

<div id="PRF"></div>

{% note "**Définition PRF**" %}
Soit $F: \\{0, 1\\}^s \times \\{0, 1\\}^t \rightarrow \\{0, 1\\}^t$ une fonction implémentable par un algorithme efficace.

$F$ est dite être une **fonction pseudo-aléatoire sécurisée** (_secure pseudo random function **PRF**_) si tout algorithme efficace ne peut avoir qu'un avantage négligeable au [jeu de la reconnaissance](../définition-sécurité/#jeu-reconnaissance){.interne} entre :

- la variable aléatoire $F(k \xleftarrow{U} \\{0, 1\\}^s, \cdot)$ prenant ses valeurs dans l'ensemble $\mathcal{F}(\\{0, 1\\}^t, \\{0, 1\\}^t)$ des fonctions de $\\{0, 1\\}^t$ dans $\\{0, 1\\}^t$
- la variable aléatoire $f \xleftarrow{U} \mathcal{F}(\\{0, 1\\}^t, \\{0, 1\\}^t)$

{% endnote %}

On peut utiliser une fonction pseudo-aléatoire sécurisée pour modéliser un générateur de nombres pseudo-aléatoire sécurisé :

{% note "**Proposition**" %}
Si $F: \\{0, 1\\}^s \times \\{0, 1\\}^n \rightarrow \\{0, 1\\}^n$ est une fonction pseudo-aléatoire sécurisée, alors $G(k) = F(k, \text{iv})$ est un générateur de nombres pseudo-aléatoire sécurisé pour tout $\text{iv} \in \\{0, 1\\}^t$ ($\text{iv}$ est appelé [vecteur d'initialisation](https://en.wikipedia.org/wiki/Initialization_vector)).
{% endnote %}

{% details "preuve", "open" %}
Si $G(k)$ n'est pas une fonction pseudo-aléatoire sécurisée, il existe un algorithme efficace $A$ ayant un avantage non négligeable le distinguant de $u \xleftarrow{U} \\{0, 1\\}^t$.

On crée alors l'algorithme $A'$ prenant en paramètre $f\in \mathcal{F}(\\{0, 1\\}^t, \\{0, 1\\}^t)$ et tel que $A'(f) = A(f(\text{iv}))$. Cet algorithme est un algorithme de reconnaissance de $F(k \xleftarrow{U} \\{0, 1\\}^s, \cdot)$ et son avantage est :

<div>
$$
\begin{array}{lcl}
\epsilon(A') &=& \vert \Pr_{k \xleftarrow{U} \{0, 1\}^s}[A'(F(k,\cdot)) = 1] - \Pr_{f \xleftarrow{U} \mathcal{F}(\{0, 1\}^t, \{0, 1\}^t)}[A'(f) = 1] \vert \\
&=& \vert \Pr_{k \xleftarrow{U} \{0, 1\}^s}[A(G(k)) = 1] - \Pr_{f \xleftarrow{U} \mathcal{F}(\{0, 1\}^t, \{0, 1\}^t)}[A(f(\text{iv})) = 1] \vert \\
\end{array}
$$
</div>

Si $f$ est une fonction quelconque de $\mathcal{F}(\\{0, 1\\}^t, \\{0, 1\\}^t)$ alors la probabilité que $f(\text{iv}) = x$ vaut $1/2^t$ (il faut que les valeurs coïncident bit à bit) pour tout $x\in \\{0, 1\\}^t$. De là : $\Pr_{f \xleftarrow{U} \mathcal{F}(\\{0, 1\\}^t, \\{0, 1\\}^t)}[A(f(\text{iv})) = 1] = \Pr_{u \xleftarrow{U} \\{0, 1\\}^t}[A(u) = 1]$ et :

<div>
$$
\begin{array}{lcl}
\epsilon(A') &=& \vert \Pr_{k \xleftarrow{U} \{0, 1\}^s}[A(G(k)) = 1] - \Pr_{u \xleftarrow{U} \{0, 1\}^t}[A(u) = 1] \vert \\
&=& \epsilon(A)
\end{array}
$$
</div>

Qui est non négligeable Ce qui est impossible.

{% enddetails %}

Notez qu'on est passé d'un générateur à un paramètre $G(k)$ à un générateur à deux paramètres $F(k, \text{iv})$ que l'on peut prendre indépendamment.

### Fonctions et permutations

<div id="PRP"></div>

{% note "**Définition PRP**" %}
Soit $F: \\{0, 1\\}^s \times \\{0, 1\\}^t \rightarrow \\{0, 1\\}^t$ une fonction pseudo-aléatoire sécurisée.

$F$ est une **permutation pseudo-aléatoire sécurisée** (_secure **PRP**, pseudo random permutation_) si :

- $F(k, \cdot)$ est une permutation de $\\{0, 1\\}^t$ pour tout $k \in \\{0, 1\\}^s$
- tout algorithme efficace ne peut avoir qu'un avantage négligeable au [jeu de la reconnaissance](../définition-sécurité/#jeu-reconnaissance) entre :
  - une permutation $F(k, \cdot)$ pour $k$ uniformément choisie,
  - une permutation $f$ uniformément choisie parmi toutes les permutations de $\\{0, 1\\}^t$ dans $\\{0, 1\\}^t$.

{% endnote %}

Une PRP est un cas particulier de PRF, mais si $n$ est grand, elle est indistinguable d'une fonction quelconque avec un avantage non négligeable :

{% note "**Proposition**" %}
Une **PRP** ne peut être distinguée d'une fonction **PRF** qu'avec un avantage non négligeable par un algorithme efficace.

{% endnote %}
{% details "preuve", "open" %}

On considère le jeu de la reconnaissance où un algorithme efficace cherche à distinguer une permutation $F(k, \cdot)$ pour un $k$ uniformément choisi d'une fonction $f$ uniformément choisie parmi toutes les fonctions de $\\{0, 1\\}^t$ dans $\\{0, 1\\}^t$.

La seule façon de distinguer une permutation d'une simple fonction est de chercher des points fixes : s'il existe $x\neq y$ tel que $f(x) = f(y)$, $f$ n'est pas une permutation. Comme les fonctions sont tirées aléatoirement, vérifier si $N$ éléments ont des images différentes a la même probabilité que savoir si $N$ éléments tirés aléatoirement sont différents. En reprenant la démonstration du [paradoxe des anniversaires](/cours/algorithmie/structure-dictionnaire/fonctions-hash/#paradoxe-anniversaires){.interne}, cette probabilité vaut :

<div>
$$
\bar{p}(N, 2^t) = \prod_{i=1}^{N}(1-\frac{i-1}{2^t})
$$
</div>

Le nombre de tirages $N$ est plus petit que la complexité de l'algorithme et comme celui-ci est efficace il est borné par $K\cdot n^d$ avec $d$ et $K$ deux constantes, et $n$ le paramètre de sécurité, supérieur à $t$. De là $N << 2^t$ et :

<div>
$$
\bar{p}(N, 2^t) \leq (1-\frac{1}{2^t})^N \simeq 1-\frac{N}{2^t} \leq 1-\frac{t^d}{2^t}
$$
</div>

Le meilleur avantage possible que peut avoir un adversaire efficace au jeu de la reconnaissance est donc $1-\bar{p}(N, 2^t) \leq \frac{t^d}{2^t}$, qui est négligeable.

{% enddetails %}

La proposition précédente fait des permutation pseudo-aléatoire sécurisée des candidats idéaux pour pour nos méthodes de chiffrement, ce sont des bijections mais vues de l'extérieur (_ie_ d'un adversaire) elles sont indistinguables de simples fonctions. Comme leur existence va impliquer l'existence de fonctions à sens unique, on ne sais pas si cela existe. Mais l'idée de leur construction est simple :

1. on fabrique une bijection
2. on utilise la clé pour mélanger l'entrée

Comme on doit être efficace, on ne va parcourir qu'un tout petit nombre de bijections possibles, mais si on fait un mélange qu'on espère uniforme on va bien avoir des comportement très différent quelque soit la clé utilisée.

## Implémentations

Nous allons voir trois implémentations différentes :

1. avec un PRP comme désigné précédemment. On reverra ce code plus tard
2. avec un générateur type modulo qui se base sur des fonctions à sens unique
3. avec un générateur qui s'implémente très bien sur des circuit

### Chacha20

{% lien %}
[chacha20](https://en.wikipedia.org/wiki/Salsa20#ChaCha_variant)
{% endlien %}

Nous étudierons plus tard ce protocole pour des tailles de messages variables. Mais juste pour terminer cette partie c'est un PRP très simple à taille fixe 256b.

Il implémente de nombreuses chose qu'on a vu dans ce cours :

- son principe directeur est une permutation de son état interne
- il est de complexité linéaire (fonctionne sur des mots de 32b)
- robuste à de nombreuses attaques :
  - time et side channel attack : toutes les opérations sont de même complexité
  - opérations non linéaires pour éviter [la cryptanalyse linéaire](https://fr.wikipedia.org/wiki/Cryptanalyse_lin%C3%A9aire)
  - vol de l'état interne

Nous allons uniquement survoler son principe, nous y reviendrons en détail lorsque nous étudierons son implémentation dns un chiffrement réel et complet.

#### Principe

Son cœur est une permutation, mais son implémentation diffère un peu des PRP (la clé fait partie de la valeur d'initiation) car à l'origine chacha20 était [salsa20](https://en.wikipedia.org/wiki/Salsa20), un hash cryptographique. La  proposition de sécurité reste valable puisque cette valeur peut être quelconque et on a dans notre cas la permutation $G(k) = P(k, k \;\|\; \text{IV}) = Q(K \\;\\|\\; k \\;\\|\\; \text{IV})$.

Le chiffre final est obtenu en additionnant la permutation à l'entrée :
<div>
$$
C(k) = Q(K \;\|\; k \;\|\; \text{IV}) + (K \;\|\; k \;\|\; \text{IV})
$$
</div>

Où :

- $k \in \\{0, 1\\}^{256}$
- $\text{IV} \in \\{0, 1\\}^{128}$
- $K \in \\{0, 1\\}^{128}$ une constante
- $+$ est l'addition (modulaire, donc sans retenue) sur 32b
- $Q$ est une permutation de $\\{0, 1\\}^{512}$.

{% lien %}
[exemple de modifications](https://datatracker.ietf.org/doc/html/rfc7539#section-2.3.2)
{% endlien %}

#### opérations ARX

Les opérations utilisés pour la permutation sont de type ARX sur 32b :

- Addition modulaire `+`
- Rotation `<<<` ou `>>>` de bits
- Xor `^`

Ces opérations sont suffisantes pour engendrer toutes les permutations et l'organisation de la permutation permet un parallélisme accrus.

{% lien %}
Suffisant pour faire toutes les rotations <https://eprint.iacr.org/2022/618.pdf>
{% endlien %}

#### Robustesse

- ARX pour time attack
- non linéarité (l'addition)
- vol de l'état interne (la dernière addition permet de cacher la clé car la permutation est inversible)

### Blum Blum Shub

{% lien %}
[Blum Blum Shub](https://fr.wikipedia.org/wiki/Blum_Blum_Shub)
{% endlien %}

Le générateur est basé sur la récursion suivante :

<div>
$$
\begin{cases}
x_n = x_{n-1}^2 \bmod M\\
g_n = x_n \bmod 2
\end{cases}
$$
</div>

Avec :

- $M = p \cdot q$ et $p$ et $q$ premiers tels que :
  - $p \bmod M = q \bmod M = 3\bmod 4$ (un liste [ici](http://villemin.gerard.free.fr/aNombre/TYPDIVIS/Blum.htm))
  - $2p + 1$ et $2q +1$ doivent aussi être premiers ([nombres premiers de Sophie Germain](https://fr.wikipedia.org/wiki/Nombre_premier_de_Sophie_Germain)), [safe prime](https://en.wikipedia.org/wiki/Safe_and_Sophie_Germain_primes#Cryptography)
- la seed $x_0 > 1$ premier avec $M$
- l'état interne du générateur est la suite $(x_i)_{i\geq 1}$ qui es secrète
- la sortie du générateur est la suite $(g_i)_{i\geq 1}$

Si la factorisation est une fonction à sens unique, alors l'algorithme Blum Blum Shub est un CPRNG. Il n'est pas utilisé en pratique car lent, mais il est marrant.

Sa période vaut $\lambda(M)$ où $\lambda$ est la [fonction de Carmichael](https://en.wikipedia.org/wiki/Carmichael_function).

{% lien %}

- <https://iczelia.net/posts/bbs-survey/>
- [Preuves](https://www.cs.miami.edu/home/burt/learning/Csc609.062/docs/bbs.pdf)
- <https://crypto.stackexchange.com/questions/109081/period-of-blum-blum-shub>

{% endlien %}

Attention, $M$ doit être secret. Donc pas exactement ce qu'on a vu puisque :

- soit la clé et M sont le secret mais du cop pas uniforme dans $\\{0, 1\\}^s$. Un autre espace
- soit ne respecte pas Kerskoff.

De toute façon il est lent et son intérêt est plutôt théorique.

### Registre à décalage cryptographique

> TBD renvoyer vers aléatoire et le gros TP
> TBD (monter que c'était implémenté partout) et mal ou de façon ancienne => du coup marche plus quand le nb de clés doit augmenter.

{% lien %}
[Rapport Laura](Rapport_de_Stage_Laura_Michelutti.pdf)
{% endlien %}

### Cryptographie en python

> TBD module [secrets](https://docs.python.org/fr/3/library/secrets.html#module-secrets)


<!-- ## Attaques

### Trouver les états internes

> TBD 

### Utiliser des PRNG à la place de CPRNG

- <https://book-of-gehn.github.io/articles/2018/12/23/Mersenne-Twister-PRNG.html>
- <https://www.schutzwerk.com/en/blog/attacking-a-rng/>
 -->

