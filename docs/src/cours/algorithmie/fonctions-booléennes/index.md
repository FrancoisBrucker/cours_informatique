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

Et une **_fonction booléenne vectorielle_** est une fonction booléenne qui rend un vecteur :

<div>
$$
f: \{0, 1\}^n \rightarrow \{0, 1\}^m
$$
</div>

{% endnote %}

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
 x | y | x OR y     |  x AND y    |  x XOR y    |
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
x \oplus y = (x \lor y) \land \neg(x \land y)
$$
</div>

{% exercice %}
Démontrez que la formule précédente est bien correcte.
{% endexercice %}
{% details "corrigé" %}
On le fait avec une table :


 x | y | $x \lor y$ | $\neg(x \land y)$ |$x \oplus y$ |
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
x \text{NAND} y = \neg(x \land y)
$$
</div>

{% endnote %}

On peut tout retrouver grâce à elle :

{% exercice %}
Montrer que toute fonction de $\\{0, 1\\}^2 \rightarrow \\{0, 1\\}$ peut s'écrire comme combinaison de la fonction $\text{NAND}(x, y)$.

{% endexercice %}
{% details "corrigé" %}

Il nous suffit de montrer que l'on peut reconstruire $\text{NOT}(x)$, $\text{AND}(x, y)$, et $\text{OR}(x, y)$ avec $\text{NAND}(x, y)$ :

- $\text{NOT}(x) = \text{NAND}(x, x)$
- $\text{AND}(x, y) = \text{NOT}(\text{NAND}(x, y))$
- $\text{OR}(x, y) = \text{NAND}(\text{NOT}(x), \text{NOT}(y))$

{% enddetails %}
{% info %}
Cela marche aussi avec le [OU exclusif](https://fr.wikipedia.org/wiki/Fonction_OU_exclusif) ($\text{XOR}(x, y) = \text{AND}(\text{OR}(x, y), \text{NAND}(x, y))$).
{% endinfo %}

#### Généralisation

Commençons par montrer la proposition suivante :

{% note "**Proposition**" %}
Toute fonction booléenne peut s'écrire sous une [forme normale disjonctive](https://fr.wikipedia.org/wiki/Forme_normale_disjonctive)
{% endnote %}
{% details "preuve", "open" %}

Soit $f(x_1, \dots, x_n)$ une fonction de $\\{0, 1\\}^n$ dans $\\{0, 1\\}$.

À tout élément $x=(x_1, \dots, x_n)$ de $\\{0, 1\\}^n$ on peut associer la fonction $l^x(y_1, \dots, y_n) = l^x_1 \land \dots \land l^x_i \land \dots \land l^x_n$ où $l^x_i = y_i$ si $x_i = 1$ et $l^x_i = \overline{y_i}$ sinon. La fonction $f$ est alors égale à :

<div>
$$
f(x) = \lor \{l^y(x) | f(y) = 1\}
$$
</div>

{% enddetails %}

La proposition suivante étant le résultat aux fonctions booléennes vectorielles

{% note "**Proposition**" %}
Toute fonction booléenne vectorielle de $\\{0, 1\\}^n$ dans $\\{0, 1\\}^m$ peut s'écrire comme un tuple de $m$ [formes normales disjonctives](https://fr.wikipedia.org/wiki/Forme_normale_disjonctive)
{% endnote %}
{% details "preuve", "open" %}

Soit $f(x_1, \dots, x_n)$ une fonction de $\\{0, 1\\}^n$ dans $\\{0, 1\\}^m$. On peut écrire cette fonction comme la combinaison de $m$ fonctions booléennes $f_i(x_1, \dots, x_n)$ telles que $f(x_1, \dots, x_n) = (f_1(x_1, \dots, x_n), \dots, f_m(x_1, \dots, x_n))$ et utiliser la proposition précédente sur les $m$ fonctions booléennes.

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

La preuve est immédiate puisqu'une fonction booléenne vectorielle est la concaténation d'un nombre constant ($m$) de fonctions booléennes calculables en $\mathcal{O}(1)$ et n'utilisant que la fonction $\text{NAND}$.

{% enddetails %}

La preuve de la proposition précédente est lourde de conséquences. Ce qui fait qu'une fonction $f: \\{0, 1\\}^\star \rightarrow \\{0, 1\\}^\star$ ne peut pas être un algorithme est uniquement lié à la taille variable de l'entrée. Un algorithme ne peut calculer que celles ayant des régularités que l'on peut exploiter via des structures de contrôles (exécution conditionnelle et boucles pour un pseudo-code).

D'un point de vue d'un pseudo-code, on écrira ces fonctions en spécifiant la taille des tableau d'entrée et de sortie en commentaire :

```pseudocode
algorithme f(x: [bit])  # taille n
           → [bit]      # taille m
```

Ou encore en indiçant les tableaux lorsque le type est clair :

```pseudocode
algorithme f(x_1, ..., x_n) → (y_1, ..., y_m)
```
ou encore :

```pseudocode
algorithme f([x_0, ..., x_n-1]) → [y_0, ..., y_m-1]
```

## Données booléennes

[On a vu](../bases-théoriques/définition/#paramètres-binaires){.interne} qu'un algorithme pouvait ne manipuler que des bits. On peut donc redéfinir la notion de pseudo-code ainsi :

{% note "**Proposition**" %}
On peut sans perte de généralité supposer qu'[un pseudo-code](../pseudo-code/briques-de-base/){.language-} ne peut manipuler que :

- des objets (uniquement) de type `bit`{.language-}
- des tableaux de type `[bit]`{.language-}
{% endnote %}

Pour un tableau de bit $x$, on appelle $x[0]$ le **_bit de poids faible_** de $x$ et $x[-1]$ le **_bit de poids faible_**. On a coutume de représenter le tableau **de droite à gauche** pour respecter l'ordre de [la représentation binaire](https://fr.wikipedia.org/wiki/Syst%C3%A8me_binaire) d'un nombre. Par exemple le tableau $x = [1, 1, 1, 0, 0, 1, 1, 0]$ sera représenté par le nombre binaire 01100111, correspondant aux indice allant de droite à gauche :

```text
indice : 76543210
   x   : 01100111
```

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

On utilise la représentation binaire classique :

{% note "**Définition**" %}

On note $u$ la bijection $u: \\{0, 1\\}^\star \rightarrow \mathbb{N}$ telle que :


<div>
$$
u([x_0, \dots, x_{n-1}]) = \sum_{i=0}^{n-1}x_i \cdot 2^i
$$
</div>

On note $u^{-1}(x)$ l'inverse de $u$ et $u^{-1}_n(x)$ le tableau y de $\\{0, 1\\}^n$ tel que $u(y) = x \mathbin{\small\\%} 2^n$
{% endnote %}

Ainsi, si $x=[0,1,0, 1]$ :

- $u(x) = 10$ (de notation binaire 1010),
- $u^{-1}(10) = [0,1,0, 1]$
- $u_3^{-1}(10) = [0,1,0]$
- $u_8^{-1}(10) = [0,1,0, 1, 0, 0, 0, 0]$


Pour gérer les nombres négatifs, on utilise [le complément à deux](https://fr.wikipedia.org/wiki/Compl%C3%A9ment_%C3%A0_deux) défini telle que :

{% note "**Définition**" %}

On note $i^{-1}_n: [-2^{n-1}\mathrel{\{.\}\\,\{.\}} 2^{n-1}-1] \rightarrow \\{0, 1\\}^n$ la bijection telle que :


<div>
$$
i^{-1}_n(x) = 
\begin{cases}
u^{-1}_n(x)\text{ si } x \geq 0\\
u^{-1}_n(2^n + x)\text{ si } x < 0\\
\end{cases}
$$
</div>

{% endnote %}

On verra l'intérêt du complément à deux lorsque l'on donnera les algorithmes d'arithmétique sur les [bit], pour l'instant retenez que cette notation dépend du nombre de bits de la représentation de l'entier. Ainsi :

- $i^{-1}_2(1) = [1, 0]$ (de représentation binaire 01)
- $i^{-1}_4(1) = [1, 0, 0, 0]$ (de représentation binaire 0001)
- $i^{-1}_2(-1) = [1, 1]$
- $i^{-1}_4(-1) = [1, 1, 1, 1]$


### Réels

Les approximation de nombres réels sont encodées sur 64 bits.

{% lien %}
[Format IEEE 744 double précision](https://fr.wikipedia.org/wiki/IEEE_754#Format_double_pr%C3%A9cision_(64_bits))
{% endlien %}

Nous ne parlerons pas plus de cet encodage ici, l'algorithmie ne s'intéressant que très peu aux nombres réels, mais certains algorithmes de magie noir sur l'utilisation astucieuse de ce format existent :

{% lien %}
<https://fr.wikipedia.org/wiki/Racine_carr%C3%A9e_inverse_rapide> (voir aussi : <https://www.youtube.com/watch?v=Fm0vygzVXeE>)
{% endlien %}

### Chaînes de caractères

Format UNICODE sur 21 bits permet d'encoder jusqu'à $2^{21} = 2097152$ informations. Actuellement seuls 154998 sont assignés, UNICODE appelle ces informations **_glyphes_**, permettant d'encoder plus de 150 langues :

{% lien %}
[Format UNICODE](https://fr.wikipedia.org/wiki/Unicode)
{% endlien %}

Ne confondez pas la correspondance entre une glyphe (en gros un caractère) et un nombre qui est le format UNICODE et son implémentation informatique qui utilise la conversion [UTF-8](https://fr.wikipedia.org/wiki/UTF-8) qui permet d'écrire ces nombres sur un format allant de 8 à 32 bits.

## Logique

> TBD le mettre avec des formules logiques. 
> TBD généraliser NOT AND etc pour les [bit]
> Rappeler ce que l'on a fait avec SAT.

### Opérateurs

Les opérateurs sont à la base dédiés aux éléments binaire, mais ils s'étendent bit à bit aux vecteurs.

- XOR : ou exclusif binaire, se note $\oplus$ :
  - $0 \oplus 1 = 1 \oplus 0 \coloneqq 1$
  - $0 \oplus 0 = 1 \oplus 1 \coloneqq 0$
- NON : se note $\bar{x}$ :
  - $\bar{0} \coloneqq 1$
  - $\bar{1} \coloneqq 0$
- OR : ou binaire, se note $x \vee y$
  - $0 \vee 1 = 1 \vee 0 = 1 \vee 1 \coloneqq 1$
  - $0 \vee 0 \coloneqq 0$
- AND : : et binaire, se note $x \land y$
  - $1 \vee 1 \coloneqq 1$
  - $0 \vee 1 = 1 \vee 0 = 0 \vee 0 \coloneqq 0$
  
### Décalages de bits

On utilise deux direction de décalage (gauche et droite) et deux types de décalage selon que les bit poussés à l'extérieur sont réinjectés de l'autre côté ou disparaissent (les bit qui arrivent sont à 0).

- $x << k$ : ***shift*** de $k$ bit vers la gauche. Les $k$ bits de poids faibles sont des $0$ (identique à une multiplication par $2^k$)
- $x >> k$ : ***shift*** de $k$ bit vers la droite. Les $k$ bits de poids forts sont des $0$ (identique à une division par $2^k$)
- $x <<< k$  : ***rotation*** de $k$ bit vers la gauche.
- $x >>> k$  : ***rotation*** de $k$ bit vers la droite.

### Concaténation

$ x || y$ est la concaténation des $n$ bits de $x$ aux $n'$ bits de $y$.

## Arithmétique

> TBD à nb de bit fixé clair. Mais marche aussi avec des tailles aussi grand que l'on veut.
> TBD multiplication plus complexe que addition
> TBD dire qu'on peut s'en sortir par "concaténation" de fonctions de taille fixe (ie 64 bit, on y reviendra)

> TBD toute les notations.
> TBD intervalle entier [a..b] et vide si a>b
> TBD écriture binaire b00110, octal o744, décimale et hexadécimale #FF42.

On considérera ici que l'on a des vecteurs de $n$ bits, allant du bit de poids faible au bit de poids fort :

```
index  :     876543210
valeur : x = 010100110
```

$n$ est grand. Même si $\mathcal{O}(1)$ pour des mot sur 64b, comme n>64, c'est plus.

C'est pourquoi les complexités (voir Knuth) sont souvent données en fonction de $n$, le nombre de bit des paramètres et de $B$, la base de calcul (64b pour nous actuellement). Nous ne nous embêterons pas ici avec ça et donnerons les complexités uniquement en fonction de $n$.

### Somme

Sur deux entiers non signés

```
  100101
+ 001011
--------
  110001
```

> TBD : algo avec retenue.

Modulo n :

```
  100101
+ 011011
--------
  000001
```

### Opposé

{% lien %}
[complément à 2](https://fr.wikipedia.org/wiki/Compl%C3%A9ment_%C3%A0_deux)
{% endlien %}

Code sur les n-1 premiers bit, le dernier est laissé pour la gestion du signe.

<div>
$$
-x \coloneqq \bar{x} + 0b1
$$
</div>

### Soustraction

somme de deux entiers signés

<div>
$$
x-y \coloneqq x + (-y)
$$
</div>

### Multiplication

On utilise la [multiplication posée](https://fr.wikipedia.org/wiki/Multiplication#Techniques_de_multiplication). Les nombres binaires simplifient grandement le calcul car il suffit de faire des additions.

La complexité de l'algorithme est en $\mathcal(O)(n^2)$.

```
       100101
     * 001011
    ---------
       100101
      100101
     000000   
    100101
   000000
+ 000000 
------------
  00110010111
```

On trouve que $0b100101 \cdot 0b1011 = 0b110010111$ ($37 \cot 11 = 407$).

{% info %}
Les meilleurs algorithmes connus pour effectuer la multiplication sont en $\mathcal(O)(n\log(n))$ mais ne sont presque jamais implémenté car leurs valeurs ajoutées est asymptotique et est atteinte pour des nombres trop grand par rapport aux nombres utilisés.
{% endinfo %}

### Division euclidienne

On utilise la [division posée](https://fr.wikipedia.org/wiki/Division_pos%C3%A9e). Les nombres binaires simplifient grandement le calcul car il suffit de faire des soustractions.

La complexité de l'algorithme est en $\mathcal(O)(n^2)$.

```
  100101 | 1011
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

On trouve que : $0b100101 / 0b1011 = 0b11$ et $0b100101 \mathbin{\small\\%} 0b1011 = 100$

$37 / 11 = 3$ et $37 \mathbin{\small\\%} 11 = 4$

### pgcd

> TBD voir si on ne l'a pas déjà quelque part ?

Le calcul du pgcd (*GCD* en anglais) peut être fait en utilisant l'algorithme d'Euclide (on y reviendra pour sa version étendue), mais pour des nombres binaires, il est plus simple d'utiliser un algorithme chinois datant de la même époque qu'Euclide : le [*binary GCD*](https://en.algorithmica.org/hpc/algorithms/gcd/#binary-gcd).

L'algorithme fonctionne récursivement en utilisant les propriétés suivantes :

{% note %}
Pour deux nombre entiers positifs :

1. $\text{pgcd}(a, 0) = a$
2. si $a$ et $b$ sont pairs, alors $\text{pgcd}(a, b) = 2\cdot \text{pgcd}(a/2, b/2)$
3. si $a$ est pair et $b$ impair, alors $\text{pgcd}(a, b) = \text{pgcd}(a/2, b)$
4. si $a$ et $b$ sont impairs, alors $\text{pgcd}(a, b) = \text{pgcd}(\vert a-b\vert , \min(a, b))$
{% endnote %}
{% details "preuve" %}

clair.

{% enddetails %}

Cet algorithme est très efficace pour les nombres binaires puisque la division par deux est un shift de 1 bit vers la droite. De plus l'analyse de sa complexité est identique à même de l'[exponentiation indienne](/cours/algorithme-code-théorie/algorithme/étude-exponentiaion#algo-rapide), ce qui mène à une complexité de $\mathcal{O}(n^2)$ car le shift n'est pas une opération binaire si $n$ est grand.

{% info %}
Pour une étude étendu de l'algorithme d'Euclide, Voir Knuth tome 2 (*Art of computer Programming*, tome 2)
{% endinfo %}

## Pseudo-code

> TBD pseudo-code = FB et structures de contrôles. et se généralise à NAND et structure de contrôle.
> Voir comment les structures de contrôles s'écrive comme test et saut.
> 
> TBD donner def. Uniquement manipulation d'un bit et variables = tableau de bit.
> TBD complexité 