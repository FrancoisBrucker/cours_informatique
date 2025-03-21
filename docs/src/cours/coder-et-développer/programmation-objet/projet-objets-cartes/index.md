---
layout: layout/post.njk 
title: "Projet : objets cartes"

eleventyComputed:
  eleventyNavigation:
    key: "{{ page.url }}"
    title: "{{ title | safe }}"
    parent: "{{ '../' | siteUrl(page.url) }}"
---

<!-- début résumé -->

Encore un projet d'initiation dans le codage des objets. On s'intéresse ici aux méthodes spéciales qui permettent d'utiliser les objets comme des nombres.

<!-- end résumé -->

Vous allez coder une classe `Carte`{.language-}, ce qui permettra par la suite de jouer à la bataille. La classe carte en elle-même ne fera pas grand chose, mais elle illustrera la notion de [value object](https://en.wikipedia.org/wiki/Value_object) :

{% note "**Définition**" %}
Un ***value object*** est un objet ne pouvant pas être modifié une fois créé : il ne possède aucune méthode lui permettant de changer ses attributs qu'il faut renseigner à sa création.
{% endnote %}

Ce projet va vous faire utiliser des méthodes d'améliorations d'objets comme :

- l'utilisation de [la fonction spéciale d'affichage `__str__`{.language-}](../améliorer-ses-objets/#représentation){.interne}
- l'utilisation de [fonctions spéciale de comparaisons](../améliorer-ses-objets/#comparaison){.interne}

Remémorez vous ces parties avant de commencer le projet.

## Projet

### Vscode

{% faire %}
Créez un dossier `projet-cartes`{.fichier} sur votre ordinateur et ouvrez leu avec visual studio code pour un faire votre projet.
{% endfaire %}

### Programme principal & User stories

Le but du projet est de pouvoir jouer à une variante de [la bataille](https://fr.wikipedia.org/wiki/Bataille_(jeu)) :

{% note "**But**" %}

On veut pouvoir mélanger un jeu de 32 cartes (sans joker) puis le séparer en 2 *pioches* de 16 cartes, un tas par joueur.

A chaque tour les deux joueurs prennent la première carte de leur pioche et la révèle. Le joueur ayant la plus grande carte (7 < 8 < 9 < 10 < V < D < R < 1 et si égalité de rang alors : ♠ > ♥ > ♦ > ♣︎) prend les deux cartes et les place dans sa pile de défausse (initialement vide).

Lorsqu'un joueur doit prendre une carte alors que sa pioche est vide, il mélange les cartes de sa défausse qui forment une nouvelle pioche. Si la pioche et la défausse sont vides, le joueur perd la partie.

{% endnote %}

### Carte UML

La pioche et la défausse pouvant être facilement modélisées par des listes, il nous reste à créer une classe Carte pour avoir tous les éléments de base de notre projet.

{% exercice %}
Proposez une modélisation UML d'une classe Carte pour notre projet
{% endexercice %}
{% details "solution" %}

Un constructeur, un formatage en chaîne de caractères pour affichage à l'écran et des opérateurs de comparaison :

![carte UML](./carte_uml.png)
{% enddetails %}

### User stories

Le projet nécessite de faire plein de choses. Pour vous aider à réaliser ce but, on va se placer des objectifs intermédiaires, sous la forme de user stories.

Je vous en propose une ci-après qui exhibe la capacité à créer un jeu de 32 cartes et à afficher les cartes à l'écran :

{% note "**User Story**" %}

- Nom : "Voyance"
- Utilisateur : un voyant extralucide.
- Story : On veut pouvoir tirer les cartes
- Actions :
  1. créer un paquet de 32 cartes (sans joker)
  2. prendre au hasard 3 cartes du paquet
  3. afficher à l'écran les trois cartes, dans l'ordre où elles ont été tirées

{% endnote %}

Par rapport au jeu, il manque essentiellement la fonctionnalité permettant d'ordonner les cartes :

{% exercice %}
Créez une user story qui exhibe la fonctionnalité de pouvoir ordonner les cartes.

En affichant 10 cartes tirées avec remise dans l'ordre où elles ont été tirées, puis dans l'ordre croisant.

{% endexercice %}
{% details "corrigé" %}

- Nom : "Ordonnancement"
- Utilisateur : un adepte de réussite
- Story : On veut pouvoir ranger les cartes par ordre croissant
- Actions :
  1. choisir 10 cartes au hasard (on peut avoir les mêmes cartes)
  2. afficher à l'écran les 10 cartes, dans l'ordre où elles ont été tirées
  3. afficher à l'écran les 10 cartes, dans l'ordre croissant

{% enddetails %}

Créons les fichiers pour nos users stories, même si le code n'est pas encore clair. Par exemple pour la user story *"voyance"*, on crée un fichier `story_voyance.py`{.fichier} contenant :

```text
# création d'un paquet de 32 cartes
# prendre au hasard 3 cartes du paquet
# afficher à l'écran les trois cartes, dans l'ordre où elles ont été tirées
```

On ajoutera petit à petit le code permettant d'implémenter la story, au fur et à mesure de l'avancement du projet.

{% faire %}
Créez les deux fichiers de story.
{% endfaire %}

## Code

{% faire %}
Créez les fichiers qui nous permettront de coder la carte :

- `carte.py`{.fichier}
- `test_carte.py`{.fichier}

{% endfaire %}

### Constructeur

Le constructeur d'une carte nécessite 2 paramètres : la valeur et la couleur.

{% exercice %}
En  considérant que les deux paramètres couleur et valeur sont des chaînes de caractères,
quelles sont les possibilités admissibles pour construire une carte ?
{% endexercice %}
{% details "corrigé" %}

Par exemple, pour les valeurs :

- `"sept"`{.language-}
- `"huit"`{.language-}
- `"neuf"`{.language-}
- `"dix"`{.language-}
- `"valet"`{.language-}
- `"dame"`{.language-}
- `"roi"`{.language-}
- `"as"`{.language-}

Pour les couleurs :

- `"pique"`{.language-}
- `"cœur"`{.language-}
- `"carreau"`{.language-}
- `"trèfle"`{.language-}

{% enddetails %}

{% faire %}
Implémentez le constructeur de la classe `Carte`{.fichier} et ses tests en supposant que l'utilisateur entre les bonnes valeurs de paramètres.

{% endfaire %}

### Affichage à l'écran

Pour permettre un affichage à l'écran plus convivial :

{% faire %}
Codez la méthode `__str__`{.language-} d'une carte. Le code suivant doit pouvoir fonctionner :

```python
>>> from carte import Carte
>>> ace_pique = Carte("as", "pique")
>>> print(ace_pique)
as de pique
```

Faites un test de cette méthode en testant la représentation sous la forme d'une chaîne de caractères d'une `Carte`{.language-}.
{% endfaire %}
{% info %}

La représentation sous la forme d'une chaîne de caractères un objet `x` est le résultat de `str(x)`{.language-}.

{% endinfo %}

Lorsque l'on écrit `print(ace_pique)`{.language-}, python transforme l'objet en chaîne de caractères avec la commande `str`{.language-} qui elle-même cherche la méthode `__str__`{.language-}. Les trois instructions suivantes sont donc équivalentes :

1. `print(ace_pique)`{.language-}
2. `print(str(ace_pique))`{.language-}
3. `print(ace_pique.__str__())`{.language-}

### Représentation de l'objet

Vous verrez parfois une autre méthode de représentation d'un objet utilisant la commande `repr()`{.language-}. Cette fonction doit permettre de reconstruire l'objet si nécessaire.

Par exemple :

```python
>>> from carte import Carte
>>> ace_pique = Carte("as", "pique")
>>> print(repr(ace_pique))
Carte('as', 'pique')
```

On utilise souvent `repr()`{.language-} pour du débogage (donc de l'affichage développeur), alors que `str()`{.language-} est utilisé pour de l'affichage utilisateur.

{% note %}

- on utilise `str(objet)` (créée avec la méthode `__str__`{.language-}) pour un affichage à l'écran. On transforme l'objet en un texte.
- on utilise `repr(objet)` (créée avec la méthode `__repr__`{.language-}) pour représenter l'objet sous la forme d'une chaîne de caractères. On doit pouvoir reconstruire un objet identique avec la commande [`eval`{.language-}](https://docs.python.org/fr/3/library/functions.html#eval) (`eval(repr(objet))`{.language-} doit rendre un objet similaire à `objet`{.language-}.

{% endnote %}

{% lien %}
Un petit tuto français pour expliciter les différences entre les deux représentations : <https://www.youtube.com/watch?v=ejGYAnf_X24>
{% endlien %}

{% exercice %}
Créez et testez la méthode `__repr__`{.language-}
{% endexercice %}
{% details "corrigé" %}

```python
class Carte:
    # ...

    def __repr__(self):
        return "Carte(" + repr(self.valeur) + ", " + repr(self.couleur) + ")"
    
    # ...

```

{% enddetails %}

### Constantes de classes

Avant de pouvoir finir la partie de création d'une carte, il nous reste un problème à résoudre. Comment indiquer à l'utilisateur les possibilités de valeur et de couleurs ?

La solution communément utilisée pour cela est de créer des constantes :

{% faire %}
Créez les constantes :

- `SEPT`{.language-}, `HUIT`{.language-}, `NEUF`{.language-}, `DIX`{.language-}, `VALET`{.language-}, `DAME`{.language-}, `ROI`{.language-}, `AS`{.language-}
- `PIQUE`{.language-}, `COEUR`{.language-}, `CARREAU`{.language-}, `TREFLE`{.language-}

En leur associant les chaînes de caractères adéquates.
{% endfaire %}

Il ne faudra qu'utiliser ces constantes pour créer les cartes et ne plus directement utiliser des chaînes de caractères comme `"sept"`{.language-} qui sont des [MAGIC NUMBERS](../projet-objets-dés/#mantra-no-magic-numbers){.interne}.

Par exemple, on écrira `Carte(AS, TREFLE)`{.language-} plutôt que `Carte("as", "trèfle)`{.language-}

{% faire %}
Utilisez dans le code et les tests les constantes à la place des chaînes de caractères.
{% endfaire %}
{% info %}
Vous n'êtes pas obligé d'importer toutes les constantes, une à une. En utilisant juste `import carte`{.language-}, vous pourrez utiliser `carte.PIQUE`{.language-} (constante `PIQUE`{.language-} dans l'espace de nom de `carte`{.language-}) directement par exemple.
{% endinfo %}

Enfin, pour grouper ces constantes, vous pourrez :

{% faire %}

Créer deux autres constantes, qui rassemblent les couleurs et les valeurs entre elles :

- `VALEURS = [SEPT, HUIT, NEUF, DIX, VALET, DAME, ROI, AS]`{.language-}
- `COULEURS = [TREFLE, CARREAU, COEUR, PIQUE]`{.language-}

{% endfaire %}
{% info %}
Remarquez que l'on a rangé les différentes valeurs par ordre croissant de valeur et de couleur.

{% endinfo %}

## User story voyance

Vous avez tous les outils nécessaires pour créer la user story *"voyance"* :

{% faire %}
Codez la user story *"voyance"*.
{% endfaire %}
{% info %}
Vous pourrez utiliser la fonction [`random.sample`{.language-}](https://docs.python.org/fr/3/library/random.html#random.sample) pour tirer des cartes sans remise d'un paquet.
{% endinfo %}

## Comparaisons

{% faire %}
Codez et testez les [opérateurs de comparaisons](../classes-et-objets/#comparaison){.interne} :

- `==`{.language-} qui correspond a à la méthode `__eq__`{.language-}
- `!=`{.language-} qui correspond a à la méthode `__ne__`{.language-}
- `<`{.language-} qui correspond a à la méthode `__lt__`{.language-}
- `>`{.language-} qui correspond a à la méthode `__gt__`{.language-}
- `<=`{.language-} qui correspond a à la méthode `__le__`{.language-}
- `>=`{.language-} qui correspond a à la méthode `__ge__`{.language-}

{% endfaire %}
{% info %}
N'hésitez pas à utiliser des opérateurs déjà codé. Vous pouvez par exemple utiliser les fonctions `==`{.language-} et `<`{.language-} pour coder les autres les comparaisons.
{% endinfo %}

Ceci devrait être suffisant pour la deuxième user story :

{% faire %}
Codez la seconde user story.
{% endfaire %}
{% info %}
Vous pourrez utiliser la fonction [`random.choices`{.language-}](https://docs.python.org/fr/3/library/random.html#random.choices) pour tirer des cartes avec remise d'un paquet.
{% endinfo %}

## Jeu

Vous pouvez maintenant finir le projet en codant le jeu !

La règle du jeu est :

1. mélangez un jeu de 32 cartes en deux **pioches** de 16 cartes, une pour chaque joueur
2. chaque joueur dispose également d'une **défausse**, initialement vide
3. N = 1
4. chaque joueur dévoile la carte du dessus de leur pioche
5. le joueur ayant la carte la plus élevée remporte la carte de l'adversaire et pose les deux cartes (la sienne et celle de son adversaire) dans sa défausse
6. si un joueur n'a plus de cartes dans sa pioche, il mélange les cartes de sa défausse pour en faire un nouvelle pioche
7. si un joueur n'a plus de carte dans sa pioche, il perd la partie
8. N = N + 1
9. si N est inférieur ou au nombre maximum de tour, retour en 4, sinon le jeu s'arrête.

{% faire %}
Codez le jeu dans un fichier `main.py`{.fichier}
{% endfaire %}
