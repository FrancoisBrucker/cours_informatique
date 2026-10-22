---
layout: layout/post.njk

title: Définitions

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

On appelle complexité le nombre d'instructions basiques utilisé pour exécuter un pseudo-code. La complexité est proportionnelle au temps mis pour l'exécuter en supposant que que toutes les instructions basiques prennent le même temps (au pire on prend le temps max).

{% retenir %}
La complexité d'un pseudo-code est le nombre d'instructions qu'il effectue lors de son exécution.
{% endretenir %}

Considérons par exemple le pseudo-code suivant :

```pseudocode/
ref age int
age ← 16
si ((age ≥ 12) ET (age < 18)):
    affiche "Tu es un adolescent."
```

Si on compte le nombre d'instructions utilisées pour son exécution : 

- première ligne : 1 instruction, création de la variable `age`{.language-}, 
- deuxième ligne : 2 instructions
  1. Création de l'entier valant 16 : 1 instruction
  2. on affecte l'entier à la variable `age`{.language-} : 1 instruction
- troisième ligne : 8 instructions
  1. faire `age ≥ 12`{.language-}. Pour cela :
     - on crée l'entier valant 12 : 1 instruction
     - on récupère la valeur de `age`{.language-} : 1 instruction
     - on effectue la comparaison : 1 instruction
  2. faire `age < 18`{.language-}. Pour cela :
       - on crée l'entier valant 18 : 1 instruction
       - on récupère la valeur de `age`{.language-} : 1 instruction
       - on effectue la comparaison : 1 instruction
  3. faire l'instruction `ET`{.language-} : 1 instruction
  4. faire l'instruction `si`{.language-} : 1 instruction
- troisième ligne : 2 instructions
  1. on crée la chaîne : 1 instruction
  2. puis affiche le résultat : 1 instruction

Sa complexité vaut le nombre total d'instructions, c'est à dire 13.

## Complexité d'un pseudo-code

La notion d'instruction à effectuer dépend du pseudo-code utilisé. On verra plus tard un moyen radical de simplifier la définition (temps constant vs temps dépendant de paramètres) mais pour l'instant on va supposer qu'un instruction élémentaire correspond à celles que l'on a donné lorsque l'on a [défini le pseudo-code](../../../1-algorithme/pseudo-code/briques-de-base) :

- création d'une variable ou d'un objet
- affectation d'une variable
- trouver l'objet associé à une variable
- un test ou une opération arithmétique entre 2 objets
- l'affichage d'un objet à l'écran

### Boucles

On compte bien toutes les instructions et pas seulement ceux qui le constitue, donc pour le pseudo-code suivant :

```pseudocode/
ref message ← "j'aime me répéter"
ref i ← 1
tant que i ≤ 10000:
    affiche message
    i ← i + 1
```

Chaque ligne va prendre  :

- 3 instructions pour la première ligne : création de variable, de la chaîne et son affectation
- 3 instructions pour la deuxième ligne : création de variable, de la chaîne et son affectation
- 4 instructions pour la troisième ligne : recherche de la variable, création de l'entier,  test et saut si nécessaire
- 2 instructions pour la quatrième ligne : recherche de la variable et affichage
- 4 instructions pour la quatrième ligne : recherche de la variable, création de l'entier,  addition et affectation

Mais comme les lignes 4, et 5 sont exécutées 10000 fois et la ligne 3 10001 fois (ne pas oublier le test final lorsque $i > 10000$), la complexité du pseudo-code vaut :

<div>
$$
3 + 3 + 4 \cdot 10001 + (2+4) \cdot 10000 = 100010
$$
</div>

{% retenir %}
Lorsque l'on calcule la complexité d'un pseudo-code utilisant des boucles, il faut multiplier le nombre d'instructions de chaque ligne par le nombre de fois où elle a été exécutée.
{% endretenir %}

### Utilisation de tableaux

Combien d'instructions nécessitent la création et l'accès à un tableau ?

La création d'un objet de type tableau revient à créer autant de variables qu'il a d'indices puisqu'il faut mettre toutes ses valeurs à `∅`{.language-} (aucun objet n'est encore associé aux valeurs du tableau). Ainsi, dans notre modèle de pseudo-code, la création d'un tableau prend autant d'instructions que sa longueur.

{% info %}
On verra bien plus tard un autre modèle de pseudo-code où les variables ne sont pas initialisées par défaut, la complexité de création d'un objet tableau sera alors différente.
{% endinfo %}

L'accès à un indice particulier du tableau est rapide et ne nécessite qu'une seule instruction. Ainsi :

- accéder à un indice donnée en lecture nécessite 1 instruction
- accéder à un indice donnée pour une affectation nécessite 1 instruction

De là l'instruction :

- créer une variable de type tableau nécessite  1 instruction
- créer un tableau de taille 42 nécessite  42 instructions
- `afficher F[3]`{.language-} nécessite 2 instructions : une pour retrouver l'objet associé à `F[3]`{.language-} et l'autre pour l'afficher (on accède au quatrième élément du tableau, d'indice valant 3, on n'a pas besoin de créer un entier valant 3)
- `F[3] ← 42`{.language-} nécessite aussi 2 instructions : une pour créer l'entier `42`{.language-} l'autre pour l'affecter au quatrième élément du tableau
- `F[i] ← 42`{.language-} nécessite en revanche 3 instructions, une pour créer l'entier `42`{.language-}, une pour trouver l'objet associé à `i`{.language-} (ce n'est pas une constante) l'autre pour l'affecter
- `F[i-1] ← 42`{.language-} nécessite 5 instructions, une pour créer l'entier `42`{.language-}, une pour trouver l'objet associé à `i`{.language-}, une pour créer l'entier 1, une pour l'addition et la dernière pour l'affectation.
- `F ← [1 .. 42]`{.language-} nécessite 127 instructions :
  -  42 pour la création de l'objet tableau de longueur 42
  -  42 pour la création des entiers  allant de 1 à 42
  -  42 pour l'affectation des entiers aux éléments du tableau
  -  1 pour l'affectation du tableau à la variable `F`{.language-} (que l'on suppose déjà créée)


{% retenir %}
Lorsque l'on utilise des tableaux ne confondez pas la création de la variable de type tableau (1 instruction) et la création d'un objet tableau qui, pour notre pseudo-code, prend autant d'instructions que sa longueur car on initialise chaque variable à `∅`{.language-}

Pour le reste accéder (en lecture ou en écriture) à une case du tableau prend 1 instruction si on connaît la case.
{% endretenir %}

### Appels de fonctions

La plupart du temps on utilise plus que les instructions basiques comme des fonctions que l'on suppose accessible (comme le min ou le max) ou des algorithmes que l'on a défini nous même. Il ne faut pas oublier d'ajouter leurs complexités au calcul.

{% retenir %}
Lorsque l'on calcule la complexité d'un pseudo-code utilisant des fonctions, il faut compter le nombre d'instructions de l'exécution des fonctions !
{% endretenir %}

Reprenons par exemple [le code de l'algorithme recherche](../../../1-algorithme/pseudo-code/algorithmes-fonctions/#algorithme-recherche) et comptons les instructions utilisées au cours de l'exécution du code suivant :

```pseudocode/
fonction recherche(T: []int, x: int) → bool:
    pour chaque e de T:
        si e == x:
            rendre Vrai
    rendre Faux

ref T []int
T ← [1, 2, 6]
ref trouve int
trouve ← recherche(T, 6)
affiche trouve
```

1. exécution de la ligne 7 : 1 instructions ; création d'une variable tableau
2. exécution de la ligne 8 : 10 instructions
   - création et initialisation à `∅`{.language-} d'un tableau à 3 indices 
   - création de 3 entiers : 3 instructions
   - affectation des 3 entiers aux indices du tableau :  3 instructions
   - affectation du tableau à une variable : 1 instruction
3. exécution de la ligne 9 : 1 instructions ; création d'une variable
4. exécution de la ligne 10 :
   1. exécution de la fonction recherche (ligne à ligne) :
      1. exécution de la ligne 1 : affectation des paramètres
         1. trouver les objets à mettre en paramètres :
            - pour le premier paramètre il faut trouver l'objet associé à t : 1 instruction
            - pour le second paramètre, l'objet est à créer : 1 instruction
         2. affecter les paramètres aux variables de la fonction :
            - affectation du premier paramètre à la variable locale `t`{.language-} : 1 instruction
            - affectation du second paramètre à la variable locale `x`{.language-} : 1 instruction
      2. exécution de la ligne 2 (3 fois)
         1. uniquement la première fois : on crée la variable `e`{.language-} ; 1 instruction
         2. les 3 fois : trouver l'objet du tableau puis l'affecter à `e`{.language-} ; $2$ instructions 
      3. exécution de la ligne 3 (3 fois) : un test
         - on trouve les objets associées à `t`{.language-} et `e`{.language-} : 2 instructions
         - on teste l'égalité : 1 instruction
         - on fait le `si`{.language-} : 1 instruction
      4. exécution de la ligne 4 (1 fois) : on arrive à cette ligne à la troisième itération : 2 instructions (une pour créer le booléen, l'autre pour le rendre)
   2. affection de la variable `trouve`{.language-} : 1 instruction
5. afficher quelque chose à l'écran :
   - 1 instruction pour trouver l'objet à afficher
   - 1 instruction pour trouver l'afficher

Au total on eu besoin de $1+10+1+\underbracket{(4 + 1 + 3 \cdot (4+4) + 2)}_{\mbox{recherche(t, 6)}} + 1 + 2$
instructions c'est à dire $46$ instructions.

## Complexité d'un algorithme

Le pseudo-code suivant, qui calcule la dixième valeur de la suite de Fibonacci a une complexité $C = 159$ :

```pseudocode/
ref F []int
F ← [10]int
F[0] ← 1
F[1] ← 1

ref i ← 2
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

- ligne 1 : 1 instructions
- ligne 2 : 10 instructions
- ligne 3 : 2 instructions (une création et une affectation)
- ligne 4 : 2 instructions (une création et une affectation)
- ligne 5 : 0 instruction
- ligne 6 : 3 instructions (une création de variable et d'un entier puis une affectation)
- ligne 7 : 4 instructions
  - création de l'entier 9
  - récupération de la variable `i`{.language-}
  - test logique `≤`{.language-}
  - gestion du `tant que`{.language-}
- ligne 8 : 9 instructions
  - 2 créations d'entiers (l'entier 1 et 2)
  - 3 récupérations de la variable `i`{.language-}
  - 2 opérations `-`{.language-}
  - 1 opération `+`{.language-}
  - 1 affectation
- ligne 9 : 4 instructions
  - 1 création de l'entier 1
  - 1 récupération de la variable `i`{.language-}
  - 1 opération `+`{.language-}
  - 1 affectation
- ligne 10 : 0 instructions
- ligne 11 : 2 instructions
  - 1 récupération de l'objet associé à `F[9]`{.language-}
  - 1 instruction `rendre`{.language-}

Comme la ligne 7 est exécutée 9 fois et les lignes 8 et 9 sont exécutées 8 fois, on en conclut que la complexité est :

<div>
$$
1+10+2+2+0+2 + 9 \cdot 4 + 8\cdot(9 + 4) + 0 + 2 =  159
$$
</div>

{% enddetails %}

Mais souvent on ne va pas utiliser juste un pseudo-code, on crée des algorithmes pour être utilisé avec différents objets, ou dans d'autres algorithmes. On ne cherche alors plus à calculer la complexité de l'exécution effective d'un pseudo-code mais de l'exécution potentielle d'un code selon ses paramètres.

Transformons le pseudo-code précédent en algorithme pour qu'il puisse calculer tous les fermes de la suite de Fibonacci et pas uniquement le 10ème :


```pseudocode/
algorithme fibonacci(n: int) → int:
    ref F []int
    F ← [n]int
    F[0] ← 1
    F[1] ← 1

    ref i ← 2
    tant que i < n :
        F[i] ← F[i - 1] + F[i - 2]    
        i ← i + 1

    rendre F[-1]
```

Le nombre de fois où l'on rentre dans la boucle va dépendre de l'entrée $n$ et on a maintenant une complexité de :

<div>
$$
\begin{align}
    C(n) &= 1+n+2+2+0+2 + (n-2 + 1) \cdot 4 +  (n-2)\cdot(9 + 4) + 0 + 2 \\
         &= 18\cdot n - 21
\end{align}
$$
</div>

Cependant, en règle générale, la complexité dépend trop profondément de la nature même de ses entrées pour empêcher d'en tirer une allure générale. Par exemple l'algorithme suivant qui cherche si une valeur `x`{.language-} est dans un tableau `T`{.language-} :

```pseudocode/
algorithme recherche(T: []int, x: int) → bool:
    pour chaque e de T:
        si e == x:
            rendre Vrai
    rendre Faux
```

La complexité de cet algorithme va dépendre de l'endroit où se trouve la valeur dans le tableau. Si l'on utilise la longueur $n$ du tableau comme paramètre de complexité, sa complexité ira de 11 lorsque la valeur est le premier élément du tableau (les deux affectations des paramètres `T`{.language-} et `x`{.language-} ; la création de `e`{.language-} ; trouver `t[0]`{.language-} puis l'affecter à `e`{.language-} ; deux lectures, une opération booléenne et un test ; une création d'objet puis un retour) à $6\cdot n + 5$ si la valeur n'est pas dans le tableau (les deux affectations des paramètres ; la création de `e`{.language-} ; $2n$ instruction de l'affectation de la boucle `pour chaque`{.language-} ; $2n$ lectures, $n$ opérations booléennes et $n$ tests ; une création d'objet puis un retour). La complexité de l'algorithme est alors $C(i) = 6i + 5$ où $i$ est la position de la valeur dans le tableau.

Lorsque l'on utilise un algorithme on a jamais beaucoup de connaissances _a priori_ sur ses entrées. Pour l'algorithme `rechercher`{.language-} on sait que l'on a un tableau et un entier en paramètres mais pas la nature des entiers contenus dans le tableau. Avoir une complexité qui dépend des valeurs contenues dans le tableau est donc inutile en pratique. Il est plus intéressant de connaître la complexité de l'algorithme pour un tableau d'une longueur donnée.


{% retenir %}
On calcule la complexité d'un algorithme par rapport à un paramètre qui rend compte de la connaissance _a priori_ que l'on a sur les entrées de celui-ci.
{% endretenir %}

### Connaissances minimales sur les entrées

Les connaissances minimales que l'on possède sur les données sont leurs tailles de stockage en mémoire.

{% definition %}

**_la taille des entrées d'un algorithme_** est le nombre de cases mémoires nécessaires pour stocker toutes ses entrées.
{% enddefinition %}

Dans la partie pseudo-code on a considéré deux types de données :

- les types simples que sont les nombres, les booléens, les approximation de réels et les caractères qui sont stockable sur 1 unité de mémoire,
- les tableaux et les chaînes de caractères dont la taille est leur longueur multiplié par la taille de leurs données.

### Complexité algorithmique

En prenant en compte les connaissances minimales que l'on a sur les entrées d'un algorithme, sa complexité est définie comme suit :

<div id="complexité"></div>
{% definition %}

**_La complexité_** $C(N)$ d'un algorithme $A$ est le nombre maximum d'instructions élémentaires effectuées pour exécuter l'algorithme $A$ pour des données de paramètre $N$.

{% enddefinition %}

En utilisant la définition ci-dessus, la complexité de l'algorithme `recherche`{.language-} vaut $6N+5$, en utilisant la longueur du tableau passé en entrée comme paramètre : pour tout tableau de longueur $N$ passé en paramètre, la complexité maximale est de $6N+5$ instructions.

Lorsque les données sont de taille fixe, on ne peut pas utiliser la taille prise par les données comme paramètre. C'est le cas de la fonction `fibonacci(n)`{.language-}, puisque pour nous la taille de stockage d'un entier sera toujours de 1. On peut alors souvent utiliser la valeur elle même des données comme paramètre, ce qui donne : pour des données de valeur $n$ la complexité de l'algorithme est de de $18n - 21$.

Il n'y a pas de règle immuable dans le choix des connaissances que l'on s'accorde sur les paramètres, mais ne vous inquiétez pas, cela ressortira immédiatement du calcul. En revanche, comme la nature du paramètre peut changer :

{% retenir %}
Lorsque l'on donne une complexité en fonction d'un paramètre, il faut :

- obligatoirement l'**expliciter** (taille des données, valeur d'une entrée, etc)
- s'assurer que l'on peut calculer ce paramètre pour **toutes les entrées**
- ne pas oublier que la complexité est le **maximum** du nombre d'instructions pour les exécutions de l'algorithme avec des entrées de paramètre constant (même taille de donnée, même valeur d'entrée, etc)

{% endretenir %}

## Autres types de complexités

Lorsque l'on parle de complexité d'un algorithme ce sera toujours en utilisant la définition précédente. Il existe cependant d'autres types de complexité que l'on pourra utiliser.

## Complexité min

Lorsqu'à paramètre fixé le nombre d'instructions varie selon les paramètres utilisé (l'algorithme `recherche`{.language-} par exemple), la complexité prend le maximum ($6N+5$ où $N$ est la la taille du tableau en entrée pour l'algorithme `recherche`{.language-}) mais il peut être utile de connaître le minimum ($10$ pour l'algorithme `recherche`{.language-}, indépendant de la taille du tableau en entrée) pour voir la variation de ce nombre en fonction des entrées.

{% definition %}

**_La complexité minimum_** $C_{\min}(N)$ d'un algorithme $A(p_1, \dots, p_m)$ est le nombre minimum d'instructions élémentaires effectuées pour exécuter l'algorithme $A$ avec des entrées de paramètre $N$.
{% enddefinition %}

## <span id="complexité-temps"></span>Complexité en temps

Lorsqu'un algorithme est codé, on peut l'exécuter et mesurer son temps d'exécution. On peut alors définir la **_complexité en temps_** d'exécution d'un code :

{% definition %}

**_La complexité temporelle_** $T(N)$ d'un algorithme $A(p_1, \dots, p_m)$ est le temps maximum pris pour exécuter le code $A$ avec des entrées de paramètre $N$.
{% enddefinition %}

Si chaque instruction élémentaire prend le même temps à être effectuée sur une machine (ou que l'on borne le tout par l'instruction élémentaire la plus gourmande), la complexité d'un pseudo-code nous donne un nombre proportionnel au temps qu'il mettra à s'exécuter :

{% retenir %}
Le temps mis pour un code à être exécuté est proportionnelle au nombre d'instructions exécutés de son pseudo-code associé, ce qui implique que la complexité en temps (le temps maximum) est proportionnelle à la complexité en nombre d'instructions (le nombre maximum d'instructions).
{% endretenir %}

Si l'on connaît le jeu de paramètres d'entrée réalisant la complexité $C(N)$ d'un algorithme, on peut alors exécuter le code qui lui est associé et mesurer son temps d'exécution pour tracer la courbe de la complexité.

## Complexité spatiale

Enfin, L'autre paramètre utile que l'on mesure est le nombre de cases mémoires utilisées par l'algorithme, c'est à dire la taille des variables dont il a eu besoin pour fonctionner.

<div id="complexité-spatiale"></div>
{% definition %}

**_La complexité spatiale_** $S(N)$ d'un algorithme $A(p_1, \dots, p_m)$ (aussi appelée **_complexité en mémoire_**) est le nombre maximum de cases mémoires utilisées (lues ou modifiées) pendant l'exécution de l'algorithme $A$ avec des entrées de paramètre $N$.

On **ne compte pas** dans ce calcul la taille nécessaire pour stocker les différents paramètres de l'algorithme.
{% enddefinition %}

Par exemple notre fonction `fibonacci(n)`{.language-} nécessite $n+2$ cases mémoires, en plus de ses paramètres, pour fonctionner :

- 1 case mémoire pour le stockage du paramètre $n$
- $n$ cases pour le tableau
- 1 case pour le stockage de l'entier $i$

Comparez avec l'algorithme suivant qui calcule aussi le $n$ème élément de la suite de Fibonacci :

```pseudocode/
algorithme fibonacci_sobre(n):
  ref a ← 1
  ref b ← 1
  ref c int

  ref i ← 2
  tant que i < n :
    c ← a + b
    a ← b
    b ← c
    
    i ← i + 1

  rendre b
```

Il demande beaucoup moins de mémoire, 4 cases mémoires seulement pour stocker les 4 variables ($a$, $b$, $c$ et $i$), sans compter le paramètre $n$, ce qui lui permet de calculer de grandes valeurs de la suite de Fibonacci, plus grande que la taille mémoire de l'ordinateur qui exécutera le code associé.

{% info %}
Ce n'est pas le cas ici mais souvent, lors du design de nos algorithmes, on aura le choix entre entre consommer beaucoup de mémoire et être sobre en instructions ou le contraire.
{% endinfo %}

Complexité et complexité spatiale sont liées :

{% note "**Proposition**" %}
Si toutes les variables définies sont affectées (cela inclut toutes les cases des objets de type tableau), la complexité spatiale est toujours inférieure à la complexité.
{% endnote %}
{% details "preuve", "open" %}

Chaque affectation d'une variable prend une instruction.

{% enddetails %}

On peut même avoir un encadrement plus précis :

{% note "**Proposition**" %}
Soit `A(p: []bit) → []bit`{.language} un algorithme ne manipulant en interne que des `[]bit`{.language}. Si sa complexité est en $C(N)$ avec $N$ la longueur de son paramètre et $S(N)$ sa complexité spatiale, on a l'encadrement :

<div>
$$
S(N) \leq C(N) \leq L \cdot 2^{S(N)}
$$
</div>

Avec $L$ le nombre de lignes de l'algorithme.
{% endnote%}
{% details "preuve", "open" %}

On sait déjà que $S(N) \leq C(N)$.

Si une même ligne est exécutée deux fois avec la même affectation des variables, l'algorithme va boucler infiniment. Une même instruction ne peut donc être exécutée au maximum que $2^{S(N)}$ fois qui correspond aux nombre maximum de valeurs différentes que peuvent prendre les $S(N)$ bits utilisés par l'algorithme.

{% enddetails %}

La proposition précédente est très générale puisqu'[on a vu](../../../1-algorithme/bases-théoriques/définition/#manipuler-01) que tout algorithme peut être écrit comme n'utilisant que des `[]bit`{.language}.
