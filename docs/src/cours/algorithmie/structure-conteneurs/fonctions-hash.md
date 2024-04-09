---
layout: layout/post.njk
title: "Fonction de hachage"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le but d'une fonction de hachage est d'associer un entier borné à tout objet. Son utilité est de permettre de distinguer rapidement deux objets avec une forte probabilité. Les fonctions de hash sont utilisés tous les jours par des millions de personnes et encore plus d'ordinateurs. Une des fonctions de hash la plus utilisée est la famille de fonction [sha](https://fr.wikipedia.org/wiki/Secure_Hash_Algorithm).

On verra plus tard, qu'elles peuvent également être utilisées pour permettre d'indexer des tableaux par autre chose que des entiers (ce sont les [tableaux ssociatifs](../tableau-associatif){.interne}).

## Définitions

On peut définir une [fonction de hachage](https://fr.wikipedia.org/wiki/Fonction_de_hachage) $f$ comme étant :

{% note "**Définition**" %}
Une **_fonction de hachage_** est une fonction $f$ :

<div>
$$
f: \mathbb{N} \rightarrow [0 \mathrel{ {.}\,{.} } m[
$$
</div>

où $m$ est un entier positif.
{% endnote %}

Une définition alternative, également souvent utilisée, est :

{% note "**Définition**" %}
Une **_fonction de hachage_** est une fonction $f$ qui associe à tout mot de $\\{0, 1\\}^\star$ un mot de $\\{0, 1\\}^k$. Avec $k$ est un entier positif.
{% endnote %}

Enfin, comme tout en informatique est codé comme une suite de 0 et de 1, une fonction de hachage peut ainsi être vue comme :

{% note "**Définition**" %}
Une **_fonction de hachage_** est une fonction qui associe à tout **objet** soit :

- un entier entre 0 et $m$
- un mot de $\\{0, 1\\}^k$ ($k > 0$)

{% endnote %}

En python par exemple, on peut utiliser la fonction [`hash`{.language-}](https://docs.python.org/fr/3/library/functions.html?highlight=hash#hash) :

```python
>>> hash("du texte")
1183064373567153871
>>> hash(True)
1
>>> hash(1)
1
>>> hash(3.14)
322818021289917443
```

Remarquez que la fonction de hash utilisée dépend du type d'objet.

De plus, comme un hash est défini à la création d'un objet, il n'existe pas de hash pour des objets mutable en python. Ainsi `hash([])`{.language-} produira une erreur (`TypeError: unhashable type: 'list'`{.language-}).

La principale raison de l'utilisation es fonctions de hachage est :

{% note %}
Si $f$ est une fonction de hachage, alors :

$$
f(a) \neq f(b) \Rightarrow a \neq b
$$

{% endnote %}

Une fonction de hachage permet de partitionner les entiers (_ie._ les objets) en $m+1$ classes. Pour que ce partitionnement soit utile, on demande à une _bonne_ fonction de hachage d'avoir en plus les propriétés suivantes :

{% note %}

Pour qu'une fonction de hachage $f: \mathbb{N} \rightarrow [0\mathrel{ {.}\,{.} } m]$ soit **_utile_**, elle doit avoir les 3 propriétés suivantes :

1. elle doit être **déterministe** : un même message doit toujours avoir la même valeur de hachage.
2. elle doit être **facilement calculable**
3. elle doit être **uniforme** : la probabilité que $f(a) = i$ doit être de $\frac{1}{m}$ pour tout $a\in \mathcal{N}$ et $0 \leq i \leq m$

{% endnote %}

## Exemples

### Une constante

La fonction constante :

<div>
$$
\begin{array}{ccccc}
f & : & \mathbb{N} & \to & [0\mathrel{ {.}\,{.} } m[ \\
 & & x & \mapsto & f(x)=0 \\
\end{array}
$$
</div>

est une fonction de hachage.

Elle n'est cependant que peu utile, car elle n'est pas uniforme. Ceci dit, elle est utilisé plus souvent qu'on ne le croit par des informaticiens trop pressés par le temps...

### Le modulo

La fonction modulo (le reste de la division entière) :

<div>
$$
\begin{array}{ccccc}
f & : & \mathbb{N} & \to & [0\mathrel{ {.}\,{.} } m[ \\
 & & x & \mapsto & f(x) = x \mod m \\
\end{array}
$$
</div>

est une fonction de hachage.

Sous certaines conditions, elle respecte bien les 3 propriétés d'une fonction de hachage utile.

#### Déterministe

Comme $a \mod m$ est égal au reste de la division entière de $a$ par $m$ son calcul est bien déterministe.

#### Facilement calculable

Même lorsque les objets deviennent grand, le calcul du modulo peut se faire aisément. En effet le fait que :

- $(a + b) \mod m$ = $((a \mod m) + (b\mod m)) \mod m$
- $(a \times b) \mod m$ = $((a \mod m) \times (b\mod m)) \mod m$

Par exemple :

- $7 \mod 3 = (4 \mod 3) + (3 \mod 3) = 1 + 0 = 1$
- $4 \times 3 \mod 3 = (4 \mod 3) \times (3 \mod 3) = 1 \times 0 = 0$

Ce qui permet de calculer le modulo _par morceau_.

Per exemple, prenons un objet $n$, qui est représenté en mémoire par une suite de $k \times l$ $0$ et $1$ :

<div>
$$
n = \underbracket{0 \cdots 1}_{k \times l}
$$
</div>

On peut alors le découper en paquets de $k$ bits (souvent $k = 256$, voir par exemple l'algorithme [sha-2](https://fr.wikipedia.org/wiki/SHA-2)) :

<div>
$$
n = \underbracket{0 \cdots 1}_{k} \cdots \underbracket{1 \cdots 0}_{k} \cdots \underbracket{1 \cdots 1}_{k}
$$
</div>

Et calculer le modulo sur chacun de ces paquets indépendamment, puis sommer le tout (en faisant à chaque fois le modulo).

Par exemple, en notant $n_i$ le nombre associé aux $i$ème $k$ bits de $n$ on a :

<div>
$$
\begin{array}{lcl}
n &=& n_l2^{kl} + n_{l-1} 2^{k(l-1)} + \dots + n_{i} 2^{ki} + \dots + n_0\\
&=& \sum_{i=0}^l n_i2^{ki}
\end{array}
$$
</div>

Et donc :

<div>
$$
\begin{array}{lcl}
n \mod m &=&  (\sum_{i=0}^l n_i2^{ki}) \mod m \\
&=& (\sum_{i=0}^l ((n_i \mod m)\cdot ((2^{k} \mod m)^i \mod m) \mod m)) \mod m
\end{array}
$$
</div>

Faire tous les calculs de somme et de produit modulo $m$ est très efficace sur un ordinateur car cela revient à travailler à nombre de bit fixé. Or accéder à $k$ bits dans la mémoire ou faire le modulo d'un nombre de taille fixe est une opération élémentaire pour un processeur : on peut facilement calculer le modulo d'un objet aussi grand qu'il soit.

De la un pseudo-code du calcul du modulo de $n$ :

```python
e = (2 ** k) mod m
exp = 1
res = n_0 mod m
for 1 <= i <= l:
    exp = (exp * e) mod m
    c = (exp * n_i) mod m
    res = (res + c) mod m
```

#### Équiprobable

Si les nombres à hacher sont pris aléatoirement, le modulo est bien uniforme quelque soit $m$ (les ensembles $M_i = \\{k\cdot m+i \\mid k \geq 0\\}$ pour $0\leq i \leq m-1$ sont en bijections 2 à 2, sont disjoints et recouvrent tous les entier: un entier pris au hasard a autant de chance d'être dans $M_i$ que dans $M_j$).

Attention cependant :

$$
(k \times p) \mod (p \times q) = (k \mod q) \times p
$$

Les nombres qui ont un diviseur commun avec $m$ seront hachés par un nombre qui est un multiple de ce diviseur !
De là, si l'ensemble de nombre que l'on a à hacher n'est pas uniforme mais admets des diviseurs communs, ce qui arrive souvent, la probabilité de hachage ne sera pas uniforme.

Pour palier ce problème :

{% note %}
Si l'on utilise le modulo comme fonction de hachage, il est recommandé d'utiliser un nombre $m$ premier.
{% endnote %}

### Hash de python

L'algorithme utilisé par python pour effectuer le hash est [sipHash](https://en.wikipedia.org/wiki/SipHash)

{% lien %}

- [déscription](https://cs108.epfl.ch/archive/17/e/SIPH/SIPH.html)
- [Implémentation de SipHash par un de ses créateurs](https://github.com/veorq/SipHash)

{% endlien %}

## Hash de structures composées

Par exemple considérons le tuple suivant : `(1, 'un', 3.14)`{.language-}. Il contient 3 types de données différents. On pourrait très bien utiliser sa représentation binaire et faire le hash de cet objet mais, souvent, ce n'est pas cette approche qui est utilisée. On préfère combiner les hash des des différents types d'objets en un hash unique.

En java par exemple, une façon classique de procéder est :

```text
res = 0
pour chaque élément e du tuple:
    res = hash(31 * res + hash(e))

```

Ceci assure :

- d'avoir un hash facile à calculer si le chaque de chaque élément l'est
- de ne pas avoir de soucis de diviseurs (voir le soucis du modulo) grâce à la multiplication par 31 qui va _mélanger_ le tout à chaque fois

## Collisions
Comme le but premier d'une fonction de hachage est de distinguer deux objets, mais que le nombre de possibilité est fini, il faut minimiser la probabilité que deux objets aient le même hash.

{% note "**Définition**" %}
Une **_collision_** pour une fonction de hachage $h$ est deux nombre $a$ et $b$ telle que $f(a) = f(b)$
{% endnote %}

On va distinguer deux types de collisions, celle d'obtenir un nombre précis :

{% note "**Proposition**" %}
Pour une fonction de hachage $f: \mathbb{N} \rightarrow [0 \mathrel{ {.}\,{.} } m[$ uniforme, la probabilité $p(n, m)$ de tirer $n > 1$ nombres $x$ au hasard sans avoir $f(x) = h$ (avec $0 \leq h <m$ donné) est :

$$
p(n, m) = \left(1-\frac{1}{m}\right)^n
$$

{% endnote %}
{% details "preuve", "open" %}
À chaque tirage, la probabilité que la fonction de hash soit égale à $h$ est $\frac{1}{m}$, la probabilité de ne pas être égale à $h$ est donc $1-\frac{1}{m}$. Les tirages étant équiprobables, la probabilité est bien celle demandée.
{% enddetails %}

Et cell d'obtenir deux fois le même nombre :

{% note "**Proposition**" %}
Pour une fonction de hachage $f: \mathbb{N} \rightarrow [0 \mathrel{ {.}\,{.} } m[$ uniforme, la probabilité $\bar{p}(n, m)$ de tirer $n > 1$ nombres $x_1, \dots, x_n$ au hasard tels que $h(x_i) \neq h(x_j)$ pour tous $i \neq j$, c'est à dire sans avoir de collisions est de :

$$
\bar{p}(n, m) = \prod_{i=1}^{n}(1-\frac{i-1}{m})
$$

{% endnote %}
{% details "preuve", "open" %}

A chaque fois que l'on tire un nombre au hasard, il faut que son hash soit différent de ceux des tirages précédents. Au $i$ème essai il y a donc une probabilité de $\frac{i-1}{m}$ de tomber sur un hash déjà vu et une probabilité de $1-\frac{i-1}{m}$ d'en obtenir un nouveau.

{% enddetails %}

On peut en extraire des solutions approchées si $m$ est très grand devant $n$ :

{% note  "**Proposition**" %}
Si $m$ est grand devant $n$, on a :

$$
p(n, m) \simeq \exp(-\frac{n}{ m})
$$

$$
\bar{p}(n, m) \simeq \exp(-\frac{n^2}{2\cdot m})
$$

et donc :

<div>
$$
\begin{array}{lcl}
n &\simeq &m\ln(p(n, m))\\
&\simeq & \sqrt{-2\cdot m\cdot \ln(\bar{p}(n, m))}
\end{array}
$$
</div>

{% endnote %}
{% details "preuve" %}

Les deux dernières égalités se déduisent aisément des deux premières.

Pour $p(n, m)$ :

<div>
$$
\begin{array}{lcll}
 p(n, m)&=&\left(1-\frac{1}{m}\right)^n&\\
 \ln(p(n, m))&=&\ln(\left(1-\frac{1}{m}\right)^n)&\mbox{car }\ln \mbox{ est une fonction croissante}\\
 \ln(p(n, m))&=&n\ln((1-\frac{1}{m}))&\mbox{car }\ln(ab) = \ln(a) + \ln(b)\\
 \ln(\bar{p}(n, m))&\simeq&n(-\frac{1}{m})&\mbox{car }\ln(1+x) \simeq x\mbox{ si } x \simeq 0\\
 \ln({p}(n, m))&\simeq&\frac{-n}{m}&\\
 {p}(n, m))&\simeq&\exp(-\frac{n}{m})&\mbox{car }\exp \mbox{ est une fonction croissante}\\
 \end{array}
$$
</div>

De la même manière pour $\bar{p}(n, m)$ :

<div>
$$
\begin{array}{lcll}
 \bar{p}(n, m)&=&\prod_{i=1}^{n}(1-\frac{i-1}{m})&\\
 \ln(\bar{p}(n, m))&=&\ln(\prod_{i=1}^{n}(1-\frac{i-1}{m}))&\mbox{car }\ln \mbox{ est une fonction croissante}\\
 \ln(\bar{p}(n, m))&=&\sum_{i=1}^{n}\ln((1-\frac{i-1}{m}))&\mbox{car }\ln(ab) = \ln(a) + \ln(b)\\
 \ln(\bar{p}(n, m))&\simeq&\sum_{i=1}^{n}(-\frac{i-1}{m})&\mbox{car }\ln(1+x) \simeq x\mbox{ si } x \simeq 0\\
 \ln(\bar{p}(n, m))&\simeq&\frac{-1}{m}\sum_{i=1}^{n}(i-1)&\\
 \ln(\bar{p}(n, m))&\simeq&\frac{-1}{m}\sum_{j=1}^{n-1}(j)&\mbox{avec le changement de variable } j = i-1\\
 \ln(\bar{p}(n, m))&\simeq&\frac{-1}{m}\frac{n(n-1)}{2}&\\
 \ln(\bar{p}(n, m))&\simeq&\frac{-n^2}{2\cdot m}& \mbox{car } n \simeq n-1\\
 \bar{p}(n, m)&\simeq&\exp(\frac{-n^2}{2\cdot m})&\mbox{car }\exp \mbox{ est une fonction croissante}\\
\end{array}
$$
</div>

{% enddetails %}

Ces inégalités permettent par exemple de calculer le nombre d'étudiants qu'il faut avoir dans une classe pour avoir 50% de chances d'avoir deux dates d'anniversaires identiques. Ce résultat est connu sous le nom de [paradoxe des anniversaires](https://fr.wikipedia.org/wiki/Paradoxe_des_anniversaires), car il faut :

- 523 étudiants (${-365 \cdot \ln(.5)} \simeq 523$) pour qu'il y ait plus de 50% de chance qu'une personne soit née le même jour que moi,
- seulement 23 étudiants ($\sqrt{-2\cdot 365 \cdot \ln(.5)} \simeq 22.5$) pour qu'il y ait plus de 50% de chance que 2 personnes soient nées le même jour.

{% faire %}
Faites le test !
{% endfaire %}

Si l'on prend un exemple réaliste de fonction de hash, par exemple celle utilisée par [git](https://fr.wikipedia.org/wiki/Git), qui rend un mot de $\\{0, 1\\}^{160}$ (git utilise la fonction de hachage [sha-1](https://fr.wikipedia.org/wiki/SHA-1)), il faudrait avoir un nombre de tirages de :

$$
n = \sqrt{-2\times 2^{160}\ln({.5})} \simeq 1.2 \cdot \sqrt{2^{160}} \simeq 1.2 \cdot 2^{80}
$$

Pour avoir 50% de chance d'obtenir une collision. Ce qui fait tout de même un sacré paquet !

De ce qui découle on en déduit une règle universelle de toute fonction de hash :

{% note "**Paradoxe des anniversaires**" %}
Pour toute fonction de hash rendant un mot de $p$ bits, il faut : $n \simeq 1.2 \cdot 2^{p/2}$ tirages différents pour avoir 50% de chance d'avoir 2 tirages de même hash.
{% endnote %}

## Utilisation

On l'a vu, si la taille du hachage est grand, il faut a priori un grand nombre d'objet pour espérer avoir une collision. C'est pourquoi on considère souvent que :

{% note %}
_En pratique_ une fonction de hachage utile est une **injection** de l'ensemble des objets utilisés dans le programme dans $[0 \mathrel{ {.}\,{.} } m]$ ou $\\{0, 1\\}^k$ selon la fonction utilisée
{% endnote %}

Cette propriété permet d'utiliser les fonctions de hachage pour :

- proposer des résumés d'un objet (c'est comme ça que git stocke ses objets) : deux objets sont considérés identiques si'l ont le même hash, ce qui est bien plus rapide que de comparer bit à bit les 2 objets.
- créer des structures de données avancées comme les dictionnaires

Les fonctions de hachages sont même utilisées pour stocker les mots de passe sur votre ordinateur, mais pour que ne soit pas (ou très difficilement) piratable, il faut utiliser des [fonctions de hachage cryptographiques](https://fr.wikipedia.org/wiki/Fonction_de_hachage_cryptographique) qui assurent qu'il est _difficile_ :

- de trouver $m$ à partir de $h$ tel que $f(m) = h$
- de trouver $m'$ à partir de $m$ tel que $f(m') = d(m)$
