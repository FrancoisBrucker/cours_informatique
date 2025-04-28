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

## Attributs

Par défaut une structure de donnée va posséder des **_attributs_** qui regroupent les objets de la structure. Pour notre point en 2D on aurait la structure :

```pseudocode
structure Point:
    attributs:
        x: entier
        y: entier
```

Par rapport au tuple, les attributs sont des variables et possèdent ainsi des noms. On peut accéder à ces noms par la notation pointée.

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

Pour créer des nouveau objet d'une structure, on utilise une fonction spéciale appelée `création` qui rend un objet de la structure. Pour notre point cela donnerait :

```pseudocode/
structure Point:
    attributs:
        x: entier
        y: entier
    création(_x: entier, _y: entier) → Point:
        x ← _x
        y ← _y
```

Remarquez que `création`{.language-} rend _implicitement_ un Point. Son but est d'initialiser les attributs à des valeurs. Les attributs de l'objet créés sont directement accessibles (lignes 6 et 7).

Enfin, comme les attributs sont déjà crées, les paramètres de la fonction création ne peuvent êtres nommées comme eux. Mais si ces paramètres snt directement affectés à la valeur de l'attribut on a coutume de place un `_`{.language-} (_underscore_) avant sont nom pour à la fois les différentier et monter leurs relations.

On utilise cette méthode implicitement la fonction création dans le pseudocode suivant :

```pseudocode
p ← un nouveau Point de paramètres 3 et 4
```

Ou explicitement :

```pseudocode
p ← Point.création(3, 4)
```

{% info %}
Il n'est pas nécessaire que les paramètres de `création`{.language-} soient exactement les attributs. La structure suivante est tout à fait possible :

```pseudocode/
structure Point:
    attributs:
        x: entier
        y: entier
    création() → Point:
        x ← 0
        y ← 0
```

{% endinfo %}

### Méthodes

L'intérêt fondamental des structures de données est les méthodes qui permettent d'opérer sur les objets de la structure. Transformons la fonction `additionne_point`{.language-} précédente en méthode :

```pseudocode/
structure Point:
    attributs:
        x: entier
        y: entier
    création(_x: entier, _y: entier) → Point:
        x ← _x
        y ← _y
    méthodes:
        méthode addition(p: Point) → vide:
            x ← x + p.x
            y ← y + p.y

```

On appelle les méthodes avec la notation pointée :

```pseudocode
p1 ← création d'un Point avec les paramètres 1 et 2
p2 ← Point.création(4, 5)  #  création équivalente en explicitant la structure de donnée utilisée

affiche à l'écran p1.x et p1.y  # affiche 1 et 2
p1.addition(p2)
affiche à l'écran p1.x et p1.y  # affiche 5 et 7
```

Dans le code de l'addition, la notation pointée assure que les variables `x`{.language-} et `y`{.language-} des lignes 10 et 11 d la définition sont celle de l'objet à gauche de l'appel, ici `p1` dns le programme précédent.

### Résumé

{% attention "**À retenir**" %}
Une **_structure de données_** est composée :

- une fonction `création`{.language-} permettant de créer un objet de cette structure
- de **_méthodes_** qui sont des fonctions permettant d’interagir avec une donnée de cette structure.
- d'**_attributs_** qui correspondent aux différentes données la constituant (de types de base ou d'autres structures de données)

On accède au attributs et aux méthodes d'une structure avec la notation pointée.
{% endattention %}

Une fois une structure de données définie, on pourra l'utiliser comme un type de base dans tous nos algorithmes. La taille d'une structure est déterminée par rapport à la taille de ses attributs :

{% attention "**À retenir**" %}
On considérera toujours que la taille en mémoire d'une structure est proportionnelle à la taille des objets qui la compose et est connue à sa création.
{% endattention %}

Pour qu'une structure de donnée puisse être utilisée, il est crucial de connaître la complexité de la création d'un objet de la structure ($\mathcal{O}(1)$ pour notre `Point`{.language-}) et de chaque méthode de celle-ci.

## mot clé `self`{.language-}

L'objet courant, celui qui appelle (à gauche du `.` en notation pointée), peut être parfois nommé par le mot-clé `self`{.language-}. Cela permet d'utiliser la notation pointée partout (et est indispensable si l'on veut connaître l'objet appelant, comme pour la structure de liste chaînée que l'on verra plus tard). En utilisant complètement cette convention, le pseudocode de la structure devient :

```pseudocode
structure Point:
    attributs:
        x: entier
        y: entier
    création(x: entier, y: entier) → Point:
        self.x ← x
        self.y ← y
    méthodes:
        méthode addition(p: Point) → vide:
            self.x ← self.x + p.x
            self.y ← self.y + p.y
```

{% info %}
Certains langages comme python n'autorisent que cette notation ce qui rend le code sans ambiguïté, d'autres comme le java autorise les deux versions (avec ou sans `self`{.language-}).
{% endinfo %}

La plupart du temps, on fera un mix des deux approches pour rendre le pseudocode plus digeste. Par exemple pour `Point`, on pourra utiliser `self`{.language-} pour le constructeur et ainsi se passer des `_`{.language-} et s'en passer pour la méthode `addition`{.language-} qui est claire sans lui :

```pseudocode
structure Point:
    attributs:
        x: entier
        y: entier
    création(x: entier, y: entier) → Point:
        self.x ← x
        self.y ← y
    méthodes:
        méthode addition(p: Point) → vide:
            x ← x + p.x
            y ← y + p.y
```

Il faut garder le pseudo-code lisible donc :

{% attention "**À retenir**" %}

- n'utilisez pas de nom d'attribut comme variable d'une méthode
- si le paramètre d'une méthode à le même nom qu'un attribut : c'est qu'il est directement affecté à celui-ci avec `self`{.language-}. On utilise essentiellement ça dans la fonction `création`{.language-}

{% endattention %}
