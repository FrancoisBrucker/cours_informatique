---
layout: layout/post.njk 
title:  "Exercices Problème du doublon"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Le but de ces exercices est de résoudre le problème algorithmique suivant :

{% note "**Problème algorithmique**" %}

- Nom : Doppelganger
- Entrée : Un tableau de $n$ entiers compris entre 1 et $n-1$
- Sortie : Un entier $v$ tel qu'il existe $0\leq i\neq j < n$ avec $v = T[i] = T[j]$

{% endnote %}

Ce projet comportent deux parties : l'une algorithmique et l'autre dédiée au code et l'ordre de ses questions racontent une histoire. La suivre vous permettra, j'espère, de passer un bon moment algorithmique.

On vous demande de faire les différents exercices en respectant les consignes suivantes :

- Tout algorithme doit être donné en pseudocode et être démontré (finitude et correction).
- Toute fonction de code devra être testée.

## I. Prélude

Commençons par montrer que notre problème est bien défini et algorithmique :

### I.1 Existence

{% faire "**I.1.1**" %}

Démontrez que l'entier $v$ du problème _Doppelganger_ existe toujours.

{% endfaire %}
{% faire "**I.1.2**" %}

Démontrez que le problème _Doppelganger_ peut admettre plusieurs solutions.

{% endfaire %}

### I.2 Algorithme

Montrez que l'algorithme suivant permet de résoudre le problème _Doppelganger_ avec comme complexités :

- temporelle en $\mathcal{O}(n^2)$
- spatiale en $\mathcal{O}(1)$ (sans compter l'entrée)

```pseudocode
algorithme doppelganger_naif(T: [entier]) → entier:
    pour chaque (i := entier) de [0 .. T.longueur[:
        pour chaque (j := entier) de [i+1, T.longueur[:
            si T[i] == T[j]:
                rendre T[i]
```

### I.3 Complexité du problème

Le but du problème est de trouver une solution optimale au problème. Commençons par donner des bornes à celui-ci.

{% faire "**I.3.1**" %}

Montrer que la complexité temporelle du problème _Doppelganger_ est en $\Omega(n)$ et en $\mathcal{O}(n^2)$.

{% endfaire %}
{% faire "**I.3.2**" %}

Montrer que la complexité spatiale du problème _Doppelganger_ est en $\mathcal{O}(1)$ (sans compter l'entrée).

{% endfaire %}

### I.4 Simulation

On vous demande de  créer un projet vscode dans le dossier `doppelganger`{.fichier}. Ce projet contiendra :

- un fichier `doppelganger.py`{.fichier}
- un fichier `test_doppelganger.py`{.fichier} qui contiendra les tests des fonctions du fichier `doppelganger.py`{.fichier}
- autant de programmes principaux que demandé dans la suite du projet.


{% faire "**I.4.1 (vérification)**" %}

Créez une fonction python vérifiera qu'un tableau passé en paramètre est une entrée valide du problème doppelganger Qui devra rendre une entrée du problème. Sa signature doit être :

```pseudocode
doppelganger_valide(T: [int]) → bool
```

{% endfaire %}

{% faire "**I.4.2 (entrée)**" %}

Créez une fonction python qui devra rendre une entrée du problème. Sa signature doit être :

```pseudocode
doppelganger_entrée(n: int) → [int]
```

Vous ferez en sorte que la probabilité $\Pr(T[i] =  x)$ soit de $1/(n-1)$ quelques soient $x$ et $i$.

{% endfaire %}


{% info %}
Vous pourrez utiliser [la méthode `randrange`{.language-} du module `random`{.language-} ](https://docs.python.org/fr/3.14/library/random.html#random.randrange)
{% endinfo %}

{% faire "**I.4.3 (sortie)**" %}

Implémentez l'algorithme du I.2 dans une fonction de signature :

```pseudocode
doppelganger_naif(T: [int]) → int
```

{% endfaire %}

{% faire "**I.4.4 (programme principal)**" %}

Créez un programme principal dans un fichier `main_I.py`{.fichier} permettant à un utilisateur de rentrer une taille de tableau. Le programme devra :

1. rendre une sortie du problème Doppelganger
2. donner le temps mis par l'algorithme pour s'exécuter

{% endfaire %}


{% info %}
Vous pourrez utiliser [la technique présentée dans l'étude expérimentale du projet exponentiation](../projet-exponentiation/implémentation-code/#temporelle-comment-faire){.interne} pour mesurer le temps d'exécution de votre algorithme.
{% endinfo %}

## II. Une première borne

Affinons un peu la complexité de notre problème.

### II.1 Trié

{% faire "**II.1.1**" %}

Montrer que si le tableau en entrée du problème est trié, on peut résoudre le problème Doppelganger en temps linéaire.

{% endfaire %}

{% faire "**II.1.2**" %}

Implémentez un algorithme du II.1.2 dans une fonction de signature :

```pseudocode
doppelganger_tri(T: [int]) → int
```
Qui commence par trier la liste $T$ passée en entrée puis utilise votre algorithme du II.1.1 pour résoudre le problème.
{% endfaire %}
{% info %}
Vous pourrez lire [technique de tri](https://docs.python.org/fr/3.14/howto/sorting.html) du tutoriel python pour savoir comment trier une liste en python.
{% endinfo %}

{% faire "**II.1.3**" %}

Le tri utilisé par python est de complexité $\mathcal{O}(n\log(n))$. En déduire que le problème Doppelganger peut être résolu avec une complexité :

- temporelle en $\mathcal{O}(n\log(n))$
- spatiale en $\mathcal{O}(1)$ (sans compter l'entrée)

{% endfaire %}

{% faire "**II.1.4**" %}

Créez un programme principal dans un fichier `main_II.py`{.fichier} permettant à un utilisateur de rentrer une taille de tableau. Le programme devra :

1. rendre une sortie du problème Doppelganger
2. comparer les temps d'exécution des deux algorithmes `doppelganger_tri`{.language-} et `doppelganger_naif`{.language-}

{% endfaire %}

Expérimentalement, lorsque $n$ augmente, votre algorithme naif doit très souvent aller plus vite que votre algorithme qui tri au préalable votre tableau. Si cela n'arrive pas, faite une amélioration de votre algorithme naif pour que cela arrive.

{% faire "**II.1.5**" %}
Montrez que la probabilité que $T[0] \neq T[i]$ pour tout $i >0$ vaut $(1-1/(n-1))^n$
{% endfaire %}

En utilisant le fait que $\lim_{n\to +\infty}(1-1/(n-1))^n = 1/e$ :

{% faire "**II.1.6**" %}
Montrez que si $n$ est grand, il y a plus de 50% de chance que $T[0]$ soit répété.
{% endfaire %}
{% faire %}
Montrez que si $n$ est grand, quelle est la probabilité qu'aucun des 5 premiers éléments de soient répétés ?
{% endfaire %}
{% faire "**II.1.7**" %}
Montrez le expérimentalement en rendant le plus petit indice répété pour des tableaux de grande taille.
{% endfaire %}

Le résultat précédent est cependant statistique. IL existe des cas où notre algorithme naïf est effectivement plus lent que l'algorithme qui tri au préalable :

{% faire "**II.1.8**"%}

Donnez un tableau d'entré où le programme de tri est plus rapide que l'algorithme naïf et vérifiez le expérimentalement en ajoutant ce tableau à `main_II.py`{.fichier}.

{% endfaire %}


### II.2

Utilisons le fait que les entiers du tableau pour lequel il faut trouver le doublon sont entre 1 et n-1, soit les indices d'un tableau de taille $n$.

{% faire "**II.2.1**" %}

Montrez qu'en utilisant un tableau `B`{.language-} de $n$ booléens, on peut créer un algorithme permettant de résoudre le problème Doppelganger avec une complexité :

- temporelle en $\mathcal{O}(n)$
- spatiale en $\mathcal{O}(n)$ (sans compter l'entrée)

{% endfaire %}
{% faire "**II.2.2**" %}

Implémentez l'algorithme du II.2.1 dans une fonction de signature :

```python
doppelganger_bool(T: [int]) → int
```

Ajoutez au programme principal du fichier `main_II.py`{.fichier} le temps d'exécution de l'algorithme `doppelganger_bool`{.language-}.

{% endfaire %}

{% faire "**II.2.3**"%}

L'algorithme `doppelganger_bool`{.language-} est-il effectivement le plus rapide ?

{% endfaire %}


### II.3

{% faire "**II.3.1**" %}

Montrer que  pour le problème _Doppelganger_ :

- sa complexité temporelle du  est en $\Theta(n)$ 
- sa complexité spatiale de $\mathcal{O}(1)$ (sans compter l'entrée).

{% endfaire %}

{% faire %}

Quelle est (pour l'instant) la complexité spatiale de l'algorithme en $\mathcal{O}(n)$ et la complexité temporelle de l'algorithme de complexité spatiale $\mathcal{O}(1)$ ?

{% endfaire %}

On va montrer dans la suite qu'il existe un algorithme optimal pour les deux types de complexités en même temps !

Réfléchissez-y un instant avant de continuer. Pensez-vous que ce soit possible ?

## III. Interlude

Nous allons montrer que notre problème est équivalent à celui de [la recherche de points fixe d'une suite ultimement périodique](..//projet-complexité-problème/#point-fixe){.interne} que nous avons déjà étudié.

{% note2 "**Problème algorithmique**" %}

- Nom : Point fixe
- Entrées :
  - $f: [\\![ 1, n]\\!] \to [\\![ 1, n]\\!]$
  - $x \in [\\![ 1, n]\\!]$
- Sortie : Un entier positif $x'$ tel qu'il existe $u \neq v$ pour lesquels $f^u(x) = f^{v}(x) = x'$

{% endnote2 %}

Commençons par rappeler ce qu'est une suite ultimement périodique :

{% note2 "**Définition**" %}

Une suite $(a_i)_{0\leq i}$ est dite _ultimement périodique_ si il existe $\lambda$ et $\mu$ tels que :

- les valeurs $a_0$ à $a_{\lambda + \mu - 1}$ sont distinctes
- $a_{ n + \lambda} = a_{ n }$ pour tout $n\geq \mu$

{% endnote2 %}


Puis associons en une à $f$ :

{% faire  "**III.1.1**" %}

Montrez que si $f: [\\![ 1, n]\\!] \to [\\![ 1, n]\\!]$ et $x \in [\\![ 1, n]\\!]$ alors la suite $(a_i)_{0\leq i}$ définie telle que :

- $a_0 = x$
- $a_i = f(a_{i-1})$ pour $i>0$

est ultimement périodique.

{% endfaire %}
{% faire  "**III.1.2**" %}
Soit $f$ la fonction telle que $f(i) \coloneqq T[i]$ avec $T = [x, 1, 6, 2, 3, 4, 5]$. Donnez la suite associée lorsque $a_0 = T[0] = x$ pour $x$ allant de 1 à 6.

{% endfaire %}


### III.2

{% exercice  "**III.2.1**" %}
Adaptez l'algorithme du lièvre et de la tortue des suites ultimement périodiaque pour nos fonctions. Sa signature doit être `lièvre_tortue(f: (entier) → entier, x: entier) → entier`{.language-} avec :

- `f`{.language-} la fonction
- `x`{.language-} l'entier tel que $a_0 = f(x)$

{% endexercice %}
{% details "corrigé" %}
```pseudocode
programme lièvre_tortue(f: (entier) → entier,
                        x: entier
                       ) → entier:
    (tortue := entier) ← f(x)
    (lièvre := entier) ← f(f(x))

    tant que tortue ≠ lièvre:
        tortue ← f(tortue)
        lièvre ← f(f(lièvre))
    
    rendre tortue
```

{% enddetails %}
{% info %}
Vous aurez remarqué qu'un des paramètres du programme est une fonction. [Le type d'une fonction est sa signature](/cours/algorithmie/pseudo-code/algorithmes-fonctions/#type).
{% endinfo %}

{% faire  "**III.2.2**" %}
Montrez que la complexité de l'algorithme `lièvre_tortue`{.language-} est en $\mathcal{O}(n)$ si $f: [\\![ 1, n]\\!] \to [\\![ 1, n]\\!]$ ?
{% endfaire %}

### III.3

Nous allons coder cette partie. Pour cela, créez deux fichiers, `point_fixe.py`{.language-} et `test_point_fixe.py`{.language-}, dans lesquels vous créerez les fonctions demandées.

{% faire  "**III.3.1**" %}
Codez l'algorithme de la question III.2.2. Cet algorithme devra être de signature :

```pseudocode
lièvre_tortue(T: [entier]) -> entier
```

Le tableau en entrée `T`{.language-} sera un tableau de taille $n+1$ et composé d'entiers entre 1 et $n$ avec :

- $f(i) = T[i]$ pour tout $1\leq i \leq n$
- $x = T[0]$

{% endfaire %}
{% faire  "**III.3.2**" %}

Codez l'algorithme `mu` de l'exercice [recherche de points fixe d'une suite ultimement périodique](..//projet-complexité-problème/#point-fixe-mu){.interne} pour nos fonctions. Cet algorithme devra être de signature :

```pseudocode
mu(T: [entier]) -> entier
```

Le tableau en entrée `T`{.language-} sera un tableau de taille $n+1$ et composé d'entiers entre 1 et $n$ avec :

- $f(i) = T[i]$ pour tout $1\leq i \leq n$
- $x = T[0]$

{% endfaire %}

{% faire  "**III.3.2**" %}

Dans un nouveau programme principal `main_III.py`{.fichier}, demandez à un utilisateur de rentrer une taille $n$ de tableau. Le programme devra :

1. afficher un tableau créé aléatoirement avec `doppelganger_entrée(n + 1)`{.language-}
2. afficher la sortie de l'algorithme `lièvre_tortue`{.language-}
3. affiche la période de la suite ultimement périodique associée au tableau commençant avec $a_\mu$

{% endfaire %}

## IV. Solution optimale

Nous allons montrer dans cette partie que l'on peut résoudre le problème _Doppelganger_ avec un algorithme de complexité :

- temporelle en $\mathcal{O}(n)$
- spatiale en $\mathcal{O}(1)$ (sans compter l'entrée)

Cet algorithme sera alors optimal et en temps et en espace !

### IV.1

Soit ${(a_i)}_{i\geq 0}$ une suite ultimement périodique de paramètres $\mu > 0$ et $\lambda$.

{% faire  "**IV.1**" %}

Montrez que $f(a_{\mu - 1}) = f(a_{\mu + \lambda - 1})$ et en déduire que $a_\mu$ est une solution au problème _Doppelganger_ pour le tableau $T$ tel que :

- $T[0] = a_0$
- $f(i) = T[i]$ pour tout $1\leq i \leq n$
- $a_{i+1} = f(a_i)$

{% endfaire %}


### IV.2

{% faire  "**IV.2**" %}

Déduire de ce qui précède un algorithme permettant de résoudre le problème _Doppelganger_ avec un algorithme de complexité :

- temporelle en $\mathcal{O}(n)$
- spatiale en $\mathcal{O}(1)$ (sans compter l'entrée)

{% endfaire %}


### IV.3

On termine ce projet en implémentant tout ça !

#### IV.3.1

{% faire  "**IV.3.1**" %}

Ajoutez dans le fichier `doppelganger.py`{.fichier} un algorithme de signature :

```pseudocode
doppelganger_optimal(T: [entier]) -> entier
```

Qui résout de façon optimale en temps et en espace le problème _Doppelganger_.


{% endfaire %}
{% faire  "**IV.3.2**" %}

Créez un programme principal dans un fichier `main_IV.py`{.fichier} qui compare le temps mis pour résoudre le problème Doppelganger avec la version naive, triée et optimale pour une taille de tableau donnée par l'utilisateur et en utilisant 2 tableaux :

- un crée par `doppelganger_entrée`{.language-}
- l'autre dans le cas le pire pour l'algorithme naif **et** pour le tri

Vous devez expérimentalement retrouver l'ordre de complexité attendu pour le cas le pire.

{% endfaire %}
{% attention %}
Assurez vous d'être **effectivement** dans le cas le pire pour le tri ! Le tri de python est en effet en $\mathcal{O}(n)$ si le tableau initial est déjà presque trié et en $\mathcal{O}(n\log(n))$ sinon.

Pour éviter les effets de bords (non utilisation du tri et du coup algorithme avec le tri plus rapide que l'algorithme optimal), utilisez un exemple du II.1.6 pour le quel le tableau n'est pas déjà trié (vous pourrez utiliser la méthode [random.shuffle](https://docs.python.org/fr/3.13/library/random.html#random.shuffle) pour mélanger un tableau trié).

{% endattention %}
