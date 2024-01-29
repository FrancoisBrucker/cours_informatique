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

## Palindrome

{% note "**Définition**" %}
Une chaîne de caractères `s`{.language-} de longueur $n > 0$ est un ***palindrome*** si : $s[i] = s[n-1-i]$ pour tout $0 \leq i < n$
{% endnote %}

{% faire %}

1. Explicitez le problème de la reconnaissance d'un palindrome par un problème de décision.
2. Donnez un algorithme de complexité linéaire (pour la taille de la chaîne en entrée) résolvant le problème le problème de reconnaissance. Cet algorithme sera de signature : `palindrome(s: str) -> bool`{.language-}
3. Démontrez que la complexité du problème de reconnaissance est linéaire pour la taille de la chaîne en entrée.

{% endfaire %}

## Sous-palindrome

Cette partie est consacrée à 

{% note "**Définition**" %}
Un mot `s[i:j]` ($i < j$) d'une chaîne de caractères `s`{.language-} de longueur $n > 0$ est un ***sous-palindrome de `s`{.language-}*** si : $s[i:j]$ est un palindrome.
{% endnote %}


## Code

> TBD

1. créez des mots aléatoires de taille $n$ à partir d'une chaîne alphabet $A$
2. texte :
   1. téléchargement et lecture (dossier courant)
   2. trick utf8
   3. uppercase et suppression espace
3. palindrome algo