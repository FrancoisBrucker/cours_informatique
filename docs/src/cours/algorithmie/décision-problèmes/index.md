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

Un algorithme est ainsi [un vérifieur](../problèmes-NP/#vérifieur). Nous allons monter dans cette partie une version équivalente, plus simple à manipuler théoriquement, mais moins opérationnelle en pratique d'un algorithme.

### Décideur et algorithmes

 On peut combiner les deux mots en entrée d'un vérifieur en un seul pour arriver à la formulation d'un algorithme qui nous intéressera ici. Pour cela, la façon classique de procéder est de coder chaque information (0 et 1) sur 2 bits ce qui permet d'avoir un caractère supplémentaire de séparation :

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

> TBD un même problème peut se voir sous sa forme fonction, vérifieur ou décideur.
> TBD : exemple du Max tableau et de ? un élément strictement plus grand que K.

{% note "**À retenir**" %}
D'un point de vue théorique on peut donc uniquement considérer la version décideur d'un algorithme sans aucune perte de généralité.
{% endnote %}

### Langages et Turing

{% lien %}

- <https://pageperso.lis-lab.fr/~alexis.nasr/Ens/THL/mt.pdf>
- <https://www.enseignement.polytechnique.fr/informatique/INF423/uploads/Main/chap8-good.pdf>

{% endlien %}

Si on veut appliquer la notion de décideur à une machine de Turing, cela revient à ne considérer que la case du ruban sous le curseur lorsque la machine s'arrête. On dira alors :

<div id="accepte-rejette"></div>
{% note "**Définition**" %}
Soit $M$ une machine de Turing. Une entrée $E$ est :

- **_acceptée_** par $M$ si $M(E)$ s'arrête et que la case sous la position finale du curseur vaut 1
- **_rejetée_** par $M$ si $M(E)$ s'arrête et que la case sous la position finale du curseur vaut 0
{% endnote %}

> TBD exemple avec accepte, rejette et infini.

On peut alors chercher à connaître toutes les entrées acceptées par une machine :

{% note "**Définition**" %}
Soit $M$ une machine de Turing. Son **_langage_** $L$ est l'ensemble des entrées acceptées. On dira que :

- $M$ **_reconnaît_** $L$ si elle n'accepte que les élément de $L$.
- $M$ **_décide_** $L$ si elle si elle accepte les élément de $L$ et rejette tous les autres.
{% endnote %}

Remarquez que dans la définition précédente, **_décider un langage_** est bien plus fort qu'uniquement **_reconnaître un langage_** puisque la machine ne bouclera jamais indéfiniment.

> TBD reprendre exemple précédent. Puis transformer M pour qu'elle décide.

Enfin, l'algorithmie peut être vu comme la reconnaissance des ensembles pouvant être un langage reconnaissable ou, mieux encore, décidable.

{% note "**Définition**" %}
Un ensemble de mots  $L \subset \\{0, 1\\}^\star$ est appelé un **_langage_**. Il est :

- **_reconnaissable_** s'il existe une machine de Turing qui le reconnaît
- **_décidable_** s'il existe une machine de Turing que le décide.
{% endnote %}

> TBD exemple de langages reconnaissable et décidable.

### Décideur et Langage

En conclusion, en utilisant les machines de Turing, on définit les problèmes algorithmiques comme étant des problèmes de décision associé à un langage décidable :

<div id="algorithme-décision"></div>
{% note "**Définition**" %}
Un **_problème de décision_** est un problème n'acceptant que deux réponses : OUI ou NON, et tel qu'il existe une machine de Turing décidant l'ensemble des entrées OUI du problème.
{% endnote %}

Algorithme, décision et langages sont donc trois notions équivalentes : un algorithme est caractérisé par l'ensembles des mots qu'il décide.

## Complexités des problèmes de décision

La complexité d'un problème est la complexité la plus petite d'une machine de Turing qui le résout. Comme résoudre un problème de décision revient à trouver un décideur pour son langage on a :

{% note "**Définition**" %}
La **_complexité d'un langage (décidable)_** est la complexité la plus faible d'une machine de Turing qui le décide.

{% endnote %}

Comme une machine de Turing prend en entrée un mot de $\\{0, 1\\}^\star$, sa complexité sera forcément calculé par rapport à sa taille. Pour une machine de Turing $M$ prenant une entrée $E$ en paramètre, on notera dans cette partie :

- $C(\vert E \vert)$ sa [complexité](../complexité-calculs/définitions/#complexité){.interne}.
- $S(\vert E \vert)$ sa [complexité spatiale](../complexité-calculs/définitions/#complexité-spatiale){.interne},

On sait que la complexité spatiale d'une machine de Turing est forcément plus petite que sa complexité temporelle, mais la proposition suivante va plus loin et propose un encadrement :

{% note "**Proposition**" %}
Pour toute machine de Turing lisant toute son entrée, on a l'encadrement :

<div>
$$
S(n) \leq C(n) \leq S(n) \cdot 2^{S(n)}
$$
</div>

{% endnote%}
{% details "preuve", "open" %}

Si la machine lit toute ses donnée, il lui faudra se déplacer (une operation à chaque fois) sur chacune des cases du ruban où quelque chose est écrit, d'où : $S(n) \leq C(n)$.

Le curseur de la machine peut être sur $S(n)$ cases au maximum et pour ne pas boucler si le curseur repasse par une case où il était déjà présent, au moins une des valeurs des $S(n)$ cases doit être différente par rapport à son dernier passage. Comme il y a $2^{S(n)}$ possibilités pour les $S(n)$ cases (soit 0 soit 1 pour chaque case) il ne peut repasser par la même case que $^{S(n)}$ fois : il y a donc au maximum $S(n) \cdot 2^{S(n)}$ instructions d'où la seconde inégalité.

{% enddetails %}

## P, NP et décision

On peut maintenant redéfinir les classes $P$ et $NP$ grace aux langages. Commençons par la classe $P$ :

{% note "**Définition**" %}
**_Un langage est de la classe_** $P$ s'il existe une machine de Turing de complexité polynomiale qui le décide.
{% endnote %}

Pour définir précisément ce qu'est la classe NP en revanche, il faut introduire un autre modèle de Machine de Turing, les machines non déterministes :

{% aller %}
[Machines de Turing non déterministes](./Turing-non-déterministe){.interne}
{% endaller %}

On a alors :

{% note "**Définition**" %}
**_Un langage est de la classe_** $NP$ s'il existe une machine de Turing non déterministe de complexité polynomiale qui le décide.
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

## SAT est NP-complet

{% aller %}
[SAT est un problème NP-complet](./SAT-NPC){.interne}
{% endaller %}

On verra qu'il y en a beaucoup, beaucoup d'autres.

## Hiérarchie des complexités

Terminons cette partie en montrant qu'il existe bien d'autres algorithmes que ceux de NP. On peut même trouver des problèmes de toute complexité.

{% aller %}
[Hiérarchie des complexités](hiérarchie-complexité){.interne}
{% endaller %}
