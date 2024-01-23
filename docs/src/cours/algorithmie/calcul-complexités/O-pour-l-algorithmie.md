---
layout: layout/post.njk

title: Les $\mathcal{O}()$ pour le calcul de complexité

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Les comparaisons asymptotiques sont plutôt intéressantes en algorithmie car elles permettent de supprimer les effets négatifs du comptage explicite de la complexité. La comparaisons la plus utilisée, et de loin, est le $\mathcal{O}$. Elle nous permettra de majorer par rapport à la taille $N$ de l'entrée de l'algorithme :

- le nombre d'opérations élémentaires effectuées par l'algorithme avant de s'arrêter
- le temps mis par l'algorithme pour s'exécuter
- la taille de la mémoire utilisée pour par l'algorithme

Si le majorant n'est pas trop éloigné du compte exact, cela nous donne une **idée générale** de la valeur lorsque $N$ devient grand.

{% info %}
C'est le grand informaticien D. Knuth qui a popularisé l'usage de ces fonctions dans le calcul de la complexité avec son célèbre article [BIG OMICRON AND BIG OMEGA AND BIG THETA](https://danluu.com/knuth-big-o.pdf){.fichier}
{% endinfo %}

## Gérer les constantes additives et multiplicatives

Les constantes additives et multiplicatives ne changent pas l'allure de la complexité.

Le plus grand intérêt dans le comptage de complexité algorithmique est que [la règle des constantes](../comparaisons-asymptotiques/#OA-constantes-additives){.interne} montre qu'un nombre constant est toujours en $\mathcal{O}(1)$ (ainsi qu'en $\Omega(1)$ et en $\Theta(1)$). On l'a vu et vous l'avez expérimenté, pour un algorithme, il est souvent compliqué de savoir exactement de combien d'[instructions basiques](../pseudo-code#instruction-basique){.interne} est constituée une opération ou le temps exact qu'elle va prendre. On pourra cependant toujours montrer qu'il y en a un nombre constant ou plus généralement borné :

{% note "**À retenir**" %}
La complexité d'une instruction basique est de $\Theta(1)$ (donc également $\mathcal{O}(1)$) opérations.
{% endnote %}

De là :

{% note  "**Proposition**" %}
Un nombre constant d'instructions basiques nécessite $\Theta(1)$ (donc également $\mathcal{O}(1)$) opérations.
{% endnote %}

Enfin, [la règle des constantes multiplicatives](../comparaisons-asymptotiques/#OA-constantes-multiplicatives){.interne} montre la proposition suivante :

{% note "**Proposition**" %}
L'exécution un nombre constant de fois d'un bloc d'instruction de complexité $f(N)$ nécessite $\Theta(f(N))$ (donc également $\mathcal{O}(f(N))$) opérations.
{% endnote %}
{% note "**Corollaire**" %}
L'exécution un nombre constant de fois d'un bloc d'instruction :

- de complexité $\Theta(f(N))$ nécessite $\Theta(f(N))$ opérations.
- de complexité $\mathcal{O}(f(N))$ nécessite $\mathcal{O}(f(N))$ opérations.
{% endnote %}

Ceci est pratique, car cela permet de ne pas compter toutes les opérations basiques précisément. Ainsi, en reprenant l'exemple de la partie [complexité des pseudo-code](../pseudo-code#complexité){.interne} :

```text#
x = 30
if ((x > 12) AND (x < 36)):
    z = x * "coucou"
```

1. on affecte un objet à x : 1 instruction, donc $\mathcal{O}(1)$ opérations.
2. un test avec 2 comparaisons et un `AND`{.language-} pour deux variables : 6 instructions, donc $\mathcal{O}(6) = \mathcal{O}(1)$ opérations.
3. on affecte le résultat d'une opération élémentaire : 3 instructions, donc $\mathcal{O}(3) = \mathcal{O}(1)$ opérations.

Un nombre total d'instructions de $3 \cdot \mathcal{O}(1) = \mathcal{O}(1)$ opérations.

En revanche, faites attention, cela ne marche que pour les constantes !

{% attention %}
Si le nombre d'opérations élémentaires est variable on a : $n \cdot \mathcal{O}(1) = \mathcal{O}(n)$. **On ne peut pas simplifier les éléments variables**.
{% endattention %}

## Gérer des polynômes

Enfin, comme en algorithmie on manipulera souvent des polynômes, montrez que l'on peut, avec [les différentes règles *fonctions* asymptotiques](../comparaisons-asymptotiques/#règles) que :

{% exercice %}

On a :
$$\sum_{i=0}^na_i x^i = \mathcal{O}(x^n) \mbox{ si } a_n \neq 0$$
{% endexercice %}
{% details "corrigé" %}

1. $\sum_{i=0}^na_i x^i = \mathcal{O}(\sum_{i=0}^na_i x^i)$
2. la règle des constantes multiplicative liée à la règle des polynômes montre que $\mathcal{O}(a_ix^i) = \mathcal{O}(a_jx^j)$ pour tout $i \leq j$.  
3. on peut alors appliquer itérativement la règle des sommes négligeables pour montrer que $\mathcal{O}(\sum_{i=0}^na_i x^i) \Rightarrow \mathcal{O}(\sum_{i=j}^na_i x^i)$ pour tout $j \leq n$
4. pour $j=n$ on a $\mathcal{O}(\sum_{i=0}^na_i x^i) \Rightarrow \mathcal{O}(x^n)$
5. Donc $\sum_{i=0}^na_i x^i = \mathcal{O}(x^n)$
{% enddetails %}

## Voir l'infini

Calculer avec les fonction asymptotiques va nous permettre de donner la complexité sous la forme d'une allure de complexité :

{% note "**À retenir**" %}

On cherchera à borner la complexité par une allure de complexité :

- ***complexité constante*** en $\mathcal{O}(1)$
- ***complexité logarithmique*** en $\mathcal{O}(\log_2(n))$
- ***complexité linéaire*** en $\mathcal{O}(n)$
- ***complexité polynomiale*** en $\mathcal{O}(n^k)$ avec $k>1$ constant le plus petit possible
- ***complexité exponentielle*** en $\mathcal{O}(k^n)$ avec $k>1$ constant le plus petit possible
{% endnote %}

Si nos approximations ne sont pas disproportionnés (genre en disant que $log_2(n) = \mathcal{O}(2^n)$)$, on aura trouvé l'allure de la complexité de notre algorithme sans trop de soucis.

## Usage de $\Omega$ et $\Theta$

### $\Omega$

On utilisera très peut les fonctions $\Omega$ qui ne serviront qu'à montrer le type de croissance de notre algorithme.

> TBD exemple

### $\Theta$

Les fonctions $\Theta$ serviront lorsque l'on cherchera le meilleur algorithme possible pour résoudre un problème.

> TBD exemple
