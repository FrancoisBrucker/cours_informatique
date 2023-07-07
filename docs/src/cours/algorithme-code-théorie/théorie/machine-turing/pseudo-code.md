---
layout: layout/post.njk 
title:  "Turing et pseudo-code"

eleventyNavigation:
    order: 2
    prerequis:
        - "../../../algorithme/pseudo-code/"


eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le [pseudo-code]("../../../algorithme/pseudo-code/") est une façon d'écrire des algorithmes, nous allons voir dans cette partie qu'un pseudo-code est équivalent à une machine de Turing et qu'on (les informaticiens) est même persuadé que c'est aussi équivalent à la notion même d'algorithme.

1. Turing peut faire tout ce que fait le pseudo code
2. et réciproquement grace à la machine de Turing universelle
3. exemple de chose Turing complète (du bizarre avec la rule ?)
4. Thèse de Turing church
5. conclusion : pseudo-code ok car équivalent à machine de Turing.

## Turing et pseudo-code

On a défini un [pseudo-code]("../../../algorithme/pseudo-code/") comme pouvant :

* utiliser 6 types d'objets (entiers, réels, complexes, booléen, caractères, vide) en utilisant les opérations arithmétiques usuelles sur ceux-ci
* stocker un objet dans une variable ou un tableau
* faire une exécution conditionnelle (si condition alors exécute un bloc)
* répéter un bloc d'instructions tant qu'un condition est vraie

### Pseudo-code minimal

On peut diminuer les exigences de propriétés d'un pseudo-code sans perdre en généralité. On descendra juste assez pour montrer que l'on faire tout ça facilement tout ça avec une machine de Turing

{% info %}
Il existe plusieurs simplifications possibles. Une autre possibilité serait de se focaliser sur les instruction conditionnelles de blocs, comme par exemple [ici](https://en.wikipedia.org/wiki/Structured_program_theorem).
{% endinfo %}

#### objets

> TBD : écrire mieux

* réels n'existent pas en informatique (ils peuvent avoir une longueur infinie) : approximation finie, donc réels = entiers
* complexe = tableau d'entiers
* entiers = tableaux de bits
* caractères = entier
* booléen = 1 bit
* uniquement test pour vide/pas vide = booléen

On peut donc toujours représenter un objet par un tableau de bits.

De plus, toutes les opérations arithmétiques sur les nombres binaires peuvent se déduire de l'addition et l'addition peut s'écrire en utilisant uniquement l'opération [NON-ET](https://fr.wikipedia.org/wiki/Fonction_NON-ET).

{% lien %}
Sur comment faire, voir par exemple <https://www.circuits-logiques.polymtl.ca/help/Chapitre05.pdf>
{% endlien %}

On peut donc se restreindre aux pseudo-codes pouvant manipuler des bits avec l'opération booléenne NON-ET.

#### Variables et tableaux

Une variable n'étant qu'un tableau de longueur 1, on peut se restreindre aux pseudo-codes manipulant des variables tableaux (de bits).

(même si ce sera plus compliqué d'écrire le code) à trois types d'instructions et à trois façon de les exécuter :

#### Structures de contrôles

Un pseudo-code doit avoir 2 structures :

* une instruction conditionnelle
* une répétition conditionnelle

Une condition devant être vraie (1) ou fausse (0), on peut se restreindre :

* SI v == 0 ALORS bloc
* Tant que v == 0 EXÉCUTER bloc

### Turing et pseudo-code minimal

L'[équivalence de différents modèles de machine de Turing](../définitions/#équivalences) nous permet d'utiliser la définition suivante d'une machine de Turing :

* Alphabet $\\{0, 1, #\\}$
* un ruban pour les données, on sépare les tableaux de bits par un `#`
* un ruban pour le reste

Ceci nous permet d'avoir :

* nos objets bit
* la notions de variables tableaux

Comme il est facile d'implémenter avec une fonction de transition :

* l'opération NON-ET
* l'instuction conditionnelle
* le tant que

On en conclut :

{% note "**Proposition**" %}
Tout ce qui peut s'écrire avec un pseudo-code peut s'écrire avec une machine d Turing
{% endnote %}

## Pseudo-code et Turing

Il nous reste à montrer l'autre implication : tout ce qui peut s'écrire avec une machine de Turing peut s'écrire avec du pseudo-code pour conclure cette partie.

La preuve de cette implication est magnifique (on la dot à Turing lui-même) car elle montre qu'un ordinateur dont le but est d'exécuter des programme est lui aussi une machine de Turing.

### <span id="mtu"></span>Machine de Turing universelle

Ce qui différencie une machine de Turing d'une autre c'est l'alphabet et la fonction de transition. On a vu qu'on pouvait utiliser un alphabet commun ($\\{ \sharp, 0, 1\\}$), les différences entre machines sont donc uniquement dues à la fonction de transition.

Un des résultats les plus surprenant de Turing est qu'en fait on ne peut construire qu'**une seule machine** qui simulera toutes les autres. Cette machine est appelée [Machine de Turing universelle](https://fr.wikipedia.org/wiki/Machine_de_Turing_universelle) et possède deux paramètres, le premier, $M$ représentant le programme d'une machine de Turing et le second $E$ une entrée.

{% note %}
Il existe une machine de Turing $U$ à 2 rubans sur l'alphabet d'entrée $\\{ 0, 1\\}$ (et $\\{\sharp, 0, 1\\}$ comme alphabet de travail) telle que pour une machine de Turing $M$ et une entrée $\mu$ donnée, $U(M, \mu)$ calculera ce que calcule $M$ pour l'entrée $\mu$ :

* elle accepte $\mu$ si $M$ l'accepte et sa sortie est celle de $M$ pour l'entrée $\mu$.
* elle ne s'arrête pas si l'exécution de $M$ avec $\mu$ comme entrée ne s'arrête pas,

{% endnote %}

Nous ne démontrerons pas ce résultat que l'on doit à Turing lui-même, contentons nous de voir comment on peut encoder une Machine de Turing $M$ sur l'alphabet $\\{ 0, 1\\}$ pour en faire un paramètre d'entrée possible d'une machine de Turing.

Il y a bien des façons de faire. Nous prendrons ici celle utilisée dans la partie 3.3.4 de [ce document](http://pageperso.lif.univ-mrs.fr/~kevin.perrot/documents/2016/calculabilite/Cours_16.pdf). L'idée est de pouvoir :

* encoder chaque transition
* avoir des séparateurs nous permettant de délimiter chaque transition

Soit $M$ une machine de Turing à $n$ états (de $q_0$ à $q_{n-1}$) et $m$ caractères (de $c_1$ à $c_m$). Une transition est alors $\delta(q_i, c_j) = (q_k, c_l, D)$  où $D$ est soit $\leftarrow$ soit $\rightarrow$.

On code :

* $q_i$ par $\underbrace{0 \cdots 0}_{i}{}$
* $c_j$ par $\underbrace{0 \cdots 0}_{j}{}$,
* $\leftarrow$ par $0$,
* $\leftarrow$ par $00$
* le séparateur par $1$

La transition $\delta(q_i, c_j) = (q_k, c_l, \leftarrow)$ est alors :

<div>
$$
{
\underbrace{0 \cdots 0}_{i}{1} \underbrace{0 \cdots 0}_{j}{1} \underbrace{0 \cdots 0}_{k}{1} \underbrace{0 \cdots 0}_{l}{1} \underbrace{0}_{\leftarrow}
}
$$
</div>

On sépare ensuite toutes les transitions par $11$ :

$$
\cdots11\mbox{transition}11\cdots
$$

Il nous reste à renseigner le nombre d'états et de caractères en début de code et de donner un début et une fin à ce code ($111$) pour finaliser notre encodage $\langle M \rangle$ de la machine de Turing $M$ :

<div>
$$
\langle M \rangle = 111\underbrace{0 \cdots 0}_{n}11\underbrace{0 \cdots 0}_{m}11\mbox{transition}_111\cdots11 \mbox{transition}_i11\cdots11\mbox{transition}_N111
$$
</div>

**Félicitations !** : vous venez de créer votre 1er ordinateur !

> TBD : une machine de Turing pour les lier toutes au sein ...
>

{% note %}
La machine de Turing universelle $U$ permet d'exécuter n'importe quelle machine $M$ : c'est un ordinateur dont le langage machine est l'encodage $\langle M \rangle$.
{% endnote %}

C'est un résultat extrêmement puissant. On a besoin que d'une machine de Turing pour exécuter toutes les machines de Turing.

Attention cependant, On a l'impression qu'on a besoin de rien, que toutes les machines de Turing sont en faite une seule. Ce n'est pas exactement le cas car l'encodage cache la machine. C'est un petit peu comme dans la blague ci-dessous. Un numéro n'est drôle que parce qu'il code une blague !

```text
Une famille qui connaît toutes les blagues de la planète 
les a classées et numérotées. Ainsi, le seul numéro suffit 
à les faire rire.

Lors d' un repas le père s'exclame : "12" !
Tout le monde pouffe de rire.
La mère dit : "32" !
Et ils éclatent de rire.
Le petit sort alors : "104" !
Et personne ne rit.
Son frère lui dit alors : " Tu la racontes mal !"
```

Grâce à la machine de Turing universelle, démontrer qu'un langage est [Turing complet](https://fr.wikipedia.org/wiki/Turing-complet) c'est à dire qu'il permet de calculer tout ce qu'une machine de Turing peut calculer revient à montrer qu'on peut simuler une machine de Turing. C'est comme ça par exemple qu'on a démontrer que la [règle 110](https://en.wikipedia.org/wiki/Rule_110) est un ordinateur.

## Church-Turing

Un pseudo-code est a priori un cas particulier d'algorithme puisque l'on se limite à un nombre fixé d'instructions et à une construction rigide et normée de ceux ci (uniquement des blocs avec une instruction par ligne). Mais toutes les tentatives de généralisation ont échoués : elle n'ont jamais permis de faire des algorithmes impossible à réaliser en pseudo-code.

On pense donc (mais ce n'est pas démontré) que :

{% note "**Thèse de Church-Turing**" %}
Les notions d'algorithme et de pseudo-code sont équivalentes.

Tout algorithme peut être écrit en pseudo-code.
{% endnote %}

En bon informaticien, on considérera la thèse de Church-Turing vérifiée et :

* on écrira tous nos algorithmes en pseudo-code
* pseudo-code et algorithme seront considérés comme synonyme

{% note %}
Si ces considérations vous intéressent, n'hésitez pas à jeter un coup d'œil à ce lien :
<https://plato.stanford.edu/entries/turing-machine/#ThesDefiAxioTheo>

C'est en Anglais, mais c'est très bien.
{% endnote %}

