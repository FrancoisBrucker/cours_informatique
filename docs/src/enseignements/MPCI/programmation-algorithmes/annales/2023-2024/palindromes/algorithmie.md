---
layout: layout/post.njk

title:  "Résolution du problèmes des (sous-)palindromes"
---

{% attention %}
Lorsque l'on demande de fournir un algorithme pour résoudre un problème, il faudra impérativement :

1. en donner le pseudo-code
2. démontrer :
   1. sa finitude
   2. qu'il est bine une solution au problème
3. en donner (en justifiant) sa complexité
{% endattention %}

Commençons par poser le problème du palindrome de façon algorithmique.

## Problème du palindrome

{% faire %}

Explicitez le problème de la reconnaissance d'un palindrome par un problème de décision.

{% endfaire %}

### Résolution du problème

{% faire %}
Proposez un algorithme de complexité linéaire (pour la taille de la chaîne en entrée) résolvant le problème le problème de reconnaissance d'un palindrome.

Cet algorithme devra être de signature : `palindrome(s: str) -> bool`{.language-}
{% endfaire %}

### Complexité du problème

{% faire %}

Démontrez que **la complexité du problème de reconnaissance** d'un palindrome est linéaire pour la taille de la chaîne en entrée.

{% endfaire %}

### Propriétés

Démontrez quelques propriétés qui seront utiles (ou juste intéressante) plus tard :

{% faire %}

1. Démontrez qu'une chaîne de caractères composée uniquement d'un caractère est un palindrome,
2. Démontrez que pour un palindrome tout caractère, à part peut-être 1, apparaît un nombre pair de fois.

{% endfaire %}

### Création de palindromes

{% faire %}

Proposez un **algorithme récursif** de signature `aléatoire_palindrome_rec(s: str, n: int) -> bool`{.language-} qui rend un palindrome aléatoire de longueur $n$ formé uniquement avec les caractères de `s`{.language-}.

En supposant que la complexité de concaténation d'une chaîne et d'un caractère soit en $\mathcal{O}(1)$, assurez vous que sa complexité soit en $\mathcal{O}(n)$.

{% endfaire %}

{% faire %}

Proposez un **algorithme itératif** de signature `aléatoire_palindrome_iter(s: str, n: int) -> bool`{.language-} qui rend un palindrome aléatoire de longueur $n$ formé uniquement avec les caractères de `s`{.language-}.

En supposant que la complexité de concaténation d'une chaîne et d'un caractère soit en $\mathcal{O}(1)$, assurez vous que sa complexité soit en $\mathcal{O}(n)$.

{% endfaire %}

## Problème du sous-palindrome

Cette partie est consacrée à l'étude des mots palindromiques d'une chaîne de caractères. Commençons par définir ce qu'est ***un mot*** d'une chaîne de caractères :

{% note "**Définition**" %}
Un mot $s[i:j]$ ($i < j$) d'une chaîne de caractères $s=s_0\dots s_{n-1}$ est la chaîne :

<div>
$$
s[i:j] = s_i \dots s_{j-1}
$$
</div>

{% endnote %}

Puis de caractériser les mots palindromiques :

{% note "**Définition**" %}
Un mot $s[i:j]$ ($i < j$) d'une chaîne de caractères `s`{.language-} de longueur $n > 0$ est un ***sous-palindrome de `s`{.language-}*** si : $s[i:j]$ est un palindrome.
{% endnote %}

### Propriétés des sous-palindromes

Commençons par une propriété triviale :

{% faire %}
Montrer que toute chaîne de caractères non vide admet un sous-palindrome.
{% endfaire %}

Poursuivons par un cas particulier :

{% faire %}
Montrer que toute chaîne de caractères de longueur supérieure ou égale à 3 composée d'au plus 2 caractères différents admet un sous-palindrome de longueur supérieure ou égale 2.
{% endfaire %}

Et enfin la non existence :

{% faire %}
Montrer que pour tout $n>1$ et tout $m>2$, il existe il existe une chaîne de caractères de longueur $n$ et de $m$ caractères différents ne contenant aucun sous-palindromes de longueur strictement supérieure à 1.
{% endfaire %}

### Problème des sous-palindromes

On considère le problème d'optimisation suivant :

{% note "**Problème**" %}

- **nom** : max-sous-palindrome
- **données** : $s$ une chaîne de caractères
- **question** : Quel est la longueur maximum des sous-palindromes de $s$ ?
{% endnote %}

Commençons par montrer que c'est bien un problème algorithmique :

{% note "**Problème**" %}

- **nom** : max-sous-palindrome
- **données** : $s$ une chaîne de caractères de taille $n>0$
- **question** : Quel est la longueur maximum des sous-palindromes de $s$ ?
{% endnote %}

{% faire %}

En utilisant l'algorithme linéaire `palindrome(s: str) -> bool`{.language-}, montrer que le problème `max-sous-palindrome` est **un problème algorithmique** en exhibant un algorithme (simple) de complexité $\mathcal{O}(n^3)$ pour le résoudre.
{% endfaire %}

Et donnez une borne minimum du problème :

{% faire %}

Montrer que la complexité du problème `max-sous-palindrome` est en $\Omega(n)$, avec $n$ la taille de la chaîne passée en entrée.
{% endfaire %}

Le but de la fin de la partie algorithmique de ce DM est de montrer que la complexité du problème est linéaire. Mais ne boudons pas notre plaisir et progressions pas étapes. Commençons par passer de $\mathcal{O}(n^3)$ à $\mathcal{O}(n^2)$.

### Résolution par matrice interposée du problème des sous-palindromes

On suppose que l'on possède [une matrice carrée triangulaire supérieure](https://fr.wikipedia.org/wiki/Matrice_triangulaire#Matrices_triangulaires_sup%C3%A9rieures) $P(s)$ à $n$ lignes, associée à la chaîne de caractères $s$ (de longueur $n$), définie telle telle que :

- $P(s)[i][j] = 1$ si $s[i:j+1]$ est un sous-palindrome de $s$ (donc il faut que $i\leq j$)
- $P(s)[i][j] = 0$ sinon

> TBD exemple

On peut facilement calculer les deux premières diagonales :

{% faire %}
Montrer que l'on peut facilement calculer $P(s)[i][i]$ et $P(s)[i][i+1]$ pour tout $i$.
{% endfaire %}

De plus, il existe une relation simple entre les autres éléments de la matrice :

{% faire %}
Montrer que l'on peut facilement calculer (en $\mathcal{O}(1)$) $P(s)[i][j]$ à partir de $P(s)[i+1][j-1]$ si $0 \leq i < j + 1$.
{% endfaire %}

En déduire un algorithme de création de la matrice $P(s)$ :

{% faire %}

Donner un algorithme qui construit la matrice $P(s)$ en $\mathcal{O}(n^2)$ instructions, avec $n$ la longueur de la chaîne de caractères $s$.
{% endfaire %}

Cette matrice peut ensuite servir à résoudre le problème `max-sous-palindrome` :

{% faire %}
Déduire des parties précédentes que l'on peut résoudre le problème `max-sous-palindrome` en $\mathcal{O}(n^2)$ instructions.
{% endfaire %}

Et maintenant, le clou du spectacle, prouvons l'impossible : on peut passer de $\mathcal{O}(n^2)$ à $\mathcal{O}(n)$.

### Résolution linéaire du problème des sous-palindromes

L'algorithme que nous allons développer dans cette partie nécessite de n'avoir que des sous-palindromes de longueur impair. Montrons qu'il est toujours possible de s'y ramener

#### De $s$ à $s^\sharp$

{% note "**Définition**" %}
Soit $s =s_0 \dots s_{n-1}$ une chaîne de caractères et $\sharp$ un caractère non présent dans $s$. On note $s^\sharp$ la chaîne de caractères de longueur $2n+1$ telle que :

<div>
$$
s^\sharp = \sharp s_0\sharp  \dots s_{i-1} \sharp s_i \sharp s_{i+1} \dots \sharp s_{n-1} \sharp
$$
</div>
{% endnote  %}

Les sous-palindromes de $s$ et $s^\sharp$ sont liés :

{% faire %}
Montrer que :

1. les sous-palindromes de $s^\sharp$ sont tous de longueurs impaires
2. il existe un sous-palindrome de taille $m$ dans $s$ si et seulement si il existe un sous-palindrome de taille $2m + 1$ dans $s^\sharp$
{% endfaire %}

Cette correspondance permet de déduire que :

{% faire %}

Montrer que s'il existe un algorithme de complexité $C(n)$ pour trouver le plus grand sous-palindrome de longueur impair d'une chaîne $s$ de longueur $n$, il existe un autre algorithme de même complexité pour résoudre `max-sous-palindrome` avec la même complexité.

{% endfaire %}

#### Mots palindromiques impairs

Les palindromes de longueur impair sont centrées autour d'un élément. On appelle ***rayon***

> TBD faire mieux
On considère alors le tableau :

{% note "**Définition**" %}
Soit $s =s_0 \dots s_{n-1}$ une chaîne de caractères. On note $M_s$ le tableau de taille $n$ tel que $M_s[i]$ soit la taille du plus grand rayon sous-palindrome de taille impair centrée en $s_i$ pour $s$.
{% endnote  %}

> TBD exemple

Le tableau $M_s$ possède une propriété très intéressante :

{% faire %}
Démontrez que pour tous $i < j \leq i + M_s[i]$, on a :

<div>
$$
M_s[j] \geq \max 
$$
</div>
{% endfaire %}

palindrome (i,+k)

1. en n trouver le palindrome de taille max centré en x
2. en déduire n2 qui rend un tableau K ou K[i] est la longueur max du rayon pour i
3. en déduire n2 qui rend le nombre de palindromes impairs

On peut faire mieux.

(i, +k) un palindrome impair de taille max et on connaît  (i-u,+k')

que vaut (i+u,+k'') si :

- k' < k-u
- k' > k-u

Que faire si k' = k-u pour déterminer k''.

Faire un algo `suivant`{.language-} qui :

1. rend le premier élément i'' tel que k'=k-u ou i + k + 1.
2. que vaut K[i'] pour i < i' < i''
3. K[i''] >= K[i]

En déduire un algorithme linéaire pour rendre K (pour justifier de la linéarité, on pourra  remarquer que i'+K[i'] est croissant et $i' > i$ pour chaque sortie de l'algo `suivant(i)`{.language-})

## Nombre de sous-palindromes

> TBD : compter le nombre de sous-palindromes d'une chaine