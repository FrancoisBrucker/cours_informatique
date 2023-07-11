---
layout: layout/post.njk 
title:  "Problèmes décidable"

eleventyNavigation:
    order: 1
    prerequis:

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


On a vu dans la partie [fonctions](../fonctions){.interne} qu'un algorithme ne pouvait pas tout calculer, qu'il y a avait même bien plus de choses qu'on ne pouvait pas faire avec un algorithme que de chose qu'on pouvait faire avec.

Nous allons étudier le problème sous l'angle de *décidabilité*, c'est à dire de savoir si un problème donné admet un algorithme pour le résoudre.

{% info %}
On peut aussi regarder le problème sous l'angle de la [calculabilité](../calculabilité){.interne}, c'est à dire de savoir si telle fonction ou tel nombre peut être calculé par un algorithme.
{% endinfo %}

Ce qui faut retenir de cette partie :

* un décideur est un algorithme spécifique à un problème de décision donné. Il répond oui si l'entrée admet une réponse au problème et non sinon
* savoir si un algorithme va s'arrêter est un problème indécidable
* connaître les algorithmes qui résolvent tel ou tel problème est indécidable

## Problèmes de décision

Commençons par définir un *problème de décision* :

{% note "**définition**" %}
Un ***problème de décision***, est une question qui ne peut avoir que deux réponses *vrai* ou *fausse* selon l'entrée donnée.
{% endnote %}

Par exemple le problème suivant est un problème de décision :

* **nom** : premier
* **entrée** : un nombre $n$
* **question** : $n$ est-il un nombre premier ?

Un problème de décision est **décidable**,  si on peut lui associer un algorithme (on dit un *décideur*) qui répond comme lui :

{% note "**définition**" %}
Un ***décideur*** est un algorithme qui pour toute entrée, répond *Vrai* ou *faux*
{% endnote %}

Le problème de décision *premier* admet un décideur (il suffit de tester tous les entiers plus petit que $n$ pour voir si le reste de la division entière vaut 0), mais ce n'est pas de tous les les problèmes.

Par exemple le problème suivant [n'admet pas de décideur](./#arrêt){.interne}, il est **indécidable** :

* **nom** : arrêt
* **entrées** : un algorithme $A$, et une entrée $E$
* **question** : L'algorithme $A$ s'arrête-t-il avec $E$ comme entrée ?

La décidabilité est donc le fait de savoir si on peut reconnaître l'ensemble $L$ des entrées qui satisfont une propriété donnée :

{% note "**définition**" %}
Un ensemble de mots $L$ est ***décidable*** s'il existe un **décideur** qui répond *vrai* si l'entrée est dans $L$ et *faux* sinon.
{% endnote %}

Il existe un cas plus faible que la décidabilité, c'est la *reconnaissabilité* :

{% note "**définition**" %}
Un ensemble de mots $L$ est ***reconnaissable*** s'il existe un algorithme $M$ telle que $L = \mathcal{L}(M)$ (l'algorithme ne va s'arrêter que pour les entrées de $L$)
{% endnote %}

Notez que tout problème décidable est reconnaissable (à la place de répondre *Faux* on boucle indéfiniment), mais ce n'est pas le cas de tous les problèmes ([ce problème](./#poli-z){.interne} par exemple).

## Exemples

Nous allons montrer ici trois exemples de problèmes décidable ou non qui sont fondamentaux.

### <span id="poli-z"></span>Racines de polynômes à coefficients dans $\mathbb{Z}$

Soit le problème de décision suivant :

* **nom** : racine polynôme
* **entrées** : $P(X)$ un [polynôme](https://fr.wikipedia.org/wiki/Polyn%C3%B4me) à coefficients dans $\mathbb{Z}$
* **question** : $P(X)$ Possède-t-il une [racine](https://fr.wikipedia.org/wiki/Racine_d%27un_polyn%C3%B4me) dans $\mathbb{N}$ (un entier $a$ tel que $P(a) = 0$) ?

{% details "ce problème est reconnaissable" %}

On peut facilement créer un algorithme qui, à partir d'un polynôme $P(x)$ à coefficients dans $\mathbb{Z}$ et d'un entier $a$ calcule $P(a)$.

Il suffit ensuite d'essayer tous les entiers un à un. Si le polynôme en entrée admet une racine entière, on va bien tomber dessus à un moment donné.

{% enddetails %}

{% details "il est même décidable" %}

Soit $P(X) = \sum_{i=0}^na_iX^i$ (avec $a_n \neq 0$) un polynôme. On va montrer que pour tout $\mid X \mid > \max( 1, \frac{\sum_{i=0}^{n-1}\mid a_i\mid}{\mid a_n\mid})$, on a $\mid P(X)\mid > 0$.

Toutes les racine du polynôme seront donc plus petites que $\frac{\sum_{i=0}^{n-1}\mid a_i\mid}{\mid a_n\mid}$ et on pourra stopper l'algorithme d'énumération au bout d'un nombre fini d'itérations.

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

En revanche le problème suivant qui en est une généralisation n'est pas décidable, bien qu'il reste reconnaissable :

* **nom** : racine polynôme plusieurs variables
* **entrées** : $P(X)$ un [polynôme à plusieurs variables](https://fr.wikipedia.org/wiki/Polyn%C3%B4me_en_plusieurs_ind%C3%A9termin%C3%A9es) à coefficients dans $\mathbb{Z}$
* **question** : $P(X)$ Possède-t-il une [racine](https://fr.wikipedia.org/wiki/Racine_d%27un_polyn%C3%B4me) dans $\mathbb{N}$ (un entier $a$ tel que $P(a) = 0$) ?

{% note %}
*"Racine polynôme plusieurs variables"* est un problème **reconnaissable** mais **indécidable**.
{% endnote %}
{% details "éléments de preuve" %}
Cela a été [démontré en 1970 par Matiiassevitch](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Matiiassevitch) en prouvant que l'on ne pouvait pas borner les racines d'un polynôme à plusieurs variables.

Il n'existe donc pas d'algorithme qui s'arrête au bout d'un temps fini si un polynôme à plusieurs variables n'a pas de racine dans $\mathbb{N}$.

{% enddetails %}

**Félicitations !** Vous venez de rencontrer votre premier problème que ne pourra pas résoudre un ordinateur.

{% info %}
Ce cas est historiquement important car il correspond au [dixième problème de Hilbert](https://fr.wikipedia.org/wiki/Dixi%C3%A8me_probl%C3%A8me_de_Hilbert).
{% endinfo %}

