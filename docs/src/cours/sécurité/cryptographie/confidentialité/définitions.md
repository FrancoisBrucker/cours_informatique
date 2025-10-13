---
layout: layout/post.njk

title: Définitions de la confidentialité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

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
--->|       |     E(k,mb) =c     |          | -------------------->
    |       | -----------------> |          |
    ---------                    ------------
```

Ce jeu permet de simuler des attaques par messages choisis (_Chosen-plaintext attackers, CPA_). Si notre méthode de chiffrement y résiste elle sera également robuste pour les attaques plus faible par message connu ou chiffre uniquement.

Ce type d'attaque, bien qu'elle ne permet pas de déchiffrer les messages permet tout de même d'avoir des informations sur le type de message chiffré, par exemple si la réponse est positive (`m0 = "oui"`) ou négative (`m1 = "non"`).

Par exemple supposons que nous chiffrons/déchiffrons nos messages avec l'algorithme de Vigenère et que l'on chiffre des messages avec des clés de longueur $\vert k \vert\ = 2$.
L'adversaire pourrait choisir `m0 = "aa"` et `m1 = "ab"` et décider de répondre 1 si `c[1] ≠ c[0]`.

Il est clair que si l'adversaire essaie toutes les possibilités il trouvera toujours la solution (presque toujours en fait, car il peut exister des cas où `E(k,m0) = E(k', m1)`. Mais comme l'adversaire peut choisir ses mots il peut minimiser – voir supprimer ce cas). Cela prendra cependant un temps énorme. Pour l'exemple précédent du chiffrement de Vigenère avec une clé de taille $\vert k \vert\ = 2$ il y a $26^{2} = 676$ possibilités ce que l'on peut faire très rapidement (un peut plus de 11 minutes si on met 1 seconde à vérifier un cas), mais si la clé $k$ possède 128bits, il y a $2^{128}$ possibilité et même si l'adversaire peut tester 1000 milliards de possibilités par seconde ($10^{12}$) il lui faudrait tout de même plus de $10^{17}$ siècles pour tester toutes les possibilités.

Ceci montre trois choses :

{% attention "**À retenir**" %}

1. un adversaire motivé et ayant du temps pourra toujours déchiffrer un message
2. on peut être en sécurité assez longtemps si la seule attaque possible est l'attaque brute force
3. La méthode $A(\cdot)$ utilisé doit être rapide : c'est un algorithme

Il n'est donc pas possible d'être sécurisé pour toujours, mais on peut tenter de garante d'être en sécurité assez longtemps.

{% endattention %}

## Avantage Probabiliste







Pour notre exemple avec le chiffre de Vigenère de taille deux :

- $\Pr[b' = 1 \\;\mid\\; b = 1] = 1- \Pr[b' = 0 \\;\mid\\; b = 1]$. On ne peut répondre $b'=0$ alors que $b=1$ que si la lettre $a$ se chiffre avec la même lettre que $b$ ce qui arrive 26 fois (choisir la première lettre de $k$ entraîne sa deuxième). Donc $\Pr[b' = 1 \\;\mid\\; b = 1] = 1- 26/26^2 = 1-1/26$
- $\Pr[b' = 0 \\;\mid\\; b = 0] = 1$ on ne se trompe jamais si c'est `m0` qui est encodé.

Pour notre algorithme on a donc un avantage de $\epsilon(A) = 1-1/26 \geq 95\\%$ ce qui est très bon !

Attention, cela ne veut pas dire que le chiffrement de Vigenère est mauvais, juste que connaître la taille de la clé permet de reconnaître le chiffrement de messages connus.

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

La probabilité de gagner vaut $\Pr[b'=b] = 1/2\cdot \Pr[b'=0 \\;\mid\\; b=0] + 1/2\cdot \Pr[b'=1 \\;\mid\\; b=1] = 1/2 +\epsilon(A)/2$ et la proba de perdre $1/2 - \epsilon(A)/2$
Du coup :

<div>
$$
\Pr[b'=1 \;\mid\; b=1] - \Pr[b'=0 \;\mid\; b=1] + \Pr[b'=0 \;\mid\; b=0] - \Pr[b'=1 \;\mid\; b=0] = 2\cdot \epsilon(A)
$$
</div>

Si $m_0$ et $m_1$ sont équivalent on a $\Pr[b'=1 \\;\mid\\; b=1] - \Pr[b'=1 \\;\mid\\; b=0] = \Pr[b'=0 \\;\mid\\; b=0] - \Pr[b'=0 \\;\mid\\; b=1]$ ce qui conclut la preuve.

{% enddetails %}

Puisque l'adversaire peut choisir les 2 mots, il va prendre ceux ayant statistiquement le plus de différence : un avantage nul signifie que tous les mots sont équivalents :

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



## Vernam biaisé

La notion d'avantage négligeable nous donne une méthode de construction sécurisée : l' avantage négligeable se propage au reste de la chaîne sans exploser. Illustrons le en montrant que l'on peut créer un chiffre de Vernam sémantiquement sécurisé en partant d'un générateur de no,bre aléatoire biaisé, du moment que le biais est négligeable.

Soit la distribution de Bernoulli biaisée $B$ telle que $B(1) = 1/2 + \epsilon/2$. et $B^n$ la distribution sur $\\{0, 1\\}^n$ où chaque bit est tiré indépendamment avec $B$. On essaie de comparer cette distribution au tirage uniforme $N$.

On a vu que $A$, le meilleur algorithme permettant de distinguer $B^n$ et $N$ va répondre $B^n$ si $B^n(x) \geq (1/2)^n$ et $N$ sinon.

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

Et comme $\Pr[A(X') = 1 \\;\mid\\; X=X'] = 1$ si $B^n(X')\geq (1/2)^n$, l'avantage vaut :

<div>
$$
\begin{array}{lcl}
\epsilon(A) &=&  \sum_{X\in \{0, 1\}^n}\max((1/2)^n, B^n(X)) - 1
\end{array}
$$
</div>

En utilisant le fait que $\max(a, b) = \frac{1}{2}\cdot (a+b+|b-a|)$ on obtient :

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

Si on fait bien les choses (on verra qu'on peut se tromper si on ne fait pas attention), on peut construire une méthode de chiffrement sémantiquement sécurisée en chaînant des blocs de biais négligeable, tout comme en algorithmie une composition d'algorithmes  de complexités polynomiales reste polynomiale.

Ceci va être utilisé intensivement par la suite où l'on construira chaque bloc de la méthode de chiffrement indépendamment les une des autres : si chaque bloc ne donne qu'un avantage négligeable toute la chaîne également.

## Chiffre utilisable en pratique

La méthode de chiffrement que l'on a vu précédemment n'est pas utilisable en pratique. Déjà parce qu'un chiffrement de de Vernam nécessite une taille de clé égale au message à chiffrer, mais aussi parce qu'un générateur de nombre aléatoire, même biaisé, est compliqué car non implémentable facilement.

Pour qu'une méthode de chiffrement puisse être utilisé en pratique, il faut pouvoir avoir deux choses :

- des clés de petites tailles par rapport au message à faire passer
- des algorithmes de complexité linéaires pour chiffrer et déchiffrer les messages.

Même si on s'autorise théoriquement des algorithmes polynomiaux, en pratique, efficaces veut plutôt dire linéaire car il faut que ces algorithmes puissent chiffrer de très nombreuses données. Efficace prend donc deux significations différentes, selon que l'on cherche à prouver théoriquement des résultats où que l'on veuille en pratique chiffrer des données. L'un ne va cependant pas sans l'autre.

Ces deux contraintes vont forcément nous faire passer des informations à l'adversaire. Selon le type d'information que l'on ne veut pas divulguer on va utiliser une méthode plutôt qu'une autre.
