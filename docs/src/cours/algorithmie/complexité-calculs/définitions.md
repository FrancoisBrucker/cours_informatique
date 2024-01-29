---
layout: layout/post.njk

title: Définitions

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

[On l'a vu](../../écrire-algorithmes/pseudo-code/#complexité), on appelle complexité d'un pseudo-code le nombre d'instructions élémentaires utilisées pour son exécution.

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

Il y a quatre types d'instructions élémentaires :

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

- ligne 1 : 1 instruction
- ligne 2 : 1 instruction
- ligne 3 : 1 instruction
- ligne 4 : 0 instruction
- ligne 5 : 1 instruction
- ligne 6 : 4 instructions
- ligne 7 : 0 instruction
- ligne 8 : 2 instructions

Comme la ligne 5 et 6 sont exécutées 8 fois, on en conclut que la complexité est :

$$
1+1+1+0+ 8\cdot(1 + 4) + 0 + 2 = 45
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

Le nombre de fois où l'on rentre dans la boucle va dépendre de l'entrée et on a maintenant une complexité de $C(n) = 5\cdot(n-1)$ qui dépend de la valeur du paramètre d'entrée.

{% exercice %}
Montrez que la complexité est bien de $5\cdot(n-1)$
{% endexercice %}
{% details "corrigé" %}

On ne rentre plus 8 fois dans la boucle mais $n-2$ fois. La complexité est alors : $5 + (n-1)\cdot 5 = 5\cdot n-5$.

{% enddetails %}

Enfin, en règle générale, la complexité dépend trop profondément de la nature même de ses entrées et empêche d'en tirer une allure général. Par exemple l'algorithme suivant, écrit en python, qui cherche si une `valeur`{.language-} est dans un `tableau`{.language-} :

```text#
fonction est_dans_tableau(valeur, tableau):
    pour chaque élément x du tableau:
        si x == valeur:
            rend OUI
    rend NON
```

La complexité de cet algorithme va dépendre de l'endroit où se trouve la valeur dans le tableau. Si l'on utilise la taille $n$ du tableau comme paramètre de complexité, sa complexité ira de 3 lorsque la valeur est le premier élément du tableau (une affectation de $x$, un test et un retour) à $2n + 1$ si la valeur n'est pas dans le tableau ($n$ affectations de $x$, $n$ tests et un retour). La complexité de l'algorithme est alors $C(i) = 2i + 1$ où $i$ est la position de la valeur dans le tableau.

## Complexité d'un algorithme

Lorsque l'on utilise un algorithme on a jamais beaucoup de connaissances *a priori* sur ses entrées. Pour la fonction `est_dans_tableau`{.language-} on sait que l'on a un entier et un tableau en paramètre mais pas la natures des entiers contenus dans le tableau. Avoir une complexité qui dépend des valeurs contenues dans le tableau est donc inutile en pratique. Il serait pus intéressant de connaître la complexité de l'algorithme pour un tableau d'une taille donnée. Dans ce cas là on calculera la complexité maximale pour tous les tableaux de même taille.

{% note %}
On calcule la complexité d'un algorithme par rapport à un paramètre qui rend compte de la connaissance *a priori* que l'on a sur les entrées de celui-ci.
{% endnote %}

### Connaissances minimales sur les entrées

Les connaissances minimales que l'on possède sur les données sont leurs tailles de stockage en mémoire.

{% note %}

***la taille des entrées d'algorithme*** est le nombre de cases mémoires nécessaires pour les stocker.
{% endnote %}

Dans la partie pseudo-code on a considéré deux types de données :

- les types simples que sont les nombres et les caractères qui sont stockable sur 1 case mémoire
- les tableaux dont la taille est la somme des tailles de leurs éléments

### Complexité algorithmique

En prenant en compte les connaissances minimales que l'on a sur les entrées d'un algorithme, sa complexité est définie comme suit :

{% note "**Définition**" %}

***La complexité $C(N)$ d'un algorithme $A(p_1, \dots, p_m)$***  est le nombre maximum d'instructions élémentaires effectuées pour exécuter l'algorithme $A$ avec des entrées dont la taille vaut $N$.
{% endnote %}

En utilisant la définition ci-dessus, la complexité de l'algorithme `est_dans_tableau`{.language-} vaut $2N+1$.

Comme rien n'est jamais simple, il existe des cas où la connaissance de la taille ne done pas un critère pertinent pour établir une complexité. C'est souvent le cas lorsque les paramètres de l'algorithmes sont de taille fixe, comme pour la fonction `fibonacci(n)`{.language-}, la taille de stockage d'un entier étant de 1 case mémoire.

Si l'on avait calculé la complexité en regroupant les entrées par taille, on aurait eu qu'une seule classe d'entrée et la complexité aurait été infinie... Il a donc fallu supposer que l'on connaissait la valeur de l'entrée pour calculer une complexité finie.

Il n'y a pas de règle immuable dans le choix des connaissances que l'on s'accorde sur les paramètres, mais ne vous inquiétez pas, cela ressortira immédiatement du calcul. En revanche, comme la nature du paramètre peut changer :

{% note %}
Lorsque l'on donne une complexité en fonction d'un paramètre, il faut :

- obligatoirement l'**expliciter** (taille de données, valeur d'une entrée, etc)
- s'assurer que l'on peut calculer ce paramètre pour **toutes les entrées**
- ne pas oublier que la complexité est le **maximum** du nombre d'instructions pour les exécutions de l'algorithme avec des entrées de paramètre constant (même taille de donnée, même valeur d'entrée, etc)
{% endnote %}

## Autres types de Complexité

Lorsque l'on parle de complexité d'un algorithme ce sera toujours en utilisant la définition précédente. Il existe cependant d'autres types de complexité que l'on pourra utiliser.

### Complexité min

Lorsqu'à paramètre fixé le nombre d'instructions varie selon les paramètres utilisé (l'algorithme `est_dans_tableau`{.language-} par exemple), la complexité prend le maximum ($2N+1$ où $N$ est la la taille du tableau en entrée pour l'algorithme `est_dans_tableau`{.language-}) mais il peut être utile de connaître le minimum ($3$ pour l'algorithme `est_dans_tableau`{.language-}, indépendant de la taille du tableau en entrée) pour voir la variation de ce nombre en fonction des entrées.

{% note "**Définition**" %}

***La complexité minimum $C_{\min}(N)$ d'un algorithme $A(p_1, \dots, p_m)$***  est le nombre minimum d'instructions élémentaires effectuées pour exécuter l'algorithme $A$ avec des entrées dont la taille vaut $N$.
{% endnote %}

### <span id="complexité-temps"></span>Complexité en temps

Lorsqu'un algorithme est codé, on peut l'exécuter et mesurer son temps d'exécution. On peut alors définir la ***complexité en temps*** d'exécution d'un code :
{% note "**Définition**" %}

***La complexité en temps $C_{t}(N)$ d'un code $A(p_1, \dots, p_m)$***  est le temps maximum pris pour exécuter le code $A$ avec des entrées dont la taille vaut $N$.
{% endnote %}

Si chaque instruction élémentaire prend le même temps à être effectuée sur une machine (ou que l'on borne le tout par l'instruction élémentaire la plus gourmande), la complexité d'un pseudo-code nous donne un nombre proportionnel au temps qu'il mettra à s'exécuter :

{% note %}
Le temps mis pour un code à être exécuté est proportionnelle à la complexité de son pseudo-code associé.
{% endnote %}

Si l'on connaît le jeu de paramètres d'entrée réalisant la complexité $C(N)$ d'un algorithme, on peut alors exécuter le code qui lui est associé et mesurer son temps d'exécution pour tracer la courbe de la complexité.

### Complexité en mémoire

Enfin, L'autre paramètre utile que l'on mesure est le nombre de cases mémoires utilisées par l'algorithme, c'est à dire la taille des variables dont il a eu besoin pour fonctionner.

{% note "**Définition**" %}

***La complexité en mémoire $C_M(N)$ d'un algorithme $A(p_1, \dots, p_m)$***  est le nombre maximum de cases mémoires utilisées en même temps pendant l'exécution de l'algorithme $A$ avec des entrées dont la taille vaut $N$.
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

Sa complexité un peu plus élevée, $8\cdot n-12$, mais reste comparable au premier.

{% info %}
Souvent, lors du design de nos algorithmes on aura le choix entre entre consommer beaucoup de mémoire et être sobre en instructions ou le contraire.
{% endinfo %}

Complexité et complexité en mémoire sont liées puisque chaque affectation d'une variable prend une instruction :

{% note %}
La complexité en mémoire est toujours inférieure à la complexité.
{% endnote %}

## <span id="forme-asymptotique"></span>Importance de la complexité

Nous allons illustrer l'importance pratique de la complexité en considérant 5 allures de complexité :  :

{% note "**Définition**" %}
On note $C(n)$ la complexité d'un algorithme. On dira de cette complexité que c'est une (avec $K$ et $k$ deux constantes et $\sim$ l'[équivalent mathématique](https://fr.wikipedia.org/wiki/%C3%89quivalent)) :

- ***complexité constante*** si $C(n) \sim K$
- ***complexité logarithmique*** si $C(n) \sim K\cdot \ln(n)$
- ***complexité linéaire*** si $C(n) \sim K\cdot n$
- ***complexité polynomiale*** $C(n) \sim K\cdot n^k$
- ***complexité exponentielle*** $C(n) \sim K\cdot k^n$

{% endnote %}

Les types de complexités ci-dessus sont rangés par ordre, de la moins grande à la plus grande.

Remarquez que si $n$ représente la taille des données, un algorithme de complexité linaire nécessite de lire toutes les données au plus un nombre constant de fois pour s'exécuter, alors qu'un algorithme de complexité logarithmique n'a même pas besoin de lire une fois toutes les données pour s'exécuter ! Ceci n'est souvent possible que si les données en entrées ont une structure très particulière. Par exemple pour le problème de la recherche d'une valeur particulière dans un tableau :

- trouver cette valeur nécessite un temps linéaire si on utilise notre algorithme `est_dans_tableau`{.language-},
- trouver cette valeur nécessite un temps logarithmique si le tableau est un tableau trié et qu'on utilise l'algorithme de [recherche dichotomique](https://fr.wikipedia.org/wiki/Recherche_dichotomique)

{% info %}
Notez bien que la complexité logarithmique est la même quelque soit la base utilisée puisque $\log_k(n) = \frac{\ln (n)}{\ln (k)}$ et donc $\log_k(n) = K\cdot \ln(n)$ avec $K = \frac{1}{\ln (k)}$ constant.
{% endinfo %}

Il est crucial de chercher la meilleure complexité pour un algorithme car ses performance seront drastiquement différentes selon le type de complexité qu'il possède, comme le montre les deux tableaux ci-dessous, repris du livre [Computer and intractability](https://en.wikipedia.org/wiki/Computers_and_Intractability). Ce qu'il faut retenir :

{% note %}

- il y a une **gigantesque différence** entre complexité logarithmique et complexité linéaire
- il y a une **énorme différence** entre complexité linéaire et complexité polynomiale, mais moins grande qu'entre logarithmique et linéaire
- il y a une **gigantesque différence** entre complexité polynomiale et complexité exponentielle (qu'il ne faut donc jamais avoir si possible)

{% endnote %}

### Temps pour résoudre un problème de taille $n$

Exemple d'évolution du temps de calcul par rapport à la complexité. En supposant, que l'on ait un ordinateur qui résout des problèmes de complexité $n$ en 0.01 ms pour des données de taille 10, on peut remplir le tableau ci-après.

En colonnes le nombre $n$ de données, en lignes les complexités des algorithmes.

| complexité  |     10     |   20     |    30   |      40     |     50                   |       60                   |
|-------------|------------|----------|---------|-------------|--------------------------|----------------------------|
|   $\ln(n)$  |  2 $\mu s$ | 3 $\mu s$|3 $\mu s$|  4 $\mu s$  | 4 $\mu s$                | 4 $\mu s$                  |
|    $n$      |    0.01 ms | 0.02 ms  | 0.03 ms |  0.04 ms    | 0.05 ms                  | 0.06 ms                    |
|    $n^2$    |    0.1 ms  | 0.4 ms   | 0.9 ms  |  1.6 ms     | 2.5 ms                   | 3.6 ms                     |
|    $n^3$    |    1 ms    | 8 ms     | 27 ms   |  64 ms      | 125 ms                   | 216 ms                     |
|    $n^5$    |    1s      | 3.2 s    | 24.3 s  |  1.7 min    | 5.2 min                  | 13 min                     |
|    $2^n$    |    1 ms    | 1s       | 17.9 min|  12.7 jours | 35.7 ans                 | 36600 ans                  |
|    $3^n$    |    59 ms   | 58 min   | 6.5 ans |  385500 ans | $2.27\cdot 10^8$ siècles | $1.3\cdot 10^{13}$ siècles |

L'évolution est dramatique plus la complexité augmente. Pour une complexité logarithmique, le temps *semble* constant et pour une complexité polynomiale, la croissance reste maîtrisée même s'il vaut mieux avoir une petite complexité pour traiter plus de données. Pour une complexité exponentielle ($2^n$ et $3^n$) en revanche, la durée est tout simplement rédhibitoire.

{% info %}
Pour générer le tableau, on voit que le temps  $t$ pour exécuter 1 opération est de .001ms (on regarde la ligne de complexité linéaire : pour $n=10$ on prend 0.01 opérations, donc 1 opération nécessite $0.01/10ms$). Le temps pris pour exécuter $f(n)$ opérations avec une entrée de taille de $n$ est alors : $t \cdot f(n)$
{% endinfo %}

### Nombre de problèmes résolus par heure

En colonne la rapidité de la machine, en ligne la taille maximale d'un problème que l'on peut résoudre en 1heure.

| complexité | machine actuelle | 100x plus rapide | 1000x plus rapide |
|------------|------------------|------------------|-------------------|
|  $\ln(n)$  |        $N0$      |$e^{100} \cdot N0$|$e^{1000} \cdot N0$|
|    $n$     |        $N1$      |  $100 \cdot N1$  |  $1000 \cdot N1$  |
|    $n^2$   |        $N2$      |  $10 \cdot N2$   |  $31.6 \cdot N2$  |
|    $n^3$   |        $N3$      |  $4.64 \cdot N3$ |  $10 \cdot N3$    |
|    $n^5$   |        $N4$      |  $2.5 \cdot N4$  |   $3.98 \cdot N4$ |
|    $2^n$   |        $N5$      |    $N5 + 6.64$   |   $N5 + 9.97$     |
|    $3^n$   |        $N6$      |    $N6 + 4.19$   |   $N6 + 6.29$     |

La encore, l'évolution est dramatique plus la complexité augmente. Pour des complexités logarithmiques et polynomiales le nombre de problèmes augmente d'un facteur multiplicatif lorsque la vitesse augmente, mais ce n'est pas le cas pour des complexités exponentielles. Pour ces problèmes, augmenter la vitesse de la machine ne change pas fondamentalement le nombre de problèmes que l'on peut résoudre.

{% info %}
Pour générer le tableau, on suppose que l'on peut résoudre $K$ opérations en 1 heure. On cherche alors $n$ tel que $f(n)$ soit égal à $K$ et donc $n = f^{-1}(K)$. En remarquant que $K$ est égal à la taille maximale d'un problème de complexité linéaire résoluble en 1heure, on la taille maximale $n$ d'un problème de complexité $f(n)$ résoluble en 1 heure pour une machine allant $k$ fois pus vite qu'une machine actuelle vaut $f^{-1}(k \cdot N1)$.
{% endinfo %}

### <span id="n_factoriel"></span> Le cas particulier de $n!$

Souvent les étudiants veulent que leurs algorithmes soient de complexité $C(n) = n!$. Ce n'est **presque jamais exact** ! En effet, la [formule de Stirling](https://fr.wikipedia.org/wiki/Formule_de_Stirling) donne l'équivalent suivant pour $n!$ :

$$
n! \sim \sqrt{2\pi n}(\frac{n}{e})^n
$$

On a donc que $n!$ est de l'ordre de $n^{n+1/2}$, qui est vachement plus grand que $2^{n}$ qui est déjà gigantesque.

Par exemple :

- $10! = 3628800$
- $2^{10} = 1024$

Et la différence s’accroît exponentiellement  avec le nombre :

- $74! = 330788544151938641225953028221253782145683251820934971170611926835411235700971565459250872320000000000000000$
- $2^{74} = 18889465931478580854784$

{% info %}
Si vous pensez que votre algorithme tout bête est de complexité $C(n) = n!$. Réfléchissez-y à deux fois. C'est presque sûrement une erreur... Et si ce n'est est pas une, votre algorithme est inefficace et devrait sûrement être oublié plutôt que montré à votre enseignant.
{% endinfo %}
