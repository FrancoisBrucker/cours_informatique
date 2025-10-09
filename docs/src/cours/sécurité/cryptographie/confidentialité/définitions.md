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
- les clés $k$ suivent une loi uniforme $k \xleftarrow{U} \mathcal{K}$

On a :

<div>
$$
\Pr_{k \xleftarrow{U} \mathcal{K}}[E(k, m) = c] = \Pr_{k \xleftarrow{U} \mathcal{K}}[E(k, m') = c]
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

La variable aléatoire $(k \xleftarrow{U} \mathcal{K}) \oplus m$ est uniforme quelque soit $m$ : la probabilité d'obtenir n'importe quel chiffre est ainsi une constante et vaut $\frac{1}{\vert \mathcal{C}\vert}$ ce qui est indépendant de $m$.

{% enddetails %}

Shannon montre cependant qu'avoir une confidentialité parfaite est trop restrictive en pratique :

{% note "**Théorème**" %}
Un code à confidentialité parfaite nécessite un nombre de clés différentes supérieur ou égal au nombre de messages à chiffrer.
{% endnote %}
{% details "preuve", "open" %}

Soit $k^{\star} \in \mathcal{K}$, $m^{\star} \in \mathcal{M}$ et notons $c^{\star} = E(k^{\star}, m^{\star})$. S'il existe un message $m'$ tel que $E(k, m') \neq c^\star$ quelque soit la clé $k$ alors $\Pr_{k \xleftarrow{U} \mathcal{K}}[E(k, m') = c^\star] = 0 < \Pr_{k \xleftarrow{U} \mathcal{K}}[E(k, m^\star) = c^\star]$ et le code ne peut être à confidentialité parfaite.

On en déduit que l'ensemble $\mathcal{M}' = \\{m \vert E(k, m)=c^{\star}, k \in \mathcal{K}\\}$ des messages chiffrés en $c^\star$ doit être égal à $\mathcal{M}$ et comme $\vert \mathcal{M}' \vert \leq \vert \mathcal{K} \vert$ on a que $\vert \mathcal{M} \vert \leq \vert \mathcal{K} \vert$.

{% enddetails %}

De là, tout comme le code de Vernam, si on encode des mots de $\\{0, 1\\}^t$, il faut que la taille de la clé soit plus grande que $L$. Mais alors, si on peut se partager un secret de taille $L$, pourquoi ne pas directement se partager le message ?

Il faut donc :

1. relâcher la contrainte de confidentialité parfaite
2. assumer que l'on donnera de toute façons des informations à l'adversaire.
3. faire en sorte de quantifier la quantité d'information consentie.

{% lien %}
De nombreux exemples et preuves sont tirées du livre suivant, que tout informaticien désireux d'avoir des connaissances théoriques sur la cryptanalyse devrait avoir :

[Introduction to modern cryptography](https://www.cs.umd.edu/~jkatz/imc.html)
{% endlien %}

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

> TBD donner type d'attaque chosen text. Dre que si ça résiste à ça on résiste à plein d'attaques

Il est clair que si l'adversaire essaie toutes les possibilités il trouvera toujours la solution (presque toujours en fait, car il peut exister des cas où `E(k,m0) = E(k', m1)`. Mais comme l'adversaire peut choisir ses mots il peut minimiser – voir supprimer ce cas). Cela prendra cependant un temps énorme. Par exemple si la clé $k$ possède 128bits, il y a $2^{128}$ possibilité et même si l'adversaire peut tester 1000 milliards de possibilités par seconde ($10^{12}$) il lui faudrait tout de même plus de $10^{17}$ siècles pour tester toutes les possibilités.

L'exemple précédent montre trois choses :

{% attention "**À retenir**" %}

1. un adversaire motivé et ayant du temps pourra toujours déchiffrer un message
2. on peut être en sécurité assez longtemps si la seule attaque possible est l'attaque brute force
3. La méthode $A(\cdot)$ utilisé doit être rapide : c'est un algorithme

Il n'est donc pas possible d'être sécurisé pour toujours, mais on peut tenter de garante d'être en sécurité assez longtemps.

{% endattention %}

Formalisons tout ça.

### Sécurité en pratique

Une méthode de chiffrement sera dite $(t, \epsilon)$-sécurisée si tout algorithme passant $t$ secondes à résoudre le problème ne peut réussir à résoudre le problème avec une probabilité supérieure à $0\leq \epsilon \leq 1$.

Comme l'algorithme brute force teste une clé en plus d'une opération, toute méthode de chiffrement sera au maximum $(t, \frac{t}{2^s})$-sécurisée où $s$ est la taille de la clé et $t$ le temps mis pour tester une clé.

{% info %}
On peut aussi mesurer le nombre d'opérations mis pour exécuter l'algorithme puis mesurer sa probabilité de réussite. On aura alors une sécurité définie par nombre d'opérations effectuées.
{% endinfo %}

Il est crucial de garder ceci en tête pour toujours vérifier que la méthode brute force ne soit pas utilisable en pratique.

{% exercice %}

Quelle taille de clé faut-il avoir pour qu'un algorithme brute force tournant pendant 35 ans ne puisse avoir qu'une chance en 100 siècles de déchiffrer un message ?
{% endexercice %}
{% details "corrigé" %}
100 siècles vaut environ $2^{39}$ secondes et 35 ans environ $2^{30}$ secondes. on veut donc que notre méthode soit : $(2^{30}, 2^{-39})$-sécurisée.

L'algorithme étant brute force, on a : $2^{-39} = \frac{2^{30}}{2^s}$ ce qui donne $s = 69$.

Attention, les algorithmes tournent souvent en parallèle pour diminuer leur temps de calcul. C'est pourquoi, actuellement, on recommande des tailles de clés d'au moins 128bits.
{% enddetails %}

### Avantage Probabiliste

L'adversaire possède un **_[avantage](<https://en.wikipedia.org/wiki/Advantage_(cryptography)>)_** si la probabilité que `A(E(k,mb))=b'` coïncide avec $b$ soit supérieure à 1/2. Comme $P[b=1] = P[b=0] = 1/2$ cet avantage vaut :

{% note "**Définition**" %}
L'avantage $\epsilon(A)$ pour l'adversaire $A$ dans un jeu est défini tel que :

<div>
$$
\epsilon(A) \coloneqq | (\Pr[b' = 1 \;\mid\; b = 1] + \Pr[b' = 0 \;\mid\; b = 0]) - 1 |
$$
</div>

{% endnote %}

Si l'adversaire $A$ n'a pas d'idée de comment gagner au jeu, il peut toujours répondre au hasard : au pire il a 50% de chance de gagner et $\epsilon(A) = 0$. Au contraire s'il ne se trompe jamais son avantage vaut $\epsilon(A) = 1$.

Le corollaire ci-après montre que l'avantage est également la différence entre gagner ou perdre en choisissant tout le temps $m_0$ ou $m_1$. C'est cette définition que nous utiliserons dans tous les autres jeux que nous définirons.

{% note "**Corollaire**" %}
Si $m_0$ est traité de façon équivalente à $m_1$, On a :

<div>
$$
\epsilon(A) = \vert \Pr[b' = 1 \;\mid\; b = 1] - \Pr[b' = 1 \;\mid\; b = 0] \vert = \vert \Pr[b' = 0 \;\mid\; b = 0] - \Pr[b' = 0 \;\mid\; b = 1] \vert
$$
</div>

{% endnote %}
{% details "preuve", "open" %}

<div>
$$
1/2\cdot \Pr[b'=0 \;\mid\; b=0] + 1/2\cdot \Pr[b'=1 \;\mid\; b=1] +1/2\cdot  \Pr[b'=0 \;\mid\; b=1] + 1/2\cdot \Pr[b'=1 \;\mid\; b=0]  = 1
$$
</div>

La proba de gagner vaut $\Pr[b'=b] = 1/2\cdot \Pr[b'=0 \;\mid\; b=0] + 1/2\cdot \Pr[b'=1 \;\mid\; b=1] = 1/2 +\epsilon(A)/2$ et la proba de perdre $1/2 - \epsilon(A)/2$
Du coup :

<div>
$$
\Pr[b'=1 \;\mid\; b=1] - \Pr[b'=0 \;\mid\; b=1] + \Pr[b'=0 \;\mid\; b=0] - \Pr[b'=1 \;\mid\; b=0] = 2\cdot \epsilon(A)
$$
</div>

Si $m_0$ et $m_1$ sont équivalent on a $\Pr[b'=1 \;\mid\; b=1] - \Pr[b'=1 \;\mid\; b=0] = \Pr[b'=0 \;\mid\; b=0] - \Pr[b'=0 \;\mid\; b=1]$ ce qui conclut la preuve.

{% enddetails %}

On a clairement que :

{% note %}
Confidentialité parfaite et avantage nul au jeu du chiffrement sont deux notions équivalentes.
{% endnote %}

Terminons cette partie par un petit exercice qui montre, faut il encore le faire, que le code de Vernam est une excellente façon de chiffrer ses messages :

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

> TBD example 2.8 avec vigenère "intro of modern cryptography

## <span id="sémantiquement-sécurisé"></span>Sémantiquement Sécurisée

La méthode précédente donne idée de la sécurité _actuelle_ d'une méthode de chiffrement puisqu'elle mesure le nombre d'opérations ou le temps pris pour décrypter une méthode de chiffrement. Cela ne dit rien de ce qui pourra se passer dans 5 ou 10 ans lorsque les ordinateurs iront plus vite ou que les méthodes de résolutions seront plus évoluées. De plus, un algorithme brute force qui teste toutes les possibilités aura toujours un avantage de 1 (ou quasi 1 si l'on prend en compte les collisions) si on lui laisse un temps exponentiel par rapport à la taille de la clé pour s'exécuter.

Il faut donc d'un côté :

- trouver une autre mesure que le temps pour déterminer la sécurité,
- ne prendre en compte que les adversaires s'exécutant en temps raisonnable

La solution est d'utiliser la complexité algorithmique et son analyse asymptotique. On considérera alors :

- des clés assez grandes pour que l'attaque brute force nécessite un temps exponentiel non réalisable
- les adversaires qui ont une chances de terminer assez rapidement, c'est à dire ceux dont les algorithmes de résolution sont polynomiaux,
- qu'un avantage est acceptable s'il est  exponentiellement petit par rapport à la taille de la clé.

Par exemple l'algorithme brute force pour lequel on ne lui accorde qu'un nombre d'exécution polynomial, disons $\mathcal{O}(s^d)$, aura un avantage de $\epsilon(s) = \frac{1}{2^{s-d}}$ qui devient exponentiellement petit lorsque la taille de la clé $s$ augmente !

{% note "**Définition**" %}
Pour calculer une complexité, il faut connaître la taille de l'entrée, c'est à dire les informations données à l'adversaire.

De façon classique, la taille de cette entrée ($n$), nommé **_paramètre de sécurité_**, consiste en la taille de la clé (valant $s$) plus la taille du message à chiffrer (valant $t$) :

<div>
$$
n \coloneqq s+t
$$
</div>

{% endnote %}

L'augmentation de la taille des clés va certes avoir un effet sur le temps d'exécution mais ce sera surtout sur l'avantage que cela se fera sentir, s'il est exponentiellement petit par rapport au paramètre de sécurité :

{% exercice %}
On suppose que l'exécution d'un adversaire de complexité temporelle (en secondes) $n^3$ ait un avantage de $\min(1, \frac{2^{40}}{2^n})$.

Pour $n=40$, combien faut-il de temps pour qu'il puisse décrypter la méthode de façon certaine ? Quel est son avantage pour $n=50$ et en combien de temps s'exécute-t-il ?
{% endexercice %}
{% details "corrigé" %}

Pour $n=40$, il aura besoin de $40^3$ secondes pour s'exécuter, c'est à dire un peut moins de 18 heures, et son avantage de sera de 1.

Pour $n=40$, il aura besoin de $50^3$ secondes pour s'exécuter, c'est à dire un peut moins de 35 heures, mais son avantage ne sera plus que de $10^{-3}$.
{% enddetails %}

Autre exemple, on la vitesse de calcul ne bénéficie pas forcément à l'adversaire :

{% exercice %}
Supposons qu'une méthode de chiffrement se chiffre et se déchiffre en $n^2$ opérations et qu'un adversaire possède un algorithme en $n^4$ pour le décrypter.

Soit $n=50$. Si l'on prend un ordinateur qui va 16 fois plus vite, quelle est la taille de $n$ que l'on peut se permettre en gardant le même temps de chiffrement ? Que s'est-il passé pour l'adversaire ?
{% endexercice %}
{% details "corrigé" %}

On cherche $n'$ tel que : $16\cdot 50^2 = n'^2$, c'est à dire $n' = 200$. On a pu augmenter le paramètre de sécurité de 4.

Pour l'adversaire, c'est moins profitable puisque son temps d'exécution est multiplié par $200^4/50^4 = 256$.
{% enddetails %}

Définissons formellement les adversaire et les avantages que l'on admet pour qu'une méthode soit sécurisée.

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
- tout algorithme **efficace** n'a qu'un **avantage négligeable** au jeu du chiffrement.
  {% endnote %}

La négligeabilité permet de définir théoriquement les avantages que l'on peut accepter de la part de l'adversaire.

La négligeabilité se compose tout comme la polynomialité (somme et produit de polynôme restent des polynôme) :

- $p(n) \cdot \epsilon$ reste négligeable si $\epsilon$ l'est
- $\epsilon + \epsilon'$ reste négligeable si $\epsilon$ et $\epsilon'$ le sont
- $\epsilon \cdot \epsilon'$ reste négligeable si $\epsilon$ et $\epsilon'$ le sont

## <span id="jeu-reconnaissance"></span>Jeu de la reconnaissance

Le jeu du chiffrement est un cas particulier du cas du jeu de la reconnaissance ci-dessous (on chercher à différentier la loi suivie par $E(k, m_0)$ de celle suivi par $E(k, m_1)$ lorsque $k$ est distribué de façon uniforme).

Soient $D_i: \mathcal{U} \to [0, 1]$ pour $i \in \\{0, 1\\}$ deux lois de distribution. On cherche à distinguer si un élément de $\mathcal{U}$ a été tiré selon la loi $D_0$ ou $D_1$.

```

     testeur                              adversaire
    ---------                            ------------
    |       |                            |          |  
 b  |  D0   |   x tiré selon D0 si b=0   |    D0    |   A(x) = b'
--->|  D1   |   x tiré selon D1 si b=1   |    D1    | ------------->
    |       | -------------------------> |          |
    ---------                            ------------
```

Ce jeu explicite le fait que toute la cryptographie se résume à savoir si la suite générée par notre méthode de chiffrement est assez proche de l'aléatoire pour que l'on ne puisse pas, en pratique, en exploiter les différences. L'avantage de l'adversaire est, comme pour le jeu du chiffrage, défini tel que :

<div>
$$
\epsilon(A) \coloneqq \Pr[b'=1 \;\mid\; b=1] - \Pr[b'=1 \;\mid\; b=0]
$$
</div>

Les deux lois seront dites :

- **_équivalentes_** si $D_0 = D_1$ : on ne peut les distinguer
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
  3. si p0 ≥ p1 rendre 0, sinon rendre 1

Si son avantage est négligeable, tous les adversaires, qu'ils soient efficaces ou non, n'auront également qu'un avantage négligeable.

{% endnote %}

Pour se fixer les idée commençons par un petit exercice :
{% exercice %}
Montrez que l'on peut distinguer la loi uniforme sur $\\{0, 1\\}^n$ de la fonction constante $F(x) = \mathbb{0}$ avec un avantage non négligeable.
{% endexercice %}
{% details "preuve" %}
Comme :

- la probabilité d'obtenir n'importe quel mot de $\\{0, 1\\}^n$ vaut $1/2^n$ pour la loi uniforme,
- la probabilité d'obtenir $\mathbb{0}$ vaut 1 pour la fonction constante

Le meilleur algorithme va :

- répondre la fonction constante si le mot en entrée vaut $\mathbb{0}$
- répondre la fonction uniforme sinon

En supposant sans perte de généralité que si $b=0$ le testeur va rendre la fonction constante, l'avantage de cet algorithme vaut :

<div>
$$
\begin{array}{lcl}
\epsilon(A) &=& |\Pr[x \neq \mathbb{0} \;\mid\; b=1] - \Pr[x \neq \mathbb{0} \;\mid\; b=0]|\\
&=&|1-1/2^n - 0|\\
\end{array}
$$
</div>

{% enddetails %}

## Vernam biaisé

> TBD motivation. Vernam parfait mais pas attrapable en pratique, supposons un chiffrement biaisé (dés pas parfaitement équilibré). Est-ce que l'avantage devient important ?
> TBD montre la propagation du biais. Mais si négligeable reste ok (comme en algorithme avec une composition de poly reste poly : une composition de negl reste negligeable)

Prenons par exemple la distribution de Bernoulli $B$ telle que $B(1) = 1/2 + \epsilon/2$. et $B^n$ la distribution sur $\\{0, 1\\}^n$ où chaque bit est tiré indépendamment avec $B$. On essaie de comparer cette distribution au tirage uniforme $N$.

Soit $A$ le meilleur algorithme permettant de distinguer $B^n$ et $N$. Il va répondre $B^n$ si $B^n(x) > (1/2)^n$ et $N$ sinon.

Son avantage est alors :

<div>
$$
\begin{array}{lcl}
\epsilon(A) &=&| \Pr[b'=1 \;\mid\; b=1] - \Pr[b'=1 \;\mid\; b=0] | \\
&=& |\sum_{X\in \{0, 1\}^n}(\Pr[A(X') = 1 \;\mid\; X=X']\cdot B^n(X) - \Pr[A(X') = 1 \;\mid\; X=X']\cdot (1/2)^n)|\\
&=& |\sum_{X\in \{0, 1\}^n}(\Pr[A(X') = 1 \;\mid\; X=X']\cdot B^n(X) + \Pr[A(X') = 0 \;\mid\; X=X']\cdot (1/2)^n) - 1|
\end{array}
$$
</div>

Or $\Pr[A(X') = 1 \;\mid\; X=X'] = 1$ si $B^n(X')\geq (1/2)^n$, l'avantage vaut donc :

<div>
$$
\begin{array}{lcl}
\epsilon(A) &=&  \sum_{X\in \{0, 1\}^n}\max((1/2)^n, B^n(X)) - 1
\end{array}
$$
</div>

Et comme $\max(a, b) = \frac{1}{2}\cdot (a+b+|b-a|)$ on a au final :

<div>
$$
\begin{array}{lcl}
\epsilon(A) &=&  \frac{1}{2}\sum_{X\in \{0, 1\}^n}| (1/2)^n - B^n(X) |
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

Si $\epsilon$ est négligeable, la génération d'éléments de $\\{0, 1\\}^n$ l'est aussi.

On peut utiliser ce qui précède pour créer un chiffrement statistiquement sécurisé en utilisant un chiffre de Vernam avec notre générateur aléatoire :

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
