---
layout: layout/post.njk
title: "Problèmes NP"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les classes de problèmes et leurs significations donnent toujours des problèmes aux étudiants. Ils ne sont certes pas aidés par la terminologie qui, lorsqu'elle n'est pas cryptique, peut induire en erreur. Nous allons tenter d'être le plus clair possible en n'introduisant que ce qu'il est nécessaire de jargon pour comprendre l'enjeu de cette classification.

En algorithmie théorique on ne peux pas utiliser la thèse de Church-Turing puisqu'elle n'est pas démontrée, ici on considérera que les algorithmes sont écrit en pseudo-code.

## Problèmes utilisables en pratique

Un [problème algorithmique](../probleme-algorithmique/){.interne} implique qu'il existe un algorithme pour le résoudre On appelle ces problèmes calculables ou **_décidable_**. Comme on sait qu'il existe des problèmes non solvable par un algorithme (on a vu [la complexité de Kolmogorov](../bases-théoriques/calculabilité/#complexité-Kolmogorov){.interne} par exemple), on peut commencer par se restreindre aux problèmes décidables :

![décidable](./NP-décidable.png)

Mais parmi ces derniers, pour être utile en pratique, encore faut-il que l'on puisse les traiter en temps raisonnable (la durée d'une vie humaine par exemple). On va donner deux définitions du terme _traiter_. Commençons par la plus évidente : **la résolution**.

### Résolution efficace

{% note "**Définition**" %}
Un problème algorithmique est dit **_polynomial_** s'il existe un pseudo-code de complexité polynomiale en la taille de son entrée permettant de le résoudre.

L'ensemble des problèmes polynomiaux est nommé $P$.
{% endnote %}

On a vu un certains nombre de problèmes polynomiaux, on peut par exemple citer :

- Trouver le maximum d'un tableau d'entiers dont [on a démontré que sa complexité était linéaire](../complexité-problème/#recherche){.interne},
- Trier un tableau d'entiers dont [on a démontré que sa complexité était $\mathcal{O}(n\ln(n))$](../problème-tris/complexité-problème){.interne} où $n$ est la taille du tableau,

![décidable](./NP-P.png)

Le cas du [problème de l'exponentiation](../projet-exponentiation/étude-algorithmique){.interne} est intéressant car on a démontré qu'il était en $\mathcal{O}(\ln(n))$ où $n$ est la valeur de l'exposant. Il n'est donc pas évident au premier coup d'œil que cela est bien polynomial en la taille des entrées, c'est à dire 2 entiers.

En informatique théorique l'unité d'information est le bit, la taille de l'entrée d'un algorithme est toujours égale au nombre de bits nécessaires pour la stocker. Pour un entier il s'agit donc du logarithme en base 2 de sa valeur et donc le problème de l'exponentiation est bien polynomiale, il est même linéaire en la taille de l'entrée...

{% info %}
Si pour être rigoureux et formel il est nécessaire de considérer qu'une case mémoire ne peut contenir qu'un seul bit plutôt qu'un entier quelconque, cela alourdit les calculs de complexité sans réel apport.
En effet l'entier étant la donnée élémentaire, toute opération qui en manipule (c'est à dire presque toutes les opérations) devra lire chaque bits les constituant, ce qui ne fait qu'ajouter un facteur linéaire en la taille des données.

Enfin, les entiers sont usuellement bornés, sur 64bits pour un processeur courant, ce qui permet d'avoir assez d'entiers pour ne pas être limité en pratique et de bien avoir une taille en $\mathcal{O}(1)$ (64 étant une constante).
{% endinfo %}

### Vérification efficace

Il existe de nombreux problèmes dont on ne connaît pas d'algorithme polynomiaux pour les résoudre mais la complexité, ou dont on ne connaît pas d'algorithmes polynomiaux pour les résoudre, mais dont dont sait facilement, grace à un algorithme efficace de vérification nommé **_vérifieur_**, voir si proposition de solution en est une ou pas.

<div id="définition-vérifieur"></div>

{% note "**Définition**" %}
Un **_vérifieur_** est un algorithme de :

$$v: \\{0, 1\\}^\star \times \\{0, 1\\}^\star \rightarrow \\{0, 1\\}$$

Il est dit **_efficace_** s'il est de complexité polynomiale.
{% endnote %}

Cette notion de vérification est cruciale. Si on ne sait pas construire de solutions nous même mais que quelqu'un arrive avec une solution potentielle, il faut pouvoir vérifier qu'elle est correcte avant de l'utiliser. Sans cette condition le problème n'a pas de solution réaliste : toute valeur peut être solution puisqu'on ne peut pas savoir avant d'essayer.

On peut voir le vérifieur comme une preuve (il y a équivalence entre preuve mathématique et algorithme, rappelons-le) automatisée et efficace (polynomiale, donc pouvant être écrite puis lue par des humains) de l'exactitude d'une solution.

Formalisons cette notion de vérification efficace :

{% note "**Définition**" %}
Un **_vérifieur efficace d'un problème décidable_** $p$ ayant pour entrée $e \in E$ et pour sortie $s \in S$ est un algorithme $V: E \times S \rightarrow \\{0, 1\\}$ tel que :

- $V(e, s)$ vaut 1 si et seulement si $s$ est une sortie de $p(e)$
- la complexité de $V$ est **polynomiale** en la taille de $e$ et ne **dépend pas** de la taille de $s$.

{% endnote %}
{% info %}
Le retour d'un vérifieur est classiquement un bit mais pas la suite, pour être plus explicite, nous utiliserons des booléens en associant 0 à faux et 1 à vrai.
{% endinfo %}

Remarquez que l'on ne demande **pas** que sa complexité soit polynomiale par rapport à la sortie ! Seule, l'entrée compte.

Cependant, comme la complexité doit être polynomiale dans la taille de l'entrée cela implique que la taille de la sortie est polynomiale par rapport à la taille de l'entrée : si l'algorithme est de complexité $\mathcal{O}(|e|^k)$ alors seule $\mathcal{O}(|e|^k)$ bits de $s$ peuvent être examinés, cela ne sert à rien d'avoir des sorties plus longues.

Enfin, cette définition est réaliste puisque si l'on possède une solution on veut pouvoir vérifier de façon réaliste (_ie._ polynomialement) que c'est une solution : si sa taille est exponentielle, on ne peut même pas la lire en temps raisonnable !

Tout algorithme de $P$ admet un vérifieur efficace puisqu'il suffit d'exécuter l'algorithme de résolution et de vérifier si sa solution est égale à l'entrée.

Ainsi, pour [le problème MAX (trouver le maximum d'un tableau)](../#problème-MAX){.interne} :

```pseudocode
algorithme vérification_max(T: [entier], sol: entier) → booléen:
  m ← max(T)  # algorithme linaire trouvant le maximum d'un tableau
  rendre m == sol
```

Dans le cas d'algorithme de résolution linéaire (comme pour le problème de la recherche du maximum), cette approche est optimale. Mais pour des problèmes dont l'algorithme de résolution est non linéaire on peut souvent trouver un algorithme de vérification de complexité plus faible.

{% exercice %}
Montrez que le problème [3-SUM'](../problème-réduction/#problème-3-SUM'){.interne} admet un vérifieur linéaire.
{% endexercice %}
{% details "solution" %}

```pseudocode
algorithme vérification_3_SUMprim(T: [entier], sol: (entier, entier, entier)) → booléen:
  i, j, k ← sol
  si T[i] + T[j] == T[k]:
      rendre Vrai
  rendre Faux
```

{% enddetails %}

### Vérifieur efficace et algorithme de résolution

Les problème admettant un vérifieur ne sont pas forcément décidables. Considérons par exemple le vérifieur `stop(E: chaîne, n: entier) → booléen`{.language-} qui rend vrai si le programme décrit par la chaîne de caractères `E`{.language-} s'arrête au bout de `n`{.language-} itération. Ce vérifieur correspond [au problème de l'arrêt](../bases-théoriques/arrêt-rice/){.interne} qui est indécidable.

Le fait que le problème admette un vérifieur dont la complexité ne dépend que du premier paramètre est donc cruciale. Si de plus sa complexité est polynomiale on a de plus :

{% note "**Proposition**" %}
Si un problème admet un **_vérifieur efficace_** de complexité $\mathcal{O}(|e|^k)$, alors il est décidable et sa complexité est en $\mathcal{O}(|e|^k\cdot 2^{|e|^k})$ opérations.

{% endnote %}
{% details "preuve", "open" %}

Tout problème admettant un vérifieur efficace est décidable car il n'y a qu'un nombre fini de l'ordre de $\mathcal{O}(2^{|e|^k})$ . En effet, si le vérifieur est un pseudo-code de complexité $\mathcal{O}(|e|^k)$ (avec $k$ une constante), la taille de la solution est bornée par $\mathcal{O}(|e|^k)$ et donc sa valeur par $\mathcal{O}(2^{|e|^k})$.

On peut alors pour une entrée donnée tester toutes les solutions possibles ce qui va coûter de l'ordre de $\mathcal{O}(|e|^k\cdot 2^{|e|^k})$ opérations (puisque tester une entrée coûte $\mathcal{O}(|e|^k)$ opérations), ce qui est certes beaucoup mais reste fini.

{% enddetails %}

### La classe de Problèmes NP

Les problèmes utiles qui s'appellent en algorithmie les problèmes NP :

{% note "**Définition**" %}
**_Un problème algorithmique est dit_** $NP$ s'il existe un vérifieur efficace de ses solutions.
{% endnote %}

Ce qui donne le schéma suivant :

![décidable](./NP-NP-1.png)

La définition ci-dessus appelle deux remarques :

- premièrement le nom a été très mal choisi. Il signifie _Non Déterministe Polynomial_ (et **_pas du tout_** non polynomial...) car cette classe de problème  peut être résoluble de façon polynomiale par des algorithmes non déterministes (un test si peut avoir plusieurs alors choisi de façon non déterministe). Dans ce cadre la définition fait sens puisqu'elle est identique à $P$ pour un autre type d'algorithme. Nous verrons ces types d'algorithmes plus tard.
- deuxièmement l'inclusion est stricte. Il existe des problèmes décidables qui ne sont pas dans NP. Ça aussi on le démontrera plus tard lorsque l'on étudiera .

{% attention "**À retenir**" %}
Un problème est dans $NP$ s'il existe un vérifieur efficace de ses solutions. Ce sont exactement les problèmes algorithmiques utilisable en pratique car :

- On peut énumérer toutes les solutions possibles en temps fini, mais en temps exponentiel (ce qui fonctionne lorsque la taille d'entrée est faible).
- On peut vérifier efficacement (en temps polynomial) si une proposition de solution est réellement une solution.

{% endattention %}

## Structure de NP

Regardons la structure de NP d'un peu plus prêt en utilisant notre comparateur de problèmes : [la réduction polynomiale](../problème-réduction/#définition-réduction-polynomiale){.interne}.

De façon extrêmement surprenante lorsqu'on y pense, il existe un problème de $NP$, SAT, qui majore tous les autres problèmes. Nous démontrerons ceci précisément plus tard, admettons donc (pour l'instant) le théorème suivant :

{% note "**Théorème ([Cook & Levin en 1971](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Cook))**" %}

Pour tout problème $A$ de $NP$ il existe une **réduction polynomiale** de $A$ vers le problème SAT.

{% endnote %}

C'est en effet surprenant qu'il n'y ait pas plusieurs élément maximaux de l'ordre induit par la réduction polynomiale.

### <span id="SAT"></span>Le problème SAT

Le problème SAT cherche à vérifier si une formule logique peut-être satisfaite.

Pour cela, commençons par définir un concept fondamental en logique la **_conjonction de clauses_** :

<div id="définition-clauses"></div>

{% note "**Définition**" %}
Soient $x_1, \dots, x_n$, $n$ variables booléennes. On définit :

- un **_littéral_** $l$ comme étant soit une variable $l = x_i$, soit sa négation $l = \overline{x_i}$
- une **_clause_** comme étant une disjonction de littéraux $c = l_1 \lor \dots \lor l_k$ (avec $l_1, \dots l_k$ littéraux)
- une **_conjonction de clauses_** comme étant $c = c_1 \land \dots \land c_m$ (avec $c_1, \dots c_m$ des clauses)
{% endnote %}

Le problème `SAT` cherche à savoir s'il existe des valeurs pour lesquelles $f$ est vraie. Si telle est le cas, la conjonction de clause est dite **_satisfiable_** :

{% note "**Problème**" %}

- **Nom** : SAT
- **Entrée** : $f$ une conjonction de clauses sur les variables $x_1$ à $x_n$
- **Sortie** : Une assignation des variables $x_1$ à $x_n$ telle que $f$ soit vraie (ou `∅`{.language-} si cela n'est pas possible).

{% endnote %}
{% info %}
Une formule logique sous la forme d'une disjonction de clause est dite sous la [forme normale conjonctive](https://fr.wikipedia.org/wiki/Forme_normale_conjonctive). Toute formule logique peut être mise sous cette forme grâce à [la transformation de Tseitin](https://fr.wikipedia.org/wiki/Transformation_de_Tseitin) qui est linéaire en nombre d'opérations. Ceci exige de se retrouver avec un nombre exponentiel de clauses si on utilise juste [la distributivité des opérations logiques](https://fr.wikipedia.org/wiki/Forme_normale_conjonctive#Conversion_lin%C3%A9aire_%C3%A9quisatisfiable).

{% endinfo %}

<span id="exemple-SAT"></span>
Par exemple considérons les 4 clauses suivantes, sur 5 variables booléennes :

<div>
$$
(x_1 \lor {x_2}) \land (\overline{x_1} \lor \overline{x_2} \lor \overline{x_3}) \land (\overline{x_1} \lor x_3 \lor x_4 \lor \overline{x_5}) \land ({x_1} \lor \overline{x_3} \lor \overline{x_4} \lor {x_5})
$$
</div>

Il y $2^5 = 32$ possibilités (O ou 1 ; Vrai ou Faux) pour chaque variable. Essayons en quelques une :

- $x_1 = x_2 = x_3 = x_4 = x_5 = 0$ ne permet pas de satisfaire la formule car $x_1 \lor {x_2} = 0$
- $x_1 = x_2 = x_3 =x_4 = x_5 = 1$ non plus ($\overline{x_1} \lor \overline{x_2} \lor \overline{x_3} = 0$)
- $x_1 = \overline{x_2} = x_3 = \overline{x_4} = x_5 = 1$ fonctionne

La formule précédente est satisfiable !

Montrons que SAT admet un vérifieur efficace (il est même linéaire) :

{% exercice %}
Montrez que l'on peut encoder une clause sur $n$ variables booléennes par un tableau d'entiers relatifs.

En déduire un moyen d'encoder une conjonction de clauses sur $n$ variables booléennes.
{% endexercice %}
{% details "corrigé" %}
Il suffit de noter un littéral :

- $+i$ s'il correspond à $x_i$
- $-i$ s'il correspond à $\overline{x_i}$

Et d'encoder une clause comme un tableau de littéraux. Notez qu'on ne peut pas commencer à 0 car $+0 = -0 = 0$

Enfin, une conjonction de clauses est un tableau de clauses.

{% enddetails %}
{% exercice %}
Quel est l'encodage de l'exemple ? Comment encoderiez vous une solution ?
{% endexercice %}
{% details "corrigé" %}

```pseudocode
[[1, 2],
 [-1, -2, -3],
 [-1, 3, 4, -5],
 [1, -3, -4, 5]
]
```

Et la solution est un tableau de taille $n$ de booléens. Par exemple pour la solution $x_1 = \overline{x_2} = x_3 = \overline{x_4} = x_5 = 1$ on a l'encodage : `[Vrai, Faux, Vrai, Faux, Vrai]`{.language-}
{% enddetails %}

{% exercice %}
Utilisez le codage précédent pour montrer que SAT admet un vérifieur linéaire.
{% endexercice %}
{% details "corrigé" %}

L'algorithme suivant est (clairement) un vérifieur de SAT utilisant l'encodage précédent :

```pseudocode
algorithme vérif_SAT(conj_clauses: [[entier]], # [c_1, ..., c_m]
                     solution: [booléen]) # [x_1, ..., x_n]
                     → booléen:
    pour chaque c de conj_clauses:
        sat ← Faux
        pour chaque l de c:
            si l > 0 et solution[l-1]:
                sat ← Vrai
            si l < 0 et (solution[-l-1] == Faux):
                sat ← Vrai
        si sat == Faux:
            rendre Faux
    rendre Vrai            
```

La complexité est clairement linéaire : on regarde au pire chaque littéral de chaque clause une fois.

{% enddetails %}

Même s'il est facile de vérifier si une solution potentielle est une solution, on ne connaît pas d'algorithme polynomial pour résoudre SAT. L'algorithme naïf consistant à tester toutes les solutions possibles prendrait $\mathcal{O}(mn\cdot 2^n)$ opérations ($2^n$ possibilités pour les variables et la taille d'une conjonction de clause est $nm$). Aussi surprenant que cela paraisse, on ne connaît pas d'algorithme fondamentalement meilleur :

{% attention "**À retenir**" %}
Il existe des problème facile à vérifier dont on ne connaît pas d'algorithme pour le résoudre.
{% endattention %}

### Réduction vers SAT

Le théorème de Cook et Leven stipule que **tout** problème de NP peut se réduire à un cas particulier du problème SAT. Pour démontrer cela ils montrent que tout problème algorithme de NP peut s'écrire polynomialement comme une formule SAT qui n'est satisfiable que pour des solutions du problème initial. 

Nous ne démontrerons pas ici ce théorème mais allons montrer quelques exemples pour que vous puissiez appréhender ce résultat fondamental.

#### MAX

Montrons que l'on peut le faire pour le problème MAX. Le but de cette réduction est de passer de la comparaison d'entiers à la comparaisons de variables booléennes. Nous allons faire ça en plusieurs étapes.

1. le test $(x_i = x_j)$ pour deux variables booléennes s'écrit $(x_i \land x_j) \lor (\overline{x_i} \land \overline{x_j})$
2. un entier $x$ peut s'écrire sous sa forme binaire $x^px^{p-1}\dots x^0$ où $x^i \in \\{0, 1\\}$ et $x = \sum_{0\leq i \leq p}x^i2^i$

Des deux remarques précédentes, on en déduit que le test $(x_i > x_j)$ pour deux entiers s'écrit par le fait qu'il existe $k$ tel que les k-1 derniers bits sont égaux et le $k$ème bit de x_i est plus grand que celui de x_j :

<div>
$$
\bigvee_{1\leq k \leq p}(\bigwedge_{k < l \leq p}(x_i^l = x_j^l)  \land (x_i^k \land \overline{x_j^k}))
$$
</div>

Et donc la formule logique :

<div>
$$
\bigvee_{1\leq k \leq p}(\bigwedge_{0 \leq l < k}((x_i^l \land x_j^l) \lor (\overline{x^l_i} \land \overline{x^l_j})) \land (x_i^k \land \overline{x_j^k}))
$$
</div>

Enfin, pour avoir $(x_i \geq x_j)$ on rajoute le fait que tous les bit de $x_i$ et $x_j$ peuvent être égaux :

<div>
$$
\bigvee_{1\leq k \leq p}(\bigwedge_{0 \leq l < k}((x_i^l \land x_j^l) \lor (\overline{x^l_i} \land \overline{x^l_j})) \land (x_i^k \land \overline{x_j^k})) \bigvee (\bigwedge_{0 \leq l \leq p}((x_i^l \land x_j^l) \lor (\overline{x^l_i} \land \overline{x^l_j})))
$$
</div>

De là la formule logique permettant de décrire un problème MAX est :

<div>
$$
\bigvee_{1\leq i \leq n}(\bigwedge_{j \neq i} T[i] \geq T[j])
$$
</div>

On utilise ensuite [la transformation de Tseitin](https://fr.wikipedia.org/wiki/Transformation_de_Tseitin) pour transformer cette formule logique en une conjonction de clauses ce qui montre que le problème MAX peut se résoudre via le problème SAT.

{% info %}
Dans tout ce qui suivra, on ne s'embêtera pas nécessairement à trouver la conjonction de clause qui sera l'entrée du problème SAT. On se contentera de formules logiques que l'on sait pouvoir transformer en conjonction de clauses.
{% endinfo %}

#### Plus

L'exemple précédent était éclairant mais pas forcément bluffant : le problème MAX pouvant se représenter facilement comme une succession de tests logiques. Nous allons donc aller un peu plus loin et transformer un algorithme, la somme de deux nombres binaires en une conjonction de clause.

Commençons par quelque chose de simple, l'addition de 2 bits :

```pseudocode
algorithme somme_binaire(x: bit, 
                         y: bit)
                         → [bit]  # somme = T[0] + 2 * T[1]
    somme ← [0, 0]
    si (x == 1) et (y == 1):
        rendre [0, 1]             # le nombre 10
    si (x == 1) ou (y == 1):
        rendre [1, 0]             # le nombre 01
    rendre [0, 0]                 # le nombre 00
```

{% attention %}
Pour simplifier l'écriture de la formule logique on a utilisé la notation mathématique qui stipule que le nombre représenté par un tableau binaire s'écrit $\sum_{0 \leq i < n} 2^i \cdot T[i]$ (les nombres sont écrits de droite à gauche, le tableau `[1, 1, 0]` correspond au nombre binaire `011`). C'est **l'opposée** de la notation classique en informatique qui lit les nombres de gauche à droite (le tableau `[1, 1, 0]` correspond bien au nombre binaire `110`) associant le nombre $\sum_{1 \leq i \leq n} 2^{i-1} \cdot T[-i]$ à un tableau de bis $T$.
{% endattention %}

Ce qui donne comme clause, en notant la sortie de l'algorithme $z = [z^0, z^1]$ :

<div>
$$
((x \land y) \land (z^1 \land z^0)) \lor ((x \lor y) \land (\overline{z^1} \land z^0)) \lor (\overline{z^1} \land \overline{z^0}))
$$
</div>

À vous maintenant. On considère l'algorithme suivant qui généralise l'addition sur 1 bit :

<span id="algorithme-somme_binaire"></span>

```pseudocode
algorithme somme_binaire(x: [bit], 
                         y: [bit])  # on suppose x et y de même taille
                         → [bit]  # de la taille de x et y + 1
    
    somme ← un tableau de taille x.longueur + 1 bits
    retenues ← un tableau de taille x.longueur + 1 bits
    retenues[0]  ← 0

    pour chaque i de [0 .. x.longueur - 1[:
        si (x[i] == 1) et (y[i] == 1) et (retenues[i] == 1):
            somme[i]  ← 1
            retenues[i + 1]  ← 1
        sinon si ((x[i] == 1) et (retenues[i] == 1)) ou ((y[i] == 1) et (retenues[i] == 1)) ou ((x[i] == 1) et (y[i] == 1)):
            somme[i]  ← 0
            retenues[i + 1]  ← 1
        sinon si (x[i] == 1) ou (y[i] == 1) ou (retenues[i] == 1):
            somme[i]  ← 1
            retenues[i + 1]  ← 0
        sinon:
            somme[i]  ← 0
            retenues[i + 1]  ← 0
    somme[-1] ← retenues[-1]
    rendre somme
```

{% exercice %}
Montrez que le résultat de l'addition des nombres `1011` et `0111` donne bien `10011`
{% endexercice %}
{% details "solution" %}

```text
  1011  = 11
+ 0111  =  7
------------
 10010  = 18
```

Pour l'algorithme on a comme entrée `x=[1,1,0,1]`{.language-} et `y=[1,1,1,0]`{.language-} et on doit avoir `[0,1,0,0,1]`{.language-} comme sortie.

> TBD : déroulement de l'algo avec les retenues.

{% enddetails %}
{% exercice %}
Écrivez l'algorithme sous la forme d'une formule logique.
{% endexercice %}
{% details "solution" %}

> TBD

{% enddetails %}

#### 3-SUM'

Terminons cette partie de réécriture en montrant que toutes ces clauses peuvent se combiner :
{% exercice %}
Montrer que le problème 3-SUM' peut être résolu par SAT
{% endexercice %}
{% details "solution" %}

<div>
$$
\bigvee_{0\leq i < n}(\bigwedge_{j\neq i}(T[i] \geq T[j]))
$$
</div>

{% enddetails %}

## Problèmes NP-Complet

Le théorème de Levin et Cook stipule que tout problème de NP peut se réduire polynomialement à un cas particulier de SAT : le problème SAT est un élément maximal de l'ordre entre problèmes de NP induit par la réduction polynomiale. Ce théorème montre l'existence de problèmes _universels_, on les appelle **_NP-complet_**, dont tous les autres problèmes ne sont que des cas particuliers :

{% note "**Définition**" %}
Un problème $A$ de NP est NP-complet si $B \leq A$ pour tout problème $B$ de NP.
{% endnote %}

Cette définition est consistante car deux problèmes différents de NP peuvent êtres tels que $A \leq B$ et $B \leq A$ (on l'a vu pour 3-SUM' et 3-SUM par exemple). Rien n'empêche donc d'avoir plusieurs problèmes se comportant comme SAT, La structure de NP est donc maintenant la suivante :

![décidable](./NP-NP-2a.png)

Fixons nous les idées en démontrant que le problème suivant est NP-complet.

### Couverture Exacte est NP-complet

<span id="problème-EC"></span><span id="problème-CE"></span>

{% note "**Problème**" %}

- **Nom** : Couverture Exacte (_exact cover_)
- **Entrée** :
  - un ensemble fini $U$ d'éléments
  - un ensemble $\mathcal{S}$ de sous-ensembles de $U$
- **Sortie** : Un ensemble $\mathcal{P} \subseteq \mathcal{S}$ formant une partition de $U$ (ou `∅`{.language-} si cela n'est pas possible).
{% endnote %}
{% info %}
Une partition $\mathcal{P}$ d'un ensemble $U$ est un ensemble de sous-ensembles de $U$ tel que :
- l'union des éléments de $\mathcal{P}$ vaut $U$,
- l'intersection de deux éléments différents de $\mathcal{P}$ est vide.
{% endinfo %}

Illustrons ce problème en reprenant [un exemple tiré de Wikipédia](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_la_couverture_exacte#Exemple_2) :

- $U = \\{1, 2, 3, 4, 5, 6, 7\\}$
- $\mathcal{S} = \\{ \\{1, 4, 7\\}, \\{1, 4\\}, \\{4, 5, 7\\},\\{3, 5, 6\\},\\{2, 3, 6, 7\\},\\{2, 7\\}  \\}$

Résoudre ce problème revient à faire plein de choix. Parfois ces choix sont simple : si on place $\\{1, 4, 7\\}$ on ne peut plus mettre que la classe $\\{3, 5, 6\\}$ qui ne forme pas une partition ; parfois les choix sont plus cornéliens : doit-on placer la classe $\\{3, 5, 6\\}$, ce qui empêche d'utiliser la classe  $\\{4, 5, 7\\}$ (par exemple) ? Ou ne pas la mettre ? A priori on ne sais pas.

{% exercice %}
Montrez que l'exemple possède une solution.
{% endexercice %}
{% details "solution" %}

On prend les 3 classes :

- $\\{1, 4\\}$,
- $\\{3, 5, 6\\}$,
- $\\{2, 7\\}$

{% enddetails %}

Prouver que le problème de Couverture Exact (CE) est NP-Complet va être plus facile que celle du théorème de Cook/Levin. En effet, maintenant que l'ensemble des problème NP-complet est non vide (il y a au moins SAT dedans), pour montrer qu'un problème $A$ est NP-complet il nous suffit maintenant de :

1. choisir un problème $B$ NP-complet
2. montrer que $B \leq A$

En effet, si $C$ est un problème quelconque de NP, on a $C\leq B$ (par définition de l'ensemble NP-complet) ce qui amène par transitivité de la réduction polynomiale à $C \leq A$.

Pour l'instant nous ne connaissons qu'un problème NP-Complet : SAT. Montrons donc que $SAT \leq CE$.

On considère alors une instance de SAT que l'on va transformer polynomialement en une instance de CE. Posons ses paramètres :

- $x_1, \dots, x_n$ : les $n$ variables booléennes
- $c_1 \land \lor \land c_m$ : les $m$ conjonctions de clauses
- $c_i = l^1_i \lor \dots \lor l^{k_i}_i$ : les littéraux formant les clauses.

On suppose de plus sans perte de généralité que :

1. il n'existe pas de clause ayant à la fois $x_i$ et $\overline{x_i}$ comme littéral (sinon cette clause est trivialement toujours vérifiée)
2. pour toute variable booléenne $x_i$ il existe une clause ayant $x_i$ comme littéral et une autre clause ayant $\overline{x_i}$ (sinon il suffit de mettre la modalité de $x_i$ à celle apparaissant dans les clauses pour les rendre trivialement vraies)

Notez que l'on peut transformer toute instance de $SAT$ en une instance satisfaisant les deux conditions ci-dessus en supprimant les clauses satisfaisant la première condition et en supprimant la variable booléenne satisfaisant la seconde condition. Cette transformation se fait en temps polynomial par rapport à l'entrée de $SAT$.

On peut maintenant transformer cette instance de  $SAT$ en une instance de $CE$ ayant comme entrée :

<div>
$$
\begin{array}{lll}
U = &\{ x_i \vert 1 \leq i \leq n \} \cup&\text{variables booléenne}\\
&\{ c_i \vert 1 \leq i \leq m \} \cup&\text{clauses}\\
&\{ l_{ij} \vert 1 \leq i \leq m, 1\leq j \leq k_i \}&\text{littéraux}\\
F = &(\cup_{1\leq i \leq n}\{ x_i, l_{j, k} \vert l_{j, k} = x_i, 1 \leq j \leq m, 1\leq k \leq k_i\}) \cup &\text{littéraux vrais pour }x_i\\
&(\cup_{1\leq i \leq n}\{ x_i, l_{j, k} \vert l_{j, k} = \overline{x_i}, 1 \leq j \leq m, 1\leq k \leq k_i\}) \cup &\text{littéraux faux pour }x_i\\
&(\cup_{1\leq i \leq m}(\cup_{1\leq k \leq k_i}\{ c_i, l_{i, k} \})) &\text{liens entre clauses et littéraux}\\
&(\cup_{1\leq i \leq m}(\cup_{1\leq k \leq k_i}\{ l_{i, k} \})) &\text{les littéraux}\\
\end{array}
$$
</div>

L'ensemble de $CE$ couvre tous les éléments de $SAT$ : les variables booléennes, les clauses et les littéraux. Les classes forment les liens entre les différents éléments : pour chaque $x_i$ les littéraux valant $x_i$, pour chaque $x_i$ les littéraux valant $\overline{x_i}$ et pour chaque clause l'ensemble de ses littéraux. Cette construction est bien polynomiale par rapport à la taille de l'entrée du problème $SAT$.

{% exercice %}
Transformez [l'instance exemple SAT](#exemple-SAT){.interne} en une instance de $CE$.
{% endexercice %}
{% details "solution" %}

<div>
$$
\begin{array}{ll}
U = &\{ x_1, x_2, x_3, x_4, x_5, c_1, c_2, c_3, c_4, l_1^1, l_1^2, l_2^1, l_2^2, l_2^3, l_3^1, l_3^2, l_3^3, l_3^4, l_4^1, l_4^2, l_4^3, l_4^4\}\\
F = &\{\{x_1, l_1^1, l_4^1\}, \{x_2, l_1^2\}, \{x_3, l_3^2\}, \{x_4, l_3^3, l_4^3\}, \{x_5, l_4^4\},\\
& \{x_1, l_2^1, l_3^1\}, \{x_2, l_2^2\}, \{x_3, l_2^3, l_4^2\}, \{x_5, l_3^4\},\\
& \{c_1, l_1^1\}, \{c_1, l_1^2\}, \{c_2, l_2^1\}, \{c_2, l_2^2\}, \{c_2, l_2^3\}, \{c_3, l_3^1\}, \{c_3, l_3^2\}, \{c_3, l_3^3\}, \{c_3, l_3^4\}, \{c_4, l_4^1\}, \{c_4, l_4^2\}, \{c_4, l_4^3\}, \{c_4, l_4^4\}\\
& \{l_1^1\}, \{l_1^2\}, \{l_2^1\}, \{l_2^2\}, \{l_2^3\}, \{l_3^1\}, \{l_3^2\}, \{l_3^3\}, \{l_3^4\}, \{l_4^1\}, \{l_4^2\}, \{l_4^3\}, \{ l_4^4\}\}
\end{array}
$$
</div>

{% enddetails %}

Il faut maintenant montrer deux choses :

- que si notre instance de $SAT$ à une solution alors notre instance de $CE$ en a également une
- que si notre instance de $CE$ à une solution alors on peut trouver une solution du problème $SAT$ associé en temps polynomial

Si l'instance de SAT a une solution, chaque clause $c_i$ possède au moins un littéral $l_i^{v(i)}$ qui est vrai. On peut alors considérer l'ensemble des classes formé de l'union de :

- $\\{c_i, l_i^{v(i)}\\}$ pour tout $ 1\leq i \leq m$,
- Considérons ensuite chaque littéral $l_i^j$ avec $ j \neq v(i)$ pour la solution de SAT. On a deux cas :
  - soit $l_i^j$ est vrai et on ajoute $\\{ l_i^j\\}$ à la solution de $CE$
  - soit $l_i^j$ est faux et on ajoute l'unique classe de $\mathcal{F}$ contenant $\\{x_i, l_i^j\\}$ à la solution de $CE$

De part nos hypothèses sur l'entrée de $SAT$ il est clair que cet ensemble de classes forme une solution à notre problème de $CE$. De plus, la construction de cette solution est bien polynomiale.

{% exercice %}
À partir de la solution $x_1 = \overline{x_2} = x_3 = \overline{x_4} = x_5 = 1$ de [l'exemple SAT](#exemple-SAT){.interne}, construisez la solution de $CE$ associée.
{% endexercice %}
{% details "solution" %}

<div>
$$
\begin{array}{ll}
F' = &\{ \{x_2, l_1^2\},  \{x_4, l_3^3, l_4^3\},\\
& \{x_1, l_2^1, l_3^1\}, \{x_3, l_2^3, l_4^2\}, \{x_5, l_3^4\},\\
& \{c_1, l_1^1\}, \{c_2, l_2^2\}, \{c_3, l_3^1\}, \{c_4, l_4^1\},\\
&   \{l_3^2\}, \{l_3^4\}, \{ l_4^4\}\}
\end{array}
$$
</div>

{% enddetails %}

On construit la réciproque de la même façon. Supposons que l'on ait une solution à notre problème de $CE$. Il ne peut exister qu'une seule classe contenant $x_i$ pour chaque $1 \leq i \leq n$. On place sa valeur à l'opposé des littéraux formant cette classe, ce qui donne en utilisant les mêmes arguments que précédemment une solution au problème $SAT$. Cette transformation est là encore clairement polynomiale.

{% exercice %}
Donnez une solution de CE pour l'exemple différente de celle de l'exercice précédent et servez vous en pour reconstruire une solution du problème SAT initial.
{% endexercice %}
{% details "solution", "open" %}

<div>
$$
\begin{array}{ll}
F' = &\{\{x_1, l_1^1, l_4^1\}, \{x_3, l_3^2\}, \{x_4, l_3^3, l_4^3\}, \\
& \{x_2, l_2^2\}, \{x_5, l_3^4\},\\
& \{c_1, l_1^2\}, \{c_2, l_2^3\}, \{c_3, l_3^1\}, \{c_4, l_4^2\},\\
& \{l_2^1\}, \{l_3^3\}, \{ l_4^4\}\}
\end{array}
$$
</div>

Ce qui donne comme solution de $SAT$ : $\overline{x_1} = {x_2} = \overline{x_3} = \overline{x_4} = x_5 = 1$
{% enddetails %}

On vient de prouver $SAT\leq CE$ : on a trouvé un deuxième élément à la classe des problèmes NP-complets !

![décidable](./NP-NP-2b.png)

### Que signifie NP-complet

Il existe un grand nombre de problèmes NP-complet. Juste après la démonstration de Levin et Cook en 1971, [Karp démontrait en 1972](https://en.wikipedia.org/wiki/Karp%27s_21_NP-complete_problems) qu'il y en avait au moins 21 de plus ! Et on ne cesse d'en découvrir d'autres.

Comme tout problème de NP est un cas particulier de tout problème de NP, ceci signifie ces problèmes sont _universels_. D'un point de vue algorithmique ceci signifie qu'il n'y a pas de lien polynomial entre les entrées et les solutions : ce sont des problèmes sans structure, [il n'y a pas de balle en argent](https://fr.wikipedia.org/wiki/Pas_de_balle_en_argent) pour résoudre magiquement le problème. Il faut tout essayer.

{% attention "**À retenir**" %}

Il faut voir les problèmes NP-complet comme des problèmes sans raccourcis, où il faut _a priori_ tout vérifier car la solution peut se trouver n'importe où _a contrario_ des problèmes polynomiaux où, selon l'entrée, les solutions sont circonscrites à un petit endroit que l'on peut rapidement (en temps polynomial) parcourir.

{% endattention %}

### P et NP

Si les problèmes de $P$ sont inclus dans $NP$, on ne sait pas si l'inclusion est stricte. On a implicitement supposé que les problèmes NP-complets ne sont pas dans P, mais en vrai on en sait rien : la question est ouverte ! Certains se demandent même si cette question est décidable (_ie._ démontrable).

{% info %}
Il existe même un prix d'un million de dollar pour qui donnerai une réponse à cette question (la valeur de cette récompense semble dérisoire par rapport à l'enjeu, mais elle a été proposée [à une époque où un million de dollar c'était quelque chose](https://www.youtube.com/watch?v=LCZMhs_xpjc) et n'a jamais été réévaluée...).
{% endinfo %}

![décidable](./NP-NP-3.png)

Ce qui est en revanche sur c'est que tout le monde espère que c'est vrai car sinon tout code informatique devient facilement déchiffrable et s'en est fini de la sécurité sur les réseaux (pour ne donner qu'une des conséquence de l'égalité de $P$ et de $NP$).

{% attention "**À retenir**" %}
Même si la chose n'est pas démontrée on considérera que $P \neq NP$ dans toute la suite de ce cours (et notre vie). Prouver qu'un problème est NP-complet sera donc une garantie que l'on ne pourra pas le résoudre de façon efficace et que l'on peut chercher une solution approchée via un algorithme polynomial.
{% endattention %}

### Pas dans P ni NPC ?

Pour ne rien rendre simple, il existe de nombreux problèmes pour lesquels on ne connaît pas d'algorithme polynomiaux mais que l'on arrive pas à démontrer NP-complet. Par exemple le problème suivant :

{% note "**Problème**" %}

- **Nom** : isomorphisme
- **Entrées** : [deux graphes](<https://fr.wikipedia.org/wiki/Graphe_(math%C3%A9matiques_discr%C3%A8tes)#D%C3%A9finition_et_vocables_associ%C3%A9s>) :
  - $G_1 = (V_1, E_1)$
  - $G_2 = (V_2, E_2)$
- **Sortie** : Rendre une bijection $\sigma$ de $V_1$ dans $V_2$ telle que $\\{x, y\\}$ est une arête de $G_1$ si et seulement si $\\{\sigma(x), \sigma(y) \\}$ est une arête de $G_2$ (ou `∅`{.language-} si une elle bijection n'existe pas).
  {% endnote %}

Par exemple en considérant les 3 graphes ci dessous :

![iso graphes](./iso-graphes.png)

Il est clair de voir que les 2 premiers sont isomorphes ($\sigma(a) = 1$, $\sigma(b) = 2$, $\sigma(c) = 4$ et $\sigma(d) = 3$) alors que le troisième ne l'est pas.

Mais c'est moins clair avec les deux suivants :

![Petesen iso](./petersen-iso.png)

{% exercice %}
Montrez que les deux graphes précédents sont isomorphes
{% endexercice %}
{% details "corrigé" %}

Le graphe en question est le graphe de Petersen, que l'on peut représenter de plein de jolis façons : <https://mathworld.wolfram.com/PetersenGraph.html>.

![Petesen iso](./petersen-iso-solution.png)

{% enddetails %}

Pour vérifier que la deux graphes $G_1 = (V_1, E_1)$ et $G_2 = (V_2, E_2)$ sont isomorphes avec une fonction $\sigma: V_1 \to V_2$ il faut montrer que :

- $\sigma$ est une bijection de $V_1$ dans $V_2$, donc que les deux tableaux $T_1 = [\sigma(x) \mbox{ pour chaque } x \in V_1]$ et $T_2 = [x \mbox{ pour chaque } x \in V_2]$ contiennent les mêmes éléments
- que les arêtes de $V_2$ sont bien arêtes de $V_1$ envoyées via $\sigma$, donc que les deux tableaux $T'_1 = [\\{\sigma(x), \sigma(y)\\} \mbox{ pour chaque } x \in E_1]$ et $T_2 = [xy \mbox{ pour chaque } xy \in E_2]$ contiennent les mêmes éléments

Ceci peut donc se faire en utilisant deux fois l'algorithme [égalité de tableaux](../projet-calcul-complexite/#égalité-tableaux){.interne} avec une complexité totale de $\mathcal{O}(\\; |\\; E_1\\; |^2\\; + \\; |\\; V_1\\; |^2\\;)$ (en supposant que $\\; |\\; E_1\\; |\\; = \\; |\\; E_2\\; |\\;$ et $\\; |\\; V_1\\; |\\; = \\; |\\; V_2\\; |\\;$). On en conclut que :

{% note %}
Le problème de l'isomorphisme de graphe admet un vérifieur efficace.
{% endnote %}

Le statut du problème de l'isomorphisme de graphe est au statut inconnu : on ne connaît aucun algorithme polynomial pour le résoudre et on n'arrive pas à prouver qu'il est NP-complet.

![décidable](./NP-NP-4.png)

{% exercice %}
Donnez une réduction polynomiale permettant de résoudre l'isomorphie de graphe avec SAT.
{% endexercice %}
{% details "solution" %}
Soient $G_1$ et $G_2$ deux graphes ayant $\\{1, \dots, n\\}$ comme ensemble de sommets.

On cherche une bijection entre les sommets de $G_1$ et $G_2$ qui respecte les arêtes. on va considérer $n^2$ variables binaires $x_{i, j}$ ($1\leq i, j\leq n$) telle que $x_{i, j}$ est vrai si et seulement si la bijection entre les  sommets de $G_1$ et $G_2$ associe le sommet $i$ de $G_1$ au sommet $j$ de $G_2$.

Les différentes contraintes sont alors :

- si $x_{i, j} = 1$ alors $x_{i, k} = 0$ pour tout $k\neq j$ : $\bigvee_{i}(x_{i, j} \land (\bigwedge_{k\neq j} \overline{x_{i, k}}))$
- si $x_{i, j} = 1$ alors $x_{k, j} = 0$ pour tout $k\neq i$ : $\bigvee_{j}(x_{i, j} \land (\bigwedge_{k\neq i} \overline{x_{k, j}}))$
- si $\\{i, j \\}$ est une arête de $G_1$ et $\\{k, l \\}$ n'est pas une arête de $G_2$, alors ni $x_{i, k}$ et $x_{j, l}$ ni $x_{i, l}$ et $x_{j, k}$ ne peuvent être vrai simultanément : $(\overline{x_{i, k}} \lor \overline{x_{j, l}}) \land (\overline{x_{i, l}} \lor \overline{x_{j, k}})$
- si $\\{i, j \\}$ est une arête de $G_2$ et $\\{k, l \\}$ n'est pas une arête de $G_1$, alors ni $x_{k, i}$ et $x_{l, j}$ ni $x_{l, i}$ et $x_{k, j}$ ne peuvent être vrai simultanément  : $(\overline{x_{k, i}} \lor \overline{x_{l, j}}) \land (\overline{x_{l, i}} \lor \overline{x_{k, j}})$

Regrouper toutes ces contraintes forme bien un ensemble de contraintes polynomial dans la taille des graphes $G_1$ et $G_2$ qui, si elles sont toutes satisfaites garantissent l'isomorphie.
{% enddetails %}

Même si le statut de l'isomorphie de graphe est inconnue, [il est très fortement suspecté](https://en.wikipedia.org/wiki/Graph_isomorphism_problem#Complexity_class_GI) qu'il ne soit ni sans P ni dans NPC. Il existe de nombreux autres problèmes dans ce cas là comme [le problème de la factorisation](https://fr.wikipedia.org/wiki/Factorisation) (alors que savoir si un nombre est premier ou pas [est polynomial](https://www.cse.iitk.ac.in/users/manindra/algebra/primality_v6.pdf). Mais cela dépasse de loin le cadre de ce cours introductif) ou [le logarithme discret](https://fr.wikipedia.org/wiki/Logarithme_discret) à la base des algorithmes de chiffrement.

## Autres classes

Nous nous restreindrons dans ce cours uniquement aux problèmes de $NP$ (et souvent uniquement à ceux de $P$) mais il en existe une foultitudes d'autres. On peut par exemple citer :

- la classe des problèmes de complexité poly-logarithmique $\mathcal{O}(\log^k(n))$
- la classe des problèmes de complexité polynomial en espace $\mathcal{O}(n^k)$
- ...

{% lien %}
Le lecteur intéresser pourra consulter [la page Wikipedia sur les classes de complexité](https://fr.wikipedia.org/wiki/Classe_de_complexit%C3%A9) qui en liste certaines.
{% endlien %}
