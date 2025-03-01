---
layout: layout/post.njk
title: "Hiérarchie des complexité"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


> TBD refaire propre avec les MTU.

On va montrer dans cette partie qu'il existe des langages de toute complexité et donc que les problèmes algorithmiques ne sont pas tous polynomiaux, loin de là.

La preuve est belle et simple mais atypique.

## Pseudo-code et entier

On suppose sans perte de généralité que nos programmes sont écrits en pseudo-code. Ils sont encodés sous forme binaire en utilisant le format [Unicode](Unicode) : chaque caractère est écrit sur 32 bits (c'est le format UTF-32). Toute entrée $E$ suite finie de 0 et de 1 peut alors :

1. parfois être vu comme une suite de caractères (si sa longueur est un multiple de 32)
2. moins souvent, mais c'est possible, la suite de caractères forme un texte en français, terminé par un ou plusieurs caractères retour à la ligne (le retour à la ligne est un caractère Unicode correspondant à l'entier binaire `00000000000000000000000000001010` (10 en décimal sur 32 bits)).
3. encore moins souvent ce texte, privé des derniers retours à la ligne est un programme écrit en pseudo-code.
4. et, cerise sur le gâteau parfois ce pseudo-code ne prend qu'un paramètre.

Soit alors $d(E)$ un décideur tel que si $e$ satisfait la condition 4, alors $d(e)$ vaut 1, sinon il vaut 0. Savoir si un texte est un pseudo-code est facile. On regarde juste si [chaque instruction est autorisée](../../écrire-algorithmes/pseudo-code){.interne} et ceci est possible avec un [analyseur lexical](https://fr.wikipedia.org/wiki/Analyse_lexicale) de complexité quadratique dans la taille de la données, c'est à dire ici $\vert e \vert^2$. Si vous voulez vous fixer les idées, vous pouvez supposer sans perte de généralité que le pseudo-code est en fait écrit en python et que l'on vérifie qu'il est syntaxiquement correct (le programme pourra toujours planter, mais chaque ligne est une instruction valide).

Le décideur $d(e)$ est ainsi décidable avec une complexité $\mathcal{O}(\vert e \vert^2)$.

Enfin, si l'entrée $e$ correspond à un pseudo-code terminé par un ou plusieurs retour à la ligne, on appelle $\[e\]$ celui-ci. L'intérêt de supprimer les derniers retour à la ligne c'est que le même programme va apparaître une infinité de fois puisque $\[e\]$ sera égal à $\[e'\]$ avec $e'$ valeur $e$ concaténé à `00000000000000000000000000001010` .

{% attention "**À retenir**"%}
On peut associer à tout entrée $e$ un texte qui peut parfois être du pseudo-code correspondant à un programme à un paramètre $\[e\]$.
{% endattention %}

## Exécution de pseudo-code

Considérons le programme suivant, qui prend en paramètre un pseudo-code :

```text
Nom : Exécution (on le notera E(e, K))
Entrées :
    - un mot e correspondant à un pseudo-code [e] à un paramètre
    - un entier K
Programme :
    on exécute de programme [e](e) instruction après instruction :
        soit I la prochaine instruction de [e](e)

        si l'exécution de I stoppe [e](e) :
            si le retour de [e](e) est 0 :
                Rendre 1
            sinon :
                Rendre 0

        exécution de I

        K = K - 1
        si K ≤ 0 :
            Rendre 0
```

Le code ci-dessus est bien un programme car il est syntaxiquement correct. C'est de plus un algorithme puisqu'il s'arrête forcément : soit après l'exécution de $\[e\](e)$, soit si le pseudo-code de $\[e\]$ contient une instruction non syntaxiquement correcte, soit enfin après l'exécution de $K$ instructions de $\[e\](e)$.

Enfin, il va rendre :

- 1 si $\[e\](e)$ s'arrête en moins de $K$ instructions et rend la valeur 0
- 0 dans tous les autres cas.

{% attention "**À retenir**"%}
Il existe un un algorithme qui permet d'exécuter au plus $K$ instructions d'un programme.
{% endattention %}

## Décideur final

On a maintenant tous les ingrédients pour créer le décideur, dépendant d'une fonction calculable $f$, qui va nous servir de preuve.

```text
Nom : complexité-f (on va le noter cf(n))
Entrée : un entier n
Programme :
    K = f(n)
    e = la représentation binaire de n en ajoutant des 0 au début pour avoir une longueur multiple de 32.
    Si d(e) vaut 0
        rendre 0
    sinon
        Rendre E(e, K)

```

On a bien affaire à un algorithme puisque :

- $f$ est calculable
- $P(e)$ et $E(e, K)$ sont des pseudo-codes.

On peut donc lui associer :

- sa complexité $C_{cf}(n)$
- son langage $L_f$

{% note "**Proposition**" %}
On a : $C_{cf}(n) = \Omega(f(n))$
{% endnote %}
{% details "preuve", "open" %}
Comme tout pseudo-code sera encodé par un entier, il existe $n_0$ l'entier correspondant au programme suivant :

```text
tant que Vrai:
    ne rien faire
```

Qui ne va jamais s'arrêter.

Comme $\[e\] = \[e + 00000000000000000000000000001010\]$ il va exister une infinité d'entiers avec $\[e_0\]$ comme pseudo-code associé et que pour ces entrées $E(e, f(n))$ va effectuer $f(n)$ instructions de $\[e_0\]$ qui boucle à l'infini, on a bien que $C_{cf}(n) = \Omega(f(n))$

{% enddetails %}

On peut être plus précis quand à la complexité de $cf(n)$ :

1. il doit calculer $f(n)$.
2. il doit savoir si $f(n)$ correspond à un pseudo-code, ce qui peut se faire en carré de la longueur binaire de $f(n)$ : $\mathcal{O}(\log^2(f(n)))$.
3. il exécute au pire $f(n)$ instructions de a $\[e\](n)$ et décrémente le compteur $K$ à chaque fois. Comme en informatique théorique on ne manipule que des bits, cette décrémentation va prendre non pas 1 instruction mais la taille binaire de $K$, c'est à dire $\log(f(n))$, opération. Cette étape va donc prendre au maximum $f(n) \cdot \log(f(n))$ opérations.

La complexité théorique de $cf(n)$ est donc $C_{cf}(n) = \Theta(f(n) \cdot \log(f(n)))$.

Terminons en montrant que le langage de $cf$ est de complexité supérieure à $f(n)$ :

{% note "**Proposition**" %}
La complexité de $L_f$ est en $\Omega(f(n))$
{% endnote %}
{% details "preuve", "open" %}
Supposons qu'il existe un décideur $B(e)$ de complexité asymptotique $C_B(n)$ strictement inférieure à $f(n)$. Il existe alors $N_0$ tel que $C_B(n) < f(n)$ pour tout $n>N_0$.

Le décideur $B$ pouvant être décrit par un pseudo-code, il existe une entrée $e_B$, associée à l'entier $n_B$ tel que $d(e_B)$ vaut 1 et $\[e_B\]$ vaut $B$. En ajoutant assez de retour à la ligne au pseudo-code de $B$, il va exister un entier $n^{\star} > \max(N_0, n_B)$ tel que $P(e^{\star})$ vaut 1 et $\[e^{\star}\]$ vaut $B$ (avec $e^{\star}$ le mot binaire associé à $n^{\star}$).

Comme $n^{\star} > N_0$, on a que $C_B(n^{\star}) < f(n^{\star})$ et donc que $\[e^{\star}\](e^{\star}) = \[e_B\](e^{\star})$ et va être exécuté dans sont intégralité par $cf(n^{\star})$. Ceci amène à une contradiction car :

- soit $e^{\star} \in L_f$ et donc $\[e_B\](e^{\star})$ vaut 1 mais comme il est exécuté dans son intégralité par $cf(n^{\star})$, on a $cf(n^{\star})$ qui vaut 0 et $e^{\star} \notin L_f$
- soit $e^{\star} \notin L_f$ et donc $\[e_B\](e^{\star})$ vaut 0 mais comme il est exécuté dans son intégralité par $cf(n^{\star})$, on a $cf(n^{\star})$ qui vaut 1 et $e^{\star} \in L_f$

{% enddetails %}

## Théorèmes

La proposition précédente montre qu'il existe des langages de complexité aussi grande que l'on veut puisque $f(n)$ est une fonction calculable quelconque. On a donc le théorème suivant :

<div id="hiérarchie-complexité"></div>
{% note "**Théorème**" %}
Pour toute fonction calculable $f$, il existe des problèmes de décision de complexité $\Omega(f(n))$.
{% endnote %}

Comme $2^n$, $n!$ voir la [fonction d'Ackermann](https://fr.wikipedia.org/wiki/Fonction_d%27Ackermann) sont des fonctions calculables, il existe des problèmes de décision de très grande complexité !

{% attention "**À retenir**"%}
Il existe des problèmes algorithmiques de complexités aussi grande ou aussi petite que l'on veut.
{% endattention %}

Ainsi on en conclut :

{% note "**Proposition**" %}
Il existe des problèmes de décision décidables qui ne sont pas dans $NP$.
{% endnote %}
{% details "preuve", "open" %}

La complexité d'un problème de décision est bornée par $\mathcal{O}(|e|^k\cdot 2^{|e|^k})$ où $\mathcal{O}(|e|^k)$ est la complexité de son vérifieur efficace. Or [le théorème de la hiérarchie des complexité](../décideur-décision/#hiérarchie-complexité) nous indique qu'il existe des problèmes de décision de complexité plus grande que toute fonction calculable, en particulier $f(n) = 2^{2^n}$ qui sera en $\Omega(n^k\cdot e^{n^k})$, quelque soit l'entier $k$.

{% enddetails %}

Nous ne donnons pas d'exemple concret, bien qu'il en existe, car ils demanderaient beaucoup de définitions pour être compris. Retenez seulement que trouver un problème décidable qui n'est pas dans $NP$ est difficile : la très grande majorités des problèmes de décisions que vous rencontrerez seront dans $NP$ et les autres problèmes pourront facilement s'écrire sous la forme d'un problème de décision de $NP$ à résoudre.
