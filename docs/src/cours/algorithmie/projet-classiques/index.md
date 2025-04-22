---
layout: layout/post.njk

title: Algorithmes classiques

eleventyNavigation:
  prerequis:
    - /cours/algorithmie/projet-itératif-récursif/
    - /cours/algorithmie/projet-calcul-complexite/

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD à refaire bien
> faire une partie énumération dans classique (compteur, permutation, 8 reines (vor ds),lancer de dés aussi ds ?).
> TBD séparer les exos qui sont mieux avec une liste en récursif. Preparer.
> TBD rendu de piece par programmation dynamique
> TBD Ackermann et décurrification.
> 
> TBD les 8 reines en récursif et itératif, puis généralisation aux autres pièces d'échec et aux reines avec ds échiquiers plus grands et en dimensions plus élevées <https://interstices.info/le-probleme-des-8-reines-et-au-dela/>

Algorithmes classiques dont l'intérêt est à la fois esthétique (ce sont de jolis algorithmes),pratiques (ils mettent en oeuvre des techniques facilement réutilisables) et didactiques (trouver et prouver leurs fonctionnement vous fera progresser).

{% info %}
Pour tous ces exercices, si la structure de donnée n'est pas précisé, vous utiliserez des listes.
{% endinfo %}

## <span id="fibonacci"></span>Fibonacci

[La suite de Fibonacci](https://fr.wikipedia.org/wiki/Suite_de_Fibonacci), bien connue, se définie ainsi pour tout $n>0$ :

<div>
$$
F_n = \left\{
    \begin{array}{ll}
        1 & \mbox{si } n \leq 2 \\
        F_{n-1} + F_{n-2}& \mbox{sinon.}
    \end{array}
\right.
$$
</div>

{% exercice %}
Utilisez la définition précédente pour créer un algorithme récursif calculant $F_n$ de signature :

```pseudocode
fibonacci_rec(n: entier) → entier
```

{% endexercice %}
{% details "corrigé" %}

```pseudocode/
algorithme fibonacci_rec(n: entier) → entier:
    si n ≤ 2:
        rendre 1
    rendre fibonacci_rec(n-1) + fibonacci_rec(n-2)
```

Il faut démontrer que ce programme est bien un algorithme car il y a plusieurs récursions !

Ceci se fait facilement par une récurrence sur $n$ car chaque appel se rapproche strictement de la condition d'arrêt.

1. initialisation : $\mbox{fibonacci\\_rec}(n)$ admet un nombre fini de récursion pour $n\leq 2$.
2. hypothèse de récurrence : $\mbox{fibonacci\\_rec}(m)$ admet un nombre fini de récursion pour $m\leq n$.
3. Pour $n + 1$, $\mbox{fibonacci\\_rec}(n)$ et $\mbox{fibonacci\\_rec}(n-1)$ se terminent en un nombre fini de récursion donc la ligne 4 de l'algorithme aura aussi un nombre fini de récursion.

Une fois la finitude démontrée la correction est évidente, comme souvent avec les algorithmes récursif, puisque l'algorithme ne fait que transcrire l'équation de récursion.

{% enddetails %}

La preuve de l'exercice précédent donne une règle générale de preuve de finitude d'un programme récursif :

{% note "**À retenir**" %}
Si tous les appels récursifs d'un programme se _rapprochent strictement_ de la condition d'arrêt, alors le nombre de récursion est fini.

La condition de rapprochement va dépendre des paramètres et du programme et doit être explicitée.
{% endnote %}

L'algorithme précédent n'est pas sous la forme de récursion terminale. On peut le rentre terminal en utilisant 2 accumulateurs :

{% exercice %}
Modifiez l'algorithme récursif précédent pour qu'il devienne une récursion terminale grace à l'utilisation de deux accumulateurs. Cet algorithme sera de signature :

```pseudocode
fibo(n: entier, u_i, u_i_moins_un) → entier
```

Quels seraient les paramètres pour calculer $F_n$ ?
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme fibo(n: entier, u_i, u_i_moins_un) → entier:
    si n == 1:
        rendre u_i
    sinon:
        rendre fibo(n-1, u_i + u_i_moins_un, u_i)
```

Pour calculer $F_n$ :

```pseudocode
fibo(n: entier, 1, 0)
```

{% enddetails %}

Maintenant que la récursion est terminale il est facile de transformer notre algorithme récursif en un algorithme itératif :

{% exercice %}
Modifiez l'algorithme récursif précédent pour qu'il devienne itératif. Sa signature doit être :

```pseudocode
fibo(n: entier) → entier
```

{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme fibo(n: entier) → entier:
    u_i ← 1
    u_i_moins_un ← 0

    tant que n > 1:
        temp ← u_i 
        u_i ← u_i + u_i_moins_un
        u_i_moins_un ← u_i
    
    rendre u_i
```

N'oubliez pas le stockage temporaire de `u_i`{.language-} dans la variable `temp`{.language-}.

{% enddetails %}

## <span id="triangle-pascal"></span>Triangle de Pascal

Formule du coefficient binomial dit du [triangle de Pascal](https://fr.wikipedia.org/wiki/Triangle_de_Pascal), avec $1\leq k \leq n$ :

<div>
$$
\binom{n}{k} = \binom{n-1}{k-1} \mathrel{+} \binom{n-1}{k}
$$
</div>

et :

<div>
$$
\binom{n}{0} = \binom{n}{n} = 1
$$
</div>

{% exercice %}
Après avoir examiné les conditions d'arrêt, donner un algorithme récursif permettant de calculer le coefficient binomial.

{% endexercice %}
{% details "corrigé" %}

La formule de récursion s'arrête dans deux cas possibles soit $k = 1$ (première récursion) soit $n - 1 = k$ deuxième récursion. On a alors deux conditions d'arrêts à regarder pour $1\leq k \leq n$ :

- soit $k = 0$ et $\binom{n}{0} = 1$
- soit $k = n$ et $\binom{n}{n} = 1$

On a alors le code :

```pseudocode
algorithme binom_rec(n: entier, k: entier) → entier:
    si (n == k) ou (k == 0):
        rendre 1
    sinon:
        rendre binom_rec(n-1, k-1) + binom_rec(n - 1, k)
```

Comme $n$ diminue strictement et $1\leq k \leq n$ on se rapproche strictement de la condition d'arrêt, le programme s'arrête à chaque fois : c'est un algorithme.

{% enddetails %}

Pas de récursion terminale garantie si double récursion. Mais on peut tout de même ici en donner une version itérative. Avant de résoudre l'exercice suivant, regardez comment vous faisiez au lycée en remplissant petit à petit chaque ligne d'une matrice. La ligne $n$ correspond aux coefficients
$\binom{n}{k}$ pour tout $0\leq k \leq n$, et vous la remplissiez en utilisant les lignes précédentes avec l'équation. Mais si, rappelez-vous :

{% lien %}
[Calculer un coefficient binomial : triangle de Pascal - Terminale](https://www.youtube.com/watch?v=6JGrHD5nAoc)
{% endlien %}

Pour ces algorithme on utilisera [le type matrice](../pseudo-code/#type-matrice){.interne} défini lorsque l'on a parlé de pseudo-code. Une matrice $M$ est un tableau de (tableaux d'entiers)de telle sorte que :

- $M$ est de type `[[entier]]`{.language-}
- $M[i]$ est la (i+1) ème ligne de la matrice
- $M[i][j]$ est le (j+1) ème élément de la (i+1) ème ligne de la matrice.

Le code suivant crée une matrice triangulaire inférieure à $n$ lignes valant 1 à toutes les cases du tableau :

```pseudocode
algorithme crée_matrice(n: entier) → [[entier]]
matrice ← un tableau de [entier] de taille n

pour chaque i de [1, n]:
    ligne ← un tableau d'entiers de taille i

    matrice[i-1] ← ligne
    pour chaque j de [1, i]:
        ligne[j-1] ← 1 
```

Utiliser le code précédent pour résoudre l'exercice suivant :

{% exercice %}
En créant itérativement la matrice triangulaire inférieure, donner une version itérative de l'algorithme calculant le triangle de Pascal. Sa signature devra être :

```pseudocode
algorithme binom_matrice(n: entier) → [[entier]]:
```

{% endexercice %}
{% details "corrigé" %}

Première version qui calcule toute la matrice triangulaire inférieure :

```pseudocode/
algorithme binom_matrice(n: entier) → [[entier]]:
    matrice ← un tableau de [entier] de taille n+1

    pour chaque i de [0, n]:
        ligne ← un tableau d'entiers de taille i+1

        matrice[i] ← ligne
        pour chaque j de [0, i]:
            si (j == i) ou (j == 0):
                ligne[j] ← 1
            sinon:
                précédent ← matrice[i-1]
                ligne[j] ← précédent[j-1] + précédent[j]

    rendre matrice
```

Il y a deux boucles imbriquées, donc deux invariants à trouver !

L'invariant de la boucle 4-13 peut être :

> **Invariant de la boucle 4-13** : `matrice[i-1]`{.language-} contient la $i$ème ligne de la matrice triangulaire inférieure de Pascal.

Pour le prouver, il faut trouver un invariant à la boucle 8-13. Par exemple :

> **Invariant de la boucle 8-13** : si `matrice[i-2]`{.language-} contient la $i-1$ème ligne de la matrice triangulaire inférieure de Pascal, alors `ligne`{.language-} contient la $i$ème ligne de la matrice triangulaire inférieure de Pascal.

Ce dernier invariant est évidemment vrai par construction de la boucle (c'est la relation de récurrence). Une fois la boucle 8-13 prouvée, cela prouve l'invariant de la boucle 4-13.

{% enddetails %}

## <span id="dichotomie"></span>Dichotomie

> - **Utilité** : brique de base à connaître par cœur
> - **Difficulté** : trivial

On l'a déjà vu. Uniquement un rappel car fondamental.

{% aller %}

1. [dichotomie : création et preuve](../projet-itératif-récursif/#dichotomie){.interne}
2. [dichotomie : complexité](../projet-calcul-complexite/#dichotomie){.interne}

{% endaller %}

## Fibonacci

> - **Utilité** : à connaître car :
>   - exemple de transformation d'un algo de complexité exponentiel à linéaire.
>   - un algo dont la complexité vaut son retour dans le cas récursif simple
> - **Difficulté** : facile pour la création et la complexité de base

On l'a déjà vu. Uniquement un rappel.

{% aller %}

1. [Fibonacci : création et preuve](../projet-itératif-récursif/#fibonacci){.interne}
2. [Fibonacci : complexité](../projet-calcul-complexite/fibonacci/){.interne}

{% endaller %}

## Triangle de Pascal

On a déjà vu les 2 premiers. Le troisième est un peu plus compliqué

### Rappel

> - **Utilité** : à connaître car exercice classique réduction de complexité spatiale.
> - **Difficulté** : facile

{% aller %}

1. [Triangle de Pascal : création et preuve](../projet-itératif-récursif/#triangle-pascal){.interne}
2. [Triangle de Pascal : complexité](../projet-calcul-complexite/triangle-pascal/){.interne}

{% endaller %}

### Optimisé

> - **Utilité** : classique d'optimisation
> - **Difficulté** : moyen.

{% aller %}
[Triangle de Pascal : complexité spatiale minimale](triangle-pascal/){.interne}

{% endaller %}

## Suppression d'éléments

### Suppression de valeurs

> - **Utilité** : utilisation d'une liste
> - **Difficulté** : facile.

On a déjà vu comment faire avec un tableau.

#### Tableau

{% aller %}

1. [Suppression de valeur : création et preuve](../projet-itératif-récursif/#suppression-valeur){.interne}
2. [Suppression de valeur : complexité](../projet-calcul-complexite/#suppression-valeur){.interne}

{% endaller %}

#### Liste

Regardons comment tout ceci peut fonctionner avec une liste :

{% aller %}
[Suppression de valeurs](suppression-valeurs){.interne}
{% endaller %}

### Suppression de doublons

> - **Utilité** : classique et simple.
> - **Difficulté** : facile

{% aller %}
[Suppression des doublons](suppression-doublons){.interne}
{% endaller %}

## Complexité

Exercices de base de complexité. Il est important de les connaître pour éviter les fautes idiotes.

### Erreur bête

> - **Utilité** : crucial à comprendre
> - **Difficulté** : moyen

{% aller %}
[Noob trap](noob-trap){.interne}
{% endaller %}

### $X$ marks the spot

> - **Utilité** : crucial à comprendre
> - **Difficulté** : dur

Un robot se déplace sur une droite d'une unité par unité. Il doit chercher un endroit particulier sur cette droite à $X$ unités de 0, $X$ pouvant être **positif ou négatif**. Cette endroit est inconnu pour le robot, mais s'il passe sur cet endroit il le reconnaîtra.

{% exercice %}
Donnez un algorithme en $\mathcal{O}(X)$ permettant au robot d'atteindre $X$ à partir de sa position initiale qui vaut $0$.
{% endexercice %}
{% details "corrigé" %}

Remarquer que l'on ne peut pas :

1. avancer uniquement dans une direction : il faut osciller
2. osciller en incrémentant d'un pas constant : on est de complexité au carré de $X$ (c'est facile à montrer)

L'idée est d'osciller autour de l'origine en puissances de 2 :

1. avancer de $2^0 = 1$ : position finale $+1$
2. reculer de $2^0 + 2^0$ : position finale $-1$
3. avancer de $2^0 + 2^1$ : position finale $+2$
4. reculer de $2^1 + 2^1$ : position finale $-2$
5. avancer de $2^1 + 2^2$ : position finale $+4$
6. reculer de $2^2 + 2^2$ : position finale $-4$
7. avancer de $2^2 + 2^3$ : position finale $+8$
8. reculer de $2^3 + 2^3$ : position finale $-8$
9. ...

Au pire, le robot arrivera sur la marque $X$ au bout de $2 \cdot \log_2(X)$ itérations.

Il aura effectué un déplacement d'au plus : $2 \cdot (X + X/2 + X/4 + \dots + 1)$ unités. Or $2 \cdot (X + X/2 + X/4 + \dots + 1) = 2\cdot X \cdot \sum_{i=0}^{i=\log_2(X)} 1/2^i = 2\cdot X \cdot(1- 1/2^{\log_2(X)}) = \mathcal{O}(X)$.

L'astuce de se déplacer par puissance de 2 permet de majorer la distance par $X$ car la série des $\sum 1/2^i$ est convergente. Il est crucial de connaître cette technique qui vous tirera de nombreux mauvais pas en algorithmie.

{% enddetails %}

### Équations de récurrence

Quelques équations de récurrences sont à connaître car elles donnent de complexités très différentes.

{% exercice %}
Que vaut $C(n)$ si :

<div>
$$
C(n) = \mathcal{O}(1) + C(n - K)
$$
</div>
{% endexercice %}
{% details "corrigé" %}

> TBD $C(n) = \mathcal{O}(n)$

{% enddetails %}
{% exercice %}
Que vaut $C(n)$ si :

<div>
$$
C(n) = \mathcal{O}(n) + C(n - K)
$$
</div>
{% endexercice %}
{% details "corrigé" %}

> TBD $C(n) = \mathcal{O}(n^2)$

{% enddetails %}

{% exercice %}
Que vaut $C(n)$ si :

<div>
$$
C(n) = \mathcal{O}(1) + C(\frac{n}{2})
$$
</div>
{% endexercice %}
{% details "corrigé" %}

> TBD $C(n) = \mathcal{O}(\ln(n))$

{% enddetails %}
{% exercice %}
Que vaut $C(n)$ si :

<div>
$$
C(n) = \mathcal{O}(n) + C(\frac{n}{2})
$$
</div>
{% endexercice %}
{% details "corrigé" %}

> TBD $C(n) = \mathcal{O}(n)$

{% enddetails %}

{% exercice %}
Que vaut $C(n)$ si :

<div>
$$
C(n) = \mathcal{O}(1) + 2\cdot C(\frac{n}{2})
$$
</div>
{% endexercice %}
{% details "corrigé" %}

> TBD $C(n) = \mathcal{O}(n)$

{% enddetails %}
{% exercice %}
Que vaut $C(n)$ si :

<div>
$$
C(n) = \mathcal{O}(n) + 2\cdot C(\frac{n}{2})
$$
</div>
{% endexercice %}
{% details "corrigé" %}

> TBD $C(n) = \mathcal{O}(n\ln(n))$

{% enddetails %}

## Tours de Hanoï

> - **Utilité** : classique parmi les classique. La preuve que la complexité est minimale est à connaître
> - **Difficulté** : moyen

{% aller %}
[Tours de Hanoi](tours-hanoi){.interne}
{% endaller %}

## Compteur binaire

> - **Utilité** : algorithme à la base de nombreux autres algorithme d'énumération.
> - **Difficulté** : moyen

{% aller %}
[Compteur binaire](compteur-binaire){.interne}
{% endaller %}

## Col de listes

> - **Utilité** : à connaître car un classique des concours (on le donne sans indications...)
> - **Difficulté** : moyen

{% aller %}
[Cols de listes et de matrices](cols){.interne}
{% endaller %}

## Tris

> - **Utilité** : tris pouvant être utile dans des cas particuliers et surtout à la base de nombreux pièges
> - **Difficulté** : moyen

Des tris utiles dans des cas spécifiques, et dont la complexité semble plus petite que $n\log(n)$. Connaître pourquoi ce n'est (bien sur) pas le cas.

{% aller %}
[Tris spéciaux](tris-spéciaux){.interne}
{% endaller %}

## Min et max d'un tableau d'entiers

> - **Utilité** : une optimisation élégante et une astuce utile à garder dans sa poche, car elle se retrouve dans plusieurs algorithmes optimaux classiques.
> - **Difficulté** : moyen

### Un algo

{% exercice %}
Donnez un algorithme avec $T.\mbox{\small longueur} - 1$ comparaisons permettant de trouver le minimum d'un tableau d'entier.

Que faut-il modifier pour trouver le maximum ?
{% endexercice %}
{% details "corrigé" %}
> TBD simple
{% enddetails %}

### Complexité du Problème

{% exercice %}
Montrer que si l'on cherche à trouver l'élément minimum d'un tableau d'entiers $T$ il faut au moins $T.\mbox{\small longueur} - 1$ comparaisons
{% endexercice %}
{% details "corrigé" %}
> TBD graphe connexe.
{% enddetails %}
On veut minimiser le nombre de comparaisons dans la recherche d'un élément min et max d'un tableau.

### Une astuce

{% exercice %}
Montrer que si l'on cherche à trouver à la fois le minimum et le maximum d'un tableau d'entiers $T$, on peut s'en sortir avec  $3/2 \cdot T.\mbox{\small longueur} - 1$ comparaisons.
{% endexercice %}
{% details "corrigé" %}
Si on fait les deux à la suite on a 2n comparaisons.

On commence par trier les éléments $T[i]$ et $T[i+1]$ pour tout $i$ ($n/2$ comparaisons)

Puis on cherche le min sur les $T[2i]$ ($n/2$ comparaisons) et le max sur les $T[2i +1]$ ($n/2$ comparaisons)

{% enddetails %}

## Piles

> - **Utilité** : les piles ça sert toujours. Ces exercices vous montrerons des cas classiques d'utilisation
> - **Difficulté** : moyen

### File avec pile

On reprend l'[exercice sur la création d'une file avec 2 piles](../structure-flux/#file-avec-pile){.interne}.

{% exercice %}
Montrer que la complexité amortie d'ajout et de suppression d'un élément dans la structure de file créée avec 2 pile est en $\mathcal{O}(1)$
{% endexercice %}
{% details "corrigé" %}
On procède comme pour le compteur, on associe une complexité amortie de +2 lorsque l'on empile dans P1 et de 0 lorsque l'on empile dans P2.

{% enddetails %}

### Parenthésage

Soit $C$ une expression arithmétique avec des parenthèses et des crochets. On cherche à savoir si le parenthésage est équilibré :

- `[3 + 3 * (1 + 3)]` sera Ok
- `[3 + 3 * (1 + 3])` sera pas Ok

On ne vérifiera pas que l'expression est arithmétiquement correcte, c'est à dire que pour nous, `[3 + + 3 (1 + 3)]` sera Ok.

{% exercice %}

Montrer que l'on peut utiliser une pile pour savoir si un parenthésage est équilibré entre les `()` et les `[]`.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme parenthèse(C):
    P ← une nouvelle pile de caractères
    pour chaque c de C:
        si c == "(" ou c == "[":
            P.empile(c)
        sinon si c == ")":
            si P.vide() ou P.dépile() ≠ "(":
                rendre Faux
        sinon si c == "]":
            si P.vide() ou P.dépile() ≠ "[":
                rendre Faux
    rendre Vrai
```

{% enddetails %}

### Calcul d'une expression avec deux piles

Soit $C$ une expression arithmétique avec uniquement des parenthèses, des `+` et des `*`. On suppose qu'elle est arithmétiquement correcte, comme `(3 + 3 * (1 + 3))`

{% exercice %}

Montrer que l'on peut utiliser deux piles (une pour les opérateurs et les parenthèses et l'autre pour les nombres) pour calculer $C$.
{% endexercice %}
{% details "corrigé" %}

Il faut faire attention au fait que `*` a une priorité supérieure à `+` : `3 + 4 * 3 = 15`.

On lit l'expression de gauche à droite :

1. si le caractère lu est un nombre on le place dans la pile P2
2. sinon si le caractère lu est un opérateur O :
   1. on évalue l'expression comme on la fait avec la notation polonaise inversée :
      1. pop de P1 dans op
      2. pop de p2 dans y
      3. pop de p2 dans x
      4. x op y = z
      5. push de z dans P2
   2. jusqu'à ce que :
      1. P1 est vide ou
      2. l'opérateur O a une priorité supérieure à celle sur P1
   3. place O dans P1
3. sinon si le caractère lu est une parenthèse ouvrante : on la place dans P1
4. sinon si le caractère lu est une parenthèse fermante :
   1. on évalue l'expression jusqu'à trouver une parenthèse ouvrante
   2. on push le résultat dans P2

Si on a fini de lire l'expression on évalue le reste des deux piles.

{% lien %}
à 9min13  <https://www.youtube.com/watch?v=2vBVvQTTdXg>
{% endlien %}
{% enddetails %}

## <span id="2-3-sum"></span>2-sum et 3-sum

> - **Utilité** : un classique des concours !
> - **Difficulté** : dur

> TBD un classique des concours, sans aucune indications bien sur.

{% info %}

3-SUM est la base de bien d'autres problèmes. On en reparlera bien plus tard, mais ce problème est une des bases algorithmique de [la géométrie algébrique](https://fr.wikipedia.org/wiki/G%C3%A9om%C3%A9trie_alg%C3%A9brique).

{% endinfo %}

### <span id="2-sum"></span>2-SUM

{% note "Problème" %}

- **nom** : 2-SUM
- **données** : Un tableau T d'entiers relatifs
- **question** : Existe-t-il deux indices $i$ et $j$ (ils peuvent être égaux) tels que $T[i] + T[j] = 0$ ?
{% endnote %}

On a déjà vu une variante de ce problème lorsque l'on a étudié les dictionnaires. Si vous ne vous en rappelez plus, refaites le :

{% exercice %}
[Exercice fondamental des dictionnaires](../structure-dictionnaire/tableau-associatif/#exercice-fondamental){.interne}
{% endexercice %}

Regardons maintenant ce problème d'un point de vue complexité spatiale et temporelle.

{% exercice %}
Donnez une solution au problème 2-SUM avec comme complexité :

- temporelle de $\mathcal{O}(T.\mbox{\small longueur}^2)$
- spatiale en $\mathcal{O}(1)$

{% endexercice %}
{% details "corrigé" %}

> TBD : brute force

{% enddetails %}

{% exercice %}
Donnez une solution au problème 2-SUM avec comme complexité :

- temporelle de $\mathcal{O}(T.\mbox{\small longueur}\ln(T.\mbox{\small longueur}))$
- spatiale en $\mathcal{O}(T.\mbox{\small longueur})$

{% endexercice %}
{% details "corrigé" %}

> TBD : tri

{% enddetails %}

{% exercice %}
Donnez une solution au problème 2-SUM avec comme complexité :

- temporelle de $\mathcal{O}(T.\mbox{\small longueur})$ en moyenne
- spatiale en $\mathcal{O}(T.\mbox{\small longueur})$

{% endexercice %}
{% details "corrigé" %}

> TBD : dictionnaire

{% enddetails %}

Un nouvel algorithme :

{% exercice %}
Donnez une solution au problème 2-SUM avec comme complexité $\mathcal{O}(\max(T))$.

Est-ce réaliste ?

{% endexercice %}
{% details "corrigé" %}

> TBD : bucket sort de la valeur absolue. Dès que l'on rencontre la case la deuxième fois on sort.
> TBD attention : même si on ne visite pas toutes les cases du tableau il faut les initialiser à 0 (le contenu de la mémoire est inconnu à l'affectation).

> TBD complexité spatiale $\mathcal{O}(\max(T))$ ce qui est déraisonnable car cela peut être aussi grand que l'on veut.
> TBD c'est même exponentiel en la taille du tableau ($\log_2(n)$ bits pour stocker l'entier $n$).
> TBD : même si la complexité de créer un tableau de taille arbitraire est en  $\mathcal{O}(2)$, et que l'on ne fait de boucle que sur la taille du tableau, l'algorithme est tout de même en $\mathcal{O}(\max(T))$ car il faut initialiser les cases : à la création d'un tableau ses valeurs sont indéterminées.

{% enddetails %}

### <span id="3-sum"></span>3-SUM

{% note "Problème" %}

- **nom** : 3-SUM
- **données** : Un tableau T d'entiers relatifs
- **question** : Existe-t-il trois indices $i$, $j$ et $k$ (ils peuvent être égaux) tel que $T[i] + T[j] + T[k] = 0$ ?
{% endnote %}

{% exercice %}
Donnez une solution au problème 3-SUM avec comme complexité :

- temporelle de $\mathcal{O}(T.\mbox{\small longueur}^3)$
- spatiale en $\mathcal{O}(1)$

{% endexercice %}
{% details "corrigé" %}

> TBD : brute force

{% enddetails %}

{% exercice %}
Donnez une solution au problème 3-SUM avec comme complexité :

- temporelle de $\mathcal{O}(T.\mbox{\small longueur}^2)$ en moyenne
- spatiale en $\mathcal{O}(T.\mbox{\small longueur})$

{% endexercice %}
{% details "corrigé" %}

> TBD : dictionnaire

{% enddetails %}

Le dictionnaire est souvent la meilleure réponse en moyenne, mais ce n'est pas le cas avec un 3-SUM :

{% exercice %}
Donnez une solution au problème 3-SUM avec comme complexité :

- temporelle de $\mathcal{O}(T.\mbox{\small longueur}^2)$
- spatiale en $\mathcal{O}(T.\mbox{\small longueur})$

{% endexercice %}
{% details "corrigé" %}

> TBD : un tri puis on cherche en $\mathcal{O}(T.\mbox{\small longueur})$ s'il existe i et j pour lesquels $T[i] + T[j] = -T[k]$ pour k allant de 0 à la taille du tableau ($\mathcal{O}(T.\mbox{\small longueur})$ boucles)

{% enddetails %}

## Chaînes de caractères

> - **Utilité** : classique mais pas indispensable
> - **Difficulté** : ?

{% aller %}
[Chaines de caractères](./chaine-caracteres){.interne}
{% endaller %}

## Suites de caractères

> créer toutes les suite de caractères possibles.
> TBD On commence par afficher le tout

### 0/1

> TBD on utilise une fonction auxiliaire récursive  comme pour ds 1 2025

### Alphabet

> TBD on généralise

### liste

> TBD On stocke dans une liste.
>
> 1. variable globale hors algo
> 2. abec une liste et des appends

## Autres séries d'exercices

- <https://www.inf.usi.ch/carzaniga/edu/algo19s/exercises.pdf>
- ...
