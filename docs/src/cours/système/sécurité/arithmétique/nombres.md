---
layout: layout/post.njk

title: Nombres entiers

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On considérera ici que l'on a des vecteurs de $n$ bits, allant du bit de poids faible au bit de poids fort :

```
index  :     876543210
valeur : x = 010100110
```

$n$ est grand. Même si $\mathcal{O}(1)$ pour des mot sur 64b, comme n>64, c'est plus.

C'est pourquoi les complexités (voir Knuth) sont souvent données en fonction de $n$, le nombre de bit des paramètres et de $B$, la base de calcul (64b pour nous actuellement). Nous ne nous embêterons pas ici avec ça et donnerons les complexités uniquement en fonction de $n$.

## Logique

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
  
### décalages de bits

On utilise deux direction de décalage (gauche et droite) et deux types de décalage selon que les bit poussés à l'extérieur sont réinjectés de l'autre côté ou disparaissent (les bit qui arrivent sont à 0).

- $x << k$ : ***shift*** de $k$ bit vers la gauche. Les $k$ bits de poids faibles sont des $0$ (identique à une multiplication par $2^k$)
- $x >> k$ : ***shift*** de $k$ bit vers la droite. Les $k$ bits de poids forts sont des $0$ (identique à une division par $2^k$)
- $x <<< k$  : ***rotation*** de $k$ bit vers la gauche.
- $x >>> k$  : ***rotation*** de $k$ bit vers la droite.

### Concaténation

$ x || y$ est la concaténation des $n$ bits de $x$ aux $n'$ bits de $y$.

## Arithmétique

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
Les meilleurs algorithmes connus pour effectuer la multiplication sont en $\mathcal(O)(n\log(n))$ mais ne sont presque jamais implémenté cqr leurs valeurs ajoutée est asymptotique et est atteinte pour des nombres trop grand par rapport aux nombres utilisés.
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

On trouve que : $0b100101 / 0b1011 = 0b11$ et $0b100101 \mod 0b1011 = 100$

$37 / 11 = 3$ et $37 \mod 11 = 4$

## Exponentiation

L'algorithme suivant est décrit intensivement dans Knuth, volume XXX. C'est une utilisation de l'exponentiation indienne en utilisant l'écriture binaire des nombres.

Rappelons l'algorithme d'exponentiation indienne qui calcule $x^y$ :

```
expo(x, y):

  r = 1
  tant que y n'est pas nul :
    si y est impair:
      y = y - 1
      r = r * y    # MULTIPLY
    sinon:
      x = x * x    # SQUARE
      y = y / y    
  
  rendre r
```

Nous avons mis en exergue deux lignes (`SQUARE` et `MULTIPLY`, l'algorithme est connu en langue anglaise comme *square and multiply algorithm*). L'astuce pour encore accélérer l'algorithme est de regarder la forme binaire de y. Par exemple supposons que $y = 0b101101$ et suivons l'algorithme pas à pas :

```
101101  # MULTIPLY
101100  -1
101100  # SQUARE
10110   /2
10110   # SQUARE
1011    /2
1011    # MULTIPLY
1010    -1
1010    # SQUARE
101     /2
101     # MULTIPLY
100     -1
100     # SQUARE
10      /2
10      # SQUARE
1       /2
1       # MULTIPLY
0       -1
```

1. Il suffit de regarder le dernier bit de y
2. diviser par deux revient à shift 1 vers la droite
3. le nombre de :
   - `MULTIPLY` est exactement égal au nombre de bits à 1 dans $y$
   - `SQUARE` est exactement égal au nombre de bits de $y$

Au final, si $x$ est sur $m$ bits et $y$ sur $n$ bit, $x^y$ aura $2^n\cdot m$ bits.

## PGCD

Le calcul du PGCD (*GCD* en anglais) peut être fait en utilisant l'algorithme d'Euclide (on y reviendra pour sa version étendue), mais pour des nombres binaires, il est plus simple d'utiliser un algorithme chinois datant de la même époque qu'Euclide : le [*binary GCD*](https://en.algorithmica.org/hpc/algorithms/gcd/#binary-gcd).

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

## Algorithme d'Euclide Étendu

- Si $a > b > 0$ on a $\text{pgcd}(a, b) = \text{pgcd}(b, a \mod b)$
- si $a > b = 0$ on a $\text{pgcd}(a, 0) = a$

Soit alors la suite de division euclidienne définies telles que:

- $a_0 = a$ ; $b_0 = b$
- $a_i = q_i \cdot b_i + r_i$
- $a_{i+1} = b_i$ ; $b_{i+1} = r_i$

Jusqu'à trouver $b_{i} = 0$, et donc $a_i = $\text{pgcd}(a, b)$.

Comme :

- $a_{i} = b_{i-1}$
- $b_{i} = r_{i-1} = a_{i-1} - q_{i-1}\cdot b_{i-1}$

On peut remonter de proche en proche jusqu'à obtenir une équation du type : $\text{pgcd}(a, b) = u\cdot a + v\cdot b$

De façon surprenante, cet enchaînement s'écrit très bien sous la forme de [pseudo code](https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide_%C3%A9tendu#Pseudo-code) si o peut assigner 6 variables en même temps :

```python#
(r, u, v, ) = (a, 1, 0, b, 0, 1)

tant que r2 != 0:
  q = r % r2 
  (r, u, v, r2, u2, v2) = (r2, u2, v2, r - q*r2, u - q*u2, v - q*v2)

return (r, u, v) 
```

Les deux égalités suivantes sont les invariants de boucle de la ligne 3 :

- $r = a\cdot u+ b\cdot v$
- $r2 = a\cdot u2+b\cdot v2$

## Racine carrée entière

### Dichotomie

Avec de la dichotomie :

```
def racine(N):
  g = 1
  d = N

  m = (g + d) / 2
  tant que m * m != N:
    si m * m > N:
      d = m - 1
    sinon:
      l = m + 1
```

Le temps pris sera de l'ordre de $\mathcal{O}(\log_2(N))$ boucles tant que, avec une multiplication par boucle. La complexité totale sera donc de l'ordre de $\mathcal{O}(n^3)$ où $n4 est la taille de $N$ en bits.

### Bit à bit

```
1100011100011
      1000000  plus grande puissance de 2 dont le carré est < à N
      1x00000  x vaut 1 si 1100000 au carré <= N, vaut 0 sinon
      10x0000  x vaut 1 si 1010000 au carré <= N, vaut 0 sinon
      100x000  x vaut 1 si 1001000 au carré <= N, vaut 0 sinon
      1001x00  x vaut 1 si 1001100 au carré <= N, vaut 0 sinon
      10011x0  x vaut 1 si 1001110 au carré <= N, vaut 0 sinon
      100111x  x vaut 1 si 1001111 au carré <= N, vaut 0 sinon
      1001111  
```

On est pas obligé d'élever au carré à chaque fois, on peut s'en sortir juste avec des shift et des additions en stockant judicieusement des variables intermédiaires, voir [wikipedia](https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Binary_numeral_system_(base_2)). On arrive à une formulation en $\mathcal{O}(n^2)$

> TBD expliciter les variables

## Factorisation

{% lien %}
[integer factorization](https://en.wikipedia.org/wiki/Integer_factorization)
{% endlien %}

> TBD : problème : sachant $n$, trouver $p$ et $q$ $n=pq$.
>

Pas d'algorithmes connu pour faire rapidement le calcul.

> TBD :
>
> - <https://gaati.org/bisson/tea/pepites-fact.pdf>
> - <https://webusers.imj-prg.fr/~pascal.molin/cours/crypto/cours_factorisation.html>

### Factorisation de Fermat

{% lien %}
[Factorisation de Fermat](https://fr.wikipedia.org/wiki/M%C3%A9thode_de_factorisation_de_Fermat)
{% endlien %}

Marche bien si $p$ est proche de $q$

Donc pour RSA, il faut bien choisir deux nombres premiers indépendamment. Si vous vous contentez de prendre 1 nombre aléatoire puis de chercher le premier nombre premier au-dessus et en-dessous, la factorisation de Fermat va trouver très rapidement la solution.

## Génération de nombres premiers

> TBD :
>
> - <https://en.wikipedia.org/wiki/Generation_of_primes>
> - [algos](https://www.baeldung.com/cs/prime-number-algorithms)