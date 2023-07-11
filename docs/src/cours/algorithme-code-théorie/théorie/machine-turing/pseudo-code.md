---
layout: layout/post.njk 
title:  "Équivalence entre pseudo-code et machine de Turing"

eleventyNavigation:
    order: 3
    prerequis:
        - "../../../algorithme/définition/"
        - "../../../algorithme/pseudo-code/"


eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le [pseudo-code]("../../../algorithme/pseudo-code/") est une façon d'écrire des algorithmes, nous allons voir dans cette partie qu'un pseudo-code est équivalent à une machine de Turing et qu'on (les informaticiens) est même persuadé que c'est aussi équivalent à la notion même d'algorithme.

> 
> TBD
>
> 1. exemple de chose Turing complète (du bizarre avec la rule ?)
> 2. Thèse de Turing church
> 3. conclusion : pseudo-code ok car équivalent à machine de Turing.

## Pseudo-code minimal

Nous allons donner ici une version expurgé de la notion d'algorithme et de pseudo-code. Cette version, plus compliquée à écrire mas pas plus puissante sera plus facile à mettre en correspondance avec les machines de Turing.

Nous allons démontrer dans cette partie le théorème suivant :

{% note "**théorème**" %}

[Pseudo-code]("../../../algorithme/pseudo-code/") et [machine de Turing](../définition) sont deux notions équivalentes.

{% endnote %}

### Objets et opérations d'un algorithme

On a vu qu'un [algorithme](../../../algorithme/définition/){.interne} pouvait ne manipuler que des entiers.

Sous sa représentation binaire, un entier étant un tableau de bit, on en conclut :

{% note %}
Les seuls objets qu'un **algorithme** peut utiliser sont les tableaux de bits.
{% endnote %}

De plus, toutes les opérations arithmétiques sur les nombres binaires peuvent se déduire de l'addition et l'addition peut s'écrire en utilisant uniquement l'opération [NON-ET](https://fr.wikipedia.org/wiki/Fonction_NON-ET).

{% lien %}
Sur comment faire, voir par exemple <https://www.circuits-logiques.polymtl.ca/help/Chapitre05.pdf>
{% endlien %}

De là :

{% note %}
La seule opération qu'un **algorithme** peut utiliser est l'opération [NON-ET](https://fr.wikipedia.org/wiki/Fonction_NON-ET)
{% endnote %}

On peut donc se restreindre aux pseudo-codes pouvant manipuler des bits avec l'opération booléenne NON-ET.

### Structures de contrôles

Un algorithme dans toute sa généralité n'a pas de définition précise d'une structure de contrôle, mais un [pseudo-code](../../../algorithme/pseudo-code/){.interne}, oui. Il possède :

* une instruction conditionnelle : SI condition ALORS bloc
* une répétition conditionnelle : TANT QUE condition EXÉCUTE bloc

Une condition devant être vraie (1) ou fausse (0), on peut se restreindre à :

{% note %}
Les seules structures de contrôle nécessaires pour un **pseudo-code** sont :

* SI v == 0 ALORS  bloc
* TANT QUE v == 0 EXÉCUTER bloc

{% endnote %}

## Turing et pseudo-code minimal

Il est clair que la machine de Turing possède les propriétés nécessaire pour un pseudo code :

* le ruban nous permet d'avoir des tableaux de bits
* les condition `SI r == 0 ALORS  machine` a été définie dans la partie [composition de machines](../définition/#composition-machine){.interne}. Une machine étant pouvant être considéré comme un bloc d'instructions.
* l'opération NON-ET peut être est trivialement construite sous la forme d'une fonction de transition

Pour gérer les variables, l'équivalence des machines de Turing nous permet d'utiliser une machine à plusieurs rubans, dont 1 est consacré au stockage des variables. Ceci nous permet de définir les opérations :

* SI v == 0 ALORS  bloc
* TANT QUE v == 0 EXÉCUTER bloc

Et donc on en conclut :

{% note "**Proposition**" %}
Tout ce qui peut s'écrire avec un pseudo-code peut s'écrire avec une machine d Turing.
{% endnote %}

## Pseudo-code et Turing <span id="mtu"></span>

Il nous reste à montrer l'autre implication : tout ce qui peut s'écrire avec une machine de Turing peut s'écrire avec du pseudo-code.

La preuve de cette implication est magnifique (on la doit à Turing lui-même) car elle montre qu'un ordinateur - dont le but est d'exécuter des programmes donc des machines - est lui aussi une machine de Turing.

Ce qui différencie une machine de Turing d'une autre c'est la fonction de transition.

Un des résultats les plus surprenant de Turing est qu'en fait on ne peut construire qu'**une seule machine** qui simulera toutes les autres. Cette machine est appelée [Machine de Turing universelle](https://fr.wikipedia.org/wiki/Machine_de_Turing_universelle) et possède deux paramètres, le premier, $M$ représentant le programme d'une machine de Turing et le second $E$ une entrée.

Avant de construire effectivement une machine de Turing universelle, essayons de voir comment en encoder une sous la forme d'une ou plusieurs chaînes de 0 et de 1.

### Encodage d'une machine

Une machine de Turing, est définie par sa fonction de transition. Il nous faut donc un moyen d'encoder les 3 fonctions constituant la fonction de transition :

* $\delta_e: Q \times \\{1, 0\\} \mapsto Q$
* $\delta_c: Q \times \\{1, 0\\} \mapsto \\{1, 0\\}$
* $\delta_d: Q \times \\{1, 0\\} \mapsto \\{\leftarrow, \rightarrow\\}$

Par des suites de `0` et de `1`.

On peut pour cela considérer des bijections :

* $\phi_q: Q \mapsto [\\![ 0, |Q|-1]\\!]$ telle que :
  * $\phi_q(\text{START}) = 0$
  * $\phi_q(\text{STOP}) = 1$
* $\phi_d: \\{\leftarrow, \rightarrow\\} \mapsto \\{0, 1\\}$ telle que :
  * $\phi_d(\leftarrow) = 0$
  * $\phi_d(\rightarrow) = 1$

Encoder une transition par un quintuplet :

$$
T(q, r) = (\phi_q(q), r, \phi_q(\delta_e(q, r)), \delta_c(q, r), \phi_d(\delta_d(q, r)))
$$

Et finalement associer à la fonction de transition le tableau constitué de la concaténation :

$$
T = T(q_1, 0) + CT(q_1, 1) + \dots + CT(q_i, 0) + CT(q_i, 1) + \dots + CT(q_{|Q|}, 0) + CT(q_{|Q|}, 1)
$$

On a alors les correspondances :

* $\delta_e(q, r) = T[5 \cdot (k + r) + 2]$
* $\delta_c(q, r) = T[5 \cdot (k + r) + 3]$
* $\delta_d(q, r) = T[5 \cdot (k + r) + 4]$

Avec $k$ le plus petit indice tel que $T[5\cdot k] = \phi_q(q)$

### MTU

#### Principe

Le pseudo-code ci-après décrit le principe d'une machine de Turing universelle.

```
Nom : MTU
Entrée : 
    T : une fonction de transition sous la forme d'un tableau
Programme :
    Soit R un ruban initialement vide et un curseur c qui pointe sur une de ses cases.
    q = 0

    Tant que q ≠ 1:
      Soit r la valeur de la case du ruban pointée par c    
      Trouver le plus petit k tel que T[5k] = q

      écrire T[5(k+r) + 3] sur R
      déplacer le curseur à droite si T[5(k+r) + 4] == 1 et vers la gauche sinon
      q = T[5(k+r) + 2]

    Rendre R
```

On voit que la MTU va simulée toute machine de Turing encodée par T.

#### Création effective

Pour terminer la preuve, il nous reste à montrer que le pseudo-code précédent et T peuvent être converti en une machine de Turing et son entrée.

Ceci est plus facile qu'attendu car :

* on peut simuler une [machines de Turing `01#`](../définitions-alternatives/#MT-01#) par une machine de Turing.
* on peut simuler tout pseudo-code par une machine de Turing

Commençons par transformer $T$ en une entrée composée des caractères `0`, `1` et `#` :

* on sépare chaque élément par des `#`
* le seul élément qui n'est pas un `0` ou un `1` est l'état qui est un entier. On peut le représenter par sa représentation unaire. Pour représenter $0 \leq q < |Q| on a :
  * $q$ caractères `1`
  * suivis de $|Q| - 1 - q$ caractères `0`

> TBD : un exemple

Cette transformation est l'entrée $E$ de notre MTU.

Puis nous allons simuler la MTU par une machine de Turing `01#`. Faisons simple et séparons les variables en autant de ruban :

* un ruban pour stocker l'état courant `q` : On supposera que le curseur est toujours placé au début de l'état. On initialisera ce ruban en recopiant le premier élément de l'entrée $E$
* cinq rubans permettant de stocker la transition :
  * un ruban contenant les éléments $E[5\cdot k]$ séparé par des `#`
  * un ruban contenant les éléments $E[5\cdot k + 1]$ séparé par des `#`
  * un ruban contenant les éléments $E[5\cdot k + 2]$ séparé par des `#`
  * un ruban contenant les éléments $E[5\cdot k + 3]$ séparé par des `#`
  * un ruban contenant les éléments $E[5\cdot k + 4]$ séparé par des `#`
* un ruban contenant le ruban de la machine simulée
* un dernier ruban pour les opérations internes de la MTU

Enfin, il faut adapter le pseudo-code de la MTU à notre machine. Ceci est aisé puisque l'on peut bouger les curseur de façon indépendante avec une machine de Turing `01#`.

1. Initialisation : Tous les curseurs se trouvent sur la case la plus à gauche contenant les entrées (s'il y en a), c'est à dire une case contenant un `0` ou un `1` et dont les deux cases précédentes contiennent un `#`.
2. 

> TBD : uniquement faire trouver la bonne transition
> TBD : égalité de tableau de bit pour `01#`
> en faire une simple

### Conclusion

Nous venons de faire un ordinateur dans une machine de Turing !

* les registres : état
* l'unité arithmétique : le ruban interne
* le code : la représentation de la transition.
* la mémoire : le ruban de la machine à simuler
Nous utiliserons dans cette partie des , ce qui permet d'écrire les choses plus simplement sans perte de généralité.

def MT(E)

#### Entrée

En utilisant un alphabet à trois lettres `01#`, la transition $T(q, r)$ peut être encodée par la chaîne :

$$
CT(q, r) = \phi_q(q)\sharp r\sharp \phi_q(\delta_e(q, r))\sharp \delta_c(q, r)\sharp \phi_d(\delta_d(q, r))
$$

Et la fonction de transition globale en concaténant toutes les transitions :

$$
CT(q_1, 0)\sharp CT(q_1, 1)\sharp \dots \sharp CT(q_i, 0) \sharp CT(q_i, 1)\sharp \dots CT(q_{|Q|}, 0)\sharp CT(q_{|Q|}, 1)
$$

La transition $\delta(q, r)$
une fonction de transition est la concaténation de toutes les transitions écrites :

#### Machine

Si on peut simuler une machine de Turing, on peut simuler une MTU et donc faire tout ce que fait une machine de Turing !

> TBD Turing complete. 

, on peut faire tout ce que fait une machine de Turing, puique l'on peut construire 

> TBD : rule 110

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

### Implications

> encoder = compiler
> il n'y a pas de différence entre un texte et le programme
> il suffit d'une machine pour lier toutes les autres machines.

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


## Conclusion
