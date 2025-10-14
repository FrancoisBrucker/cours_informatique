---
layout: layout/post.njk

title: Sémantiquement sécurisé

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La sécurité d'une méthode de chiffrement va dépendre, certes de la méthode employée, mais surtout du temps et des moyens mis en œuvre par l'attaquant.

En effet on a vu que seule une clé égale à la taille du message pouvait garantir [une confidentialité parfaite](../../chiffre-vernam/#confidentialité-parfaite){.interne}, or ceci est irréalisable en pratique puisque deux ordinateurs doivent pouvoir communiquer de façon sécurisée sans s'être au préalable rencontré : toute méthode réaliste de chiffrement va laisser fuiter de l'information.

Enfin comme la taille des clés est finie un algorithme brute force arrivera toujours _in fine_ à casser décrypter le message chiffré. Selon les moyens et les personnes impliquées (d'un adolescent dans sa chambre à un état) cela pourra prendre plus ou moins de temps.

## Sécurisé en temps

{% note "**Définition**" %}
Une méthode de chiffrement est **_$(t, \epsilon)$-sécurisée_** si tout algorithme passant $t$ secondes à résoudre le problème ne peut réussir à résoudre le problème avec une probabilité supérieure à $0\leq \epsilon \leq 1$.
{% endnote  %}

L'intérêt de la $(t, \epsilon)$-sécurité est qu'elle peut se mesurer expérimentalement. Par exemple si un algorithme brute force teste le déchiffrement pour toutes les clés de taille $s$ possibles et met $t$ secondes pour en tester une, sa probabilité de réussite au bout de $T$ seconde sera de $T \cdot (t/2^s)$. Ceci nous donne une borne maximum pour toute méthode de chiffrement :

{% attention "**À retenir**" %}
Toute méthode de chiffrement avec une clé de $s$ bit est au mieux $(t, \frac{t}{2^s})$-sécurisée avec $t$ le temps mis pour déchiffrer un message.
{% endattention  %}

Il est crucial de garder ceci en tête pour toujours vérifier que la méthode brute force ne soit pas utilisable en pratique. Pour cela on commence par déterminer la durée de vie du message chiffré :

{% exercice %}
Quelle taille de clé faut-il avoir pour qu'un algorithme brute force tournant pendant 35 ans ne puisse avoir qu'une chance en 100 siècles de déchiffrer un message ?
{% endexercice %}
{% details "corrigé" %}
100 siècles vaut environ $2^{39}$ secondes et 35 ans environ $2^{30}$ secondes. on veut donc que notre méthode soit : $(2^{30}, 2^{-39})$-sécurisée.

L'algorithme étant brute force, on a : $2^{-39} = \frac{2^{30}}{2^s}$ ce qui donne $s = 69$.

Attention, les algorithmes tournent souvent en parallèle pour diminuer leur temps de calcul. C'est pourquoi, actuellement, on recommande des tailles de clés d'au moins 128bits.
{% enddetails %}

La notion de $(t, \epsilon)$-sécurité est indissociable de l'algorithme qui décrypte et donc de sa complexité. Si l'algorithme est polynomial le ratio entre ce qu'il peut tester (de l'ordre de $\mathcal{O}(n^k)$) et l'espace à tester (de l'ordre de $\mathcal{O}(2^n)$) va très rapidement tendre vers $0$ ($10/2^{10}$ vaut déjà $10^{-3}$) et si l'algorithme est exponentiel il prendra rapidement trop de temps.

## Paramètre de sécurité

Lorsque l'on calcule la complexité des algorithmes de décryptage on le fait (comme toujours) par rapports à la taille de ses entrées. Les entrées correspondent aux différents paramètres de la méthode de chiffrement :

{% note "**Définition**" %}
Pour calculer une complexité, il faut connaître la taille de l'entrée, c'est à dire les informations données à l'adversaire.

De façon classique, la taille de cette entrée ($n$), nommé **_paramètre de sécurité_**, consiste en la taille de la clé (valant $s$) plus la taille du message à chiffrer (valant $t$) :

<div>
$$
n \coloneqq s+t
$$
</div>

{% endnote %}

Ce paramètre de sécurité permet d'exprimer la $(t, \epsilon)$-sécurité non plus en fonction du temps, mais comme un nombre d'opération. Tout comme le passage de la complexité temporelle (mesurable) à la complexité en nombre d'opérations (calculable) permet une étude plus théorique des performances d'un algorithme, le paramètre de sécurité va nous permettre de comparer les algorithme de déchiffrement de façon générale et abstraite.

Par exemple l'algorithme brute force pour lequel on ne lui accorde qu'un nombre d'exécution polynomial, disons $\mathcal{O}(s^d)$, aura un avantage de $\epsilon(s) = \frac{1}{2^{s-d}}$ qui devient exponentiellement petit lorsque la taille de la clé $s$ augmente !

L'augmentation de la taille des clés va certes avoir un effet sur le temps d'exécution mais ce sera surtout sur l'avantage que cela se fera sentir, s'il est exponentiellement petit par rapport au paramètre de sécurité :

{% exercice %}
On suppose que l'exécution d'un adversaire de complexité temporelle (en secondes) $n^3$ ait un avantage de $\min(1, \frac{2^{40}}{2^n})$.

Pour $n=40$, combien faut-il de temps pour qu'il puisse décrypter la méthode de façon certaine ? Quel est son avantage pour $n=50$ et en combien de temps s'exécute-t-il ?
{% endexercice %}
{% details "corrigé" %}

Pour $n=40$, il aura besoin de $40^3$ secondes pour s'exécuter, c'est à dire un peut moins de 18 heures, et son avantage de sera de 1.

Pour $n=40$, il aura besoin de $50^3$ secondes pour s'exécuter, c'est à dire un peut moins de 35 heures, mais son avantage ne sera plus que de $10^{-3}$.
{% enddetails %}

Autre exemple, où la vitesse de calcul ne bénéficie pas forcément à l'adversaire :

{% exercice %}
Supposons qu'une méthode de chiffrement se chiffre et se déchiffre en $n^2$ opérations et qu'un adversaire possède un algorithme en $n^4$ pour le décrypter.

Soit $n=50$. Si l'on prend un ordinateur qui va 16 fois plus vite, quelle est la taille de $n$ que l'on peut se permettre en gardant le même temps de chiffrement ? Que s'est-il passé pour l'adversaire ?
{% endexercice %}
{% details "corrigé" %}

On cherche $n'$ tel que : $16\cdot 50^2 = n'^2$, c'est à dire $n' = 200$. On a pu augmenter le paramètre de sécurité de 4.

Pour l'adversaire, c'est moins profitable puisque son temps d'exécution est multiplié par $200^4/50^4 = 256$.
{% enddetails %}

Cette méthode permet de formaliser :

- l'utilisation de clés assez grandes pour que l'attaque brute force nécessite un temps exponentiel non réalisable
- l'utilisation d'adversaires dont les algorithmes de décryptage sont polynomiaux,
- que donner de l'information à un attaquant est acceptable s'il est exponentiellement petit par rapport à la taille de la clé.

C'est cette dernière notion que nous allons maintenant formaliser.

{% attention "**À retenir**" %}

1. un adversaire motivé et ayant du temps pourra toujours décrypter un message
2. on peut être en sécurité assez longtemps si la seule attaque possible est l'attaque brute force
3. La méthode de chiffrement utilisée doit être rapide : c'est un algorithme efficace

Il n'est donc pas possible d'être sécurisé pour toujours, mais on peut tenter de garante d'être en sécurité assez longtemps.

{% endattention %}

## <span id="sémantiquement-sécurisé"></span>Sémantiquement Sécurisée

{% lien %}

- [semantically secure](https://en.wikipedia.org/wiki/Semantic_security)
- [fonction négligeable](https://en.wikipedia.org/wiki/Negligible_function)

{% endlien %}

Commençons par définir une fonction négligeable :

{% note "**Définition**" %}
Une fonction $f(n)$ est **_négligeable_** si $f(n) = \mathcal{O}(1/n^d)$ pour tout entier $d$.
{% endnote %}
{% info %}
On peut de façon équivalente dire que $f(n)$ est négligeable si $f(n)n^d$ tend vers 0 en plus l'infini pour tout $d$.
{% endinfo %}

L'intérêt de cette formalisation est que négligeabilité se compose tout comme la polynômialité (somme et produit de polynôme restent des polynômes) :

- $p(n) \cdot \epsilon(n)$ reste négligeable si $\epsilon(n)$ l'est
- $\epsilon(n) + \epsilon(n)'$ reste négligeable si $\epsilon(n)$ et $\epsilon(n)'$ le sont
- $\epsilon(n) \cdot \epsilon(n)'$ reste négligeable si $\epsilon(n)$ et $\epsilon(n)'$ le sont

Si on ne possède que des fonctions négligeable pour décrypter un code on ne peut donc pas arriver à grand chose, ce qui permet d'être en sécurité :

{% note "**Définition**" %}
Une méthode de chiffrement est **_sémantiquement sécurisée_** (_Semantically secured_) si elle est $(1, f(n))$-sécurisé avec $f(n)$ une fonction négligeable.
{% endnote %}

La définition précédente nous permet de définir un cadre pour construire une méthode de chiffrement sécurisée :

{% attention "**À retenir**" %}

On supposera toujours pour la suite que :

- les adversaires n'ont à leurs dispositions que des algorithmes **_efficaces_**, c'est à dire polynomiaux
- qu'on ne veut consentir qu'une possibilité de réussite **_négligeable_**

{% endattention %}

## Avantage

La sécurité sémantique stipule qu'une méthode doit être sécurisé quelque soit l'algorithme efficace utilisé. Pour obtenir ce genre de résultat sans connaître tous les algorithmes possibles on utilise une modélisation statistique cherchant à mesurer l'écart entre la distribution produite par la méthode et la loi uniforme.

Classiquement ceci se formalise par la modélisation sous la forme d'un jeu.

### <span id="jeu-reconnaissance"></span>Jeu de la reconnaissance

{% lien %}
[Indistinguabilité calculatoire](https://fr.wikipedia.org/wiki/Indistinguabilit%C3%A9_calculatoire)
{% endlien %}

La confidentialité peut s'écrire sous la forme d'un _jeu_ à deux joueurs :

- un **_adversaire_** qui essaie de trouver une information
- un **_testeur_** qui fournit des données à l'adversaire.

L'adversaire doit choisir parmi deux réalisations, la première issue d'une variable aléatoire $x \xleftarrow{D0} \\{0, 1\\}^t$ et la seconde de la variable aléatoire $x \xleftarrow{D1} \\{0, 1\\}^t$.

Le schéma du jeu est alors le suivant :

```

     testeur                              adversaire
    ---------                            ------------
    |       |                            |          |
 b  |  D0   |   x tiré selon D0 si b=0   |    D0    |   A(x) = b'
--->|  D1   |   x tiré selon D1 si b=1   |    D1    | ------------->
    |       | -------------------------> |          |
    ---------                            ------------
```

Et se déroule ainsi :

1. un bit $b \in \\{0, 1\\}$ est fournit au testeur choisi de façon uniforme
2. selon $b$ choisit soit une réalisation de $x \xleftarrow{D0} \\{0, 1\\}^t$ soit de $x \xleftarrow{D1} \\{0, 1\\}^{t}$
3. le testeur envoie $x$ à l'adversaire
4. l'adversaire répond un bit $b'$, résultat d'un algorithme efficace (_ie._ polynomial)
5. l'adversaire :
   - gagne si $b = b'$
   - perd si $b \neq b'$

Ce jeu explicite le fait que toute la cryptographie se résume à savoir si la suite générée par notre méthode de chiffrement est assez proche de l'aléatoire pour que l'on ne puisse pas, en pratique, en exploiter les différences.

L'adversaire possède un **_[avantage](<https://en.wikipedia.org/wiki/Advantage_(cryptography)>)\_** si la probabilité que `A(x)=b'` coïncide avec $b$ soit supérieure à 1/2. Comme $P[b=1] = P[b=0] = 1/2$ cet avantage vaut :

{% note "**Définition**" %}
L'avantage $\epsilon(A)$ pour l'adversaire $A$ dans un jeu est défini tel que :

<div>
$$
\epsilon(A) \coloneqq | (\Pr[b' = 1 \;\mid\; b = 1] + \Pr[b' = 0 \;\mid\; b = 0]) - 1 |
$$
</div>

{% endnote %}

Si l'adversaire $A$ n'a pas d'idée de comment gagner au jeu, il peut toujours répondre au hasard : au pire il a 50% de chance de gagner et $\epsilon(A) = 0$. Au contraire s'il ne se trompe jamais son avantage vaut $\epsilon(A) = 1$.

Pour se fixer les idée commençons par un exemple. On suppose que l'on cherche à différentier deux mots de $\\{0, 1\\}^t$, le premier issu a distribution constante de réalisation $\mathbb{0}$ ($D0$), le second d'une loi uniforme ($D1$). Comme :

- la probabilité d'obtenir n'importe quel mot de $\\{0, 1\\}^t$ vaut $1/2^t$ pour la loi uniforme,
- la probabilité d'obtenir $\mathbb{0}$ vaut 1 pour la fonction constante

On peut utiliser l'algorithme efficace $A$ suivant :

- $A(x)=0$ si $x=\mathbb{0}$
- $A(x)=1$ sinon

Dont l'avantage vaut :

<div>
$$
\begin{array}{lcl}
\epsilon(A) &=& |\Pr[x \neq \mathbb{0} \;\mid\; b=1] + \Pr[x = \mathbb{0} \;\mid\; b=0] - 1|\\
\end{array}
$$
</div>

Comme la seule façon de se tromper si $b=1$ est lorsque le mot $\mathbb{0}$ est tiré avec une probabilité $1/2^t$ et que l'on ne se trompe jamais si $b=0$ on a :

<div>
$$
\begin{array}{lcl}
\epsilon(A) &=& |\Pr[x \neq \mathbb{0} \;\mid\; b=1] + \Pr[x = \mathbb{0} \;\mid\; b=0] - 1|\\
&=& | (1-1/2^t) + 1 - 1\\
&=& 1-1/2^t\\
\end{array}
$$
</div>

On est presque toujours assuré de gagner !

Le corollaire ci-après montre que l'avantage est également la différence entre gagner ou perdre en choisissant tout le temps $D0$ ou $D1$. C'est cette définition que nous utiliserons dans tous les autres jeux que nous définirons :

{% note "**Corollaire**" %}
Si $D0$ est traité de façon équivalente à $D1$ dans l'algorithme $A$, on a :

<div>
$$
\begin{array}{lcl}
\epsilon(A) &=& \vert \Pr[b' = 1 \;\mid\; b = 1] - \Pr[b' = 1 \;\mid\; b = 0] \vert\\
&=& \vert \Pr[b' = 0 \;\mid\; b = 0] - \Pr[b' = 0 \;\mid\; b = 1] \vert\\
\end{array}
$$
</div>

Et ainsi :

<div>
$$
\begin{array}{lcl}
\epsilon(A) &=& \vert \Pr_{x \xleftarrow{D1} \{0, 1\}^t}[A(x) = 1 ] - \Pr_{x \xleftarrow{D0} \{0, 1\}^t}[A(x) = 1 ] \vert\\
&=& \vert \Pr_{x \xleftarrow{D0} \{0, 1\}^t}[A(x) = 1 ] - \Pr_{x \xleftarrow{D1} \{0, 1\}^t}[A(x) = 1 ] \vert\\
\end{array}
$$
</div>


{% endnote %}
{% details "preuve", "open" %}

<div>
$$
1/2\cdot \Pr[b'=0 \;\mid\; b=0] + 1/2\cdot \Pr[b'=1 \;\mid\; b=1] +1/2\cdot  \Pr[b'=0 \;\mid\; b=1] + 1/2\cdot \Pr[b'=1 \;\mid\; b=0]  = 1
$$
</div>

La probabilité de gagner vaut $\Pr[b'=b] = 1/2\cdot \Pr[b'=0 \\;\mid\\; b=0] + 1/2\cdot \Pr[b'=1 \\;\mid\\; b=1] = 1/2 +\epsilon(A)/2$ et la proba de perdre $1/2 - \epsilon(A)/2$
Du coup :

<div>
$$
\Pr[b'=1 \;\mid\; b=1] - \Pr[b'=0 \;\mid\; b=1] + \Pr[b'=0 \;\mid\; b=0] - \Pr[b'=1 \;\mid\; b=0] = 2\cdot \epsilon(A)
$$
</div>

Si $D0$ et $D1$ sont équivalent (l'algorithme répond le contraire si on inverse les deux distributions) on a $\Pr[b'=1 \\;\mid\\; b=1] - \Pr[b'=1 \\;\mid\\; b=0] = \Pr[b'=0 \\;\mid\\; b=0] - \Pr[b'=0 \\;\mid\\; b=1]$ ce qui conclut la preuve.

{% enddetails %}

Les deux lois seront dites :

- **_équivalentes_** si $D0 = D1$ : on ne peut les distinguer
- **_statistiquement sécurisés_** si le meilleur algorithme de reconnaissance ne peut obtenir qu'un avantage négligeable
- **_sémantiquement sécurisés_** si le meilleur algorithme **efficace** de reconnaissance ne peut obtenir qu'un avantage négligeable

On cherchera toujours à obtenir un comportement sémantiquement sécurisé. Ceci est facilité par la remarque ci-dessous :

{% note %}

Pour ce jeu il est facile de formaliser le meilleur algorithme possible permettant de résoudre ce problème :

- Entrée :
  - une valeur x
- Programme :
  1. calculer la probabilité p0 d'obtenir x selon la loi D0
  2. calculer la probabilité p1 d'obtenir x selon la loi D1
  3. si p0 > p1 rendre 0, sinon rendre 1

Si son avantage est négligeable, tous les adversaires, qu'ils soient efficaces ou non, n'auront également qu'un avantage négligeable.

{% endnote %}

### Jeu du chiffrement

Si l'on cherche à prouver qu'une méthode de chiffrement est sémantiquement sécurisée pour des attaques par messages choisis (_Chosen-plaintext attackers, CPA_) on peut utiliser le jeu suivant. Notez que si notre méthode de chiffrement y résiste elle sera également robuste pour les attaques plus faible (par message connu ou chiffre uniquement).

Le jeu consiste alors en 6 étapes :

1. le testeur choisit uniformément une clé $k$
2. un bit $b \in \\{0, 1\\}$ est fournit au testeur choisi de façon uniforme
3. l'adversaire **choisit** deux messages $m_0$ et $m_1$ de même taille à donner au testeur
4. le testeur renvoie à l'adversaire $E(k, m_b)$
5. l'adversaire répond un bit $b'$
6. l'adversaire :
   - gagne si $b = b'$
   - perd si $b \neq b'$

```
     testeur                      adversaire
    ---------        m0, m1      ------------
 b  |       | <----------------- |          |  A(c) = b'
--->|   k   |    E(k,mb) = c     |          | -------------------->
    |       | -----------------> |          |
    ---------                    ------------
```

Le jeu du chiffrement est un cas particulier du cas du jeu de la reconnaissance puisque l'on cherche à différentier la loi suivie par $E(k, m_0)$ de celle suivi par $E(k, m_1)$ lorsque $k$ est distribué de façon uniforme. Ce type d'attaque, bien qu'elle ne permet pas de déchiffrer les messages permet tout de même d'avoir des informations sur le type de message chiffré, par exemple si la réponse est positive (`m0 = "oui"`) ou négative (`m1 = "non"`).

Par exemple supposons que nous chiffrons/déchiffrons nos messages avec l'algorithme de Vigenère et que l'on chiffre des messages avec des clés de longueur $\vert k \vert\ = 2$. L'adversaire pourrait choisir `m0 = "aa"` et `m1 = "ab"` et décider de répondre 1 si `c[1] ≠ c[0]`. L'avantage de cet algorithme va être énorme puisque :

- $\Pr[b' = 1 \\;\mid\\; b = 1] = 1- \Pr[b' = 0 \\;\mid\\; b = 1]$. On ne peut répondre $b'=0$ alors que $b=1$ que si la lettre $a$ se chiffre avec la même lettre que $b$ ce qui arrive 26 fois (choisir la première lettre de $k$ entraîne sa deuxième). Donc $\Pr[b' = 1 \\;\mid\\; b = 1] = 1- 26/26^2 = 1-1/26$
- $\Pr[b' = 0 \\;\mid\\; b = 0] = 1$ on ne se trompe jamais si c'est `m0` qui est encodé.

Pour notre algorithme on a donc un avantage de $\epsilon(A) = 1-1/26 \geq 95\\%$ ce qui est très bon ! Attention, cela ne veut pas dire que le chiffrement de Vigenère est mauvais, juste que connaître la taille de la clé permet de reconnaître le chiffrement de messages connus.

Puisque l'adversaire peut choisir les 2 mots, il va prendre ceux ayant statistiquement le plus de différence : un avantage nul signifie que tous les mots sont équivalents :

{% exercice %}
Montrer que tout adversaire ne peut avoir un avantage différent de 0 au au jeu du chiffrement utilisant le chiffre le Vernam.
{% endexercice %}
{% details "corrigé" %}

<div>
$$
\vert \Pr[b' = 1 \;\mid\; b = 1] - \Pr[b' = 1 \;\mid\; b = 0] \vert = \vert \Pr[A(k\oplus m_1) = 1] - \Pr[A(k\oplus m_0) = 1] \vert
$$
</div>

Or $k\oplus m_1$ et $k\oplus m_0$ suivent une loi uniforme ($U$) puisque $k$ est uniforme : $\Pr[A(U) = 1] = \Pr[A(k\oplus m_1) = 1] = \Pr[A(k\oplus m_0) = 1]$ et l'avantage est bien nul quelque soit l'algorithme utilisé.
{% enddetails %}

## Construction de méthode de chiffrement

Les méthodes sémantiquement sécurisées permettent construire une méthode de chiffrement bloc par bloc : si chaque bloc est sémantiquement sécurisé l'ensemble le sera aussi. Illustrons le en montrant que l'on peut créer un chiffre de Vernam sémantiquement sécurisé en partant d'un générateur de nombre aléatoire biaisé, du moment que le biais est négligeable.

Soit la distribution de Bernoulli biaisée $B$ telle que $B(1) = 1/2 + \epsilon/2$. et $B^t$ la distribution sur $\\{0, 1\\}^t$ où chaque bit est tiré indépendamment avec $B$. On essaie de comparer cette distribution au tirage uniforme $U$. L'avantage d'un algorithme permettant de discriminer les deux distribution est alors :

### Étape 1 : génération de la clé

<div>
$$
\begin{array}{lcl}
\epsilon(A) &=&| \Pr[b'=1 \;\mid\; b=1] - \Pr[b'=1 \;\mid\; b=0] | \\
\end{array}
$$
</div>

Le meilleur algorithme, appelons-le $A$, permettant de distinguer $B^t$ et $U$ va répondre $B^t$ si $B^t(x) > (1/2)^t$ et $U$ sinon. On ne suppose pas que cet algorithme soit efficace. Si $b=1$ signifie choisir la distribution de Bernoulli biaisée alors :

<div>
$$
\begin{array}{lcl}
\Pr[b'=1 \;\mid\; b=1] &=&\sum_{x\in \{0, 1\}^t}(Pr[A(x)=1 ]\cdot B^t(x)) \\
&=& \sum_{x\in \{0, 1\}^t}\delta(x)\cdot B^t(x) \\
\end{array}
$$
</div>

Où $\delta(x) = 1$ si $B^t(x) > (1/2)^t$ et $0$ sinon. De là :

<div>
$$
\begin{array}{lcl}
\Pr[b'=1 \;\mid\; b=0] &=& 1 - \Pr[b'=0 \;\mid\; b=0]\\
&=&1- \sum_{x\in \{0, 1\}^t}(Pr[A(x)=0 ]\cdot (1/2)^t) \\
&=&1- \sum_{x\in \{0, 1\}^t}(1-\delta(x))\cdot (1/2)^t \\
\end{array}
$$
</div>

Et donc :

<div>
$$
\begin{array}{lcl}
\epsilon(A) &=& \sum_{x\in \{0, 1\}nt}[\delta(x)(B^t(x) + (1-\delta(x))\cdot (1/2)^t)] - 1 \\
&=&  \sum_{x\in \{0, 1\}^t}\max((1/2)^t, B^t(x)) - 1
\end{array}
$$
</div>

En utilisant le fait que $\max(a, b) = \frac{1}{2}\cdot (a+b+|b-a|)$ on obtient :

<div>
$$
\begin{array}{lcl}
\epsilon(A) &=&  \frac{1}{2}\sum_{x\in \{0, 1\}^t}| (1/2)^t - B^t(x) |
\end{array}
$$
</div>

Une autre astuce nous permet d'écrire tout cela de façon plus simple. On a en effet :

<div>
$$
\begin{array}{lcl}
\frac{1}{2}\sum_{x\in \{0, 1\}^t}| (1/2)^t - B^t(x) |&=&\frac{1}{2}\sum_{x\in \{0, 1\}^t}|\sum_\limits{0 < i \leq n}((1/2)^{n-i+1} - (1/2)^{n-i}B^{i}(x)) |\\
&\leq&\frac{1}{2}\sum_{x\in \{0, 1\}^t}\sum_\limits{0 < i \leq n}| ((1/2)^{n-i+1} - (1/2)^{n-i}B^{i}(x)) |\\
&\leq&\frac{1}{2}\sum_{x\in \{0, 1\}^t}\sum_\limits{0 < i \leq n}((1/2)^{n-i}B^{i-1}(x))| ((1/2)^{n-i+1} - (1/2)^{n-i}B^{i}(x)) |\\
&\leq&n\frac{1}{2^{n+1}}\sum_{x\in \{0, 1\}^t}(1/2-B(x))\\
&\leq&\frac{n}{2}\epsilon
\end{array}
$$
</div>

Si $\epsilon$ est négligeable, la génération d'éléments de $\\{0, 1\\}^t$ l'est aussi.

### Étape 2 : chiffrement

On peut utiliser ce qui précède pour créer un chiffrement statistiquement sécurisé en utilisant un chiffre de Vernam avec notre générateur aléatoire. Montrons que si $U$ est la loi uniforme sur $\\{0, 1\\}^t$ et $m$ un élément de $\\{0, 1\\}^t$, alors la loi de distribution associée à la variable aléatoire $(x \xleftarrow{B^t} \\{0, 1\\}^t) \oplus m$ est sémantiquement sécurisé.

Soit $C^t$ la loi de distribution associée à la variable aléatoire $(x \xleftarrow{B^t} \\{0, 1\\}^t) \oplus m$. Tout comme précédemment, le meilleur algorithme a comme avantage :

<div>
$$
\begin{array}{lcl}
A &=&  \frac{1}{2}\sum_{x\in \{0, 1\}^t}| (1/2)^t - C^t(x) |
\end{array}
$$
</div>

La même astuce consistant à décomposer $x=x_1\dots x_t$ et $m=m_1\dots m_t$ en indices donne :

<div>
$$
\begin{array}{lcl}
A &\leq&\frac{1}{2^{n+1}}\sum_{x\in \{0, 1\}^t}\sum_i(1/2-C_i(x_i))\\
  &\leq&\sum_i\frac{1}{2^{n+1}}\sum_{x\in \{0, 1\}^t}(1/2-C_i(x_i))
\end{array}
$$
</div>

Où $C_i(x_i)$ est la loi de distribution de $(x \xleftarrow{B} \\{0, 1\\}^t)\oplus m_i$.

Ceci donne $A\leq \frac{n}{2}\epsilon$ qui est négligeable si $\epsilon$ l'est.

### Étape 3 : jeu de la reconnaissance

On en conclut que si $m_1$ et $m_2$ sont deux éléments de $\\{0, 1\\}^t$ alors les lois de distributions associées aux variables aléatoires $(x \xleftarrow{B^t} \\{0, 1\\}^t) \oplus m_1$ et $(x \xleftarrow{B^t} \\{0, 1\\}^t) \oplus m_2$ sont statistiquement sécurisées. En effet en notant $C^t$ et $D^t$ les lois de distributions associées à $(x \xleftarrow{B^t} \\{0, 1\\}^t) \oplus m_1$ et $(x \xleftarrow{B^t} \\{0, 1\\}^t) \oplus m_2$, on aura :

<div>
$$
\begin{array}{lcl}
\epsilon(A) &=&  \frac{1}{2}\sum_{x\in \{0, 1\}^t}| D^t(x) - C^t(x) |\\
&=&  \frac{1}{2}\sum_{x\in \{0, 1\}^t}| D^t(x) -(1/2)^t + (1/2)^t - C^t(x) |\\
\epsilon(A) &\leq& \frac{1}{2}\sum_{x\in \{0, 1\}^t}| (1/2)^t - C^t(x) | + \frac{1}{2}\sum_{x\in \{0, 1\}^t}| (1/2)^t - D^t(x) |\\
&\leq& {n}\cdot\epsilon
\end{array}
$$
</div>

Comme ce calcul a été fait avec $m_0$ et $m_1$ quelconque, ce chiffrement est sémantiquement sécurisé pour des attaques de types _Chosen-plaintext attackers_.

### Conclusion

Si on fait bien les choses (on verra qu'on peut se tromper si on ne fait pas attention), on peut construire une méthode de chiffrement sémantiquement sécurisée en chaînant des blocs de biais négligeable, tout comme en algorithmie une composition d'algorithmes de complexités polynomiales reste polynomiale.

Ceci va être utilisé intensivement par la suite où l'on construira chaque bloc de la méthode de chiffrement indépendamment les une des autres : si chaque bloc ne donne qu'un avantage négligeable toute la chaîne également.
