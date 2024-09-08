---
layout: layout/post.njk
title: "Langages et mots"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


> on se restreint à 0, 1 mais marche aussi si alphabet plus gros

> TBD <https://www.youtube.com/watch?v=miOofcAiINM&list=PLhqug0UEsC-IDomfNsn8e3neoy34o8oye&index=2>
>

## Vérifieur et Décideur

Rappelons qu'un algorithme est [dans toute sa généralité](../../bases-théoriques/calculabilité/#algorithme-fonction){.interne} une fonction qui prend et rend un mot de $\\{0, 1\\}$. On peut lui associer de façon équivalente la fonction $v_f : \\{0, 1\\}^\star \times \\{0, 1\\}^\star \rightarrow \\{0, 1\\}$ ci-dessous :

$$
v_f(n, m) = \left\\\{
    \begin{array}{ll}
        1 & \mbox{si } f(n) = m\\\\
        0 & \mbox{sinon.}
    \end{array}
\right.
$$

On peut voir l'algorithme $v_f$ comme un **_vérifieur_**. Il vérifie que le second paramètre est la sortie du premier paramètre. On reparlera de ces algorithmes plus tard dans le cours, pour l'instant ils nous permettent de montrer que l'espace d'arrivée d'un algorithme peut être uniquement deux valeurs 0 ou 1. Un algorithme peut ainsi être vu comme un vérifieur :

<div id="vérifieur"></div>
{% note "**Définition**" %}
Un **_vérifieur_** est une fonction de :

$$v: \\{0, 1\\}^\star \times \\{0, 1\\}^\star \rightarrow \\{0, 1\\}$$
{% endnote %}

De là, on peut combiner les deux mots en entrée en un seul pour arriver à la formulation d'un algorithme qui nous intéressera ici. Pour cela, la façon classique de procéder est de coder chaque information (0 et 1) sur 2 bits ce qui permet d'avoir un caractère supplémentaire de séparation :

- on code l'information `0`{.language-} en `00`{.language-}
- on code l'information `1`{.language-} en `01`{.language-}
- `11`{.language-} est le caractère de séparation des paramètres

Ainsi, si un algorithme possède 2 paramètres valant `1001`, `001` par exemple, cela devient le paramètre `0100000111000001`. on modifie alors l'algorithme pour que la première chose qu'il fasse soit de retrouver les deux paramètres en entrée :

1. on trouve les paramètres en découpant la chaîne d'entrée aux endroits où se trouvent le séparateur `11`{.language-}
2. on reconvertit chaque caractère en binaire en ne prenant qu'un bit sur 2

Au final on obtient qu'un algorithme est équivalent à un **_décideur_** :

<div id="décideur"></div>
{% note "**Définition**" %}
Un **_décideur_** est une fonction de :

$$f: \\{0, 1\\}^\star \rightarrow \\{0, 1 \\}$$

{% endnote %}

On ne va bien sur pas uniquement utiliser des décideurs en pratique, loin de là, mais cela montre que l'on peut se contenter de considérer les propriétés théoriques des décideurs puisqu'on pourra les appliquer sans perte de généralité aux autres types d'algorithmes.

Avant de passer à l'étude théorique des problèmes et de les classer en plusieurs catégories, analysons les 3 formes d'algorithmes (équivalentes) utiles :

{% attention "**À retenir**" %}
On peut représenter un algorithme sous 3 formes équivalentes :

- les **_fonctions_** : $f: \\{0, 1\\}^\star \rightarrow \\{0, 1 \\}^\star$ qui permettent le calcul effectif,
- les **_décideurs_** : $d: \\{0, 1\\}^\star \rightarrow \\{0, 1 \\}$ qui permettent de séparer les mots en 2 ensembles, ceux qui sont _vrais pour $A$_ : $\\{ x \vert A(x) = 1 \\}$ et les autres
- les **_vérifieurs_** : $v: \\{0, 1\\}^\star \times \\{0, 1\\}^\star \rightarrow \\{0, 1\\}$ qui, associé à un problème algorithmique $P$, permettent de vérifier si le couple $(x, y)$ en entrée est tel que $y$ soit une solution de $P$ avec $x$ comme entrée.

{% endattention %}

## Langages et algorithmes

La partie précédente nous a montré qu'un algorithme peut être vu comme un décideur et, les mots qui sont vrais, son langage :

{% note "**Définition**" %}
On appelle **_langage_** d'un décideur $d$ l'ensemble $d^{-1}(1)$.

On dira qu'un décideur $d$ **_accepte le langage_** $L$ si $L = d^{-1}(1)$ et qu'un langage $L$ est **_décidable_** s'il existe un algorithme pour l'accepter.
{% endnote %}

Il est donc équivalent de parler de langages ou d'algorithmes, et chaque problème algorithmique est un langage à reconnaître.

Tout langage n'est bien sur pas décidable. On a vu qu'il était impossible de savoir _a priori_ si un programme va s'arrêter ou pas ([l'algorithme STOP n'existe pas](../../bases-théoriques/arrêt-rice/#algorithme-STOP){.interne}). Le langage composé des pseudo-codes associés aux algorithmes — c'est à dire les programmes qui s'arrêtent — n'est donc pas décidable. En revanche, le langage composé des pseudo-codes, est décidable (on peut facilement vérifier si un texte respecte les règles syntaxiques associé à un pseudo-code).

{% exercice %}
Montrez que l'ensemble des palindromes d'un alphabet $\mathcal{A}$ est décidable.
{% endexercice %}
{% details "corrigé" %}

```python
def palindrome(mot):
    for i in range(len(mot)):
        if mot[i] != mot[len(mot) - 1 - i]:
            return False
    return True

```

{% enddetails %}

> même distinction entre programme et algorithme : langages reconnaissable si programme (ne s'arrête pas forcément).
