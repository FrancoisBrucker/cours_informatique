---
layout: layout/post.njk
title: "Problème algorithmique"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous n'avons pour l'instant décrit les algorithmes que comme des fonctions permettant de calculer des nombres. La principale utilité de ceux-ci est cependant ailleurs. Les algorithmes sont utilisés parce ce qu'il permettent de répondre à des questions, de résoudre des problèmes. Bref, le résultat d'un algorithme a un _sens_.

## Problème

Formalisons cette intuition en définissant la notion de **_problème_**.

{% note "**Définition**" %}
Un **_problème_** est un texte composé de 3 parties :

- **nom** : le nom du problème
- **données** : les paramètres dont on a besoin
- **question** : ce que l'on cherche à résoudre

{% endnote %}

Par exemple :

{% note "**Problème**" %}

- **nom** : maximum
- **données** : un tableau d'entiers
- **question** : quel est l'entier maximum du tableau ?

{% endnote %}

Une importante classe de problème est **_les problèmes de décision_** :

<span id="problème-décision"></span>
{% note "**Définition**" %}
Un **_problème de décision_** est un problème dont la réponse est soit OUI, soit NON.

{% endnote %}

Par exemple :

{% note "**Problème de décision**" %}

- **nom** : présence
- **données** :
  - v : un entier
  - t : un tableau d'entiers
- **question** : v est-elle une valeur du tableau t ?

{% endnote %}

On se placera dans ce cours dans un cadre algorithmique. On se posera donc uniquement des questions sérieuses comme la recherche d'un éléments dans un tableau ou l'existence d'un algorithme pour résoudre un problème. On laissera de côté les problèmes futiles comme ["quand est-ce qu'on mange ?"](https://www.youtube.com/watch?v=WtetsFQHD9A) ou encore ["quel est le sens de la vie ?"](https://www.youtube.com/watch?v=LAwDWZoETk4).

{% note "**Définition**" %}
**_Un problème est algorithmique_** s'il existe un algorithme pour le résoudre, c'est à dire que cet algorithme :

- prend en paramètres les entrées du problème
- donne la réponse à la question.

{% endnote %}

Dans la suite de ce cours nous allons nous concentrer sur les problèmes algorithmique et voir comment les résoudre le plus vite possible. Mais avant de conclure cette courte partie examinons quelques problèmes non décidables mais informatisable.

## <span id="décidable"></span> Décidabilité

On peut très souvent se restreindre aux problèmes de décision solvable par un algorithme :

{% note "**Définition**" %}
Un problème de décision est **_décidable_** s'il existe un algorithme pour le résoudre (on dit un **_décideur_**), c'est à dire que cet algorithme :

- prend en paramètres les entrées du problème
- répond OUI ou NON selon la véritable réponse à donner.

{% endnote %}

<span id="décideur"></span>
{% note "**Définition**" %}
Un **_décideur_** est un algorithme qui pour toute entrée, répond _OUI_ ou _NON_.
{% endnote %}
{% info %}
Vous verrez parfois des décideurs qui à la place de répondre OUI rendent 1 et à la place de répondre NON, rendent 0.

L'important est que la sortie du décideur soit binaire et que l'on puisse associer une sémantique de vérité à la sortie.

{% endinfo %}

En effet, on peut très souvent se ramener à un problème décidable pour prouver qu'un problème est algorithmique. Par exemple le problème maximum peut être associé au problème de décision `maximum-v`{.language-} :

{% note "**Problème de décision**" %}

- **nom** : maximum-v
- **données** :
  - t : un tableau d'entiers
  - v un entier
- **question** : v est-elle l'entier maximum du tableau ?

{% endnote %}

Si maximum-v est décidable, il suffit d'exécuter l'algorithme décideur pour chaque valeur de t.

En revanche le problème de décision suivant n'est pas décidable :

{% note "**Problème de décision**" %}

- **nom** : arrêt
- **données** :
  - a : un entier représentant un programme
  - n : un entier
- **question** : a(n) s'arrête-t-il ?

{% endnote %}

## Reconnaissabilité

Il existe un cas plus faible que la décidabilité, c'est la **_reconnaissabilité_**, qui permet d'utiliser des programmes plutôt que des algorithme pour décider :

{% note "**Définition**" %}
Un problème de décision est **_reconnaissable_** s'il existe un programme qui prend en paramètres les entrées du problème et :

- s'arrête que pour les réponse OUI
- ne s'arrête pas les réponses NON

{% endnote %}

Il est clair qu'un problème décidable est reconnaissable, il suffit de laisser tourner indéfiniment le décideur plutôt que de lui faire répondre NON, mais la réciproque est fausse, le problème de l'arrêt étant clairement reconnaissable (il suffit de laisser tourner l'algorithme et s'il s'arrête répondre 1).

## Exemple

Nous allons finir cette partie en montrant deux exemples de problèmes qui ont fait grand bruit à l'époque.

### <span id="poli-z"></span>Racines de polynômes à coefficients dans $\mathbb{Z}$

{% note "**Problème de décision**" %}

- **nom** : racine polynôme
- **données** : $P(X)$ un [polynôme](https://fr.wikipedia.org/wiki/Polyn%C3%B4me) à coefficients dans $\mathbb{Z}$
- **question** : $P(X)$ Possède-t-il une [racine](https://fr.wikipedia.org/wiki/Racine_d%27un_polyn%C3%B4me) dans $\mathbb{N}$ (un entier $a$ tel que $P(a) = 0$) ?

{% endnote %}

Ce problème est reconnaissable :

{% note "**Proposition**" %}
Le problème de décision `racine polynôme`{.language-} est reconnaissable.
{% endnote %}
{% details "preuve", "open" %}

On peut facilement créer un algorithme qui, à partir d'un polynôme $P(x)$ à coefficients dans $\mathbb{Z}$ et d'un entier $a$ calcule $P(a)$.

Il suffit ensuite d'essayer tous les entiers un à un. Si le polynôme en entrée admet une racine entière, on va bien tomber dessus à un moment donné.

{% enddetails %}

Il est même décidable !

{% note "**Proposition**" %}
Les racine d'un polynôme $P(X) = \sum_{i=0}^na_iX^i$ (avec $a_n \neq 0$) sont bornées par $\max( 1, \frac{\sum_{i=0}^{n-1}\mid a_i\mid}{\mid a_n\mid})$.
{% endnote %}
{% details "preuve" %}

On va montrer que pour tout $\mid X \mid > \max( 1, \frac{\sum_{i=0}^{n-1}\mid a_i\mid}{\mid a_n\mid})$, on a $\mid P(X)\mid > 0$.

On a en effet la suite d'implications :

<div>
$$
\begin{array}{lcll}
    \mid X \mid & > & \frac{\sum_{i=0}^{n-1}\mid a_i\mid}{\mid a_n\mid}&\mbox{et } \mid X \mid > 1\\
    \mid a_n X^n \mid & > & \sum_{i=0}^{n-1}(\mid a_i X^{n-1} \mid)&\\
    \mid a_n X^n \mid & > & \mid a_{n-1}X^{n-1}\mid + \mid X \mid \cdot \sum_{i=0}^{n-2}(\mid a_i X^{n-2} \mid)&\\
    \mid a_n X^n \mid & > & \mid a_{n-1}X^{n-1}\mid + \sum_{i=0}^{n-2}(\mid a_i X^{n-2} \mid)& \mbox{car } \mid X \mid > 1\\
    \mid a_n X^n \mid & > & \dots&\\
    \mid a_n X^n \mid & > & \sum_{i=0}^{n-1}\mid a_i X^{i} \mid&\\
    \mid a_n X^n \mid & > & \mid \sum_{i=0}^{n-1} a_i X^{i} \mid&\\
\end{array}
$$
</div>

qui prouvent que $\mid P(X) \mid = \mid a_nX^n + \sum_{i=0}^{n-1} a_i X^{i}\mid$ sera toujours non nul et du signe de $a_n$ pour tout $\mid X \mid > \max( 1, \frac{\sum_{i=0}^{n-1}\mid a_i\mid}{\mid a_n\mid})$
{% enddetails %}

{% note "**Corollaire**" %}
Le problème de décision `racine polynôme`{.language-} est décidable.
{% endnote %}
{% details "preuve", "open" %}

Toutes les racines du polynôme sont bornées par un nombre calculable, on pourra stopper l'algorithme d'énumération au bout d'un nombre déterminé d'itérations.

{% enddetails %}

### Racines de polynômes à plusieurs variables à coefficients dans $\mathbb{Z}$

En revanche les choses se corsent pour le problème ci-après, généralisation de `racine polynôme`{.language-} :

{% note "**Problème de décision**" %}

- **nom** : racine polynôme plusieurs variables
- **données** : $P(X)$ un [polynôme à plusieurs variables](https://fr.wikipedia.org/wiki/Polyn%C3%B4me_en_plusieurs_ind%C3%A9termin%C3%A9es) à coefficients dans $\mathbb{Z}$
- **question** : $P(X)$ Possède-t-il une [racine](https://fr.wikipedia.org/wiki/Racine_d%27un_polyn%C3%B4me) dans $\mathbb{N}$ (un entier $a$ tel que $P(a) = 0$) ?

{% endnote %}

{% note "**Théorème**" %}
Le problème `Racine polynôme plusieurs variables`{.language-} est un problème **reconnaissable** mais **indécidable**.
{% endnote %}
{% details "éléments de preuve", "open" %}
Cela a été [démontré en 1970 par Matiiassevitch](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Matiiassevitch) en prouvant que l'on ne pouvait pas borner les racines d'un polynôme à plusieurs variables.

Il n'existe donc pas d'algorithme qui s'arrête au bout d'un temps fini si un polynôme à plusieurs variables n'a pas de racine dans $\mathbb{N}$.

{% enddetails %}

Ce cas est historiquement important car il correspond au [dixième problème de Hilbert](https://fr.wikipedia.org/wiki/Dixi%C3%A8me_probl%C3%A8me_de_Hilbert).
