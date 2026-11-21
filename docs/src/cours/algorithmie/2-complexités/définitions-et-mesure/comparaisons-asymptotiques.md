---
layout: layout/post.njk

title: Comparaisons asymptotiques

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

{% lien %}
[comparaisons asymptotiques](https://fr.wikipedia.org/wiki/Comparaison_asymptotique).
{% endlien %}

Les comparaisons asymptotiques servent à comparer l'_allure_ de deux fonctions à l'infini : plus grande, plus petite ou équivalente. En gros on oublie les constantes multiplicatives et additives qui dépendent du langage de programmation ou sont sujettes à interprétation.

{% info %}
C'est le grand informaticien D. Knuth qui a popularisé l'usage de ces fonctions dans le calcul de la complexité avec son célèbre article [BIG OMICRON AND BIG OMEGA AND BIG THETA](https://danluu.com/knuth-big-o.pdf){.fichier}
{% endinfo %}

Comme on utilise les fonctions asymptotique dans le cadre de la complexité on se restreindra aux fonctions issues de la complexité. En particulier :

{% attention %}
On considérera dans la suite de ce cours uniquement des fonctions plus grande que 1 à partir d'un certain rang.
{% endattention %}

On utilise en algorithmie 3 _fonctions_ asymptotiques différentes , la plus utilisée étant la fonction $\mathcal{O}()$ :

{% definition %}
- Une fonction <span>$f(n)$</span> est en $\mathcal{O}(g(n))$ s'il existe 2 constantes $C_0$ et $N_0$ telles que $f(n) \leq C_0 \cdot g(n)$ pour tout $n > N_0$,
- une fonction <span>$f(n)$</span> est en $\Omega(g(N))$ s'il existe 2 constantes $C_0$ et $N_0$ telles que $f(n) \geq C_0 \cdot g(n)$ pour tout $n > N_0$,
- une fonction <span>$f(n)$</span> est en $\Theta(g(N))$ si $f(n)$ est en $\mathcal{O}(g(N))$ et $f(n)$ est en $\Omega(g(N))$.
{% enddefinition %}

{% definition "**Abus de notation**" %}
Par abus de langage on associera $\mathcal{O}(f(N))$ à une fonction en $\mathcal{O}(f(N))$ ce qui nous permettra d'écrire $f(N) = \mathcal{O}(g(N))$ plutôt que : "la fonction $f(N)$ est en $\mathcal{O}(g(N))$"
{% enddefinition %}

Ces trois fonctions partagent nombre de propriétés, ce qui les rend facile à manipuler. Par exemple la transitivité :

{% note "**Proposition**" %}
- Si $f(n) = \mathcal{O}(g(n))$ et $g(n) = \mathcal{O}(h(n))$ alors $f(n) = \mathcal{O}(h(n))$,
- si $f(n) = \Omega(g(n))$ et $g(n) = \Omega(h(n))$ alors $f(n) = \Omega(h(n))$,
- si $f(n) = \Theta(g(n))$ et $g(n) = \Theta(h(n))$ alors $f(n) = \Theta(h(n))$.

{% endnote %}
{% details  "preuve", "open" %}

On ne va faire la preuve que pour les $\mathcal{O}$, la preuve étant identique pour les $\Omega$.

- Si $f(n)$ est en $\mathcal{O}(g(n))$ il existe $C_0$ et $N_0$ tels que pour tout $n\geq N_0$ on ait $f(n) \leq C_0 g(n)$
- Si $g(n)$ est en $\mathcal{O}(h(n))$ il existe $C'_0$ et $N'_0$ tels que pour tout $n\geq N'_0$ on ait $g(n) \leq C'_0 h(n)$

Donc pour tout $n \geq \max(N_0, N'_0)$ on a $f(n) \leq C_0 \cot C'_0 h(n)$ : $f(N)$ est en $\mathcal{O}(h(n))$

{% enddetails %}

Deux exercices pour voir si on a compris comment ces fonctions se manipulent :

{% exercice %}
Montrez que :

- si $f(n) = \mathcal{O}(g(n))$ alors une fonction en $\mathcal{O}(f(n) + g(n) + h(n))$ est également en $\mathcal{O}(g(n) + h(n))$,
- si $g(n) = \Omega(f(n))$ alors une fonction en $\mathcal{O}(f(n) + g(n) + h(n))$ est également en $\mathcal{O}(g(n) + h(n))$,
{% endexercice %}
{% details  "corrigé" %}

Si $f(n) = \mathcal{O}(g(n))$ il existe $C_0$ et $N_0$ tels que $f(n) \leq C_0 \cdot g(n)$ pour $n > N_0$ et si $f'(n) = \mathcal{O}(f(n) + g(n) + h(n))$ il existe $C'_0$ et $N'_0$ tels que $f'(n) \leq C'_0(f(n) + g(n) + h(n))$ pour $N > N'_0$.

De là, $f'(n) \leq C'_0 \cdot C_0 g(n) + C'_0 g(n) + C'_0 h(n)$ pour $n > \max( N_0, N'_0)$ ce qui implique $f'(n) \leq C'_0 \cdot (V_0 + 1) g(n) + C'_0h(n) \leq C'_0 \cdot (C_0 + 1) (g(n) + h(n))$ pour $n > \max(N_0, N'_0)$ : $f'(n) = \mathcal{O}(g(n) + h(n))$

La seconde implication se résout de façon similaire.
{% enddetails %}

{% exercice %}
Montrez que si $f(n) = \mathcal{O}(g(n))$ alors une fonction en $\mathcal{O}(f(n) \cdot g(n) \cdot h(n) + h'(n))$ est également en $\mathcal{O}((g(N))^2 \cdot h(N)+ h'(N))$.

{% endexercice %}
{% details  "corrigé" %}

Soit $f(n) = \mathcal{O}(g(n))$. Il existe donc $C_0$ et $N_0$ tels que $f(n) \leq C_0 \cdot g(n)$ pour $n > N_0$. Les fonctions étant positives à partir d'un certain rang, on peut considérer sans perte de généralité que $C_0 > 1$

Si $f'(n) = \mathcal{O}(f(n)\cdot g(n) \cdot h(n) + h'(n))$ il existe $C'_0$ et $N'_0$ tels que $f'(n) \leq C'_0(f(n) \cdot g(n) \cdot h(n) + h'(n))$ pour $n > N_0$.

De là, $f'(n) \leq C'_0 (C_0 g(n) \cdot g(n) \cdot h(n) + h'(n))$ pour $n > \max(N_0, N'_0)$ ce qui implique $f'(n) \leq C'_0C_0 g^2(n) \cdot h(n) + C'_0 h'(n) \leq C'_0C_0 g^2(n) \cdot h(n) + C'_0\cdot C_0\cdot h'(n) \leq C'_0C_0 \cdot (g(n)^2 \cdot h(n) + h'(n))$ pour $n > \max( N_0, N'_0)$.

On a bien : $f'(n) = \mathcal{O}((g(n))^2 \cdot h(n) + h'(n))$

{% enddetails %}

Les trois fonctions vont avoir des utilités différentes lors du calcul de complexité.

## Les $\mathcal{O}()$ pour majorer

Le but du calcul de complexité est d'être le plus proche possible du compte exact sans que ce soit pénible. 
Il existe plusieurs comparateur asymptotique, celui qui est le plus utilisé en algorithmie est le $\mathcal{O}$ :

### Nombres constants d'opérations

{% note "**Proposition**" %}
Pour tous réels strictement positifs $\alpha$ et $\beta$ : 

<div>
$$
\begin{cases}
\alpha = \mathcal{O}(1)\\
\alpha \cdot \mathcal{O}(\beta) = \mathcal{O}(1)\\
\end{cases}
$$
</div>

{% endnote %}
{% details  "preuve", "open" %}

- Comme $\alpha = \alpha\cdot 1$ on a $\alpha = \mathcal{O}(1)$.
- Si $f(n) = \mathcal{O}(\beta)$ il existe $C_0$ et $N_0$ tels que pour tout $n > N_0$ on ait $\alpha \cdot f(n) \leq \alpha \cdot C_0 \cdot \beta$, donc  $f(n) \leq (\alpha \cdot C_0 \cdot \beta) \cdot 1$ : $\alpha \cdot f(n) = \mathcal{O}(1)$.

{% enddetails %}

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

### Nombre linéaire d'opérations

Le plus grand intérêt de l'utilisation de la fonction asymptotique $\mathcal{O}$ est que l'on peut facilement négliger les constantes additives et multiplicatives pour se concentrer sur l'allure générale.

<span id="OA-constantes-additives-multiplicatives"></span>

{% note "**Proposition**" %}
Pour tous réels strictement positifs $\alpha$ et $\beta$ :

<div>
$$
\mathcal{O}(\alpha \cdot g(n) + \beta) = \mathcal{O}(g(n))
$$
</div>

{% endnote %}
{% details  "preuve", "open" %}
Par hypothèse il existe $N_1$ tel que $g(n) \geq 1$ pour $n \geq N_1$.

- Si $f(n) = \mathcal{O}(\alpha \cdot g(n) + \beta)$ il existe $C_0$ et $N_0$ tels que pour tout $n\geq N_0$ on ait $f(n) \leq C_0 \cdot (\alpha \cdot g(n) + \beta) = C_0 \cdot \alpha \cdot g(n) + C_0 \cdot \beta$, donc $f(n) \leq (C_0 \cdot \alpha  + C_0 \cdot \beta) \cdot g(n)$ pour $n \geq \max(N_0, N_1)$ : $f(n) = \mathcal{O}(g(n))$.
- Réciproquement, si $f(n) = \mathcal{O}(g(n))$ il existe $C_0$ et $N_0$ tels que pour tout $n\geq N_0$ on ait $f(n) \leq C_0\cdot g(n)$,  donc $f(n) \leq \max(1, \frac{1}{\min(\alpha, \beta)}) \cdot C_0 (\alpha g(n) + \beta)$ pour $n \geq \max(N_0, N_1)$ : $f(n) = \mathcal{O}(\alpha \cdot g(n) + \beta)$.

{% enddetails %}
{% note "**Proposition**" %}
Pour tous réels strictement positifs $\alpha$ et $\beta$ :


- $\alpha \cdot \mathcal{O}(f(n)) + \beta \cdot \mathcal{O}(g(n)) = \mathcal{O}(f(n) + g(n))$
- $\mathcal{O}(f(n)) \cdot \mathcal{O}(g(n)) = \mathcal{O}(f(n) \cdot g(n))$


{% endnote %}
{% details  "preuve", "open" %}


Si $f'(n) = \mathcal{O}(f(n))$ et $g'(n) = \mathcal{O}(g(n))$, il est clair que $\alpha \cdot f'(n) = \mathcal{O}(\alpha \cdot f(n))$ et $\beta \cdot g'(n) = \mathcal{O}(\beta \cdot g(n))$ donc $\alpha \cdot f'(n) = \mathcal{O}(f(n))$ et $\beta \cdot g'(n) = \mathcal{O}(g(n))$ en utilisant la proposition précédente.

Si $1 \leq \alpha \cdot f'(n) \leq C_0 \cdot f(n)$ pour $n \geq N_0$ et $1\leq \beta \cdot g'(n) \leq C'_0 \cdot g(n)$ pour $n \geq N'_0$ on a :
- $\alpha \cdot f'(n) + \beta \cdot g'(n) \leq \max(C_0, C'_0) \cdot (f(n) + g(n))$ pour $n \geq \max(N_0, N'_0)$ 
- $f'(n) \cdot g'(n) \leq C_0 \cdot C'_0 \cdot (f(n) \cdot g(n))$ pour $n \geq \max(N_0, N'_0)$ 

{% enddetails %}

La proposition précédente permet de résoudre les problèmes de comptages. Les pseudo-code suivant ayant même complexité, $\mathcal{O}(n)$ :


```pseudocode/
pour chaque i de [2 .. n]:
    affiche i
```

- ligne 1 : une affectation ($\mathcal{O}(1)$) et $n-1$ itérations ($\mathcal{O}(n)$) :
- ligne 2 : une instruction élémentaire ($\mathcal{O}(1)$) d'une variable qu'il faut aller récupérer $\mathcal{O}(1)$ de total $\mathcal{O}(1) + \mathcal{O}(1) = \mathcal{O}(1 + 1) = \mathcal{O}(2) = \mathcal{O}(1)$
- total : $\mathcal{O}(n) \cdot (\mathcal{O}(1) + \mathcal{O}(1)) = \mathcal{O}(n) \cdot (\mathcal{O}(1)) =  \mathcal{O}(n)$

et 

```pseudocode
ref i ← 2
tant que i ≤ n:
  affiche i
  i ← i + 1
```

- ligne 1 : une création et une affectation de variable ($\mathcal{O}(1)$)
- ligne 2 : un test de 2 variables ($\mathcal{O}(1)$)
- ligne 3 : une instruction élémentaire ($\mathcal{O}(1)$) d'une variable qu'il faut aller récupérer $\mathcal{O}(1)$ de total $\mathcal{O}(1)$
- ligne 4 : une opération et une affectation ($\mathcal{O}(1)$)
- total : le test de la ligne 2 ainsi que les instructions des lignes 3 et 4 sont répétées $n-1$ fois (donc $\mathcal{O}(n)$ fois), pour un total de $\mathcal{O}(n)$ opérations.

Tout devient plus simple !

{% retenir %}

- si le nombre d'itération est $n$ plus ou moins une constante, il est en $\mathcal{O}(n)$,
- si la condition de répétition d'une boucle tant que est en $\mathcal{O}(1)$, seul, le no,bre d'itération va compter dans le calcul de la complexité.
{% endretenir %}

On ne peut cependant appliquer la règle que pour des constantes ! Si $f(n) = \mathcal{O}(g(n))$ on a $n \cdot f(n) = \mathcal{O}(n\cdot g(n))$ puisque $n$ est une fonction en $\mathcal{O}(n)$ pas du tout en $\mathcal{O}(1)$.

{% attention %}
**On ne peut pas simplifier les éléments variables**

Si le nombre d'opérations élémentaires est variable on a : $n \cdot \mathcal{O}(1) = \mathcal{O}(n)$.
{% endattention %}

### <span id="complexité-max"></span>Calcul de complexité max

Enfin, pour le calcul de complexité maximale le $\mathcal{O}$ se trouver être très adapté. Prenons par exemple [notre algorithme recherche](../../../1-algorithme/bases-théoriques/définition/#algorithme-recherche) :

```pseudocode/
algorithme recherche(T: []int, x: int) → bool:
    pour chaque e de T:
        si e == x:
            rendre Vrai
    rendre Faux
```

Toutes les instructions de l'algorithme sont en $\mathcal{O}(1)$ :

- ligne 1 : affectation des différentes variables paramètre pour l'exécution de l'algorithme,
- ligne 2 : affectation de la variable `pour chaque`{.language-},
- ligne 3 : un test
- ligne 4 : un retour
- ligne 5 : un retour

Sa complexité $C(T, x)$ d'une exécution vaut alors :

<div>
$$
\begin{array}{lclr}
C(T, x) 
&=& \mathcal{O}(1) + & \text{ligne 1}\\
&& k \cdot ( & \text{nombre d'exécution de boucle}\\
&& \mathcal{O}(1) + & \text{affectation de la ligne 2}\\
&& \mathcal{O}(1)) + & \text{test de la ligne 3}\\
&& \mathcal{O}(1) + & \text{retour de la ligne 3 ou 4}\\
\end{array}
$$
</div>

Pour ce calcul on a compté :

- l'affectation des paramètre au début de l'exécution (qui est toujours en $\mathcal{O}(1)$, on ne le comptera plus dans la suite de ce cours),
- le retour de la ligne 3 est sortie de la boucle puisque s'il est exécuté c'est la dernière instruction de l'algorithme.

La complexité totale de l'algorithme est donc égale au nombre $k$ de fois où ou la boucle tant que est exécutée. Comme elle est exécutée au maximum $n$ fois où $n$ est la longueur du tableau on en conclut que :

- on peut prendre la longueur $n$ du tableau comme paramètre de la complexité,
- $C(n) = \mathcal{O}(n)$.

## Les $\Omega()$ pour minorer

De façon symétrique, les _grand Omega_, $\Omega()$, permettent de caractériser les fonctions qui en minorent une autre. Elle est le symétrique de la fonction $\mathcal{O}$ :

<span id="omega-GO"></span>
{% note "**Proposition**" %}
$f(N) = \mathcal{O}(g(N)) \Leftrightarrow g(N) = \Omega(f(N))$
{% endnote %}
{% details  "preuve", "open" %}
Si $f(N) = \mathcal{O}(g(N))$, il existe $c_0$ et $N_0$ tels que $f(N) \leq c_0 \cdot g(N)$ pour $N > N_0$. Les fonctions étant positives, on a $c_0 > 0$ et donc $\frac{1}{c_0} \cdot f(N) \leq  g(N)$ pour $N > N_0$ : $g(N) = \Omega(f(N))$

Réciproquement, si $g(N) = \Omega(f(N))$, il existe $c_0$ et $N_0$ tels que $c_0 \cdot f(N) \leq g(N)$ pour $N > N_0$. Les fonctions étant positives, on a $c_0 > 0$ et donc $\frac{1}{c_0} \cdot g(N) \geq  f(N)$ pour $N > N_0$ : $f(N) = \mathcal{O}(g(N))$

{% enddetails %}

Les propositions précédentes démontrées pour les $\mathcal{O}$ fonctionnent également pour les $\Omega$ (on change le signe de l'inégalité dans la démonstration).

### linéarité de la comparaison

{% note "**Proposition**" %}
Pour tous réels strictement positifs $\alpha$ et $\beta$ : 

<div>
$$
\begin{cases}
\alpha = \Omega(1)\\
\alpha \cdot \Omega(\beta) = \Omega(1)\\
\Omega(\alpha \cdot g(n) + \beta) = \Omega(g(n))\\
\alpha \cdot \Omega(f(n)) + \beta \cdot \Omega(g(n)) = \Omega(f(n) + g(n))\\
\Omega(f(n)) \cdot \Omega(g(n)) = \Omega(f(n) \cdot g(n))
\end{cases}
$$
</div>

{% endnote %}

### <span id="complexité-min"></span>Calcul de complexité min

Les $\Omega$ sont utilisés pour minorer des complexité et donc très utiles pour des calculs de complexité min. En reprenant l'algorithme recherche, l'algorithme va forcément rentrer au moins une fois dans la boucle `tant que`{.language-}, on en conclut donc que :

<div>
$$
C(n) = \Omega(1)
$$
</div>

Cela ne veut pas (encore) dire qu'il existe des tableaux et des entiers pour lesquels l'exécution de l'algorithme ne va pas dépendre de la longueur du tableau, juste qu'il prendra au moins un temps constant quelque soient les entrées (ce qui n'es pas très informatif pour cet algorithme, je vous l'accorde).

## Les $\Theta()$ pour les équivalences

Enfin, la dernière comparaison asymptotique utilisée en algorithme est _le grand theta_. Elle rend compte de fonctions aux allures similaires :

{% note "**Proposition**" %}
$f(n) = \Theta(g(n)) \Rightarrow g(n) = \Theta(f(n))$
{% endnote %}
{% details  "preuve", "open" %}
si $f(n)$ est en $\Theta(g(n))$, alors :

- $f(n) = \Theta(g(n))$ donc $g(n)$ est en $\Omega(f(n))$
- $f(n) = \mathcal{O}(g(n))$ donc $g(n)$ est en $\mathcal{O}(f(n))$

{% enddetails  %}

Elle respecte bien sûr également les propriétés communes aux $\mathcal{O}$ et $\Omega$ :

{% note "**Proposition**" %}
Pour tous réels strictement positifs $\alpha$ et $\beta$ : 

<div>
$$
\begin{cases}
\alpha = \Theta(1)\\
\alpha \cdot \Theta(\beta) = \Theta(1)\\
\Theta(\alpha \cdot g(n) + \beta) = \Theta(g(n))\\
\alpha \cdot \Theta(f(n)) + \beta \cdot \Theta(g(n)) = \Theta(f(n) + g(n))\\
\Theta(f(n)) \cdot \Theta(g(n)) = \Theta(f(n) \cdot g(n))
\end{cases}
$$
</div>

{% endnote %}

Enfin, la proposition suivante (triviale) lies les 3 fonctions :

{% note "**Proposition**" %}

<div>
$$
\begin{cases}
f(n) = \Theta(g(n)) \Leftrightarrow f(n) = \Omega(g(n)) \text{ et } g(n) = \Omega(f(n))\\
f(n) = \Theta(g(n)) \Leftrightarrow f(n) = \mathcal{O}(g(n)) \text{ et } g(n) = \mathcal{O}(f(n))\\
\end{cases}
$$
</div>

{% endnote %}

Les $\Theta$ sont utilisés pour calculer la meilleure estimation possible (à un facteur multiplicatif et additif prêt) d'une complexité.

Ainsi, pour l'algorithme recherche, on sait que si $n$ est la longueur du tableau en entrée :

- sa complexité maximale est en $\mathcal{O}(n)$. Comme cette complexité est atteinte pour des tableaux ne contenant pas la valeur recherchée (la complexité est en $\Omega(n)$ pour eux) on en conclut que la complexité max vaut $C_{\max}(n) = \Theta(n)$
- sa complexité minimale est en $\Omega(n)$. Comme cette complexité est atteinte pour des tableaux ne contenant la valeur recherchée en première position (la complexité est en $\mathcal{O}(1)$ pour eux) on en conclut que la complexité max vaut $C_{\min}(n) = \Theta(1)$.

Ceci est important car on pourrait très bien dire que la complexité de l'algorithme recherche est en $\mathcal{O}(n^2)$, voir en $\mathcal{O}(n!)$ qui est tout aussi exact. 

{% retenir %}
Lorsque c'est possible, essayez de trouver des complexités maximale et minimales en $\Theta$ pour vos algorithmes. 

Pour cela on commence par trouver un encadrement en $\mathcal{O}$ et en $\Omega$ puis on trouve des instance de l'algorithme pour lesquels ces bornes sont atteintes.

{% endretenir %}