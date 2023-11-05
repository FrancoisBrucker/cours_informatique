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

> TBD
