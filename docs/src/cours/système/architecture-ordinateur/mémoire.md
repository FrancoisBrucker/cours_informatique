---
layout: layout/post.njk

title: Mémoire

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les contraintes et choix matériels vont avoir des conséquence sur le code. En particulier pour la mémoire qui est au cœur du système

## Type de mémoire

- DDR5 : <https://fr.wikipedia.org/wiki/DDR5_SDRAM>
- fonctionnement : <https://fr.wikipedia.org/wiki/Double_data_rate>

La vitesse d'accès et de transfert augmente.

## Valeurs

### Endianness

On l'a vu, la valeur d'un byte dépend de son contexte.  C'est encore pire lorsque l'on considère des valeurs sur plusieurs adresses consécutives :

```
Indice   :        1       2
Valeur b : 0000110010010001
       B :       12     145 
```

Sa valeur en word va dépendre de selon qu'on lire la valeur par indice croissant ou décroissant.

Si on lit par indice décroissant (sens commun de lecture) on trouvera l'entier binaire : `0000110010010001` qui correspond à l'entier décimal 3217.

Et si on lit par indice décroissant, on trouvera l'entier binaire : `1001000100001100` qui lui correspond à l'entier décimal 37132.

{% attention %}
L'unité fondamentale de lecture est **toujours** le byte, on inverse donc les bytes, pas les bits qui le compose.
{% endattention %}

Ceci est loin d'être anecdotique et s'appelle l'[Endianness](https://fr.wikipedia.org/wiki/Boutisme) :

- les processeurs ARM, tout comme les protocoles réseau ou PCIe sont dit *big endian* les bytes sont lu de droite à gauche (sens de lecture usuel)
- les processeur intel sont dit *little endian* les byte sont lu de gauche à droite (sens non usuel)

Un word étant composé de deux byte, le byte des 8 premiers bits est dit de poids faible et le byte des 8 derniers bits est dit byte de poids fort. Les système big endian mette le byte de poids fort à l'adresse la plus petite et les systèmes little endian à l'adresse la plus forte.

{% note %}
Il est important de connaître la taille des objets que l'on manipule et de laisser le système gérer l'Endianness pour nous.
{% endnote %}
{% info %}
L'Endianness est un exemple parmi tant d'autre que s'il existe une convention vous pouvez être sur que les deux choix seront choisis (écrire de gauche à droite, nord vers le haut, etc)
{% endinfo %}

### Padding

La quasi totalité des données manipulées par un processeur sont sur 64b (8B), parfois moins moins, mais quasi tout le temps strictement plus qu'un byte. Les transferts de données entre la mémoire et le processeurs sont optimisées pour une taille de 8B : si l'on cherche à lire à l'adresse A de la mémoire, la mémoire transférera les valeurs des cases A à A + 8.

Pour des raisons de coût, il est cependant impossible d'avoir ce comportement à toutes les adresses. La lecture des données se fait **toutes les 8 adresses** et non à chaque adresse. Si les données à lire ne sont pas sur un multiple de sa taille de lecture, il faudra faire deux lectures avant de rassembler les données. Par exemple pour une taille de lecture de 8B :

```
Adresse         : 012345670123456701234567
valeur à lire   :       XXXXXXXX
lecture 1       : XXXXXXXX
lecture 2       :         XXXXXXXX
recollage bus   :       XXXXXXXX
```

Alors que si c'est un multiple, une seule lecture suffit :

```
Adresse         : 012345670123456701234567
valeur à lire   :         XXXXXXXX
lecture 1       :         XXXXXXXX
recollage bus   :         XXXXXXXX
```

Si lon ne veut récupérer que 4B on peut transférer des données en une lecture pour toutes les données en multiple de 4 :

```
Adresse         : 012345670123456701234567
valeur à lire   :     XXXX
lecture 1       : XXXXXXXX
recollage bus   : 0000XXXX
```

C'est ce que l'on appelle les [problèmes d'alignement](https://fr.wikipedia.org/wiki/Alignement_en_m%C3%A9moire). Il faut s'arranger pour que nos données soient alignées avec la mémoire pour que la lecture se fasse en 1 cycle et non 2.

Ceci se fait habituellement pour nous, les compilateurs vont s'arranger pour les stocker chaque donnée à des multiples de leur taille en mémoire quite à perdre un peu de place (c'est ce que l'on appelle le padding). Les données sont alors dites *bien alignées*.

## Adressage logique et physique

Dans les OS actuels, la mémoire s'adresse sur 64b. C'est à dire qu'il est théoriquement possible d'adresser $2^{64}$ byte, c'est à dire 16[EiB](https://fr.wikipedia.org/wiki/Pr%C3%A9fixe_binaire#Tableaux_des_pr%C3%A9fixes_binaires_et_d%C3%A9cimaux) et donc 16777216 TiB.

Cette limite est actuellement inatteignable en pratique, c'est pourquoi pour limiter la complexité de l'adressage les processeurs actuels autorise moins d'adresse. Pour un (https://en.wikipedia.org/wiki/X86-64#Virtual_address_space_details) par exemple (pour un ARM, c'est pareil):

- seule 48bit sont adressables, des bit 0 à 47
- les bits 47 à 63 doivent être identiques (0 ou 1)

{% info %}
Cet adressage est dit ***logique*** (ou virtuel) car c'est l'adressage vu depuis le processeur. L'adressage ***physique***, directement sur la RAM, est lui autorisé sur 52bits.
{% endinfo %}
