---
layout: page
title:  "fonction de hash"
category: cours
---

Les fonctions de hachage. De la définition mathématique à son utilité en informatique.

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [théorie]({% link cours/algorithme-code-theorie/theorie/index.md %}) / [fonctions de hash]({% link cours/algorithme-code-theorie/theorie/fonctions-hash.md %})
>
> prérequis :
>
>* [fonctions]({% link cours/algorithme-code-theorie/theorie/fonctions.md %})
{: .chemin}

## définition

Dans notre cas, en informatique, on peut définir une [fonction de hachage](https://fr.wikipedia.org/wiki/Fonction_de_hachage) $f$ comme étant :

> Une **fonction de hachage** est une fonction $f$ :
>
> $$f: \mathbb{N} \rightarrow [0 \mathrel{ {.}\,{.} } m]$$
>
> où $m$  est un entier positif.
{: .note}

Une définition alternative, également souvent utilisée, est :

> Une **fonction de hachage** est une fonction $f$ qui associe à tout mot de $\\{0, 1\\}^\star$ un mot de $\\{0, 1\\}^k$.
>
> où $k$  est un entier positif.
{: .note}

Enfin, comme tout en informatique est codé comme une suite de 0 et de 1, une fonction de hachage peut ainsi être vue comme :

> Une **fonction de hachage** est une fonction qui associe à tout **objet** soit :
>
> * un entier entre 0 et $m$
> * un mot de $\\{0, 1\\}^k$
>
> {:.note}

En python par exemple, on peut utiliser la fonction [`hash`](https://docs.python.org/fr/3/library/functions.html?highlight=hash#hash) :

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

> Remarquez que la fonction de hash utilisée dépend du type d'objet.
>
> De plus, comme un hash est défini à la création d'un objet, il n'existe pas de hash pour des objet mutable en python. Ainsi `hash([])` produira une erreur (`TypeError: unhashable type: 'list'`).

La principale raison de l'utilisation des fonctions de hachage est :

> Si $f$ est une fonction de hachage, alors :
>
> $$ f(a) \neq f(b) \Rightarrow a \neq b$$
>
{:.note}

Une fonction de hachage permet de partitionner les entiers (*ie.* les objets) en $m+1$ classes. Pour que ce partitionnement soit utile, on demande à une *bonne* fonction de hachage d'avoir en plus les propriétés suivantes :

> Une fonction de hachage $f: \mathbb{N} \rightarrow [0\mathrel{ {.}\,{.} } m]$ utile doit avoir les 3 propriétés suivantes :
>
> 1. elle doit être **déterministe** : un même message doit toujours avoir la même valeur de hachage.
> 2. elle doit être facilement calculable
> 3. elle doit être  **uniforme** : la probabilité que $f(a) = i$ doit être de $\frac{1}{m+1}$ pour tout $a\in \mathcal{N}$ et $0 \leq i \leq m$
>
{:.note}

## exemples

### une constante

La fonction constante :

$$
\begin{array}{ccccc}
f & : & \mathbb{N} & \to & [0\mathrel{ {.}\,{.} } m] \\
 & & x & \mapsto & f(x)=0 \\
\end{array}
$$

est une fonction de hachage.

Elle n'est cependant que peu utile, car elle n'est pas uniforme. Ceci dit, elle est utilisé plus souvent qu'on ne le croit par des informaticiens trop pressés par le temps...

### le modulo

La fonction modulo (le reste de la division entière) :

$$
\begin{array}{ccccc}
f & : & \mathbb{N} & \to & [0\mathrel{ {.}\,{.} } m] \\
 & & x & \mapsto & f(x) = x \mod m \\
\end{array}
$$

est une fonction de hachage.

Sous certaines conditions, elle respecte bien les 3 propriétés d'une fonction de hachage utile.

#### déterministe

Comme $a \mod m$  est égal au reste de la division entière de $a$ par $m$ son calcul est bien déterministe.

#### facilement calculable

Même lorsque les objets deviennent grand, le caclul du modulo peut se faire aisément. En effet le fait que :

* $(a + b) \mod m$ = $((a \mod m) + (b\mod m)) \mod m$
* $(a \times b) \mod m$ = $((a \mod m) \times (b\mod m)) \mod m$

Par exemple :

* $7 \mod 3 = (4 \mod 3) + (3 \mod 3) = 1 + 0 = 1$
* $4 \times 3 \mod 3 = (4 \mod 3) \times (3 \mod 3) = 1 \times 0 = 0$

Permet de calculer le modulo *par morceau*.

Per exemple, prenons un objet $n$, qui est représenté en mémoire par une suite de $k \times l$ $0$ et $1$ :

$$
n = \underbrace{0 \cdots 1}_{k \times l}
$$

On peut alors le découper en paquets de $k$ bits (souvent $k = 256$) :

$$
n = \underbrace{0 \cdots 1}_{k} \cdots \underbrace{1 \cdots 0}_{k} \cdots \underbrace{1 \cdots 1}_{k}
$$

Et calculer le modulo sur chacun de ces paquets indépendamment, puis sommer le tout (en faisant à chaque fois le modulo).

Par exemple, en notant $n_i$ le nombre associé aux $i$ème $k$ bits de $n$ on a :

$$
\begin{array}{lcl}
n &=& n_l2^{kl} + n_{l-1} 2^{k(l-1)} + \dots + n_{i} 2^{ki} + \dots + n_0\\
& & \sum_{i=0}^l n_i2^{ki}
\end{array}
$$

De la un pseudo-code du calcul du modulo de $n$ est alors :

```python
exp = (2 ** k) mod k
res = n_0 mod k
for 1 <= i <= k:
    c = (exp * i) mod k
    c = (c * n_i) mod k
    res = (res + c) mod k
```

Comme accéder à $k$ bits dans la mémoire ou faire le modulo d'un nombre de taille fixe est très facile pour un ordinateur, on peut facilement calculer le modulo d'un objet aussi grand qu'il soit.

#### équiprobable

Si les nombres à hacher sont pris aléatoirement, le modulo est bien uniforme quelque soit $m$.

Attention cependant :

$$
(k \times p) \mod (p \times q) = (k \mod q) \times p
$$

Les nombres qui ont un diviseur commun avec $m$ seront hachés par un nombre qui est un multiple de ce diviseur !
De là, si l'ensemble de nombre que l'on a à hacher n'est pas uniforme mais admets des diviseurs commun, ce qui arrive souvent, la probabilité de hachage ne sera pas uniforme.

Pour palier ce problème :

> Si l'on utilise le modulo comme fonction de hachage, il est recommandé d'utiliser un nombre $m$ premier.
{: .note}

#### hash de structures composées

Par exemple considérons le tuple suivant : `(1, 'un', 3.14)`. Il contient 3 types de données différents. On pourrait très bien utiliser sa représentation binaire et faire le hash de cet objet mais, souvent, ce n'est pas cette approche qui est utilisée. On préfère combiner les hash des des différents types d'objets en un hash unique.

En java par exemple, une façon classique de procéder est de :

```text
res = 0
pour chaque élément e du tuple:
    res = hash(31 * res + hash(e))

```

Ceci assure :

* d'avoir un hash facile à calculer si le chaque de chaque élément l'est
* de ne pas avoir de soucis de diviseurs (voir le soucis du modulo) grâce à la multiplication par 31 qui va *mélanger* le tout à chaque fois

## collisions

> Une **collision** pour une fonction de hachage $h$ est deux nombre $a$ et $b$ telle que $f(a) = f(b)$
{: .note}

Le but est — bien sûr — de minimiser les collisions.

> Pour une fonction de hachage $f: \mathbb{N} \rightarrow [0 \mathrel{ {.}\,{.} } m]$ uniforme, la probabilité $\bar{p}(n, m)$ de tirer $n > 1$ nombres au hasard sans avoir de collisions est de :
>
> $$
> \bar{p}(n, m) = \prod_{i=1}^{n-1}(1-\frac{i}{m+1})
> $$
>
{: .note}
{% details preuve %}

A chaque fois que l'on tire un nombre au hasard, il faut que son hash soit différent de ceux des tirages précédents. Au $i$ème essai il y a donc une probabilité de $\frac{i-1}{m+1}$ de tomber sur un hash déjà vu et une probabilité de $1-\frac{i-1}{m+1}$ d'en obtenir un nouveau.

{% enddetails %}

On peut en extraire des solutions approchées si $m$ est très grand devant $n$ :

> Si $m$ est grand devant $n$, on a :
>
> $$
> \bar{p}(n, m) \simeq \exp(\frac{n^2}{2(m+1)})
> $$
>
> et donc :
>
> $$
> n \simeq \sqrt{2(m+1)\ln(\frac{1}{\bar{p}(n, m)})}
> $$
>
{: .note}
{% details preuve %}

$$
\begin{array}{lcll}
 \bar{p}(n, m)&=&\prod_{i=1}^{n-1}(1-\frac{i}{m+1})&\\
 \ln(\bar{p}(n, m))&=&\ln(\prod_{i=1}^{n-1}(1-\frac{i}{m+1}))&\mbox{car }\ln \mbox{ est une fonction croissante}\\
 \ln(\bar{p}(n, m))&=&\sum_{i=1}^{n-1}\ln((1-\frac{i}{m+1}))&\mbox{car }\ln(ab) = \ln(a) + \ln(b)\\
 \ln(\bar{p}(n, m))&\simeq&\sum_{i=1}^{n-1}(-\frac{i}{m+1})&\mbox{car }\ln(1+x) \simeq x\mbox{ si } x \simeq 0\\
 \ln(\bar{p}(n, m))&\simeq&\frac{-1}{m+1}\sum_{i=1}^{n-1}i&\\
 \ln(\bar{p}(n, m))&\simeq&\frac{-1}{m+1}\frac{n(n-1)}{2}&\\
 \ln(\bar{p}(n, m))&\simeq&\frac{-n^2}{2(m+1)}& \mbox{car } n \simeq n-1\\
\end{array}
$$

La dernière égalité nous nonne aisément la deuxième égalité à prouver, et en repassant aux exponentielle on en déduit aussi la première égalité.

{% enddetails %}

Ces inégalités permettent par exemple de calculer le nombre d'étudiants qu'il faut avoir dans une classe pour avoir 50% de chances d'avoir deux dates d'anniversaires identiques. Ce résultat est connu sous le nom de [paradoxe des anniversaires](https://fr.wikipedia.org/wiki/Paradoxe_des_anniversaires), car le nombre de 23 ($\sqrt{2\times 365 \ln(1/.5)} \simeq 22.5$) semble très petit.

Si l'on prend un exemple réaliste de fonction de hash, par exemple celle utilisée par [git](https://fr.wikipedia.org/wiki/Git), qui rend un mot de $\\{0, 1\\}^{160}$ (git utilise la fonction de hachage [sha-1](https://fr.wikipedia.org/wiki/SHA-1)), il faudrait avoir un nombre de tirage de :

$$
n = \sqrt{2\times 2^{160}\ln(\frac{1}{.5})} \simeq 2^{80}
$$

Pour avoir 50% de chance d'obtenir une collision. Ce qui fait tout de même un sacré paquet !

## utilisation

On l'a vue, si la taille du hashage est grand, il faut a priori un grand nombre d'objet pour espérer avoir une collision. C'est pourquoi on considère souvent que :

> *En pratique* une fonction de hashage utile est une **injection** de l'ensemble des objets utilisés dans le programme dans $[0 \mathrel{ {.}\,{.} } m]$ ou $\\{0, 1\\}^k$  selon la fonction utilisée
{: .note}

Cette propriété permet d'utiliser les fonctions de hashage pour :

* proposer des résumés d'un objet (c'est comme ça que git stocke ses objets) : deux objets sont considérés identiques si'l ont le même hash, ce qui est bien plus rapide que de comparer bit à bit les 2 objets.
* créer des structures de données avancées comme les dictionnaires

Les fonctions de hachages sont même utilisées pour stocker les mots de passe sur votre ordinateur, mais pour que ne soit pas (ou très difficilement) piratable, il faut utiliser des fonctions de hashage dites *cryptographique*.

## hash cryptographique

> ici
{: .tbd}

### propriétés en plus

* doit changer (beaucoup) si on change un peu l'entrée (crypto)
* difficile de trouver 2 mots de même hash (crypto)
* trouver un mot qui a le même hash doit être compliqué (pour crypto)

il faut que de petit changement dans l'entrée produisentde gros changements dans la sortie.

### comment

sha-X

### exemple d'utilisation

* les mots de passes
* l'empreinte/vérification d'un texte/bibliothèque (hash sha)