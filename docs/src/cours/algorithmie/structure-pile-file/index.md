---
layout: layout/post.njk
title: "Structure de pile et file"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


> TBD liste circulaires.

Lorsqu'un algorithme doit gérer un _flux_ de données (des données à traiter vont arriver tout au long de son exécution), il doit être capable de stocker les données arrivantes avant de pouvoir les traiter une à une.

{% note %}
Une structure de données permettant de gérer un flux de données de type `Type`{.language-} (tout type fonctionne) doit avoir au moins trois méthodes :

- `push(donnée: Type) → vide`{language-pseudocode} : une méthode de **stockage** d'une donnée dans la structure
- `pop() → Type`{language-pseudocode} une méthode permettant de **rendre** une donnée stockée, la donnée est également supprimée de la structure
- `number() → int`{language-pseudocode} une méthode permettant de connaître le nombre de données actuellement stockées dans la structure

{% endnote %}

Une structure générale de flux d'entiers serait alors (en ajoutant des méthodes pour savoir si la structure peut accueillir des données) :

```pseudocode
structure Flux<T>:
    attributs:
        taille: entier

        # autres attributs dépendant de la structure réelle
    méthodes:
        fonction push(donnée: T) → ∅
        fonction pop() → T
        fonction number() → entier

        fonction empty() → booléen  # Vrai si vide
        fonction full() → booléen   # Vrai si plein
```

Les structures de gestion de flux de données se distinguent selon que la donnée rendue soit :

- la plus récente
- la plus ancienne
- la plus prioritaire
- ...

{% info %}
La gestion de flux de données de priorités différentes sera vu plus tard, lorsque l'on étudiera les arbres.
{% endinfo %}

## Pile

La pile est la structure de données qui rend toujours la donnée la plus **récemment** stockée :

{% aller %}
[La pile](pile){.interne}
{% endaller %}

## File

La pile est la structure de données qui rend toujours la donné la plus **anciennement** stockée :

{% aller %}
[La file](file){.interne}
{% endaller %}

## Deques

Souvent, la pile et la file sont réunies en une seule structure : [le **_deque_** (_"doubled ended queue"_)](https://en.wikipedia.org/wiki/Double-ended_queue).

{% exercice %}
Montrer que l'on peut facilement ajouter les méthodes `empile` et `depile` des piles à notre [structure de file](./file.md/#structure).
{% endexercice %}
{% details "corrigé" %}

```pseudocode
structure Deque<Type>:
    attributs:
        taille: entier

        T: [Type] ← Tableau de longueur taille
        début: entier ← taille - 1
        fin: entier ← 0
    méthodes:
        fonction empile(donnée: Type) → ∅:
            T[fin] ← donnée
            fin ← (fin + 1) % longueur
        fonction dépile() → Type:
            fin ← (fin - 1 + longueur) % longueur
            rendre T[fin]

        fonction enfile(donnée: Type) → ∅:
            T[fin] ← donnée
            fin ← (fin + 1) % longueur
        fonction defile() → Type:
            début ← (début + 1) % longueur
            rendre T[début]
        fonction nombre() → entier:
            rendre (fin - début - 1 + taille) % taille

        fonction vide() → booléen:
            si nombre() == 0:
                rendre Faux
            rendre Vrai
        fonction pleine() → booléen:
            si (nombre() == taille):
                rendre Vrai
            rendre Faux
```

{% enddetails %}

C'est souvent la structure de Deque qui est utilisée par défaut et remplace les structures de pile et file car elle combine les deux structures sans perte de complexité.

{% info %}
En python, c'est [la classe deque](https://docs.python.org/fr/3.13/library/collections.html#collections.deque) du module [collections](https://docs.python.org/fr/3.13/library/collections.html) qui contient une série de classes implémentant des structures de données utiles.

{% endinfo %}

## <span id="exercices"></span>Exercices

### Parités

On se donne deux piles :

- `P1`{.language-} contenant des entiers positifs
- `P2`{.language-} une pile d'entier initialement vide

{% exercice %}

Écrire un algorithme pour copier dans une pile d'entiers `P2`{.language-} les nombres pairs contenus dans `P1`{.language-}.

- Le contenu de `P1`{.language-} après exécution de l’algorithme doit être identique à celui avant exécution.
- Les nombres pairs dans `P2`{.language-} doivent être dans l’ordre où ils apparaissent dans `P1`{.language-}.

{% endexercice %}
{% details "corrigé" %}

On utilise une troisième pile où on va placer tous les nombres impairs :

```pseudocode
algorithme parité(P1: Pile<entier>, P2: Pile<entier>) → ∅:
    P3 ← Pile<entier> {taille: P1.longueur}

    tant que P1.vide() est Faux:
        x ← P1.depile()
        si x est pair:
            P2.empile(x)
        sinon:
            P3.empile(x)

    tant que P3.vide() est Faux:
        x ← P3.depile()
        P1.empile(x)
```

{% enddetails %}

### Palindromes

{% exercice %}
Montrer que l'on peut trouver si une chaîne de caractères est un palindrome en utilisant une pile et une file.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme palindrome(s: chaîne) → booléen:
    P ← Pile<caractère> {taille: longueur de s}
    F ← File<caractère> {taille: longueur de s}

    pour chaque c de s:
        P.empile(c)
        F.enfile(c)

    tant que P.vide() est Faux:
        c1 ← P.depile()
        c2 ← F.defile()

        si c1 ≠ c2:
            rendre Faux
    rendre Vrai
```

L'algorithme est correct puisque la pile va dépiler de la fin vers le début et la file du début vers la fin.
{% enddetails %}
{% exercice %}
Donnez la complexité de votre algorithme.
{% endexercice %}
{% details "corrigé" %}
Les méthodes des piles et des files sont toutes en $\mathcal{O}(1)$ opérations, l'algorithme précédent est de complexité $\mathcal{O}(|s|)$.

{% enddetails %}

### Permutation circulaire

Soit $T$ un tableau d'entier.

{% exercice %}
En utilisant uniquement une file, donnez un algorithme de complexité $\mathcal{O}(T.\mbox{\small longueur})$ permettant de procéder à une permutation circulaire de $T$ de $k$ éléments ($T'[(i + k) \bmod T.\mbox{\small longueur}] = T[i]$ pour tout $i$) **in place** (on doit modifier $T$).
{% endexercice %}

{% details "corrigé" %}

```pseudocode
algorithme permutation(T: [entier], k: entier) → ∅:
    F ← File<entier> {taille: T.longueur}

    pour chaque i de [0 .. T.longueur[:
        F.enfile(T[i])
    répéter k fois:
        x ← F.defile()
        F.enfile(x)

    pour chaque i de [0 .. T.longueur[:
        T[i] ← F.défile()

```

{% enddetails %}

### <span id="file-avec-pile"></span>Pile et file

On dispose uniquement de la structure de donnée de Pile et on souhaite créer, en utilisant deux piles `P1`{.language-} et `P2`{.language-}, une nouvelle structure de File.

{% exercice %}

Écrire la structure de File en utilisant uniquement 2 piles en attributs.

{% endexercice %}
{% details "corrigé" %}

```pseudocode
structure File<T>:
    attributs:
        taille: entier

        P1 : Pile<T> {taille: taille}
        P2 : Pile<T> {taille: taille}
    méthodes:
        fonction enfile(donnée: T) → vide:
            P1.empiler(donnée)
        fonction defile() → T:
            si P2.vide():
                tant que P1.vide() est Faux:
                    x ← P1.dépiler()
                    P2.empiler(x)
            rendre P2.dépiler()
        fonction nombre() → entier:
            rendre P1.nombre() + P2.nombre()

        fonction vide() → booléen:
            rendre P1.vide() et P2.vide()
        fonction pleine() → booléen:
            si P1.nombre() + P2.nombre() ≥ longueur:
                rendre Vrai
            rendre Faux
```

{% enddetails %}
{% exercice %}

Quelle est la complexité de l'enfilage et du défilage avec cette structure ?
{% endexercice %}
{% details "corrigé" %}

L'enfilage sera toujours en $\mathcal{O}(1)$, mais le défilage peut prendre $\mathcal{O}({\small longueur})$ dans le pire des cas si la pile `P1`{.language-} est pleine et la pile `P2`{.language-} vide.

{% enddetails %}



## TBD

## Piles

> - **Utilité** : les piles ça sert toujours. Ces exercices vous montrerons des cas classiques d'utilisation
> - **Difficulté** : dur

### Parenthésage

> TBD rappel de l'exo non corrigé. vois que sa complexité est grande et faire avec pile.

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


### Élément majoritaire

> TBD
> naif
> tri
> pile

## Liste chaînée

> TBD à déplacer plus loin.
> TBD dire base des algos récursifs.
> TBD donner le type récursif associé.

> TBD reprendre exercices suppression/ head, tail , rendre éléments pair et impair/ retournements
> TBD : knuth dancing links <https://www.youtube.com/watch?v=_cR9zDlvP88>

## Autre structures

- skip list
- listes triées : pas évident de pourquoi on fait ça : ie réduire le coup d'insertion. Reprendre l'idée du compteur. Exercice 3 : <https://perso.ens-lyon.fr/laureline.pinault/Algo1/TD06-correction.pdf>
