---
layout: page
title:  "Structure : chaine de caractères"
category: cours
---

Qu'est-ce qu'une chaine de caractères et comment on peut l'utiliser.

<!--more-->

> [Algorithme, code et théorie]({% link cours/algorithme-code-théorie/index.md %}) / [algorithmie]({% link cours/algorithme-code-théorie/algorithme/index.md %}) / [structure : chaine de caractères]({% link cours/algorithme-code-théorie/algorithme/structure-chaine-de-caracteres.md %})
>
> **prérequis :**
>
> * [mémoire et espace de noms]({% link cours/algorithme-code-théorie/code/mémoire-espace-noms.md %})
>
{.chemin}

En informatique tout est nombre. La base étant l'octet (équivalent à un byte, 8bits, 0xFF en hexadécimal, 255 en décimal). Texte et caractères n'a donc pas vraiment de sens intrinsèque en informatique : ce sont des octets et on les fait correspondre à des caractères.

> On a coutume d'écrire les octets de façon hexadécimale, de 00 (0) à FF (255)

## codage des caractères

Le premier codage utilisé était le code [ASCII](http://fr.wikipedia.org/wiki/ASCII) dont chaque symbole était codé sur 7 bits, ce qui permettait de représenter 128 symboles. Plusieurs extensions ont été ensuite proposées par la suite dont le codage [ISO-8859-1](http://fr.wikipedia.org/wiki/ISO_8859-1) où chaque symbole est codé sur un octet (8 bits). Ce codage avait l'avantage de permettre d'écrire en français, les accents y étant présents.

Il y en a eu une foultitude d'autres jusqu'à arriver à l'encodage actuel : [utf-8](https://fr.wikipedia.org/wiki/UTF-8).

A priori lorsque l'on ouvre un fichier texte avec un éditeur rien ne dit quel est l'encodage utilisé : ce n'est qu'une suite d'octets. Par exemple, la chaine de caractère "j'écris en Français" se code :

* `6A27E96372697320656E204672616EE7616973` dans le format [ISO-8859-1](https://fr.wikipedia.org/wiki/ISO/CEI_8859-1) aussi appelé ISO-latin 1, un format populaire pour écrire du Français avant l'utf-8. Remarquez qu'il y a autant d'octets que de lettres.
* `6A278E6372697320656E204672616E8D616973` dans le format [mac-roman](https://fr.wikipedia.org/wiki/MacRoman). Remarquez comment le `é` et le `ç` ne se codent pas de la même manière... Vous imaginez l'enfer pour se passer des fichier entre possesseurs de mac et de pc ?
* `6A27C3A96372697320656E204672616EC3A7616973` dans le format [utf-8](https://fr.wikipedia.org/wiki/UTF-8). Remarquez qu'il y a plus d'octets que de lettres.
* `FEFF006A002700E9006300720069007300200065006E0020004600720061006E00E7006100690073` dans le format [utf-16 big endian](https://fr.wikipedia.org/wiki/UTF-16)

Il n'y a aucun moyen a priori de savoir en quel format le texte est codé. Pour éviter des problèmes :

> Codez tous vos textes en utf-8, ce qui devrait être le comportement par défaut de votre éditeur de texte.
{.note}

## unicode

Les formats d'encodage anciens, comme le codage ASCII ou le ISO-8859-1 permettent d'écrire en anglais, voire en Français. Mais... Pas dans beaucoup de langues parlés par plus de locuteurs comme le Chinois ou encore le Russe. Ils avaient eux aussi leur propre format d'encodage.

Pour rationaliser cela, le format [unicode](https://fr.wikipedia.org/wiki/Unicode) a été créé. Son but est d'associer un nombre à chaque caractère de toute les langues humaines possibles (donc pas de [Tengwar](https://fr.wikipedia.org/wiki/Tengwar), de [klingon](https://fr.wikipedia.org/wiki/Klingon_(langue)) ou encore de [Khuzdul](https://fr.wikipedia.org/wiki/Khuzdul) dans unicode)

Ce n'est pas un format fixe, il évolue sans cesse en ajoutant de nouveaux caractères. Il y a actuellement (en 2022) prés de 150000 caractères possible. A chaque caractère est associé un numéro entre 0 et FFFFFF (16777215).

> On a coutume de faire précéder ce nombre par `U+` pour préciser que c'est un code unicode écrit en hexadécimal.
>
> Ainsi `U+1823` correspond à la lettre mongole o : ᠣ
{.note}

Allez voir <https://unicode-table.com/fr/#> et scrollez vers le bas pour voir tous les symboles unicode possibles (bizarrement ça ne marche pas le navigateur chrome).

Les caractères sont organisées [en blocs](https://unicode-table.com/fr/blocks/), par exemple :

* de [0 à 7F](https://unicode-table.com/fr/blocks/basic-latin/) : Latin de base
* de [80 à FF](https://unicode-table.com/fr/blocks/latin-1-supplement/) : supplément latin-1 : les accents
* ...
* de [4DC0 à 4DFF](https://unicode-table.com/fr/blocks/yijing-hexagram-symbols/) : le [Yi-king](https://fr.wikipedia.org/wiki/Yi_Jing) pour faire ses propres prédictions
* ...

> Unicode permet d'unifier tous les encodages de caractères en associant à tout caractère d'une langue humaine un numéro.
{.note}

Cependant unicode n'est **pas** un système d'encodage de caractère, c'est juste une table de correspondance. Cette table est cependant utilisé dans les système d'encodage de caractères, comme l'utf-8.

## utf-8 {#utf8}

On ne peut pas vraiment utiliser unicode directement pour encoder les caractères, sinon chaque caractère devrait être encodé par 3 octets, alors que seul un très petit nombre de caractères seraient utilisé. En particulier si on écrit du code ou en anglais.

On utilise donc une transformation de ces codes pour diminuer la taille de l'encodage. On appelle ce format *utf* (unicode transformation format) et il  permet de coder chaque symbole sur 1 à 4 octets. C'est un octet de plus que tout nombre unicode au maximum, mais le plus souvent -- si on écrit en anglais -- tout est stocké sur 1 octet par caractère, comme l'ascii.

Il existe plusieurs format utf, mais c'est [utf-8](https://fr.wikipedia.org/wiki/UTF-8) qui s'est imposé.

### organisation du code

Comment encoder des caractères sur un nombre variables d'octets ? Il faut pour cela résoudre deux problèmes épineux :

* connaitre le nombre d'octets nécessaires pour décoder un caractère
* savoir si on est au début d'un caractère ou au milieu de son encodage

Utf-8 résout ce problème de façon élégante (voir [la description de l'encodage](https://fr.wikipedia.org/wiki/UTF-8#Description)) :

* tout octet qui n'est pas un début d'encodage commencent par `10`
* le nombre d'octets utilisés est encodé au début :
  * `0` pour 1 octet
  * `110` pour 2 octets
  * `1110` pour 3 octets
  * `11110` pour 4 octets

Les autre bits des octets de codes raboutés entre eux donne le code unicode du caractère utilisé.

### exemple du `é` en python

Le symbole `é` est par exemple de code : `U+00E9`.

1. code unicode : `0xE9 = 233`. On l'obtient en python avec la commande `ord('é')`
2. son code utf-8 est sur 2 octets. On l'obtient en convertissant la chaine de caractère en utf-8 : `'é'.encode('utf8')`. Ce résultat donne : `b'\xc3\xa9'`. Le `b` avant la chaine en python indique que ce n'est pas une chaine de caractère, mais une successions d'octets (byte), valant C3 et A9 (`\x` signifie que ce qui suit est un nombre hexadécimal).
3. les deux octets `0xC3` et `0xA9` (en python les nombres hexadécimaux sont écrit en commançant par `0x`. Ecrire un nombre en hexadécimale se fait par la fonction [`hex`](https://docs.python.org/3/library/functions.html#hex)). correspondent à l'écriture binaire : `bin(0xC3)`qui rend '0b11000011' et `bin(0xA9)` qui rend '0b10101001'. Le nombre est ainsi codé en utf-8 avec les deux octets : `11000011 10101001`.
4. en regardant le code utf-8 sur 2 octets <https://fr.wikipedia.org/wiki/UTF-8#Description>, on voit que le code unicode est la concaténation des 5 derniers bits du premier octet (qui commence par `110`) et des 6 dernier bits du deuxième (qui commence par `10`). On obtient ainsi `00011101001` qui est : `int('00011101001', 2)` et vaut : 233. Ouf, la boucle est bouclée on retrouve bien le code unicode de `é`.

>
> * On peut écrire des nombres en python en base 10, de façon normale, `42` par exemple. On peut écrire des nombres en base 2 directement en commençant le nombre par `0b`, comme `0b101010` par exemple. On encore en base 16, en les faisant commencer par `0x`, comme `0x2A`.
> * convertir un nombre en binaire ou en hex via les fonctions `bin` et `hex` rendent des chaînes de caractères. En effet, un nombre est un nombre; sa représentation dans une autre base est une chaine de caractères. Ainsi `bin(42)` donne `'0b101010'` et `hex(42)` donne `'0x2a'`.
> * notez bien la différence entre écrire un nombre en base 10, 2, et 16 et voir sa forme dans une base particulière (2 ou 16)

## python et chaines de caractères

Une chaine de caractères `s` est de type `str`. Elle peuvent être considérées comme des tableaux de `len(s)` cases. Ces objets son **non modifiables**.

En python, la concaténation est symbolisée par l'opérateur `+`.

On peut faire de nombreuses choses avec des chaines de caractères en python :

* <https://miamondo.org/le-langage-python/chapitre-7-apercu-de-quelques-methodes-associees-aux-objets-de-type-chaine-de-caracteres-str/>
* N'hésitez pas à aller voir la documentation si vous voulez faire une opérations sur les chaines, souvent elle est déjà implémentée : <https://docs.python.org/3/library/stdtypes.html#textseq>

### texte vers types

Toute chose tapée au clavier par un utilisateur sera considéré comme du texte :

```python
x = input('entrez un nombre :')
```

Dans le bout de code ci-dessus, `x` est une chaine de caractères. Pour la convertir en entier, on fera : `int(x)` qui rendra la conversion de `x` en entier.

> **Toujours** convertir les données entrées par un utilisateur ou lues d'un fichier dans le type voulu.
{.note}

### byte et str

Par défaut toutes les chaînes de caractères sont de type `str`, et encodées en `utf-8`. Si on veut connaitre explicitement les octets d'une chaine, il faut l'encoder en un autre format par la méthode `encode`  des chaines de caractères qui rend un objet de type byte qui est une suite d'octets.

C'est comme une chaine de caractères mais qui commence par `b` . On peut ensuite décoder un byte pour le retransformer en `str` :

```python
x = "ma chaîne de caractères"
x_en_byte = x.encode('utf8')  # devient : b'ma cha\xc3\xaene de caract\xc3\xa8res'
re_x = x_en_byte.decode('utf8')
```

Ceci va s'avérer utile lorsque l'on récupérera des fichiers depuis internet. Ce seront des `byte` qu'il faudra re-écrire en `utf8`.

Les différents encoding possibles sont disponibles [dans la documentaion](https://docs.python.org/3/library/codecs.html#standard-encodings).

### exercices

On utilisera [les nombres de Mersenne](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier) comme prétexte à la manipulation de chaines de caractères en python. Ces exercices sont pour une grande partie tirés d'un cours donné il y a quelques temps par Aristide Grange, à l'université Paul Verlaine de Metz).

> Notez `m27` le 27ième nombre de Mersenne $2^{44497} -1$ :
{.a-faire}
{% details solution %}

```python
m27 = 2 ** 444497 - 1
```

{% enddetails %}

> Combien de chiffres en base 10, 2 et 16 possède ce nombre ?
{.a-faire}
{% details solution %}

* en base 10 : `len(str(m27))` : conversion de l'entier en chaine de caractères puis son nombre de chiffres
* en base 2 : `len(bin(m27)) - 2` : `bin` transforme un entier en sa représentation binaire. C'est une chaine de caractères qui commence par `0b` donc on retranche 2 à la longueur.
* en base 16 : `len(hex(m27)) - 2` : `hex` transforme un entier en sa représentation héxadécimale. C'est une chaine de caractères qui commence par `0x` donc on retranche 2 à la longueur.

{% enddetails %}

#### méthodes de chaines de caractères

Utilisez la documentation sur les [méthodes de chaines](https://docs.python.org/3/library/stdtypes.html#string-methods) en python pour résoudre les exercices suivants

> Index de la première occurence de `1234` dans m27. Et de la deuxième ?
{.a-faire}
{% details solution %}

* `str(m27).find('1234')`
* `str(m27).find('1234', 19260 + 1)` : la première occurence est à l'indice 19260, on cherche donc après.
* on peut faire en une ligne : `str(m27).find('1234', str(m27).find('1234') + 1)`

{% enddetails %}

> Nombre de 2 dans m27, nombre de 7
{.a-faire}
{% details solution %}

* `str(m27).count('2')`
* `str(m27).count('7')`

{% enddetails %}

> Remplacer des 2 par des 7 dans m27.
{.a-faire}
{% details solution %}

`str(m27).replace('2', '7')`

{% enddetails %}

> Echanger les 2 et les 7 dans m27
{.a-faire}
{% details solution %}

`str(m27).replace('2', 'X').replace('7', '2').replace('X', '7')`

{% enddetails %}

#### slice

L'extraction de sous-chaines en python se fait par une opération appelé [slice](https://zestedesavoir.com/tutoriels/582/les-slices-en-python/). Cela peut se résumer en une seule grosse opération :

> Si `s` est une chaine de caractères, la chaîne de caractères `s[a:b:c]` est la sous chaine de `s` allant de l'indice `a` à l'indice `b-1` avec un pas de `c`.
>
> Par défaut `a=0`, `b=-1` et `c=1`
{.note}

Ainsi `"abcdefghijklmnopqrstuvwxyz"[2:15:4]` vaut : `'cgko'`.

> Quels sont les 10 premiers chiffres de m27 ?
{.a-faire}
{% details solution %}

`str(m27)[:10]`

{% enddetails %}

> Quels sont les 10 derniers chiffres de m27 ?
{.a-faire}
{% details solution %}

`str(m27)[-10:]`

{% enddetails %}

> Est-ce que m27 est un [palindrome](https://fr.wikipedia.org/wiki/Palindrome) ?
{.a-faire}
{% details solution %}

`str(m27) == str(m27)[::-1]` (`s[::-1]` renverse la chaine)

{% enddetails %}
