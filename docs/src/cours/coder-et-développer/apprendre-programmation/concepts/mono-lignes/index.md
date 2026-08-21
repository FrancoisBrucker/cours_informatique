---
layout: layout/post.njk

title: "42 * 2 Mono-lignes en python"
authors:
  - "Aristide Grange"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Les mono-lignes sont des petits exercices que l'on doit à Aristide Grange. Ils permettent de se creuser un peu la tête pour écrire de façon condensé du code python. J'ai modifié le sujet initial pour qu'il puisse être fait avec une version actuelle de python (il a été fait en 2005 pour une version 2 de python) et ai supprimé quelques questions, en particulier les questions relatives aux fichiers que l'on a pas encore vu.

{% details "Sujet initial et modifications à apporter si vous voulez le faire une version actuelle de python" %}
[Le sujet initial](monolignes-questions.pdf){.interne}

Ce sujet initial montre aussi en creux les évolutions de python : 

- la fonction `print`{.language-} prend des parenthèses,
- les f-string sont apparues,
- `chr`{.language-} et `ord`{.language-} sont des code unicode maintenant
- la fonction `raw_input`{.language-} a disparu,
- `input`{.language-} n'évalue plus automatiquement les entrées, 
- `range`{.language-} ne rend plus une liste mais un itérateur,
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
40. Utiliser la fonction `help`{.language-} pour aﬃcher la documentation de la fonction `range`{.language-}.
41. Calculer la liste $[0, 1, 2,\dots ,99]$.
42. Calculer la liste $[1,2,3,\dots, 100]$.
43. Calculer la liste $[1,3,5,\dots,99]$.
44. Calculer la liste [100,99,98,...,1].
45. Calculer $\sum_{i=1}^{100}i$.
46. Aﬀecter à une variable `l`{.language-} la liste $[-5, -3, -1, 1, 3, 1, 5, 9, 13, 17, 9, 6, 3, 0]$ que vous obtiendrez par concaténation de trois listes issues de `range`{.language-} à déterminer.
47. Calculer 20 répétitions de `l`{.language-}.
48. Évaluer le minimum, le maximum et la moyenne des éléments de `l`{.language-}.
49. Aﬀecter à une variable `lm`{.language-} une copie de `l`{.language-}.
50. Supprimer le dernier élément de `lm`{.language-}.
51. Calculer le nombre de 1 de `lm`{.language-}.
52. Calculer l’indice du plus grand élément de `lm`{.language-}.
53. Supprimer le premier 1 de `lm`{.language-}.
54. Insérer la liste `["a","b","c"]`{.language-} après le 3e élément de `lm`{.language-}.
55. Supprimer cette insertion.
56. Trier `lm`{.language-}.
57. Inverser `lm`{.language-}.
58. Ajouter la chaîne "fin" au bout de lm.
59. Aﬀecter à une variable `e`{.language-} l’ensemble des éléments de `l`{.language-}.
60. Calculer la diﬀérence de `e`{.language-} d’avec l’ensemble $\\{−5, 0, 5, \dots, 20\\}$.\
61. Retirer 13 de e.
62. Ajouter "treize" à e.
63. Aﬀecter à une variable `rep`{.language-} le répertoire téléphonique suivant :
  – Le numéro de Jean est 03 87 65 45 67 ;
  – le numéro de Pierre est 03 87 31 55 21 ;
  – le numéro de Michel est 03 87 12 23 52.
64. Quel est le numéro de Jean ?
65. Modifier le numéro de Michel en 03 84 35 21 00.
66. Ajouter au répertoire Paul, de numéro 03 87 24 56 79.
67. Albert est-il répertorié ?
68. Aﬃcher les noms des personnes répertoriées.
69. Aﬃcher les numéros des personnes répertoriées.
70. Aﬀecter à une liste `lc`{.language-} les couples (nom, numéro) des personnes répertoriées.
71. Trier `lc`{.language-} par ordre alphabétique décroissant des noms.
72. Supprimer Paul du répertoire.
73. Supprimer un élément arbitraire du répertoire tout en renvoyant sa valeur.
74. Calculer la liste des inverses des entiers naturels positifs inférieurs à 10.
75. Même question pour une borne supérieure saisie par l’utilisateur.
76. Aﬃcher la liste des grains de blé à placer sur [l’échiquier de Sissa](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_l%27%C3%A9chiquier_de_Sissa).
77. Évaluer le nombre total de grains de blé à placer.
78. Concaténer dans l’ordre tous les caractères de codes Unicode entre 32 et 126.
79. Calculer la liste des diviseurs de $170170$.
80. $[[], [0], [0,1], [0,1,2], \dots, [0,1,2,...,99]]$.
81. Calculer la liste $[[1], [1,2], [1,2,3], \dots, [1,2,3,...,100]]$.
82. Calculer la liste $[\sum_{i=1}^{1}i, \sum_{i=1}^{2}i, \sum_{i=1}^{3}i, \dots, \sum_{i=1}^{100}i]$ (s’aider de l’exercice 45).
83. Calculer l'ensemble $\\{ i * j \vert 1 \leq i, j\leq 10 \\}$.
84. Calculer une liste de listes contenant [les tables de Pythagore](https://fr.wikipedia.org/wiki/Table_de_multiplication#Table_usuelle) de 1 à 10.

## Corrigé

{% details "corrigé" %}

```python/
print(pow(10, 80))
m23 = pow(2, 11213) - 1
m23 += 1
m23 -= 1
print(1000 / 7)
print(1000 // 7)
print(1000 % 7)
print(divmod(1000, 7))
q, r = divmod(1000, 7)
c = (q, r)
c = (q, r) = divmod(1000, 7)
q, r = r, q
a = int(input("Votre age ? :"))
d = abs(int(input("Différence de vos années de naissance ? :")))
print(len(str(m23)))
print(str(m23)[999])
print(str(m23)[:10])
print(str(m23)[-1])
print(str(m23)[len(str(m23))-1])
print(str(m23)[-10:])
print("123" in str(m23))
print(str(m23).index("1234"))
print(str(m23).count("7"))
print(str(m23).replace("2", "7"))
print(str(m23).replace("2", "x").replace("7", "2").replace("x", "7"))
p = input("Votre prénom ? :")
nc = input("Votre nom complet ? :")
p, n = input("Votre nom complet ? :").split()
p, n = input("Votre nom complet ? :").split(' ', 1)
print(p[0].isupper() and n[0].isupper())
print(p.title(), n.upper())
nc = p.title() + " " + n.upper()
print(f"Bonsoir, {nc} !, comment allez-vous ?")
print(f"Bonsoir, {p} {n} !, comment allez-vous ?")
print(chr(126))
print(ord('a') - ord('A'))
print("20\ta\n100\tb\n32\t\\")
print("Developers ! " * 14)
print(("Developers ! " * 14)[:-1])
help(range)
print(list(range(100)))
print(list(range(1, 101)))
print(list(range(1, 100, 2)))
print(list(range(100, 0, -1)))
print(sum(range(1, 101)))
l = list(range(-5, 5, 2)) + list(range(1, 20, 4)) + list(range(9, -1, -3))
print(l * 20)
print(min(l), max(l), sum(l)/len(l))
lm = l[:]
del lm[-1]
print(lm.count(1))
print(lm.index(max(lm)))
lm.remove(1)
lm[3:3] = ["a","b","c"]
del lm[3:6]
lm.sort()
lm.reverse()
lm.append("fin")
e = set(l)
print(e- set(range(-5, 21, 5)))
e.remove(13)
e.add("treize")
rep = {"Jean": "03 87 65 45 67", "Pierre": "03 87 31 55 21", "Michel": "03 87 12 23 52"}
print(rep["Jean"])
rep["Michel"] = "03 84 35 21 00"
rep["Paul"] = "03 87 24 56 79"
print("Albert" in rep)
print(list(rep.keys()))
print(list(rep.values()))
lc = list(rep.items())
lc.sort(reverse=True)
del rep["Paul"]
print(rep.popitem())
print([1/n for n in range(1, 11)])
print([1/n for n in range(1, int(input("borne sup :")))])
print([2 ** i for i in range(64)])
print(sum([2 ** i for i in range(64)]))
print("".join([chr(x) for x in range(32, 127)]))
print([x for x in range(1, 170171) if 170170 % x == 0])
print([list(range(i)) for i in range(101)])
print([list(range(1, i)) for i in range(2, 102)])
print([sum(range(1, i)) for i in range(2, 102)])
print({i * j for i in range(1, 11) for j in range(1, 11)})
print([[i * j for i in range(1, 11)] for j in range(1, 11)])
```

{% enddetails %}


