---
layout: layout/post.njk

title:  "Projet Doppelganger"
authors:
    - François Brucker
---

Le but du projet est de résoudre le problème algorithmique suivant :

{% note "**Problème algorithmique**" %}

- Nom : Doppelganger
- Entrée : Un tableau de $n$ entiers compris entre 1 et $n-1$
- Sortie : Un entier $v$ tel qu'il existe $0\leq i\neq j < n$ avec $v = T[i] = T[j]$

{% endnote %}

## Rendu

Le projet comporte deux partie : l'une algorithmique et l'autre dédiée au code.

Il faudra rendre la partie algorithmique sous la forme d'un fichier markdown et la partie développement sous la forme d'un projet informatique.

### Ordre des questions

Le but du projet est de faire les questions dans l'ordre. Non seulement les questions se suivent, mais elles racontent une histoire. La suivre vous permettra, j'espère, de passer un bon moment algorithmique.

### Partie algorithmique

Tout algorithme doit être donné en pseudocode et être démontré (finitude et correction).

### Partie code

Toute fonction devra être testée.

## I. Prélude

Commençons par montrer que notre problème est bien défini et algorithmique.

### I.1 Existence

#### I.1.1

{% faire %}

Démontrez que l'entier $v$ du problème _Doppelganger_ existe toujours.

{% endfaire %}

#### I.1.2

{% faire %}

Démontrez que le problème _Doppelganger_ peut admettre plusieurs solutions.

{% endfaire %}

### I.2 Algorithme

Montrez que l'algorithme suivant permet de résoudre le problème _Doppelganger_ avec comme complexités :

- temporelle en $\mathcal{O}(n^2)$
- spatiale en $\mathcal{O}(1)$ (sans compter l'entrée)

```pseudocode
algorithme doppelganger_naif(T: [entier]) → entier:
    pour chaque i de [0, T.longueur -1 ]:
        pour chaque j de [i+1, T.longueur -1 ]:
            si T[i] == T[j]:
                rendre T[i]
```

### I.3 Complexité du problème

Le but du problème est de trouver une solution optimale au problème. Commençons par donner des bornes à celui-ci.

#### I.3.1

Montrer que la complexité temporelle du problème _Doppelganger_ est en $\Omega(n)$ et en $\mathcal{O}(n^2)$.

#### I.3.2

Montrer que la complexité spatiale du problème _Doppelganger_ est en $\Theta(1)$ (sans compter l'entrée).

### I.4 Simulation

On vous demande de  créer un projet vscode dans le dossier `doppelganger`{.fichier}. Ce projet contiendra :

- un fichier `doppelganger.py`{.fichier}
- un fichier `test_doppelganger.py`{.fichier} qui contiendra les tests des fonctions du fichier `doppelganger.py`{.fichier}
- autant de programmes principaux que demandé dans la suite du projet.

#### I.4.1 Vérification

Créez une fonction python vérifiera qu'un tableau passé en paramètre est une entrée valide du problème doppelganger Qui devra rendre une entrée du problème. Sa signature doit être :

```python
doppelganger_valide(T: [int]) → bool
```

#### I.4.2 Entrée

Créez une fonction python Qui devra rendre une entrée du problème. Sa signature doit être :

```python
doppelganger_entrée(n: int) → [int]
```

Vous ferez en sorte que la probabilité que T[i] soit égal à x soit de 1/(n-1) quelque soient x et i.

#### I.4.3 Sortie

Implémentez l'algorithme du I.2 dans une fonction de signature :

```python
doppelganger_naif(T: [int]) → int
```

#### I.4.4 programme principal

Créez un programme principal dans un fichier `main_I.py`{.fichier} permettant à un utilisateur de rentrer une taille de tableau. Le programme devra :

1. rendre une sortie du problème Doppelganger
2. donner le temps mis par l'algorithme pour s'exécuter

## II. Une première borne

Affinons un peu la complexité de notre problème.

### II.1 Trié

#### II.1.1

Montrer que si le tableau en entrée du problème est trié, on peut résoudre le problème Doppelganger en temps linéaire.

#### II.1.2

Déduire de la question précédente un algorithme modifiant le tableau en entrée et résolvant le problème Doppelganger avec une complexité :

- temporelle en $\mathcal{O}(n\log(n))$
- spatiale en $\mathcal{O}(1)$ (sans compter l'entrée)

#### II.1.3

Implémentez l'algorithme du II.1.2 dans une fonction de signature :

```python
doppelganger_tri(T: [int]) → int
```

#### II.1.4

Créez un programme principal dans un fichier `main_II.py`{.fichier} permettant à un utilisateur de rentrer une taille de tableau. Le programme devra :

1. rendre une sortie du problème Doppelganger
2. comparer les temps d'exécution des deux algorithmes `doppelganger_tri`{.language-} et `doppelganger_naif`{.language-}

#### II.1.5

Expérimentalement, votre algorithme naif doit très souvent aller plus vite que votre algorithme qui tri au préalable votre tableau. Si cela n'arrive pas, faite une amélioration de votre algorithme naif pour que cela arrive.

Pourquoi ?

#### II.1.6

Donnez un tableau d'entré où le programme de tri est plus rapide que l'algorithme naïf.

### II.2

Utilisons le fait que les entiers dont sont composés le tableau pour lequel il faut trouver le doublon sont entre 0 et n-1, soit les indices d'un tableau de taille $n$.

#### II.2.1

Montrez qu'en utilisant un tableau `B`{.language-} de taille $n$ de booléens, on peut créer un algorithme permettant de résoudre le problème Doppelganger avec une complexité :

- temporelle en $\mathcal{O}(n)$
- spatiale en $\mathcal{O}(n)$ (sans compter l'entrée)

#### II.2.2

Implémentez l'algorithme du II.2.1 dans une fonction de signature :

```python
doppelganger_bool(T: [int]) → int
```

Ajoutez au programme principal du fichier `main_II.py`{.fichier} le temps d'exécution de l'algorithme `doppelganger_bool`{.language-}.

#### II.2.3

L'algorithme `doppelganger_bool`{.language-} est-il effectivement le plus rapide ?

### II.3

Utilisez la question II.2.3 pour montrer que la complexité temporelle du problème _Doppelganger_ est en $\Theta(n)$ et la complexité spatiale de $\mathcal{O}(1)$ (sans compter l'entrée).

Quelle est (pour l'instant) la complexité spatiale de l'algorithme en $\mathcal{O}(n)$ et la complexité temporelle de l'algorithme de complexité spatiale $\mathcal{O}(1)$ ?

{% info %}
On va montrer dans la suite qu'il existe un algorithme optimal pour les deux types de complexités en même temps !

Réfléchissez-y un instant avant de continuer. Pensez-vous que ce soit possible ?
{% endinfo %}

## III. Interlude

Prenons un petit moment pour analyser un autre problème.

{% note "**Problème algorithmique**" %}

- Nom : Période
- Entrées :
  - $f: [\\![ 1, n]\\!] \to [\\![ 1, n]\\!]$
  - $x \in [\\![ 1, n]\\!]$
- Sortie : Deux entiers positifs $\lambda$ et $\mu$ tels que $f^\lambda(x) = f^{\lambda +\mu}(x)$

{% endnote %}

### III.1 Existence

Une suite $(a_i)_{0\leq i}$ est dite _ultimement périodique_ si il existe $\lambda$ et $\mu$ tels que :

- les valeurs $a_0$ à $a_{\lambda + \mu - 1}$ sont distinctes
- $a_{ n + \lambda} = a_{ n }$ pour tout $n\geq \mu$

Une suite  ultimement périodique ressemble à un $\rho$ (rho) :

![rho](rho.png)

#### III.1.1

Donnez les $\lambda$ et $\mu$ pour la suite représentée par la figure précédente.

#### III.1.2

Montrez que si $(a_i)_{0\leq i}$ est ultimement périodique alors les entiers $\lambda$ et $\mu$ sont uniques.

#### III.1.3

Montrez que si $f: [\\![ 1, n]\\!] \to [\\![ 1, n]\\!]$ et $x \in [\\![ 1, n]\\!]$ alors la suite $(a_i)_{0\leq i}$ définie telle que :

- $a_0 = x$
- $a_i = f(a_{i-1})$ pour $i>0$

est ultimement périodique.

#### III.1.4

Donnez une fonction $f: [\\![ 1, n]\\!] \to [\\![ 1, n]\\!]$ telle que la suite ultimement périodique associée (comme en III.1.3) avec $a_0 = 1$ a le même $\rho$ que la figure.

#### III.1.5

Montrez que le problème _Période_ est bien un problème algorithmique.

### III.2

Soit $(a_i)_{0\leq i}$ une suite ultimement périodique de paramètres $\lambda$ et $\mu$.

#### III.2.1

Montrez qu'il existe $\lambda \leq m \leq \lambda +\mu$ tel que $a_{m} = a_{2m}$.

#### III.2.2

Montrez que programme suivant est un algorithme pour tout couple (f, x) entrée du problème du point fixe.

```pseudocode
programme lièvre_tortue(f: (entier) → entier,
                        x: entier
                       ) → entier:
    t ← f(x)
    l ← f(f(x))
    m ← 1
    tant que t ≠ l:
        t ← f(t)
        l ← f(f(l))
        m ← m + 1
    
    rendre m
```

{% info %}
Vous aurez remarqué qu'un des paramètres du programme est une fonction. [Le type d'une fonction est sa signature](/cours/algorithmie/pseudo-code/fonctions/#type).
{% endinfo %}

#### III.3.3

Montrer que l'algorithme `lièvre_tortue`{.language-} permet de retrouver $\lambda$ et $\mu$ pour une suite ultimement périodique définie comme en III.1.3 (vous pourrez utiliser un tableau auxiliaire comme en II.2.1).

#### III.3.4

Montrer que la complexité de l'algorithme `lièvre_tortue`{.language-} est en $\mathcal{O}(n)$ si $f: [\\![ 1, n]\\!] \to [\\![ 1, n]\\!]$.

### III.4

Nous allons coder cette partie. Pour cela, vous créerez deux fichiers, `point_fixe.py`{.language-} et `test_point_fixe.py`{.language-} dans lesquels vous créerez les fonctions demandées.

#### III.4.1

Créez la fonction de signature :

```pseudocode
suite_création(T: [entier]) -> ((entier) -> entier)
```

Le tableau en entrée `T`{.language-} sera tel que `1 ≤ T[i] < T.longueur`{.language-} et la fonction `f` de sortie sera telle que f(i) = T[i] pour tout `1 ≤ i < T.longueur`{.language-}.

Un test de cette fonction pourrait être :

```python
def test_suite_création():
    T = [0, 1, 3, 2, 6, 4, 5]
    f = suite_création(T)

    for i in range(1, len(T)):
        assert f(i) == T[i]
```

#### III.4.2

Implémentez l'algorithme de la question III.2.2.

#### III.4.3

Dans le programme `main_III.py`{.fichier}

#### III.4.4

Implémentez un algorithme permettant de résoudre le problème du point fixe.

#### III.4.5


> TBD à montrer $\rho$ et toute fonction de ce type
>  2 parties.
> lièvre et tortue
> application normale suite
> application crypto

## IV. Solution optimale

## Courbes
