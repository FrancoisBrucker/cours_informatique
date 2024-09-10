---
layout: layout/post.njk
title: "Recherche universelle"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On doit cet algorithme à [Léonid Levin](https://fr.wikipedia.org/wiki/Leonid_Levin).

L'algorithme de recherche universelle est un algorithme permettant de résoudre tout problème de NP, de manière optimale du moment qu'on ait un vérifieur pour lui.

{% lien %}
[Une vidéo de l'excellence chaîne polylog](https://www.youtube.com/watch?v=9ONm1od1QZo)
{% endlien %}

## Recherche universelle première approche

> TBD dire qu'on peut le faire en python :
>   1. on envoie un texte dans l'interpréteur et soit il plante soit c'est du python
>   2. avec le débugeur on peut exécuter une instruction à la fois
>   3. k instructions les k premiers (pas encore finis) puis on augmente k
>   3. si ça plante on le sort de la liste des programmes
>   4. s'il finit on vérifie si c'est ok. Si c'est pas ok on le sort de la liste des programmes

> TBD on ajoute juste une instruction à chaque fois.
> Reste possible mais complexité plus élevée.

## Exécution fragmenté d'un algorithme

Pour comprendre comment fonctionne la recherche universelle, commençons par étudier l'algorithme suivant, qui prend en paramètre un algorithme `A`{.language-} et une de ses entré possible, `E`{.language-} :

```python
def exécution_fragmentée(T, A, E):
  I = 1
  tant que I < T:
    exécuter I instructions de A(E)
    Si l'algorithme A s'est arrêté:
      rendre sa sortie
    I = 2 * I
```

On a la proposition suivante :

{% note "**Proposition**" %}
La complexité d'exécution de l'algorithme `exécution_fragmentée`{.language-} est en $\Theta(C(\vert E \vert ))$ où $C(n)$ est la complexité de l'algorithme `A`{.language-}
{% endnote %}
{% details "preuve", "open" %}
Supposons que l'algorithme $A(E)$ s'arrête au bout de $K$ instructions. Le nombre maximum d'itération de l'algorithme est alors donné pour `exécution_fragmentée(K, A, E)`{.language-}

L'algorithme `exécution_fragmentée(T, A, E)`{.language-} sera rentré dans la boucle `tant que`{.language-} $\log_2(K)$ fois puisque c'est à ce moment que $I$ sera égal ou plus grand que $K$. Le nombre total d'instructions de l'algorithme `exécution_fragmentée(A, E)`{.language-} a alors été :

$$
1 + 2 + 4 + \dots + 2^i + \dots + 2^{\log_2(K)}
$$

C'est à dire que :

1. les $K/2$ dernières instructions de $A(E)$ ont été exécutées 1 fois
2. parmi les $K/2$ premières opérations, la moitié ($K/4$) a été exécutée 2 fois (pour les 2 dernières boucles)
3. parmi les $K/4$ premières opérations, la moitié ($K/8$) a été exécutée 3 fois (pour les 3 dernières boucles)
4. ...
5. la première opération a été exécuté $\log_2(K)$ fois

Le nombre d'opérations effectuées par l'algorithme est alors :

$$
K\cdot \frac{1}{2} + K\cdot \frac{2}{4} + K\cdot \frac{3}{8} + \dots + K\cdot \frac{i}{2^i} + \dots + K\cdot \frac{\log_2(K)}{2^{\log_2(K)}} = K\cdot (\sum_{1\leq i \leq \log_2{K}}\frac{i}{2^i})
$$

En notant $S_n = \sum_{1\leq i \leq n}$ on a :

$$
\frac{S_n}{2} = S_n - \frac{S_n}{2} = \sum_{1\leq i \leq n }\frac{1}{2^i} = 1- \frac{1}{2^n}
$$

Et donc $S_n \leq S_{\infty} = 2$ ce qui nous permet de conclure que le nombre d'opérations total est $2K$, ce qui conclut la preuve.

{% enddetails %}

## Exécution fragmentée générale

L'algorithme de la recherche universelle va procéder un peu de la même manière que celui d'exécution fragmentée mais pour tous les algorithmes.

Un pseudo-code étant un texte, on peut considérer tous les textes rangés par ordre lexico-graphique. On peut tenter d'exécuter chaque texte comme un pseudo-code et voir ce qu'il se passe. Exécuter $K$ instructions d'un de ces texte peut résulter en 3 cas :

1. un plantage (ce n'est pas un pseudo-code on tente d'exécuter quelque chose qui n'est pas une instruction, on fait une instruction interdite comme une division par zéro par exemple, etc)
2. le texte est un pseudo-code valide et on a exécuté entièrement son code.On peut récupérer sa sortie.
3. le texte est un pseudo-code valide (au moins pour les $K$ instructions) mais il ne s'est pas arrêté : il tourne toujours après $K$ instructions.

On considère alors l'algorithme `next(B)`{.language-} qui, rend la chaîne $B'$ qui suit la chaîne $B$ dans l'ordre lexico-graphique.

```python
def exécution_fragmentée_universelle(A, E):
  I = 1
  tant que VRAI:
    B = ""
    tant que I ≥ 1:
      B = next(B)
      exécuter I instructions de B(E)
      Si on s'est arrêté et que B == A:
        rendre sa sortie
      I = I / 2
    I = 2 * I
```

{% note "**Proposition**" %}
La complexité d'exécution de l'algorithme `exécution_fragmentée_universelle`{.language-} est en $\Theta(C(\vert E \vert ))$ où $C(n)$ est la complexité de l'algorithme `A`{.language-}
{% endnote %}
{% details "preuve", "open" %}
Supposons que l'algorithme $A(E)$ s'arrête au bout de $K$ instructions et que la chaîne de caractère qui correspond à son pseudo-code soit en position $L$ de la liste ordonnée de tous les textes.

L'algorithme `exécution_fragmentée_universelle`{.language-} va s'arrêter lorsqu'il aura effectué $K$ opération de l'algorithme $A$

Tout se passe alors comme si :

- on avait exécuté `exécution_fragmentée(K2**L, A1, E)`{.language-} pour `A1`, le premier élément de la liste ordonnée des textes
- on avait exécuté `exécution_fragmentée(K2**(L-1), A2, E)`{.language-} pour `A2`, le second élément de la liste ordonnée des textes
- ...
- on avait exécuté `exécution_fragmentée(K, AL, E)`{.language-} pour `AL`, le $L$ ème élément de la liste ordonnée des textes
- on avait exécuté `exécution_fragmentée(K/2, A(L+1), E)`{.language-} pour `A(L+1)`, le $L+1$ ème élément élément de la liste ordonnée des textes
- ...
- on avait exécuté `exécution_fragmentée(1, A(L+1), E)`{.language-} pour `A(L+log(K))`, le $L+\log_2(K)$ ème élément élément de la liste ordonnée des textes.

La complexité maximale est alors :

<div>
$$
\begin{array}{lcl}
2 \cdot 2^L\cdot K +  2 \cdot 2^{L-1} \cdot K + \dots + 2 \cdot 2^{0} \cdot K + 2 \cdot \frac{1}{2} \cdot K + \dots + 2 \cdot \frac{1}{2^i} \cdot K + \dots + 2 \cdot \frac{1}{2^{\log_2(K)}} \cdot K&=&\\
2\cdot(2^{L+1}-1)\cdot K + 2\cdot (1-\frac{1}{2^{\log_2(K)}})\cdot K&\leq&\\
2^{L+2}\cdot K
\end{array}
$$
</div>

Comme $L$ est une constante, on a bien le résultat demandé
{% enddetails %}

On voit que la complexité asymptotique est la même que celle de l'algorithme initial. Ce qui change c'est la constante multiplicative, $2^{L+2} qui peut être gigantesque !

## Recherche universelle

L'algorithme de recherche universelle est une variation de l'algorithme précédent pour les problèmes de NP. Soit $P$ un problème de NP et $v$ un de ses vérificateurs.

On alors l'algorithme :

```python
def recherche_universelle(v, E):
  I = 1
  tant que VRAI:
    B = ""
    tant que I ≥ 1:
      B = next(B)
      exécuter I instructions de B(E)
      Si B(E) s'est arrêté et que v(B(E), E) est vrai:
        rendre sa sortie
      I = I / 2
    I = 2 * I
```

{% note "**Proposition**" %}
La complexité d'exécution de l'algorithme `recherche_universelle`{.language-} est en $\Theta(C(\vert E \vert ) + \log_2(C(\vert E \vert )) \cdot D(\vert E \vert ))$ où :

- $C(n)$ est la complexité minimale d'un algorithme résolvant $P$
- $D(n)$ est la complexité du vérifieur $v$

{% endnote %}
{% details "preuve", "open" %}
Idem que la preuve précédente. Il faut juste ajouter qu'il faut vérifier chaque pseudo-code (il y en a $L+ \log_2(C(\vert E \vert ) ))$ qui s'arrête une fois.
{% enddetails %}

Dans de très nombreux cas, $D(n)$ est petite devant $C(n)$, par exemple si $D(n) = \Theta(n^a)$ et $C(n) = \Theta(n^b)$ avec $b>a$ puisqu'asymptotiquement $\frac{n^{\epsilon}}{\ln(n)}$ tend vers l'infini. Et on peut négliger le terme en $D(n)$, ce qui donne un algorithme optimal pour résoudre tout problème de NP !

Donc si $P = NP$ alors la recherche universelle est l'algorithme optimal qui résout tout. Bien sur l'arnaque se situe au niveau de la constante multiplicative, $2^L$ qui peut être gigantesque ce qui fait que même si asymptotiquement le résultat est optimal ce n'est pas le cas dans des cas d'utilisation normale des algorithme. La recherche universelle n'est donc pas une excuse pour ne pas chercher l'algorithme le plus efficace pour résoudre un problème.