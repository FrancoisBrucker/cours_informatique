---
layout: layout/post.njk 
title:  "Structures de données"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---



> TBD faire comme GO. Juste struct. Et ajouter un type méthode qui prend en receiver un objet.


Un structure de donnée généralise les tuples et est une version algorithmique des objets de la programmation orientée objet. Une fois définis on pourra utiliser une structure comme un nouveau type de variable.

## Attributs

Par défaut une structure de donnée va posséder des **_attributs_** qui regroupent les objets de la structure. Pour notre point en 2D on aurait la structure :

```pseudocode
structure Point:
    attributs:
        x: entier
        y: entier
```

Par rapport au tuple, les attributs sont des variables et possèdent ainsi des noms. Si on accède aux éléments d'un tuple avec son indice, on accède aux attributes par **_la notation pointée_** :

```pseudocode
algorithme affiche_point(p: Point) → vide:
    affiche à l'écran p.x
    affiche à l'écran p.y
```

En notation pointée `a.b`{.language-} signifie que `b`{.language-} dépend de `a`{.language-}.

Si `p`{.language-} est un point, `p.x`{.language-} signifie que `x`{.language-} est la valeur de l'attribut `x`{.language-} pour le point `p`{.language-}.

On peut tout à fait modifier les attributs d'un objet. Par exemple la fonction :

```pseudocode
algorithme additionne_point(p1: Point, p2: Point) → vide:
    p1.x ← p1.x + p2.x
    p1.y ← p1.y + p2.y
```

Va modifier les attributs du premier paramètre.

{% lien %}
[Notation pointée en python](https://reeborg.ca/docs/fr/oop/oop.html)
{% endlien %}

### Création

{% note "**Définition**" %}
**_Créer_** un objet d'une structure revient à créer ses attributs. La taille en mémoire d'un objet est proportionnelle à la taille de ses attributs.
{% endnote %}

Ainsi le code :

```pseudocode
p ← un nouveau Point
```

Va créer un nouveau point `p`{.language-} pour le quel on pourra accéder à ses attributs via la notation pointée :

```pseudocode
p.x ← 0
```

Comme toute variable nouvellement crée les valeurs des attributs est indéterminée : il faut **toujours initialiser avant de les utiliser**.

#### Initialisation par défaut

Pour être sur que les paramètres sont initialisés par défaut, on utilise _l'abus_ suivant :

```pseudocode
structure Point:
    attributs:
        x: entier ← 1
        y: entier ← -1

```

Qui correspond au code :

```pseudocode
p ← un nouveau Point
p.x ← 1
p.y ← -1
```

On peut bien initialiser partiellement les paramètres (en ne donnant qu'un valeur par défaut à `x` par exemple), mais ce n'est pas recommandé :

{% attention "**À retenir**" %}
Dans la mesure du possible donnez **toujours** une valeur par défaut à tous les attributs.
{% endattention %}

#### Initialisation explicite

Si l'on veut avoir des valeurs spécifiques pour nos attributs sans alourdir le code, on utilise _l'abus_ suivant :

```pseudocode
p ← Point {x: 3, y: 12}
```

Qui correspond au code :

```pseudocode
p ← un nouveau Point
p.x ← 3
p.y ← 12
```

Les valeurs non explicitement assignées aurons les valeurs par défaut s'il y en a.

#### Constructeur

On utilisera tout au long de ce cours le processus de construction d'objets suivant :

{% note "**Construction**" %}

1. les différents attributs sont crées sous la forme de variables
2. les initiations explicites des attributs sont effectuées
3. les initiations par défaut des attributs **sans initialisation explicite** sont effectuées

{% endnote %}
{% info %}
Une bonne pratique algorithmique est qu'au terme de ce processus tous les attributs soient initialisés.
{% endinfo %}

Ainsi pour la structure suivante :

```pseudocode
structure Point:
    attributs:
        x: entier
        y: entier ← 2 * x

```

Le code suivant produira des valeurs indéterminées pour `p.x`{.language-} et `p.y`{.language-} :

```pseudocode
p ← Point 
```

Le code suivant sera tel que `p.y = 6`{.language-} :

```pseudocode
p ← Point {x: 3}
```

Le code suivant sera tel que `p.y = 42`{.language-} :

```pseudocode
p ← Point {x: 3, y: 42}
```

{% exercice %}
Que donnent les exemples précédent avec la structure :

```pseudocode
structure Point:
    attributs:
        x: entier ← 0
        y: entier ← 2 * x

```

{% endexercice %}
{% details "corrigé" %}

1. `p ← Point`{.language-} : `p.x = 0`{.language-} et `p.y = 0`{.language-}
2. `p ← Point {x: 3}`{.language-} : `p.x = 3`{.language-} et `p.y = 6`{.language-}
3. `p ← Point {x: 3, y: 42}`{.language-} : `p.x = 3`{.language-} et `p.y = 42`{.language-}
{% enddetails %}

### Méthodes

L'intérêt fondamental des structures de données est de leur associer des fonctions spécifiques, appelées **_méthodes_**. Le but des méthodes est d'opérer sur les objets de la structure. Transformons la fonction `additionne_point`{.language-} précédente en méthode :

```pseudocode/
structure Point:
    attributs:
        x: entier ← 0
        y: entier ← 0
    méthodes:
        fonction addition(p: Point) → vide:
            x ← x + p.x
            y ← y + p.y

```

On appelle les méthodes avec la notation pointée :

```pseudocode
p1 ← un nouveau Point
p2 ← Point {x: 4, y: 7}

affiche à l'écran p1.x et p1.y  # affiche 0 et 0
p1.addition(p2)
affiche à l'écran p1.x et p1.y  # affiche 4 et 7
```

Dans le code de l'addition, la notation pointée assure que les variables `x`{.language-} et `y`{.language-} des lignes 10 et 11 d la définition sont celle de l'objet à gauche de l'appel, ici `p1` dans le programme précédent.

### Résumé

{% attention "**À retenir**" %}
Une **_structure de données_** est composée :

- d'**_attributs_** qui correspondent aux différentes données la constituant (de types de base ou d'autres structures de données). On accède au attributs et aux méthodes d'une structure avec la notation pointée.
- de **_méthodes_** qui sont des fonctions permettant d’interagir avec une donnée de cette structure.

Une structure de donnée défini un nouveau type qui peut être utilisé ensuite comme un type de base.
{% endattention %}

Une fois une structure de données définie, on pourra l'utiliser comme un type de base dans tous nos algorithmes. La taille d'une structure est déterminée par rapport à la taille de ses attributs :

Pour qu'une structure de donnée puisse être utilisée, il est crucial de connaître la complexité de la création d'un objet de la structure ($\mathcal{O}(1)$ pour notre `Point`{.language-}) et de chaque méthode de celle-ci.

## Génériques

Tout come un tableau peut stocker tout type de données, il peut être intéressant de définir une structure générique, c'est à dire pouvant gérer plusieurs types de la même façon, plutôt que de définir une structure par type.

{% lien %}
[type générique](https://fr.wikipedia.org/wiki/G%C3%A9n%C3%A9ricit%C3%A9)
{% endlien %}

Pour être explicite, On signifie la généricité entre "<>" dans la définition de la structure, par exemple dans l'exemple suivant :

```pseudocode
structure Point<T>:
    attributs:
        valeur: T

        x: entier ← 0
        y: entier ← 0

```

L'attribut valeur est du **_type générique_** `T`{.language-}. Ce type est abstrait et doit être défini explicitement à l'utilisation. Par exemples :

```pseudocode
utm ← Point<chaîne> {valeur: "Marseille", x: 694669, y: 4796927}
masse ← Point<réel> {valeur: 3.14}
```

On peut bien sur combiner le tout avec des exemples plus ou moins tordu comme :

- `[Point<réel>]`{.language-} : un tableau de Points à valeurs réelles
- `Point<[Point<Point<chaîne>>]>`{.language-} : un Points à valeurs valant un tableau de Point à valeur de Point de chaînes.

Mais la plupart du temps, on reste simple.

## Sous-structures

On aura parfois besoin de spécifier dans nos structures des attributs dont les paramètres ont sont fixes ou dans une gamme de valeurs. Plutôt que de faire un type particulier on pourra utiliser une syntaxe similaire aux génériques en spécifiant le paramètre qui doit être fixé ou contraint :

```pseudocode
structure Point:
    attributs:
        coords: [entier]<longueur: 2>
```

> TBD vérifier que la suite est cohérente

## Mot clé `self`{.language-}

L'objet courant, celui qui appelle (à gauche du `.` en notation pointée), peut être parfois nommé par le mot-clé `self`{.language-}.

{% info %}
Certains langages comme python n'autorisent que cette notation ce qui rend le code sans ambiguïté, d'autres comme le java autorise les deux versions (avec ou sans `self`{.language-}).
{% endinfo %}

Cela permet d'utiliser la notation pointée partout (et est indispensable si l'on veut connaître l'objet appelant pour le rendre par exemple. Voir l'exemple suivant). En utilisant cette convention, le pseudocode de la structure devient :

```pseudocode
structure Point:
    attributs:
        x: entier ← 0
        y: entier ← 0
    méthodes:
        fonction addition(p: Point) → Point:
            self.x ← self.x + p.x
            self.y ← self.y + p.y

            rendre self
```

Dans l'exemple précédent utiliser `x`{.language-} ou `self.x`{.language-} est équivalent. Rendre l'objet appelant est une technique très utilisées en programmation objet car elle permet ce genre de code :

```pseudocode
p1 ← Point {x: -2, y: 3}
p2 ← Point {x: 4, y: 7}
p3 ← Point {x: 12, y: 21}

affiche à l'écran p1.x et p1.y  # affiche 0 et 0
p1.addition(p2).addition(p3)
affiche à l'écran p1.x et p1.y  # affiche 14 et 31
```

La ligne `p1.addition(p2).addition(p3)`{.language-} sera exécutée de gauche à droite :

1. `p1.addition(p2)`{.language-} rendre l'objet `p1`{.language-}
2. on effectue `.addition(p3)`{.language-} sur l'objet rendu (c'est à dire `p1`{.language-})

Enfin, souvent, on n'utilise que partiellement cette convention puisque **si une variable à le même nom qu'un attribut, c'est l'attribut**. Par exemple :

```pseudocode
structure Point:
    attributs:
        x: entier ← 0
        y: entier ← 0
    méthodes:
        fonction addition(p: Point) → Point:
            x ← x + p.x
            y ← y + p.y

            rendre self
```
