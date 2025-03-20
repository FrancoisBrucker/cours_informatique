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

Algorithmes classiques dont l'intérêt est à la fois esthétique (ce sont de jolis algorithmes),pratiques (ils mettent en oeuvre des techniques facilement réutilisables) et didactiques (trouver et prouver leurs fonctionnement vous fera progresser).

{% info %}
Pour tous ces exercices, si la structure de donnée n'est pas précisé, vous utiliserez des listes.
{% endinfo %}

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

## 2-sum et 3-sum

> - **Utilité** : un classique des concours !
> - **Difficulté** : dur

> TBD un classique des concours, sans aucune indications bien sur.

{% info %}

3-SUM est la base de bien d'autres problèmes. On en reparlera bien plus tard, mais ce problème est une des bases algorithmique de [la géométrie algébrique](https://fr.wikipedia.org/wiki/G%C3%A9om%C3%A9trie_alg%C3%A9brique).

{% endinfo %}

### 2-SUM

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

{% enddetails %}

### 3-SUM

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
