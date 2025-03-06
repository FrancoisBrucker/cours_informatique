---
layout: layout/post.njk
title: "Structure de pile et file"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Lorsqu'un algorithme doit gérer un _flux_ de données (des données à traiter vont arriver tout au long de son exécution), il doit être capable de stocker les données arrivantes avant de pouvoir les traiter une à une.

{% note %}
Une structure de données permettant de gérer un flux de données doit avoir au moins trois méthodes :

- `push(donnée: type des données stockées) -> vide`{language-pseudocode} : une méthode de **stockage** d'une donnée dans la structure
- `pop() -> type des données stockées`{language-pseudocode} une méthode permettant de **rendre** une donnée stockée, la donnée est également supprimée de la structure
- `number() -> int`{language-pseudocode} une méthode permettant de connaître le nombre de données actuellement stockées dans la structure

{% endnote %}

Une structure générale serait alors (en ajoutant des méthodes pour savoir si la structure peut accueillir des données) :

```pseudocode
structure Flux:
    création(taille: entier) → Flux
    méthodes:
        méthode push(donnée: entier) → vide
        méthode pop() → entier
        méthode number() → entier
        méthode empty() → booléen  # Vrai si vide
        méthode full() → booléen   # Vrai si plein
```

Les structures de gestion de flux de données se distingue selon que la donnée rendue soit :

- la plus récente
- la plus ancienne
- la plus ancienne ou la plus ancienne
- ...

{% info %}
La gestion de flux de données de priorités différentes sera vu plus tard, lorsque l'on étudiera les arbres.
{% endinfo %}

## La pile

La pile est la structure de données qui rend toujours la donné la plus récente :

{% aller %}
[La pile](pile){.interne}
{% endaller %}

## La file

La pile est la structure de données qui rend toujours la donné la plus ancienne :

{% aller %}
[La file](file){.interne}
{% endaller %}

## Variantes

Vous trouverez sûrement aussi quelques variantes de ce structures, comme les deques ou les listes chaînées :

{% aller %}
[Variantes](variantes){.interne}
{% endaller %}

## <span id="exercices"></span>Exercices

### Parités

On se donne une pile P1 contenant des entiers positifs.

{% exercice %}

Écrire un algorithme pour copier dans P2 les nombres pairs contenus dans P1. Le contenu de P1 après exécution de l’algorithme doit être identique à celui avant exécution. Les nombres pairs dans P2 doivent être dans l’ordre où ils apparaissent dans P1 .
{% endexercice %}
{% details "corrigé" %}

On utilise une autre pile où on va placer tous les nombres impairs :

```pseudocode
P3 ← une pile d'entier de taille P1.longueur

tant que P1.vide() est Faux:
    x ← P1.dépiler()
    si x est pair:
        P2.empiler(x)
    sinon:
        P3.empiler(x)

tant que P3.vide() est Faux:
    x ← P3.dépiler()
    P1.empiler(x)
```

{% enddetails %}

### Palindromes

{% exercice %}
Montrer que l'on peut trouver si une chaîne de caractères est un palindrome en utilisant une pile et une file.
{% endexercice %}
{% details "corrigé" %}

```pseudocode
algorithme palindrome(s: chaîne) → booléen:
    P ← une pile de caractères
    F ← une file de caractères

    pour chaque c de s:
        P.empile(c)
        F.enfile(c)
    
    tant que P.vide() est Faux:
        c1 ← P.dépile()
        c2 ← F.défile()

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
En utilisant uniquement une file, donnez un algorithme de complexité $\mathcal{O}(T.\mbox{\small longueur})$ permettant de procéder à une permutation circulaire de $T$ de $k$ éléments ($T'[(i + k) \mod T.\mbox{\small longueur}] = T[i]$ pour tout $i$) **in place** (on doit modifier $T$).
{% endexercice %}

{% details "corrigé" %}

```pseudocode
F une file d'entier de taille T.longueur

pour chaque i de [0, T.longueur[:
    F.enfiler(T[i])
répéter k fois:
    x ← F.défile()
    F.enfile(x)

pour chaque i de [0, T.longueur[:
    x ← F.défile()
    T[i] ← x

```

{% enddetails %}

### Pile et file

On dispose uniquement de la structure de donnée de Pile et on souhaite créer, en utilisant deux piles P1 et P2, une nouvelle structure de File.

{% exercice %}

Écrire la structure de File en utilisant uniquement 2 piles en attributs.

{% endexercice %}
{% details "corrigé" %}

```pseudocode
structure File:
    attributs:
        P1 : Pile d'entiers
        P2 : Pile d'entiers
        longueur: entier
    création(taille: entier) → File:
        P1 ← une nouvelle pile de taille entiers
        P2 ← une nouvelle pile de taille entiers
        longueur ← taille
    méthodes:
        méthode enfiler(donnée: entier) → vide:
            P1.empiler(donnée)
        méthode défiler() → entier:
            si P2.vide():
                tant que P1.vide() est Faux:
                    x ← P1.dépiler()
                    P2.empiler(x)
            rendre P2.dépiler()
        méthode vide() → booléen:
            rendre P1.vide() ET P2.vide()
        méthode pleine() → booléen:
            si P1.nombre() + P2.nombre() ≥ longueur:
                rendre Vrai
            rendre Faux
        méthode nombre() → entier:
            rendre P1.nombre() + P2.nombre()
```

{% enddetails %}
{% exercice %}

Quelle est la complexité de l'enfilage et du défilage avec cette structure ?
{% endexercice %}
{% details "corrigé" %}

L'enfilage sera toujours en $\mathcal{O}(1)$, mais le défilage peut prendre $\mathcal{O}({\small longueur})$ dans le pire des cas si la pile `P1`{.language-} est pleine et la pile `P2`{.language-} vide.

{% enddetails %}
