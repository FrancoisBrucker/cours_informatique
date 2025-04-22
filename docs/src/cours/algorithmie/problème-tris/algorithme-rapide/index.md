---
layout: layout/post.njk 
title: "Algorithme du tri rapide"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Le tri rapide est un algorithme qui a été très utilisé par le passé. On le montre encore maintenant car c'est un exemple de [diviser pour régner](./#diviser-pour-régner){.interne} et, surtout, le calcul des complexités est très intéressant.

Le principe est ici de séparer le tableau en entrée `T`{.language-} en 2 tableaux `T1`{.language-} et `T2`{.language-} et une valeur nommé `pivot`{.language-} de tel sorte que :

- toutes les valeurs de `T1`{.language-} soient plus petites que `pivot`{.language-}
- toutes les valeurs de `T2`{.language-} soient strictement plus grande que `pivot`{.language-}

On a coutume de prendre pivot comme étant `T[0]`{.language-}.

Une fois ce découpage des données fait, la fonction `combiner`{.language-} est triviale puisqu'il suffit de concaténer `T1`{.language-} trié à `[T[0]]`{.language-} puis à `T2`{.language-} trié.

{% attention %}
Les preuves formelles de complexités sont ardues. On ne vous demande pas de les connaître (mais jetez-y un coup d'oeil elle valent cependant le détour).

**En revanche** vous devez intégrer les preuves intuitives car les arguments exposés sont courant et vous permettront de sentir la complexité de nombreux algorithmes.
{% endattention %}

## pseudo-code

En pseudo-code cela donne :

```pseudocode/
fonction combiner(T1: [entier], pivot: entier, T2: [entier])  → [entier]:
    T ← un nouveau tableau de taille T1.longueur + T2.longueur + 1
    i ← 0
    pour chaque e de T1
        T[i] ← e
        i ← i + 1

    T[i] ← pivot
    i ← i + 1

    pour chaque e de T2
        T[i] ← e
        i ← i + 1

    rendre T

algorithme rapide(T: [entier]) → [entier]:
    si T.longueur <= 1:
        rendre T

    l1 ← le nombre d'éléments de T[1:] ≤ T[0]
    T1 ← un nouveau tableau de longueur l1
    i1 ← 0
    l2 ← le nombre d'éléments de T[1:] > T[0]
    T2 ← un nouveau tableau de longueur l2
    i2 ← 0
    pour chaque e de T[1:]:
        si e ≤ T[0]:
            T1[i1] ← e
            i1 ← i1 + 1
        sinon:
            T2[i2] ← e
            i2 ← i2 + 1

    rendre combiner(rapide(T1), T[0], rapide(T2))
```

{% details "code python", "open" %}

En utilisant [des list comprehension](/cours/coder-et-développer/bases-python/structurer-son-code/conteneurs/listes/#list-comprehension){.interne} de python, le code est plus compacte et plus clair que sa version en pseudocode :

```python/
def rapide(T):
    if len(T) <= 1:
        return T

    pivot = T[0]

    T1 = [T[i] for i in range(1, len(T)) if T[i] <= pivot]
    T2 = [T[i] for i in range(1, len(T)) if T[i] > pivot]

    return rapide(T1) + [pivot] + rapide(T2)
```

Les _list comprehension_ sont un moyen clair et efficace de générer des listes. Utilisez-les !

{% enddetails %}

## <span id="preuve-rapide"></span> Preuve

Comme `rapide`{.language-} est une implémentation de la méthode diviser pour régner : on tri deux tableaux, le premier contenant les éléments plus petit que T[0], l'autre les éléments strictement plus grand puis on les recombine. Son fonctionnement est donc assuré **si** les récursions s'arrêtent.

C'est effectivement le cas ici puisque les tableaux  `T1`{.language-} et  `T2`{.language-} sont strictement plus petit que  `T`{.language-} et qu'il y a une condition d'arrêt sur la taille du tableau.

## <span id="complexités-rapide"></span> Complexités

En notant $n$ la taille de la liste on a comme équation de récurrence pour la complexité $C(n)$ :

<div>
$${
C(n) = \underbracket{\mathcal{O}(n)}_{\mbox{cr\'eation des tableaux}}{} + \underbracket{C(n_1) + C(n_2)}_{\mbox{r\'ecursions}}{}
}$$
</div>

Où $n_1$ est la taille du tableau de gauche et $n_2$ celle de droite ($n_1 + n_2 = n-1$). Pour trouver $n_1$ et $n_2$, il faut résoudre l'équation :

$${
C(n) = \mathcal{O}(n) + \max_{0 \leq i < n}(C(i) + C(n-i-1))
}$$

On va montrer que :

{% attention "**À retenir**" %}
Pour trier un tableau de longueur $n$, les complexités de `rapide`{.language-} sont :

- la complexité (maximale) est $C_{\max}(n) = \mathcal{O}(n^2)$,
- la complexité en moyenne est $C_{\mbox{moy}} =  \mathcal{O}(n\ln (n))$,
- la complexité minimale est $C_{\min}(n) = \mathcal{O}(n\ln (n))$,

{% endattention %}

Retenez les complexités ci-dessus et les raisons intuitives de leurs calculs. Si vous voulez aller plus loin, vous pouvez étudier les preuves formelles, surtout qu'elles sont jolies et vous apprendront à calculer des complexités dans des cas non triviaux.

### Complexité (maximale) du tri rapide

{% note "**Proposition**" %}
La complexité du tri rapide est en $\mathcal{O}(n^2)$ avec $n$ la taille tu tableau à trier.
{% endnote %}
{% details "preuve intuitive", "open" %}

La complexité maximale va arriver si un des deux tableaux est toujours vide. Par exemple lorsque le tableau est déjà trié.

Pour des tableaux triés, `T1`{.language-} ou `T2`{.language-} est vide et l'autre tableau est de taille $n-1$, ce qui donne une complexité de :

<div>
$$
\begin{array}{lcl}
C_{\mbox{tri\'e}}(n) &=& \mathcal{O}(n) + C_{\mbox{tri\'e}}(0) +  C_{\mbox{tri\'e}}(n-1)\\
&=&\mathcal{O}(n) + C_{\mbox{tri\'e}}(n-1)\\
&=& \mathcal{O}(n) + \mathcal{O}(n-1) + C_{\mbox{tri\'e}}(n-2)\\
&=& ...\\
&=& \sum_{i=1}^{n}\mathcal{O}(i) + C_{\mbox{tri\'e}}(0)\\
&=& \mathcal{O}(\sum_{i=1}^{n}i)\\
&=& \mathcal{O}(n^2)\\
\end{array}
$$
</div>

Et donc :

$$
C_{\max}(n) = \mathcal{O}(n^2)
$$
{% enddetails %}
{% details "preuve formelle" %}
Formellement, nous ne venons que de montrer que $\mathcal{O}(n^2) \leq C_{\max}(n)$. Pour conclure la preuve, il nous reste à montrer la réciproque, c'est à dire $\mathcal{O}(n^2) \geq C_{\max}(n)$.

Faisons-le par récurrence. Notre hypothèse de récurrence est : il existe $k$ tel que $C(n) \leq k \cdot n^2$
Cette hypothèse est trivialement vraie pour $n=1$ et supposons la vraie pour $n-1$. Examinons le cas $n$ :

<div>
$$
\begin{array}{lcll}
C_{\max}(n) & = & \mathcal{O}(n) + \max_{0 \leq i < n}(C_{\max}(i) + C_{\max}(n-i-1))&\\
& \leq & \mathcal{O}(n) + \max_{0 \leq i < n}(k\cdot i^2 + k\cdot(n-i-1)^2)&\text{par hypothèse de récurrence}\\
& \leq & \mathcal{O}(n) + \max_{0 \leq i < n}(k\cdot(i + n-i-1)^2)&\text{car } a^2+b^2 \leq (a+b)^2 \text{ pour des entiers positifs}\\
& \leq & \mathcal{O}(n) + \max_{0 \leq i < n}(k\cdot(n-1)^2)&\\
& \leq & \mathcal{O}(n) + k\cdot(n-1)^2&\\
& \leq & \mathcal{O}(n) + k\cdot n^2 -k(2n-1)&\\
& \leq & \mathcal{O}(n^2)&\\
\end{array}
$$
</div>

Notre hypothèse est démontrée.

On a finalement l'encadrement : $\mathcal{O}(n^2) \leq C_{\max}(n) \leq \mathcal{O}(n^2)$, ce qui nous permet de conclure que la complexité (maximale) du tri rapide pour un tableau de taille $n$ est $\mathcal{O}(n^2)$.
{% enddetails %}

### Complexité minimale du tri rapide

{% note "**Proposition**" %}
La complexité du tri rapide est en $\mathcal{O}(n\ln(n))$ avec $n$ la taille tu tableau à trier.
{% endnote %}
{% details "preuve intuitive", "open" %}

On a que $C(n) \geq \mathcal{O}(n)$, la complexité de l'algorithme croit donc de façon linéaire ou plus. Si la forme de $C(n)$ est sans point d'inflexion, au moins asymptotiquement, la courbe de complexité sera au-dessus de sa tangente : c'est une fonction convexe.

![croissance convexe](tris-4.png)

On a alors $C_{\min}(\frac{n}{k}) + C_{\min}(\frac{(k-1)n}{k}) \geq 2\cdot C_{\min}(\frac{n}{2})$. Il sera donc **toujours** plus intéressant de couper notre tableau en 2 exactement. Dans ce cas là, on a l'équation de récurrence : $C_\min(n) = \mathcal{O}(n) + 2 \cdot C_\min(\frac{n}{2})$ et [la preuve de l'algorithme fusion](../algorithme-fusion/#complexités-fusion){.interne} nous permet de conclure que :

$$
C_{\min(n)} = \mathcal{O}(n\ln(n))
$$

{% enddetails %}

{% info %}
De façon générale, les courbes de complexités sont sans points d'inflexions (d'où viendraient-ils de toute façon ?). Les complexités plus grande que $\mathcal{O}(n)$ sont donc (quasiment) toutes convexes.
{% endinfo %}
{% details "preuve formelle" %}
Faisons la preuve de complexité rigoureusement.

Pour chaque exécution de l'algorithme, on crée (au maximum) deux tableaux à partir du tableau $T$ passé en paramètre. On peut ranger ces créations par *étage*, comme le montre la figure suivante :

![étages récursions](./étages-récursions.png)

On lance l’algorithme à l'étage 0 avec $T_0$ comme tableau originel. Ce tableau crée (au maximum) les tableaux $T_1$ et $T_2$ à l'étage 1 qui eux-même vont créer d'autres tableaux qui formeront l'étage 2 et ainsi de suite.

Chaque tableau $T_i$ crée donc soit :

- 0 tableau
- 1 tableau nommé $T_{2\cdot i}$
- 2 tableaux nommés $T_{2\cdot i}$ et $T_{2\cdot i + 1}$

L'étage $k>1$ est ainsi formé d'au plus $2^{k-1}$ tableaux, allant des tableaux allant des indices $(\sum_{0\leq i \leq k - 2}2^i) +1$ à $(\sum_{0\leq i \leq k-1}2^i)$.

Comme chaque exécution de l'algorithme hors récursion est proportionnelle à la taille du tableau en entrée, la complexité totale de l'exécution de toutes les récursion de l'algorithme sera proportionnelle à la somme des tailles des tableaux qui la composent (le tableau de $T_i$ ayant $n_i$ éléments) :

<div>
$$
C = \mathcal{O}(\sum_{i} n_i)
$$
</div>

**La complexité minimale sera atteinte pour la plus petite somme de $n_i$. Nous allons montrer que cela arrive lorsque l'on coupe le tableau en 2 parts égales à chaque itération.**

Chaque élément est compté 1 fois pour chaque tableau qui le compose. Comme l'ensemble des tableaux ayant un élément $x$ donné forme un chemin allant de $T_1$ à un tableau $T_i$ pour lequel $x$ est choisi comme pivot. En notant $e(x)$ l'étage pour lequel l'élément $x$ de $T_0$ a été choisi comme pivot, la complexité $C$ de l'algorithme vaut alors également :

<div>
$$
C = \mathcal{O}(\sum_{x \in T_0}e(x))
$$
</div>

La complexité minimale va donc être atteinte pour des arbres les plus tassés possibles puisqu'un élément $x$ choisi tard comme pivot aura un $e(x)$ plus important qu'un élément choisi plus tôt comme pivot. Comme chaque arbre de chaque étage produit 1 pivot on en conclut que :

**La complexité minimale est atteinte si chaque étage $k$ est constitué du nombre maximum d'arbres, c'est à dire $2^k$**.

Comme le nombre total d'arbre vaut $n$ on en déduit que pour les arbres réalisant la complexité minimale, on a :

<div>
$$
n = 1 + \sum_{2 \leq k \leq K}2^{k-1} = 2^K - 1
$$
</div>

La hauteur minimale de l'arbre est donc atteinte pour $K \simeq \log_2(n)$ avec des rangées pleines. Cet arbre minimisera effectivement $C = \mathcal{O}(\sum_{x \in T_0}e(x))$ puisque toutes les couches minimales seront prises. Pour cet arbre on aura $K=\log_2(n)$ et :

<div>
$$
C_{\min} = \mathcal{O}(\sum_{x \in T_0}e(x)) = \sum_{1 \leq k \leq K}k\cdot 2^{k-1} = (K-1)2^{K} + 1 = \mathcal{O}(n\log_2(n))
$$
</div>

On a utilisé le fait que $\sum_{1 \leq k \leq K}k\cdot 2^{k-1} = (K-1)2^{K} + 1$, ce qui se démontre aisément par récurrence.

{% enddetails %}

### <span id="tri-rapide-complexité-moyenne"></span>Complexité en moyenne du tri rapide

{% note "**Proposition**" %}
La complexité en moyenne du tri rapide est en $\mathcal{O}(n\ln(n))$ avec $n$ la taille tu tableau à trier.
{% endnote %}
{% details "preuve intuitive", "open" %}

on utilise l'argument utilisé pour calculer la complexité en moyenne du [tri par insertion](../algorithme-insertion/#complexités-insertion){.interne}. Si les données sont aléatoires la moitié de `T[1:]`{.language-} est plus grande que `T[0]`{.language-}. De là, en moyenne, on va toujours couper le tableau en 2 parties (plus ou moins) égales.

Si l'on coupe toujours au milieu on a alors la même équation que pour la complexité minimale : $C(n) = \mathcal{O}(n) + 2 \cdot C(\frac{n}{2})$, ce qui donne une complexité de $\mathcal{O}(n\ln(n))$.

{% enddetails %}
{% details "preuve formelle" %}
Il faut résoudre l'équation :

$${
C_{\mbox{moy}}(n) = \mathcal{O}(n) + \sum_{0 \leq i < n}p_i(C_{\mbox{moy}}(i) + C_{\mbox{moy}}(n-i-1))
}$$

où $p_i$ est la probabilité que le pivot soit le $i+1$ plus petit élément du tableau.

Pour éviter de nous trimballer des $\mathcal{O}(n)$ partout, on va considérer que l'on y effectue $K\cdot n$ opérations où $K$ est une constante. On peut alors écrire :

$${
C_{\mbox{moy}}(n) = K\cdot n + \sum_{0 \leq i < n}p_i(C_{\mbox{moy}}(i) + C_{\mbox{moy}}(n-i-1))
}$$

De plus on va considérer que nos données sont équiprobables, c'est à dire que le pivot a la même probabilité d'être le $u$ème ou le $v$ ème plus petit élément du tableau : $p_i = \frac{1}{n}$. On a alors à résoudre :

$${
C_{\mbox{moy}}(n) = K\cdot n + \frac{1}{n}\sum_{0 \leq i < n}(C_{\mbox{moy}}(i) + C_{\mbox{moy}}(n-i-1))
}$$

Comme :

- $\sum_{0 \leq i < n}C_{\mbox{moy}}(i) = \sum_{1 \leq i \leq n}C_{\mbox{moy}}(i-1)$
- $\sum_{0 \leq i < n}C_{\mbox{moy}}(n-i-1) = \sum_{1 \leq i \leq n}C_{\mbox{moy}}(i-1)$

On a :

$${
C_{\mbox{moy}}(n) = K\cdot n + \frac{2}{n}\sum_{1 \leq i \leq n}C_{\mbox{moy}}(i-1)
}$$

Il va maintenant y avoir 2 astuces coup sur coup. La première astuce est de considérer l'équation $n\cdot C_{\mbox{moy}}(n) - (n-1)\cdot C_{\mbox{moy}}(n-1)$ qui va nous permettre d'éliminer la somme :

<div>
$$
\begin{array}{lcl}
n\cdot C_{\mbox{moy}}(n) - (n-1)\cdot C_{\mbox{moy}}(n-1) & = & K\cdot n^2 +2\sum_{1 \leq i \leq n}C_{\mbox{moy}}(i-1)\\
&&- K\cdot (n-1)^2 - 2\sum_{1 \leq i \leq n-1}C_{\mbox{moy}}(i-1)\\
&=& K(n^2 - (n-1)^2) + 2\cdot C_{\mbox{moy}}(n-1)\\
&=& K(2n - 1) + 2\cdot C_{\mbox{moy}}(n-1)\\
\end{array}
$$
</div>

On en déduit :

$$
n\cdot C_{\mbox{moy}}(n) = K(2n - 1) + (n+1)\cdot C_{\mbox{moy}}(n-1)
$$

Et maintenant la seconde astuce : on divise l'équation ci-dessus par $n(n+1)$ pour obtenir un terme générique identique des deux côtés de l'équation :

$$
\frac{C_{\mbox{moy}}(n)}{n+1}=\frac{C_{\mbox{moy}}(n-1)}{n} + K\cdot\frac{2n - 1}{n(n+1)}
$$

On peut alors poser $A(n) = \frac{1}{n+1} \cdot C_{\mbox{moy}}(n)$ et on doit maintenant résoudre :

$$
A(n) = A(n-1) + K\cdot\frac{2n - 1}{n(n+1)}
$$

Ce qui donne :

<div>
$$
\begin{array}{lcl}
A(n) &=& A(n-1) + K\cdot\frac{2n - 1}{n(n+1)}\\
&=& A(n-2) + K\cdot\frac{2(n-1) - 1}{(n-1)(n)} +  K\cdot\frac{2n - 1}{n(n+1)}\\
&=& \dots \\
&=&K \sum_{i=1}^{n}\frac{2i-1}{i(i+1)} + A(0)\\
&=&K \sum_{i=1}^{n}\frac{2}{(i+1)} - K \sum_{i=1}^{n}\frac{1}{i(i+1)} + A(0)\\
\end{array}
$$
</div>

On peut facilement montrer (par récurrence) que $\sum_{i=1}^{n}\frac{1}{i(i+1)} = \frac{n}{n+1} \leq 1$ et donc que :

<div>
$$
\begin{array}{lcl}
A(n) &=& 2K\sum_{i=1}^{n}\frac{1}{(i+1)} + \mathcal{O}(1)\\
&=& 2K\sum_{i=1}^{n}\frac{1}{i} - 2K + \mathcal{O}(1)\\
&=& 2K\sum_{i=1}^{n}\frac{1}{i} + \mathcal{O}(1)\\
&=& \mathcal{O}(\sum_{i=1}^{n}\frac{1}{i})\\
\end{array}
$$
</div>

La suite $A(n)$ se comporte comme un $\mathcal{O}(H(n))$ où $H(n) = \sum_{i=1}^{n}\frac{1}{i}$.

Cette fonction est connue, elle s'appelle la [série harmonique](https://fr.wikipedia.org/wiki/S%C3%A9rie_harmonique),
et est [équivalente](https://fr.wikipedia.org/wiki/%C3%89quivalent) à $\ln(n)$ lorsque $n$ tend vers $+\infty$.  On a alors que $\mathcal{O}(H(n)) = \mathcal{O}(\ln(n))$, et de là :

$$
A(n) = \mathcal{O}(\ln(n))
$$

En revenant aux $C_{\mbox{moy}}(n) = n\cdot A(n)$ :

$$
C_{\mbox{moy}}(n) = \mathcal{O}(n\ln(n))
$$

ouf.

La complexité en moyenne du tri rapide pour un tableau de taille $n$ est $\mathcal{O}(n\ln(n))$
{% enddetails %}

## Conclusion

Le tri rapide a :

- une complexité moyenne qui vaut sa complexité minimale et qui est $\mathcal{O}(n \ln(n))$, donc la meilleur possible
- il très rapide pour les tableaux en désordre et très lent pour les tableaux déjà triés.

C'est donc *rigolo* :

{% note "**Fun fact**"  %}
Commencer par mélanger un tableau pour le trier avec `rapide`{.language-} ensuite est plus rapide en moyenne que de le trier directement.
{% endnote %}
