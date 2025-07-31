---
layout: layout/post.njk 
title:  "SAT et pseudo-code"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


> TBD plan

Le but de cette partie est de montrer que l'on peut "_compiler_" tout algorithme de signature `f(e:[bit]) → [bit]`{.language-} écrit en pseudo-code en une formule SAT.

## Pseudo-code utilisé

> TBD dire que l'on a un algo écrit en pseudo code avec fct booléenne que l'on peut écrire sous notre forme.
> Donner la complexité nouvelle nouvelle par rapport à l'ancienne en temps : même O et en mêmoire du carré.

On utilise une version épurée (mais équivalente) au [pseudo-code utilisant des opérations de fonctions booléennes](../fonctions-booléennes){.interne}.

Soit $A$ un algorithme (il s'arrête pour toute entrée) écrit en pseudo-code. On peut supposer sans perte de généralité que :

- son entrée est une variable `e:[bit:n]`{.language-} de longueur $n$, 
- sa sortie est une variable `s:[bit]`{.language-},
- chaque ligne $A_i$ du pseudocode correspond à une instruction
- Sa complexité temporelle vaut $C(n)$ et sa complexité spatiale $S(n)$

On va de plus simplifier l'écriture des instructions et des variables pour notre conversion en une formule SAT soit plus simple.

### Allocation de variables

On suppose que la taille de chaque variable est connue et ne dépend que de la taille de l'entrée. Ceci peut se faire sans perte de généralité et à un coût en complexité acceptable.

En effet pour tout algorithme de complexité temporelle et spatiale valant respectivement $C(n)$ et $S(n)$, on peut créer chaque variable de type `[bit]`{.language-} avec une taille de $S(n)$. Ce nouvel algorithme aura la même complexité temporelle que l'original (les tableaux  sont tous juste plus grand) et aura une complexité spatiale bornée par $C(n) \cdot S(n)$ (il y a au pire $C(n)$ variables binaires).

{% note %}
Les seules instructions de création de variables seront :

1. `b ← nouveau bit`{.language-} création d'une variable $b$ de type `bit`{.language-}
2. `t ← nouveau [bit]`{.language-} création d'une variable $t$ de type `[bit]`{.language-} de longueur dépendant de la taille de l'entrée

Toutes ces instructions vont nécessiter $\mathcal{O}(1)$ opérations élémentaires
{% endnote %}

> TBD allocation doit être connue à la "compilation"

### Affectation de variables

> TBD on peut se ramener à des affectations de bits.

- `b ← 0`{.language-} où $b$ est une variable de type `bit`{.language-}
- `b ← 1`{.language-} où $b$ est une variable de type `bit`{.language-}
- `b ← b'`{.language-} où $b$ et $b'$ sont des variables de type `bit`{.language-}
- `t[u(i)] ← b`{.language-} où $b$ est une variable de type `bit`{.language-}, $t$ et $u$ des des variables de type `[bit]`{.language-}
- `b ← t[u(i)]`{.language-}où $b$ est une variable de type `bit`{.language-}, $t$ et $u$ des des variables de type `[bit]`{.language-}

### Opérations

> TBD
> toute fonction booléenne `f(e:[bit:N]) → [bit:N']`{.language-} avec  $N$ et $N'$ fixé.
> De même que pour les variables on se restreint aux fonction booléennes. Toute fonction booléenne vectorielle est une suite finie de fonction booléennes.  Mais on peut encore simplifier en `f(e:[bit:N]) → bit`{.language-}

### Instruction de saut

On remplace l'instruction de test (`si x: ...bloc...`{.language-}) et de répétition `tant que x: ...bloc...`{.language-} par une unique instruction de saut : `x ← 1; si x va l`{.language-} où `x` est une variable binaire. Si `x = 1`{.language-} alors l'algorithme "_saute_" à la ligne $l$ pour sa prochaine instruction plutôt que d'aller à la ligne suivante.

{% note %}
La seule instruction de contrôle utilisée sera :  `si b va l`{.language-} où $b$ est une variable de type `bit`{.language-} et $l$ un numéro de ligne.
{% endnote %}

## Formule logique et SAT


L'exécution d'un pseudo-code consiste à exécuter une ligne du pseudo-code après l'autre jusqu'à exécuter une instruction de fin. 

> TBD à la fin arriver à `algo(e:[bit:n], s: [bit:n']) -> vide` et il rend rien. 

Commençons par remarquer que si l'on possède une formule CNF pour toute instruction possible de l'algorithme, la formule suivante exécute la ligne $l$ de l'algorithme si $F_i$ est la formule logique associée à la ligne $l$ de celui-ci :

<div>
$$
EXE(l) \coloneqq ((l == 1) \land F_1) \lor ((l == 2) \land F_2) \lor ((l == L) \land F_L)
$$
</div>

Remarquez que l'équation ci-dessus est bien une formule logique car $l\leq L$ qui est une constance donc $l == i$ pour $1\leq i \leq L$ est une fonction booléenne et s'écrit comme une CNF.

Cette instruction est exécutée avec un jeu de variables donné :

<div>
$$
V \coloneqq (b_1 = B_1) \land \dots \land (b_k = B_k) \dots (t_1 = T_1) \land \dots \land (t_{k'} = B_{k'})
$$
</div>

Avec :

- $(b = B) \coloneqq (b \land B) \lor (\overline{b} \land \overline{B})$ pour des variables binaires $b$ et des valeurs $B \in \\{0, 1\\}$
- $(t = T) \coloneqq [(t[0] \land T[0]) \lor (\overline{t[0]} \land \overline{T[0]})] \land \dots \land [(t[K-1] \land T[K-1]) \lor (\overline{t[K-1]} \land \overline{T[K-1]})]$ pour des variables tableau $t$ et des valeurs $T \in \\{0, 1\\}^K$

On en conclut que si l'on connaît l'état des variable du programme et la ligne à exécuter, ceci peut s'écrire sous la forme de la formule logique :

<div>
$$
EXE(l) \land V
$$
</div>

Le but de ce qui va suivre est de terminer le travail, c'est à dire de passer de l'exécution d'une ligne à l'exécution de tout un algorithme. Ceci va être possible en conservant toutes les itérations de l'exécution de l'algorithme en une seule formule.

### Suivi des instructions

Il faut pouvoir garder trace de chaque instruction tout au long de l'exécution de l'algorithme. Pour cela on peut définir une variable spéciale $l$ de type `[bit:log(L)]`{.language-} qui va contenir le numéro de la ligne exécuté. On aura besoin de la fonction booléenne $(l == m)$ définie de $\\{0, 1\\}^{\log(L)} \rightarrow \\{0, 1\\}$. Et que l'on peut écrire avec $\mathcal{O}(\log(L)) = \mathcal{O}(1)$ littéraux.

Comme on doit modifier cette ligne après chaque instruction, on va considérer la variable $l^i$ qui est la ligne de l'algorithme exécutée à l'itération $i$ :

- soit l'instruction n'était pas une instruction de saut et $l^{i+1} ← \text{INC}(l^i)$ avec INC la fonction booléenne vectorielle sur des tableaux de longueur $\log_2(L)$
- soit l'instruction était une instruction de saut réussi `si x va l'`{.language-} et $l^{i+1} ← s(l_i)$ avec $s(l_i)$ une constante valant la ligne vers laquelle sauter présente à la ligne $l_i$ de l'algorithme.

Dans les deux cas, on peut écrire cela sous la forme d'une formule :

- si pas de saut : on utilise la forme normale conjonctive associée à `INC`{.language-} : $N(i) \coloneqq \text{CNF}(\text{INC}, l^{i}, l^{i+1})$
- si un saut vers la ligne $s$ : on utilise la formule logique $(l^{i+1} = s)$ si le saut est réussi et on incrémente sinon : $S(i, s) \coloneqq (\overline{x} \land \text{CNF}(\text{INC}, l^{i}, l^{i+1})) \lor (l^{i+1} = s)$. 

Tout ces choix peuvent s'écrire comme une grande formule en notant $L_S$ l'ensemble des lignes avec saut, $\overline{L_S}$ l'ensemble des lignes sans saut et $L_F$ l'ensemble des ligne de rendu (`rendre s`{.language-}) :

<div>
$$
L^i \coloneqq [\bigvee_{l \in \overline{L_S}}((l^i == l) \land N(i))] \lor [\bigvee_{l \in {L_S}}((l^i == l) \land S(i, s(l)))] \lor [\bigvee_{l \in {L_F}}((l^i == l) \land (l^{i+1} = l^i))]
$$
</div>

Cette formule est constituée de $\mathcal{O}(L \cdot \log_2(L)) = \mathcal{O}(1)$ littéraux. 

On a ajouté l'ensemble des lignes de fin comme sentinelle pour s'assurer qu'il y aura toujours $C(n)$ itérations : une fois arrivé à une ligne de rendu on ne change plus de ligne. Ceci permet d'écrire la formule logique générale permettant de suivre les lignes exécutées tout au long de l'algorithme :

{% note %}
Le suivi des lignes d'instructions effectuées par l'algorithme tout au long de son exécution est une formule à $\mathcal{O}(C(n) \cdot L \cdot \log_2(L)) = \mathcal{O}(C(n))$ littéraux :

<div>
$$
L \coloneqq (l^1 = u(1)) \land [\bigwedge_{1\neq i \leq C(n)} L^i]
$$
</div>

{% endnote %}

### Suivi des variables

Le programme commence par initialiser la variable d'entrée, puis chaque itération va modifier une variable. Pour rendre compte de ces modifications au cours du temps on va dupliquer chaque variables pour chaque itération. La variable $v$ aura ainsi $C(n)$ copies telle que :

- $v^1$ soit sa valeur à la première itération,
- $v^i$ soit sa valeur au début de la $i$ème itération
- $v^{C(n)}$ sa valeur à la fin de l'exécution

Pour écrire cela sans peine, on peut supposer sans perte de généralité que l'algorithme possède $S(n)$ variables $v_1$ à $v_K$ et telles que $v_1$ soit l'entrée et $v_2$ la sortie. L'initialisation des variables est alors :

<div>
$$
V^0 \coloneqq (v_1 = e)
$$
</div>

Qui est une formule de $S(n)$ littéraux

Entre la $i$ème et la $i+1$ème itérations toutes les variables non modifiées par l'instruction courant sont les mêmes. En notant $v^i$ la variable à l'itération $i$ on a $v^i = v^{i+1}$ sauf si l'instruction $i$ la modifie. On peut alors définir :


<div>
$$
V(i, k) \coloneqq \bigwedge_{j\neq k}(v^{i+1}_j = v^i_j)
$$
</div>

La formule précédente conserve toutes les variable à part $v_k$ entre l'itération $i$ et l'itération $i+1$ et possède $\mathcal{O}(S(n) \cdot S(n))$ littéraux (si toutes les variables sont des tableaux).

En notant $k_l$ la variable modifiée par l'instruction de la ligne $l$ du programme on a :

<div>
$$
V^i \coloneqq \bigvee_{1\neq m \leq L}((l^i == m) \land V(i, k_m))
$$
</div>

Qui est une formule de $\mathcal{O}(S(n) \cdot S(n) \cdot L)$ littéraux permettant de conserver toutes les variables saut celle modifiée d'une itération à l'autre.

{% note %}
La conservation des variables non modifiées tout au long du programme est une formule à $\mathcal{O}(C(n) \cdot S(n) \cdot S(n) \cdot L) = \mathcal{O}(C(n) \cdot S(n) \cdot S(n))$ littéraux :

<div>
$$
V \coloneqq (v^1_1 = e) \land (\bigwedge_{1\neq i \leq C(n)} V^i) \land (s = v^{C(n)}_2)
$$
</div>
{% endnote %}


### Opération

> TBD les seules instructions qu'il faut convertir en formule sont les affectations de variables et les fonctions booléennes

#### Fonction booléennes

En utilisant le fait que [toute fonction booléenne peut s'écrire sous une forme normale conjonctive](../fonctions-booléennes/#){.interne}, on peut associer à toute opération `y ← f(x)`{.language} telle que `f(x:[bit:n]) → bit`{.language-} une formule normale conjonctive `F(x)`{.language-} telle que $y = F(x)$ et on a la formule normale conjonctive suivante : $CNF(f, x, y) = (F(x) \land y) \lor \overline{y} = F(x) \lor \overline{y}$. En faisant rentrer $\overline{y}$ dans toutes les clauses, on a bien une forme normale conjonctive $CNF(f, x, y)$ qui est vrai si et seulement si $f(x) = y$.

> TBD montrer avec `b ← NAND(b', b'')`{.language-} où $b$, $b'$ et $b''$ sont des variables de type `bit`{.language-}
>  et dire que ça suffit puisque tout fct booléenne est un gros `NAND`.

#### Affectation de variables

> TBD facile si constante, on fait comme pour les fonctions booléenne, problème = $t[u(i)] \leftrightarrow$ car i n'est pas une constante

### Formule finale

> TBD taille totale. On fait complexité fois chaque itération
> TBD NB de clauses totales
> TBD Tseitin pour tout mettre ensemble en CNF
> TBD pour chaque entrée on crée une clause en temps dépendant de la complexité spatiale et temporelle par rapport à l'entrée.

## Résolution

> TBD dire que c'est polynomiale en la complexité spatiale et temporelle. Donc si algo poly alors nb de littéraux aussi poly.


## Inversibilité de SAT


5. résoudre sortie = résoudre entrée ! 
6. ce n'est pas encore Cook et Levin car pas polynomial.

> Inversibilité du problème SAT

> TBD fct booléenne de l'addition ou du produit. Comme c'est une fonction booléenne cela permet d'avoir une réponse mais aussi d'avoir les entrées.
>
> TBD on y reviendra mais en crypto c'est crucial de ne pas pouvoir  faire... Par exemple pour les produit de 2 nombres premiers. On revient au fait que factor doit être de complexité importante.
> 
> polylog circuit et sat : <https://www.youtube.com/watch?v=6OPsH8PK7xM>
>
>

> exemple réduction :
>

> TBD une seule grosse variable  qui est la mémoire et des registres qui permettent de faire le lien.

## odds and ends

> TBD à mettre avant

### SAT et résolution

> 
Pour chaque variable on fait varier $l$ pour toute les lignes du pseudo-code.

Le nombre d'instruction étant 
On peut alors encore simplifier 

> TBD crée des variables 
> TBD faire des variables sans se préoccuper de combien puis dire que c'est un problème et dire que c'est la complexité spatiale et on peut créer un SAT juste avec la taille d'entrée.
> 
1. formule logique : avec et ou non. On a vu que ça fait tout. On peut "programmer" le tout en remplaçant des choses plus évoluée. Et max d'un tableau.
2. transformation en CNF avec Tseitin Linéaire rappel de ce que l'on a vu

s.

> TBD attention complexité spatiale et temporelle.
>- création et affectation d'une variable :
  - `x ← 0`{.language-} où $x$ est une variable de type `bit`{.language-} : création d'une variable de type `bit`{.language-} et initialisation à 0
  - `x[:K] ← 0`{.language-} création d'une variable de type `[bit]`{.language-} à $K$ éléments et initialisation de chacun de ses éléments à 0
  - `x[:u(k)] ← 0`{.language-} création d'une variable de type `[bit]`{.language-} à $u(k)$ éléments et initialisation de chacun de ses éléments à 0

> TBD faire la fonction associe un déplacement pour contraindre toute case allouée à être utilisée avec un dictionnaire de taille la complexité, change rien si poly on  est en complexité au carré.
> TBD mais cases non initialisé implique résultat pas déterministe (aussi dans la vraie vie...) donc on alloue = bonne pratique et on force ici: `t[:n] ← 0` pour allouer. NB ne change rien. en vrai mais plus propre. même en code.

### Pseudo-code et transcription vers une formule logique

3. pseudo-code = pseudo-code binaire = instructions minimales
4. pseudo-code = formule logique = SAT (taille des tableaux = complexité)

> TBD attention à la taille des tableaux. Elle doit être connue à la "compilation" donc doit uniquement dépendre de la taille des entrées
à chaque étape toute les variables.

{% note "**Proposition**" %}
Un pseudo-code utilisant uniquement :

- des variables binaires ou des tableaux binaires
- l'opération logique `NAND`{.language-}
- des affectations de bit (variable binaire ou une case de tableaux)
- des boucles `tant que x: <bloc>`{.language-} avec $x$ une variable binaire :  le bloc n'est exécuté que si $x = 1$.
- des instructions conditionnelles de la forme `si x: <bloc>`{.language-} avec $x$ une variable binaire :  le bloc n'est exécuté que si $x = 1$.
 
A la même expressivité que [le pseudo-code classique](../pseudo-code/){.interne}.
{% endnote %}

> TBD tout algo est un sat.
> TBD on a vue que les opérations peuvent être mise sous forme logique. C'est aussi vrai pour les structures de contrôle.
> TBD on vu que toute fonction est un sat et que tout circuit logique est un sat. Le problème SAT va être fondamental.
> TBD dire que toute fonction booléenne vectorielle s'écrit comme une conjonction de clause. et que comme on passe d'un problème à l'autre, on peut le faire puisque nos entrées sont données.

> TBD dire taille des variables dépendant de la taille des entrées. Au pire = complexité. Ne change pas si dans P.

> TBD : Dire, mais laisser la démo pour plus tard, que SAT est supérieur à tout et donner exemple de réduction ≤ SAT et aussi ≥ SAT mais pas le sac à dos.

