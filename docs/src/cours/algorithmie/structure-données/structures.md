---
layout: layout/post.njk 
title:  "Structures de données"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---


Un structure de donnée généralise les tuples et est une version algorithmique des objets de la programmation orientée objet. Une fois définis on pourra utiliser une structure comme un nouveau type de variable.


{% attention2 "**À retenir**" %}
Une **_structure de données_** est composée :

- d'**_attributs_** qui correspondent aux différentes données la constituant (de types de base ou d'autres structures de données). On accède au attributs et aux méthodes d'une structure avec la notation pointée.
- de **_méthodes_** qui sont des fonctions permettant d’interagir avec une donnée de cette structure.

Une structure de donnée définit un nouveau type qui peut être utilisé ensuite comme un type de base.
{% endattention2 %}

Une fois une structure de données définie, on pourra l'utiliser comme un type de base dans tous nos algorithmes. La taille d'une structure est déterminée par rapport à la taille de ses attributs :

Pour qu'une structure de donnée puisse être utilisée, il est crucial de connaître la complexité de la création d'un objet de la structure et de chaque méthode de celle-ci.

## Attributs

Une structure de donnée est composée d'**_attributs_** qui la définisse :

{% note2 "**Définition**" %}
Une structure de donnée est définie par ses **_attributs_** qui sont des variables. Par exemple :

```pseudocode
structure Nom_structure:
    v1: type1
    v2: type2

```

Définit **_une structure_** de nom `Nom_structure`{.language-} ayant deux attributs nommés `v1`{.language-} (de type `type1`{.language-}) et `v2`{.language-} (de type `type2`{.language-}).

On crée un objet de la structure en affectant toutes ses variables :

```pseudocode
x := Nom_structure
x ← Nom_structure{v1: o1, v2: o2}
```

On accède à un attribut via la **_notation pointée_** :

```pseudocode
x.v1 ← o'
```

En notation pointée `a.b`{.language-} signifie que `b`{.language-} est un attribut de la structure `a`{.language-}.
{% endnote2 %}

Par exemple si on veut définir une structure pouvant simuler des points de $\mathbb{R}^2$, on pourrait écrire :

```pseudocode
structure Point:
    x: réel
    y: réel
```

Que l'on crée en affectant tous ses attributs :

```pseudocode
x := Point
x ← Point{x: 3.1, y:0.0}
```

Par rapport au tuple, les attributs sont des variables et possèdent ainsi des noms, ce qui rend l'accès aux attributs bien plus simple :

```pseudocode
algorithme affiche_point(p: Point) → ∅:
    affiche à l'écran p.x
    affiche à l'écran p.y
```

De plus, contrairement à un tuple, on peut tout à fait modifier les attributs d'un objet. Par exemple la fonction :

```pseudocode
algorithme additionne_point(p1: Point, p2: Point) → ∅:
    p1.x ← p1.x + p2.x
    p1.y ← p1.y + p2.y
```

Va modifier les attributs du premier paramètre.

## Création

{% note2 "**Définition**" %}
**_Créer_** un objet d'une structure revient à créer ses attributs (des variables) **et** y affecter des objets. 

La taille en mémoire d'un objet est proportionnelle à la taille de ses attributs.
{% endnote2 %}

Pour que ce processus ne soit pas lourd à écrire on s'autorise les abus de notations suivant

### Initialisation par défaut

Pour être sur que les paramètres sont initialisés par défaut, on utilise _l'abus_ suivant :

```pseudocode
structure Point:
    x: réel ← 0.0
    y: réel ← 0.0

```

Ce qui nous permettra d'écrire :

```pseudocode
p := Point
p ← Point{}
```

Qui correspond au code :

```pseudocode
p := Point
p ← Point{x: 0.0, y:0.0}
```

### Constructeur

On utilisera tout au long de ce cours le processus de construction d'objets suivant :

{% note2 "**Définition**" %}

Processus de construction d'une structure de donnée :

1. les différents attributs sont crées sous la forme de variables
2. les initiations explicites des attributs sont effectuées
3. les initiations par défaut des attributs **sans initialisation explicite** sont effectuées

{% endnote2 %}
{% info %}
Au terme de ce processus tous les attributs sont initialisés.
{% endinfo %}

Le processus précédent nous permet d'écrire le pseudocode suivant :

```pseudocode
structure Point:
    x: réel
    y: réel ← 2 * x

```

Qui nous permet d'écrire :


```pseudocode
p := Point 
p ← Point{x: 3.1}
```

Le code précédent affectera bien 6.2 à `p.y`{.language-}. Notez que l'on peut aussi écrire :

```pseudocode
p := Point 
p ← Point{x: 3.1, y:0}
```

Comme l'attribut `y` est affecté à la construction, l'initiation par défaut de `y` n'est pas utilisée. Enfin, comme `x` n'a pas de valeur par défaut, il est indispensable de l'initialiser à la construction.

## Méthodes

L'intérêt fondamental des structures de données est de leur associer des fonctions spécifiques, appelées **_méthodes_**. Le but des méthodes est d'opérer sur les objets de la structure.

{% note2 "**Définition**" %}
Une **_méthode_** est une fonction spéciale de signature :

```pseudocode
méthode (self: Struct) nom_méthode(p1: type1, ..., pn: typen) → type_sortie
```

Une méthode est associée à la structure (`Struct`{.language-} dans notre exemple) du type du paramètre définit à gauche de son nom (`self`{.language-} dans notre exemple). Son utilisation se fait via la notation pointée. Si `s`{.language-} est un objet de la structure de donnée `Struct`{.language-}, on pourra écrire :

```pseudocode
s.nom_méthode( ... )
```

{% endnote2 %}


Transformons la fonction `additionne_point`{.language-} précédente en méthode  de `Point`{.language-} :

```pseudocode/
structure Point:
    x: réel ← 0.0
    y: réel ← 0.0

méthode (self: Point) addition(p: Point) → ∅:
    self.x ← self.x + p.x
    self.y ← self.y + p.y

```

Et utilisons là :

```pseudocode

(p1 := Point) ← Point{x: 1}
(p2 := Point) ← Point {x: 4, y: 7}

affiche p1.x et p1.y  # affiche 1 et 0
p1.addition(p2)
affiche p1.x et p1.y  # affiche 5 et 7
```

## Complexités

Manipuler des objets ou des structures en algorithmie va nécessiter des opérations élémentaires qu'il faut compter pour en connaître la complexité. On peut classer ces manipulations en trois grandes catégories :

{% note2 "**Définition**" %}

Pour chaque type de donnée (base ou structure) ses **_complexités_** sont  :

- **_complexité de création_** d'un objet de ce type
- **_complexité de suppression_** d'un objet de ce type
- **_complexité d'opération_** qui regroupe la complexité de chaque opération ou méthode lié à ce type

{% endnote2 %}

Toutes les manipulations d'objets de type basique (booléens, bit, entiers, réels, caractères et chaines de caractères) ou de type tableau sont en $\mathcal{O}(1)$ opérations. Ce n'est plus le cas lorsque l'on utilise des types plus complexes.

C'est d'autant plus crucial en code où l'on ne connaît pas le code des différentes méthodes que l'on utilise. Ne vous laissez pas méprendre : ce n'est pas parce qu'une instruction fait 1 seule ligne que sa complexité est en $\mathcal{O}(1)$. Par exemple en python la complexité de la méthode `index`{.language-} des listes (comme une `l.index("?")`{.language-}) ou encore  la méthode `max`{.language-} de python, qui prend en entrée une liste `l` :

```python
l = [1, 3, 2, 6, 4, 5]
print(l.max())
```

Sont de complexité $\mathcal{O}(n)$  où $n$ est la taille de la liste `l` et pas $\mathcal{O}(1)$. Il **faut** en effet parcourir tous les éléments d'une liste (a priori non triée) pour en trouver le maximum.

{% attention %}
Lorsque vous utilisez des fonctions et des méthodes en python, **il faut toujours vérifier la complexité de celles-ci**. Ce n'est pas toujours $\mathcal{O}(1)$.
{% endattention %}


## Types spécifiques

Il peut être utile de définir des types génériques ou spécifiques pour nos structures.

### Génériques

Tout comme un tableau peut stocker tout type de données, il peut être intéressant de définir une structure générique, c'est à dire pouvant gérer plusieurs types de la même façon, plutôt que de définir une structure par type.

{% lien %}
[type générique](https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9ricit%C3%A9)
{% endlien %}

Pour être explicite, On signifie la généricité entre "<>" dans la définition de la structure, par exemple dans l'exemple suivant :

```pseudocode
structure Marque<T>:
    valeur: T

    x: entier ← 0
    y: entier ← 0

```

L'attribut valeur est du **_type générique_** `T`{.language-}. Ce type est abstrait et doit être défini explicitement à l'utilisation. Par exemples :

```pseudocode
utm ← Marque<chaîne> {valeur: "Marseille", x: 694669, y: 4796927}
masse ← Marque<réel> {valeur: 3.14}
```

On peut bien sur combiner le tout avec des exemples plus ou moins tordu comme :

- `[Marque<réel>]`{.language-} : un tableau de Marques à valeurs réelles
- `Marque<[Marque<Marque<chaîne>>]>`{.language-} : une Marque à valeurs valant un tableau de Marque à valeur de Marque de chaînes.

Mais la plupart du temps, on reste simple.

### Sous-structures

On aura parfois besoin de spécifier dans nos structures des attributs dont les paramètres ont sont fixes ou dans une gamme de valeurs. Plutôt que de faire un type particulier on pourra utiliser une syntaxe similaire aux génériques en spécifiant le paramètre qui doit être fixé ou contraint :

```pseudocode
structure Point:
    coords: [entier]<longueur: 2>
```

L'exemple précédent spécifie que la longueur du tableau est forcément de 2.