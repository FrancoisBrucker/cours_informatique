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

{% note2 "**Définition**" %}
La complexité d'un pseudo-code est la complexité en temps de celui-ci.
{% endnote2 %}

Par exemple le pseudo-code suivant :

```pseudocode/
age := entier
age ← 16
si ((age ≥ 12) et (age < 18)):
    personne ← "adolescent"
```

- première ligne : 1 instruction, création de la variable `age`{.language-}, 
- deuxième ligne : 2 instructions
  1. Création de l'entier valant 42 : 1 instruction
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
  3. faire l'instruction `et`{.language-} : 1 instruction
  4. faire l'instruction `si`{.language-} : 1 instruction
- troisième ligne : 2 instructions
  1. on crée la chaîne : 1 instruction
  2. puis affecte le résultat : 1 instruction

Un nombre total d'instructions de 13 pour ces quatre lignes de pseudo-code.

## Complexité des appels de fonctions

Si l'on devait à chaque pseudo-code redéfinir tout les algorithmes qu'on utilise ce serait vraiment fastidieux. On utilise souvent des fonctions non basiques (comme l'affichage à l'écran qu'on a déjà vu) ou des structures plus élaborées (les listes par exemples qui sont des extensions des tableaux). Il faudra cependant toujours connaître les complexités de ce qu'on utilise.

{% attention %}
Lorsque l'on calcule la complexité d'un pseudo-code utilisant des fonctions, il faut compter le nombre d'instructions de l'exécution des fonctions !
{% endattention %}

Reprenons par exemple [le code de l'algorithme recherche](../../bases-théoriques/définition/#algorithme-recherche){.interne} et comptons les instructions utilisées au cours de son exécution :

```pseudocode/
fonction recherche(T: [entier], x: entier) → booléen:
    pour chaque (e := entier) de T:
        si e == x:
            rendre Vrai
    rendre Faux

T := [entier] 
T ← [1, 2, 6]
trouve := entier
trouve ← recherche(T, 6)
affiche à l'écran trouve
```

1. exécution de la ligne 7 : 1 instructions ; création d'une variable tableau
2. exécution de la ligne 8 : 7 instructions
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

Au total on eu besoin de $1+7+1+\underbracket{(4 + 1 + 3 \cdot (4+4) + 2)}_{\mbox{recherche(t, 6)}} + 1 + 2$
instructions c'est à dire $43$ instructions.

## Complexité des accès à un tableau ?

Combien d'instructions nécessitent la création et l'accès à un tableau ?

On considérera en algorithmie que tous les accès à un élément donné d'un tableau nécessite 1 instruction. Ainsi :

- créer un tableau de taille $n$ nécessite 1 instruction
- accéder à un indice donnée en lecture nécessite 1 instruction
- accéder à un indice donnée pour une affectation nécessite 1 instruction

De là l'instruction :

- créer un tableau de taille 42 nécessite  1 instruction
- créer un tableau de taille $2^{42}$ nécessite  1 instruction
- `afficher à l'écran F[3]`{.language-} nécessite 2 instructions, une pour retrouver l'objet associé à `F[3]`{.language-}, l'autre pour l'afficher
- `F[3] ← 42`{.language-} nécessite 2 instructions, une pour créer l'entier `42`{.language-}, l'autre pour l'affecter
- `F[i] ← 42`{.language-} nécessite 3 instructions, une pour créer l'entier `42`{.language-}, une pour trouver l'objet associé à `i`{.language-} (ce n'est pas une constante) l'autre pour l'affecter
- `F[i-1] ← 42`{.language-} nécessite 5 instructions, une pour créer l'entier `42`{.language-}, une pour trouver l'objet associé à `i`{.language-}, une pour créer l'entier 1, une pour l'addition et la dernière pour l'affectation.
- `F ← [1 .. 42]`{.language-} nécessite 86 instructions :
  -  1 pour la création de l'objet tableau de longueur 42
  -  42 pour la création des entiers  allant de 1 à 42
  -  42 pour l'affectation des entiers aux éléments du tableau
  -  1 pour l'affectation du tableau à la variable `F`{.language-} (que l'on suppose déjà créée)


## Complexité d'un algorithme

Le pseudo-code suivant, qui calcule la dixième valeur de la suite de Fibonacci a une complexité $C = 144$ :

```pseudocode/
F := [entier]
F ← [entier]{longueur: 10}
F[0] ← 1
F[1] ← 1

i := 2
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
- ligne 2 : 1 instructions
- ligne 3 : 2 instructions (une création et une affectation)
- ligne 4 : 2 instructions (une création et une affectation)
- ligne 5 : 0 instruction
- ligne 6 : 2 instructions (une création et une affectation)
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
  F := [entier]
  F ← [entier]{longueur: n}
  F[0] ← 1
  F[1] ← 1

  i := 2
  tant que i < n :
    F[i] ← F[i - 1] + F[i - 2]    
    i ← i + 1

  rendre F[n-1]
```

Le nombre de fois où l'on rentre dans la boucle va dépendre de l'entrée et on a maintenant une complexité de $C(n) = 17\cdot n-19$ qui dépend de la valeur du paramètre d'entrée.

{% exercice %}
Montrez que la complexité est bien de $17\cdot n-19$
{% endexercice %}
{% details "corrigé" %}
Il y a plusieurs différences :

- il faut affecter un objet au paramètre $n$ : 1 instruction supplémentaire
- il faut trouver la valeur de $n$ pour la création du tableau (ce n'est plus une constante) : 1 instruction supplémentaire
- on ne rentre plus 8 fois dans la boucle mais $n-2$ fois
- la case de retour n'est plus une constante mais dépend d'un calcul ($n-1$) : 3 instructions supplémentaires

La complexité est alors :

<div>
$$
1 + 1+ +2+2+2+0+2 + (n-2)\cdot(4 + 9 + 4) + 0 + 3 + 2 = 14 + (n-2) \cdot 17 = 17\cdot n-19
$$
</div>

{% enddetails %}

Enfin, en règle générale, la complexité dépend trop profondément de la nature même de ses entrées et empêche d'en tirer une allure générale. Par exemple l'algorithme suivant qui cherche si une valeur `v`{.language-} est dans un tableau `T`{.language-} :

```pseudocode/
algorithme recherche(T: [entier], x: entier) → booléen:
    pour chaque (e := entier) de T:
        si e == x:
            rendre Vrai
    rendre Faux
```

La complexité de cet algorithme va dépendre de l'endroit où se trouve la valeur dans le tableau. Si l'on utilise la taille $n$ du tableau comme paramètre de complexité, sa complexité ira de 11 lorsque la valeur est le premier élément du tableau (les deux affectations des paramètres ; la création de `e`{.language-} ; trouver `t[0]`{.language-} puis l'affecter à `e`{.language-} ; deux lectures, une opération booléenne et un test ; une création d'objet puis un retour) à $6n + 5$ si la valeur n'est pas dans le tableau (les deux affectations des paramètres ; la création de `e`{.language-} ; $2n$ instruction de l'affectation de la boucle `pour chaque`{.language-} ; $2n$ lectures, $n$ opérations booléennes et $n$ tests ; une création d'objet puis un retour). La complexité de l'algorithme est alors $C(i) = 6i + 5$ où $i$ est la position de la valeur dans le tableau.

Lorsque l'on utilise un algorithme on a jamais beaucoup de connaissances _a priori_ sur ses entrées. Pour l'algorithme `rechercher`{.language-} on sait que l'on a un entier et un tableau en paramètre mais pas la natures des entiers contenus dans le tableau. Avoir une complexité qui dépend des valeurs contenues dans le tableau est donc inutile en pratique. Il serait pus intéressant de connaître la complexité de l'algorithme pour un tableau d'une taille donnée. Dans ce cas là on calculera la complexité maximale pour tous les tableaux de même taille.

{% attention2 "**À retenir**" %}
On calcule la complexité d'un algorithme par rapport à un paramètre qui rend compte de la connaissance _a priori_ que l'on a sur les entrées de celui-ci.
{% endattention2 %}

### Connaissances minimales sur les entrées

Les connaissances minimales que l'on possède sur les données sont leurs tailles de stockage en mémoire.

{% note2 "**Définition**" %}

**_la taille des entrées d'un algorithme_** est le nombre de cases mémoires nécessaires pour stocker toutes ses entrées.
{% endnote2 %}

Dans la partie pseudo-code on a considéré deux types de données :

- les types simples que sont les nombres et les caractères qui sont stockable sur 1 case mémoire,
- les tableaux dont la taille est leur longueur multiplié par la taille d'une de ses données.

### Complexité algorithmique

En prenant en compte les connaissances minimales que l'on a sur les entrées d'un algorithme, sa complexité est définie comme suit :

<div id="complexité"></div>
{% note2 "**Définition**" %}

**_La complexité_** $C(N)$ d'un algorithme $A(p_1, \dots, p_m)$ est le nombre maximum d'instructions élémentaires effectuées pour exécuter l'algorithme $A$
pour des données de paramètre $N$.

{% endnote2 %}

En utilisant la définition ci-dessus, la complexité de l'algorithme `recherche`{.language-} vaut $6N+5$, en utilisant la taille du tableau passé en entrée comme paramètre : pour tout tableau de longueur $N$ passé en paramètre, la complexité maximale est de $6N+5$ instructions.

Lorsque les données sont de taille fixe, on ne peut pas utiliser la taille prises par les données comme paramètre. C'est le cas de la fonction `fibonacci(n)`{.language-}, puisque pour nous la taille de stockage d'un entier sera toujours de 1. On peut alors souvent utiliser la valeur elle même des données comme paramètre, ce qui donne : pour des données de valeur $n$ la complexité de l'algorithme est de de $17n -19$.

Il n'y a pas de règle immuable dans le choix des connaissances que l'on s'accorde sur les paramètres, mais ne vous inquiétez pas, cela ressortira immédiatement du calcul. En revanche, comme la nature du paramètre peut changer :

{% attention2 "**À retenir**" %}
Lorsque l'on donne une complexité en fonction d'un paramètre, il faut :

- obligatoirement l'**expliciter** (taille des données, valeur d'une entrée, etc)
- s'assurer que l'on peut calculer ce paramètre pour **toutes les entrées**
- ne pas oublier que la complexité est le **maximum** du nombre d'instructions pour les exécutions de l'algorithme avec des entrées de paramètre constant (même taille de donnée, même valeur d'entrée, etc)

{% endattention2 %}

## Autres types de complexités

Lorsque l'on parle de complexité d'un algorithme ce sera toujours en utilisant la définition précédente. Il existe cependant d'autres types de complexité que l'on pourra utiliser.

## Complexité min

Lorsqu'à paramètre fixé le nombre d'instructions varie selon les paramètres utilisé (l'algorithme `recherche`{.language-} par exemple), la complexité prend le maximum ($6N+5$ où $N$ est la la taille du tableau en entrée pour l'algorithme `recherche`{.language-}) mais il peut être utile de connaître le minimum ($10$ pour l'algorithme `recherche`{.language-}, indépendant de la taille du tableau en entrée) pour voir la variation de ce nombre en fonction des entrées.

{% note2 "**Définition**" %}

**_La complexité minimum_** $C_{\min}(N)$ d'un algorithme $A(p_1, \dots, p_m)$ est le nombre minimum d'instructions élémentaires effectuées pour exécuter l'algorithme $A$ avec des entrées de paramètre $N$.
{% endnote2 %}

## <span id="complexité-temps"></span>Complexité en temps

Lorsqu'un algorithme est codé, on peut l'exécuter et mesurer son temps d'exécution. On peut alors définir la **_complexité en temps_** d'exécution d'un code :
{% note2 "**Définition**" %}

**_La complexité en temps_** $T(N)$ d'un algorithme $A(p_1, \dots, p_m)$ est le temps maximum pris pour exécuter le code $A$ avec des entrées de paramètre $N$.
{% endnote2 %}

Si chaque instruction élémentaire prend le même temps à être effectuée sur une machine (ou que l'on borne le tout par l'instruction élémentaire la plus gourmande), la complexité d'un pseudo-code nous donne un nombre proportionnel au temps qu'il mettra à s'exécuter :

{% attention2 "**À retenir**" %}
Le temps mis pour un code à être exécuté est proportionnelle au nombre d'instructions exécutés de son pseudo-code associé, ce qui implique que la complexité en temps (le temps maximum) est proportionnelle à la complexité en nombre d'instructions (le nombre maximum d'instructions).
{% endattention2 %}

Si l'on connaît le jeu de paramètres d'entrée réalisant la complexité $C(N)$ d'un algorithme, on peut alors exécuter le code qui lui est associé et mesurer son temps d'exécution pour tracer la courbe de la complexité.

## Complexité spatiale

Enfin, L'autre paramètre utile que l'on mesure est le nombre de cases mémoires utilisées par l'algorithme, c'est à dire la taille des variables dont il a eu besoin pour fonctionner.

<div id="complexité-spatiale"></div>
{% note2 "**Définition**" %}

**_La complexité spatiale_** $S(N)$ d'un algorithme $A(p_1, \dots, p_m)$ (aussi appelée **_complexité en mémoire_**) est le nombre maximum de cases mémoires utilisées (lues ou modifiées) pendant l'exécution de l'algorithme $A$ avec des entrées de paramètre $N$.

On **ne compte pas** dans ce calcul la taille nécessaire pour stocker les différents paramètres de l'algorithme.
{% endnote2 %}

Par exemple notre fonction `fibonacci(n)`{.language-} nécessite $n+2$ cases mémoires, en plus de ses paramètres, pour fonctionner :

- 1 case mémoire pour le stockage du paramètre $n$
- $n$ cases pour le tableau
- 1 case pour le stockage de l'entier $i$

Comparez avec l'algorithme suivant qui calcule aussi le $n$ème élément de la suite de Fibonacci :

```pseudocode/
algorithme fibonacci_sobre(n):
  (a := entier) ← 1
  (b := entier) ← 1
  c := entier

  (i := entier) ← 2
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
Si toutes les variables définies sont affectées (cela inclut toutes les cases des objets de type tableau), la complexité spatiale est toujours inférieure à la complexité 
{% endnote %}
{% details "preuve", "open" %}

Chaque affectation d'une variable prend une instruction.

{% enddetails %}


On peut même avoir un encadrement plus précis :

{% note "**Proposition**" %}
Soit $A(p_1, \dots, p_m)$ un algorithme ne manipulant que des tableaux de bits et affectant toutes ses variables.

Si sa complexité est en $C(N)$ et sa complexité spatiale en $S(N)$, on a l'encadrement :

<div>
$$
S(N) \leq C(N) \leq L \cdot 2^{S(N)}
$$
</div>

Avec $L$ le nombre de lignes de l'algorithme.
{% endnote%}
{% details "preuve", "open" %}

On sait déjà que $S(n) \leq C(n)$.

Si une même ligne est exécutée deux fois avec la même affectation des variables, l'algorithme va boucler infiniment. Une même instruction ne peut donc être exécutée au maximum que $2^{S(n)}$ fois qui correspond aux nombre maximum de valeurs différentes que peuvent prendre les $S(N)$ bits utilisés par l'algorithme.

{% enddetails %}
