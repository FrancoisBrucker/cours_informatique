---
layout: layout/post.njk

title: Définitions de la confidentialité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous avons démontré précédemment que le code de Vernam est inviolable sans la connaissance de la clé. Mais y en a-t-il d'autres ?

[Claude Shannon](https://en.wikipedia.org/wiki/Claude_Shannon#Information_theory), dans son article séminale de 1949 sur la théorie de l'information donne une définition d'un code assurant une confidentialité parfaite :

{% note "**Définition**" %}
Un code $(E, D)$ assure une **_confidentialité parfaite_** si pour :

- tous messages $m$ et $m'$ de même taille
- tout chiffre $c$
- les clés $k$ suivent une loi uniforme sur $\mathcal{K}$ : $k \xleftarrow{R} \mathcal{K}$

On a :

<div>
$$
Pr_{k \xleftarrow{R} \mathcal{K}}[E(k, m) = c] = Pr_{k \xleftarrow{R} \mathcal{K}}[E(k, m') = c]
$$
</div>

{% endnote %}

Un code assurant une confidentialité parfaite ne doit donner aucune information sur $k$ ou $m$ en ne sachant que $E(k, m)$, ce qui se traduit par le fait que :

- tout message peut donner un chiffre donné si on choisit la bonne clé
- et avec la même probabilité

{% note "**Théorème**" %}
Le code de Vernam assure une confidentialité parfaite.
{% endnote %}
{% details "preuve", "open" %}

La variable aléatoire $(k \xleftarrow{R} \mathcal{K}) \oplus m$ est uniforme quelque soit $m$ : la probabilité d'obtenir n'importe quel chiffre est ainsi une constante et vaut $\frac{1}{\vert \mathcal{C}\vert}$ ce qui est indépendant de $m$.

{% enddetails %}

Shannon montre cependant qu'avoir une confidentialité parfaite est trop restrictive en pratique :

{% note "**Théorème**" %}
Un code à confidentialité parfaite nécessite un nombre de clés différentes supérieure ou égale au nombre de messages à chiffrer.
{% endnote %}
{% details "preuve", "open" %}

Soit $k^{\star} \in K$, $m^{\star} \in M$ et notons $c^{\star} = E(k^{\star}, m^{\star})$. S'il existe un message $m'$ tel que $E(k, m') \neq c^\star$ quelque soit la clé $k$ alors $Pr_{k \xleftarrow{R} \mathcal{K}}[E(k, m') = c^\star] = 0 < Pr_{k \xleftarrow{R} \mathcal{K}}[E(k, m^\star) = c^\star]$ et le code ne peut être à confidentialité parfaite.

On en déduit que l'ensemble $M' = \\{m \vert E(k, m)=c^{\star}, k \in K\\}$ des messages chiffrés en $c^\star$ doit être égal à $\mathcal{M}$ et comme $\vert M' \vert \leq \vert \mathcal{K} \vert$ on a que $\vert \mathcal{M} \vert \leq \vert \mathcal{K} \vert$.

{% enddetails %}

De là, tout comme le code de Vernam, si on encode des mots de $\\{0, 1\\}^L$, il faut que la taille de la clé soit plus grande que $L$. Mais alors, si on peut se partager un secret de taille $L$, pourquoi ne pas directement se partager le message ?

Il faut donc :

1. relâcher la contrainte de confidentialité parfaite
2. assumer que l'on donnera de toute façons des informations à l'adversaire.
3. faire en sorte de quantifier la quantité d'information consentie.

## Jeu du chiffrement

La confidentialité peut s'écrire sous la forme d'un _jeu_ où si un adversaire présente deux messages et qu'on lui en rend un des deux chiffré, il ne peut déterminer lequel c'est avec ue probabilité supérieure à $1/2$.

Formalisons ce jeu à deux joueurs :

- un **_adversaire_** qui essaie de trouver une information
- un **_testeur_** qui fournit des données à l'adversaire.

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
 b  |   k   | <----------------- |          |  A(E(k,mb)) = b'
--->|       |       E(k,mb)      |          | -------------------->
    |       | -----------------> |          |
    ---------                    ------------
```

Il est clair que si l'adversaire essaie toutes les possibilités il trouvera toujours la solution (presque toujours en fait, car il peut exister des cas où `E(k,m0) = E(k', m1)`. Mais comme l'adversaire peut choisir ses mots il peut minimiser – voir supprimer ce cas). Cela prendra cependant un temps énorme. Par exemple si la clé $k$ possède 128bits, il y a $2^{128}$ possibilité et même si l'adversaire peut tester 1000 milliards de possibilités par seconde ($10^{12}$) il lui faudrait tout de même plus de $10^{17}$ siècles pour tester toutes les possibilités.

L'exemple précédent montre trois choses :

1. un adversaire motivé et ayant du temps pourra toujours déchiffrer un message
2. on peut être en sécurité assez longtemps si la seule attaque possible est l'attaque brute force
3. La méthode $A(\cdot)$ utilisé doit être rapide : c'est un algorithme

Il n'est donc pas possible d'être sécurisé pour toujours, mais on peut tenter de garante d'être en sécurité assez longtemps. Formalisons tout ça.

### Sécurité en pratique

Une méthode de chiffrement sera dite $(t, \epsilon)$-sécurisée si tout algorithme passant $t$ opérations à résoudre le problème ne peut réussir à résoudre le problème avec une probabilité supérieure à $1/2\leq \epsilon \leq 1$.

Comme l'algorithme brute force teste une clé en plus d'une opération, toute méthode de chiffrement sera au maximum $(t, \frac{t}{2^k})$-sécurisée.

{% info %}
On peut aussi mesurer le temps mis pour exécuter l'algorithme puis mesurer sa probabilité de réussite. On aura alors une sécurité définie par unité de temps.
{% endinfo %}

Il est cruciale de garde ceci en tête pour toujours vérifier que la méthode brute force ne soit pas utilisable en pratique.

> TBD exemple un ordi à 5Ghz pour 35 ans et une clé de taille 128b. Modern cryptography, exemple 3.1 p49

### Avantage Probabiliste

L'adversaire possède un **_[avantage](<https://en.wikipedia.org/wiki/Advantage_(cryptography)>)_** si la probabilité que `A(E(k,mb))=b'` coïncide avec $b$ soit supérieure à 1/2. Comme $P[b=1] = P[b=0] = 1/2$ cet avantage vaut :

{% note "**Définition**" %}
L'avantage dans ce jeu est $\epsilon$ :

<div>
$$
| (Pr[b' = 1 | b = 1] + Pr[b' = 0 | b = 0]) - 1 | = \epsilon
$$
</div>

{% endnote %}

Si l'adversaire n'a pas d'idée de comment gagner au jeu, il peut toujours répondre au hasard : au pire il a 50% de chance de gagner et $\epsilon = 0$.

Le corollaire ci-après montre que l'avantage est également la différence entre gagner ou perdre en choisissant tout le temps $m_0$ ou $m_1$. C'est cette définition que nous utiliserons dans tous les autres jeux que nous définirons.

{% note "**Corollaire**" %}
Si $m_0$ est traité de façon équivalente à $m_1$, l'avantage est aussi :

<div>
$$
\vert Pr[b' = 1 | b = 1] - Pr[b' = 1 | b = 0] \vert = \vert Pr[b' = 0 | b = 0] - Pr[b' = 0 | b = 1] \vert
$$
</div>

{% endnote %}
{% details "preuve", "open" %}

<div>
$$
1/2\cdot Pr[b'=0 | b=0] + 1/2\cdot Pr[b'=1 | b=1] +1/2\cdot  Pr[b'=0 | b=1] + 1/2\cdot Pr[b'=1 | b=0]  = 1
$$
</div>

La proba de gagner vaut $Pr[b'=b] = 1/2\cdot Pr[b'=0 | b=0] + 1/2\cdot Pr[b'=1 | b=1] = 1/2 +\epsilon/2$ et la proba de perdre $1/2 - \epsilon/2$
Du coup :

<div>
$$
Pr[b'=1 | b=1] - Pr[b'=0 | b=1] + Pr[b'=0 | b=0] - Pr[b'=1 | b=0] = 2\cdot \epsilon
$$
</div>

Si $m_0$ et $m_1$ sont équivalent on a $Pr[b'=1 | b=1] - Pr[b'=1 | b=0] = Pr[b'=0 | b=0] - Pr[b'=0 | b=1]$ ce qui conclut la preuve.

{% enddetails %}

On a clairement que :

{% note %}
Confidentialité parfaite et avantage nul au jeu du chiffrement sont deux notions équivalentes.
{% endnote %}

### Exemple du Code de Vernam

Reprenons l'exemple du code de Vernam pour montrer que quelque soit l'adversaire, son avantage vaut 0.

<div>
$$
\vert Pr[b' = 1 | b = 1] - Pr[b' = 1 | b = 0] \vert = \vert Pr[A(k\oplus m_1) = 1] - Pr[A(k\oplus m_0) = 1] \vert
$$
</div>

Or $k\oplus m_1$ et $k\oplus m_0$ suivent une loi uniforme ($U$) puisque $k$ est uniforme : $Pr[A(U) = 1] = Pr[A(k\oplus m_1) = 1] = Pr[A(k\oplus m_0) = 1]$ et l'avantage est bien nul quelque soit l'algorithme utilisé.

## Sémantiquement Sécurisée

La méthode précédente donne idée de la sécurité _actuelle_ d'une méthode de chiffrement puisqu'elle mesure le nombre d'opérations ou le temps pris pour décrypter une méthode de chiffrement. Cela ne dit rien de ce qui pourra se passer dans 5 ou 10 ans lorsque les ordinateurs iront plus vite ou que les méthodes de résolutions seront plus évoluées.

Pour tenir compte de ceci on va prendre le parti pris de la complexité algorithmique car les seuls algorithmes dépendant de la rapidité d'un ordinateurs sont ceux qui sont polynomiaux :

1. Une méthode de cryptanalyse ne peut efficacement exploiter un avantage, que si celle ci s'exécute en temps polynomial.
2. L'avantage donné par une méthode de cryptanalyse dépend de ce qu'il a à décrypter.

Par exemple l'algorithme brute force a un avantage valant $\epsilon(k+m) = \frac{m}{2^k}$ pour déchiffrer un chiffre de Vernam avec un message de taille $m$ et une clé de taille $k$.

Le nombre $n=k+m$ représente la taille de l'entrée du problème de chiffrement.

### Exemple 1

> TBD Modern cryptography, exemple 3.2 p51

### Exemple 2

Rapide peut aussi aider la défense

> TBD Modern cryptography, exemple 3.3 p51

### Définition formelle

{% lien %}

- [semantically secure](https://en.wikipedia.org/wiki/Semantic_security)
- [fonction négligeable](https://en.wikipedia.org/wiki/Negligible_function)

{% endlien %}

On suppose que :

- les adversaires n'ont à leurs dispositions que des algorithmes **_efficaces_**, c'est à dire polynomiaux
- qu'on ne veut consentir qu'un avantage **_négligeable_**

{% note "**Définition**" %}
Une fonction $f(n)$ est **_négligeable_** si $f(n) = \mathcal{O}(1/n^d)$ pour tout entier $d$.
{% endnote %}
{% info %}
On peut de façon équivalente dire que $f(n)$ est négligeable si $f(n)n^d$ tend vers 0 en plus l'infini pour tout $d$.
{% endinfo %}

De ces considérations on peut définir :

{% note "**Définition**" %}
Une méthode de chiffrement est **_sécurisée_** (_Semantically secured_) si tout algorithme efficace ne peut obtenir qu'un avantage négligeable au jeu du chiffrement.
{% endnote %}

{% lien %}
[Indistinguabilité calculatoire](https://fr.wikipedia.org/wiki/Indistinguabilit%C3%A9_calculatoire)
{% endlien %}

{% note "**Définition**" %}
Le couple $(E, D)$ d'algorithmes efficaces est une **_méthode de chiffrement sécurisée_** si :

- $D(k, E(k, m)) = m$
- tout algorithme efficace n'a qu'un avantage négligeable au jeu du chiffrement.
  {% endnote %}

La négligeabilité permet de définir théoriquement les avantages que l'on peut accepter de la part de l'adversaire. Propagation de la négligeabilité :

- $p(n) \cdot \epsilon$ reste négligeable si $\epsilon$ l'est
- $\epsilon + \epsilon'$ reste négligeable si $\epsilon$ et $\epsilon'$ le sont
- $\epsilon \cdot \epsilon'$ reste négligeable si $\epsilon$ et $\epsilon'$ le sont

### Valeurs numériques

> TBD refaire

{% note %}
L'avantage ne doit pas permettre de créer des algorithmes de cryptanalyse ayant une probabilité moyenne de gagner supérieure à 50% en les relançant $1/\epsilon$ fois.
{% endnote %}

Un avantage de $1/2^{30}$ par exemple est insuffisant. Il suffit de relancer $2^{30}$ fois notre algorithme, ce qui ne fait que un millions de fois. En **2024**, on considère que si $\epsilon \leq 1/2^{80}$, on peut se considérer **_sémantiquement sécurisé_**, car cela correspond à une attaque brute force sur une clé de taille 128b

> TBD pourquoi ? <https://www.cs.purdue.edu/homes/ninghui/courses/526_Fall13/handouts/526_topic04.pdf>

## Jeu de la reconnaissance

> TBD dire et montrer que le jeu de la sécurité est un cas particulier du jeu de la reconnaissance.

Tout le jeu en cryptographie est de savoir si la suite générée est assez proche de l'aléatoire pour que l'on ne puisse pas, en pratique, en exploiter les différences.

On peut modéliser ceci par un jeu, le jeu de la reconnaissance de deux distributions en adaptant le jeu du chiffrement.

Soient $D_i: \mathcal{U} \to [0, 1]$ pour $i \in \\{0, 1\\}$ deux lois de distribution. On cherche à distinguer si un élément de $\mathcal{U}$ a été tiré selon la loi $D_0$ ou $D_1$.

```

     testeur                              adversaire
    ---------                            ------------
 b  |   k   |                            |          |  rép(X) = b'
--->|  D0   |   X tiré selon D0 si b=0   |          | ------------->
    |  D1   |   X tiré selon D1 si b=1   |          |
    |       | -------------------------> |          |
    ---------                            ------------
```

Ce jeu généralise le jeu du chiffrement et est la base de tous les autres jeu que nous verrons en cryptographie. L'avantage de l'adversaire est, comme pour le jeu du chiffrage, défini tel que :

<div>
$$
Pr[b'=1 | b=1] - Pr[b'=1 | b=0]
$$
</div>

Les deux lois seront dites :

- **_équivalentes_** si $D_0 = D_1$ : on ne peut les distinguer
- **_statistiquement sécurisés_** si le meilleur algorithme de reconnaissance ne peut obtenir qu'un avantage négligeable
- **_sémantiquement sécurisés_** si le meilleur algorithme **efficace** de reconnaissance ne peut obtenir qu'un avantage négligeable

On cherchera toujours à obtenir un comportement sémantiquement sécurisé. Pour ce jeu
il est facile de formaliser le meilleur algorithme possible permettant de résoudre ce problème :

- Entrée :
  - un X
- Programme :
  1. calculer la probabilité p0 d'obtenir x selon la loi D0
  2. calculer la probabilité p1 d'obtenir x selon la loi D1
  3. si p0 ≥ p1 rendre 0, sinon rendre 1

Si son avantage est négligeable, tous les algorithmes auront aussi un seulement un avantage négligeable.

Prenons par exemple la distribution de Bernoulli $B$ telle que $B(1) = 1/2 + \epsilon/2$. et $B^n$ la distribution sur $\\{0, 1\\}^n$ où chaque bit est tiré indépendamment avec $B$. On essaie de comparer cette distribution au tirage uniforme de distribution de probabilité $N$.

Soit $A$ le meilleur algorithme permettant de distinguer $B^n$ et $N$. Son avantage est alors :

<div>
$$
\begin{array}{lcl}
A &=&| Pr[b'=1 | b=1] - Pr[b'=1 | b=0] | \\
&=& |\sum_{X\in \{0, 1\}^n}(Pr[A(X') = 1 | X=X']\cdot B^n(X) - Pr[A(X') = 1 | X=X']\cdot (1/2)^n)|\\
&=& |\sum_{X\in \{0, 1\}^n}(Pr[A(X') = 1 | X=X']\cdot B^n(X) + Pr[A(X') = 0 | X=X']\cdot (1/2)^n) - 1|
\end{array}
$$
</div>

Or $Pr[A(X') = 1 | X=X'] = 1$ si $B^n(X')\geq (1/2)^n$, l'avantage vaut donc :

<div>
$$
\begin{array}{lcl}
A &=&  \sum_{X\in \{0, 1\}^n}\max((1/2)^n, B^n(X)) - 1
\end{array}
$$
</div>

Et comme $\max(a, b) = \frac{1}{2}\cdot (a+b+|b-a|)$ on a au final :

<div>
$$
\begin{array}{lcl}
A &=&  \frac{1}{2}\sum_{X\in \{0, 1\}^n}| (1/2)^n - B^n(X) |
\end{array}
$$
</div>

Une autre astuce nous permet d'écrire tout cela de façon plus simple. On a en effet :

<div>
$$
\begin{array}{lcl}
\frac{1}{2}\sum_{X\in \{0, 1\}^n}| (1/2)^n - B^n(X) |&=&\frac{1}{2}\sum_{X\in \{0, 1\}^n}|\sum_\limits{0 < i \leq n}((1/2)^{n-i+1} - (1/2)^{n-i}B^{i}(X)) |\\
&\leq&\frac{1}{2}\sum_{X\in \{0, 1\}^n}\sum_\limits{0 < i \leq n}| ((1/2)^{n-i+1} - (1/2)^{n-i}B^{i}(X)) |\\
&\leq&\frac{1}{2}\sum_{X\in \{0, 1\}^n}\sum_\limits{0 < i \leq n}((1/2)^{n-i}B^{i-1}(X))| ((1/2)^{n-i+1} - (1/2)^{n-i}B^{i}(X)) |\\
&\leq&n\frac{1}{2}\sum_{X\in \{0, 1\}^n}(1/2-B(X))\\
&\leq&\frac{n}{2}\epsilon
\end{array}
$$
</div>

Si $\epsilon$ est négligeable, la génération d'éléments de $\\{0, 1\\}^n$ l'est aussi. De là, on peut alors créer un chiffrement statistiquement sécurisé en utilisant un chiffre de Vernam avec notre générateur aléatoire.

{% exercice %}
Montrez que si $U$ est la loi uniforme sur $\\{0, 1\\}^n$ et $m$ un élément de $\\{0, 1\\}^n$, alors la loi de distribution associée à la variable aléatoire $X \oplus m$ où $X$ suit la loi de $B^n$ est statistiquement sécurisé.
{% endexercice %}
{% details "corrigé" %}

Soit $C^n$ la loi de distribution associée à $X \oplus m$.

Tout comme précédemment, le meilleur algorithme a comme avantage :

<div>
$$
\begin{array}{lcl}
A &=&  \frac{1}{2}\sum_{X\in \{0, 1\}^n}| (1/2)^n - C^n(X) |
\end{array}
$$
</div>

La même astuce consistant à décomposer $X=X_1\dots X_n$ et $m=m_1\dots m_n$ en indices donne :

<div>
$$
\begin{array}{lcl}
A &\leq&\frac{1}{2}\sum_{X\in \{0, 1\}^n}\sum_i(1/2-C_i(X_i))\\
  &\leq&\sum_i\frac{1}{2}\sum_{X\in \{0, 1\}^n}(1/2-C_i(X_i))
\end{array}
$$
</div>

Où $C_i(X_i)$ est la loi de distribution de $Y\oplus m_i$ avec $Y$ généré selon $B$.

Ceci donne $A\leq \frac{n}{2}\epsilon$ qui est négligeable si $\epsilon$ l'est.

{% enddetails %}

En conclure que :

{% exercice %}
Montrez que si $m_1$ et $m_2$ sont deux éléments de $\\{0, 1\\}^n$ alors les lois de distributions associés aux variables aléatoires $X \oplus m_1$ et $X \oplus m_2$ sont statistiquement sécurisés.
{% endexercice %}
{% details "corrigé" %}
En notant $C^n$ et $D^n$ les lois de distributions associées à $X \oplus m_1$ et $X \oplus m_2$, on aura :

<div>
$$
\begin{array}{lcl}
A &=&  \frac{1}{2}\sum_{X\in \{0, 1\}^n}| D^n(X) - C^n(X) |\\
&=&  \frac{1}{2}\sum_{X\in \{0, 1\}^n}| D^n(X) -(1/2)^n + (1/2)^n - C^n(X) |\\
A &\leq& \frac{1}{2}\sum_{X\in \{0, 1\}^n}| (1/2)^n - C^n(X) | + \frac{1}{2}\sum_{X\in \{0, 1\}^n}| (1/2)^n - D^n(X) |\\
&\leq& {n}\cdot\epsilon
\end{array}
$$
</div>

{% enddetails %}

## Chiffre utilisable en pratique

La méthode de chiffrement que l'on a vu précédemment n'est pas utilisable en pratique. Déjà parce qu'un chiffrement de de Vernam nécessite une taille de clé égale au message à chiffrer, mais aussi parce qu'un générateur de nombre aléatoire, même biaisé, est compliqué car non implémentable facilement.

Pour qu'une méthode de chiffrement puisse être utilisé en pratique, il faut pouvoir avoir deux choses :

- des clés de petites tailles par rapport au message à faire passer
- des algorithmes de complexité linéaires pour chiffrer et déchiffrer les messages.

Même si on s'autorise théoriquement des algorithmes polynomiaux, en pratique, efficaces veut plutôt dire linéaire car il faut que ces algorithmes puissent chiffrer de très nombreuses données. Efficace prend donc deux significations différentes, selon que l'on cherche à prouver théoriquement des résultats où que l'on veuille en pratique chiffrer des données. L'un ne va cependant pas sans l'autre.

Ces deux contraintes vont forcément nous faire passer des informations à l'adversaire. Selon le type d'information que l'on ne veut pas divulguer on va utiliser une méthode plutôt qu'une autre.
