---
layout: layout/post.njk 
title: Calculabilité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On vient de le voir : il y a plus de nombres réels que d'algorithmes. Il existe donc forcément des choses que ne peut pas calculer un algorithme.

Mais avant de voir ce que ne peut pas faire un algorithme, voyons des choses que l'on peut faire avec.

## Algorithmes et fonctions

On a vu qu'un algorithme et tout ce qu'il manipulait pouvait être considéré comme une suite finie de 0 et de 1. On en déduit immédiatement la proposition suivante :

{% note "**Proposition**" %}
Un algorithme est une fonction :

$$f: \\{0, 1\\}^\star \rightarrow \\{0, 1\\}^\star$$

Où $\\{0, 1\\}^\star$ est l'ensemble des suites finies de $0$ et de $1$.
{% endnote %}

Remarquez que ceci fonctionne même si un algorithme possède plusieurs entrées. Il suffit de les écrire sous la forme d'une chaîne de caractère où chaque paramètre est séparé par une virgule par exemple et de transcrire cette chaîne en suite de 0 et de 1.

Comme une suite finie de 0 et de 1 est une écriture binaire d'un entier positif on en déduit immédiatement que :

{% note "**Proposition**" %}
Un algorithme est une fonction :

$$f: \mathbb{N} \rightarrow \mathbb{N}$$

{% endnote %}

Par exemple la fonction identité est un algorithme puis'on peut l'écrire :

```text
Nom : identité
Entrées : 
    n : un entier
Programme :
    rendre n
```

De même, je vous laisse reprendre vos cours de primaire pour le faire, les fonctions $f(n) = 2n$, $f(n) = 12 \cdot n$ ou encore $f(n) = n^2$ sont des algorithmes ! On dit que ces fonctions sont ***calculables*** :

{% note "**Définition**" %}
Une fonction $f: \mathbb{N} \rightarrow \mathbb{N}$ est ***calculable*** s'il existe un algorithme permet de la calculer.

{% endnote %}

Montrons tout de suite que cette notion a un sens :

{% note "**Proposition**" %}
Il y a strictement plus de fonctions $f: \mathbb{N} \rightarrow \mathbb{N}$ que de nombres entiers.

{% endnote %}
{% details "preuve", "open" %}
La preuve est identique à celle du [Théorème montrant qu'il y a strictement plus de réels que d'entiers](../définition/#diagonale-cantor).

Comme les fonctions $f^k: \mathbb{N} \rightarrow \mathbb{N}$ définies telles que $f^k(x) = x + k$ sont deux à deux différentes lorsque $k$ parcourt $\mathbb{N}$, on en déduit qu'il existe au moins autant de fonctions $f: \mathbb{N} \rightarrow \mathbb{N}$ que d'entiers.

On suppose alors qu'il y en a autant et donc qu'il existe une bijection entre les fonctions $f: \mathbb{N} \rightarrow \mathbb{N}$ et les nombres entiers. On peut alors numéroter chaque fonction $f_0$, $f_1$, $\dots$, $f_n$.

Cet ordre nous permet de construire la fonction $g: \mathbb{N} \rightarrow \mathbb{N}$ telle que $g(i) = f_i(i) + 1$ pour tout $i \in \mathbb{N}$.

Mais ceci est impossible puisque  $g \neq f_i$ pour tout $i$ ($g(i) \neq f_i(i)$ par définition de $g$) : il existe strictement plus de fonctions $f: \mathbb{N} \rightarrow \mathbb{N}$ que d'entiers.

{% enddetails %}

Comme il existe au plus autant d'Algorithmes que de nombres entiers, il y a bien des fonctions $f: \mathbb{N} \rightarrow \mathbb{N}$ intraduisibles par un algorithme.

{% info %}
Nous utiliserons parfois des algorithmes sans paramètre. Ils permettent de créer les fonctions constantes et peuvent être vue comme un cas particulier d'Algorithme ou la réponse est la même quelque soit l'entrée donnée.
{% endinfo %}

## Exemples de fonctions calculables

Commençons par montrer quelques fonction que l'on peut calculer.

[Quelques exemples](https://en.wikipedia.org/wiki/Computable_function#Examples) :

- les fonctions constantes sont calculables
- si $f$ et $g$ sont deux fonctions calculables, alors $f+g$, $f \cdot g$ et $f \circ g$ sont calculables
- les fonctions dont le domaine de définition est fini, sont calculables
- ...

En utilisant uniquement la fonction successeur $\text{succ}(x) \rightarrow x + 1$ (qui est clairement calculable) on arrive par exemple à [reconstruire toutes les opérations usuelles](https://fr.wikipedia.org/wiki/Axiomes_de_Peano).

{% exercice %}
Créez la fonction $\text{somme}(x, y) \rightarrow x + y$ en utilisant uniquement la fonction successeur, un test d'égalité et une boucle.
{% endexercice %}
{% details "corrigé" %}

```text
Nom : somme
Entrées : 
    x, y : deux entiers
Programme :
    c = 0
    tant que c < x:
        y = succ(y)
        c = succ(c)
```

{% enddetails  %}

Les fonctions calculables par compositions de fonctions simples (successeur et projection essentiellement) sont appelées [fonctions récursives primitives](https://fr.wikipedia.org/wiki/Fonction_r%C3%A9cursive_primitive). Elles ont été utilisées par Gödel pour montrer son [théorème d'incomplétude](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8mes_d%27incompl%C3%A9tude_de_G%C3%B6del). On a démontré plus tard (voir [la fonction d'Ackermann](./#fonction-ackermann))que les fonctions récursives primitives sont des cas particuliers de fonctions calculables (ce sont les [fonctions récursives](https://fr.wikipedia.org/wiki/Fonction_r%C3%A9cursive) qui sont exactement les fonctions calculables).

Beaucoup, beaucoup, beaucoup de fonctions sont calculables, il suffit d'exhiber un pseudo-code pour le prouver.

{% note "**À retenir**" %}
La quasi totalité des fonctions mathématiques usuelles sont calculables
{% endnote %}

De façon plus bizarre, il existe aussi des fonctions, que l'on sait calculable, mais dont on ne connaît pas l'algorithme pour les calculer. Par exemple :

```text
Nom : 5-consécutifs
Entrées : 
    n : un entier
Programme :
    si il existe n "5" consécutifs dans les décimales de π:
        rend 1
    sinon:
        rend 0
```

Le texte ci-dessus n'est **pas** un programme car le "il existe" n'est pas ue opération élémentaire que je peux effectuer de tête. De plus, sans connaissance a priori, je suis obligé de tester toutes les décimales de $\pi$ pour répondre à la question du "il existe", ce qui fait que s'il n'existe pas n "5" successifs, le programme ne s'arrêtera pas.

Mais en vrai, le texte ci-dessus peut se re-écrire de deux façons.

Soit existe n "5" consécutifs dans les décimales de $\pi$ quelque soit $n$ (on appelle les nombres qui vérifient cette propriété [des nombres univers](https://fr.wikipedia.org/wiki/Nombre_univers)) et alors le programme devient l'algorithme ci-dessous :

```text
Nom : 5-consécutifs
Entrées : 
    n : un entier
Programme :
    rend 1
```

Soit il existe au plus N "5" consécutifs dans les décimales de $\pi$ et le programme devient :

```text
Nom : 5-consécutifs
Entrées : 
    n : un entier
Programme :
    si n < N + 1:
        rend 1
    sinon:
        rend 0
```

Dans les deux cas, c'est un algorithme.

Le problème est que l'on ne sait pas si π est [un nombre univers](https://fr.wikipedia.org/wiki/Nombre_univers) et donc on ne sait pas lequel des deux algorithmes est le bon.

{% note "**À retenir**" %}
Savoir qu'on peut créer un algorithme pour calculer une fonction ne signifie pas que c'est facile de le faire. Il faut souvent avoir des connaissances annexes, hors algorithmie, poussée sur le problème à résoudre pour le faire
{% endnote %}

## Nombres calculables

{% note "**définition**" %}
Un nombre $x$ est ***calculable*** s'il existe un algorithme $A$ tel que :

- $A(0)$ rend la partie entière de $x$
- $A(i)$ rend la $i$-ème décimale de $x$, pour tout $i > 0$

{% endnote %}

**Tous les entiers sont calculables** :

```text
Nom : Entier i
Entrées : 
    n : un entier
Programme :
    si n == i
        rend i
    sinon:
        rend 0
```

C'est bien un algorithme puisque :

- sa description est finie pour tout i
- son temps d'exécution est fini pour tout n

On en déduit immédiatement que **tous les rationnels sont calculables** : il suffit d'utiliser [l'algorithme de la division de deux entiers décimaux](https://fr.wikipedia.org/wiki/Division#Algorithmes_de_la_division_de_nombres_d%C3%A9cimaux) après en primaire.

Enfin, certains réels sont calculables, même si leurs nombres de décimales est infini. Par exemple tous les réels qui sont des limites de suites elles mêmes calculables :

{% note "**Proposition**" %}
Si $x$ est la limite d'une suite $(u_n)_{n \geq 0}$ et qu'il existe deux Algorithmes $A$ et $B$ tels que :

- $A(n)$ rende la partie entière de $u_n$
- $B(n)$ rende les $n$ premières décimales de $u_n$

Alors $x$ est calculable.

{% endnote %}
{% details "preuve", "open" %}

Comme $u_n$ converge vers $x$, pour tout $i> 0$, il existe $N_i$ tel que $\mid x - u_n\mid < 10^{-i}$ pour tout $n > N_i$. Si l'on veut calculer la $i$-ème décimale de $x$, Il suffit de calculer $u_{max(i, N_{i})}$ et de prendre sa $i$-ème décimale.

{% enddetails %}

La proposition ci-dessus permet de montrer que nombre de réels connus sont calculables, comme $\pi$ par exemple puisqu'il est la limite de  [la série de Leibniz de $\pi$](https://fr.wikipedia.org/wiki/Formule_de_Leibniz#S%C3%A9rie_altern%C3%A9e).

De la même manière, on peut calculer $cos(x)$, $sin(x)$ ou encore $\sqrt{x}$ pour tout $x$ calculable grâce à leur [développement en séries entières](https://fr.wikipedia.org/wiki/Formulaire_de_d%C3%A9veloppements_en_s%C3%A9ries).

{% note %}
Si l'on pense à un réel calculé à partir d'une fonction mathématique usuelle, il y a toute les chances qu'il soit calculable.
{% endnote %}

{% attention %}
Il faut que ce soit **le même algorithme** qui est utilisé pour chaque élément de la suite. Si on utilise un algorithme différent pour chaque $n$, le réel obtenu n'est pas forcément calculable, c'est le cas des [suite de speker](https://fr.wikipedia.org/wiki/Suite_de_Specker) par exemple.
{% endattention %}

{% lien %}

[Page Wikipédia sur les réels calculables](https://fr.wikipedia.org/wiki/Nombre_r%C3%A9el_calculable), des nombres calculable.
{% endlien %}

En conclusion :

{% note "**À retenir**" %}
La quasi-totalité des nombres réels utilisées en mathématiques en tant que tel ($\pi$, $e$, etc) ou comme résultat de fonctions (comme $cos$, $sin$, racine carrée, etc) sont calculables :

Il existe un algorithme prenant un entier $i$ en paramètre et qui rend sa $i$ème décimale.
{% endnote %}

Attention cependant à ne pas confondre le réel en tant que tel (non calculable puisqu'il possède une infinité de décimale) et son approximation que l'on peut utiliser dans les calculs.

## Fonctions calculables rigolotes

On va montrer deux exemples de fonctions calculables. L'une qui grossi très très vite (la fonction d'Ackermann) et l'autre (la fonction de Takeuchi) qui calcule des choses simples de façon compliquées.

Ces deux fonctions sont parfois utilisées pour des tests de performance d'ordinateurs car est sont très  gourmandes en temps de calcul.

### <span id="fonction-ackermann"></span>Fonction d'Ackermann

La [fonction d'Ackermann](https://fr.wikipedia.org/wiki/Fonction_d%27Ackermann), outre le fait qu'elle est rigolote car elle croît très très rapidement (plus que factoriel, c'est dire), est importante théoriquement car c'est la première fonction connue que l'on ne peut pas écrire avec des boucles `for`{.language-}. On est obligé d'utiliser soit des boucles `while`{.language-} pour écrire son pseudo-code de façon itérative, soit d'utiliser la récursivité (ce que l'on va faire). Enfin, cette fonction est d'utilité théorique certaine car c'est la première fonction connue à être calculable mais non primitive récursive.

{% info %}
Notez que tout algorithme récursif peut s'écrire de façon itérative. C'est ce quel'on appelle la dé-curryfication.
{% endinfo %}

Elle se définit de la manière suivante, pour tous entiers m et n positifs :

<div>
$$
A(m, n) = \left\{
    \begin{array}{ll}
        n + 1 & \mbox{si } m = 0 \\
        A(m - 1, 1) & \mbox{si } n = 0 \\
        A(m - 1, A(m, n - 1)) & \mbox{sinon.}
    \end{array}
\right.
$$
</div>

{% note "**Proposition**" %}
La fonction d'Ackermann est bien définie pour tout $m$ et $n$ entiers.
{% endnote %}
{% details "preuve", "open" %}
Pour chaque appel récursif de la fonction d'Ackermann, soit m, soit $n$ est strictement plus petit dans la fonction appelée que dans la fonction appelante. On arrivera donc toujours à $m = 0$ qui stoppera la récursion ou $n = 0$ qui fera baisser la valeur de $m$.
{% enddetails %}

Le nombre de récursion est très très important. Pour calculer $A(2, 3)$ par exemple, on a les récurrences suivantes :

- $A(2, 3) = A(1, A(2, 2))$
- $A(2, 2) = A(1, A(2, 1))$
- $A(2, 1) = A(1, A(2, 0))$
- $A(2, 0) = A(1, 1)$
- $A(1, 1) = A(0, A(1, 0))$
- $A(1, 0) = A(0, 1) = 2$
- puis on remonte d'un cran et les récursions recommencent...

Au final on trouve $A(2, 3) = 9$. La fonction croît très très vite. Par exemple $A(5, 0) = A (4, 1) = 65533$ et $A(4, 2) = $2^{65536} - 3$.

Sa complexité est de plus supérieure : il faut plus de $A(m, n)$ opérations pour calculer $A(m, n)$ puisque l'on ne fait qu'ajouter 1 à n comme calcul et les valeurs de n sont modifiées de +1 ou -1.

### Fonction de Takeuchi

La [fonction de Takeuchi](https://fr.wikipedia.org/wiki/Fonction_de_Takeuchi) est surprenante, bien malin qui sait ce qu'elle fait juste en la regardant.

Elle est définie pour tous entiers $x$, $y$ et $z$ telle que :

<div>
$$
\tau(x, y, z) = \left\{
    \begin{array}{ll}
         y & \mbox{si } x \leq y\\
        \tau(\tau(x-1, y, z), \tau(y-1, z, x), \tau(z-1, x, y)) & \mbox{sinon.}
    \end{array}
\right.
$$
</div>

Le nombre de récurrence est très élevé et pourtant, on peut montrer qu'elle calcule :

<div>
$$
\tau(x, y, z) = \left\{
    \begin{array}{ll}
        y & \mbox{si } x \leq y\\
        z & \mbox{si } x > y \mbox{ et } y \leq z\\
        x & \mbox{si } x > y \mbox{ et } y > z\\
    \end{array}
\right.
$$
</div>
{% details "preuve", "open" %}

Par récurrence sur $x+y+z= k$.

Si $x+y+z=0$, on a  $x=y=z=0$ et $\tau(0, 0, 0) = 0$, la récurrence est vérifiée. On suppose la récurrence vraie pour $x+y+z=k$.

Pour $x+y+z=k+1$, on analyse tous les cas possibles :

- $x \leq y$ : Ok
- $x > y$ et $y \leq z$ : On a $\tau(x, y, z) = \tau(\tau(x-1, y, z), \tau(y-1, z, x), \tau(z-1, x, y))$ :
  - on a $y-1 \leq z$ donc (par hypothèse de récurrence) $\tau(y-1, z, x) = z$
  - soit $x-1 > y$ et $y \leq z$ et alors (par hypothèse de récurrence) $\tau(x-1, y, z) = z$ : $\tau(x, y, z) = \tau(z, z, ?) = z$
  - soit $x-1 \leq y$ et alors (par hypothèse de récurrence) $\tau(x-1, y, z) = y$ : $\tau(y, z, ?) = z$ (puisque $y \leq z$)
- $x > y > z$ : On a $\tau(x, y, z) = \tau(\tau(x-1, y, z), \tau(y-1, z, x), \tau(z-1, x, y))$
  - on a $z-1 < y< x$ et donc $\tau(x, y, z) =  \tau(\tau(x-1, y, z), \tau(y-1, z, x), x)$
  - on procède de même que précédemment en analysant tous les cas
    - $x-1 > y$ et $y-1>z$ : $\tau(x, y, z) = \tau(x-1, x, x) = x$
    - $x-1 > y$ et $y-1=z$ : $\tau(x, y, z) = \tau(x-1, z, x) = x$
    - $x-1 = y$ et $y-1>z$ : $\tau(x, y, z) = \tau(y, x, x) = x$
    - $x-1 = y$ et $y-1=z$ : $\tau(x, y, z) = \tau(y, z, x) = x$
{% enddetails %}

Cette fonction montre, encore une fois, qu'il est très difficile de déterminer ce que fait un algorithme sans l'analyser finement (voyez le comme un exemple du [théorème de Rice](../arrêt-rice/#théorème-rice) vu précédemment).

{% note "**À retenir**" %}
La fonction de Takeuchi montre que pour résoudre un problème simple il existe des solutions compliquée.

Lorsque vous essayer de résoudre un problème avec un algorithme essayer toujours de trouver la solution la plus simple possible. Vous verrez que souvent, sans réfléchir on va produire la version compliquée plutôt la version simple.
{% endnote %}

## Non calculabilité

Trouver une fonction ou un nombre qu'on ne peut pas calculer est un exercice mental compliqué. En effet, si l'on pense à un nombre précis, on lui associe une définition et donc très souvent un moyen de le construire.

Mais ces objets existent puisqu'il y a strictement plus de fonction et de réels que d'algorithmes.

Nous allons donner un exemple de chaque ci-après.

### Une Fonction non calculable : la complexité de Kolmogorov

{% lien %}
[Complexité de Kolmogorov](https://fr.wikipedia.org/wiki/Complexit%C3%A9_de_Kolmogorov)
{% endlien %}

La complexité de Kolmogorov est un exemple classique de fonction non calculable.

{% note "**Définition**" %}
La complexité de Kolmogorov est une fonction $k: \mathbb{N} \rightarrow \mathbb{N}$ telle que $k(n)$ soit le nombre de caractères minimum d'un algorithme sans paramètre dont la sortie est l'affichage à l'écran du nombre $n$
{% endnote %}
{% info %}
La valeur de la fonction va dépendre de la langue utilisée bien sur. Il est probable que la complexité de Kolmogorov allemande soit plus grande que la complexité de Kolmogorov anglaise ou chinoise.
{% endinfo %}

La définition semble idiote. Pour rendre 5 Il suffit d'utiliser l'algorithme trivial qui écrit directement le nombre en base 2 :

```text
affiche à l'écran la chaîne de caractères "101"
```

Mais il faut écrire $\log_{10}(n)$ chiffres dans l'algorithme, ce qui donne une taille de $\log_{10}(n) + 42 + 2$ (le nombre en base 10, le texte avant et les deux `"`). Si ce nombre est gros, on peut fait bien mieux.

Par exemple :

```text
affiche à l'écran la concaténation de 1000 caractères "1"
```

Possède 57 caractères et permet d'écrire un nombre de 1000 chiffres ! La question du nombre minimal de caractères est donc une question pertinente, ou au moins légitime.

De plus la fonction $k(n)$ existe. En rangeant tous les textes possibles par ordre lexicographique : d'abord les textes à 1 caractère, puis les textes à 2 caractères, etc. on va forcement trouver l'algorithme trivial qui donne une réponse. Parmi tous les textes plus petits ou égal à l'algorithme trivial, il y en a un nombre fini, on peut en extraire tous les programme (facile, c'est les texte qui veulent dire quelque chose algorithmiquement) et notre algorithme minimum est dedans.

La difficulté réside bien sur dans le fait de savoir si tel ou tel programme rend la notation binaire de $n$ ou pas (c'est encore une fois le [théorème de Rice](../arrêt-rice/#théorème-rice) qui entre en jeu).

On a maintenant assez de bille pour démontrer la non-calculabilité de la complexité de Kolmogorov :

{% note "**Théorème**" %}
La complexité de Kolmogorov est non calculable.
{% endnote %}
{% details "preuve", "open" %}

Supposons que la complexité de Kolmogorov soit calculable. Notons `Kolmogorov(n)`{.language-} un algorithme la calculant et $K$ le nombre de caractères de celui-ci.

On peut alors définir l'algorithme sans paramètre suivant :

```text
n = 0
tant que Kolmogorov(n) < K + 1000:
    n = n + 1
rend n
```

Ce programme (de 61 caractères) est bien un algorithme car :

- `Kolmogorov(n)`{.language-} est un algorithme
- il y a un nombre infini de nombres mais seulement un nombre fini d'algorithmes sans paramètres ayant moins de $K + 1000$ caractères : il existe forcément un nombre qui n'est pas la sortie d'un algorithme sans paramètre de moins de $K + 1000$ caractères.

Le retour de cet algorithme sans paramètre est le plus petit nombre de complexité de Kolmogorov plus grand que $K + 1000$. Mais ceci est impossible puisqu'il est déterminé par notre algorithme qui fait, en lui concaténant l'algorithme de `Kolmogorov(n)`{.language-} pour qu'il soit indépendant, bien moins de $K + 1000$ caractères.

Notre hypothèse de départ est donc fausse : la complexité de Kolmogorov n'est pas calculable.
{% enddetails %}

### Un nombre non calculable : $\Omega$ de Chaitin

Nous allons en montrer un nombre non calculable, dérivé du célèbre [nombre oméga de Chaitin](https://fr.wikipedia.org/wiki/Om%C3%A9ga_de_Chaitin), lui aussi non dénombrable.

Rangeons, comme on l'a fait pour la complexité de Kolmogorov, tous les programmes sans paramètres dans l'ordre lexicographique. Nommons les programmes selon cet ordre : $P_1$ le premier programme, $P_2$ le second, etc.

Le nombre  $\Omega$ est un réel entre 0 et 1 tel que sa $i$-ème décimal soit :

- égale à 1 si le programme $P_i$ s'arrête
- égale à 0 si le programme $P_i$ se s'arrête pas

Ce nombre existe mais n'est évidemment pas calculable car si on pouvait le faire, [le problème de l'arrêt](../arrêt-rice){.interne} serait décidable.
