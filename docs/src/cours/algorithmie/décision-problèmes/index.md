---
layout: layout/post.njk
title: "Problèmes et algorithmes de décision"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On définit la classe de problèmes NP comme étant ceux permettant de vérifier efficacement leurs solutions. Cette approche, pratique, permet de comprendre l'utilité de cette classe, mais n'est pas très opérationnelle pour faire des démonstrations.

Nous allons dans cette partie redéfinir la notion de problème algorithmique via les problèmes de décision.

{% lien %}

- <https://www2.math.upenn.edu/~wilf/AlgoComp.pdf>
- <https://www.youtube.com/watch?v=s9l6QTX9n0Q&list=PLwF3A0R8OzMpO6_9WbT1kK16akYFh3_Nt>
- <https://www.youtube.com/watch?v=KydXVE9Su5g&list=PLdUzuimxVcC0DENcdT8mfhI3iRRJLVjqH>

{% endlien %}

## Décision et algorithmes

Rappelons qu'un algorithme est [dans toute sa généralité](../bases-théoriques/calculabilité/#algorithme-fonction){.interne} une fonction qui prend et rend un mot de $\\{0, 1\\}$. On peut lui associer de façon équivalente la fonction $v_f : \\{0, 1\\}^\star \times \\{0, 1\\}^\star \rightarrow \\{0, 1\\}$ ci-dessous :

$$
v_f(n, m) = \left\\\{
    \begin{array}{ll}
        1 & \mbox{si } f(n) = m\\\\
        0 & \mbox{sinon.}
    \end{array}
\right.
$$

Un algorithme est ainsi [un vérifieur](../problèmes-NP/#vérifieur). De là, on peut combiner les deux mots en entrée en un seul pour arriver à la formulation d'un algorithme qui nous intéressera ici. Pour cela, la façon classique de procéder est de coder chaque information (0 et 1) sur 2 bits ce qui permet d'avoir un caractère supplémentaire de séparation :

- on code l'information `0`{.language-} en `00`{.language-}
- on code l'information `1`{.language-} en `01`{.language-}
- `11`{.language-} est le caractère de séparation des paramètres

Ainsi, si un algorithme possède 2 paramètres valant `1001`, `001` par exemple, cela devient le paramètre `0100000111000001`. on modifie alors l'algorithme pour que la première chose qu'il fasse soit de retrouver les deux paramètres en entrée :

1. on trouve les paramètres en découpant la chaîne d'entrée aux endroits où se trouvent le séparateur `11`{.language-}
2. on reconvertit chaque caractère en binaire en ne prenant qu'un bit sur 2

Au final on obtient qu'un algorithme est équivalent à un **_décideur_** :

<div id="décideur"></div>
{% note "**Définition**" %}
Un **_décideur_** est un algorithme de :

$$f: \\{0, 1\\}^\star \rightarrow \\{0, 1 \\}$$

{% endnote %}

On peut représenter un algorithme sous 3 formes équivalentes :

- une **_fonction_** : $f: \\{0, 1\\}^\star \rightarrow \\{0, 1 \\}^\star$ qui permettent le calcul effectif,
- un **_décideur_** : $d: \\{0, 1\\}^\star \rightarrow \\{0, 1 \\}$ qui permettent de séparer les mots en 2 ensembles, ceux qui sont _vrais pour $A$_ : $\\{ x \vert A(x) = 1 \\}$ et les autres
- un **_vérifieur_** : $v: \\{0, 1\\}^\star \times \\{0, 1\\}^\star \rightarrow \\{0, 1\\}$ qui, associé à un problème algorithmique $P$, permettent de vérifier si le couple $(x, y)$ en entrée est tel que $y$ soit une solution de $P$ avec $x$ comme entrée.

{% note "**À retenir**" %}
D'un point de vue théorique on peut donc uniquement considérer la version décideur d'un algorithme sans aucune perte de généralité.
{% endnote %}

En conclusion, en utilisant les machines de Turing, on définit les problème algorithmique comme étant ds problèmes de décision :

<div id="algorithme-décision"></div>
{% note "**Définition**" %}
Un **_problème de décision_** est un problème algorithmique n'acceptant que deux réponses : OUI ou NON, et pouvant être résolu par une machine de Turing acceptant tous les mots de $\\{0, 1\\}^\star$ et dont les sorties sont 0 (FAUX) ou 1 (VRAI).

Le **_langage_** d'un problème de décision est l'ensemble des mots de sortie 1.
{% endnote %}

Problème et langage sont donc deux notions équivalentes : un algorithme est caractérisé par l'ensemble des mots qu'il reconnaît.

## Complexités des problèmes de décision

La complexité d'un problème est la complexité la plus petite d'une machine de Turing qui le résout. Comme résoudre un problème de décision revient à trouver un décideur pour son langage on a :

{% note "**Définition**" %}

La **_complexité d'un langage (décidable)_** est la complexité la plus faible d'une machine de Turing qui l'accepte.

{% endnote %}

Comme une machine de Turing prend en entrée un mot de $\\{0, 1\\}^\star$, sa complexité sera forcément calculé par rapport à sa taille. Pour une machine de Turing $M$ prenant une entrée $E$ en paramètre, on notera dans cette partie :

- $C(\vert E \vert)$ sa [complexité](../complexité-calculs/définitions/#complexité){.interne}.
- $S(\vert E \vert)$ sa [complexité spatiale](../complexité-calculs/définitions/#complexité-spatiale){.interne},

On sait que la complexité spatiale d'une machine de Turing est forcément plus petite que sa complexité temporelle, mais la proposition suivante va plus loin et propose un encadrement :

{% note "**Proposition**" %}
Pour toute machine de Turing sans instructions inutiles, on a l'encadrement :

<div>
$$
S(n) \leq C(n) \leq \mathcal{O}(S(n) \cdot 2^{S(n)})
$$
</div>

{% endnote%}
{% details "preuve", "open" %}
On suppose que la machine de Turing correspond à un pseudo-code à $L$ instructions.

1. si la même ligne est exécutée plusieurs fois elle laisse à chaque fois la mémoire dans un état différent, sans quoi (les mêmes causes ayant les mêmes conséquences) le pseudo-code va forcément boucler indéfiniment. Chaque ligne va donc être exécutée au maximum $2^{S(n)}$ fois
2. chaque ligne peut lire ou modifier toutes les cases utilisées de la mémoire, sa complexité est donc en $\mathcal{O}(S(n))$

La complexité totale est donc bornée par $L \cdot 2^{S(n)} \cdot \mathcal{O}(S(n))$ et comme le nombre d'instructions du décideur est une constante on en déduit le résultat demandé.

{% enddetails %}

## P, NP et décision

On peut très facilement définir la classe $P$ :

{% note "**Définition**" %}
**_Un langage est de la classe_** $P$ s'il existe une machine de Turing de complexité polynomiale qui l'accepte.
{% endnote %}

Pour définir précisément ce qu'est la classe NP en revanche, il faut introduire un autre modèle de Machine de Turing, les machines non déterministes :

{% aller %}
[Machines de Turing non déterministes](./Turing-non-déterministe){.interne}
{% endaller %}

On a alors :

{% note "**Définition**" %}
**_Un langage est de la classe_** $NP$ s'il existe une machine de Turing non déterministe de complexité polynomiale qui l'accepte.
{% endnote %}

La classe de problème $NP$ a été précédemment construite via l'existence d'un vérifieur polynomial qui vérifie si la solution est correcte ou pas.
Avec cette nouvelle définition, le certificat est la suite de choix effectués par la machine de Turing non déterministe. Voyez ces choix comme un oracle (ou un prof) qui vous guide tout au long du déroulement de la machine. On peut s'en passer mais cela prendrait beaucoup de temps (faire tout les choix amène à une complexité exponentielle). Si on sait déjà ou aller en revanche, on peut trouver rapidement une solution (en temps polynomiale).

{% attention %}
Tout ceci fonctionne car le nombre d'état est une **constante**, il ne dépend pas de l'entrée qui peut être aussi grande que l'on veut.
{% endattention %}

## Cas du NON

{% aller %}
[co-NP](./co-NP){.interne}
{% endaller %}

## Problèmes NP-complets

{% aller %}
[Problèmes NP complets](./problèmes-NPC){.interne}
{% endaller %}

## Hiérarchie des complexités

Terminons cette partie en montrant qu'il existe bien d'autres algorithmes que ceux de NP. On peut même trouver des problèmes de toute complexité.

{% aller %}
[Hiérarchie des complexités](hiérarchie-complexité){.interne}
{% endaller %}
