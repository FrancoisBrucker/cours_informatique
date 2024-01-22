---
layout: layout/post.njk

title: L'outils de mesure du $\mathcal{O}()$

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


## Problème du comptage exhaustif de la complexité

Nous avons calculé explicitement des complexité dans la partie précédente. Vous avez du vous en rendre compte, c'est assez pénible car plusieurs problèmes surviennent.

### Ligne au compte incertain

Certaines ligne n'on pas le même nombre d'instruction selon comment on compte :

- est-ce que `x = a + 1`{.language-} c'est 1, 2 ou 3 instructions ? Ou plus ?
- quel est le nombre d'instructions de la ligne `pour chaque élément x du tableau T`{.language-} ? Une ou deux ?

### Algorithme équivalents aux comptes très différents

De plus, selon l'implémentation, un même algorithme peut avoir plusieurs complexités :

```text
pour i allant de 2 à 9:
  affiche à l'écran i
```

Peut être considéré de complexité $9\cdot 3 = 27$ si l'on considère que :

- la première ligne est uniquement une affectation
- l'affichage nécessite une opération et qu'il faut retrouver la valeur d $i$

En remplaçant la boucle for par une boucle tant que, on obtient :

```text
i = 2
tant que i ≤ 9:
  affiche à l'écran i
  i = i + 1
```

Qui est de complexité : $1 + 9\cdot (2+2+3) = 64$ ce qui semble énorme !

En revanche, si l'on remplace $9$ par $n$ le rapport des deux complexité tend vers une constante : la différence n'est plus si importante que cela lorsque $n$ devient grand.

### Dépend du code/pseudo-code

En écrivant le pseudo-code en code, par exemple en python, il n'est pas garantie du tout que les instructions basiques de mon pseudo-code seront aussi les instructions basiques de l'interpréteur.

L'instruction python `x = 1`{.language} prendra certainement plus d'une instruction élémentaire pur l'interpréteur python (il lui faut d'abort créer l'entier, la variable puis les lier) et cela prendra encore plus d'instructions basique au processeur pour réaliser tout ça.

Ah oui, et ça dépend du processeur : un processeur ARM (comme sur les mac) prendra plus d'instructions qu'un processeur INTEL (sur les PC).

Sans parler du fait que chaque instruction basique pour un processeur peut prendre plusieurs cycles processeur et que ce n'est pas constant, même pour une instruction donnée (à cause des prédictions).

### Beaucoup de calcul pour par grand chose

Enfin, ce calcul exact semble un peu vain puisqu'au final seule la forme générale et asymptotique de la complexité nous intéresse. Em effet, si les entrées sont de petites tailles c'est de toute façon rapide et plus important, [on a vu](../définitions/#forme-asymptotique) que :

{% note %}
Les coefficients multiplicatifs constants sont négligeable par rapport à la forme logarithmique, linéaire, polynomiale ou exponentielle de la complexité.
{% endnote %}

## Notation $\mathcal{O}$

Comme il est impossible de connaître le nombre exact d’instructions et qu'au final on s'en fiche puisque seule la forme générale et asymptotique est importante, on utilise l'outil de la [comparaison asymptotique](https://fr.wikipedia.org/wiki/Comparaison_asymptotique) les *grand O*, $\mathcal{O}()$, qui permettent de trouver des classes d'équivalence de fonctions.

Avant de montrer l'application de cet outil aux mesures de complexités, commençons par voir comment tout ça peut s'utiliser de façon formelle.

{% note %}
Une fonction <span>$f(N)$</span> est en $\mathcal{O}(f'(N))$ s'il existe 2 constantes $c_0$ et $N_0$ tels que $f(N) < c_0 \cdot f'(N)$ pour tout $N > N_0$.
{% endnote %}

Cela permet :

- d'avoir un majorant de notre mesure lorsque $N$ devient grand
- de ne pas s'occuper des constantes puisque (on va le démontrer) une fonction en $\mathcal{O}(\text{constante})$ est également en $\mathcal{O}(1)$
- de ne pas s'occuper de la proportionnalité car (on va le démontrer) une fonction en $\mathcal{O}(\text{constante} \cdot f(N))$ est également en $\mathcal{O}(f(N))$

{% note %}
Connaître le comportement en $\mathcal{O}$ d'une mesure dépendant de $N$ nous donne un majorant de son comportement lorsque $N$ devient grand. Si le majorant n'est pas trop éloigné de la mesure originale, cela nous donne une **idée générale** de la valeur de la mesure lorsque $N$ devient grand.
{% endnote %}

On considérera dans la suite de ce cours uniquement des fonctions **positives**, ce qui est le cas lorsque l'on appliquera à la mesure de complexité. Donc :

{% attention %}
Certaines équivalences ci-dessous ne sont vraies que dans ce cas là.
{% endattention %}

### Arithmétique des $\mathcal{O}$

Par abus de langage, on notera :

- $\mathcal{O}(f(N))$ plutôt que : soit $f'(N)$ une fonction en $\mathcal{O}(f(N))$
- $f(N) = \mathcal{O}(g(N))$ plutôt que : "la fonction $f(N)$ est en $\mathcal{O}(g(N))$"
- $\mathcal{O}(f(N)) \Rightarrow \mathcal{O}(g(N))$ plutôt que : "une fonction en $\mathcal{O}(f(N))$ est également en $\mathcal{O}(g(N))$"
- $\mathcal{O}(f(N)) \Leftrightarrow \mathcal{O}(g(N))$ plutôt que : "une fonction en $\mathcal{O}(f(N))$ est également en $\mathcal{O}(g(N))$ et réciproquement"

On a les règles suivantes (si les fonctions sont positives) :

<span id="OA1"></span>
{% note %}
$\mathcal{O}(A) \Leftrightarrow \mathcal{O}(1)$, avec $A$ une constante strictement positive
{% endnote %}
{% details  "preuve" %}

Soit $f(N) = \mathcal{O}(A)$. Il existe donc $c_0$ et $N_0$ tels que pour tout $N > N_0$, on ait $f(N) < c_0 \cdot A$.

En posant $c'_0 = c_0 \cdot A$, on a $f(N) < c'_0 \cdot 1$ pour tout $N > N_0$. Donc : $f(N) = \mathcal{O}(1)$.

Réciproquement, soit $f(N) = \mathcal{O}(1)$.

Il existe donc $c_0$ et $N_0$ tels que pour tout $N > N_0$, on ait $f(N) < c_0 \cdot 1$. En posant $c'_0 = c_0 / A$, on a $f(N) < c'_0 \cdot A$ pour tout $N > N_0$. Donc $f(N) = \mathcal{O}(A)$.

{% enddetails %}

{% note %}
$\mathcal{O}(N^p) \Rightarrow \mathcal{O}(N^q)$ pour $q \geq p$
{% endnote %}
{% details "preuve" %}

Soit $f(N) = \mathcal{O}(N^p)$. Il existe donc $c_0$ et $N_0$ tels que $f(N) < c_0 \cdot N^p$ pour $N > N_0$.

Comme $1 < 2 \cdot N^\alpha$ pour $\alpha \geq 0$ et $N> 1$, on a $N^p < N^p \cdot (2 \cdot N^{q-p}) = c_0 \cdot N^q$ pour $c_0 = 2$, $N > 1 = N_0$  et $p \leq q$. Donc $N^p = \mathcal{O}(N^q)$ pour tout $p \leq q$

{% enddetails %}

{% note %}
$f(N) = \mathcal{O}(g(N))$ implique $\mathcal{O}(f(N) + g(N) + h(N)) \Rightarrow \mathcal{O}(g(N) + h(N))$ pour f, g et h des fonctions positives.
{% endnote %}
{% details  "preuve" %}

Soit $f(N) = \mathcal{O}(g(N))$. Il existe donc $c_0$ et $N_0$ tels que $f(N) < c_0 \cdot g(N)$ pour $N > N_0$.

Si $f'(N) = \mathcal{O}(f(N) + g(N) + h(N))$ il existe $c'_0$ et $N'_0$ tels que $f'(N) < c'_0(f(N) + g(N) + h(N))$ pour $N > N'_0$.

De là, $f'(N) < c'_0 c_0 g(N) + c'_0 g(N) + c'_0 h(N)$ pour $N > \max( N_0, N'_0 )$ ce qui implique $f'(N) < c'_0 \cdot (c_0 + 1) g(N) + c'_0h(N) < c'_0 \cdot (c_0 + 1) (g(N) + h(N))$ pour $N > \max(N_0, N'_0)$

On a bien : $f'(N) = \mathcal{O}(g(N) + h(N))$

{% enddetails %}

{% note %}
$f(N) = \mathcal{O}(g(N))$ implique $\mathcal{O}(f(N) \cdot g(N) \cdot h(N) + h'(N)) \Rightarrow \mathcal{O}((g(N))^2 \cdot h(N)+ h'(N))$ pour f, g, h et h' des fonctions positives.

{% endnote %}
{% details  "preuve" %}

Soit $f(N) = \mathcal{O}(g(N))$. Il existe donc $c_0$ et $N_0$ tels que $f(N) < c_0 \cdot g(N)$ pour $N > N_0$. Les fonctions étant positives, on pet considérer sans perte de généralité que $c_0 > 1$

Si $f'(N) = \mathcal{O}(f(N)\cdot g(N) \cdot h(N) + h'(N))$ il existe $c'_0$ et $N'_0$ tels que $f'(N) < c'_0(f(N) \cdot g(N) \cdot h(N) + h'(N))$ pour $N > N_0$.

De là, $f'(N) < c'_0 (c_0 g(N) \cdot g(N) \cdot h(N) + h'(N)$ pour $N > \max(N_0, N'_0)$ ce qui implique $f'(N) < c'_0c_0 g^2(N) \cdot h(N) + c'_0 h'(N) < c'_0c_0 g^2(N) \cdot h(N) + c'_0 c_0h'(N) < c'_0c_0 \cdot (g(N)^2 \cdot h(N) + h'(N))$ pour $N > \max( N_0, N'_0)$.

On a bien : $f'(N) = \mathcal{O}((g(N))^2 \cdot h(N) + h'(N))$

{% enddetails %}

{% note %}
En combinant les $\mathcal{O}$ pour $f$ et $g$, deux fonctions positives :

$\mathcal{O}(f(N)) + \mathcal{O}(g(N)) \Rightarrow \mathcal{O}(f(N) + g(N))$

{% endnote %}
{% details  "preuve" %}

Soient $f'(N) = \mathcal{O}(f(N))$ et $g' = \mathcal{O}(g(N))$, il existe donc $c_0$, $c'_0$, $N_0$ et $N'_0$ tels que $f'(N) < c_0 f(N)$ pour $N > N_0$ et $g'(N) < c'_0 g(N)$ pour $N > N'_0$.

On a alors $f'(N) + g'(N) < c_0 f(N) +  c'_0 g(N) < \max(c_0, c'_0) \cdot (f(N) + g(N))$ pour $N > \max( N_0, N'_0)$.

On a bien : $f'(N) + g'(N) = \mathcal{O}(f(N) + g(N))$.

{% enddetails %}
{% note %}
En combinant les $\mathcal{O}$ pour $f$ et $g$ deux fonctions positives :

$\mathcal{O}(f(N)) \cdot \mathcal{O}(g(N)) \Rightarrow \mathcal{O}(f(N) \cdot g(N))$

{% endnote %}
{% details  "preuve" %}

Soient $f'(N) = \mathcal{O}(f(N))$ et $g' = \mathcal{O}(g(N))$, il existe donc $c_0$, $c'_0$, $N_0$ et $N'_0$ tels que $f'(N) < c_0 f(N)$ pour $N > N_0$ et $g'(N) < c'_0 g(N)$ pour $N > N'_0$.

On a alors $f'(N) \cdot g'(N) <  c_0f(N) \cdot c'_0g(N) = c_0c'_0 \cdot (f(N)g(N)) $ pour $N > \max(N_0, N'_0)$.

{% enddetails %}

### Conséquences algorithmiques

Ceci est plutôt intéressant en algorithmie car l'on ne connaît pas toujours exactement le nombre d'opérations élémentaires utilisées, mais on peut les majorer de façon assez précise. On utilisera ainsi les $\mathcal{O}$ pour mesurer par rapport à la taille $N$ de l'entrée de l'algorithme :

* le nombre d'opérations élémentaires effectuées par l'algorithme avant de s'arrêter
* le temps mis par l'algorithme pour s'exécuter
* la taille de la mémoire utilisée pour par l'algorithme


La [première règle](./#OA1){.interne} montre qu'un nombre constant est toujours en $\mathcal{O}(1)$. Pour un algorithme, il est souvent compliqué de savoir exactement de combien d'[opérations basiques](../pseudo-code#instruction-basique){.interne} est constituée une opération ou le temps exact qu'elle va prendre (pour un ordinateur, cela dépend du type de processeur. Par exemple, l'addition avec un x68 est faite [avec des registres](https://ensiwiki.ensimag.fr/index.php?title=Constructions_de_base_en_assembleur_x86), elle nécessite ainsi 2 opérations du processeur). On pourra cependant toujours montrer qu'il y en a un nombre constant (ou borné) :

{% note %}
La complexité d'une opération basique nécessite $\mathcal{O}(1)$ opérations.
{% endnote %}

De là :

{% note %}
Un nombre constant d'opérations basiques nécessite $\mathcal{O}(1)$ opérations.
{% endnote %}

Les règles précédentes permettent plus généralement de montrer :

{% note %}
$\mathcal{O}(A \cdot f(N)) \Leftrightarrow A \cdot \mathcal{O}(f(N)) \Leftrightarrow \mathcal{O}(f(N))$, avec $A$ une constante strictement positive et $f(N)$ une fonction strictement positive pour $N > N_0$
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

Enfin, comme en algorithmie on manipulera souvent des polynômes, on peut montrer facilement avec les règles précédentes que :

{% note %}
$$\sum_{i=0}^na_i x^i = \mathcal{O}(x^n) \mbox{ si } a_n \neq 0$$
{% endnote %}



> TBD : O et borne la plus fine possible

## Si on veut être plus précis

Omega et theta car un algo linéaire est en O exponentiel. Cela ne donne qu'une borne max.

> TBD outil pour la mesurer : $\mathcal{O}$ (parler de $\Omega$) et ajouter $\Theta$. Limite lorsque entree grossi. Si petit on s'en fiche ca va vite.


## TBD 

> TBD outil pour la mesurer : $\mathcal{O}$ (parler de $\Omega$) et ajouter $\Theta$. Limite lorsque entree grossi. Si petit on s'en fiche ca va vite.
>
> C'est un peut chiant de faire comme ça et c'est pas très utile de faire tous ces détails :
> 
> 1. pas se faire suer avec tous les détails. Par exemple, comment fonctionne la boucle for ? Juste une affectation on bien c'est une somme si on l'écrit avec un tant que ?
> 2. ce qui nous intéresse c'est les grosses valeurs, lorsque c'est petit ça va vite et on s'en fiche.
> 3. la tendance de la complexité est cruciale : faire schéma des complexités.
> solution = $\mathcal{O}$, oméga et théta.
>
> enfin 
De plus 
> allure similaire, même si on va plus vite/plus lentement.