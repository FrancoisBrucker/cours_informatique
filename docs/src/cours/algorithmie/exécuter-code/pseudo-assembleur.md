---
layout: layout/post.njk

title: Pseudo-assembleur

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

> TBD : dire que structure de donnée = code.

Nous allons présenter une version _"minimale"_ de pseudo-code que nous appellerons pseudo-assembleur. Cet assembleur idéal et théorique nous permettra de faire le lien entre pseudo-code et le langage machine qui est effectivement exécuté.

## Objet et variables

{% note "**Définition**" %}
Les objets que peut manipuler le pseudo-assembleur sont les caractères `0` et `1` et les suites finies de ces caractères.
{% endnote %}

Par exemple l'objet de nom `o` :

```python
o = 1011001
```

Dans un pseudo-code, l'endroit où sont stockés les objets n'est pas défini, dans le pseudo-assembleur, on les stocke explicitement dans un tableau nommé **_mémoire_** :

{% note "**Définition**" %}
La **_mémoire_** est un tableau $M$ de taille $N$ où chaque case peut contenir soit le caractère `0`, soit le caractère `1`.
{% endnote %}

Chaque objet $o = o_0\dots o_{p-1}$, une suite finie de `0` et de `1`, est  stocké dans des cases contiguës de la mémoire.

L'objet `o` de tout à l'heure sera alors rangé :

```python
    01234567
o = 11010100

M[i + 0] = 1
M[i + 1] = 1
M[i + 2] = 0
M[i + 3] = 1
M[i + 4] = 0
M[i + 5] = 1
M[i + 6] = 0
M[i + 7] = 0
```

Attention à la lecture, **_le bit de poids fort_** de l'objet, celui le plus à gauche, est d'indice le plus petit.

{% attention %}
Les bits de l'objet sont numérotés dans l'ordre opposé de leur lecture.
{% endattention %}

Ce stockage permet de définir les références :

{% note "**Définition**" %}
Une _**référence**_ d'un objet est l'adresse du premier indice en mémoire le contenant.
{% endnote %}

Une variable est alors une référence nommée :

{% note "**Définition**" %}
Une _**variable**_ est un nom auquel est associé une référence à un objet.
{% endnote %}

La mémoire étant finie, la référence à un objet est toujours codée sur $\log_2(N)$ bits. Ceci permet de définir rigoureusement un tableau :

{% note "**Définition**" %}
Un _**tableau**_ de taille $n$ est suite finie et contiguë de $n \cdot\log_2(N)$ cases mémoire. Chaque $\log_2(N)$ bits successifs en mémoire contient la référence d'un objet.
{% endnote %}

> TBD : exemple avec mémoire, objet et tableau. Et variables nommées qui les références. Pour l'instant, les variables ne sont pas en mémoire (on le fera avec la pile et le modèle de von Neumann).

### Objets entiers

L'objet entier n'existe pas à proprement parler, mais on suppose qu'une suite finie de $\log_2(N)$ bits, qui correspond à une adresse, peut aussi être vue comme un entier. Pour cela, on on possède les deux fonctions suivantes :

- $u: \\{0, 1\\}^{\log_2(N)}\rightarrow \mathbb{N}$ qui rend l'entier associé à la suite considérée comme sa représentation binaire
- $s: \\{0, 1\\}^{\log_2(N)}\rightarrow \mathbb{Z}$  qui rend l'entier associé à la suite considérée comme sa représentation binaire en [le complément à deux](https://fr.wikipedia.org/wiki/Compl%C3%A9ment_%C3%A0_deux)

Pour l'objet `o = 1011001` précédent, on a :

- `u(o) = 212`
- `s(o) = -44`

Si `o` code un entier, c'est qu'une adresse mémoire est codée sur 8bits et donc que sa taille vaut $N = 2^8 = 256$.

### Équivalence avec le pseudo-code

#### Tailles des objets

Dans un pseudo-code, on ne suppose pas que l'on possède une mémoire finie. Tous les objets peuvent être aussi long qu'ils le veulent (tout en restant fini).

Le pseudo-assembleur permet de tenir compte de ceci : si un programme en pseudo-assembleur atteint la limite de la mémoire, on stope sont exécution et on la recommence avec une mémoire deux fois plus grande. 

#### Objets du pseudo-code

Les objets du pseudo-code
> objet :
On l'a vu, [un programme ne peut manipuler que des suites finies de `0` et de `1`](../../bases-théoriques/définition/#paramètres-binaires){.interne}. On peut donc sans perte de généralité considérer que 
> entier on peut les découper en base $N$, on l'a vu

> taille finie de la mémoire : on recommence en doublant si nécessaire.

## Fonctions et appel de fonctions

## TBD


{% note "**Définition**" %}
Les objets manipulés par le langage machine universel sont des suites finies de "0" et de "1".
{% endnote %}



Et connaître sa taille `l(o) = 8`{.language-}
Enfin, on doit pouvoir interpréter un objet comme un entier :

- positif (on dit **_unsigned_**) en utilisant la représentation binaire de l'objet : `u(o) = 212`
- relatif (on dit **_signed_**) en utilisant [le complément à deux](https://fr.wikipedia.org/wiki/Compl%C3%A9ment_%C3%A0_deux) : `s(o) = -44`

Remarquez que le complément à deux dépend de la taille de la suite, ce qui semble contre intuitif mais sera justifié par la suite.
Il existe une autre possibilité, moins utilisée car moins pratique algorithmiquement, qui est de dédier un bit au signe usuellement celui le plus à gauche.

{% note "**Définition**" %}
Le bit le plus à gauche, donc celui d'indice le plus élevé, est appelé **_bit de poids fort_**.
{% endnote %}

On a vu que [tout objet d'un algorithme](../bases-théoriques/définition/#paramètres-binaires) pouvait être représenté par une suite finie de "0" et de "1" donc :

{% note "**Proposition**" %}
Un programme et le langage machine universel utilisent les mêmes objets.
{% endnote %}

### Opérations

Le pseudo-code doit permettre de faire les opérations arithmétiques courantes sur les objets :

- plus, moins, fois et divisé pour les entiers relatifs et les approximations des réels
- plus, moins, fois et divisé pour les approximations de réels
- concaténation des chaines de caractères

L'intérêt d'utiliser des suites binaires est que toutes les opérations arithmétiques peuvent se réaliser avec les deux opérations logiques suivantes :

- `copie(x)`
- `SHIFT(x, y)` rend un objet contenant la concaténation de y0...0 ajout de s(x) 0 à droite de y si s(x) > 0 et de -s(x) 0 à gauche si s(x) < 0
- `NAND(x, y)` : opérateur logique NON ET.

En effet, il est possible d'[obtenir toutes les opérations logiques avec NAND](https://en.wikipedia.org/wiki/NAND_logic) et l'opération SHIFT permet d'ajouter des bits à gauche ou à droite d'un objet (si on veut ajouter des 1 on peut fait NOT(SHIFT(x, NOT(y))))

Ou 1 ou 2 paramètre et une sortie.

### Structures de contrôles

> Saut conditionnel

### Fonctions

> Dans la mémoire directement. Variable = adresse du début de l'objet.
> mémoire infinie
> 

> 

### Lier Variables et objets

Comme on a que la mémoire qui est une suite de 0 et de 1 pour stocker les objets et les variables//
> TBD exemple de 2 objets un qui fait hello et l'autre qui fait -3.
> 
Pour chaque objet il faut pouvoir connaitre la taille
> savoir distinguer un nombre d'un objet : connaitre sa taille. l'endrait dans la mémoire
> 
> connaitre la taille d'un objet

### Opérations

#### Bit à bit

#### Arithmétiques

dérivées des

#### Registres

> ce qui amène a avoir que NOT et ADD comme opération. Le montrer 
> arithmétique et bit à bit
> saut
> paramètre des opérations dans des "Registres" il y en a peu.

