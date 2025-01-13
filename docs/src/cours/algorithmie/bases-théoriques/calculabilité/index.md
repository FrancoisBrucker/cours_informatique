---
layout: layout/post.njk
title: Calculabilité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On a vu qu'il y a plus de nombres réels que d'algorithmes : il existe donc forcément des choses que ne peut pas calculer un algorithme. On va s'intéresser ici à deux types de choses que peut (ou ne peut pas) calculer un algorithme : des fonctions et des nombre.

Cette introduction à ce l'on appelle [calculabilité](https://fr.wikipedia.org/wiki/Th%C3%A9orie_de_la_calculabilit%C3%A9) en informatique théorique doit vous permettre de comprendre qu'un algorithme ne peut pas tout faire.

{% lien %}

Vous pouvez consulter le lien suivant sur l'émergence en mathématiques de la notion de **_calculabilité_** :
<https://perso.ens-lyon.fr/pierre.lescanne/PUBLICATIONS/calculabilite.pdf>
{% endlien %}

## Algorithmes et fonctions

On a vu qu'un algorithme et tout ce qu'il manipulait pouvait être considéré comme une suite finie de 0 et de 1. On en déduit immédiatement la proposition suivante :

<span id="algorithme-fonction"></span>
{% note "**Proposition**" %}
Un algorithme est une fonction :

$$f: \\{0, 1\\}^\star \rightarrow \\{0, 1\\}^\star$$

Où $\\{0, 1\\}^\star$ est l'ensemble des suites finies de $0$ et de $1$.
{% endnote %}

Comme une suite finie de 0 et de 1 est une écriture binaire d'un entier positif on a aussi :

<span id="algorithme-fonction-N"></span>
{% note "**Proposition**" %}
Un algorithme est une fonction :

$$f: \mathbb{N} \rightarrow \mathbb{N}$$

{% endnote %}

Par exemple la fonction identité est un algorithme :

```text
Nom : identité
Entrées :
    n : un entier
Programme :
    rendre n
```

De même, je vous laisse reprendre vos cours de primaire pour le faire, les fonctions $f(n) = 42 \cdot n$ ou encore $f(n) = n^2$ sont des algorithmes. On dit que ces fonctions sont **_calculables_** :

{% note "**Définition**" %}
Une fonction $f: \mathbb{N} \rightarrow \mathbb{N}$ est **_calculable_** s'il existe un algorithme qui permet de la calculer.

{% endnote %}

Montrons tout de suite que cette notion a un sens, c'est à dire que l'ensemble des fonctions calculables est strictement inclue dans l'ensemble des fonctions de $\mathbb{N}$ dans $\mathbb{N}$ :

{% note "**Proposition**" %}
Il y a strictement plus de fonctions $f: \mathbb{N} \rightarrow \mathbb{N}$ que de nombres entiers.

{% endnote %}
{% details "preuve", "open" %}
La preuve est identique à celle du [Théorème montrant qu'il y a strictement plus de réels que d'entiers](../définition/#diagonale-cantor){.interne}.

Comme les fonctions $f^k: \mathbb{N} \rightarrow \mathbb{N}$ définies telles que $f^k(x) = x + k$ sont deux à deux différentes lorsque $k$ parcourt $\mathbb{N}$, on en déduit qu'il existe au moins autant de fonctions $f: \mathbb{N} \rightarrow \mathbb{N}$ que d'entiers.
On suppose alors qu'il y en a autant, donc qu'il existe une bijection entre les fonctions $f: \mathbb{N} \rightarrow \mathbb{N}$ et les nombres entiers.

On peut alors numéroter chaque fonction $f_0$, $f_1$, $\dots$, $f_n$. Cet ordre nous permet de construire la fonction $g: \mathbb{N} \rightarrow \mathbb{N}$ telle que $g(i) = f_i(i) + 1$ pour tout $i \in \mathbb{N}$. Mais ceci est impossible puisque $g \neq f_i$ pour tout $i$ ($g(i) \neq f_i(i)$ par définition de $g$) : il existe strictement plus de fonctions $f: \mathbb{N} \rightarrow \mathbb{N}$ que d'entiers.

{% enddetails %}

Comme il existe au plus autant d'Algorithmes que de nombres entiers, il y a bien des fonctions $f: \mathbb{N} \rightarrow \mathbb{N}$ intraduisibles par un algorithme.

## Exemple de fonction calculable

La plus célèbre des fonctions calculable est bien sur la fonction d'Ackermann :

{% aller %}
[Fonction d'Ackermann](./ackermann){.interne}
{% endaller %}

## Nombres calculables

{% note "**définition**" %}
Un nombre $x$ est **_calculable_** s'il existe un algorithme $A$ tel que :

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

On en déduit immédiatement que **tous les rationnels sont calculables** : il suffit d'utiliser [l'algorithme de la division de deux entiers décimaux](https://fr.wikipedia.org/wiki/Division#Algorithmes_de_la_division_de_nombres_d%C3%A9cimaux) appris en primaire.

Enfin, certains réels sont calculables, même si leurs nombres de décimales sont infinis. Par exemple tous les réels qui sont des limites de suites elles mêmes calculables :

{% note "**Proposition**" %}
Soit $(u_n)_{n \geq 1}$ une suite réelle.

Si :

- $\lim_{n\rightarrow +\infty}u_n = x$
- il existe deux algorithmes $A$ et $B$ tes que :
  - $A(n)$ rende la partie entière de $u_n$
  - $B(n)$ rende les $n$ premières décimales de $u_n$

Alors le réel $x$ est calculable.

{% endnote %}
{% details "preuve", "open" %}

Comme $u_n$ converge vers $x$, pour tout $i> 0$, il existe $N_i$ tel que $\mid x - u_n\mid < 10^{-i}$ pour tout $n > N_i$. Si l'on veut calculer la $i$-ème décimale de $x$, Il suffit de calculer $u_{max(i, N_{i})}$ et de prendre sa $i$-ème décimale.

{% enddetails %}

La proposition ci-dessus permet de montrer que la plupart des réels connus sont calculables. Par exemple $\pi$ puisqu'il est la limite de [la série de Leibniz de $\pi$](https://fr.wikipedia.org/wiki/Formule_de_Leibniz#S%C3%A9rie_altern%C3%A9e). Ce résultat s'étend naturellement aux fonctions admettant [développement en séries entières](https://fr.wikipedia.org/wiki/Formulaire_de_d%C3%A9veloppements_en_s%C3%A9ries) comme $cos(x)$, $sin(x)$ ou encore $\sqrt{x}$ qui sont calculables pour tout $x$ calculable.

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
La quasi-totalité des nombres réels utilisées en mathématiques en tant que tel ($\pi$, $e$, etc) ou comme résultat de fonctions (comme $cos$, $sin$, racine carrée, etc) sont calculables : il existe un algorithme prenant un entier $i$ en paramètre et qui rend sa $i$ème décimale.
{% endnote %}
{% attention %}
Attention cependant à ne pas confondre le réel en tant que tel (non calculable puisqu'il possède une infinité de décimale) et son approximation que l'on peut utiliser dans les calculs.
{% endattention %}

## Cas limites

Il existe tout un tas de cas limites rigolos. Nous allons en voir deux.

### Fonctions calculables sans algorithme connu

Il existe aussi des fonctions que l'on sait calculable mais dont on ne connaît pas l'algorithme pour les calculer. Par exemple :

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

Le texte ci-dessus n'est **pas** un programme car le "il existe" n'est pas une opération élémentaire que je peux effectuer de tête. De plus, sans connaissance a priori, je suis obligé de tester toutes les décimales de $\pi$ pour répondre à la question du "il existe", ce qui fait que s'il n'existe pas n "5" successifs, le programme ne s'arrêtera pas.

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
        rendre 1
    sinon:
        rendre 0
```

Dans les deux cas, c'est un algorithme. Le problème est que l'on ne sait pas si π est [un nombre univers](https://fr.wikipedia.org/wiki/Nombre_univers) et donc on ne sait pas lequel des deux algorithmes est le bon.

{% note "**À retenir**" %}
Savoir qu'on peut créer un algorithme pour calculer une fonction ne signifie pas que c'est facile de le faire. Il faut souvent avoir des connaissances annexes, hors algorithmie, poussée sur le problème à résoudre pour le faire
{% endnote %}

On va montrer deux exemples de fonctions calculables. Ces deux fonctions sont parfois utilisées pour des tests de performance d'ordinateurs car est sont très gourmandes en temps de calcul.

### Fonction écran de fumée

La [fonction de Takeuchi](https://fr.wikipedia.org/wiki/Fonction_de_Takeuchi) est surprenante, bien malin qui sait ce qu'elle fait juste en la regardant.

{% note "**Définition**" %}

La [fonction de Takeuchi](https://fr.wikipedia.org/wiki/Fonction_de_Takeuchi) est définie pour tous entiers positifs $x$, $y$ et $z$ telle que :

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
{% endnote %}

Pour prouver que cette fonction est calculable il faut montrer deux choses :

1. la véracité de la définition
2. que le nombre de récursion n'est pas infini

Faisons la première proposition avec un exercice :

{% exercice %}
Montrez par récurrence sur $k = x+y+z$ que si la définition de la fonction de Takeuchi est bien définie (le nombre de récursion est fini), alors :

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

{% endexercice %}
{% details "corrigé" %}
On suppose que $\tau(x, y, z)$ existe pour tous $x, y, z \in \mathbb{N}$. On montre le résultat par récurrence sur $x+y+z= k$.

Si $x+y+z=0$, on a $x=y=z=0$ et $\tau(0, 0, 0) = 0$, la récurrence est vérifiée. On suppose la récurrence vraie pour $x+y+z=k$.

Pour $x+y+z=k+1$, on analyse tous les cas possibles :

- $x \leq y$ : Ok
- $x > y$ et $y \leq z$ : On a $\tau(x, y, z) = \tau(\tau(x-1, y, z), \tau(y-1, z, x), \tau(z-1, x, y))$ :
  - on a $y-1 \leq z$ donc (par hypothèse de récurrence) $\tau(y-1, z, x) = z$
  - soit $x-1 > y$ et $y \leq z$ et alors (par hypothèse de récurrence) $\tau(x-1, y, z) = z$ : $\tau(x, y, z) = \tau(z, z, ?) = z$
  - soit $x-1 \leq y$ et alors (par hypothèse de récurrence) $\tau(x-1, y, z) = y$ : $\tau(y, z, ?) = z$ (puisque $y \leq z$)
- $x > y > z$ : On a $\tau(x, y, z) = \tau(\tau(x-1, y, z), \tau(y-1, z, x), \tau(z-1, x, y))$
  - on a $z-1 < y< x$ et donc $\tau(x, y, z) =  \tau(\tau(x-1, y, z), \tau(y-1, z, x), x)$
  - on procède de même que précédemment en analysant tous les cas - $x-1 > y$ et $y-1>z$ : $\tau(x, y, z) = \tau(x-1, x, x) = x$ - $x-1 > y$ et $y-1=z$ : $\tau(x, y, z) = \tau(x-1, z, x) = x$ - $x-1 = y$ et $y-1>z$ : $\tau(x, y, z) = \tau(y, x, x) = x$ - $x-1 = y$ et $y-1=z$ : $\tau(x, y, z) = \tau(y, z, x) = x$

{% enddetails %}

Il nous reste à montrer que le nombre d'itération est bien fini. Ce n'est en effet pas parce que l'équation de récurrence admet une solution qu'on peut la calculer avec un algorithme, c'est à dire en temps fini. On utilise pour cela utiliser l'exercice précédent et une récurrence :

{% note "**Proposition**" %}

La fonction $\tau(x, y, z)$ de Takeuchi est bien définie en un nombre fini de récursion et sa valeur vaut :

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
{% endnote %}
{% details "preuve", "open" %}

On va encore une fois le prouver par récurrence sur $x+y+z= k$.

Si $x+y+z=0$, on a $x=y=z=0$ et $\tau(0, 0, 0) = 0$ en 0 récursion puisque $x \leq y$, la récurrence est vérifiée. On suppose la récurrence vraie pour $x+y+z=k$.

Pour $x+y+z=k+1$, on analyse tous les cas possibles :

- $x \leq y$ : Ok en 0 récursion
- $x > y$ et $y \leq z$ : On a $\tau(x, y, z) = \tau(\tau(x-1, y, z), \tau(y-1, z, x), \tau(z-1, x, y))$. Par hypothèse de récurrence $\tau(x-1, y, z)$, $\tau(y-1, z, x)$ et $\tau(z-1, x, y)$ existent et ne peuvent valoir (exercice précédent) que :
  - $\tau(y-1, z, x) = z$
  - soit $x-1 > y$ et $y \leq z$ et alors (par hypothèse de récurrence) $\tau(x-1, y, z) = z$
  - soit $x-1 \leq y$ et alors (par hypothèse de récurrence) $\tau(x-1, y, z) = y$

  On a alors soit $\tau(x, y, z) = \tau(z, z, ?)$, soit $\tau(x, y, z) = \tau(y, z, ?)$ ce qui donne sans nouvelle récursion $\tau(x, y, z) = \tau(z, z, ?) = \tau(y, z, ?) = z$ (on a $y \leq z$).

- $x > y > z$ : On a $\tau(x, y, z) = \tau(\tau(x-1, y, z), \tau(y-1, z, x), \tau(z-1, x, y))$. Par hypothèse de récurrence $\tau(x-1, y, z)$, $\tau(y-1, z, x)$ et $\tau(z-1, x, y)$ existent et ne peuvent valoir (exercice précédent) que :
  - $\tau(z-1, x, y) = x$
  - $x-1 > y$ et $y-1>z$ : $\tau(x, y, z) = \tau(x-1, x, x)$. Comme $x-1 \leq x$ on a $\tau(x, y, z) = x$ sans nouvelle récursion.
  - $x-1 = y$ et $y-1>z$ : $\tau(x, y, z) = \tau(y, x, x)$. Comme $x > y$ on a $\tau(x, y, z) = x$ sans nouvelle récursion
  - $x-1 > y$ et $y-1=z$ : $\tau(x, y, z) = \tau(x-1, z, x)$. On a $x-1 > z$ et $x > x-1$, on est ramené au cas précédent ($x > y$ et $y \leq z$) qui converge avec une récursion en plus
  - $x-1 = y$ et $y-1=z$ : $\tau(x, y, z) = \tau(y, z, x)$. On a $y > z$ et $x > y$, on est ramené au cas précédent ($x > y$ et $y \leq z$) qui converge avec une récursion en plus.

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

On a maintenant assez de billes pour démontrer la non-calculabilité de la complexité de Kolmogorov :

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

Rangeons, comme on l'a fait pour la complexité de Kolmogorov, tous les programmes sans paramètre dans l'ordre lexicographique. Nommons les programmes selon cet ordre : $P_1$ le premier programme, $P_2$ le second, etc.

Le nombre $\Omega$ est un réel entre 0 et 1 tel que sa $i$-ème décimal soit :

- égale à 1 si le programme $P_i$ s'arrête
- égale à 0 si le programme $P_i$ se s'arrête pas

Ce nombre existe mais n'est évidemment pas calculable car si on pouvait le faire, [le problème de l'arrêt](../arrêt-rice){.interne} serait décidable.
