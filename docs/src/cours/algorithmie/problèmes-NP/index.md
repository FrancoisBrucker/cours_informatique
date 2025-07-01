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

<div id="vérifieur"></div>
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

Ainsi, pour le maximum d'un tableau :

```pseudocode
algorithme vérification_max(T: [entier], sol: entier) → booléen:
  m ← max(T)  # algorithme linaire trouvant le maximum d'un tableau
  rendre m == sol
```

Dans le cas d'algorithme de résolution linéaire (comme pour le problème de la recherche du maximum), cette approche est optimale. Mais pour des problèmes dont l'algorithme de résolution est non linéaire on peut souvent trouver un algorithme de vérification de complexité plus faible.

{% exercice %}
Montrez que le problème [3-SUM](../problème-réduction/#problème-3-SUM){.interne} admet un vérifieur linéaire.
{% endexercice %}
{% details "solution" %}

```pseudocode
algorithme vérification_3_SUM(T: [entier], sol: (entier, entier, entier)) → booléen:
  i, j, k ← sol
  si T[i] + T[j] + T[k] == 0:
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

### Vérification efficace pas dans P ?

Il existe de nombreux problèmes pour lesquels on ne connaît pas d'algorithme polynomiaux pour les résoudre mais dont on peut facilement trouver un vérifieur efficace. Citons en 2, fondamentaux, pour se fixer les idées : [le problème l'isomorphisme de graphes](https://fr.wikipedia.org/wiki/Isomorphisme_de_graphes) et [le problème de la Satisfaisabilité (SAT)](https://fr.wikipedia.org/wiki/Probl%C3%A8me_SAT).

{% info %}
On ne connaît pas d'algorithmes polynomiaux pour résoudre ces deux problèmes. Essayez d'en trouver ! Si vous y arrivez, vous allez devenir célèbre.
{% endinfo %}

#### Isomorphisme de graphe

{% note "**Problème**" %}

- **Nom** : isomorphisme
- **Entrées** : [deux graphes](<https://fr.wikipedia.org/wiki/Graphe_(math%C3%A9matiques_discr%C3%A8tes)#D%C3%A9finition_et_vocables_associ%C3%A9s>) :
  - $G_1 = (V_1, E_1)$
  - $G_2 = (V_2, E_2)$
- **Question** : Donnez, si elle existe, une bijection $\sigma$ de $V_1$ dans $V_2$ telle que $\\{x, y\\}$ est une arête de $G_1$ si et seulement si $\\{\sigma(x), \sigma(y) \\}$ est une arête de $G_2$
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

#### <span id="SAT"></span>Problème SAT

Le problème SAT cherche à vérifier si une formule logique peut-être satisfaite.

Pour cela, commençons par définir un concept fondamental en logique la **_conjonction de clauses_** :

<div id="clauses"></div>

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
- **Sortie** : Si cela est possible, une assignation des variables $x_1$ à $x_n$ telle que $f$ soit vraie.

{% endnote %}
{% info %}
Une formule logique sous la forme d'une disjonction de clause est dite sous la [forme normale conjonctive](https://fr.wikipedia.org/wiki/Forme_normale_conjonctive). Toute formule logique peut être mise sous cette forme grâce à [la transformation de Tseitin](https://fr.wikipedia.org/wiki/Transformation_de_Tseitin) qui est linéaire en nombre d'opérations. Ceci exige de se retrouver avec un nombre exponentiel de clauses si on utilise juste [la distributivité des opérations logiques](https://fr.wikipedia.org/wiki/Forme_normale_conjonctive#Conversion_lin%C3%A9aire_%C3%A9quisatisfiable).

{% endinfo %}

Par exemple considérons les 4 clauses suivantes, sur 5 variables booléennes :

<div>
$$
(x_1 \lor {x_2}) \land (\overline{x_1} \lor \overline{x_2} \lor \overline{x_3}) \land (x_1 \lor x_3 \lor x_4 \lor \overline{x_5}) \land (x_1 \lor \overline{x_3} \lor x_4 \lor {x_5})
$$
</div>

Il y $2^5 = 32$ possibilités (O ou 1 ; Vrai ou Faux) pour chaque variable. Essayons en quelques une :

- $x_1 = x_2 = x_3 =x_4 = x_5 = 0$ ne permet pas de satisfaire la formule car $x_1 \lor {x_2} = 0$
- $x_1 = x_2 = x_3 =x_4 = x_5 = 1$ non plus ($\overline{x_1} \lor \overline{x_2} \lor \overline{x_3} = 0$)
- $x_1 = \overline{x_2} = x_3 = \overline{x_4} = x_5 = 1$ fonctionne

La formule précédente est satisfiable !

Montrons que SAT est dans NP :

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
 [1, 3, 4, -5],
 [1, -3, 4, 5]
]
```

Et la solution est un tableau de taille $n$ de booléens. Par exemple pour la solution $x_1 = \overline{x_2} = x_3 = \overline{x_4} = x_5 = 1$ on a l'encodage : `[Vrai, Faux, Vrai, Faux, Vrai]`
{% enddetails %}

{% exercice %}
Utilisez le codage précédent pour montrer que SAT est dans NP.
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


> TBD dire que si on a une solution potentielle alors facile de savoir si vrai solution (donner algo) mais que trouver l'algo on ne sait pas trop à part essayer toutes les solution (donner nb de solutions).
> TBD Résolution basique énumération en $2^n$ vrai/faux pour chaque variable.

> TBD toute formule logique peut s'écrire comme une conjonction de clause. CNF-SAT mais on peut passer de toute formule à SAT en temps linéaire :

> TBD ici
> :

> TBD exemple et vérification.

## Problèmes NP

Nous venons de caractériser les problèmes utiles qui s'appellent en algorithmie les problèmes NP :

{% note "**Définition**" %}
**_Un problème algorithmique est dit_** $NP$ s'il existe un vérifieur efficace de ses solutions.
{% endnote %}

Ce qui donne le schéma suivant :

![décidable](./NP-NP-1.png)

La définition ci-dessus appelle une remarque : le nom a été très mal choisi. Il signifie _Non Déterministe Polynomial_ (et **_pas du tout_** non polynomial...) car cette classe de problème a initialement été déterminée par rapport aux [machines de Turing non déterministes](https://fr.wikipedia.org/wiki/Machine_de_Turing_non_d%C3%A9terministe) que l'on ne verra que bien plus tard : un problème est dans NP s'il peut être résoluble de façon polynomiale par une machine de Turing non déterministe. Dans ce cadre la définition fait sens puisqu'elle est identique à $P$ pour un autre type de machine.

{% attention "**À retenir**" %}
Un problème est dans $NP$ s'il existe un vérifieur efficace de ses solutions. Ce sont exactement les problèmes algorithmiques utilisable en pratique car :

- On peut énumérer toutes les solutions possibles en temps fini, mais en temps exponentiel (ce qui fonctionne lorsque la taille d'entrée est faible).
- On peut vérifier efficacement (en temps polynomial) si une proposition de solution est réellement une solution.

{% endattention %}

Il est clair que l'on a l'inclusion des classes $P$ inclut dans $NP$ inclut dans décidable. Mais cette inclusion est-elle stricte ? Nous en parlerons plus en détails dans la partie suivante, dédiée aux problèmes de décision, où l'on montrera qu'il existe des problèmes décidables mais non dans NP.

En revanche, la question de savoir s'il existe des problèmes de décision qui sont dans $NP$ mais pas dans $P$ est ouverte ! Il existe même un prix d'un million de dollar pour qui donnerai une réponse à cette question (la valeur de cette récompense semble dérisoire par rapport à l'enjeu, mais elle a été proposée [à une époque où un million de dollar c'était quelque chose](https://www.youtube.com/watch?v=LCZMhs_xpjc) et n'a jamais été réévaluée...).

Certains se demandent même si cette question est décidable (_ie._ démontrable). Ce qui est en revanche sur c'est que tout le monde espère que c'est vrai car sinon tout code informatique devient facilement déchiffrable et s'en est fini de la sécurité sur les réseaux (pour ne donner qu'une des conséquence de l'égalité de $P$ et de $NP$).

Enfin :

{% note "**(Gros) Théorème ([Cook & Levin en 1971](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_Cook))**" %}

Il existe des problèmes dans NP, nommé **NP-complets**, dont la résolution permet de résoudre tout problème de NP.

C'est à dire que si $A$ est un problème NP-complet et que $B$ est un problème de NP alors il existe une **réduction polynomiale** de $B$ vers $A$ : on a $B \leq A$.

{% endnote %}

{% note "**Théorème ([Karp en 1972](https://en.wikipedia.org/wiki/Karp%27s_21_NP-complete_problems))**" %}

Le problème du sac à dos est NP-complet.

{% endnote %}
{% info %}
Nous démontrerons ceci rigoureusement plus tard.
{% endinfo %}

![décidable](./NP-NP-2.png)

Notez que :

- le statut du problème de l'isomorphisme de graphe est au statut inconnu : on ne connaît aucun algorithme polynomial pour le résoudre et on n'arrive pas à prouver qu'il est NP-complet.
- il existe des problèmes décidables qui ne sont pas dans NP (c'est la flèche _non vide_). On le démontrera bien plus tard en montrant qu'il existe des problèmes où si l'on cherche à répondre OUI, le problème est dans NP et si l'on cherche à répondre NON au même problème, il n'y est pas.

{% attention "**À retenir**" %}

Il faut voir les problèmes NP-complet comme des problèmes sans raccourcis, où il faut _a priori_ tout vérifier car la solution peut se trouver n'importe où _a contrario_ des problèmes polynomiaux où, selon l'entrée, les solutions sont circonscrites à un petit endroit que l'on peut rapidement (en temps polynomial) parcourir.

{% endattention %}

Les problèmes NP-complets sont tous équivalents car ils correspondent tous à **des problèmes universels**, sans structure. Les entrées ne donnent pour ces problèmes aucun indice utilisable efficacement sur l'endroit où va se trouver la solution. On les rencontre vraiment partout :

{% lien %}
[Jeux video NP-complet](https://www.youtube.com/watch?v=9rUUs8SlaOE)
{% endlien %}

> TBD montrer isomorphe ≤ SAT et sur l'exemple du graphe de Petersen.
> TBD SAT pas tout seul. Montrer SAT ≤ exact cover.

## Autres classes

Nous nous restreindrons dans ce cours uniquement aux problèmes de $NP$ (et souvent uniquement à ceux de $P$) mais il en existe une foultitudes d'autres. On peut par exemple citer :

- la classe des problèmes de complexité poly-logarithmique $\mathcal{O}(\log^k(n))$
- la classe des problèmes de complexité polynomial en espace $\mathcal{O}(n^k)$
- ...

{% lien %}
Le lecteur intéresser pourra consulter [la page Wikipedia sur les classes de complexité](https://fr.wikipedia.org/wiki/Classe_de_complexit%C3%A9) qui en liste certaines.
{% endlien %}
