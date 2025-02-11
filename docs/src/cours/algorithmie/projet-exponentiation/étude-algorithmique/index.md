---
layout: layout/post.njk
title: "Étude : exponentiation"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On va étudier deux algorithmes permettant de calculer $a^b$ à partir de deux entiers $a$ et $b$. Pour chaque algorithme on étudiera son fonctionnement selon 3 axes :

- fonctionnement
- preuve
- complexité

## <span id="algo-naif"></span> Algorithme naïf

Le calcul _naïf_ de l'exponentielle est basé sur sa définition mathématique, qui peut être décrite, pour deux entiers **strictement positifs** $x$ et $n$, par l'équation suivante :

<div>
$$
x^n = \left\{
    \begin{array}{ll}
        x \cdot x^{n-1} & \mbox{si } n > 1 \\
        x & \mbox{sinon.}
    \end{array}
\right.
$$
</div>

Bien que non nécessaire, la contrainte de positivité stricte pour $x$ et $n$ nous permet d'éviter tout cas particulier qui pourrait (tôt ou tard) advenir dans les preuves lorsque $x$ ou $n$ vaut 0.

{% exercice %}
Écrivez un algorithme récursif en python pour résoudre cette équation.
{% endexercice %}
{% details  "solution" %}

```pseudocode
algorithme puissance(nombre: entier, exposant: entier) → entier:
    si exposant == 1:
        rendre nombre
    rendre nombre * puissance(nombre, exposant - 1)
```

Cet algorithme est exactement la transcription de la définition mathématique, il est donc correct.

{% enddetails %}

Pour cette étude, nous allons uniquement utiliser des algorithmes non récursifs (ils sont dit itératifs). Pour créer l'algorithme itératif à partir d'une définition récursive, il faut pouvoir stocker les résultats intermédiaires dans une variable :

<span id="pseudo-code-naif"></span>

```pseudocode/
algorithme puissance(x: entier, n: entier) → entier:
    r ← x
    c ← n - 1
    tant que c > 0:
        r ← r * x
        c ← c - 1
    rendre r
```

C'est cet algorithme itératif que nous allons étudier maintenant.

### <span id="marche-naif"></span> Est-ce que ça marche ?

On teste l'algorithme itératif sur de petits exemples qui vont nous permettre d'appréhender son fonctionnement :

{% attention "**À retenir**" %}
On teste toujours ses algorithmes sur de petits nombres en se mettant à la place de l'ordinateur.

- on numérote chaque ligne
- on note sur une feuille les variables
- on exécute ligne à ligne en notant les différents résultats
- à la fin on vérifie que le retour de l'algorithme est bien correct

{% endattention %}

Les cas simples que l'on peut essayer sans peine, et permet de **tester les cas limites** :

- `n`{.language-} vaut 1
- `x`{.language-} vaut 2 ou 3 (un peu plus que les cas triviaux)

Puis un cas un peu plus compliqué pour **tester si les boucles fonctionnent bien** :

- `n`{.language-} vaut 2 ou 3
- `x`{.language-} vaut 2 ou 3

{% faire %}
Vérifiez que l'algorithme donne bien les bons résultats sur les exemples ci-dessus.
{% endfaire %}

Une fois qu'on est convaincu que ça fonctionne, on prouve sa finitude, son exactitude et on calcule sa complexité.

### <span id="preuve-naif"></span> Preuve

En deux temps. On commence par montrer qu'il se termine, puis on prouve qu'il calcule bien l'exponentiation.

#### <span id="finitude-naif"></span> Finitude

- `c`{.language-} est un entier qui diminue strictement à chaque boucle et la condition d'arrêt est lorsqu'il vaut 0.
- condition : il faut que `c`{.language-} soit un nombre positif pour que l'algorithme s'arrête. Donc `n`{.language-} doit être un nombre strictement positif.

{% attention "**À retenir**" %}
Pour des nombres, on préférera toujours des conditions d'arrêt larges (plus petit que, plus grand que, différent de) plutôt que des conditions d'égalité. Ceci pour deux raisons majeures :

- L'égalité entre réels n'existe pas en informatique, ces conditions ne fonctionneront donc pas avec eux.
- dans l'exemple ci-dessus mettre des exposants négatifs ou des nombres réels ne fait pas boucler infiniment notre algorithme

{% endattention %}

#### Preuve de l'algorithme

Le fonctionnement de l'algorithme est _à peu près_ clair si les entrées sont des entiers : il multiplie $a$ par lui-même $b$ fois grâce à une boucle. Une preuve par récurrence doit donc fonctionner, mais essayons de faire une _jolie_ preuve en exhibant un invariant de boucle.

{% note "**Invariant de boucle**" %}
Si `x`{.language-} et `n`{.language-} sont des entiers strictement positifs, on a l'invariant de boucle : $ r \cdot x^c = x^n $
{% endnote %}
{% details "Comment trouver cet invariant", "open" %}
Un invariant doit capturer en une phrase le but de la boucle. En regardant notre boucle on remarque qu'à chaque itération :

- $r$ est multiplié par $x$
- $c$ est décrémenté de 1

Comme $r$ et $c$ valent initialement $x$ et $n-1$ respectivement, on en conclut un premier invariant possible (il faudra encore le démontrer rigoureusement plus tard) : "à la fin de la $i$ème itération, $c=n-i-1$ et $r = x^{i+1}$".

Ceci pourrait être un invariant tout ce qu'il y a de plus correct, mais on peut faire plus élégant en injectant $i = n-c-1$, la première égalité, dans la seconde :

<div>
$$
r = x^{n-c-1+1} = x^{n-c}
$$
</div>

Ce qui donne l'invariant $r \cdot x^c = x^n$ qui tient en une ligne et n'a plus besoin de la variable auxiliaire $i$ qui compte le nombre d'itérations effectuées.

{%enddetails %}
{% info %}
L'invariant est joli car il n'a pas besoin du nombre d'itérations passées pour l'exprimer. Ce ne sera pas toujours le cas.
{% endinfo %}

Prouvons cet invariant.

Juste avant la première itération de la boucle, `r = x`{.language-} et `c = n-1`{.language-} notre invariant est donc vérifié. On suppose l'invariant vrai au début de la boucle $i$. Comme expliqué dans la partie sur les [preuves d'algorithmes](../preuve-algorithme), on met un `'` aux variable après l'itération :

- `x' = x`{.language-}
- `n' = n`{.language-}
- `r' = r * x`{.language-}
- `c' = c - 1`{.language-}

On a alors :

$$
r' \cdot {(x')}^{c'} = (r \cdot x) \cdot x^{c - 1} = r \cdot x^c = x^n = {(x')}^{n'}
$$

On a démontré notre invariant de boucle.

{% note %}
Notre invariant est vrai avant et après chaque itération, il est donc également vrai à la fin de l'algorithme, lorsque `c = 0`{.language-}. Et là : $r \cdot x^c = r = x^n$
{% endnote %}

### <span id="complexité-naif"></span> Complexité de l'algorithme naif

Ligne à ligne :

1. une affection : $\mathcal{O}(1)$
2. une soustraction et une affection : $\mathcal{O}(1)$
3. une boucle de $\mathcal{O}(n)$ itération (`c`{.language-} vaut initialement `n`{.language-} et est décrémentée de $1$ à chaque itération)
4. une multiplication et une affection : $\mathcal{O}(1)$
5. une soustraction et une affection : $\mathcal{O}(1)$
6. retour de la fonction : $\mathcal{O}(1)$

Ce qui donne une complexité de :

<div>
$$
\begin{array}{lcl}
C & = & \mathcal{O}(1) + \\
& & \mathcal{O}(1) + \\
& & \mathcal{O}(n) \cdot ( \\
& & \mathcal{O}(1) + \\
& & \mathcal{O}(1)) + \\
& & \mathcal{O}(1)\\
& = & 2 \cdot \mathcal{O}(1) + \mathcal{O}(n) \cdot (2 \cdot \mathcal{O}(1)) + \mathcal{O}(1)\\
&=& 3 \cdot \mathcal{O}(1) + 2 \cdot \mathcal{O}\mbox(1) \cdot \mathcal{O}\mbox(n)\\
&=& \mathcal{O}(3 \cdot 1) + \mathcal{O}\mbox(2\cdot 1 \cdot n)\\
&=& \mathcal{O}(3) + \mathcal{O}\mbox(2n)\\
&=& \mathcal{O}(1) + \mathcal{O}(n)\\
&=& \mathcal{O}(1 + n)\\
C&=& \mathcal{O}(n)\\
\end{array}
$$
</div>

## <span id="algo-rapide"></span> Exponentiation indienne

Aussi appelé [exponentiation rapide](https://fr.wikipedia.org/wiki/Exponentiation_rapide), cette façon de calculer l'exponentielle est basée sur l'équation suivante, pour deux entiers positifs $x$ et $n$ :

<div>
$$
x^n = \left\{
    \begin{array}{ll}
        x & \mbox{si } n = 1 \\
        x \cdot x^{n-1}  &\mbox{si } n > 1 \mbox{ est impair}\\
        (x^2)^{(n/2)}  &\mbox{si } n  \mbox{ est pair}\\
    \end{array}
\right.
$$
</div>

{% exercice %}
Écrivez un algorithme récursif pour résoudre cette équation.
{% endexercice %}
{% details  "solution" %}

```pseudocode/
algorithme puissance(x: entier, n: entier) → entier:
    si n == 1:
        rendre x
    sinon si n % 2 ≠ 0:
        rendre x * puissance(x, n - 1)

    rendre puissance(x * x, n // 2)
```

On a utilisé deux choses :

- L'opérateur `%`{.language-} signifie _modulo_ en python : il retourne le reste de la division entière. L'algorithme s'en sert pour vérifier si `exposant`{.language-} est pair (reste de la division entière par 2 vaut 0) ou impair (reste de la division entière par 2 vaut 1)
- la division entière `//`{.language-} pour s'assurer que exposant reste un entier. Le type de `4 / 2`{.language-} en python est un réel alors que le type de `4 // 2`{.language-} est un entier.

Cet algorithme est exactement la transcription de la définition mathématique, il est donc correct.

Remarquez que cette version n'est cependant par récursive terminal. On pourrit le faire en ajoutant un accumulateur comme paramètre.
{% enddetails %}

Pour cette étude, nous allons uniquement utiliser des algorithmes itératifs. En procédant comme la partie précédente on obtient :

<span id="pseudo-code-rapide"></span>

```pseudocode/
algorithme puissance(x: entier, n: entier) → entier:
    r ← x
    c ← n - 1

    tant que c > 0:
        si c % 2 == 1:
            r ← r * x
            c ← c - 1
        sinon:
            x ← x * x
            c ← c / 2

    rendre r
```

C'est cet algorithme itératif que nous allons étudier maintenant.

### <span id="marche-rapide"></span> Est-ce que ça marche ?

Comme pour l'algorithme naïf, on vérifie que tout fonctionne avec les cas simples :

- `n`{.language-} vaut 1 ou 2
- `x`{.language-} vaut 2 ou 3 (un peu plus que les cas triviaux)

Enfin, comme l'algorithme vérifie si `c`{.language-} est pair ou impair, on peut essayer un exposant un peu plus grand, par exemple :

- `n = 7`{.language-}
- `x = 2`{.language-} (pas trop grand pour pouvoir calculer facilement les résultats de tête)

{% faire %}
Vérifiez que l'algorithme donne bien les bons résultats sur les exemples ci-dessus.
{% endfaire %}

### <span id="finitude-rapide"></span> Preuve de finitude

De même que pour l'algorithme simple, `c`{.language-} diminue strictement à chaque boucle (ou il diminue de `-1`{.language-} ou il est divisé par 2). Si `n`{.language-} est un entier strictement positif en entrée, `c`{.language-} reste entier après chaque boucle (on ne le divise par 2 que s'il est pair) et est strictement plus petit : l'algorithme va s'arrêter à un moment.

### <span id="preuve-rapide"></span> Preuve de l’algorithme

On va montrer que l'invariant de l'algorithme naïf fonctionne aussi. En notant `X`{.language-} la valeur initial de `x`{.language-} en entrée de l'algorithme, on a l'invariant suivant :

$$
r \cdot x^c = X^n
$$

Juste avant la première itération de la boucle, $r = x$, $x = X$ et et $c = n-1$ notre invariant est donc vérifié au départ de l'algorithme. On suppose l'invariant vrai au début de la boucle d'itération $i$. Regardons comment les variables ont été modifiées lors de cette itération :

- si compteur est impair on a :
  - $c' = c - 1$
  - $r' = r \cdot x$
  - $x' = x$
  - l'invariant vaut alors en fin d'itération : $r \cdot x^c = (r \cdot x) \cdot x^{c - 1} = r' \cdot (x')^{c'}$
- si compteur est pair on a :
  - $c' = c / 2$
  - $r' = r$
  - $x' = x \cdot x$
  - l'invariant vaut alors en fin d'itération : $r \cdot x^c = r \cdot (x \cdot x)^{c/2}  = r' \cdot (x')^{c'}$

Dans tous les cas, l'invariant est toujours vérifié puisqu'en début de boucle notre invariant vaut $r \cdot x^c = X^n$

Notre invariant est vrai avant et après chaque itération, il est donc également vrai à la fin de l'algorithme, lorsque $c = 0$, et là : $r \cdot x^c = r = X^n$

### <span id="complexité-rapide"></span> Complexité de l'exponentiation indienne

Pourquoi s'embêter avec la parité de compteur ? Parce que ça permet d'aller vachement plus vite !

On va le démontrer petit à petit, mais commençons par analyser ligne à ligne la complexité.

En notant $K$ le nombre de fois où l'on est rentré dans la boucle `tant que`{.language-} de la ligne 4 on a une complexité ligne à ligne de :

1. une affectation : $\mathcal{O}(1)$
2. une affectation : $\mathcal{O}(1)$
3. —
4. une comparaison en $\mathcal{O}(1)$ et $K$ itérations de boucle
5. une opération de division entière et un test : $\mathcal{O}(1)$
6. une opération et une affectation : $\mathcal{O}(1)$
7. une opération et une affectation : $\mathcal{O}(1)$
8. —
9. une opération et une affectation : $\mathcal{O}(1)$
10. une opération et une affectation : $\mathcal{O}(1)$
11. —
12. un retour de fonction : $\mathcal{O}(1)$

Ce qui donne une complexité de :

<div>
$$
\begin{array}{lcll}
C & = & \mathcal{O}(1) + &\\
&  & \mathcal{O}(1) + &\\
&  & K \cdot (\mathcal{O}(1) + &\\
& & \mathcal{O}(1) + &\\
& & \mathcal{O}(1) + &\mbox{(ligne 7 ou ligne 10)}\\
& & \mathcal{O}(1)) + & \mbox{(ligne 8 ou ligne 11)}\\
& & \mathcal{O}(1)&\\
&=& 2 \cdot \mathcal{O}(1) + K \cdot (5\cdot \mathcal{O}(1)) + \mathcal{O}(1)&\\
&=& 3 \cdot \mathcal{O}(1) + K \cdot 5 + &\\
C&=&\mathcal{O}(K)&\\
\end{array}
$$
</div>

La complexité est de l'ordre du nombre de fois où l'on rentre dans la boucle `tant que`{.language-} : c'est à dire le nombre de fois où `c`{.language-} a été modifié sans être égal à 0.

#### Nombre de fois où compteur est impair

Si à l'itération numéro $i$ compteur est impair, il sera pair à l'itération $i + 1$ car `c' = c - 1`{.language-} dans ce cas là.

On a donc que : **le nombre d'itérations où compteur est impair est au pire égal au nombre de fois où il est pair**

#### Nombre de fois où le compteur est pair

A chaque fois où compteur est pair, on le divise par 2. Si $K_p$ est le nombre de fois où le compteur a été pair, on a que : $2^{K_p} \leq n$.

Comme $n$ est un entier, il existe un nombre $p$ tel que $2^p \leq n < 2^{p + 1}$.

On ne peut donc pas diviser $n$ par 2, ou un nombre plus petit que lui, plus de $p$ fois. Ce nombre est exactement la partie entière de $\log_2(n)$. En effet :

<div>
$$
\begin{array}{lcccl}
    2^p &\leq &n &<& 2^{p + 1}\\
    \log_2(2^p) &\leq &\log_2(n) &< &\log_2(2^{p + 1}) \mbox{ (car la fonction est croissante)} \\
    p &\leq &\log_2(n) &<& p + 1
\end{array}
$$
</div>

{% info %}
Pour tout nombre $x$, le nombre de fois où on peut diviser le diviser par $d$ est $\log_d(x)$
{% endinfo %}

On a donc que : **le nombre d'itérations où `c`{.language-} est pair est au pire égal à $\log_2(n)$**

#### Nombre de fois où l'on rentre dans la boucle

Le nombre de fois où l'on rentre dans la boucle est égal au nombre de fois où le compteur est pair plus le nombre de fois où le compteur est impair, c'est donc au pire égal à deux fois le nombre de fois où compteur est pair, c'est à dire $2 \cdot \log_2(c)$ pour la valeur initiale de compteur.

Comme `c`{.language-} vaut initialement `n`{.language-}, le nombre de fois où l'on rentre dans la boucle est de l'ordre de $\mathcal{O}(\log_2(n))$ donc en $\mathcal{O}(\ln(n))$.

Comme les autres lignes sont en $\mathcal{O}(1)$ on a une complexité de l'algorithme en $\mathcal{O}(\ln(n))$.

Cette complexité est très faible ! Comparez par exemple : $2^{16} = 65536$ opérations et $\log_2(65536) = 16$ opérations.

Cette différence va aller exponentiellement lorsque compteur augmente, par exemple entre $2^{100} = 1267650600228229401496703205376$ et $100$ opérations

## Complexité du problème

{% lien %}
Cet exemple est traité dans le volume 2, partie 4.6.3, de _The Art of Computer Programming_ de Knuth.
{% endlien %}

Peut-on faire mieux que l'exponentiation indienne pour calculer $x^n$ ? Remarquez que la complexité des algorithmes vus (itératif naïf et exponentiation indienne) dépendent exclusivement du nombre de multiplications utilisées :

- $n$ multiplications pour l'algorithme naïf itératif
- $\mathcal{O}(\log_2(n))$ multiplications pour l'algorithme de l'exponentiation indienne

On peut alors chercher à minimiser le nombre de multiplications de l'algorithme d'exponentiation :

{% note "**Question ?**" %}
Quel est le nombre minimum de multiplications nécessaires pour calculer $x^n = x \cdot \ldots \cdot x \cdot \ldots \cdot x$ à partir de $x$ ?
{% endnote %}

Par exemple si $n=4$, on a besoin de 2 multiplications :

1. $x_1 = x \cdot x = x^2$
2. $x_2 = x_1 \cdot x_1 = x^4$

Et on a besoin de 4 multiplications si $n=10$ (on le prouve en vérifiant qu'il est impossible d'aller plus loin que $x^8$ en 3 multiplications) :

1. $x_1 = x \cdot x = x^2$
2. $x_2 = x_1 \cdot x_1 = x^4$
3. $x_3 = x_2 \cdot x_2 = x^8$
4. $x_4 = x_3 \cdot x_1 = x^{10}$

Avant de voir le cas général, allons un peu plus loin en comptant le nombre de multiplications utilisé par nos 2 algorithmes.

{% exercice %}
Combien de multiplications sont nécessaires pour calculer $x^{15}$ si on utilisait l'exponentiation naïf ?
{% endexercice %}
{% details "solution" %}

On a besoin de 14 multiplications. Pour calculer $x^n$ ($n > 0$), on rentre $n-1 \geq 0$ fois dans la boucle.

1. $x_0 = x$
2. $x_1 = x \cdot x = x^2$
3. $x_2 = x_1 \cdot x = x^3$
4. ...
5. $x_i = x_{i-1} \cdot x = x^{i+1}$
6. ...
7. $x_{14} = x_{13} \cdot x = x^{15}$

{% enddetails %}

Le nombre de multiplications effectuées en utilisant l'exponentiation indienne est bien inférieure :

{% exercice %}
Montrez que 6 multiplications sont nécessaires si on utilisait l'exponentiation indienne pour calculer $x^{15}$.
{% endexercice %}
{% details "solution" %}

L'algorithme de l'exponentiation indienne multiplie alternativement $r$ ou $x$ selon la parité de $c$. Pour calculer $x^{15}$ il procède ainsi :

1. $c = 15-1 = 14$ : une multiplication de $x$
2. $c = 14 / 2 = 7$ : une multiplication de $r$
3. $c = 7 - 1 = 6$ : une multiplication de $x$
4. $c = 6 / 2 = 3$ : une multiplication de $r$
5. $c = 3 - 1 = 2$ : une multiplication de $x$
6. $c = 2 /2 = 1$ : une multiplication de $r$
7. $c = 1 - 1 = 0$ : on ne fait plus de multiplications

On a eu besoin de 6 multiplications.

{% enddetails %}

Ce n'est pourtant pas le nombre minimum :

{% exercice %}
Montrez que l'on peut calculer $x^{15}$ en uniquement 5 multiplications.
{% endexercice %}
{% details "solution" %}

1. $x_1 = x \cdot x = x^2$
2. $x_2 = x_1 \cdot x = x^3$
3. $x_3 = x_2 \cdot x_2 = x^6$
4. $x_4 = x_3 \cdot x_3 = x^{12}$
5. $x_5 = x_4 \cdot x_2 = x^{15}$

{% enddetails %}

L'exponentiation indienne n'a donc pas exactement le nombre minimum de multiplications possible !

Sous l'angle du nombre de multiplications, le calcul d'une exponentielle $x^n$ peut s'écrire comme :

<span id="suite-multiplicative"></span>
{% note "**Définition**" %}

une **_suite multiplicative pour $x^n$_** est une suite finie $(a_i)_{0\leq i \leq r}$ telle que :

- $a_0 = x$
- $a_r = x^n$
- pour tout $i>0$, il existe $j$ et $k$ tels que $a_i = a_j \cdot a_k$ avec $0 \leq j \leq k < i$

{% endnote %}

Commençons par montrer que nos deux algorithmes peuvent s'écrire sous ce formalisme :

<span id="multiplicatif-naif"></span>
{% exercice %}
Écrivez la forme de la suite multiplicative pour $x^n$ $(a_i)_{0\leq i \leq r}$ correspondant à l'algorithme d'exponentiation naïf.
{% endexercice %}
{% details "solution" %}

- $a_0 = x$
- $a_i = a_{i-1} \cdot a_0$ pour $0 < i \leq n-1$

Cette définition donne : $a_i = x^{i+1}$ et donc : $a_{n-1} = x^n$
{% enddetails %}

<span id="multiplicatif-indienne"></span>
{% exercice %}
Montrez que l'algorithme de l'exponentiation indienne peut s'écrire sous forme d'une suite multiplicative pour $x^n$ $(a_i)_{0\leq i \leq r}$ dont les premiers termes sont $a_i = x^{(2^i)}$ pour $i \leq \log_2(n)$.
{% endexercice %}
{% details "solution" %}

Les éléments de la suite correspondent aux valeurs successives de $r$. Cependant contrairement à l'exponentiation naïve qui change à chaque fois le résultat, l'exponentiation indienne change **et** le résultat **et** la valeur $x$. Pour être conforme à la définition (chaque élément de la suite dépend d'un élément précédent), il faut donc avoir à sa disposition les différentes valeurs de $x$ calculées par l'algorithme. Ces valeurs correspondent aux puissances $x^{2^i}$ pour $i=0$ à $i = \lfloor\log_2(n)\rfloor$ (partie entière (inférieure)).

Cette suite est bien multiplicative :

- $a_0 = x$
- $a_i = a_{i-1} \cdot a_{i-1}$ pour $1 \leq i \leq \log_2(n)$

Il nous reste ensuite à ajouter les éléments restant, c'est à dire tous les cas où le compteur est impair dans l'exécution de l'algorithme et qui correspondront à des $a_j = a_{j-1} \cdot a_i$ avec $1 \leq i \leq \log_2(n) \leq j$ qui correspondent au premier cas impairs de l'exécution de l'algorithme tel que $a_{j_0} = a_{i} \cdot a_{i'}$.

Cela donne la suite :

- $a_0$
- $a_1 = a_0 \cdot a_0$
- $a_2 = a_1 \cdot a_1$
- ...
- $a_i = a_{i-1} \cdot a_{i-1}$
- $a_j = a_{0} \cdot a_{1}$ (premier impair)
- $a_{j+1} = a_{j} \cdot a_{2}$
- $a_{j+2} = a_{j+1} \cdot a_{3}$
- ...
- $a_{m} = a_{m-1} \cdot a_{\log_2(n)}$

{% enddetails %}
{% exercice %}
Que donne cette suite pour $n=15$ ? et pour $n=10$ ?
{% endexercice %}
{% details "solution" %}
Pour n=15 :

- $a_0 = x$
- $a_1 = a_0 \cdot a_0 = x^2$
- $a_2 = a_1 \cdot a_1 = x^4$
- $a_3 = a_2 \cdot a_2 = x^8$
- $a_4 = a_0 \cdot a_1 = x^3$ (premier impair)
- $a_5 = a_4 \cdot a_2 = x^7$
- $a_6 = a_5 \cdot a_3 = x^{15}$

Pour n=10 :

- $a_0 = x$
- $a_1 = a_0 \cdot a_0 = x^2$
- $a_2 = a_1 \cdot a_1 = x^4$
- $a_3 = a_2 \cdot a_2 = x^8$
- $a_4 = a_1 \cdot a_3 = x^{10}$ (premier impair)

{% enddetails %}

On peut maintenant montrer que toute suite multiplicative pour $x^n$ possède au moins $\log_2(n)$ éléments. On commence par remarquer et prouver par récurrence le résultat suivant :

{% exercice %}
Pour toute suite multiplicative $(a_i)_{0\leq i \leq r}$ pour $x^n$, on a toujours : $a_i \leq x^{2^i}$ (avec $2^0 = 1$)
{% endexercice %}
{% details "solution" %}
On le montre par récurrence.

C'est vrai pour $i=0$ puisque $a_0 = x =x^{2^0}$. On suppose la propriété vraie pour tout $j \leq i$ et on considère $i+1$. On a $a_{i+1} = a_j \cdot a_k$. Comme $k \leq j \leq i$, l'hypothèse de récurrence est satisfaite pour $a_j$ et $a_k$, donc : $a_{i+1} = a_j \cdot a_k \leq x^{2^j} \cdot x^{2^k} \leq x^{2^{i}} \cdot x^{2^{i}} = x^{2^{i+1}}$. Ce qui conclut la récurrence.

{% enddetails %}

Ceci permet de montrer que :

{% note "**Proposition**" %}
Toute suite multiplicative pour $x^n$ $(a_i)_{0\leq i \leq r}$ est telle que :

<div>
$$
\log_2(n) \leq r
$$
</div>
{% endnote %}
{% details "preuve", "open" %}

Comme $a_r = x^n$, on a $n \leq 2^r$ ce qui donne, en passant au log : $\log_2(n) \leq r$.
{% enddetails %}

Ceci permet de dire que :

{% note "**Proposition**" %}
Tout algorithme calculant l'exponentielle $x^n$ est en $\Omega(\ln(n))$
{% endnote %}
{% details "preuve", "open" %}

Il faut toujours au moins $\log_2(n)$ multiplications donc la complexité est forcément supérieure à ce nombre.
{% enddetails %}

L'exponentiation indienne n'a donc certes pas le nombre minimum de multiplications, mais son ordre de grandeur est optimal !

Ceci nous permet d'écrire :

{% note "**Proposition**" %}
La complexité du problème de l'exponentiation est en $\Theta(\log_2 (n))$.
{% endnote %}
{% details "preuve", "open" %}
Comme la complexité de l'algorithme de l'exponentiation indienne est en $\mathcal{O}(\ln(n))$, la proposition précédente permet de conclure.
{% enddetails %}

Terminons cette partie en montrant que la longueur minimale d'une suite multiplicative pour $x^n$ est **toujours** en $\mathcal{O}(\ln(n))$.

{% exercice %}
En remarquant que si $b = b_0\dots b_k$ est la représentation binaire d'un nombre alors la représentation binaire de $b/2$ est $b / 2 = b_1\dots b_k$, déduire que le nombre de fois où le compteur est impair dans l'algorithme de l'exponentiation indienne est égal au nombre de 1 de la représentation binaire de $n-1$, noté $b(n-1)$.
{% endexercice %}
{% details "solution" %}
Un nombre est impair si le premier bit de sa représentation binaire vaut 1. Le nombre $b // 2^i$ est impair si $b_i = 1$.

On conclut la preuve en remarquant que tout au long de l'algorithme, le compteur `c`{.language-} vaut soit :

- $b // 2^i$ si ce nombre est pair
- $b // 2^i - 1$ sinon

{% enddetails %}

{% exercice %}
En déduire que la longueur de la suite pour l'exponentiation indienne est :

$$
\lfloor\log_2(n)\rfloor + b(n-1) + 1
$$

Avec $\lfloor x\rfloor$ la partie entière inférieure de $x$ et $b(x)$ le nombre de bits à 1 de la représentation binaire de $x$.
{% endexercice %}
{% details "solution" %}
Les premiers éléments de la suite sont au nombre de $\lfloor\log_2(n)\rfloor + 1$ (les $a_i = x^{2^i}$ tant que $a_i < x^n$), les derniers éléments étant ajoutés à chaque fois que le compteur est impair.
{% enddetails %}

En notant $l(n)$ la taille minimale d'une suite calculant $x^n$, on a alors :

$$
\log_2(n) \leq l(n) \leq \lfloor\log_2(n)\rfloor + b(n-1) + 1
$$

Et donc, puisque $b(n-1) \leq \log_2(n)$ :

$$
\log_2(n) \leq l(n) \leq 2 \log_2(n) + 1
$$

L'encadrement ci-dessus est déjà très bon, il n'y a qu'un facteur 2 entre le minorant et le majorant. On peut même aller plus loin et montrer que $l(n) \sim \log_2 (n)$, nous ne ferons cependant pas la preuve ici (elle est longue et pas évidente du tout).

## Conclusions

- la procédure utilisée pour l'étude de ces deux algorithmes est générale, vous pouvez (et devez) l'appliquer à l'étude de tout nouvel algorithme
- il ne faut jamais penser que l'on ne peut pas faire mieux pour un algorithme. Si vous ne connaissiez pas l'exponentiation indienne, il vous aurait été difficile de penser que l'on peut faire mieux que l'algorithme naïf pour calculer une exponentielle
- un informaticien ferait beaucoup de sacrifices pour obtenir une complexité en $\mathcal{O}(\ln(n))$ tellement c'est efficace
- on peut chercher la complexité minimale pour résoudre un problème et la comparer à des algorithmes connus.
