---
layout: layout/post.njk
title: Mémoire, variables et objets

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Nous ne rentrerons pas dans les détails, la gestion de la mémoire est quelque chose de compliqué. Nous nous contenterons d'en présenter les caractéristiques fondamentales et les conséquences que cela implique sur la gestion des variables et des objets.

{% attention %}
Les explications ci-après sont **très simplifiées**. Nous nous contentons d'expliquer les principes pour que vous compreniez les enjeux de la gestion de la mémoire et l'intérêt qu'il y a à travailler par références lorsque l'on code avec des objets.
{% endattention %}

On peut considérer la mémoire d'un ordinateur comme un long tableau de taille fixe, mesurée en [octet](https://fr.wikipedia.org/wiki/Octet) (appelé _byte_ en anglais).

![mémoire](mémoire.png)

{% info %}
Un octet correspond à 8bits, permettant d'encoder $2^8 = 256$ informations ou nombres de $00000000$ (0 en base 10) à $11111111$ ($255=2^8-1$ en base 10).
{% endinfo %}

Comme un programme n'est jamais seul à être exécuté sur un ordinateur et que — pour des raisons de sécurité — un programme $A$ ne doit pas pouvoir accéder à la mémoire utilisée par un programme $B$ :

{% note %}
Le **système d'exploitation** est le seul à pouvoir accéder à une case donnée de la mémoire via son indice, comme on pourrait le faire avec un tableau normal. Un programme spécifique en revanche, ne peut accéder qu'à la partie de la mémoire qui lui a été allouée par le système d'exploitation.
{% endnote %}

## Accéder/allouer de la mémoire

Comme le système d'exploitation alloue de la mémoire et que plusieurs programmes se la partagent, il est uniquement possible pour un programme donné :

- de demander un **bloc** de $k$ octets **consécutifs** de la mémoire
- de libérer un bloc de mémoire alloué.

Il lui est en revanche impossible :

- de modifier la taille d'un bloc qui lui a été alloué
- de choisir l'endroit de la mémoire qu'il veut se faire allouer

On ne sait en effet pas si la mémoire à côté d'un bloc est libre ou non. Par exemple dans la figure ci-dessous, le seul emplacement libre en mémoire est la case blanche. Le programme _vert_ ne peut demander à augmenter le bloc de 3 octets qui lui est alloué, sinon il risque de rentrer en conflit avec le programme _rouge_ :

![mémoire partagée](mémoire-partagée.png)

{% note %}
Il est impossible d'augmenter simplement la taille d'un tableau alloué en mémoire. Il faut le recréer et recopier toutes ses valeurs dans un autre endroit de la mémoire.
{% endnote %}

## Stocker en mémoire

Avant de parler des moyens qu'a un programme de se rappeler ce qu'il a stocké, regardons comment on peut stocker des objets en mémoire en prenant l'exemple d'un entier.

La façon courante de stocker des objets est d'utiliser des **références**. Mais pour bien comprendre ce que c'est il faut commencer par parler (un peu) des valeurs.

### Stockage de valeurs

La mémoire étant une suite fini d'octets, si l'on veut stocker plus qu'un nombre entre 0 et 255 (ou -128, 127 s'il est [signé](https://en.wikipedia.org/wiki/Signed_number_representations)), il faut lui réserver plus d'une case.

Au début de l'informatique, il y avait plusieurs types d'entiers, selon ce qu'on voulait stocker. Par exemple :

- pour stocker des entier de 0 à 255 on avait le `char`{.language-} (1 octet)
- pour stocker des entiers de -32768 à 32767 on avait le type `int`{.language-} (2 octets)
- pour des entiers allant de −2147483647 à 2147483647 on avait le type `long`{.language-} (4 octets)

On précisait dans notre programme quel type d'entier on voulait utiliser pour telle ou telle variable et un espace mémoire lui était alloué :

{% note %}
Dans l'ancien temps une variable était l'indice en mémoire dans le lequel était stocké la donnée.
{% endnote %}

![un int](mémoire-int.png)

Ce type de fonctionnement a ses avantages :

- on ne se préoccupe pas de la taille en mémoire. La taille est fixée au départ selon le type de la variable choisie
- il y a une correspondance stricte entre variable et indice dans le tableau de la mémoire
- la taille d'un tableau d'objets d'un type fixé est facile à calculer.

Mais cela avait aussi de (très) gros inconvénients :

- comment coder 32768 si j'ai décidé au départ que ma variable était un `int`{.language-} ?
- on ne peut pas avoir de tableaux combinant plusieurs types d'objets car il est impossible de calculer facilement l'indice donné d'un tableau contenant plusieurs types .
- si on écrit `i = j`{.language-}, il **faut** recopier le contenu de `i`{.language-} (à l'adresse mémoire de `i`{.language-}) dans `j`{.language-} (à l'adresse mémoire de `j`{.language-}) : un même objet ne peut pas avoir plusieurs noms.

{% info %}
Lorsque l'on fait de la programmation système (en codant en C ou encore en Rust par exemple), tout ceci est toujours vrai. Les entiers ne sont pas aussi grand qu'on veut comme lorsque l'on code en python. Ceci dit, un entier sur 32bits (4 octets) permet tout de même d'encoder $2^{32} = 4294967296$ entiers, ce qui est la plupart du temps largement suffisant.
{% endinfo %}

### Stockage d'objets

Actuellement — si l'on ne fait pas de programmation système — on préfère ne pas avoir à gérer directement la mémoire et surtout, on veut dissocier la variable de sa valeur : écrire `i = j`{.language-} doit signifier que l'objet désigné par la variable `j`{.language-} doit **aussi** être désigné par `i`{.language-}. Pour cela, on dissocie la variable de l'emplacement en mémoire de l'objet.

La définition actuelle d'une _variable_ est alors :

{% note %}
Une **_variable_** est une référence à un objet stocké en mémoire.
{% endnote %}

Le moyen de le plus simple de définir une référence, c'est de prendre l'indice de la première case mémoire contenant l'objet.

Prenons un exemple : supposons que notre ordinateur dispose de 16Go (gigaoctets) de RAM. L'indice de notre tableau de mémoire va alors de $0$ à $10^9-1$ : il faut 4 octets pour stocker un indice en mémoire.

![référence](mémoire-référence.png)

La figure ci-dessus montre alors une variable (_verte_) représentant un objet entier (_orange_) : elle contient l'indice du tableau de la mémoire contenant le premier élément de l'objet (sa référence, $i^\star$ dans la figure).

{% info %}
Les ordinateurs actuels codent une adresse mémoire sur 64bit, ce qui permet d'allouer $2^{64}\text{O} \simeq 18446744\text{TO}$, ce qui est largement plus que la mémoire courante qui est d'environ $32\text{GO} = 0.03\text{TO}$ pour une machine de bureau.

{% endinfo %}

Les bénéfices de cette méthode sont énormes :

- les objets sont uniques, en écrivant `i = j`{.language-} les deux variables ont le même objet en référence
- un tableau devient un tableau de référence, il peut contenir des types d'objets différents sans soucis
- on peut facilement modifier un objet, sans avoir à changer toutes les variables qui le référencent.

{% attention %}
Comme on manipule directement les objets, il faut faire attention aux effets de bords lorsqu'on les modifie.
{% endattention %}

Par exemple en python :

```python
t = [1, 2, 3]
u = t
u[1] = 12
print(t)
```

{% details "que vaut `print(t)`{.language-} ?" %}

`[1, 12, 3]`{.language-} on a modifié l'objet référencé par `u`{.language-}, qui est le même que celui référencé par `t`{.language-}

{% enddetails %}

Plus insidieux :

```python
t = [1, 2, 3]
u = [1, t, "?"]
u[1][1] = 12
print(t)
```

{% details "que vaut `print(t)`{.language-} ?" %}

`[1, 12, 3]`{.language-} on a modifié l'objet référencé par `u[1]`{.language-}, qui est le même que celui référencé par `t`{.language-}

{% enddetails %}

## Pile et tas

En règle générale et variables et objets ne sont pas rangées au même endroit de la mémoire :

{% note %}
Un programme stocke les variables (des références) dans un endroit de la mémoire nommé **_pile_** et les objets (cases consécutives allouées en mémoire) dans l'endroit de la mémoire nommé **_tas_**.

- la **_pile (stack)_** permet d'entasser les variable (des références). Chaque case de la pile a exactement la taille d'un indice de la mémoire
- le **_tas (heap)_** est un espace contigu de la mémoire (un tableau) dont on peut allouer ou dé-allouer une partie.
  {% endnote %}

A chaque fois qu'une variable est crée, le programme :

- alloue de la mémoire dans le tas qui contiendra l'objet. Si c'est un nouvel objet, ou incrémente le nombre de variables pointant sur cet objet
- le premier indice de la mémoire contenant l'objet est empilée dans la pile (c'est la variable)

Lorsque qu'une variable disparaît :

- on dépile l'indice pointant sur l'objet de la pile
- on décrémente le nombre de variables pointant sur cet objet et si ce nombre vaut 0, on dé-alloue l'objet

Cette façon de procéder pour gérer les variables est appelé **_stockage par référence_**. La pile contient une adresse (une référence) correspondant à l'objet qui lui est stocké dans le tas.

{% info %}
Certains langages comme le C ou le Rust par exemple permettent également de stocker certaines variables directement dans la pile (les entiers par exemple, mais en vrai tout objet dont on peut connaître précisément la taille). Ceci accélère le code (on a pas besoin d'un sauter de la pile à la mémoire du tas ce qui fait gagner une indirection) mais complique le codage (la manipulation du tas est explicite et il faut faire très attention à sa gestion).
{% endinfo %}

Pour plus d'informations, vous pouvez par exemple regarder la vidéo ci-après qui explicite le tas et la pile :

{% lien %}

[Pile et tas](https://www.youtube.com/watch?v=5OJRqkYbK-4)

{% endlien %}

