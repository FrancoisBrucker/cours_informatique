---
layout: layout/post.njk

title:  "DM 1 : palindromes"
authors:
    - François Brucker
---

Le but de ce DM est de trouver des palindromes dans un texte.

Il est composée de deux parties, la première correspondant à une analyse algorithmique et la seconde au code à fournir.

{% attention %}
Lorsque l'on demande de fournir un algorithme pour résoudre un problème, il faudra impérativement :

1. en donner le pseudo-code
2. démontrer :
   1. sa finitude
   2. qu'il est bine une solution au problème
3. en donner (en justifiant) sa complexité
{% endattention %}
{% attention %}
Pour le code python, il faudra impérativement :

- faire les tests unitaires de chaque fonction. Ils devront tous se lancer via la commande `python -m pytest`
- votre code doit posséder un programme principal. Même si vous ne faites pas tout le code demandé, faites un programme qui utilise vos fonctions pour résoudre le problème demandé.
{% endattention %}

> TBD ajouter exemples

## Palindrome

{% note "**Définition**" %}
Une chaîne de caractères `s`{.language-} de longueur $n > 0$ est un ***palindrome*** si : $s[i] = s[n-1-i]$ pour tout $0 \leq i < n$
{% endnote %}

### Problème du palindrome

{% faire %}

1. Explicitez le problème de la reconnaissance d'un palindrome par un problème de décision.
2. Donnez un algorithme de complexité linéaire (pour la taille de la chaîne en entrée) résolvant le problème le problème de reconnaissance. Cet algorithme sera de signature : `palindrome(s: str) -> bool`{.language-}
3. Démontrez que la complexité du problème de reconnaissance est linéaire pour la taille de la chaîne en entrée.

{% endfaire %}

### Propriétés

> TBD

1. Si une lettre toujours palindrome
2. si deux lettre pas toujours (explicite non palindrome de taille n)

1. si pair tout caractère est en nombre pair
2. si impair tout caractère est en nombre pair saut peut-être 1
3. ce n'est pas une cns

## Sous-palindrome

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
Un mot `s[i:j]` ($i < j$) d'une chaîne de caractères `s`{.language-} de longueur $n > 0$ est un ***sous-palindrome de `s`{.language-}*** si : $s[i:j]$ est un palindrome.
{% endnote %}

Commençons par une propriété triviale :

{% faire %}
Montrer que toute chaîne de caractères non vide admet un sous-palindrome.
{% endfaire %}

Poursuivons par un cas particulier :

{% faire %}
Montrer que toute chaîne de caractères de longueur supérieure ou égale à 3 composée par au plus 2 caractères différents admet un sous-palindrome de longueur au moins 2.
{% endfaire %}

### Problème des mots palindromiques

1. opti
2. existe si-et seulement si décision existe
3. algo pour résoudre opti utilisant le palindrome et qui vérifie que tout mot est palindrome.
   1. écrire, preuve et complexité.

{% faire %}

1. Explicitez le problème de la reconnaissance d'un sous-palindrome par un problème de décision.
2. Donnez un algorithme de complexité linéaire (pour la taille de la chaîne en entrée) résolvant le problème le problème de reconnaissance. Cet algorithme sera de signature : `palindrome(s: str) -> bool`{.language-}
3. Démontrez que la complexité du problème de reconnaissance est linéaire pour la taille de la chaîne en entrée.

{% endfaire %}

### propriétés

> TBD

1. il existe toujours un mot palindromique
2. si 2 lettres et s > 2, il existe toujours un mot palindromique de taille > 1.

### Résolution par programmation dynamique

1. algo qui remplit une matrice si (i, j) est un palindrome

passer de n3 à n2 par programmation dynamique

1. relation entre (i-1, j + 1) et (i, j)
2. en déduire que si on a tous ceux de longueur k, on a ceux de longueur k+2, lien avec la matrice de sous-palindromes ?
3. en déduire que l'on peut remplir la matrice en n2.
4. sous-mot est en n2

### mots palindromiques impairs

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

### chaîne #s

> ajout de #
> lien entres mots palindromiques de s et de #s
> parité des mots palindromiques de #s
> création de #s à partir de s
> Algo linéaire pour trouver le palindrome le plus grand
> Algo linéaire pour trouver le nombre de palindromes

## Code

> TBD

1. créez des mots aléatoires de taille $n$ à partir d'une chaîne alphabet $A$
2. texte :
   1. téléchargement et lecture (dossier courant)
   2. trick utf8
   3. uppercase et suppression espace
3. palindrome algo

1. télécharge fichier <https://www.gutenberg.org/ebooks/6099> Il faudra peut-être forcer le téléchargement, parfois chrome le bloque
2. charge fichier texte en python en entier et en une fois (pas plus)
3. <https://github.com/avian2/unidecode>
4. supprime espace
5. fonction
