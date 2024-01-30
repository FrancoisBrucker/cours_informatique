---
layout: layout/post.njk

title:  "Palindromes : le code"
---

> UN bout nécessite la partie algo, un autre non.

{% attention %}
Pour le code python, il faudra impérativement :

- faire les tests unitaires de chaque fonction. Ils devront tous se lancer via la commande `python -m pytest`
- votre code doit posséder un programme principal. Même si vous ne faites pas tout le code demandé, faites un programme qui utilise vos fonctions pour résoudre le problème demandé.
{% endattention %}

> TBD

1. créez des mots aléatoires de taille $n$ à partir d'une chaîne alphabet $A$
2. texte :
   1. téléchargement et lecture (dossier courant)
   2. trick utf8
   3. uppercase et suppression espace
3. palindrome algo

4. télécharge fichier <https://www.gutenberg.org/ebooks/6099> Il faudra peut-être forcer le téléchargement, parfois chrome le bloque
5. charge fichier texte en python en entier et en une fois (pas plus)
6. <https://github.com/avian2/unidecode>
7. supprime espace (ou même garde que les caractères A-Z ?`"".join(filter(lambda x: x.isalpha(), string))`{.language-}. Liste vers chaîne sinon va être trop long. Peut être aussi d'abord voir avec un ensemble tous les caractères, puis les caractères non alphabet)
8. fonction

> <https://www.arretetonchar.fr/wp-content/uploads/2013/IMG/pdf_Georges_Perec_le_grand_palindrome.pdf>

