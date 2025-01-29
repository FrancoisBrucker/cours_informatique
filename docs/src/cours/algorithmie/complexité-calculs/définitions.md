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

- **_complexité en temps_** : le nombre d'instruction effectuées pendant son exécution
- **_complexité en espace_** : le nombre de cases mémoires maximales utilisées pendant son exécution.

Par défaut, la complexité utilisée est celle en temps :

{% note "**Définition**" %}
La complexité d'un pseudo-code est la complexité en temps de celui-ci.
{% endnote %}

Par exemple le pseudo-code suivant :

```pseudocode/
x ← 30
si ((x > 12) ET (x < 36)):
    z ← "entre 13 et 35"
```

- première ligne : 2 instructions
  1. Création de l'entier valant 30 : 1 instruction
  2. on affecte l'entier à x : 1 instruction
- deuxième ligne : 8 instructions
  1. faire `x > 12`{.language-}. Pour cela :
     - on crée l'entier valant 12 : 1 instruction
     - on récupère la valeur de `x`{.language-} : 1 instruction
     - on effectue la comparaison : 1 instruction
  2. faire `x < 36`{.language-}. Pour cela :
       - on crée l'entier valant 36 : 1 instruction
       - on récupère la valeur de `x`{.language-} : 1 instruction
       - on effectue la comparaison : 1 instruction
  3. faire l'instruction `AND`{.language-} : 1 instruction
  4. faire le `si`{.language-} : 1 instruction
- troisième ligne : 2 instructions
  1. on crée la chaîne : 1 instruction
  2. puis affecte le résultat : 1 instruction

Un nombre total d'instructions de 12 pour ces trois lignes de pseudo-code.

## Complexité des appels de fonctions

Si l'on devait à chaque pseudo-code redéfinir tout les algorithmes qu'on utilise ce serait vraiment fastidieux. On utilise souvent des fonctions non basiques (comme l'affichage à l'écran qu'on a déjà vu) ou des structures plus élaborées (les listes par exemples qui sont des extensions des tableaux). Il faudra cependant toujours connaître les complexités de ce qu'on utilise.

{% attention %}
Lorsque l'on calcule la complexité d'un pseudo-code utilisant des fonctions, il faut compter le nombre d'instructions de l'exécution des fonctions !
{% endattention %}

Prenons par exemple le code suivant et comptons les instructions utilisées au cours de son exécution :

```pseudocode/
fonction recherche(t: [entier], x: entier):
    pour chaque e de t:
        si e == x:
            rendre Vrai
    rendre Faux

t ← [1, 2, 6]
trouve ← recherche(t, 6)
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

## Complexité des structures

Si l'on devait à chaque pseudo-code redéfinir tout les algorithmes qu'on utilise ce serait vraiment fastidieux. On utilise souvent des fonctions non basiques (comme l'affichage à l'écran qu'on a déjà vu) ou des structures plus élaborées (les listes de python par exemples qui sont des extensions des tableaux). Il faudra cependant toujours connaître les complexités de ce qu'on utilise.

Par exemple pour les listes de python, qui sont des tableaux redimensionnables, on admet pour l'instant (on les verra en détails plus tard) que les complexités sont :

- complexité d'ajout d'un élément à la fin de la liste : coût de 1 instruction
- complexité de l'ajout d'un élément pas à la fin de la liste : coût de la taille de la liste instructions
- complexité de la suppression d'un élément à la fin de la liste : coût de 1 instruction
- complexité de la suppression d'un élément pas à la fin de la liste : coût de la taille de la liste instructions
- usage comme un tableau : 1 instruction

Si vous utilisez des méthodes d'objets comme vous avez l'habitude de le faire en python (comme une `ma_liste.index("?")`{.language-}, `x in ma_chaîne_de_caractères`{.language-}) ou des structures compliquées (télécharger un fichier d'internet) vous avez le droit mais vous **devez** en connaître le coût : la complexité, les cas d'usage (comme être connecté à internet), etc.

## Complexité d'un algorithme

Le pseudo-code suivant, qui calcule la dixième valeur de la suite de Fibonacci a une complexité $C = 194$ :

```pseudocode/
F ← un tableau de 10 entiers
F[0] ← 1
F[1] ← 1

i ← 2
tant que i ≤ 9 :
  j ← i - 1
  k ← i - 2
  F[i] ← F[j] + F[k]
  
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
- ligne 7 : 4 instructions
  - création de l'entier 1
  - récupération de la variable `i`{.language-}
  - opération `-`{.language-}
  - affectation
- ligne 8 : 4 instructions
  - création de l'entier 2
  - récupération de la variable `i`{.language-}
  - opération `-`{.language-}
  - affectation
- ligne 9 : 7 instructions
  - récupération des variables `i`{.language-}, `j`{.language-} et `k`{.language-}
  - récupération des 2 cases du tableau
  - opération `+`{.language-}
  - affectation
- ligne 10 : 0 instruction
- ligne 11 : 4 instructions
- ligne 12 : 0 instruction
- ligne 13 : 2 instructions

Comme les lignes 6 à 11 sont exécutées 8 fois, on en conclut que la complexité est :

<div>
$$
2+2+2+0+2 + 8\cdot(4 + 4 + 4 + 7 + 0 + 4) + 0 + 2 = 10 + 8 \cdot 23 = 194
$$
</div>

{% enddetails %}

Mais souvent la complexité dépend des paramètres du programme, comme par exemple le pseudo-code suivant qui rend la $n$ème valeur de la suite de Fibonacci où $n$ est le paramètre de l'algorithme :

```text#
fonction fibonacci(n):
  F ← un tableau de n entiers
  F[0] ← 1
  F[1] ← 1

  i ← 2
  tant que i < n :
    j ← i - 1
    k ← i - 2
    F[i] ← F[j] + F[k]
    
    i ← i + 1

  rendre F[n-1]
```

Le nombre de fois où l'on rentre dans la boucle va dépendre de l'entrée et on a maintenant une complexité de $C(n) = 23\cdot n-32$ qui dépend de la valeur du paramètre d'entrée.

{% exercice %}
Montrez que la complexité est bien de $23\cdot n-32$
{% endexercice %}
{% details "corrigé" %}
Il y a deux différences :

- il faut affecter un objet au paramètre $n$
- on ne rentre plus 8 fois dans la boucle mais $n-2$ fois
- la case de retour n'est plus une constante mais dépend d'un calcul ($n-1$)

La complexité est alors : $1 + 10 + (n-2) \cdot 23 + 3 = 23\cdot n-32$.

{% enddetails %}

Enfin, en règle générale, la complexité dépend trop profondément de la nature même de ses entrées et empêche d'en tirer une allure générale. Par exemple l'algorithme suivant qui cherche si une valeur `v`{.language-} est dans un tableau `t`{.language-} :

```pseudocode/
algorithme recherche(t: [entier], x: entier):
    pour chaque e de t:
        si e == x:
            rendre Vrai
    rendre Faux
```

La complexité de cet algorithme va dépendre de l'endroit où se trouve la valeur dans le tableau. Si l'on utilise la taille $n$ du tableau comme paramètre de complexité, sa complexité ira de 9 lorsque la valeur est le premier élément du tableau (les deux affectations des paramètres ; une affectation de $x$ ; deux lectures, une opération booléenne et un test ; une création d'objet puis un retour) à $5n + 4$ si la valeur n'est pas dans le tableau (les deux affectations des paramètres ; $n$ affectations de $x$ ; deux $n$ lectures, $n$ opérations booléennes et $n$ tests ; une création d'objet puis un retour). La complexité de l'algorithme est alors $C(i) = 5i + 4$ où $i$ est la position de la valeur dans le tableau.

Lorsque l'on utilise un algorithme on a jamais beaucoup de connaissances _a priori_ sur ses entrées. Pour la fonction `est_dans_tableau`{.language-} on sait que l'on a un entier et un tableau en paramètre mais pas la natures des entiers contenus dans le tableau. Avoir une complexité qui dépend des valeurs contenues dans le tableau est donc inutile en pratique. Il serait pus intéressant de connaître la complexité de l'algorithme pour un tableau d'une taille donnée. Dans ce cas là on calculera la complexité maximale pour tous les tableaux de même taille.

{% note %}
On calcule la complexité d'un algorithme par rapport à un paramètre qui rend compte de la connaissance _a priori_ que l'on a sur les entrées de celui-ci.
{% endnote %}

### Connaissances minimales sur les entrées

Les connaissances minimales que l'on possède sur les données sont leurs tailles de stockage en mémoire.

{% note %}

**_la taille des entrées d'algorithme_** est le nombre de cases mémoires nécessaires pour les stocker.
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

En utilisant la définition ci-dessus, la complexité de l'algorithme `recherche`{.language-} vaut $5N+4$.

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

Lorsqu'à paramètre fixé le nombre d'instructions varie selon les paramètres utilisé (l'algorithme `recherche`{.language-} par exemple), la complexité prend le maximum ($5N+4$ où $N$ est la la taille du tableau en entrée pour l'algorithme `recherche`{.language-}) mais il peut être utile de connaître le minimum ($9$ pour l'algorithme `recherche`{.language-}, indépendant de la taille du tableau en entrée) pour voir la variation de ce nombre en fonction des entrées.

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

Sa complexité un peu plus élevée puisqu'il faut gérer les variables $a$, $b$ et $c$ mais reste comparable au premier.

{% info %}
Souvent, lors du design de nos algorithmes on aura le choix entre entre consommer beaucoup de mémoire et être sobre en instructions ou le contraire.
{% endinfo %}

Complexité et complexité spatiale sont liées puisque chaque affectation d'une variable prend une instruction :

{% note %}
La complexité spatiale est toujours inférieure à la complexité.
{% endnote %}
