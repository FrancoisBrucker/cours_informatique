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

<div id="CPPRG"></div>

{% note "**Définition**" %}
Un **générateur de nombres pseudo-aléatoire sécurisé** (_secure PRG, secure pseudo random generator_) doit avoir les propriétés suivantes :

- $G: \\{0, 1\\}^s \rightarrow \\{0, 1\\}^t$, avec $s <<t$
- $G$ doit être implémentable par algorithme efficace
- tout algorithme efficace ne peut avoir qu'un avantage négligeable au jeu de la reconnaissance  [jeu de la reconnaissance](../définition-sécurité/#jeu-reconnaissance) entre :

- la variable aléatoire $G(k \xleftarrow{U} \\{0, 1\\}^s)$
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

Notez que la distribution de la sortie d'un CPRNG n'est **pas** uniforme. Considérez par exemple un CPRNG qui double la taille de son entrée. La moitié des mots de $\\{0, 1\\}^{2s}$ ne peuvent être obtenu par $G(k)$ puisque $\vert G(k \xleftarrow{U} \\{0, 1\\}^s)\vert \leq 2^s$. 

Notez qu'un CPRNG donne des résultats loin d'être aléatoire, en particulier distribution de sa sortie n'est **pas** uniforme. En effet :

- le nombre de chaînes atteignable depuis sa seed : $2^s$
- le nombre de chaînes possible : $2^{t} > 2^s$

Considérons l'algorithme **non efficace** $D$ suivant :

1. il calcule $G(k)$ pour tous les $2^s$ valeurs de $k$ possible.
2. lorsque le testeur lui montre un mot $m$ de $\\{0, 1\\}^n$ il répond 1 s'il existe $k$ tel que $G(k)=m$, et 0 sinon.

Il reconnaît $G$ avec l'avantage suivant :

- $Pr[D(x) = 1 | b=1] = Pr[D(G(k)) = 1] = 1$
- $Pr[D(x) = 1 | b=0] = Pr[D(u) = 1] = 2^s/2^t = 1/2^{t-s}$ qui correspond à la probabilité que $u \xleftarrow{U} \\{0, 1\\}^t$ soit choisit parmi les mots possibles de $G$ ($2^s$ mots de $G$ parmi les $2^t$ mots possibles)

Son avantage est donc $1-1/2^{t-s}$ qui peut être énorme si $t>>s$

Cette attaque brute force nous donne une borne min acceptable pour une attaque : il faut que $s$ soit assez grand pour que générer toute les solutions soient non efficace.
Notez que ceci ne contredit pas la définition puisque l'adversaire n'est pas efficace.


## Non prédictabilité

Si l'on utilise notre générateur pour une transmission avec un chiffre de Vernam il est nécessaire que l'on ne puisse pas déterminer la fin de $G(k)$ en ayant son début.  En effet, si un attaquant peut envoyer des messages à chiffrer, ou au moins une  partie du message, il peut envoyer des 0 :

```
  kkkkkkk
⊕ 0000000
----------
  kkkkkkk
```

Pour trouver une partie de la clé. Si à partir de là on peut prédire la suite toute la sécurité en serait compromise.

Heureusement pour nous, non-prédictabilité et CPRNG sont deux notions équivalentes.


{% note "**Définition**" %}
Une suite $(x_i^k)_{i\geq 0}$ avec $k \in \\{0, 1\\}^s$ est **_non prédictible_** si tout algorithme efficace ne peut peut prédire $x^k_{m+1}$ sachant $x^k_1, \dots x^k_{m}$ qu'avec un avantage négligeable.
{% endnote %}

Ceci disqualifie d'emblée tous les générateurs pseudo-aléatoire de type $x^k_{i+1} = a \cdot x^k_{i} + b \bmod p$, puisque connaître $x^k_i$ permet de connaître tout $x^k_j$ avec $j> i$. Ceci est la principale différence entre un générateur pseudo-aléatoire et un générateur cryptographique : le premier veut obtenir une suite uniforme (ce que fait le générateur avec un modulo si $p$ est premier) alors que le second cherche à ne pas être prédictible.

Commençons par montrer qu'un CPRNG est non prédictible :

{% note "**Proposition**" %}
Un CPRNG $G$ produit une suite $G(k)$ de $\\{0, 1\\}^t$ non prédictible.
{% endnote %}
{% details "preuve", "open" %}

Supposons qu'un CPRNG $G$ soit prédictible. Il existe alors un algorithme efficace $A$ qui possède un avantage non négligeable pour déterminer le $m+1$ ème bit de la suite à partir des $m$ premiers.

On peut utiliser cet algorithme pour déterminer si $G$ est un CPRNG : on ne considère que les $m+1$ premiers bits et on rend la valeur donnée par l'algorithme $A$. L'avantage est le même et est non négligeable.

{% enddetails %}

La réciproque est plus compliquée, mais montre que les deux notions sont équivalentes :

{% note "**Théorème (Yao, 1982)**" %}
Une suite non prédictible est un CPRNG.
{% endnote %}
{% details "preuve", "open" %}

Soit $(x^k)_{1\leq i \leq t}$ une suite non prédictible et $u \xleftarrow{U} \\{0, 1\\}^t$ une variable aléatoire uniforme sur $\\{0, 1\\}^t$.

On construit la variable aléatoire $Y_i(k)$ sur $\\{0, 1\\}^t$ telle que : 

- les $i$ premiers éléments de $Y_i(k)$ soient les $i$ premiers éléments de $(x^k)_{1\leq i \leq t}$
- les $t-i$ derniers éléments de $Y_i$ soient les $t-i$ derniers éléments d'une réalisation de $u \xleftarrow{U} \\{0, 1\\}^t$

Supposons qu'il existe $i$ tel que l'on puisse reconnaître $Y_i(k)$ de $Y_{i+1}(k)$ avec un avantage non négligeable. Prenons alors $i$ le plus petit possible et $A$ un algorithme efficace qui le reconnaît avec un avantage non négligeable $a$ (on suppose sans perte de généralité que $A$ répond 1 s'il reconnaît $Y_i(k)$).

Soit alors la variable aléatoire $Y^b_i(k)$ sur $\\{0, 1\\}^t$ avec $b\in\\{0, 1\\}$ telle que : 

- les $i-1$ premiers éléments de $Y'_i(k)$ soient les $i$ premiers éléments de $(x^k)_{1\leq i \leq t}$
- le $i$ élément de $Y'_i(k)$ est $b$
- les $t-i$ derniers éléments de $Y'_i$ soient les $t-i$ derniers éléments d'une réalisation de $u \xleftarrow{U} \\{0, 1\\}^t$

Soit $y^b$ une réalisation de $Y'_i(k)$. Si $A(y^b) = 1$, alors le $i$ élément de $y^b$ sera $(x^k)_{i}$ avec une probabilité de $a$. Comme cette probabilité est non négligeable $(x^k)_{1\leq i \leq t}$ est prédictible ce qui est contredit notre hypothèse.

On en conclut que pour tout $i$ $Y_i(k)$ est indiscernable de $Y_{i+1}(k)$, en particulier pour $i= t$ où l'on en conclut que $Y$ est indiscernable de $u \xleftarrow{U} \\{0, 1\\}^t$, do ce qui conclut la preuve.

{% enddetails %}
{% lien %}
[Article originel de Yao, 1982](https://www.di.ens.fr/users/phan/secuproofs/yao82.pdf)
{% endlien %}

## Existence

> TBD va aussi nous donner une façon d'en créer une.

> TBD vers random et donc fonction à sens unique.

## Construction

> TBD produire des elements par calcul (mod, lfsr)  plutot pour prng par permutation plutot cprng.
> 
Construire un CPRNG n'est pas une chose facile. Nous allons en montrer une qui va nous être utile lorsque nous présenterons un chiffre moderne.

> TBD chacha20. juste melange, puis compteur. On ne parle pas de nonce (ce sera pour ensuite)

> TBD rekeying. Attention au passé <https://blog.cr.yp.to/20170723-random.html> car on ne génère qu'un bout.
> TBD ? <https://crypto.stackexchange.com/questions/53295/using-chacha20-as-a-prng-with-a-variable-length-seed>

## Implémentations
 


### Cryptographie en python

> TBD module [secrets](https://docs.python.org/fr/3/library/secrets.html#module-secrets)

## Attaques

retrouver les états internes à partir des sorties pour prédire le nombre suivant.

### générateur cryptographique

> TBD

perd la propriété de pouvoir tout rejouer à partir de la seed (pour tester des simulations/générer des maps sur des jeux/fare des sauvegardes plus petites)

<https://en.wikipedia.org/wiki/Cryptographically_secure_pseudorandom_number_generator>
<https://crypto.stackexchange.com/questions/39186/what-does-it-mean-for-a-random-number-generator-to-be-cryptographically-secure>

<https://www.schutzwerk.com/en/blog/attacking-a-rng/>
<https://crypto.stackexchange.com/questions/100503/is-mersenne-twister-hard-to-break-if-it-has-a-reduced-output>
<https://book-of-gehn.github.io/articles/2018/12/23/Mersenne-Twister-PRNG.html>

<https://en.wikipedia.org/wiki/Fortuna_(PRNG)> et update : <https://fr.wikipedia.org/wiki/Fortuna_(cryptographie)>
