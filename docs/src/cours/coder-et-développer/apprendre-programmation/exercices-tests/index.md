---
layout: layout/post.njk

title: "Exercices"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Quelques exercices de code à résoudre. On vous demande de créer :

- un fichier `main.py`{.fichier} pour votre programme principal
- un fichier `fonction.py`{.fichier} pour vos fonctions
- un fichier `test_fonction.py`{.fichier} pour vos tests

Ces trois fichiers sont obligatoires.

## Google code jam

{% lien %}
<https://fr.wikipedia.org/wiki/Google_Code_Jam>
{% endlien %}

Un concours de code organisé par google de 2003 à 2023. Certains exercices étaient très chouette d'un point de vue algorithmique.

On en propose certains, avec des fichiers de tests associés. Il pourra être intéressant pour chaque problème, en plus de le résoudre, de faire un algorithme qui construit un jeu de donné.

### Reverse Words

> Given a list of space separated words, reverse the order of the words. Each input string contains L letters and W words. An input string will only consist of letters and space characters. There will be exactly one space character between each pair of consecutive words. For instance, the reverse of “this is a test” is “test a is this”, the reverse of “foobar” is “foobar”, and the reverse of “all your base” is “base your all”.

{% lien %}
Contient des jeux de données (`.in`{.fichier}) et leurs solutions (`.out`{.fichier}) : [jeux de données](https://github.com/lovebeckdy/google-code-jam/tree/master/reverse_words)

La première ligne du fichier donne le nombre d'exemples à traiter puis chaque ligne correspond à une phrase à retourner.
{% endlien %}

### Store crédit

> You receive a credit C at a local store and would like to buy two items. You first walk through the store and create a list L of all available items. From this list you would like to buy two items that add up to the entire value of the credit. The solution you provide will consist of the two integers indicating the positions of the items in your list (smaller number first). For instance, with C=100 and L={5,75,25} the solution is 2,3; with C=200 and L={150,24,79,50,88,345,3} the solution is 1,4; and with C=8 and L={2,1,9,4,4,56,90,3} the solution is 4,5.

{% lien %}
Contient des jeux de données (`.in`{.fichier}) : [jeux de données](https://github.com/lovebeckdy/google-code-jam/tree/master/store_credit)

La première ligne du fichier donne le nombre d'exemples à traiter puis chaque exemple est sur 3 lignes :

- ligne 1 : le crédit
- ligne 2 : le nombre de produits
- ligne 3 : la liste des prix de chaque produit séparé par un espace

{% endlien %}

### T9 Spelling

> The Latin alphabet contains 26 characters and telephones only have ten digits on the keypad. We would like to make it easier to write a message to your friend using a sequence of keypresses to indicate the desired characters. The letters are mapped onto the digits as 2=ABC, 3=DEF, 4=GHI, 5=JKL, 6=MNO, 7=PQRS, 8=TUV, 9=WXYZ. To insert the character B for instance, the program would press 22. In order to insert two characters in sequence from the same key, the user must pause before pressing the key a second time. The space character should be printed to indicate a pause. For example “2 2” indicates AA whereas “22” indicates B. Each message will consist of only lowercase characters a-z and space characters. Pressing zero emits a space. For instance, the message “hi” is encoded as “44 444”, “yes” is encoded as “999337777”, “foo  bar” (note two spaces) is encoded as “333666 6660022 2777”, and “hello world” is encoded as “4433555 555666096667775553”.

{% lien %}
Contient des jeux de données (`.in`{.fichier}) : [jeux de données](https://github.com/lovebeckdy/google-code-jam/tree/master/t9_spelling)

La première ligne du fichier donne le nombre d'exemples à traiter puis chaque ligne correspond à une phrase à encoder.
{% endlien %}

### Archives

Plein d'autres exercices :

{% lien %}
[Archives du Google code jam](https://zibada.guru/gcj/)
{% endlien %}

## Advent of code

{% lien %}
<https://fr.wikipedia.org/wiki/Advent_of_Code>
{% endlien %}

Le site <https://adventofcode.com/> est chaque année un calendrier de l'avent de code . Ce concours est très [populaire](https://jeroenheijmans.github.io/advent-of-code-surveys/)
 et les exercices sont résolus avec de nombreux langages différents. Vous pouvez vous connecter pour avoir des données personnalisées à résoudre.

Trois exemples, triés par difficulté :

1. [Advent of code 2017](https://adventofcode.com/2017) et [un jeu de donnée (et sa résolution en lisp)](https://github.com/gabrielelana/advent-of-code-2017)
2. [Advent of code 2023](https://adventofcode.com/2023) et [un jeu de donnée](https://github.com/dcastil/advent-of-code-2023/tree/main/data/examples)
3. [Advent of code 2019](https://adventofcode.com/2017) et [un jeu de donnée (et sa résolution en python)](https://github.com/jeroenheijmans/advent-of-code-2019)

{% attention %}
Parfois ça peut un peu piquer niveau difficulté.
{% endattention %}

<!-- ### Au delà de ce qui est demandé

- [un peu de crypto](support_eleves_cours_6.pdf)
- remplir [une grille aléatoire de sudoku](https://www.youtube.com/watch?v=2SuvO4Gi7uY) en utilisant [la réduction de paquet d'onde](https://fr.wikipedia.org/wiki/R%C3%A9duction_du_paquet_d'onde) (si si. Voir [ici](https://robertheaton.com/2018/12/17/wavefunction-collapse-algorithm/) pour une explication et un autre exemple). Attention, parfois cette méthode va rater et il faudra faire du [backtracking](https://fr.wikipedia.org/wiki/Retour_sur_trace) (ne l'implémentez pas ici, cela va au delà de cette semaine) -->
