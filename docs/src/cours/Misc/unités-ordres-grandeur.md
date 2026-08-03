---
layout: layout/post.njk

title: Unités et ordres de grandeur

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

L'informatique traite en interne des suites finies de 0 ou de 1. Les longueur de ces suites vont dépendre de l'usage que l'on en fait, mais elles sont usuellement découpées en segments de taille fixe.

## Unités

{% lien %}
<https://fr.wikipedia.org/wiki/Unit%C3%A9_de_mesure_en_informatique>
{% endlien %}

En informatique tout part du **_bit_**, d'abréviation `b` qui est l'unité fondamentale et permet de stocker 2 valeurs différentes (classiquement 0 ou 1).

On a coutume de considérer les quantités suivantes :

- 8b qui forment un **_byte_** ou **_octet_**, d’abréviation `B`
- 16b, donc 2B qui forment un **_word_** ou **_mot_**, d'abréviation `W` 
- 32b, donc 4B et 2W qui forment un **_dword_** (**_double word_** ou  **_double mot_**), d'abréviation `DW`
- 64b, donc 8B, 4W ou encore 2DW et forment un **_qword_** (**_quad word_** ou  **_quadruple mot_**), d'abréviation `QW` qui est la taille standard de travail d'un processeur.

{% note "**Unité par défaut**" %}

Un objet informatique sera, sauf mention contraire, constitué d'une suite de byte (`B`).

{% endnote %}


## Notations

Un byte ou une suite de byte peut être interprétée de multiples manières :

- comme un entier positif,
- comme un entier relatif,
- [une couleur](https://fr.wikipedia.org/wiki/Rouge-vert-bleu),
- [un caractère](https://fr.wikipedia.org/wiki/UTF-8),
- [une instruction machine](https://fr.wikipedia.org/wiki/Langage_machine),
- ...

{% attention2 "**À retenir**" %}
La signification d'une suite de bytes dépend du contexte. 
{% endattention2 %}

Si on les représente parfois directement par leur représentation binaire, leur représentation canonique est sous une forme numérique :

- décimale : `42`
- binaire : `101010`
- hexadécimale : `2A`

[La notation hexadécimale](https://fr.wikipedia.org/wiki/Syst%C3%A8me_hexad%C3%A9cimal) est pratique car un byte est encodé par un nombre allant de 00 à FF, ce qui fait qu'une suite de byte est encodé par un nombre qui est la concaténation du nombre de chaque byte (si l'on représente chaque nombre par 2 chiffres allant de 0 à F). 

{% note "**Représentation par défaut**" %}
Une suite de byte est représentée par défaut par sa représentation hexadécimale.
{% endnote %}
{% info %}
Lorsque la représentation par défaut est la représentation décimale :

- on fera commencer la notation binaire d'un nombre par `0b`, par exemple `0b101010` représentera le nombre 42.
- on fera commencer la notation hexadécimale d'un nombre par `0x` (dans les language de programmation) ou `#` (pour les couleurs), par exemple `0x2A` représentera le nombre 42 et `#BBAADD` [une couleur mauve](https://www.color-hex.com/color/bbaadd).
{% endinfo %}

## Multiples

Les taille de mémoire sont grande, on ne peut les manipuler directement en byte. Le système décimal nous permet de parler de multiples en kilo, méga, giga et tera :

- un ***kilo byte***, kB, pour $10^3$ byte et ***kilo bit***, kb, pour $10^3$ bits
- Un ***méga byte***, MB, qui vaut $10^3 \cdot 10^3 = 10^{2 \cdot 3} = 10^{6}$ byte et un ***méga bit***, Mb, qui vaut $10^{6}$ bit
- un ***giga byte***, GB et ***giga bit***, Gb, qui valent $10^9$ byte ou bit
- un ***tera byte***, TB et ***tera bit***, Tb, qui valent $10^{12}$ byte ou bit

Mais lorsque l'on parle de mémoire, on a coutume de chercher à voir la taille en byte de mémoire d'objets selon une quantité d'adresses exprimé en bit. De là 1 KB n'a que peu de sens. C'est 1024b qui en a (le nombre de byte adressable par 10 bits).

C'est pourquoi, on parlera de multiple binaires comme le ***kibi  byte***, pour **ki**lo **bi**naire d'unité kiB, qui vaut $2^{10} = 1024$ byte.

La différence n'est pas grande mais autant être précis.

On peut ainsi progresser dans les multiples :

- un ***kibi byte***, KiB, qui vaut $2^{10} \cdot 2^{10} = 2^{2 \cdot 10} = 2^{20}$ byte
- un ***mébi byte***, MiB, qui vaut $2^{10} \cdot 2^{10} = 2^{2 \cdot 10} = 2^{20}$ byte
- un ***gibi byte***,GiB, qui vaut $2^{30}$ byte (attention, ne cofondez pas avec un [Gibi](https://www.youtube.com/watch?v=3EhIQSUU4Fk&list=PLsbtzZi9n5PtE3M1zlzwQByojW7xDhExY&index=70), ça n'a rien à voir)
- un ***tebi byte***, TiB, qui vaut $2^{40}$ byte

## Ordres de grandeur

```
b  X                                                                  1b       2^1  =                    2 possibilités
B  XXXXXXXX                                                           8b = 1B  2^8  =                  256 possibilités
W  XXXXXXXXXXXXXXXX                                                  16b = 2B  2^16 =                65536 possibilités
DW XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                  32b = 4B  2^32 =           4294967296 possibilités
QW XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  64b = 8B  2^64 = 18446744073709551616 possibilités
```

<!-- TBD 

- taille mémoire, usb. disque dur
- taille cache
- ombre d'atomes dans l'univers -->

Lorsque l'on vous donne ce genre de grandeurs, ayez à l'esprit qu'il n'y a que de l'ordre de $10^{80}$ atomes dans l'univers, qui est environ égal à $2^{256}b = 2^{32}B$ soit 4 gibi byte ou encore 4.3 GB (ce qui est très peu au final).

{% attention2 "**À retenir**" %}
Le nombre de possibilité augmente de façon exponentielle par rapport à sa taille. 

Toutes les particules de l'univers peuvent être nommée par un suite de 256b.
{% endattention2 %}


{% lien %}
- <https://fr.wikipedia.org/wiki/Ordres_de_grandeur_de_nombres#1039_%C3%A0_10100>
- [Calcul du nombre d'atomes dans l'univers](https://www.youtube.com/watch?v=hIpSCJLNqtk)
{% endlien %}
