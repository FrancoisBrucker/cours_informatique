---
layout: layout/post.njk

title: "Mono-lignes en python"
authors:
  - "Aristide Grange"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Les mono-lignes sont des petits exercices que l'on doit à Aristide Grange. Ils permettent de se creuser un peu la tête pour écrire de façon condensé du code python. 

{% info %}

[Le sujet initial](monolignes-questions.pdf){.interne} était fait pour une version 2 de python, la version ci-après est une adaptation à python 3.

{% endinfo %}
{% details "Si vous voulez faire le sujet initial avec une version actuelle de python" %}
Ce sujet initial montre aussi en creux les évolutions de python : 

- la fonction `print`{.language-} prend des parenthèses,
- les f-string sont apparues,
- `chr`{.language-} et `ord`{.language-} sont des code unicode maintenant
- la fonction `raw_input`{.language-} a disparu,
- `input`{.language-} n'évalue plus automatiquement les entrées, 
- la division de deux entiers rend un flottant par défaut,
- le 27e nombre de Mersenne n'est plus affichable directement car il le nombre de chiffres d'un entier est maintenant capé. Pour le calculer, il faut augmenter le nombre maximum de chiffre d'un entier de l'interpréteur.
 

Augmenter le nombre de chiffres maximum d'un entier :

```python
import sys
sys.set_int_max_str_digits(15000)
```

{% enddetails %}

Toutes les réponses tiennent en 1 seule ligne de python. À vous de les trouver !

Dans la vraie vie on préférera toujours du code explicite et facile à lire plutôt que du code compact, mais cela reste un très bon exercice pour comprendre comment fonctionne un langage informatique en général et python en particulier.

## Sujet

{% info %}
On en a déjà vu quelques-une pendant ce cours, à vous de les retrouver.
{% endinfo %}
{% details "Indices" %}

Les fonctions suivantes vous seront utiles :

- [`divmod`{.language-}](https://docs.python.org/fr/3.14/library/functions.html#divmod)
- [`input`{.language-}](https://docs.python.org/fr/3.14/library/functions.html#input)
- [`chr`{.language-}](https://docs.python.org/fr/3.14/library/functions.html#chr) et [`ord`{.language-}](https://docs.python.org/fr/3.14/library/functions.html#ord)
- [`sum`{.language-}](https://docs.python.org/fr/3.14/library/functions.html#sum)

Les méthodes des :

- [listes](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [chaînes de caractères](https://docs.python.org/fr/3.14/library/string.html#module-string)

{% enddetails %}

1. Évaluer le nombre d’atomes de l’univers : 1080
2. Aﬀecter le 23e [nombre premier de Mersenne](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier) ($2^{11213}-1$) à une variable `m23`{.language-}.
3. Incrémenter `m23`{.language-}.
4. Décrémenter `m23`{.language-} (on retrouve le 23e nombre de Mersenne)
5. Évaluer 1000/7.
6. Évaluer ⌊1000/7⌋.
7. Évaluer 1000 mod 7.
8. Évaluer en une seule expression le quotient entier et le reste de 1000/7.
9. Aﬀecter en une seule instruction le quotient entier et le reste de 1000/7 à deux variables `q`{.language-} et `r`{.language-}.
10. Aﬀecter à une variable `c`{.language-} le couple formé de `q`{.language-} et `r`{.language-}.
11. Faire les deux exercices précédents en une seule instruction.
12.  Échanger le contenu des deux variables `q`{.language-} et `r`{.language-}.
13. Demander à l’utilisateur son âge et aﬀecter le résultat à une variable `a`{.language-}.
14. Demander à l’utilisateur la diﬀérence entre son année de naissance et celle de son voisin, et aﬀecter la valeur absolue à une variable `d`{.language-}.
15. Évaluer le nombre de chiﬀres de `m23`{.language-}.
16. Quel est le millième chiﬀre de `m23`{.language-} ?
17. Quels sont les dix premiers chiﬀres de `m23`{.language-} ?
18. Quel est le dernier chiﬀre de `m23`{.language-} (sans utiliser son nombre de chiﬀres) ?
19. Quel est le dernier chiﬀre de `m23`{.language-} (utiliser explicitement son nombre de chiﬀres) ?
20. Quels sont les dix derniers chiﬀres de `m23`{.language-} ?
21. La séquence 123 apparaît-elle dans `m23`{.language-} ?
22. À quelle position apparaît 1234 dans `m23`{.language-} ?
23. Combien `m23`{.language-} contient-il de 7 ?
24. Remplacer tous les 2 par des 7 dans `m23`{.language-} (expression).
25. Permuter tous les 2 et les 7 dans `m23`{.language-} (expression).
26. Demander à l’utilisateur son prénom et aﬀecter celui-ci à une variable p.
27. Demander à l’utilisateur son nom complet (prénom puis nom) et aﬀecter celui-ci à une variable nc.
28. Demander à l’utilisateur son nom complet et aﬀecter ses prénom et nom à deux variables `p`{.language-} et `n`{.language-} (on suppose que l’utilisateur à un nom sans espaces).
29. Demander à l’utilisateur son nom complet et aﬀecter ses prénom et nom à deux variables `p`{.language-} et `n`{.language-} (l’utilisateur peut être noble ou plus généralement avoir un nom à plusieurs mots).
30. L’utilisateur a-t-il bien mis une majuscule à ses prénom et nom ?
31. Aﬃcher les prénom (initiale en majuscule) et nom (tout en majuscules).
32. Aﬀecter le résultat à une variable nc.
33. Aﬃcher « Bonsoir, _Prénom NOM_ !, comment allez-vous ? » en substituant nc à la partie en italiques.
34. Aﬃcher « Bonsoir, _Prénom_ _NOM_ !, comment allez-vous ? » en substituant p et n aux parties en italiques.
35. Quel est le caractère de code Unicode 126 ?
36. Quel intervalle existe-t-il dans la table Unicode entre une majuscule et la minuscule correspondante d'une lettre de l'alphabet ?
37. Reproduire les trois lignes ci-dessous (tabulations pour séparer les colonnes) :
  ```text
  20  a
  100 b
  32  \
  ```
38.  Calculer 14 répétitions de `"Developers ! "`{.language-}.
39.  Calculer 14 répétitions de `"Developers ! "`{.language-} en supprimant l’espace final.
40. Utiliser la fonction help pour aﬃcher la documentation de la fonction `range`{.language-}.

Solution.
Exercice 43. Calculer la liste [0,1,2,...,99].
Solution.
Exercice 44. Calculer la liste [1,2,3,...,100].
Solution.
Exercice 45. Calculer la liste [1,3,5,...,99].
Solution.
Exercice 46. Calculer la liste [100,99,98,...,1].
Solution.
Exercice 47. Calculer 100
n=1 n.
Solution.
Exercice 48. Aﬀecter à une variable l la liste [-5, -3, -1, 1, 3, 1, 5, 9, 13, 17, 9,
6, 3, Solution.
0] (obtenue par concaténation de trois ranges à déterminer).
3
Exercice 49. Calculer 20 répétitions de l.
Solution.
Exercice 50. Évaluer le minimum, le maximum et la moyenne des éléments de l.
Solution.
Exercice 51. Aﬀecter à une variable lm une copie de l.
Solution.
Exercice 52. Supprimer le dernier élément de lm.
Solution.
Exercice 53. Calculer le nombre de 1 de lm.
Solution.
Exercice 54. Calculer l’indice du plus grand élément de lm.
Solution.
Exercice 55. Supprimer le premier 1 de lm.
Solution.
Exercice 56. Insérer la liste ["a","b","c"] après le 3e élément de lm.
Solution.
Exercice 57. Supprimer cette insertion.
Solution.
Exercice 58. Trier lm.
Solution.
Exercice 59. Inverser lm.
Solution.
Exercice 60. Ajouter la chaîne "fin" au bout de lm.
Solution.
Exercice 61. Aﬀecter à une variable e l’ensemble des éléments de l.
Solution.
Exercice 62. Calculer la diﬀérence de e d’avec l’ensemble {−5, 0, ..., 20}.
Solution.
Exercice 63. Retirer 13 de e.
Solution.
Exercice 64. Retirer 20 de e.
Solution.
Exercice 65. Ajouter "treize" à e.
Solution.
Exercice 67. Supraoesophagal est-il un mot anglais ?
Solution.
4
Exercice 72. Aﬀecter à une variable rep le répertoire téléphonique suivant :
– Le numéro de Jean est 03 87 65 45 67 ;
– le numéro de Pierre est 03 87 31 55 21 ;
– le numéro de Michel est 03 87 12 23 52.
Solution.
Exercice 73. Quel est le numéro de Jean ?
Solution.
Exercice 74. Modifier le numéro de Michel en 03 84 35 21 00.
Solution.
Exercice 75. Ajouter au répertoire Paul, de numéro 03 87 24 56 79.
Solution.
Exercice 76. Albert est-il répertorié ?
Solution.
Exercice 77. Aﬃcher les noms des personnes répertoriées.
Solution.
Exercice 78. Aﬃcher les numéros des personnes répertoriées.
Solution.
Exercice 79. Aﬀecter à une liste lc les couples (nom, numéro) des personnes répertoriées.
Solution.
Exercice 80. Trier lc par ordre alphabétique décroissant des noms.
Solution.
Exercice 81. Supprimer Paul du répertoire.
Solution.
Exercice 82. Supprimer un élément arbitraire du répertoire tout en renvoyant sa valeur.
Solution.
Exercice 83. Calculer la liste des inverses des entiers naturels positifs inférieurs à 10.
Solution.
Exercice 84. Même question pour une borne supérieure saisie par l’utilisateur.
Solution.
Exercice 85. Aﬃcher la liste des grains de blé à placer sur l’échiquier de Sessa.
Solution.
5
Exercice 86. Évaluer le nombre total de grains de blé à placer.
Solution.
Exercice 87. Concaténer dans l’ordre tous les caractères de codes ASCII entre 32 et 126.
Solution.
Exercice 88. Calculer dans Z10 la somme des chiﬀres de m27.
Solution.
Exercice 89. Aﬀecter à une variable lengths la liste des longueurs des mots de words.
Solution.
Exercice 90. Aﬀecter à une variable maxLength la longueur du plus grand mot.
Solution.
Exercice 91. Calculer une liste ln de couples répertoriant, pour chaque longueur de mot, le
nombre de mots de cette longueur.
Solution.
Exercice 92. Même exercice avec un dictionnaire.
Solution.
Exercice 93. Aﬀecter à une liste nl une copie de ln avec les couples permutés.
Solution.
Exercice 94. Quelle est longueur la plus représentée ?
Solution.
Exercice 95. Calculer la liste des diviseurs de 170170.
Solution.
Exercice 96. Calculer la liste [[], [0], [0,1], [0,1,2], ..., [0,1,2,...,99]].
Solution.
Exercice 97. Calculer la liste [[1], [1,2], [1,2,3], ..., [1,2,3,...,100]].
Solution.
Exercice 98. Calculer la liste [1, 3, 6, 10, 15, 21, ..., 5050] (s’aider de l’exercice 47).
Solution.
Exercice 99. Calculer la liste (i j : (i, j) ∈[1...10] ×[1...10]).
Solution.
Exercice 100. Calculer une liste de listes contenant les tables de Pythagore de 1 à 10.

## Corrigé

{% details "corrigé" %}

```python/

```

{% enddetails %}


