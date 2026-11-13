---
layout: layout/post.njk

title: Les $\mathcal{O}()$ pour le calcul de complexité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Comme le compte exacte du nombre $C(n)$  d'instructions élémentaires effectuées lors de l'exécution d'un algorithme est souvent difficile à faire et qu'au final souvent seule son [allure générale](../importance/#allure) compte (logarithmique, linéaire, polynomiale ou exponentielle) on utilise un outil nommé [comparaison asymptotique](https://fr.wikipedia.org/wiki/Comparaison_asymptotique){.externe} qui va nous permettre de simplifier le calcul en ne conservant que l'allure de la complexité que l'on cherche à déterminer. Il existe plusieurs comparateur asymptotique, celui qui est le plus utilisé en algorithmie est le $\mathcal{O}$ :

{% definition %}
Une fonction <span>$f(N)$</span> est en $\mathcal{O}(g(n))$ s'il existe 2 constantes $C_0$ et $N_0$ telles que $f(n) \leq C_0 \cdot g(n)$ pour tout $n > N_0$.
{% enddefinition %}

{% info %}
C'est le grand informaticien D. Knuth qui a popularisé l'usage de ces fonctions dans le calcul de la complexité avec son célèbre article [BIG OMICRON AND BIG OMEGA AND BIG THETA](https://danluu.com/knuth-big-o.pdf){.fichier}
{% endinfo %}

Connaître le comportement en $\mathcal{O}$ de $C(n)$ nous donne un **majorant** de son _allure_ lorsque $n$ devient grand. Elle nous permettra de majorer par rapport au paramètre $n$ du calcul de complexité $C(n)$. Par exemple $C(n) = \mathcal{O}(n^2)$ pour une allure de complexité polynomiale de degré 2.



{% note "**Proposition**" %}
On a l'implication suivante :

Si $f(n) = \mathcal{O}(g(n))$ et $g(n) = \mathcal{O}(h(n))$ alors $f(n) = \mathcal{O}(h(n))$

{% endnote %}
{% details  "preuve", "open" %}

> TBD

{% enddetails %}

## Gérer les constantes additives et multiplicatives

Le plus grand intérêt dans le comptage de complexité algorithmique est la propriété suivante :

<span id="OA-constantes-additives-multiplicatives"></span>

{% note "**Proposition**" %}
On a l'équivalence suivante :

<div>
$$
f(n) = \mathcal{O}(\alpha \cdot g(n) + \beta) \Leftrightarrow f(n) = \mathcal{O}(g(n))
$$
</div>

{% endnote %}
{% details  "preuve", "open" %}
Si $f(n) = \mathcal{O}(\alpha \cdot g(n) + \beta)$, il existe $C_0$ et $N_0$ tels que pour tout $n\geq N_0$ on ait $f(n) \leq C_0 \cdot (\alpha \cdot g(n) + \beta) = C_0 \cdot \alpha \cdot g(n) + C_0 \cdot \beta$.

Soit $f(N) = \mathcal{O}(A)$. Il existe donc $c_0$ et $N_0$ tels que pour tout $N > N_0$, on ait $f(N) \leq c_0 \cdot A$.

En posant $c'_0 = c_0 \cdot A$, on a $f(N) \leq c'_0 \cdot 1$ pour tout $N > N_0$. Donc : $f(N) = \mathcal{O}(1)$.

Réciproquement, soit $f(N) = \mathcal{O}(1)$.

Il existe donc $c_0$ et $N_0$ tels que pour tout $N > N_0$, on ait $f(N) \leq c_0 \cdot 1$. En posant $c'_0 = c_0 / A$, on a $f(N) \leq c'_0 \cdot A$ pour tout $N > N_0$. Donc $f(N) = \mathcal{O}(A)$.

{% enddetails %}

> TBD conséquence :O(1) et algo sur l'age.

{% note "**Règle des constantes additives**" %}
$ A = \Theta(1)$, avec $A$ une constante strictement positive.
{% endnote %}
{% details  "preuve", "open" %}

Soit $f(N) = \mathcal{O}(A)$. Il existe donc $c_0$ et $N_0$ tels que pour tout $N > N_0$, on ait $f(N) \leq c_0 \cdot A$.

En posant $c'_0 = c_0 \cdot A$, on a $f(N) \leq c'_0 \cdot 1$ pour tout $N > N_0$. Donc : $f(N) = \mathcal{O}(1)$.

Réciproquement, soit $f(N) = \mathcal{O}(1)$.

Il existe donc $c_0$ et $N_0$ tels que pour tout $N > N_0$, on ait $f(N) \leq c_0 \cdot 1$. En posant $c'_0 = c_0 / A$, on a $f(N) \leq c'_0 \cdot A$ pour tout $N > N_0$. Donc $f(N) = \mathcal{O}(A)$.

{% enddetails %}


## Majorer le nombre d'itération

> TBD +/- constante additive ou multiplicaive
> TBD majorer par quelque chose qu'on peut calculer

## Complexité max

> TBD pour ne pas dépendre des entrées : recherche.

## Autres 



La règle suivante va se révéler fort utile :

<span id="OA-constantes-additives"></span>
{% note "**Règle des constantes additives**" %}
$ A = \Theta(1)$, avec $A$ une constante strictement positive.
{% endnote %}
{% details  "preuve", "open" %}

Soit $f(N) = \mathcal{O}(A)$. Il existe donc $c_0$ et $N_0$ tels que pour tout $N > N_0$, on ait $f(N) \leq c_0 \cdot A$.

En posant $c'_0 = c_0 \cdot A$, on a $f(N) \leq c'_0 \cdot 1$ pour tout $N > N_0$. Donc : $f(N) = \mathcal{O}(1)$.

Réciproquement, soit $f(N) = \mathcal{O}(1)$.

Il existe donc $c_0$ et $N_0$ tels que pour tout $N > N_0$, on ait $f(N) \leq c_0 \cdot 1$. En posant $c'_0 = c_0 / A$, on a $f(N) \leq c'_0 \cdot A$ pour tout $N > N_0$. Donc $f(N) = \mathcal{O}(A)$.

{% enddetails %}

<span id="OA-constantes-multiplicatives"></span>
{% note "**Règle des constantes multiplicatives**" %}
$ A\cdot f(N) = \Theta(f(N))$, avec $A$ une constante strictement positive.
{% endnote %}
{% details  "preuve", "open" %}

Pour tout $N > 0$, on a $A\cdot f(N) \leq c_0\cdot f(N)$ avec $c_0 = A$ ce qui prouve que A\cdot f(N) = \mathcal{O}(f(N))$.

De même, pour tout $N>0$, $A\cdot f(N) \geq c_0\cdot f(N)$ avec $c_0 = A$ ce qui prouve que A\cdot f(N) = \Omega(f(N))$.
{% enddetails %}


> a f + b = f

que [la règle des constantes](../comparaisons-asymptotiques/#OA-constantes-additives) montre qu'un nombre constant est toujours en $\mathcal{O}(1)$ (ainsi qu'en $\Omega(1)$ et en $\Theta(1)$). On l'a vu et vous l'avez expérimenté, pour un algorithme, il est souvent compliqué de savoir exactement de combien d'[instructions basiques](../../pseudo-code/briques-de-base/) est constituée une opération ou le temps exact qu'elle va prendre. On pourra cependant toujours montrer qu'il y en a un nombre constant ou plus généralement borné :

{% retenir %}
La complexité d'une instruction basique est de $\Theta(1)$ (donc également $\mathcal{O}(1)$) opérations.
{% endretenir %}

De là :

{% note  "**Proposition**" %}
Un nombre constant d'instructions basiques nécessite $\Theta(1)$ (donc également $\mathcal{O}(1)$) opérations.
{% endnote %}

Enfin, [la règle des constantes multiplicatives](../comparaisons-asymptotiques/#OA-constantes-multiplicatives) montre la proposition suivante :

{% note "**Proposition**" %}
L'exécution un nombre constant de fois d'un bloc d'instructions de complexité $f(N)$ nécessite $\Theta(f(N))$ (donc également $\mathcal{O}(f(N))$) opérations.
{% endnote %}
{% note "**Corollaire**" %}
L'exécution d'**un nombre constant de fois** d'un bloc d'instructions :

- de complexité $\Theta(f(N))$ nécessite $\Theta(f(N))$ opérations.
- de complexité $\mathcal{O}(f(N))$ nécessite $\mathcal{O}(f(N))$ opérations.
{% endnote %}

Ceci est pratique, car cela permet de ne pas compter toutes les opérations basiques précisément. Ainsi, en reprenant [l'exemple initial de calcul de complexité](../définitions) :

```pseudocode/
ref age int
age ← 16
si ((age ≥ 12) et (age < 18)):
    personne ← "adolescent"
```

- première ligne : 2 instructions donc $\mathcal{O}(1)$ instructions.
- deuxième ligne : 8 instructions donc $\mathcal{O}(1)$ instructions.
- troisième ligne : 2 instructions donc $\mathcal{O}(1)$ instructions.

Un nombre total d'instructions de $3 \cdot \mathcal{O}(1) = \mathcal{O}(1)$ instructions.

En revanche, faites attention, cela ne marche que pour les constantes !

{% attention %}
Si le nombre d'opérations élémentaires est variable on a : $n \cdot \mathcal{O}(1) = \mathcal{O}(n)$. **On ne peut pas simplifier les éléments variables**.
{% endattention %}

{% retenir %}
Les comparaisons asymptotiques servent à comparer l'_allure_ de deux fonctions à l'infini : plus grande, plus petite ou équivalente. En gros on oublie les constantes multiplicatives et additives.
{% endretenir %}

## Gérer des polynômes

Enfin, comme en algorithmie on manipulera souvent des polynômes, montrez que l'on peut, avec [les différentes règles des *fonctions* asymptotiques](../comparaisons-asymptotiques/#règles) que :

{% exercice %}

On a :
$$\sum_{i=0}^na_i x^i = \mathcal{O}(x^n) \mbox{ si } a_n \neq 0$$
{% endexercice %}
{% details "corrigé" %}

1. $\sum_{i=0}^na_i x^i = \mathcal{O}(\sum_{i=0}^na_i x^i)$
2. la règle des constantes multiplicatives liée à la règle des polynômes montre que $\mathcal{O}(a_ix^i) = \mathcal{O}(a_jx^j)$ pour tout $i \leq j$.  
3. on peut alors appliquer itérativement la règle des sommes négligeables pour montrer que $\mathcal{O}(\sum_{i=0}^na_i x^i) \Rightarrow \mathcal{O}(\sum_{i=j}^na_i x^i)$ pour tout $j \leq n$
4. pour $j=n$ on a $\mathcal{O}(\sum_{i=0}^na_i x^i) \Rightarrow \mathcal{O}(a_nx^n) = \mathcal{O}(x^n)$
5. Donc $\sum_{i=0}^na_i x^i = \mathcal{O}(x^n)$
{% enddetails %}

## Voir l'infini

Calculer avec les fonctions asymptotiques va nous permettre de donner la complexité sous la forme d'une allure de complexité :

{% retenir %}

On cherchera à borner la complexité par une allure de complexité :

- ***complexité constante*** en $\mathcal{O}(1)$
- ***complexité logarithmique*** en $\mathcal{O}(\log_2(n)) = \mathcal{O}(\ln(n))$
- ***complexité linéaire*** en $\mathcal{O}(n)$
- ***complexité polynomiale*** en $\mathcal{O}(n^k)$ avec $k>1$ constant le plus petit possible
- ***complexité exponentielle*** en $\mathcal{O}(k^n)$ avec $k>1$ constant le plus petit possible
{% endretenir %}

Si nos approximations ne sont pas disproportionnées (genre en disant que $log_2(n) = \mathcal{O}(2^n)$), on aura trouvé l'allure de la complexité de notre algorithme sans trop de soucis.

## Usage de $\Omega$ et $\Theta$

On utilisera très peu les fonctions $\Omega$ et $\Theta$ dans le calcul de complexité d'un algorithme car le but des calculs de complexité est de majorer une complexité et non de la minorer et utiliser des $\Theta$ est presque aussi contraignant que de faire des calculs de complexité exacts.

En revanche, ces deux *fonctions* asymptotiques trouveront leur utilité lorsque l'on étudiera des complexités de problèmes algorithmiques où il faudra comparer plusieurs algorithmes entre eux.

## <span id="exemple-recherche"></span> Exemple de la recherche d'un élément dans un tableau

Prenons par exemple notre algorithme fétiche :

```pseudocode/
algorithme recherche(T: []int, x: int) → bool:
    pour chaque e de T:
        si e == x:
            rendre Vrai
    rendre Faux
```

Cet algorithme recherche si le paramètre `x`{.language-} est un élément de `T`{.language-}.

Calculons ses complexités maximale et minimale. Commençons par regarder les complexités de chaque ligne :

1. définition de la fonction : $C_1 = \mathcal{O}(1)$
2. une boucle `pour chaque`{.language-} de $k$ itérations
3. un test entre 2 variables : $C_3 = \mathcal{O}(1)$
4. un retour de fonction $C_4 = \mathcal{O}(1)$
5. un retour de fonction : $C_5 = \mathcal{O}(1)$

Comme il y a 2 retours de fonctions (lignes 4 et 5), la complexité sera soit :

- $C = C_1 + k \cdot (C_3) + C_5 = \mathcal{O}(1) + k \cdot (\mathcal{O}(1)) + \mathcal{O}(1)$ si on utilise la sortie de la ligne 5 (on n'est jamais passé par la ligne 4)
- $C' = C_1 + k \cdot (C_3) + C_4 = \mathcal{O}(1) + k \cdot (\mathcal{O}(1) + \mathcal{O}(1))$ si on utilise la sortie de la ligne 4 en passant lors de la dernière itération de la boucle `pour chaque`{.language-} de la ligne 2

Les deux cas se simplifient en : $\mathcal{O}(k)$

En effet, comme $\mathcal{O}(1) + \mathcal{O}(1) = \mathcal{O}(1)$, on a $C = C' = \mathcal{O}(1) + k \cdot (\mathcal{O}(1))$. De là, $C = C' = \mathcal{O}(1) + \mathcal{O}(k) = \mathcal{O}(k)$

On cherche le cas le pire, c'est-à-dire lorsque $k$ est maximum, donc lorsque la boucle `pour chaque`{.language-} parcourt tout le tableau, c'est-à-dire pour deux cas :

- l'élément recherché n'est pas dans le tableau
- l'élément recherché est le dernier élément du tableau

On en conclut que :

{% note %}
La complexité de l'algorithme `recherche`{.language-} est $\mathcal{O}(n)$ où $n$ est la taille du tableau qui est un paramètre d'entrée.
{% endnote %}

La complexité minimale est quant à elle atteinte lorsque l'on ne parcourt pas notre boucle, c'est-à-dire lorsque la valeur recherchée est la 1ère valeur du tableau :

{% note %}
La complexité minimale de l'algorithme `recherche`{.language-} est $\mathcal{O}(1)$.
{% endnote %}
