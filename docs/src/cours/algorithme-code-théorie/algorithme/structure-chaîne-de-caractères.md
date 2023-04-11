---
layout: layout/post.njk 
title: "Structure : chaîne de caractères"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title }}"
    parent: "{{ '../' | siteUrl(page.url) }}"

prerequis:
    - "../../code/mémoire-espace-noms/"
---

<!-- début résumé -->

Qu'est-ce qu'une chaîne de caractères et comment on peut l'utiliser.

<!-- end résumé -->

En informatique tout est nombre. La base étant l'octet (équivalent à un byte, 8bits, 0xFF en hexadécimal, 255 en décimal). Texte et caractères n'a donc pas vraiment de sens intrinsèque en informatique : ce sont des octets et on les fait correspondre à des caractères.

{% info %}
On a coutume d'écrire les octets de façon hexadécimale, de 00 (0) à FF (255)
{% endinfo %}

## Codage des caractères

Le premier codage utilisé était le code [ASCII](http://fr.wikipedia.org/wiki/ASCII) dont chaque symbole était codé sur 7 bits, ce qui permettait de représenter 128 symboles. Plusieurs extensions ont été ensuite proposées par la suite dont le codage [ISO-8859-1](http://fr.wikipedia.org/wiki/ISO_8859-1) où chaque symbole est codé sur un octet (8 bits). Ce codage avait l'avantage de permettre d'écrire en français, les accents y étant présents.

Il y en a eu une foultitude d'autres jusqu'à arriver à l'encodage actuel : [utf-8](https://fr.wikipedia.org/wiki/UTF-8).

A priori lorsque l'on ouvre un fichier texte avec un éditeur rien ne dit quel est l'encodage utilisé : ce n'est qu'une suite d'octets. Par exemple, la chaîne de caractère "j'écris en Français" se code :

* `6A27E96372697320656E204672616EE7616973` dans le format [ISO-8859-1](https://fr.wikipedia.org/wiki/ISO/CEI_8859-1) aussi appelé ISO-latin 1, un format populaire pour écrire du Français avant l'utf-8. Remarquez qu'il y a autant d'octets que de lettres.
* `6A278E6372697320656E204672616E8D616973` dans le format [mac-roman](https://fr.wikipedia.org/wiki/MacRoman). Remarquez comment le `é` et le `ç` ne se codent pas de la même manière... Vous imaginez l'enfer pour se passer des fichier entre possesseurs de mac et de pc ?
* `6A27C3A96372697320656E204672616EC3A7616973` dans le format [utf-8](https://fr.wikipedia.org/wiki/UTF-8). Remarquez qu'il y a plus d'octets que de lettres.
* `FEFF006A002700E9006300720069007300200065006E0020004600720061006E00E7006100690073` dans le format [utf-16 big endian](https://fr.wikipedia.org/wiki/UTF-16)

Il n'y a aucun moyen a priori de savoir en quel format le texte est codé. Pour éviter des problèmes :

{% note %}
Codez tous vos textes en utf-8, ce qui devrait être le comportement par défaut de votre éditeur de texte.
{% endnote %}

## Unicode

Les formats d'encodage anciens, comme le codage ASCII ou le ISO-8859-1 permettent d'écrire en anglais, voire en Français. Mais... Pas dans beaucoup de langues parlés par plus de locuteurs comme le Chinois ou encore le Russe. Ils avaient eux aussi leur propre format d'encodage.

Pour rationaliser cela, le format [Unicode](https://fr.wikipedia.org/wiki/Unicode) a été créé. Son but est d'associer un nombre à chaque caractère de toute les langues humaines possibles (donc pas de [Tengwar](https://fr.wikipedia.org/wiki/Tengwar), de [Klingon](https://fr.wikipedia.org/wiki/Klingon_(langue)) ou encore de [Khuzdul](https://fr.wikipedia.org/wiki/Khuzdul) dans Unicode)

Ce n'est pas un format fixe, il évolue sans cesse en ajoutant de nouveaux caractères. Il y a actuellement (en 2023) prés de 150000 caractères possible. A chaque caractère est associé un numéro entre 0 et FFFFFF (16777215).

{% note %}
On a coutume de faire précéder ce nombre par `U+` pour préciser que c'est un code Unicode écrit en hexadécimal.

Ainsi `U+1823` correspond à la lettre mongole o : ᠣ
{% endnote %}

Les caractères sont organisées [en blocs](https://www.compart.com/fr/unicode/block), par exemple :

* de [0 à 7F](https://www.compart.com/fr/unicode/block/U+0000) : Latin de base
* de [80 à FF](https://www.compart.com/fr/unicode/block/U+0080) : supplément latin-1 : les accents
* ...
* de [4DC0 à 4DFF](https://www.compart.com/fr/unicode/block/U+4DC0) : le [Yi-king](https://fr.wikipedia.org/wiki/Yi_Jing) pour faire ses propres prédictions
* ...

{% note %}
Unicode permet d'unifier tous les encodages de caractères en associant à tout caractère d'une langue humaine un numéro.
{% endnote %}

Cependant Unicode n'est **pas** un système d'encodage de caractère, c'est juste une table de correspondance. Cette table est cependant utilisé dans les système d'encodage de caractères, comme l'utf-8.

## <span id="utf8"></span>utf-8

On ne peut pas vraiment utiliser Unicode directement pour encoder les caractères, sinon chaque caractère devrait être encodé par 3 octets, alors que seul un très petit nombre de caractères seraient utilisé. En particulier si on écrit du code ou en anglais.

On utilise donc une transformation de ces codes pour diminuer la taille de l'encodage. On appelle ce format *utf* (Unicode transformation format) et il  permet de coder chaque symbole sur 1 à 4 octets. C'est un octet de plus que tout nombre Unicode au maximum, mais le plus souvent -- si on écrit en anglais -- tout est stocké sur 1 octet par caractère, comme l’ASCII.

Il existe plusieurs format utf, mais c'est [utf-8](https://fr.wikipedia.org/wiki/UTF-8) qui s'est imposé.

### Organisation du code

{% lien %}
[Convertisseur utf8 vers hexadécimal](https://onlineutf8tools.com/convert-utf8-to-hexadecimal)
{% endlien %}

Comment encoder des caractères sur un nombre variables d'octets ? Il faut pour cela résoudre deux problèmes épineux :

* connaître le nombre d'octets nécessaires pour décoder un caractère
* savoir si on est au début d'un caractère ou au milieu de son encodage

Utf-8 résout ce problème de façon élégante (voir [la description de l'encodage](https://fr.wikipedia.org/wiki/UTF-8#Description)) :

* tout octet qui n'est pas un début d'encodage commencent par `10`
* le nombre d'octets utilisés est encodé au début :
  * `0` pour 1 octet
  * `110` pour 2 octets
  * `1110` pour 3 octets
  * `11110` pour 4 octets

Les autre bits des octets de codes raboutés entre eux donne le code Unicode du caractère utilisé.

### Exemple du `é` en python

Le symbole `é` est par exemple de code : `U+00E9`.

1. code Unicode : `0xE9 = 233`. On l'obtient en python avec la commande `ord('é')`
2. son code utf-8 est sur 2 octets. On l'obtient en convertissant la chaîne de caractère en utf-8 : `'é'.encode('utf8')`. Ce résultat donne : `b'\xc3\xa9'`. Le `b` avant la chaîne en python indique que ce n'est pas une chaîne de caractère, mais une successions d'octets (byte), valant C3 et A9 (`\x` signifie que ce qui suit est un nombre hexadécimal).
3. les deux octets `0xC3` et `0xA9` (en python les nombres hexadécimaux sont écrit en commençant par `0x`. Écrire un nombre en hexadécimale se fait par la fonction [`hex`](https://docs.python.org/3/library/functions.html#hex)). correspondent à l'écriture binaire : `bin(0xC3)`qui rend '0b11000011' et `bin(0xA9)` qui rend '0b10101001'. Le nombre est ainsi codé en utf-8 avec les deux octets : `11000011 10101001`.
4. en regardant le [code utf-8 sur 2 octets](https://fr.wikipedia.org/wiki/UTF-8#Description), on voit que le code Unicode est la concaténation des 5 derniers bits du premier octet (qui commence par `110`) et des 6 dernier bits du deuxième (qui commence par `10`). On obtient ainsi `00011101001` qui est : `int('00011101001', 2)` et vaut : 233. Ouf, la boucle est bouclée on retrouve bien le code Unicode de `é`.

{% info "**En python**" %}

* On peut écrire des nombres en python en base 10, de façon normale, `42`{.language-} par exemple. On peut écrire des nombres en base 2 directement en commençant le nombre par `0b`{.language-}, comme `0b101010`{.language-} par exemple. On encore en base 16, en les faisant commencer par `0x`, comme `0x2A`{.language-}.
* convertir un nombre en binaire ou en hex via les fonctions `bin`{.language-} et `hex`{.language-} rendent des chaînes de caractères. En effet, un nombre est un nombre; sa représentation dans une autre base est une chaîne de caractères. Ainsi `bin(42)`{.language-} donne `'0b101010'`{.language-} et `hex(42)`{.language-} donne `'0x2a'`{.language-}.
* notez bien la différence entre écrire un nombre en base 10, 2, et 16 et voir sa forme dans une base particulière (2 ou 16)

{% endinfo %}

## Python et chaines de caractères

Une chaîne de caractères `s`{.language-} est de type `str`{.language-}. Elle peuvent être considérées comme des tableaux de `len(s)`{.language-} cases. Ces objets son **non modifiables**.

En python, la concaténation est symbolisée par l'opérateur `+`{language-}.

On peut faire de nombreuses choses avec des chaines de caractères en python, n'hésitez pas à aller voir [la documentation](https://docs.python.org/3/library/stdtypes.html#textseq) si vous voulez faire une opérations sur les chaines, souvent elle est déjà implémentée.

### Texte vers types

Toute chose tapée au clavier par un utilisateur sera considéré comme du texte :

```python
x = input('entrez un nombre :')
```

Dans le bout de code ci-dessus, `x`{.language-} est une chaîne de caractères. Pour la convertir en entier, on fera : `int(x)`{.language-} qui rendra la conversion de `x`{.language-} en entier.

{% note %}
**Toujours** convertir les données entrées par un utilisateur ou lues d'un fichier dans le type voulu.
{% endnote %}

### `byte`{.language-} et `str`{.language-}

Par défaut toutes les chaînes de caractères sont de type `str`{.language-}, et encodées en `utf-8`. Si on veut connaître explicitement les octets d'une chaîne, il faut l'encoder en un autre format par la méthode `encode`{.language-}  des chaines de caractères qui rend un objet de type byte qui est une suite d'octets.

C'est comme une chaîne de caractères mais qui commence par `b` . On peut ensuite décoder un byte pour le retransformer en `str`{.language-} :

```python
x = "ma chaîne de caractères"
x_en_byte = x.encode('utf8')  # devient : b'ma cha\xc3\xaene de caract\xc3\xa8res'
re_x = x_en_byte.decode('utf8')
```

Ceci va s'avérer utile lorsque l'on récupérera des fichiers depuis internet. Ce seront des `byte` qu'il faudra re-écrire en `utf8`.

Les différents encoding possibles sont disponibles [dans la documentation](https://docs.python.org/3/library/codecs.html#standard-encodings).

### Exercices

On utilisera [les nombres de Mersenne](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier) comme prétexte à la manipulation de chaines de caractères en python. Ces exercices sont pour une grande partie tirés d'un cours donné il y a quelques temps par Aristide Grange, à l'université Paul Verlaine de Metz.

{% exercice %}
Notez `m27` le 27ième nombre de Mersenne $2^{44497} -1$ :
{% endexercice %}
{% details "solution" %}

```python
m27 = 2 ** 444497 - 1
```

{% enddetails %}

{% exercice %}
Combien de chiffres en base 10, 2 et 16 possède ce nombre ?
{% endexercice %}
{% details "solution" %}

* en base 10 : `len(str(m27))`{.language-} : conversion de l'entier en chaîne de caractères puis son nombre de chiffres
* en base 2 : `len(bin(m27)) - 2`{.language-} : `bin` transforme un entier en sa représentation binaire. C'est une chaîne de caractères qui commence par `0b` donc on retranche 2 à la longueur.
* en base 16 : `len(hex(m27)) - 2`{.language-} : `hex` transforme un entier en sa représentation hexadécimale. C'est une chaîne de caractères qui commence par `0x` donc on retranche 2 à la longueur.

{% enddetails %}

#### Méthodes de chaines de caractères

Utilisez la documentation sur les [méthodes de chaines](https://docs.python.org/3/library/stdtypes.html#string-methods) en python pour résoudre les exercices suivants

{% exercice %}
Index de la première occurrence de `1234` dans m27. Et de la deuxième ?
{% endexercice %}
{% details "solution" %}

* `str(m27).find('1234')`{.language-}
* `str(m27).find('1234', 19260 + 1)`{.language-} : la première occurrence est à l'indice 19260, on cherche donc après.
* on peut faire en une ligne : `str(m27).find('1234', str(m27).find('1234') + 1)`{.language-}

{% enddetails %}

{% exercice %}
Nombre de 2 dans m27, nombre de 7
{% endexercice %}
{% details "solution" %}

* `str(m27).count('2')`{.language-}
* `str(m27).count('7')`{.language-}

{% enddetails %}

{% exercice %}
Remplacer des 2 par des 7 dans m27.
{% endexercice %}
{% details "solution" %}

`str(m27).replace('2', '7')`{.language-}

{% enddetails %}

{% exercice %}
Échanger les 2 et les 7 dans m27
{% endexercice %}
{% details "solution" %}

`str(m27).replace('2', 'X').replace('7', '2').replace('X', '7')`{.language-}

{% enddetails %}

#### Slice

{% aller %}
Comme pour les listes, on peut [utiliser les *slices*]({{"/cours/coder-en-python/listes/"  }}#slice) pour copier des parties de chaîne.
{% endaller %}

Ainsi `"abcdefghijklmnopqrstuvwxyz"[2:15:4]` vaut : `'cgko'`.

{% exercice %}
Quels sont les 10 premiers chiffres de m27 ?
{% endexercice %}
{% details "solution" %}

`str(m27)[:10]`{.language-}

{% enddetails %}

{% exercice %}
Quels sont les 10 derniers chiffres de m27 ?
{% endexercice %}
{% details "solution" %}

`str(m27)[-10:]`{.language-}

{% enddetails %}

{% exercice %}
Est-ce que m27 est un [palindrome](https://fr.wikipedia.org/wiki/Palindrome) ?
{% endexercice %}
{% details "solution" %}

`str(m27) == str(m27)[::-1]`{.language-} (`s[::-1]`{.language-} renverse la chaîne)

{% enddetails %}
