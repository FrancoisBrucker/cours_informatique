---
layout: layout/post.njk
title: "Décideurs et Décision"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD : chapeau

## Algorithmes, décideurs et vérifieurs

Rappelons qu'un algorithme est [dans toute sa généralité](../../bases-théoriques/calculabilité/#algorithme-fonction-N){.interne} une fonction de $\mathbb{N}$ dans $\mathbb{N}$ (tous les paramètres considérés comme des chaines de caractères peuvent être concaténés en une seule chaine. On verra dans quelques lignes une autre façon de _concaténer_ des entiers) et qu'[un décideur](../../écrire-algorithmes/problème/#décideur){.interne} est un algorithme dont la sortie est soit OUI (que l'on associe à 1) soit NON (associé à 0).

On va commencer par montrer qu'un algorithme peut être vu comme un décideur, ce qui nous permettra de voir trois formes équivalentes d'un algorithme.

Commençons par démontrer que $\mathbb{N}^2$ et $\mathbb{N}$ sont en bijection (on pourrait utiliser l'argument de [la partie calculabilité](../../bases-théoriques/calculabilité/#algorithme-fonction) en recodant les différents paramètres mais ne boudons pas notre plaisir en utilisant, et en la démontrant, la bijection classique que l'on doit au mathématicien [Cantor](https://fr.wikipedia.org/wiki/Georg_Cantor)) :

{% note "**Théorème**" %}
$\mathbb{N}^2$ et $\mathbb{N}$ sont en bijection.
{% endnote %}
{% details "preuve", "open" %}
Remarquons que tout élément de $\mathbb{N}^2$ est un point du plan :

![point de n2 dans le plan](n2_dans_plan.png)

On peut les parcourir en suivant les diagonales :

![point de n2 dans le plan](n2_dans_n.png)

On chemine alors comme ça :

1. $(0, 0)$
2. $(1, 0)$
3. $(0, 1)$
4. $(2, 0)$
5. $(1, 1)$
6. $(0, 2)$
7. $(3, 0)$
8. $(2, 1)$
9. $(1, 2)$
10. $(0, 3)$
11. $(4, 0)$
12. ...

Et on associe à un entier $(x, y)$ son ordre de cheminement $O((x, y))$ (par exemple $O((2, 1)) = 8$).

Ce cheminement est clairement une bijection.

On peut donc aussi associer un unique entier à tout couple d'entiers avec $O^{-1}$ ($O^{-1}(6) = (0, 2)$ par exemple).

{% enddetails %}
{% note "**Corollaire**" %}
$\mathbb{N}^p$ et $\mathbb{N}$ sont en bijection pour tout entier $p$.
{% endnote %}
{% details "preuve", "open" %}
La démonstration précédente montre que $\mathbb{N}^p = \mathbb{N}^2 \times \mathbb{N}^{p-2} $ est en bijection avec $\mathbb{N} \times \mathbb{N}^{p-2} = \mathbb{N}^{p-1}$ pour tout $p>2$.
{% enddetails %}

{% exercice %}
Écrivez le pseudo-code de la fonction $O^{-1}$ qui associe un couple $(x, y)$ unique à un entier $i$ passé en paramètre.
{% endexercice %}
{% details "solution" %}

```text
Nom : O^{-1}
Entrée : un entier i
Programme :
    x = y = 0
    k = 0
    tant que k < i:
        si x == 0:
            x = y + 1
            y = 0
        sinon:
            x = x - 1
            y = y + 1
    Retour (x, y)
```

{% enddetails %}

{% exercice %}
À partir du pseudo-code de $O^{-1}$, il est facile d’écrire le pseudo code de $O$ : faites le.
{% endexercice %}
{% details "solution" %}

```text
Nom : O
Entrée :  un couple (u, v) d'entiers
Programme :
    x = y = 0
    i = 0
    tant que (u, v) ≠ (x, y):
        i = i + 1
        si x == 0:
            x = y + 1
            y = 0
        sinon:
            x = x - 1
            y = y + 1
    Retour i
```

{% enddetails %}
Comme un algorithme est une fonction $f: \mathbb{N} \rightarrow \mathbb{N}$, on peut lui associer de façon équivalente la fonction $v_f$ ci-dessous :

$$
v_f(n, m) = \left\\\{
    \begin{array}{ll}
        1 & \mbox{si } f(n) = m\\\\
        0 & \mbox{sinon.}
    \end{array}
\right.
$$

On peut voir l'algorithme $v_f$ comme un vérifieur. Il vérifie que le second paramètre est la sortie du premier paramètre. On reparlera de ces algorithmes dans la suite, pour l'instant ils nous permettent de montrer que l'espace d'arriver d'un algorithme peut être uniquement deux valeurs. Un algorithme peut être vu comme une fonction de :

$$f: \mathbb{N}^2 \rightarrow \\{0, 1 \\}$$

Et comme $\mathbb{N}^2$ est en bijection avec $\mathbb{N}$, un algorithme est équivalent à un ***décideur*** :

{% note %}
Un **_décideur_** est une fonction de :

$$f: \mathbb{N} \rightarrow \\{0, 1 \\}$$

{% endnote %}

On ne va bien sur pas uniquement utiliser des décideurs en pratique, loin de là, mais cela montre que l'on peut se contenter de considérer les propriétés théoriques des décideurs  puisqu'on pourra les appliquer sans perte de généralité aux autres types d'algorithmes.

Avant de passer à l'étude théorique des problèmes et de les classer en plusieurs catégories, analysons les 3 formes d'algorithmes (équivalentes) utiles :

{% note "**À retenir**" %}
On peut représenter un algorithme sous 3 formes équivalentes :

- les **_fonctions_** : $A(x) = y$, avec $x, y \in \mathbb{N}$ qui permettent le calcul effectif,
- les **_décideurs_** : $A(x) = b$, avec $x \in \mathbb{N}$ et $b \in \\{0, 1\\}$ qui permettent de séparer les entiers en 2, les entiers _vrais pour $A$_ : $\\{ x \vert A(x) = 1 \\}$, et les autres
- les **_vérifieurs_** : $A(x, y) = b$, avec $x, y \in \mathbb{N}$ et $b \in \\{0, 1\\}$ qui, associé à un problème algorithmique $P$, permettent de vérifier si le couple $(x, y)$ est tel que $y$ soit une solution de $P$ avec $x$ comme entrée.

{% endnote %}

## Problèmes de décision 

De la même manière qu'un algorithme de type _fonction_ peut s'écrire sous la forme d'un algorithme de la forme _décideur_ on peut associer à tout problème algorithmique un problème de décision.

Considérons par exemple le problème de trouver le maximum d'un tableau. On peut lui associer le problème de décision suivant :

{% note "**Problème**" %}

- **nom** : plus grand que
- **données** :
  - un tableau d'entiers $T$
  - un entier $K$
- **question** : $T$ possède-t-il un élément plus grand ou égal à $K$

{% endnote %}

Si le problème _"plus grand que"_ est décidable, trouver le maximum d'un tableau l'est aussi en appliquant itérativement _"plus grand que"_ pour $K$ valant chaque élément de $T$.

L'équivalence entre les algorithmes et les décideurs d'une part et les problèmes algorithmiques et les problèmes de décision d'autres part, qui sont des structures plus simple à manipuler car ayant mois de paramètres en font les objets de prédilection de l'étude théorique des algorithmes.

{% note "**À retenir**" %}
Étudier les propriétés théoriques des algorithmes et des problèmes algorithmiques se fait, sans perte de généralité, via les décideurs et les problèmes de décision.
{% endnote %}

## Décideur et décision

Formalisons les notions de décideurs et des problèmes de décision (décidables) qui leurs sont associés. 

### Langage

Un algorithme décideur prend en paramètre un entier (donc de façon équivalente une suite de 0 et de 1, donc de façon équivalente une chaine de caractère, donc de façon équivalente tout ce qu'on veut d'autre de fini...) et répond soit 1 (qu'on assimile à VRAI ou OUI) soit 0 (qu'on assimile à FAUX ou NON) : il sélectionne un ensemble de nombres (donc de façon équivalente un ensemble de suites de 0 et de 1, donc de façon équivalente un ensemble de chaines de caractères, ...). 

{% note "**Définition**" %}
On appelle ***langage*** d'un décideur $A$ l'ensemble $A^{-1}(1)$.

On dira qu'un décideur $A$ ***accepte le langage $L$*** si $L = A^{-1}(1)$ et qu'un langage $L$ est ***décidable*** s'il existe un algorithme pour l'accepter.
{% endnote %}

La notion de langage est à rapprocher des ensembles décidables et des ensembles reconnaissable que l'[on a vus précédemment](../../écrire-algorithmes/problème).

### Décision

Deux décideurs sont équivalents s'ils acceptent le même langage. De façon formelle, un problème de décision est alors un langage qu'il s'agit de reconnaître avec un algorithme de la complexité la plus faible possible. De même que la complexité d'un problème est la complexité la plus faible d'un algorithme que le résout :


{% note "**Définition**" %}

La ***complexité d'un langage (décidable)*** est la complexité la plus faible d'un algorithme qui l'accepte.

{% endnote %}

## Complexités des décideurs

Comme un décideur prend en entrée un entier, sa complexité sera forcément calculé par rapport à lui. Pour un décideur $A$ prenant un entier $n$ en paramètre, on notera dans cette partie :

- $C(n)$ sa [complexité](../../complexité-calculs/définitions/#complexité).
- $S(n)$ sa [complexité spatiale](../../complexité-calculs/définitions/#complexité-spatiale),

Comme on se place d'un point de vue théorique, on supposera que chaque case mémoire ne peut contenir qu'un 0 ou un 1 (un bit) et que chaque instruction aura une complexité linaire en la taille de la donnée, codée au format binaire, qu'il manipule.

### Complexité spatiale et temporelle

On sait que la complexité spatiale d'un algorithme est forcément plus petite que sa complexité temporelle, mais la proposition suivante va plus loin et propose un encadrement :

{% note "**Proposition**" %}
Pour tout décideur sans instructions inutiles, on a l'encadrement :

<div>
$$
S(n) \leq C(n) \leq \mathcal{O}(S(n) \cdot 2^{S(n)})
$$
</div>


{% endnote%}
{% details "preuve", "open" %}
On suppose que le décideur a $L$ instructions.

1. comme le décideur est un algorithme, si la même ligne est exécutée plusieurs fois elle laisse à chaque fois la mémoire dans un état différent, sans quoi (les mêmes causes ayant les mêmes conséquences) l'algorithme va forcément boucler indéfiniment. Chaque ligne va donc  être exécutée au maximum $2^{S(n)}$ fois
2. chaque ligne peut lire ou modifier toutes les cases utilisées de la mémoire, sa complexité est donc en $\mathcal{O}(S(n))$

La complexité est donc bornée par $L \cdot 2^{S(n)} \cdot \mathcal{O}(S(n))$ et comme le nombre d'instructions du décideur est une constante on en déduit le résultat demandé.

{% enddetails %}

### Hiérarchie des complexités

On va montrer dans cette partie qu'il existe des langages de toute complexité et donc que les problèmes algorithmiques ne sont pas tous polynomiaux, loin de là.

La preuve est belle, simple mais atypique. 


#### Pseudo-code et entier

On suppose sans perte de généralité que nos programmes sont écrits en Français. Ils sont encodés sous forme binaire en utilisant le format [Unicode](Unicode) : chaque caractère est écrit sur 32 bits (c'est le format UTF-32). Tout entier, écrit au format binaire, peut alors :

1. parfois être vu comme une suite de caractères (si sa représentation binaire possède un multiple de 32 bits)
2. moins souvent, mais c'est possible, la suite de caractères forme un texte en français, terminé par un ou plusieurs caractères retour à la ligne (le retour à la ligne est un caractère Unicode correspondant à l'entier 10).
3. encore moins souvent ce texte, privé des derniers retour à la ligne est un programme écrit en pseudo-code.
4. et, cerise sur le gâteau parfois ce pseudo-code ne prend qu'un paramètre.

Savoir si un texte est un pseudo-code est facile. On regarde juste si [chaque instruction est autorisée](../../écrire-algorithmes/pseudo-code). Il existe donc un algorithme linéaire dans le nombre de caractères du programme permettant de savoir si un nombre est un pseudo-code ou pas. Si vous voulez vous fixer les idées, vous pouvez supposer sans perte de généralité que le pseudo-code est en fait écrit en python et on vérifie qu'il est syntaxiquement correct (pas de rouge dans vscode par exemple).

Si un entier $n$ correspond à un pseudo-code terminé par un ou plusieurs retour à la ligne, on appelle $P[n]()$ celui-ci. L'intérêt de supprimer les derniers retour à la ligne c'est que le même programme va apparaître une infinité de fois puisque $P[n]$ sera égal à $P[n']$ avec $n' = 2^{32}\cdot n + 10$ (on concatène à la représentation binaire de $n$ à la représentation binaire du caractère retour à la ligne en UTF-32, valant 10 codée sur 32 bits).


#### Exécution de pseudo-code

Considérons le programme suivant, qui prend en paramètre un pseudo-code :

```
Nom : Exécution
Entrées : 
    - un entier n correspondant à un pseudo-code P[n] à un paramètre
    - un entier K
Programme :
    Exécution du pseudo-code P[n](n) une instruction après l'autre :
        Avant l'exécution de l'instruction courante, on vérifie que l'instruction est corecte. 
        Si elle n'est pas correcte alors :
            Rendre 0
        Sinon :        
            on exécute l'instruction courante de P
        Si l'exécution de l'instruction stoppe P :
            si le retour de P est 0 :
                Rendre 1
            sinon :
                Rendre 0
        K = K - 1
        si K ≤ 0 :
            Rendre 0
```

Le code ci-dessus est bien un programme car il est syntaxiquement correct. C'est de plus un algorithme puisqu'il s'arrête forcément : soit après l'exécution de $P[n](n)$, soit si le pseudo-code de $P[n]$ contient une instruction non syntaxiquement correcte, soit enfin après l'exécution de $K$ instructions de $P[n](n)$. 

Enfin, il va rendre :

- 1 si $P[n](n)$ s'arrête en moins de $K$ instructions et rend la valeur 0
- 0 dans tous les autres cas.

{% note %}

{% endnote %}

{% note "**À retenir**"%}
Il existe des problèmes algorithmiques de complexités aussi grande ou aussi petite que l'on veut.

{% endnote %}
