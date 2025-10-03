---
layout: layout/post.njk 
title:  "Fonctions booléennes et pseudo-code"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD chapeau

[On a vu](../bases-théoriques/calculabilité/#algorithme-fonction){.interne} qu'un algorithme était une fonction $f: \\{0, 1\\}^\star \rightarrow \\{0, 1\\}^\star$. Nous allons voir celles que l'on peut décrire par [un pseudo-code](../pseudo-code/){.interne}.

## Fonctions booléennes vectorielles

<span id="définition-fonction-booléenne"></span>

{% note "**Définition**" %}
Une **_fonction booléenne_** est une fonction

<div>
$$
f: \{0, 1\}^n \rightarrow \{0, 1\}
$$
</div>

> TBD exemple de la projection
> 
Et une **_fonction booléenne vectorielle_** est une fonction booléenne qui rend un vecteur :

<div>
$$
f: \{0, 1\}^n \rightarrow \{0, 1\}^m
$$
</div>

{% endnote %}

> TBD exemple de la duplication

### Fonctions logiques

Parmi les fonctions booléennes, les fonctions $f: \\{0, 1\\} \rightarrow \\{0, 1\\}$ et $f: \\{0, 1\\}^2 \rightarrow \\{0, 1\\}$ sont appelées **_opérateurs logiques_**.

#### Fonctions à un bit

Il y a 4 fonctions différentes dont l'entrée est réduite à 1 bit :

- la fonction identité définie telle que $id(x) = x$ pour tout $x$,
- la fonction $\mathbb{1}$ définie telle que $\mathbb{1}(x) = 1$  pour tout $x$,
- la fonction $\mathbb{0}$ définie telle que $\mathbb{0}(x) = 0$  pour tout $x$,
- la fonction négation définie telle que $\text{NOT}(0) = \neg 0 = \overline{0} = 1$ et $\text{NOT}(1) = \neg 1 = \overline{1} = 0$

#### Fonctions à deux bits

On les décrit avec leurs  On les représentent via leurs [tables de vérité](https://fr.wikipedia.org/wiki/Table_de_v%C3%A9rit%C3%A9) :

{% note "**Définition**" %}

On décrit les 3 fonctions $f: \\{0, 1\\}^2 \rightarrow \\{0, 1\\}$ **_OU_**, **_ET_** **_OU exclusif_** comme étant :

   |   |     OU     |  ET         |  OU exclusif|
 x | y |   OR(x, y) |  AND(x, y)  |  XOR(x, y)  |
   |   | $x \lor y$ | $x \land y$ |$x \oplus y$ |
:-:|:-:|:----------:|:-----------:|:-----------:|
 0 | 0 |    0       |      0      |      0      |
 0 | 1 |    1       |      0      |      1      |
 1 | 0 |    1       |      0      |      1      |
 1 | 1 |    1       |      1      |      0      |

{% endnote %}

Nous n'en avons décrit que 3 parmi les 16 possibles car il est possible de toutes les obtenir en combinant les fonctions NON, OU et ET. Par exemple : 

<div>
$$
x \oplus y = (x \lor y) \land \overline{x \land y}
$$
</div>

{% exercice %}
Démontrez que :

<div>
$$
x \oplus y = (x \lor y) \land \overline{x \land y}
$$
</div>
{% endexercice %}
{% details "corrigé" %}
On le fait avec une table :


 x | y | $x \lor y$ | $\overline{x \land y}$ |$x \oplus y$ |
:-:|:-:|:----------:|:-----------:|:-----------:|
 0 | 0 |    0       |      1      |      0      |
 0 | 1 |    1       |      1      |      1      |
 1 | 0 |    1       |      1      |      1      |
 1 | 1 |    1       |      0      |      0      |

{% enddetails %}

On peut maintenant terminer le travail :

{% exercice %}
Montrer que toute fonction de $\\{0, 1\\}^2 \rightarrow \\{0, 1\\}$ peut s'écrire comme combinaison des fonctions $\text{NOT}(x)$, $\text{AND}(x, y)$, et $\text{OR}(x, y)$.

{% endexercice %}
{% details "corrigé" %}

Il y a 16 possibilités de fonctions :

x | y | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16  
--|---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----
0 | 0 | 0  | 1  | 0  | 0  | 0  | 1  | 1  | 1  | 1  | 0  | 1  | 1  | 1  | 0  | 0  | 0  
1 | 0 | 0  | 0  | 1  | 0  | 0  | 1  | 0  | 0  | 1  | 1  | 0  | 1  | 1  | 0  | 1  | 1  
0 | 1 | 0  | 0  | 0  | 1  | 0  | 0  | 1  | 0  | 1  | 1  | 1  | 0  | 1  | 1  | 0  | 1  
1 | 1 | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 1  | 1  | 1  | 1  | 1  | 0  | 1  | 1  | 0  

On a :

- la fonction $f_i = \overline{f_{i+8}}$ pour $1\leq i \leq 8$
- $f_1$ est la fonction constante valant 0
- $f_{2+8}(x, y)$ est la fonction $x \lor y$
- $f_{3}(x, y) = f_{4}(y, x)$ et $f_{3+8}$ est la fonction $\bar{x} \lor y$
- $f_{5}(x, y)$ est la fonction $x \land y$
- $f_{6}(x, y)$ est la fonction $\bar{y}$
- $f_{7 + 8}(x, y)$ est la fonction $x$
- $f_{8 + 8}(x, y)$ est la fonction $(x \land \bar{y}) \lor (\bar{x} \land y)$
{% enddetails %}

Vous savez quoi, on peut même faire mieux en utilisant la fonction $\text{NAND}(x, y)$.

{% note "**Définition**" %}

La fonction $\text{NAND}(x, y)$ est définie telle que :

<div>
$$
\text{NAND}(x, y) \coloneqq \overline{x \land y}
$$
</div>

{% endnote %}

On peut tout retrouver grâce à elle :

{% exercice %}
Montrer que toute fonction de $\\{0, 1\\}^2 \rightarrow \\{0, 1\\}$ peut s'écrire comme combinaison de la fonction $\text{NAND}(x, y)$.

{% endexercice %}
{% details "corrigé" %}

Il suffit de montrer que l'on peut reconstruire $\text{NOT}(x)$, $\text{AND}(x, y)$, $\text{OR}(x, y)$ et $\text{XOR}(x, y)$ avec $\text{NAND}(x, y)$ :

- $\text{NOT}(x) = \text{NAND}(x, x)$
- $\text{AND}(x, y) = \text{NOT}(\text{NAND}(x, y))$
- $\text{OR}(x, y) = \text{NAND}(\text{NOT}(x), \text{NOT}(y))$
- $\text{XOR}(x, y) = \text{NAND}(\text{NAND}(x, \text{NAND}( x, y )), \text{NAND}(x, \text{NAND}( x, y )))$ :

{% enddetails %}

Fun fact, cela fonctionne aussi avec une autre fonction  :

{% exercice %}
Montrer que l'on peut expliciter la fonction  $\text{NAND}(x, y)$ avec la fonction $\text{NOR}(x, y) \coloneqq \overline{x \lor y}$.
{% endexercice %}
{% details "corrigé" %}

- $\text{NOT}(x) = \text{NOR}(x, x)$
- $\text{NAND}(x, y) = \text{NOT}(\text{NOR}(x, y))$

{% enddetails %}

#### Généralisation

Commençons par résoudre l'exercice suivant

{% exercice %}
En utilisant sa table de vérité, montrez que toute fonction booléenne peut s'écrire sous une [forme normale disjonctive](https://fr.wikipedia.org/wiki/Forme_normale_disjonctive).
{% endexercice %}
{% details "corrigé" %}

Soit $f(x_1, \dots, x_n)$ une fonction de $\\{0, 1\\}^n$ dans $\\{0, 1\\}$.

À tout élément $y=(y_1, \dots, y_n)$ de $\\{0, 1\\}^n$ on peut associer la fonction $l^y(x) = l^y_1(x) \land \dots \land l^y_i(x) \land \dots \land l^y_n(x)$ où $l^y_i(x) = x_i$ si $y_i = 1$ et $l^y_i(x) = \overline{x_i}$ sinon pour tout $x=(x_1, \dots, x_n)$. La fonction $f$ est alors égale à :

<div>
$$
f(x) = \lor \{l^y(x) | f(y) = 1\} = \bigvee_{f(y) = 1} (l^y_1(x) \land \dots \land l^y_i(x) \land \dots \land l^y_n(x))
$$
</div>

{% enddetails %}

On peut utiliser l'exercice précédent pour montrer que l'on peut aussi écrire une fonction booléenne sous [une forme normale conjonctive, comme une formule SAT](../problème-SAT/){.interne}, sans utiliser d'artifice compliqué :

<span id="proposition-CNF-fonction"></span>

{% note "**Proposition**" %}
Toute fonction booléenne $f$ de $\\{0, 1\\}^n$ dans $\\{0, 1\\}$ peut s'écrire sous [forme normale conjonctive](https://fr.wikipedia.org/wiki/Forme_normale_conjonctive) avec autant de clauses que de vecteurs $(x_1, \dots, x_n)$ tel que $f(x_1, \dots, x_n) = 0$.
{% endnote %}
{% details "preuve", "open" %}

On utilise le fait que $\overline{a\land b} = \overline{a}\lor \overline{b}$ et que $\overline{a\lor b} = \overline{a}\land \overline{b}$ et on reprenant la fonction $l^y(x)$ définie dans le corrigé de l'exercice précédent. On a :

<div>
$$
f(x) = \overline{\bigvee_{f(y) = 0} (l^y_1(x) \land \dots \land l^y_i(x) \land \dots \land l^y_n(x))} = \bigwedge_{f(y) = 0} (\overline{l^y_1(x)} \lor \dots \lor \overline{l^y_i(x)} \lor \dots \lor \overline{l^y_n(x)})
$$
</div>

{% enddetails %}

Ce résultat s'étant aux fonctions booléennes vectorielles :

<span id="proposition-CNF-fonction-vect"></span>

{% note "**Proposition**" %}
Toute fonction booléenne vectorielle $f$ de $\\{0, 1\\}^n$ dans $\\{0, 1\\}^m$ peut s'écrire sous une forme normale conjonctive $f(x_1, \dots, x_n, y_1, \dots y_m)$ telle que $f(x_1, \dots, x_n, y_1, \dots y_m)$ est vraie si et seulement si $f(x_1, \dots, x_n) = (y_1, \dots y_m)$
{% endnote %}
{% details "preuve", "open" %}

La fonction booléenne vectorielle $f$ peut s'écrire comme $m$ fonction booléennes $f_i$ de de $\\{0, 1\\}^n$ dans $\\{0, 1\\}$ tel que f(x) = (f_1(x), \dots, f_m(x))$. En utilisant le théorème précédent, on a que :

<div>
$$
f_i(x) = \overline{\bigvee_{f_i(y) = 0} (l^y_1(x) \land \dots \land l^y_i(x) \land \dots \land l^y_n(x))} = \bigwedge_{f_i(y) = 0} (\overline{l^y_1(x)} \lor \dots \lor \overline{l^y_i(x)} \lor \dots \lor \overline{l^y_n(x)})
$$
</div>

La formule logique suivante est alors uniquement vraie si $f_i(x) = y_i$ :

<div>
$$
\begin{array}{lcl}
f_i(x, y_i) &=& (y_i \land (\bigwedge_{f_i(y) = 0} (\overline{l^y_1(x)} \lor \dots \lor \overline{l^y_i(x)} \lor \dots \lor \overline{l^y_n(x)})) ) \lor \overline{y_i} \\
& =& (y_i \lor \overline{y_i}) \land (\bigwedge_{f_i(y) = 0} (\overline{l^y_1(x)} \lor \dots \lor \overline{l^y_i(x)} \lor \dots \lor \overline{l^y_n(x)} \lor \overline{y_i}))\\
& =& \bigwedge_{f_i(y) = 0} (\overline{l^y_1(x)} \lor \dots \lor \overline{l^y_i(x)} \lor \dots \lor \overline{l^y_n(x)} \lor \overline{y_i})\\
\end{array}
$$
</div>

On en conclut que la conjonction de clauses suivante n'est vraie que si et seulement si $f(x) = y$ :

<div>
$$
f(x_1, \dots, x_n, y_1, \dots y_m) = \bigwedge_{1\leq i \leq m} f_i((x_1, \dots, x_n), y_i)
$$
</div>

{% enddetails %}

### Calculabilité des fonctions booléennes (vectorielles)

On peut conclure cette partie en montrant que toutes les fonctions booléennes vectorielles sont calculables :

{% note "**Proposition**" %}
Toute fonction booléenne est calculable en $\mathcal{O}(1)$ opérations avec un pseudo-code n'utilisant que la fonction $\text{NAND}$.
{% endnote %}
{% details "preuve", "open" %}

La taille de l'entrée d'une fonction booléenne est fixe. La taille de la forme normale disjonctive est de taille fixe et peut s'écrire uniquement avec la fonction $\text{NAND}$. Comme une forme normale disjonctive est clairement calculable, on en déduit bien que :

- une fonction booléenne est calculable
- on a besoin que de structures de contrôle et de la fonction $\text{NAND}$
- le nombre d'opérations est borné par le nombre d'opérations nécessaire pour calculer la forme normale disjonctive

{% enddetails %}
{% note "**Proposition**" %}
Toute fonction booléenne vectorielle est calculable en  $\mathcal{O}(1)$ par un pseudo-code n'utilisant que la fonction $\text{NAND}$.
{% endnote %}
{% details "preuve", "open" %}

> TBD ici composition avec projection = fct booléenne, donc calculable puis on refabrique un vecteur. Donner l'algorithme

La preuve est immédiate puisqu'une fonction booléenne vectorielle est la concaténation d'un nombre constant ($m$) de fonctions booléennes calculables en $\mathcal{O}(1)$ et n'utilisant que la fonction $\text{NAND}$.

{% enddetails %}

La preuve de la proposition précédente est lourde de conséquences. Ce qui fait qu'une fonction $f: \\{0, 1\\}^\star \rightarrow \\{0, 1\\}^\star$ ne peut pas être un algorithme est uniquement lié à la taille variable de l'entrée. Un algorithme ne peut calculer que celles ayant des régularités que l'on peut exploiter via des structures de contrôles (exécution conditionnelle et boucles pour un pseudo-code).

D'un point de vue d'un pseudo-code, on écrira ces fonctions en spécifiant la taille des tableau d'entrée :

```pseudocode
algorithme f(x: [bit: n]) → [bit: m]
```

Pour ne pas couper les cheveux en 4, on se permettra plusieurs abus de notations évident :

- `f(x_1: bit, ..., x_n: bit) → [bit]`{.language-} à la place de `f([bit: n]) → [bit]`{.language-},
- `f(x_1: [bit], ..., x_n: [bit]) → [bit]`{.language-} à la place de `f([bit]) → [bit] # n entrées de taille t_1 + ... + t_n`{.language-},

Cette notation nous permettra d'écrire facilement des fonctions :

- de plusieurs entrées de même taille: `f(x: [bit: n], y: [bit: n])`{.language-}
- d'entrée et sortie liées :`f(x: [bit: n]) → [bit: n + 3]`{.language-}

## Données booléennes

[On a vu](../bases-théoriques/définition/#paramètres-binaires){.interne} qu'un algorithme pouvait ne manipuler que des bits. On peut donc redéfinir la notion de pseudo-code ainsi :

{% note "**Proposition**" %}
On peut sans perte de généralité supposer qu'[un pseudo-code](../pseudo-code/briques-de-base/){.language-} ne peut manipuler que :

- des objets (uniquement) de type `bit`{.language-}
- des tableaux de type `[bit]`{.language-}
{% endnote %}

Pour un tableau de bit $x$, on appelle $x[0]$ le **_bit de poids faible_** de $x$ et $x[-1]$ le **_bit de poids fort_**. Attention, l'ordre de représentation des listes fait croître les indices de gauche à droite, alors que [la représentation binaire](https://fr.wikipedia.org/wiki/Syst%C3%A8me_binaire) va **de droite à gauche**. Par exemple le tableau $x = [1, 1, 1, 0, 0, 1, 1, 0]$ sera représenté par le nombre binaire 01100111, correspondant aux indice allant de droite à gauche :

```text
indice : 76543210
   x   : 01100111
```

Tout tableau de bit peut être interprété de nombreuses manière : entier, réel, caractère, etc :

{% attention "**À retenir**" %}
La signification d'une donnée est dépendante du contexte.
{% endattention %}

Pour éviter toute confusion entre les entiers on écrira :

- $[0, 1, 1]$ pour un tableau de bits
- $011 = 11$ pour l'entier 11 en base 10
- $0b011 = b11$ pour l'entier 3 écrit en [base 2](https://fr.wikipedia.org/wiki/Syst%C3%A8me_binaire)
- $0o744$ pour l'entier 484 écrit en base 8 ([base octale](https://fr.wikipedia.org/wiki/Syst%C3%A8me_octal))
- $0xBBAADD$ pour l'entier 12298973 écrit en base 16 ([base hexadécimal](https://fr.wikipedia.org/wiki/Syst%C3%A8me_hexad%C3%A9cimal))
- $\mathbb{1}_n$ comme étant un tableau de $n$ bits valant tous 1
- $\mathbb{0}_n$ comme étant un tableau de $n$ bits valant tous 0

### Booléen

{% note "**Définition**" %}

On note $b$ la bijection $b: \\{0, 1\\} \rightarrow \\{\text{Vrai}, \text{Faux}\\}$ telle que :

<div>
$$
\begin{cases}
b(0) = \text{Faux}\\
b(1) = \text{Vrai}\\
\end{cases}
$$
</div>
{% endnote %}

### Entiers

Un tableau de bit pourra être interprété de deux façons complémentaires :

- comme un entier naturel, on dira que le tableau/nombre est **_non signé_**
- comme un entier relatif (positif ou négatif) et on dira que le tableau/nombre est **_signé_**

#### Non signé

On utilise la représentation binaire classique :

{% note "**Définition**" %}

On note $u$ la bijection $u: \\{0, 1\\}^\star \rightarrow \mathbb{N}$ telle que :


<div>
$$
u([x_0, \dots, x_{n-1}]) = \sum_{i=0}^{n-1}x_i \cdot 2^i
$$
</div>


On note $u^{-1}(x)$ l'inverse de $u$ et $u^{-1}_n(x)$ le tableau y de $\\{0, 1\\}^n$ tel que $u(y) = x \bmod 2^n$
{% endnote %}

Ainsi :

- $u([0,1,0, 1]) = 10$ (de notation binaire $0b1010$),
- $u^{-1}(10) = [0,1,0, 1]$
- $u_3^{-1}(10) = [0,1,0]$ (de notation binaire $0b010$)
- $u_8^{-1}(10) = [0,1,0, 1, 0, 0, 0, 0]$ (de notation binaire $0b00001010$)

{% exercice %}
En utilisant [l'algorithme du successeur](../projet-algorithmes-classiques/compteur-binaire/){.interne}, créez un algorithme de signature `INC(x: [bit: n]) → [bit: n]`{.language-} tel que :

<div>
$$
u(\text{INC}(x)) = (u(x) + 1) \mathbin{\small\%} 2^n
$$
</div>

{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme INC(x: [bit]) → [bit]:
    y ← un tableau de bit de taille x.longueur
    y[:] ← x[:]

    i ← 0
    tant que (i < y.longueur) et (y[i] == 1):
        y[i] ← 0
        i ← i + 1

    si (i < y.longueur):
        y[i] ← 1
    
    rendre y
```

{% enddetails %}

#### Opposé

Pour gérer les nombres négatifs, on utilise [le complément à deux](https://fr.wikipedia.org/wiki/Compl%C3%A9ment_%C3%A0_deux), qui revient à  travailler modulo $2^n$.

Pour un tableau de bit $x$ on notera :

<div>
$$
-x \coloneqq \text{INC}(\overline{x})
$$
</div>

On choisit cette notion d'opposé à cause de la relation suivante :

{% note "**Proposition**" %}
pour tout tableau de bit $x$ de taille $n$ on a : 

<div>
$$
u(-x) = 2^n -u(x)
$$
</div>

{% endnote  %}
{% details "preuve", "open"  %}
On a $u(x) + u(\overline{x}) = u(\mathbb{1}_n) = 2^n-1$, donc $u(\overline{x}) + 1 = 2^n - u(x)$.

Or par définition de l'algorithme $\text{INC}$ on a également $(u(\overline{x}) + 1) = u(\text{INC}(\overline{x})) u(-x)$ ce qui conclut la preuve.

{% enddetails %}

La proposition précédente montre facilement que la définition est cohérente :

{% note "**Proposition**" %}
pour tout tableau de bit $x$ de taille $n$ on a :

<div>
$$
-(-x) = x
$$
</div>

{% endnote  %}
{% details "preuve", "open"  %}

On a $u(-(-x)) = 2^n -u(-x) = 2^n -(2^n -u(x)) = u(x)$. Comme $u$ est une bijection on a bien que $-(-x) = x$.
{% enddetails %}

On peut aussi lier l'opposé à $u_n^{-1}$ :

{% exercice %}
Montrez que pour tout $x \in [-2^{n-1}\mathrel{\{.\}\\,\{.\}} 2^{n-1}-1]$, on a :

<div>
$$
u^{-1}_n(2^n + x) =-u^{-1}_n(2^n -x)
$$
</div>

{% endexercice %}
{% details "corrigé" %}

Comme $u(-x) = -u(x) \bmod 2^n$, on a $u^{-1}(x) = -u^{-1}(2^n -x)$. De là :

- si $x\geq 0$ on a $u^{-1}_n(2^n + x) = u^{-1}(x) = -u^{-1}(2^n -x)$
- si $x < 0$ on a $u^{-1}_n(2^n + x) = -u^{-1}(-x) = -u_n^{-1}(2^n-x)$

{% enddetails %}

Enfin, tout ceci se calcule très vite :

{% attention "**À retenir**" %}
Calculer l'opposé d'un tableau de bit se fait en temps linéaire uniquement avec une boucle `tant que`{.language-} et la fonction booléenne sur 1 bit `NAND`.
{% endattention %}

#### Signé

On a tout en notre possession pour associer des entiers relatifs aux tableaux de bit :

{% note "**Définition**" %}

On note $i_n: \\{0, 1\\}^n \rightarrow  [-2^{n-1}\mathrel{\{.\}\\,\{.\}} 2^{n-1}-1]$ la bijection telle que :

<div>
$$
i_n(x) = 
\begin{cases}
u_{n-1}(x)\text{ si } x[-1] == 0\\
-u_{n-1}(-x) \text{ si } x[-1] == 1\\
\end{cases}
$$
</div>

{% endnote %}

Il est clair que $i_n$ est une bijection puisque $u_{n-1}$ en est une de $\\{0, 1\\}^{n-1}$ dans $[0 \mathrel{\{.\}\\,\{.\}} 2^{n-1}-1]$. Le bit de poids fort des tableaux de bits est appelé **_bit de signe_** car $i_n(x) < 0$ s'il vaut 1. Elle est de plus compatible avec notre négation :

{% note "**Proposition**" %}

Pour tout tableau de bit $x$ de taille $n$ on a $i_n(-x) = -i_n(x)$.

{% endnote %}
{% details "preuve", "open"  %}

- si $x[-1] == 0$, $i_n(-x) = -u_{n-1}(-(-x)) = -u_{n-1}(x) = -i_n(x)$
- si $x[-1] == 1$, $i_n(-x) = u_{n-1}(-x) = -i_n(x)$

{% enddetails %}

Il est crucial de retenir que cette notation dépend du nombre de bits de la représentation de l'entier. Ainsi :

- $i^{-1}_2(1) = [1, 0]$ (de représentation binaire $0b01$)
- $i^{-1}_4(1) = [1, 0, 0, 0]$ (de représentation binaire $0b0001$)
- $i^{-1}_2(-1) = [1, 1]$
- $i^{-1}_4(-1) = [1, 1, 1, 1]$

Remarquez deux choses :

- Un même tableau de bit dont le bit de poids fort vaut 1 peut être vu comme un entier positif ou négatif
- il ne suffit pas de changer le bit de signe pour avoir l'opposé d'un nombre.

{% note "**Définition**" %}

Un tableau de bit considéré comme :

- un entier positif est dit **_non signé_**
- un entier relatif est dit **_signé_**

Le bit de poids fort d'un tableau signé est appelé **_bit de signe_** (il ne vaut `1` `que si l'entier représenté est négatif).
{% endnote %}

### Réels

Les approximation de nombres réels sont encodées sur 64 bits.

{% lien %}
[Format IEEE 744 double précision](https://fr.wikipedia.org/wiki/IEEE_754#Format_double_pr%C3%A9cision_(64_bits))
{% endlien %}

Nous ne parlerons pas plus de cet encodage ici, l'algorithmie ne s'intéressant que très peu aux nombres réels, mais certains algorithmes de magie noir sur l'utilisation astucieuse de ce format existent :

{% lien %}
<https://fr.wikipedia.org/wiki/Racine_carr%C3%A9e_inverse_rapide> (voir aussi : <https://www.youtube.com/watch?v=Fm0vygzVXeE>)
{% endlien %}

> TBD montrer que r(x) < r(y) si u(x) < u(y) ce qui règle plein de problèmes.

### Chaînes de caractères

Format UNICODE sur 21 bits permet d'encoder jusqu'à $2^{21} = 2097152$ informations. Actuellement seuls 154998 sont assignés, UNICODE appelle ces informations **_glyphes_**, permettant d'encoder plus de 150 langues :

{% lien %}
[Format UNICODE](https://fr.wikipedia.org/wiki/Unicode)
{% endlien %}

Ne confondez pas la correspondance entre une glyphe (en gros un caractère) et un nombre qui est le format UNICODE et son implémentation informatique qui utilise la conversion [UTF-8](https://fr.wikipedia.org/wiki/UTF-8) qui permet d'écrire ces nombres sur un format allant de 8 à 32 bits.


## Opérations

Cette partie montre que toutes les opérations nécessaires pour faire un pseudo-code peuvent être faite avec des fonction booléennes vectorielles (donc uniquement des fonctions `NAND`) alliées à des structures de contrôles (tests et boucles `tant que`).


> TBD rappeler ce que doit savoir faire un pseudo-code

### Décalage de bits

Quelques opérations utiles lorsque l'on manipule des tableaux de bits comme des entiers non signés.

#### Concaténation

On utilise la concaténation lorsque l'on veut écrire des entiers plus gros. On utilise un opérateur particulier car ce n'est pas la concaténation de listes habituelle. En effet si on veut concaténer le nombre $x = 0b110$ avec le nombre $y = 0b001$ pour former le nombre $x || y = 0b11001$, on ne peut pas juste concaténer le tableau $X = [0, 1, 1]$ qui représente $x$ au tableau $Y = [1, 0, 0]$ qui représente $y$, il faut faire le contraire ($Y + X$). Explicitons le :

```pseudocode
algorithme CONCAT(x: [bit], y: [bit])  → [bit]:
    z ← un tableau de bit de taille x.longueur + y.longueur

    pour chaque i de [0 .. y.longueur[:
        z[i] ← y[i]
    
    pour chaque i de [0 .. x.longueur[:
        z[i + y.longueur] ← x[i]
    
    rendre z
```

La **concaténation** des $n$ bits de $x$ aux $n'$ bits de $y$.

<div>
$$
x || y \coloneqq \text{CONCAT}(x, y)
$$
</div>

#### Shift

On décale les bits vers la gauche ou la droite selon la représentation binaire sans changer le nombre total de bit (les bit qui arrivent sont à 0) :

- $x << k$ : ***shift*** de $k$ bit vers la gauche. Les $k$ bits de poids faibles sont des $0$ (identique à une multiplication par $2^k$)
- $x >> k$ : ***shift*** de $k$ bit vers la droite. Les $k$ bits de poids forts sont des $0$ (identique à une division entière par $2^k$)

Ainsi : $0b1101 << 3 = 0b1000$ et $0b1101 >> 2 = 0b0011$

Formellement :

<div>
$$
\begin{array}{lcl}
x << k &\coloneqq &\text{LSHIFT}(x, k)\\
x >> k &\coloneqq &\text{RSHIFT}(x, k)
\end{array}
$$
</div>

Avec :

```pseudocode
algorithme LSHIFT(x: [bit], k: entier)  → [bit]:
    z ← un tableau de bit de taille x.longueur

    z[:k] ← 0
    pour chaque i de [k .. x.longueur - k[:
        z[i] ← x[i - k]
    
    rendre z

algorithme RSHIFT(x: [bit], k: entier)  → [bit]:
    z ← un tableau de bit de taille x.longueur

    z[-k:] ← 0
    pour chaque i de [0 .. k[:
        z[i] ← x[i + k]
    
    rendre z
```

Notez que nous nous sommes autorisé l'abus de notation en utilisant des paramètres entiers. En toute logique l'algorithme `LSHIFT`{.language-} devrait être :

```pseudocode
algorithme LSHIFT(x: [bit], k: [bit])  → [bit]:
    z ← un tableau de bit de taille x.longueur

    z[:u(k)] ← 0
    pour chaque i de [u(k) .. x.longueur - k[:
        z[i] ← x[i - u(k)]
    
    rendre z
```

Cela alourdi cependant les notations sans gain de généralité.

#### rotation

- $x <<< k$  : ***rotation*** de $k$ bit vers la gauche.
- $x >>> k$  : ***rotation*** de $k$ bit vers la droite.

Ainsi : $0b1101 <<< 3 = 0b1110$ et $0b1101 >>> 2 = 0b0111$

Formellement :

<div>
$$
\begin{array}{lcl}
x << k &\coloneqq &\text{LROT}(x, k)\\
x >> k &\coloneqq &\text{RROT}(x, k)
\end{array}
$$
</div>

{% exercice %}
Donnez un algorithme linéaire pour calculer la rotation. Il devra être de signature : `LROT(x: [bit], k: entier)  → [bit]`{.language-}
{% endexercice %}
{% details "corrigé" %}

> TBD simple.

On aurait aussi pu utiliser [l'exercice sur les permutations circulaires](../projet-algorithmes-classiques/chaine-caracteres/#permutation-circulaire){.interne} si on avait voulu faire un algorithme in place
{% enddetails  %}

### Logiques

Les opérations logiques définies précédemment s'étendent naturellement aux données sous la forme de tableaux de bits. 

Il suffit de montrer la fonction `NAND` :

```pseudocode
algorithme NAND(x: [bit: n], y: [bit: n]) → [bit: n]
    z ← tableau de bit de taille x.longueur

    pour chaque i de [0 .. x.longueur[:
        z[i] ← NAND(x[i], y[i])
    rendre z
```

Puis de mimer ce que l'on a fait avec les fonction sur 1 bit, par exemple `NOT(x: [bit]) → [bit] := NAND(x, x)`{.language-}. Remarquez que cette fonction n'est **pas** une fonction booléenne vectorielle, mais bien un algorithme : ses entrées ne sont pas de taille fixe.

{% exercice %}
Écrivez un algorithme linéaire permettant de réaliser l'opération OR sur un tableau de bit de taille quelconque. Il sera de signature : `OR(x: [bit: n], y: [bit: n]) → [bit: n]`{.language-}
{% endexercice %}
{% details "corrigé" %}

On peut utiliser `NAND` puisque $\overline{x} = \overline{x \land x}$ :

```pseudocode
OR(x: [bit], y: [bit]) → [bit] := NAND(NOT(x), NOT(y))
```

{% enddetails %}

En définissant de même les algorithmes : 

- `AND(x: [bit: n], y: [bit: n]) → [bit: n]`{.language-}
- `OR(x: [bit: n], y: [bit: n]) → [bit: n]`{.language-}
- `XOR(x: [bit: n], y: [bit: n]) → [bit: n]`{.language-}

On peut définir les opérations linéaires **pour des tableaux de même taille** :

<div>
$$
\begin{array}{lcl}
\overline{x} &\coloneqq& \text{NOT}(x, x)\\
x \land y &\coloneqq& \text{AND}(x, y)\\
x \lor y  &\coloneqq& \text{OR}(x, x)\\
x \oplus y  &\coloneqq& \text{XOR}(x, x)\\
\end{array}
$$
</div>

Qui permettent de travailler sur des tableaux de bits. On va voir que ces fonctions suffisent à décrire tous les pseudo-codes.

### Tests

```pseudocode
algorithme ZERO(x: [bit]) → bit
    pour chaque i de [0 .. x.longueur[:
        si AND(x[i], 1):  # x[i] == 1
            rendre 0
    
    rendre 1

algorithme GRAND(x: [bit: n], y: [bit: n])
                → bit
    pour chaque i de [1 .. x.longueur]:
        si XOR(x[-i], y[-i]):  # x[i] != y[i]
            rendre x[-i]
    
    rendre 0

```

<div>
$$
\begin{array}{lcl}
x \neq 0 &\coloneqq& \text{ZERO}(x)\\
x == y &\coloneqq& \text{ZERO}(x - y)\\
x > y &\coloneqq& \text{GRAND}(x, y)\
x < y &\coloneqq& y < x\\
x \leq y &\coloneqq& (x == y) \lor (x < y)\\
x \geq y &\coloneqq& (y \leq x)\\
\end{array}
$$
</div>

### Arithmétique

Nous allons donner ici les complexité par rapport à la taille des entrées, c'est à dire des tableaux de bits correspondant à des entiers.

#### Somme

Sur deux entiers non signés

```
  100101
+ 001011
--------
  110001
```

Attention à la retenue :

```
  100101
+ 011011
--------
 1000000
```

L'algorithme est alors le suivant (on en a déjà vu une version lorsque l'[on a étudié les problèmes NP](../problèmes-NP/#algorithme-somme_binaire), ici on va le considéré modulo la taille des entrées) c'est à dire que l'addition de $0b100101$ et $0b011011$ donnera : $0b000000$. On utilise aussi les fonctions booléennes à 1 bit définies précédemment pour un résultat compact :

```pseudocode
algorithme somme(x: [bit: n], y: [bit: n]) → [bit: n]
    
    z ← tableau de bit de taille x.longueur
    r ← 0

    pour chaque i de [0 .. x.longueur[:
        z[i]  ← XOR(XOR(r, x[i]), y[i])
        r ← OR(AND(r, x[i]), 
               AND(OR(r, x[i]), 
                   y[i]))
    rendre z
```

Sa complexité est bien linéaire puisque les fonction utilisées sont toutes de complexité $\mathcal{O}(1)$.

Terminons cette partie en montrant que l'on peut récrire cet algorithme uniquement avec des fonctions `NAND` sans changer sa complexité. Pour cela commençons par ne mettre qu'une seule instruction par ligne :

```pseudocode
algorithme somme'(x: [bit: n], y: [bit: n]) → [bit: n]
    
    z ← tableau de bit de taille x.longueur
    r ← 0

    pour chaque i de [0 .. x.longueur[:
        a ← r
        b ← x[i]
        c ← XOR(a, b)
        
        a ← c
        b ← x[i]
        c ← XOR(a, b)
        
        z[i]  ← c

        a ← r
        b ← x[i]
        c ← OR(a, b)
        
        a ← c
        b ← y[i]
        c ← AND(a, b)

        a ← r
        b ← b[i]
        d ← AND(a, b)

        a ← c
        b ← d
        c ← OR(a, b)

        r  ← c

    rendre z
```

Puis à remplacer les fonctions logiques par leur pendant avec `NAND` pour définir notre algorithme `PLUS`{.language-}:

```pseudocode
algorithme PLUS(x: [bit: n], y: [bit: n]) → [bit: n]
    
    z ← tableau de bit de taille x.longueur
    r ← 0

    pour chaque i de [0 .. x.longueur[:
        a ← r
        b ← x[i]
        c ← NAND(NAND(a, NAND(a, b)), NAND(a, NAND(a, b)))
        
        a ← c
        b ← x[i]
        c ← NAND(NAND(a, NAND(a, b)), NAND(a, NAND(a, b)))
        
        z[i]  ← c

        a ← r
        b ← x[i]
        c ← NAND(NAND(a, a), NAND(b, b))
        
        a ← c
        b ← y[i]
        c ← NAND(NAND(a, b), NAND(a, b))

        a ← r
        b ← b[i]
        d ← NAND(NAND(a, b), NAND(a, b))

        a ← c
        b ← d
        c ← NAND(NAND(a, a), NAND(b, b))

        r  ← c

    rendre z
```

{% attention "**À retenir**" %}
Calculer la somme de deux tableaux de bit se fait en temps linéaire uniquement avec une boucle `tant que`{.language-} et la fonction booléenne sur 1 bit `NAND`.
{% endattention %}

On peut définir les opérations linéaires **pour des tableaux de même taille** :

<div>
$$
x + y \coloneqq \text{PLUS}(x, y)\\
$$
</div>

Cette addition fonctionne pour 2 (tableaux représentant des) entiers non signés.



#### Soustraction

L'utilisation du complément à deux permet 
somme de deux entiers signés

<div>
$$
x-y \coloneqq x + (-y)
$$
</div>

Cette définition est cohérente puisque $(x + 2^n - y) \bmod 2^n = x -  y \bmod 2^n$. L'utilisation du complément à 2 est donc extrêmement astucieuse et permet d'éviter tout un tas de cas particulier que l'on se trimbale [si l'on utilise uniquement un bit de signe](https://fr.wikipedia.org/wiki/Compl%C3%A9ment_%C3%A0_deux#Probl%C3%A8me_de_la_repr%C3%A9sentation_na%C3%AFve).

{% attention "**À retenir**" %}
Calculer la soustraction de deux tableaux de bit se fait en temps linéaire uniquement avec une boucle `tant que`{.language-} et la fonction booléenne sur 1 bit `NAND`.
{% endattention %}

#### Multiplication

On utilise la [multiplication posée](https://fr.wikipedia.org/wiki/Multiplication#Techniques_de_multiplication). Les nombres binaires simplifient grandement le calcul car il suffit de faire des additions.

```
       100101
     * 001011
    ---------
       100101  = 100101 * 1
      100101   = 100101 * 1
     000000    = 100101 * 0
    100101     = 100101 * 1    
   000000      = 100101 * 0      
+ 000000       = 100101 * 0
------------
  00110010111
```

On trouve que $0b100101 \cdot 0b1011 = 0b110010111$ ($37 \cot 11 = 407$).

Tout comme pour l'addition, nous allons donner ici une version modulo $2^n$ (sans perte de généralité, il suffit d'ajouter des 0 au tableau de bit) :


```
    100101
 *  001011
---------
    100101
    00101
    0000   
    101
    00
+   0 
--------
    10111
```

On obtient l'algorithme suivant :

```pseudocode
algorithme FOIS(x: [bit: n], y: [bit: n]) → [bit: n]
    
    z ← tableau de bit de taille x.longueur
    z[:] ← 0

    pour chaque k de [0 .. x.longueur[:
        r ← 0
        pour chaque i de [k .. x.longueur[:
            a ← AND(y[k], x[i])
            z[i]  ← XOR(XOR(r, a), z[i])
            r ← OR(AND(r,a), 
                   AND(OR(r, a), 
                          z[i]))
    rendre z
```

La complexité de l'algorithme est en $\mathcal(O)(n^2)$ et on a :

{% attention "**À retenir**" %}
Calculer le produit de deux tableaux de bit se fait en temps quadratique uniquement avec deux boucles `pour chaque`{.language-} et la fonction booléenne sur 1 bit `NAND`.
{% endattention %}
{% info %}
Les meilleurs algorithmes connus pour effectuer la multiplication sont en $\mathcal(O)(n\log(n))$ mais ne sont presque jamais implémenté car leurs valeurs ajoutées est asymptotique et est atteinte pour des nombres trop grand par rapport aux nombres utilisés.
{% endinfo %}

#### Division euclidienne

On utilise la [division posée](https://fr.wikipedia.org/wiki/Division_pos%C3%A9e). Les nombres binaires simplifient grandement le calcul car il suffit de faire des soustractions.

La complexité de l'algorithme est en $\mathcal(O)(n^2)$.

```
  100101 | 001011
  -------|-----  
         | 000011
  1      | ^  
  10     |  ^
  100    |   ^ 
  1001   |    ^
  10010  |     
 - 1011  |     ^
 ------  |     |
    111  |     | 
    1111 |     | 
  - 1011 |      ^
  ------ |      |
    0100 |      | 
```

On trouve que : $0b100101 / 0b1011 = 0b11$ et $0b100101 \bmod 0b1011 = 100$

$37 / 11 = 3$ et $37 \bmod 11 = 4$

Ci après une version non signée :

```pseudocode

algorithme FOIS(x: [bit: n], y: [bit: n]) → ([bit: n], [bit: n]) 

    q ← tableau de bit de taille x.longueur
    q[:] ← 0

    r ← tableau de bit de taille x.longueur
    r[:] ← 0

    pour chaque k de [1 .. x.longueur]:
            q ← q << 1
            q[0] ← x[-k]

            r ← r << 1
            si u(q) ≥ u(y):
                q ← q - y
                r[0] ← 1
            sinon:
                r[0] ← 0

    rendre (q, r)
```

{% attention "**À retenir**" %}
Calculer la division euclidienne de deux tableaux de bit se fait en temps quadratique uniquement avec deux boucles `pour chaque`{.language-} (il y a une soustraction et un test pour chaque itération de la boucle) et la fonction booléenne sur 1 bit `NAND`.
{% endattention %}


#### pgcd

[On a déjà vu cet algorithme](../projet-algorithmes-classiques/pgcd/#algorithme-pgcd-binaire){.language-}, mais de façon récursive.

{% exercice %}
Écrivez l'algorithme du pgcd binaire de façon itérative. Il devra être de signature : `PGCD(x: [bit: n], y: [bit: n]) → [bit: n]`{.language-}.
{% endexercice %}
{% details "corrigé" %}

Remarquez que diviser par 2 est égal à un shift de 1 vers la droite.
```pseudocode

algorithme PGCD(x: [bit: n], y: [bit: n]) → [bit: n]

    p tableau de bit de taille x.longueur
    p[:] ← 0
    p[0] ← 1
    tant que y ≠ 0:
        si AND(x[0], y[0]):             # x et y sont pairs
            x ← x >> 1
            y ← y >> 1
            p ← p << 1
        sinon si AND(NOT(x[0]), y[0]):  # x impair et y pair
            y ← y >> 1
        sinon si AND(x[0], NOT(y[0])):  # x pair et y impair
            x ← x >> 1
        sinon:                          # x et y sont impairs
            si x < y:
                x, y ← y, x
            x ← x - y
    rendre x * p
```

{% enddetails %}


Cet algorithme est très efficace pour les nombres binaires puisque la division par deux est un shift de 1 bit vers la droite :

{% attention "**À retenir**" %}
Calculer le pgcd de deux tableaux de bit se fait en temps quadratique.
{% endattention %}

## Pseudo-code

Ceci nous permettra _in fine_ de redéfinir la notion de pseudo-code avec des objets et et des opérations bien plus simple sans perte de généralité.

### Variables interne binaires

Si données sont toutes des tableaux de bits, nos algorithmes utilisent encore des entiers pour les variables internes des boucles `pour chaque`{.language-}. C'est un abus de notation est on peut tout à fait s'en passer, considérer par exemple l'algorithme `NAND`{.language-} suivant :

```pseudocode
algorithme NAND(x: [bit: n], y: [bit: n]) → [bit: n]
    z ← tableau de bit de taille x.longueur

    i ← tableau de bit de taille log(x.longueur)  # la même taille que pour stocker l'entier x.longueur
    i[:] ← 0
    tant que i ≠ x.longueur:
        z[i] ← NAND(x[i], y[i])
        i ← i + 1
    rendre z
```

La différence est que l'on utilise maintenant les opérations que l'on a défini pour les tableaux de bit ! Il n'y a plus d'entier, même dans les variables internes.


{% note "**Proposition**" %}
Un pseudo-code utilisant uniquement des variables de type bit ou [bit] a la même expressivité que le pseudo-code utilisant [les types basiques](../pseudo-code/briques-de-base/#objets-basiquess){.interne}.
{% endnote %}

### Opérations autorisées

On voit que [toutes les opérations autorisées pour un pseudo-code](../pseudo-code/briques-de-base/#objets-basiquess){.interne} peuvent être créées uniquement avec des fonctions booléennes vectorielles et des instructions de contrôles (test et boucles). On peut même se restreindre à l'opération logique `NAND`{.language-} :

{% note "**Proposition**" %}
Un pseudo-code utilisant uniquement :

- variables :
  - binaires ou des tableaux binaires
  - les seules affectations autorisées sont les bits `x[i] ← y[j]`{.language-} avec $i$ étant un entier possiblement issu d'une évaluation $u(z)$
- opérations : les fonctions booléennes vectorielles
- instruction de contrôle `si x: ...bloc...`{.language-} où `x` est une variable binaire. Le bloc n'est exécuté que si `x = 1`{.language-}
- répétition : `tant que x: ...bloc...`{.language-} où `x` est une variable binaire. Le bloc n'est exécuté que tant que `x = 1`{.language-}.
 
A la même expressivité que [le pseudo-code classique](../pseudo-code/){.interne}.
{% endnote %}

> TBD l'opération logique `NAND`{.language-} suffit.