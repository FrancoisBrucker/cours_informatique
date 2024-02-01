---
layout: layout/post.njk

title:  "Résolution du problème des (sous-)palindromes"
---

{% attention %}
Lorsque l'on demande de fournir un algorithme pour résoudre un problème, il faudra impérativement :

1. en donner le pseudo-code
2. démontrer :
   1. sa finitude
   2. qu'il est bien une solution au problème
3. en donner (en justifiant) sa complexité
{% endattention %}

Commençons par poser le problème du palindrome de façon algorithmique.

## Problème du palindrome

{% faire %}

Explicitez le problème de la reconnaissance d'un palindrome par un problème de décision.

{% endfaire %}

### Propriétés

Démontrez quelques propriétés qui seront utiles (ou juste intéressantes) plus tard :

{% faire %}

1. Démontrez qu'une chaîne de caractères composée uniquement d'un caractère est un palindrome
2. Démontrez que si une chaîne de longueur $n$ paire est un palindrome, alors chacun de ses caractères apparaît un nombre pair de fois.
3. Démontrez que si une chaîne de longueur $n$ impaire est un palindrome, alors :
   1. la chaîne $s$ privée de son caractère $s[(n-1)/2]$ est un palindrome,
   2. au plus 1 de ses caractères apparaît un nombre impair de fois.

{% endfaire %}

### Résolution du problème

<span id="palindrome_linéaire"></span>
{% faire %}
Proposez un algorithme de complexité linéaire (pour la taille de la chaîne en entrée) résolvant le problème le problème de reconnaissance d'un palindrome.

Cet algorithme devra être de signature : `palindrome(s: str) -> bool`{.language-}
{% endfaire %}

### Complexité du problème

{% faire %}

Démontrez que **la complexité du problème de reconnaissance** d'un palindrome est linéaire pour la taille de la chaîne en entrée.

{% endfaire %}

## Problème du sous-palindrome

Cette partie est consacrée à l'étude des mots palindromiques d'une chaîne de caractères. Commençons par définir ce qu'est ***un mot*** :

{% note "**Définition**" %}
Un mot $s[i:j]$ ($0 \leq i < j \leq n$) d'une chaîne de caractères $s=\text{"}s_0\dots s_{n-1}\text{"}$ est la chaîne :

<div>
$$
s[i:j] = s_i \dots s_{j-1}
$$
</div>

{% endnote %}

Puis de caractériser les mots palindromiques :

{% note "**Définition**" %}
Un mot $s[i:j]$ ($0 \leq i < j \leq n$) d'une chaîne de caractères $s$ de longueur $n > 0$ est un ***sous-palindrome de $s$*** si $s[i:j]$ est un palindrome.
{% endnote %}

Mettons cette définition en pratique :

{% faire %}
Explicitez tous les sous-palindromes de la chaîne : $s = \text{"babba"}$
{% endfaire %}

### Propriétés des sous-palindromes

{% faire %}

1. Montrez que toute chaîne de caractères non vide admet un sous-palindrome.
2. Montrez que toute chaîne de caractères de longueur supérieure ou égale à 3 composée d'au plus 2 caractères différents admet un sous-palindrome de longueur supérieure ou égale 2.
3. Montrez que pour tout $n>1$ et tout $m>2$, il existe une chaîne de caractères de longueur $n$ et de $m$ caractères différents ne contenant aucun sous-palindrome de longueur strictement supérieure à 1.

{% endfaire %}

### Problème des sous-palindromes

On considère le problème d'optimisation suivant :

{% note "**Problème**" %}

- **nom** : max-sous-palindrome
- **données** : $s$ une chaîne de caractères
- **question** : quelle est la longueur maximum des sous-palindromes de $s$ ?
{% endnote %}

Commençons par montrer que c'est bien un problème algorithmique :

{% note "**Problème**" %}

- **nom** : max-sous-palindrome
- **données** : $s$ une chaîne de caractères de taille $n>0$
- **question** : quelle est la longueur maximum des sous-palindromes de $s$ ?
{% endnote %}

{% faire %}

1. En utilisant l'algorithme linéaire `palindrome(s: str) -> bool`{.language-} sur chaque mot de $s$, montrez que le problème `max-sous-palindrome` est **un problème algorithmique** de complexité $\mathcal{O}(n^3)$.
2. Montrez que la complexité du problème `max-sous-palindrome` est en $\Omega(n)$, avec $n$ la taille de la chaîne passée en entrée.
3. Déduisez de la question précédente un encadrement de la complexité du problème `max-sous-palindrome`.
{% endfaire %}

Le but de la fin de la partie algorithmique de cette étude est de montrer que la complexité du problème est linéaire. Mais ne boudons pas notre plaisir et progressons par étapes. Commençons par passer d'une complexité de $\mathcal{O}(n^3)$ à $\mathcal{O}(n^2)$.

### Résolution par matrice interposée du problème des sous-palindromes

On va associer à la chaîne $s$ dont on veut trouver le plus grand sous-palindrome une [une matrice carrée triangulaire supérieure](https://fr.wikipedia.org/wiki/Matrice_triangulaire#Matrices_triangulaires_supérieures) qui va expliciter si le mot $s[i:j+1]$ est un sous-palindrome ou pas :

{% note "**Définition**" %}
Soit $M_s$ une matrice carrée à $n$ lignes ($M_s[i]$, $0 \leq i < n$, est un tableau représentant la ligne $i$ et $M_s[i][j]$, $0 \leq i, j < n$, correspond à la case de ligne $i$ et colonne $j$ de $M_s$) et $s$ une chaîne de caractères de longueur $n$.

La matrice $M_s$ est définie telle que

- pour $0\leq j < i <n$ :
  - $M_s[i][j] = 0$
- pour $0\leq i \leq j <n$ :
  - $M_s[i][j] = 1$ si $s[i:j+1]$ est un sous-palindrome de $s$,
  - $M_s[i][j] = 0$ sinon.

{% endnote  %}
Mettons cette définition en pratique :

{% faire %}
Explicitez $M_s$ pour la chaîne : $s = \text{"babba"}$
{% endfaire %}

#### Création de $M_s$

On peut facilement calculer les deux premières diagonales :

{% faire %}
Soit $s$ une chaîne de caractères de longueur $n$.

1. Créez une fonction de complexité $\mathcal{O}(n)$ qui prend en paramètres une matrice $M$ carrée à $n$ ligne et une chaîne de caractères $s$ de longueur $n$ et qui rend **la même matrice $M$** telle que :
   - $M[i][i] = M_s[i][i]$ pour $0\leq i < n$
   - $M[i][i+1] = M_s[i][i+1]$ pour $0\leq i < n-1$
2. Créez une fonction de complexité $\mathcal{O}(1)$ qui prend en paramètres $i$, $j$, $s$ et $M_s[i][j]$ et qui rend la valeur de $M_s[i-1][j+1]$ (on a bien sur $0 < i \leq j < n-1$).
3. Déduire des deux questions précédentes un algorithme de complexité $\mathcal{O}(n^2)$ qui prend $s$ en paramètre et la matrice $M_s$

{% endfaire %}

#### Résolution de `max-sous-palindrome` avec $M_s$

Cette matrice peut ensuite servir à résoudre le problème `max-sous-palindrome` :

{% faire %}

1. Créez une fonction de complexité $\mathcal{O}(n^2)$ qui prend en paramètre $M_s$ et rend la solution de `max-sous-palindrome` pour $s$,
2. Déduisez-en que le problème `max-sous-palindrome` est de complexité $\mathcal{O}(n^2)$.

{% endfaire %}

Notez qu'il n'y a pas de contradiction entre la première série de questions qui a montré que le problème `max-sous-palindrome` est de complexité $\mathcal{O}(n^3)$ et celles-ci qui montrent qu'elle est également de complexité $\mathcal{O}(n^2)$ puisque le comparateur asymptotique $\mathcal{O}()$ est un majorant.

#### Pourquoi ?

{% faire %}
Quelle est la raison pour laquelle la création et l'utilisation de la matrice $M_s$ est plus rapide que l'utilisation de la fonction `palindrome()` pour tous les sous-mots ?
{% endfaire %}

Et maintenant, le clou du spectacle, prouvons l'impossible : on peut passer d'une complexité de $\mathcal{O}(n^2)$ à de complexité de $\mathcal{O}(n)$. Avant de procéder aux questions suivantes qui vont vous guider vers une solution possible essayez quelques instants de trouver une solution par vous-même.

### Résolution linéaire du problème des sous-palindromes

L'algorithme que nous allons développer dans cette partie nécessite de n'avoir que des sous-palindromes de longueur impaire. Montrons qu'il est toujours possible de s'y ramener.

#### De $s$ à $s^\sharp$

{% note "**Définition**" %}
Soit $s =\text{"}s_0 \dots s_{n-1}\text{"}$ une chaîne de caractères et $\sharp$ un caractère non présent dans $s$. On note $s^\sharp$ la chaîne de caractères de longueur $2n+1$ telle que :

<div>
$$
s^\sharp = \text{"}\sharp s_0\sharp  \dots s_{i-1} \sharp s_i \sharp s_{i+1} \dots \sharp s_{n-1} \sharp\text{"}
$$
</div>
{% endnote  %}

Les sous-palindromes de $s$ et $s^\sharp$ sont liés :

{% faire %}
Montrez que :

1. Les sous-palindromes de $s^\sharp$ sont tous de longueurs impaires.
2. Il existe un sous-palindrome de taille $m>0$ dans $s$ si et seulement si il existe un sous-palindrome de taille $2m + 1$ dans $s^\sharp$.
3. Déduisez des deux questions précédentes que s'il existe un algorithme $A(s)$ de complexité $C(n)$ pour trouver le plus grand sous-palindrome de longueur impaire d'une chaîne $s$ de longueur $n$, on peut construire un algorithme de même complexité utilisant $A()$ qui résout `max-sous-palindrome`.

{% endfaire %}

#### Exemple

{% faire %}
En utilisant la chaîne de caractères $s = \text{"babba"}$, explicitez les sous-palindromes de la chaîne $s^\sharp$ de taille strictement supérieure à 1 et associez chacun à un sous-palindrome de $s$.
{% endfaire %}

#### Mots palindromiques impairs

Les palindromes de longueur impaire sont centrés autour d'un élément :

{% note "**Définition**" %}
Soit $s[i:j]$ un sous-palindrome de longueur impaire de $s$. On appelle :

- ***centre du sous-palindrome*** l'index $(i+j -1)/2$.
- ***rayon du sous-palindrome*** le nombre $(j-i -1)/2$.

{% endnote %}

{% faire %}
Explicitez le sous-palindrome $s^\sharp[2:11]$ ainsi que son centre et son rayon pour chaîne $s = \text{"babba"}$.
{% endfaire %}

Plutôt que de calculer tous les mot d'une chaîne et de vérifier s'ils sont palindromique on va chercher pour chaque centre le rayon maximal.

#### Tableau $T_s$

{% note "**Définition**" %}
Soit $s$ une chaîne de caractères. On note $T_s$ le tableau de taille $n$ tel que $T_s[i]$ est la taille du plus grand rayon d'un sous-palindrome de taille impaire centré en $i$.
{% endnote  %}

{% faire %}

1. Montrez que cette définition est valide : $T_s[i]$ est bien défini pour tout $s$ et tout centre $i$.
2. Montrez que $s[i-T_s[i]:i+T_s[i]+1]$ est un sous-palindrome de $s$
3. Explicitez $T_{s^\sharp}$ pour la chaîne $s = \text{"babba"}$.
4. Démontrez que le plus grand élément de $T_{s^\sharp}$ est la réponse au problème `max-sous-palindrome` pour $s$.

{% endfaire %}

#### Propriétés de $T_s$

Exhibons la propriété fondamentale de $T_s$ qui va nous permettre de le calculer rapidement.

{% faire %}

Montrez que pour tout $k \leq T_s[i]$ on a :

- $T_s[i + k] = T_s[i-k]$ si $T_s[i-k] \neq T_s[i]-k$
- $T_s[i + k] \geq T_s[i]-k$ sinon.

{% endfaire %}

#### Création de $T_s$

{% faire %}

Déduisez de la propriété précédente un algorithme de complexité $\mathcal{O}(n)$ permettant de créer $T_s$ à partir de $s$.

{% endfaire %}

#### Conclusion

{% faire %}

1. Donnez un algorithme de complexité $\mathcal{O}(n)$ permettant de résoudre le problème `max-sous-palindrome` pour une chaîne de caractères de longueur $n>0$.
2. Déduisez-en que la complexité du problème `max-sous-palindrome` est de $\Theta(n)$ pour une chaîne de caractères de longueur $n>0$.

{% endfaire %}

## Nombre de sous-palindromes

Un dernier problème pour la route :

{% note "**Problème**" %}

- **nom** : nombre-sous-palindrome
- **données** : $s$ une chaîne de caractères de taille $n>0$
- **question** : quel est le nombre de sous-palindromes de $s$ ?
{% endnote %}

{% faire %}

En utilisant l'algorithme linéaire pour calculer $T_s$, montrez que le problème `nombre-sous-palindrome` est de complexité $\mathcal{O}(n)$.

{% endfaire %}
