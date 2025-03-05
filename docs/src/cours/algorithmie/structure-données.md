---
layout: layout/post.njk 
title:  "Structures de données"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

Les variables dans un algorithme ou un programme sont souvent liées. Un nombre complexe par exemple est composée d'une partie réelle et d'une partie imaginaire.

Pour qu'un algorithme puisse utiliser ces données efficacement, on les groupe dans [Une structure de données](https://fr.wikipedia.org/wiki/Structure_de_donn%C3%A9es)

{% note %}
Une **_structure de données_** est composée :

- une fonction `création`{.language-} permettant de créer un objet de cette structure
- de **_méthodes_** qui sont des fonctions permettant d’interagir avec une donnée de cette structure.
- d'**_attributs_** qui correspondent aux différentes données la constituant (de types de base ou d'autres structures de données)
{% endnote %}

Un point en dimension 2 pourra ainsi être défini comme :

```pseudocode
structure Point:
    attributs:
        x: int
        y: int
    création(abscisse: int, ordonnée: int) → Point
    méthodes:
        méthode addition(p: Point) → vide
```

### Notation pointée

On utilisera alors les attributs et les méthode avec la notation pointée, comme on le fait avec la longueur d'un tableau, c'est à dire que l'attribut ou la méthode est appliqué à l'objet à gauche du point (`objet.attribut`{.language-} ou `objet.méthode()`{.language-}). Cette méthode est classique ne programmation, par exemple en python :

{% lien %}
[Notation pointée en python](https://reeborg.ca/docs/fr/oop/oop.html)
{% endlien %}

Par exemple pour notre point, le pseudo-code suivant fonctionne :

```pseudocode
p1 ← création d'un Point d’abscisse 1 et d'ordonnée 2
p2 ← Point.création(4, 5)  #  création équivalente en explicitant la structure de donnée utilisée

affiche à l'écran p1.x et p1.y  # affiche 1 et 2
p1.addition(p2)
affiche à l'écran p1.x et p1.y  # affiche 5 et 7

d ← p1.x * p2.x + p1.y * p2.y
affiche d à l'écran  # affiche 55
```

Remarquez que :

- l'on a utilisé la création avec ue phrase ou avec la fonction de façon équivalente
- on peut accéder aux attributs d'un objet particulier
- une méthode et un attribut s'applique **toujours** à un objet (à gauche du `.`{.language-})

Pour qu'une structure de donnée puisse être utilisée, il est crucial de connaître la complexité de la création d'un objet de la structure ($\mathcal{O}(1)$ pour notre `Point`{.language-}) et de chaque méthode de celle-ci.

Enfin, lorsque l'on définie une structure, il faut bien sur donner le code de toutes les fonctions de la structure. Pour notre point, une définition complète serait :

```pseudocode
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

Remarquez que pour la gestion des attributs on a précisé à qui l'on avait affaire aux attributs :

- les attributs de l'objet appelant sont accessibles directement dans les différentes méthode
- les attributs d'un autre objet que l'objet appelant sont appelé avec la _notation pointée_
- on a coutume de rappeler les attributs dans les paramètres de la création de l'objet. On les fait précéder d'un `_`{.language-} pour montrer leurs relations.

{% note "**À retenir**" %}

- Un attribut est différent d'une variable : il est associé à l'objet appelant.
- On différencie un attribut d'une variable dans le code d'une méthode par son nom.

{% endnote %}

### mot clé `self`{.language-}

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

{% note "**À retenir**" %}

- n'utilisez pas de nom d'attribut comme variable d'une méthode
- si le paramètre d'une méthode à le même nom qu'un attribut : c'est qu'il est directement affecté à celui-ci avec `self`{.language-}. On utilise essentiellement ça dans la fonction `création`{.language-}

{% endnote %}

### Complexités

Une fois une structure de données définie, on pourra l'utiliser comme un type de base dans tous nos algorithmes. La taille d'une structure est déterminée par rapport à la taille de ses attributs :

{% note "**À retenir**" %}
On considérera toujours que la taille en mémoire d'une structure est proportionnelle à la taille des objets qui la compose et est connue à sa création.
{% endnote %}
