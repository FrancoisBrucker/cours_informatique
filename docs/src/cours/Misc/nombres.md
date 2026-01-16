---
layout: layout/post.njk

title: Nombres entiers

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD y mettre la partie sur les tableaux de bits de </cours/algorithmie/fonctions-booléennes/>{.interne}
> TBD mémoire :
>
> - base = un octet 1B. Comme si on était en base 256. Pour avoir accès aux bits on utilise des opérations logiques.
> - en mémoire rangé dans un tableau bit faible d'index 0.
> - registre = accès mémoire par paquet de 64b = 8B. On ne peut accéder en 1 opération qu'auz adresse divisible par 8. Dans le registre bits rangés bit d'index faible = 0. Pour le reste ça se fait  en plusieurs opérations avec des décalages pour retrouver le tableau de bits.
> nombre plus gros que 8B rangé en little endian/big endian (intel vs le reste du monde...).

## <span id="exponentiation">Exponentiation

L'algorithme suivant est décrit intensivement dans Knuth, volume XXX. C'est une utilisation de l'exponentiation indienne en utilisant l'écriture binaire des nombres.

Rappelons l'[algorithme d'exponentiation indienne](/cours/algorithmie/projet-exponentiation/étude-algorithmique/#algo-rapide) qui calcule $x^y$ :

```
expo(x, y):
  r = 1
  tant que y n'est pas nul :
    si y est impair:
      y = y - 1
      r = r * x    # MULTIPLY
    sinon:
      x = x * x    # SQUARE
      y = y / 2    
  
  rendre r
```

Que l'on peut aussi écrire ainsi :

```
expo(x, y):
  r = 1
  tant que y n'est pas nul :
    si y est impair:
      y = y - 1
      r = r * x      # MULTIPLY
    x = x * x        # SQUARE
    y = y / 2    
  
  rendre r
```

Sous la forme précédente on voit bien que tout se passe comme si l'algorithme regardais chaque bit constituant $y$

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

Au final, si $x=x_{n-1}\dots x_0$ est sur $m$ bits et $y=y_{n-1}\dots y_0$ sur $n$ bit on a :

```
expo(x, y):
  r = 1
  pour chaque i de 0 à n-1:
    si y_i == 1:
      r = r * x      # MULTIPLY
    x = x * x        # SQUARE
  rendre r
```

> TBD exercice pour l'écrire dans l'autre sens voir <https://perso.telecom-paristech.fr/pacalet/HWSec/lectures/side_channels/l-nb.pdf>

## <span id="logarithme-discret">Logarithme discret

> TBD
> TBD algo de résolution puis comment voir ça comme un problème de factorisation.

## Algorithme d'Euclide Étendu

- Si $a > b > 0$ on a $\text{pgcd}(a, b) = \text{pgcd}(b, a \bmod b)$
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

```python/
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
> 4.5.4 Knuth
