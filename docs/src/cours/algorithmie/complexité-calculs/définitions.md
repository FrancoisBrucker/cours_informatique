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

```text#
x = 30
if ((x > 12) AND (x < 36)):
    z = "entre 13 et 35"
```

1. Création de l'entier valant 30 : 1 instruction
2. on affecte l'entier à x : 1 instruction
3. Pour faire cette instruction il faut :
   - faire `x > 12`{.language-}. Pour cela :
     - on crée l'entier valant 12 : 1 instruction
     - on récupère la valeur de `x`{.language-} : 1 instruction
     - on effectue la comparaison : 1 instruction
   - faire `x < 36`{.language-}. Pour cela :
     - on crée l'entier valant 36 : 1 instruction
     - on récupère la valeur de `x`{.language-} : 1 instruction
     - on effectue la comparaison : 1 instruction
   - faire l'instruction `AND`{.language-} : 1 instruction
   - faire le `if`{.language-} : 1 instruction
4. on commence par récupérer la valeur de `x`{.language-} (1 instruction), on crée la chaîne (1 instruction) puis affecte le résultat d'une opération élémentaire (2 instructions) : donc un total de 4 instructions

Un nombre total d'instructions de 14.

## Complexité des appels de fonctions

Si l'on devait à chaque pseudo-code redéfinir tout les algorithmes qu'on utilise ce serait vraiment fastidieux. On utilise souvent des fonctions non basiques (comme l'affichage à l'écran qu'on a déjà vu) ou des structures plus élaborées (les listes par exemples qui sont des extensions des tableaux). Il faudra cependant toujours connaître les complexités de ce qu'on utilise.

{% attention %}
Lorsque l'on calcule la complexité d'un pseudo-code utilisant des fonctions, il faut compter le nombre d'instructions de l'exécution des fonctions !
{% endattention %}

Prenons par exemple le code suivant et comptons les instructions utilisées au cours de son exécution :

```python/
def recherche(t, x):
    for e in t:
        if e == x:
            return True
    return False

t = [1, 2, 6]
trouve = recherche(t, 6)
affiche à l'écran trouve
```

1. exécution de la ligne 7 : création d'un tableau et affectation à une variable : 2 instructions
2. exécution de la ligne 8 :
   1. exécution de la fonction recherche (ligne à ligne) :
      1. exécution de la ligne 1 : affectation des paramètres
         1. trouver les objets à mettre en paramètres :
            - pour le premier paramètre il faut trouver l'objet associé à t : 1 instruction
            - pour le second paramètre, l'objet est à créer : 1 instruction
         2. affecter les paramètres aux variables de la fonction :
            - affectation du premier paramètre à la variable locale t : 1 instruction
            - affectation du second paramètre à la variable locale e : 1 instruction
      2. exécution de la ligne 2 (3 fois): affecter `e` : 1 instruction
      3. exécution de la ligne 3 : un test
         - on trouve les objets associées à t et e : 2 instructions
         - on teste l'égalité : 1 instruction
         - on fait le `if`{.language-} : 1 instruction
      4. exécution de la ligne 4 : on arrive à cette ligne à la troisième itération : 1 instruction
   2. affection de la variable `trouve`{.language-}
3. afficher quelque chose à l'écran :
   - 1 instruction pour trouver l'objet à afficher
   - 1 instruction pour trouver l'afficher

Au total on eu besoin de $2+2+1+\underbracket{(1+1+1+1+3 \cdot (2+1+1) + 1)}_{\mbox{recherche(t, 6)}} + 1 + 1$
instructions c'est à dire $24$ instructions.

## Complexité des structures

> TBD re-écrire sous la forme de structures avec l'exemple de la pile et de son implémentation sous la forme d'un tableau de taille fixe donné a la création et d'une méthode copie dans pile qui copie toute la structure dans une autre.

Si l'on devait à chaque pseudo-code redéfinir tout les algorithmes qu'on utilise ce serait vraiment fastidieux. On utilise souvent des fonctions non basiques (comme l'affichage à l'écran qu'on a déjà vu) ou des structures plus élaborées (les listes par exemples qui sont des extensions des tableaux). Il faudra cependant toujours connaître les complexités de ce qu'on utilise.

Par exemple pour les listes, qui sont des tableaux redimensionnables :

- complexité d'ajout d'un élément à la fin de la liste : coût de 1 instruction
- complexité de l'ajout d'un élément pas à la fin de la liste : coût de la taille de la liste instructions
- complexité de la suppression d'un élément à la fin de la liste : coût de 1 instruction
- complexité de la suppression d'un élément pas à la fin de la liste : coût de la taille de la liste instructions
- usage comme un tableau : 1 instruction

Si vous utilisez des méthodes d'objets comme vous avez l'habitude de le faire en python (comme une `ma_liste.index("?")`{.language-}, `x in ma_chaîne_de_caractères`{.language-}) ou des structures compliquées (télécharger un fichier d'internet) vous avez le droit mais vous **devez** en connaître le coût : la complexité, les cas d'usage (comme être connecté à internet), etc.

## Complexité d'un algorithme

Le pseudo-code suivant, qui calcule la dixième valeur de la suite de Fibonacci a une complexité $C = 45$ :

```text#
F = un tableau vide de 10 cases
F[0] = 1
F[1] = 2

pour i allant de 2 à 9:
  F[i] = F[i-1] + F[i-2]

rendre F[9]
```

{% exercice %}
Explicitez les différentes instructions élémentaires pour justifier la valeur de la complexité de l'algorithme précédent.
{% endexercice %}
{% details "corrigé" %}

Il y a cinq types d'instructions élémentaires :

- les créations :
  - ligne 1 : un tableau
  - ligne 2 : un entier
  - ligne 3 : un entier
  - ligne 5 : deux entiers
- les affectations :
  - ligne 1 : on affecte une valeur au tableau
  - ligne 2, 3 : on affecte une valeur à une case du tableau
  - ligne 5 : on affecte les valeurs 2 à 9 à la variable i
  - ligne 6 : on affecte une valeur à une case du tableau
- les récupérations de variables :
  - ligne 6 : on récupère les valeurs de 2 cases du tableau
  - ligne 8 : on récupère les valeurs de 1 case du tableau
- opérations sur des entiers :
  - ligne 6 : une somme
- retour de l'algorithme en ligne 8

On en conclut la complexité de chaque ligne :

- ligne 1 : 2 instruction
- ligne 2 : 2 instructions
- ligne 3 : 3 instruction
- ligne 4 : 0 instruction
- ligne 5 : 3 instructions la première fois et 1 instruction les autres fois (on ne recrée pas les objets)
- ligne 6 : 4 instructions
- ligne 7 : 0 instruction
- ligne 8 : 2 instructions

Comme la ligne 5 et 6 sont exécutées 8 fois, on en conclut que la complexité est :

$$
2+2+3+0+ 2 + 8\cdot(1 + 4) + 0 + 2 = 49
$$

{% enddetails %}

Mais souvent la complexité dépend des paramètres du programme, comme par exemple le pseudo-code suivant qui rend la $n$ème valeur de la suite de Fibonacci où $n$ est le paramètre de l'algorithme :

```text#
fonction fibonacci(n):
  F = un tableau vide de n cases
  F[0] = 1
  F[1] = 2

  pour i allant de 2 à n-1:
    F[i] = F[i-1] + F[i-2]

  rendre F[n-1]
```

Le nombre de fois où l'on rentre dans la boucle va dépendre de l'entrée et on a maintenant une complexité de $C(n) = 5\cdot n+2$ qui dépend de la valeur du paramètre d'entrée.

{% exercice %}
Montrez que la complexité est bien de $5\cdot n+2$
{% endexercice %}
{% details "corrigé" %}
Il y a deux différences :

- il faut affecter un objet au paramètre $n$
- on ne rentre plus 8 fois dans la boucle mais $n-2$ fois.

La complexité est alors : $1 + 11 + (n-2)\cdot 5 = 5\cdot n+2$.

{% enddetails %}

Enfin, en règle générale, la complexité dépend trop profondément de la nature même de ses entrées et empêche d'en tirer une allure général. Par exemple l'algorithme suivant, écrit en python, qui cherche si une `valeur`{.language-} est dans un `tableau`{.language-} :

```text#
fonction est_dans_tableau(valeur, tableau):
    pour chaque élément x du tableau:
        si x == valeur:
            rend OUI
    rend NON
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

En utilisant la définition ci-dessus, la complexité de l'algorithme `est_dans_tableau`{.language-} vaut $5N+4$.

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

Lorsqu'à paramètre fixé le nombre d'instructions varie selon les paramètres utilisé (l'algorithme `est_dans_tableau`{.language-} par exemple), la complexité prend le maximum ($5N+4$ où $N$ est la la taille du tableau en entrée pour l'algorithme `est_dans_tableau`{.language-}) mais il peut être utile de connaître le minimum ($9$ pour l'algorithme `est_dans_tableau`{.language-}, indépendant de la taille du tableau en entrée) pour voir la variation de ce nombre en fonction des entrées.

{% note "**Définition**" %}

**_La complexité minimum $C_{\min}(N)$ d'un algorithme $A(p_1, \dots, p_m)$\_** est le nombre minimum d'instructions élémentaires effectuées pour exécuter l'algorithme $A$ avec des entrées dont la taille vaut $N$.
{% endnote %}

## <span id="complexité-temps"></span>Complexité en temps

Lorsqu'un algorithme est codé, on peut l'exécuter et mesurer son temps d'exécution. On peut alors définir la **_complexité en temps_** d'exécution d'un code :
{% note "**Définition**" %}

**_La complexité en temps_** $T(N)$ d'un code $A(p_1, \dots, p_m)$ est le temps maximum pris pour exécuter le code $A$ avec des entrées dont la taille vaut $N$.
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

```text#
fonction fibonacci_sobre(n):
  a = 1
  b = 1

  pour i allant de 2 à n-1:
    c = a + b
    a = b
    b = c

  rendre b
```

Il demande beaucoup moins de mémoire, 5 cases mémoires seulement (pour stocker le paramètre $n$ et les 4 variables $a$, $b$, $c$ et $i$), ce qui lui permet de calculer de grandes valeurs de la suite de Fibonacci, plus grande que la taille mémoire de l'ordinateur qui exécutera le code associé.

Sa complexité un peu plus élevée :

1. 1 instruction : affectation du paramètre
2. 2 instructions : création d'un objet et affectation
3. 2 instructions : création d'un objet et affectation
4. -
5. $n+2$ instructions : $n-2$ affectations de `i`{.language-} et 4 instruction pour la création des bornes (2 créations (entiers 2 et 1) ; une lecture et une opération de soustraction)
6. $4(n-2)$ instructions : $n-2$ itérations de 2 lectures, une somme et une affectation
7. $2(n-2)$ instructions : $n-2$ itérations de 1 lecture et une affectation
8. $2(n-2)$ instructions : $n-2$ itérations de 1 lecture et une affectation
9. -
10. 2 instructions : 1 lecture, un retour

Pour un total de $9\cdot n-15$, mais reste comparable au premier.

{% info %}
Souvent, lors du design de nos algorithmes on aura le choix entre entre consommer beaucoup de mémoire et être sobre en instructions ou le contraire.
{% endinfo %}

Complexité et complexité spatiale sont liées puisque chaque affectation d'une variable prend une instruction :

{% note %}
La complexité spatiale est toujours inférieure à la complexité.
{% endnote %}
