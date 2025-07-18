---
layout: layout/post.njk

title: Définitions

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

La complexité d'un pseudo-code est une mesure associée au pseudo-code. Elle peut mesurer 2 grandeurs physique lors de l'exécution d'un algorithme :

- **_complexité en temps_** : le nombre d'instructions effectuées pendant son exécution
- **_complexité en espace_** : le nombre de cases mémoires maximales utilisées pendant son exécution.

Par défaut, la complexité utilisée est celle en temps :

{% note "**Définition**" %}
La complexité d'un pseudo-code est la complexité en temps de celui-ci.
{% endnote %}

Par exemple le pseudo-code suivant :

```pseudocode/
age ← 42
si ((age ≥ 12) et (age < 20)):
    personne ← "teenager"
```

- première ligne : 2 instructions
  1. Création de l'entier valant 42 : 1 instruction
  2. on affecte l'entier à la variable `age`{.language-} : 1 instruction
- deuxième ligne : 8 instructions
  1. faire `age ≥ 12`{.language-}. Pour cela :
     - on crée l'entier valant 12 : 1 instruction
     - on récupère la valeur de `age`{.language-} : 1 instruction
     - on effectue la comparaison : 1 instruction
  2. faire `age < 20`{.language-}. Pour cela :
       - on crée l'entier valant 20 : 1 instruction
       - on récupère la valeur de `age`{.language-} : 1 instruction
       - on effectue la comparaison : 1 instruction
  3. faire l'instruction `et`{.language-} : 1 instruction
  4. faire l'instruction `si`{.language-} : 1 instruction
- troisième ligne : 2 instructions
  1. on crée la chaîne : 1 instruction
  2. puis affecte le résultat : 1 instruction

Un nombre total d'instructions de 12 pour ces trois lignes de pseudo-code.

## Complexité des appels de fonctions

Si l'on devait à chaque pseudo-code redéfinir tout les algorithmes qu'on utilise ce serait vraiment fastidieux. On utilise souvent des fonctions non basiques (comme l'affichage à l'écran qu'on a déjà vu) ou des structures plus élaborées (les listes par exemples qui sont des extensions des tableaux). Il faudra cependant toujours connaître les complexités de ce qu'on utilise.

{% attention %}
Lorsque l'on calcule la complexité d'un pseudo-code utilisant des fonctions, il faut compter le nombre d'instructions de l'exécution des fonctions !
{% endattention %}

Reprenons par exemple [le code de l'algorithme recherche](../../bases-théoriques/définition/#algorithme-recherche){.interne} et comptons les instructions utilisées au cours de son exécution :

```pseudocode/
fonction recherche(T: [entier], x: entier) → booléen:
    pour chaque e de T:
        si e == x:
            rendre Vrai
    rendre Faux

T ← [1, 2, 6]
trouve ← recherche(T, 6)
affiche à l'écran trouve
```

1. exécution de la ligne 7 : 8 instructions
   - création d'un tableau : 1 instruction
   - création de 3 entiers : 3 instructions
   - affectation des 3 entiers aux indices du tableau :  3 instructions
   - affectation du tableau à une variable : 1 instruction
2. exécution de la ligne 8 :
   1. exécution de la fonction recherche (ligne à ligne) :
      1. exécution de la ligne 1 : affectation des paramètres
         1. trouver les objets à mettre en paramètres :
            - pour le premier paramètre il faut trouver l'objet associé à t : 1 instruction
            - pour le second paramètre, l'objet est à créer : 1 instruction
         2. affecter les paramètres aux variables de la fonction :
            - affectation du premier paramètre à la variable locale `t`{.language-} : 1 instruction
            - affectation du second paramètre à la variable locale `x`{.language-} : 1 instruction
      2. exécution de la ligne 2 (3 fois) : trouver l'objet du tableau puis l'affecter à `e`{.language-} : 2 instructions
      3. exécution de la ligne 3 (3 fois) : un test
         - on trouve les objets associées à `t`{.language-} et `e`{.language-} : 2 instructions
         - on teste l'égalité : 1 instruction
         - on fait le `si`{.language-} : 1 instruction
      4. exécution de la ligne 4 (1 fois) : on arrive à cette ligne à la troisième itération : 2 instructions (une pour créer le booléen, l'autre pour le rendre)
   2. affection de la variable `trouve`{.language-}
3. afficher quelque chose à l'écran :
   - 1 instruction pour trouver l'objet à afficher
   - 1 instruction pour trouver l'afficher

Au total on eu besoin de $8+\underbracket{(4 + 3 \cdot (4+4) + 2)}_{\mbox{recherche(t, 6)}} + 1 + 2$
instructions c'est à dire $41$ instructions.

## Complexité des accès à un tableau ?

Combien d'instructions nécessite la création et l'accès à un tableau ?

On considérera en algorithmie que tous les accès à un élément donné d'un tableau nécessite 1 instruction. Ainsi :

- créer un tableau de taille $n$ nécessite 1 instruction
- accéder à un indice donnée en lecture nécessite 1 instruction
- accéder à un indice donnée pour une affectation nécessite 1 instruction

De là l'instruction :

- créer un tableau de taille 42 nécessite  1 instruction
- créer un tableau de taille $2^{42}$ nécessite  1 instruction
- `F ← un tableau de taille 42`{.language-} nécessite 2 instructions, une pour la création, la seconde pour l'affectation
- `afficher à l'écran F[3]`{.language-} nécessite 2 instructions, une pour retrouver l'objet associé à `F[3]`{.language-}, l'autre pour l'afficher
- `F[3] ← 42`{.language-} nécessite 2 instructions, une pour créer l'entier `42`{.language-}, l'autre pour l'affecter
- `F[i] ← 42`{.language-} nécessite 3 instructions, une pour créer l'entier `42`{.language-}, une pour trouver l'objet associé à `i`{.language-} (ce n'est pas une constante) l'autre pour l'affecter
- `F[i-1] ← 42`{.language-} nécessite 5 instructions, une pour créer l'entier `42`{.language-}, une pour trouver l'objet associé à `i`{.language-}, une pour créer l'entier 1, une pour l'addition et la dernière pour l'affectation.

## Complexité d'un algorithme

Le pseudo-code suivant, qui calcule la dixième valeur de la suite de Fibonacci a une complexité $C = 144$ :

```pseudocode/
F ← un tableau de 10 entiers
F[0] ← 1
F[1] ← 1

i ← 2
tant que i ≤ 9 :
  F[i] ← F[i - 1] + F[i - 2]
  i ← i + 1

rendre F[9]
```

{% exercice %}
Explicitez les différentes instructions élémentaires pour justifier la valeur de la complexité de l'algorithme précédent.
{% endexercice %}
{% details "corrigé" %}

La complexité de chaque ligne :

- ligne 1 : 2 instructions (une création et une affectation)
- ligne 2 : 2 instructions (une création et une affectation)
- ligne 3 : 2 instructions (une création et une affectation)
- ligne 4 : 0 instruction
- ligne 5 : 2 instructions (une création et une affectation)
- ligne 6 : 4 instructions
  - création de l'entier 9
  - récupération de la variable `i`{.language-}
  - test logique `≤`{.language-}
  - gestion du `tant que`{.language-}
- ligne 7 : 9 instructions
  - 2 créations d'entiers (l'entier 1 et 2)
  - 3 récupérations de la variable `i`{.language-}
  - 2 opérations `-`{.language-}
  - 1 opération `+`{.language-}
  - 1 affectation
- ligne 8 : 4 instructions
  - 1 création de l'entier 1
  - 1 récupération de la variable `i`{.language-}
  - 1 opération `+`{.language-}
  - 1 affectation
- ligne 9 : 0 instructions
- ligne 10 : 2 instructions
  - 1 récupération de l'objet associé à `F[9]`{.language-}
  - 1 instruction `rendre`{.language-}

Comme les lignes 6 à 8 sont exécutées 8 fois, on en conclut que la complexité est :

<div>
$$
2+2+2+0+2 + 8\cdot(4 + 9 + 4) + 0 + 2 = 10 + 8 \cdot 17 = 144
$$
</div>

{% enddetails %}

Mais souvent la complexité dépend des paramètres du programme, comme par exemple le pseudo-code suivant qui rend la $n$ème valeur de la suite de Fibonacci où $n$ est le paramètre de l'algorithme :

```pseudocode/
algorithme fibonacci(n: entier) → entier:
  F ← un tableau de n entiers
  F[0] ← 1
  F[1] ← 1

  i ← 2
  tant que i < n :
    F[i] ← F[i - 1] + F[i - 2]    
    i ← i + 1

  rendre F[n-1]
```

Le nombre de fois où l'on rentre dans la boucle va dépendre de l'entrée et on a maintenant une complexité de $C(n) = 17\cdot n-20$ qui dépend de la valeur du paramètre d'entrée.

{% exercice %}
Montrez que la complexité est bien de $17\cdot n-20$
{% endexercice %}
{% details "corrigé" %}
Il y a deux différences :

- il faut affecter un objet au paramètre $n$ : 1 instruction supplémentaire
- on ne rentre plus 8 fois dans la boucle mais $n-2$ fois
- la case de retour n'est plus une constante mais dépend d'un calcul ($n-1$) : 3 instructions supplémentaires

La complexité est alors :

<div>
$$
1 +2+2+2+0+2 + (n-2)\cdot(4 + 9 + 4) + 0 + 3 + 2 = 14 + (n-2) \cdot 17 = 17\cdot n-20
$$
</div>

{% enddetails %}

Enfin, en règle générale, la complexité dépend trop profondément de la nature même de ses entrées et empêche d'en tirer une allure générale. Par exemple l'algorithme suivant qui cherche si une valeur `v`{.language-} est dans un tableau `T`{.language-} :

```pseudocode/
algorithme recherche(T: [entier], x: entier) → booléen:
    pour chaque e de T:
        si e == x:
            rendre Vrai
    rendre Faux
```

La complexité de cet algorithme va dépendre de l'endroit où se trouve la valeur dans le tableau. Si l'on utilise la taille $n$ du tableau comme paramètre de complexité, sa complexité ira de 10 lorsque la valeur est le premier élément du tableau (les deux affectations des paramètres ; trouver `t[0]`{.language-} puis l'affecter à `e`{.language-} ; deux lectures, une opération booléenne et un test ; une création d'objet puis un retour) à $6n + 4$ si la valeur n'est pas dans le tableau (les deux affectations des paramètres ; $2n$ instruction de l'affectation de la boucle `pour chaque`{.language-} ; $2n$ lectures, $n$ opérations booléennes et $n$ tests ; une création d'objet puis un retour). La complexité de l'algorithme est alors $C(i) = 6i + 4$ où $i$ est la position de la valeur dans le tableau.

Lorsque l'on utilise un algorithme on a jamais beaucoup de connaissances _a priori_ sur ses entrées. Pour l'algorithme `rechercher`{.language-} on sait que l'on a un entier et un tableau en paramètre mais pas la natures des entiers contenus dans le tableau. Avoir une complexité qui dépend des valeurs contenues dans le tableau est donc inutile en pratique. Il serait pus intéressant de connaître la complexité de l'algorithme pour un tableau d'une taille donnée. Dans ce cas là on calculera la complexité maximale pour tous les tableaux de même taille.

{% note %}
On calcule la complexité d'un algorithme par rapport à un paramètre qui rend compte de la connaissance _a priori_ que l'on a sur les entrées de celui-ci.
{% endnote %}

### Connaissances minimales sur les entrées

Les connaissances minimales que l'on possède sur les données sont leurs tailles de stockage en mémoire.

{% note "**Définition**" %}

**_la taille des entrées d'un algorithme_** est le nombre de cases mémoires nécessaires pour stocker toutes ses entrées.
{% endnote %}

Dans la partie pseudo-code on a considéré deux types de données :

- les types simples que sont les nombres et les caractères qui sont stockable sur 1 case mémoire
- les tableaux dont la taille est la somme des tailles de leurs éléments

### Complexité algorithmique

En prenant en compte les connaissances minimales que l'on a sur les entrées d'un algorithme, sa complexité est définie comme suit :

<div id="complexité"></div>
{% note "**Définition**" %}

**_La complexité_** $C(N)$ d'un algorithme $A(p_1, \dots, p_m)$ est le nombre maximum d'instructions élémentaires effectuées pour exécuter l'algorithme $A$ avec des entrées dont la taille vaut $N$.
{% endnote %}

En utilisant la définition ci-dessus, la complexité de l'algorithme `recherche`{.language-} vaut $6N+4$.

Comme rien n'est jamais simple, il existe des cas où la connaissance de la taille ne done pas un critère pertinent pour établir une complexité. C'est souvent le cas lorsque les paramètres de l'algorithmes sont de taille fixe, comme pour la fonction `fibonacci(n)`{.language-}, la taille de stockage d'un entier étant de 1 case mémoire.

Si l'on avait calculé la complexité en regroupant les entrées par taille, on aurait eu qu'une seule classe d'entrée et la complexité aurait été infinie... Il a donc fallu supposer que l'on connaissait la valeur de l'entrée pour calculer une complexité finie.

Il n'y a pas de règle immuable dans le choix des connaissances que l'on s'accorde sur les paramètres, mais ne vous inquiétez pas, cela ressortira immédiatement du calcul. En revanche, comme la nature du paramètre peut changer :

{% note %}
Lorsque l'on donne une complexité en fonction d'un paramètre, il faut :

- obligatoirement l'**expliciter** (taille de données, valeur d'une entrée, etc)
- s'assurer que l'on peut calculer ce paramètre pour **toutes les entrées**
- ne pas oublier que la complexité est le **maximum** du nombre d'instructions pour les exécutions de l'algorithme avec des entrées de paramètre constant (même taille de donnée, même valeur d'entrée, etc)
  {% endnote %}

## Autres types de complexités

Lorsque l'on parle de complexité d'un algorithme ce sera toujours en utilisant la définition précédente. Il existe cependant d'autres types de complexité que l'on pourra utiliser.

## Complexité min

Lorsqu'à paramètre fixé le nombre d'instructions varie selon les paramètres utilisé (l'algorithme `recherche`{.language-} par exemple), la complexité prend le maximum ($6N+4$ où $N$ est la la taille du tableau en entrée pour l'algorithme `recherche`{.language-}) mais il peut être utile de connaître le minimum ($10$ pour l'algorithme `recherche`{.language-}, indépendant de la taille du tableau en entrée) pour voir la variation de ce nombre en fonction des entrées.

{% note "**Définition**" %}

**_La complexité minimum_** $C_{\min}(N)$ d'un algorithme $A(p_1, \dots, p_m)$ est le nombre minimum d'instructions élémentaires effectuées pour exécuter l'algorithme $A$ avec des entrées dont la taille vaut $N$.
{% endnote %}

## <span id="complexité-temps"></span>Complexité en temps

Lorsqu'un algorithme est codé, on peut l'exécuter et mesurer son temps d'exécution. On peut alors définir la **_complexité en temps_** d'exécution d'un code :
{% note "**Définition**" %}

**_La complexité en temps_** $T(N)$ d'un algorithme $A(p_1, \dots, p_m)$ est le temps maximum pris pour exécuter le code $A$ avec des entrées dont la taille vaut $N$.
{% endnote %}

Si chaque instruction élémentaire prend le même temps à être effectuée sur une machine (ou que l'on borne le tout par l'instruction élémentaire la plus gourmande), la complexité d'un pseudo-code nous donne un nombre proportionnel au temps qu'il mettra à s'exécuter :

{% note %}
Le temps mis pour un code à être exécuté est proportionnelle à la complexité de son pseudo-code associé.
{% endnote %}

Si l'on connaît le jeu de paramètres d'entrée réalisant la complexité $C(N)$ d'un algorithme, on peut alors exécuter le code qui lui est associé et mesurer son temps d'exécution pour tracer la courbe de la complexité.

## Complexité spatiale

Enfin, L'autre paramètre utile que l'on mesure est le nombre de cases mémoires utilisées par l'algorithme, c'est à dire la taille des variables dont il a eu besoin pour fonctionner.

<div id="complexité-spatiale"></div>
{% note "**Définition**" %}

**_La complexité spatiale_** $S(N)$ d'un algorithme $A(p_1, \dots, p_m)$ (aussi appelée **_complexité en mémoire_**) est le nombre maximum de cases mémoires utilisées (lues ou modifiées) pendant l'exécution de l'algorithme $A$ avec des entrées dont la taille vaut $N$.

On **ne compte pas** dans ce calcul la taille nécessaire pour stocker les différents paramètres de l'algorithme.
{% endnote %}

Par exemple notre fonction `fibonacci(n)`{.language-} nécessite $n+2$ cases mémoires, en plus de ses paramètres, pour fonctionner :

- 1 case mémoire pour le stockage du paramètre $n$
- $n$ cases pour le tableau
- 1 case pour le stockage de l'entier $i$

Comparez avec l'algorithme suivant qui calcule aussi le $n$ème élément de la suite de Fibonacci :

```pseudocode/
algorithme fibonacci_sobre(n):
  F ← un tableau de n entiers
  a ← 1
  b ← 1

  i ← 2
  tant que i < n :
    c ← a + b
    a ← b
    b ← c
    
    i ← i + 1

  rendre b
```

Il demande beaucoup moins de mémoire, 5 cases mémoires seulement (pour stocker le paramètre $n$ et les 4 variables $a$, $b$, $c$ et $i$), ce qui lui permet de calculer de grandes valeurs de la suite de Fibonacci, plus grande que la taille mémoire de l'ordinateur qui exécutera le code associé.

{% info %}
Ce n'est pas le cas ici mais souvent, lors du design de nos algorithmes, on aura le choix entre entre consommer beaucoup de mémoire et être sobre en instructions ou le contraire.
{% endinfo %}

Complexité et complexité spatiale sont liées puisque chaque affectation d'une variable prend une instruction :

{% note "**Proposition**" %}
La complexité spatiale est toujours inférieure à la complexité.
{% endnote %}

On peut même avoir un encadrement plus précis :

{% note "**Proposition**" %}
Pour tout algorithme $A(p_1, \dots, p_m)$ dont la taille des entrées vaut $N$ et de complexités $C(N)$ (sa complexité en ombre d'instructions) et $S(N)$ (sa complexité spatiale), on a l'encadrement :

<div>
$$
S(N) \leq C(N) \leq L \cdot 2^{S(N)}
$$
</div>

Avec $L$ le nombre de lignes de l'algorithme.
{% endnote%}
{% details "preuve", "open" %}

On sait déjà que $S(n) \leq C(n)$.

Si une même ligne est exécutée deux fois avec la même composition de la mémoire, l'algorithme va boucler infiniment. Une même instruction ne peut donc être exécutée au maximum que $2^{S(n)}$ fois qui correspond aux nombre maximum de positions de la mémoire.

{% enddetails %}
