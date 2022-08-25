---
layout: layout/post.njk 
title: "Fonction de hash"

eleventyNavigation:
  key: "Fonction de hash"
  parent: Théorie
---

{% prerequis "**Prérequis** :" %}

* [fonctions](../fonctions)

{% endprerequis %}

<!-- début résumé -->

Les fonctions de hachage. De la définition mathématique à son utilité en informatique.

<!-- end résumé -->

## Définition

Dans notre cas, en informatique, on peut définir une [fonction de hachage](https://fr.wikipedia.org/wiki/Fonction_de_hachage) $f$ comme étant :

{% note "**Définition :**" %}
Une ***fonction de hachage*** est une fonction $f$ :

<div>
$$
f: \mathbb{N} \rightarrow [0 \mathrel{ {.}\,{.} } m]
$$
</div>

où $m$  est un entier positif.
{% endnote %}

Une définition alternative, également souvent utilisée, est :

{% note "**Définition :**" %}
Une ***fonction de hachage*** est une fonction $f$  qui associe à tout mot de $\\{0, 1\\}^\star$ un mot de $\\{0, 1\\}^k$.

Avec $k$  est un entier positif.
{% endnote %}

Enfin, comme tout en informatique est codé comme une suite de 0 et de 1, une fonction de hachage peut ainsi être vue comme :

{% note "**Définition :**" %}
Une ***fonction de hachage*** est une fonction qui associe à tout **objet** soit :

* un entier entre 0 et $m$
* un mot de $\\{0, 1\\}^k$ ($k > 0$)

{% endnote %}

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

{% info %}
Remarquez que la fonction de hash utilisée dépend du type d'objet.

De plus, comme un hash est défini à la création d'un objet, il n'existe pas de hash pour des objet mutable en python. Ainsi `hash([])`{.language-} produira une erreur (`TypeError: unhashable type: 'list'`).
{% endinfo %}

La principale raison de l'utilisation des fonctions de hachage est :

{% note %}
Si $f$ est une fonction de hachage, alors :

$$
f(a) \neq f(b) \Rightarrow a \neq b
$$

{% endnote %}

Une fonction de hachage permet de partitionner les entiers (*ie.* les objets) en $m+1$ classes. Pour que ce partitionnement soit utile, on demande à une *bonne* fonction de hachage d'avoir en plus les propriétés suivantes :

{% note %}

Pour qu'une fonction de hachage $f: \mathbb{N} \rightarrow [0\mathrel{ {.}\,{.} } m]$ soit ***utile***, elle doit avoir les 3 propriétés suivantes :

1. elle doit être **déterministe** : un même message doit toujours avoir la même valeur de hachage.
2. elle doit être **facilement calculable**
3. elle doit être  **uniforme** : la probabilité que $f(a) = i$ doit être de $\frac{1}{m+1}$ pour tout $a\in \mathcal{N}$ et $0 \leq i \leq m$

{% endnote %}

## Exemples

### Une constante

La fonction constante :

<div>
$$
\begin{array}{ccccc}
f & : & \mathbb{N} & \to & [0\mathrel{ {.}\,{.} } m] \\
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
f & : & \mathbb{N} & \to & [0\mathrel{ {.}\,{.} } m] \\
 & & x & \mapsto & f(x) = x \mod m \\
\end{array}
$$
</div>

est une fonction de hachage.

Sous certaines conditions, elle respecte bien les 3 propriétés d'une fonction de hachage utile.

#### Déterministe

Comme $a \mod m$  est égal au reste de la division entière de $a$ par $m$ son calcul est bien déterministe.

#### Facilement calculable

Même lorsque les objets deviennent grand, le calcul du modulo peut se faire aisément. En effet le fait que :

* $(a + b) \mod m$ = $((a \mod m) + (b\mod m)) \mod m$
* $(a \times b) \mod m$ = $((a \mod m) \times (b\mod m)) \mod m$

Par exemple :

* $7 \mod 3 = (4 \mod 3) + (3 \mod 3) = 1 + 0 = 1$
* $4 \times 3 \mod 3 = (4 \mod 3) \times (3 \mod 3) = 1 \times 0 = 0$

Ce qui permet de calculer le modulo *par morceau*.

Per exemple, prenons un objet $n$, qui est représenté en mémoire par une suite de $k \times l$ $0$ et $1$ :

<div>
$$
n = \underbracket{0 \cdots 1}_{k \times l}
$$
</div>

On peut alors le découper en paquets de $k$ bits (souvent $k = 256$) :

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
& & \sum_{i=0}^l n_i2^{ki}
\end{array}
$$
</div>

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

#### Equiprobable

Si les nombres à hacher sont pris aléatoirement, le modulo est bien uniforme quelque soit $m$.

Attention cependant :

$$
(k \times p) \mod (p \times q) = (k \mod q) \times p
$$

Les nombres qui ont un diviseur commun avec $m$ seront hachés par un nombre qui est un multiple de ce diviseur !
De là, si l'ensemble de nombre que l'on a à hacher n'est pas uniforme mais admets des diviseurs commun, ce qui arrive souvent, la probabilité de hachage ne sera pas uniforme.

Pour palier ce problème :

{% note %}
Si l'on utilise le modulo comme fonction de hachage, il est recommandé d'utiliser un nombre $m$ premier.
{% endnote %}

#### Hash de structures composées

Par exemple considérons le tuple suivant : `(1, 'un', 3.14)`{.language-}. Il contient 3 types de données différents. On pourrait très bien utiliser sa représentation binaire et faire le hash de cet objet mais, souvent, ce n'est pas cette approche qui est utilisée. On préfère combiner les hash des des différents types d'objets en un hash unique.

En java par exemple, une façon classique de procéder est de :

```text
res = 0
pour chaque élément e du tuple:
    res = hash(31 * res + hash(e))

```

Ceci assure :

* d'avoir un hash facile à calculer si le chaque de chaque élément l'est
* de ne pas avoir de soucis de diviseurs (voir le soucis du modulo) grâce à la multiplication par 31 qui va *mélanger* le tout à chaque fois

## Collisions

{% note "**Définition :**" %}
Une ***collision*** pour une fonction de hachage $h$ est deux nombre $a$ et $b$ telle que $f(a) = f(b)$
{% endnote %}

Le but est — bien sûr — de minimiser les collisions.

{% note "**Proposition**" %}
Pour une fonction de hachage $f: \mathbb{N} \rightarrow [0 \mathrel{ {.}\,{.} } m]$ uniforme, la probabilité $\bar{p}(n, m)$ de tirer $n > 1$ nombres au hasard sans avoir de collisions est de :

$$
\bar{p}(n, m) = \prod_{i=1}^{n-1}(1-\frac{i}{m+1})
$$

{% endnote %}
{% details "preuve" %}

A chaque fois que l'on tire un nombre au hasard, il faut que son hash soit différent de ceux des tirages précédents. Au $i$ème essai il y a donc une probabilité de $\frac{i-1}{m+1}$ de tomber sur un hash déjà vu et une probabilité de $1-\frac{i-1}{m+1}$ d'en obtenir un nouveau.

{% enddetails %}

On peut en extraire des solutions approchées si $m$ est très grand devant $n$ :

{% note  "**Proposition**" %}
Si $m$ est grand devant $n$, on a :

$$
\bar{p}(n, m) \simeq \exp(-\frac{n^2}{2(m+1)})
$$

et donc :

$$
n \simeq \sqrt{2(m+1)\ln(\frac{1}{\bar{p}(n, m)})}
$$

{% endnote %}
{% details "preuve" %}

<div>
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
</div>

La dernière égalité nous nonne aisément la deuxième égalité à prouver, et en repassant aux exponentielle on en déduit aussi la première égalité.

{% enddetails %}

Ces inégalités permettent par exemple de calculer le nombre d'étudiants qu'il faut avoir dans une classe pour avoir 50% de chances d'avoir deux dates d'anniversaires identiques. Ce résultat est connu sous le nom de [paradoxe des anniversaires](https://fr.wikipedia.org/wiki/Paradoxe_des_anniversaires), car le nombre de 23 ($\sqrt{2\times 365 \ln(1/.5)} \simeq 22.5$) semble très petit.

Si l'on prend un exemple réaliste de fonction de hash, par exemple celle utilisée par [git](https://fr.wikipedia.org/wiki/Git), qui rend un mot de $\\{0, 1\\}^{160}$ (git utilise la fonction de hachage [sha-1](https://fr.wikipedia.org/wiki/SHA-1)), il faudrait avoir un nombre de tirage de :

$$
n = \sqrt{2\times 2^{160}\ln(\frac{1}{.5})} \simeq 2^{80}
$$

Pour avoir 50% de chance d'obtenir une collision. Ce qui fait tout de même un sacré paquet !

## Utilisation

On l'a vue, si la taille du hachage est grand, il faut a priori un grand nombre d'objet pour espérer avoir une collision. C'est pourquoi on considère souvent que :

{% note %}
*En pratique* une fonction de hachage utile est une **injection** de l'ensemble des objets utilisés dans le programme dans $[0 \mathrel{ {.}\,{.} } m]$ ou $\\{0, 1\\}^k$  selon la fonction utilisée
{% endnote %}

Cette propriété permet d'utiliser les fonctions de hachage pour :

* proposer des résumés d'un objet (c'est comme ça que git stocke ses objets) : deux objets sont considérés identiques si'l ont le même hash, ce qui est bien plus rapide que de comparer bit à bit les 2 objets.
* créer des structures de données avancées comme les dictionnaires

Les fonctions de hachages sont même utilisées pour stocker les mots de passe sur votre ordinateur, mais pour que ne soit pas (ou très difficilement) piratable, il faut utiliser des fonctions de hachage dites *cryptographique*.

## Hash cryptographique

Les fonctions de hash sont très utilisée en cryptographie. Pour être robuste, elles doivent cependant avoir [des propriétés spécifiques](https://fr.wikipedia.org/wiki/Fonction_de_hachage_cryptographique) :

{% note "**Définition :**" %}

Une ***fonction de hachage cryptographique*** dot avoir les propriétés suivantes :

1. elles doivent être utiles (déterministe, facilement calculable et uniforme)
2. une petite modification de l'entrée doit produire une grosse modification du hash
3. en connaissant une valeur de hash $x$ il est très difficile de retrouver un $a$ tel que $f(a) = x$
4. en connaissant $a$ il est très difficile de trouver $b \neq a$ tel que $f(b) = f(a)$

{% endnote %}

En cryptographie, **très difficile** signifie que le temps pour le faire doit être supérieure à la durée de vie (l'utilité) du message.

Ici l'utilité réside dans le fait qu'en pratique :

* la fonction de hash est une injection
* il est impossible de trouver un objet ayant un hash donné.

La fonction de hash ($f$) peut alors être utilisée comme une serrure ($x$) qui ne s'ouvre que si l'on a la bonne clé (un $a$ tel que $f(a) = x$).

Craquer une fonction hash cryptographique revient soit :

* à pouvoir trouver 2 éléments $a$ et $a'$ tels que $f(a) = f(a')$ : trouver des collision montrerait que la fonction n'est pas injective et donc $a$ n'est pas une clé unique
* pouvoir trouver $a$ tel que $f(a) = x$ en ne connaissant que $x$ : revient à forger une clé en ne connaissant que la serrure.

### Comment

Plusieurs méthode de hash cryptographique existent. On peut en citer deux, issues de sha :

* [sha-1](https://fr.wikipedia.org/wiki/SHA-1) utilisé par git mais plus trop de façon cryptographique
* SHA256 (protocole [sha-2](https://fr.wikipedia.org/wiki/SHA-2))

{% info %}
On recommande actuellement d'utiliser l'algorithme SHA256 ou SHA512 pour un usage cryptographique.
{% endinfo %}

Ils sont directement utilisable :

* [sous mac](https://fre.applersg.com/check-sha1-checksum-mac-os-x) et [linux](https://www.lojiciels.com/quest-ce-que-shasum-sous-linux/) avec le programme `shasum`
* [sous windows](https://lecrabeinfo.net/verifier-integrite-calculer-empreinte-checksum-md5-sha1-sha256-fichier-windows.html) avec la commande [Get-FileHash](module) sous powershell.

### Exemple d'utilisation

#### Vérification de l'intégrité d'un fichier

Si l'on connaît le hash d'un fichier et qu'il est impossible de le modifier en conservant le même hash. On peut être sur qu'un fichier n'a pas été modifié. Dans ce cadre là, on appelle cette valeur de hash le [checksum ou somme de contrôle](https://fr.wikipedia.org/wiki/Somme_de_contr%C3%B4le)

#### Stockage des mots de passes

Les mots de passe d'un système son normalement stockés sous la forme d'un hash, auquel on ajoute un *sel* aléatoire. Voir par exemple [ce post de blog](https://patouche.github.io/2015/03/21/stocker-des-mots-de-passe/) qui vous explique un peu comment tout ça fonctionne.
