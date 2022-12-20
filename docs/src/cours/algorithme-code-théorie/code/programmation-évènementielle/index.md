---
layout: layout/post.njk 
title: "Programmation évènementielle"

eleventyNavigation:
  key: "Programmation évènementielle"
  parent: Code
---

{% prerequis "**Prérequis** :" %}

* [Programmation objet](../programmation-objet)

{% endprerequis %}

<!-- début résumé -->

Coder des programmes grâce à la programmation évènementielle en utilisant pyglet.

<!-- end résumé -->

Nous utiliserons la bibliothèque [pyglet](http://pyglet.org/) pour ce projet. Commencez par l'installer :

```
python -m pip install pyglet
```

{% faire %}

1. créez un dossier nommé `essais-pyglet`{.fichier} où vous placerez vos fichiers
2. créez un projet vscode dans ce dossier

{% endfaire %}

La [programmation événementielle](https://fr.wikipedia.org/wiki/Programmation_%C3%A9v%C3%A9nementielle) est un paradigme de programmation très utiliser dans les interfaces graphiques. Cette méthode consiste à réagir à des événements issus du programme comme de cliquer sur un bouton, appuyer sur une touche, etc.

Le principe est le suivant :

1. on inscrit une fonction $f$ à un type d'événement $e$
2. lorsque l'événement $e$ arrive, la fonction $f(e)$  est exécutée

Dans ce projet, les événements que nous aurons à manipuler seront les appuies sur les touches du clavier, le dessin de notre interface, la taille des fenêtres, etc, etc.

Cette méthode de programmation est basée sur le patron de conception [observateur](https://refactoring.guru/fr/design-patterns/observer).

Nous allons utiliser [pyglet](http://pyglet.org/) qui est une bibliothèque permettant de créer des interfaces pour illustrer cela. Nous ne rentrerons pas dans tous les détails de son implémentation (utilisation d'[opengl](https://fr.wikipedia.org/wiki/OpenGL), la gestion du son, etc) mais nous utiliserons assez de ses fonctionnalités pour que vous puissiez aller plus loin de votre côté.

La [documentation de pyglet](https://pyglet.readthedocs.io/en/latest/) est très bien faite et fourmille d'[exemples](https://github.com/pyglet/pyglet/tree/master/examples).

Nous allons placer les différents essais de pyglet dans un sous-dossier de notre projet. Créer un dossier `essais-pyglet`{.fichier}.

## Hello world

{% lien %}
Méthode [subclassing window](https://pyglet.readthedocs.io/en/latest/programming_guide/windowing.html#subclassing-window)
{% endlien %}

Il y a plusieurs moyen me mettre en place une fenêtre pyglet. Nous allons utiliser la méthode la plus proche de la programmation objet qui consiste à faire de l'héritage.

### une fenêtre

Fichier : `essais-pyglet/fenetre.py`{.fichier} :

```python
import pyglet


class HelloWorldWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(400, 200, "texte")

        self.label = pyglet.text.Label("Hello, world!")

    def on_draw(self):
        self.clear()
        self.label.draw()


window = HelloWorldWindow()
print(window.get_size())

pyglet.app.run()
print("c'est fini !")

```

{% faire %}
Exécutez le programme précédent.
{% endfaire %}

Vous devriez voir apparaître une fenêtre avec écrit "Hello, world!" en blanc sur fond noir en bas à gauche de la fenêtre. Vous devriez aussi voir dans le terminal le texte : `(400, 200)`{.language-} qui est la taille de la fenêtre.
En revanche, le texte `c'est fini !`{.language-} ne devrait apparaître dans le terminal que lorsque la fenêtre se ferme.

{% faire "**Comprenez :**" %}

* comment fonctionne le programme
* l'héritage de la classe `Window`{.language-} de pyglet
* la fonction de la ligne `pyglet.app.run()`{.language-}

{% endfaire %}

La méthode `on_draw`{.language-} sert à dessiner la fenêtre et est exécutée beaucoup de fois par seconde. Son code stipule que pour dessiner la fenêtre :

1. on efface son contenu
2. on dessine le label

### Une fenêtre redimensionnable

La méthode `on_draw`{.language-} est une méthode spéciale. A chaque fois que l'événement `draw`{.language-} est activé, cette méthode est exécutée. Pour le voir concrètement, modifiez le code précédent avec :

```python
import pyglet


class HelloWorldWindow(pyglet.window.Window):
    def __init__(self):
        super().__init__(400, 200, "texte", resizable=True)

        self.label = pyglet.text.Label("Hello, world!")

    def on_draw(self):
        print("draw:", self.get_size())
        self.clear()
        self.label.draw()


window = HelloWorldWindow()
print(window.get_size())

pyglet.app.run()
print("c'est fini !")

```

{% faire "**Comprenez :**" %}

* l'ajout d'un paramètre lors de l'appel au construction de `Window`{.language-} qui rend la fenêtre redimensionnable
* l'ajout d'un `print`{.language-} dans la méthode `on_draw`{.language-}
* lorsque l'on change la taille de la fenêtre, la méthode `on_draw`{.language-} est exécutée

{% endfaire %}

La méthode `on_draw`{.language-} est exécutée à chaque fois que la fenêtre est dessinée, c'est à dire beaucoup de fois par seconde. Le `print`{.language-} dans cette fonction va vite devenir pénible. Supprimez le :

```python
# ...

    def on_draw(self):
        self.clear()
        self.label.draw()

# ...
```

{% faire %}
Modifiez le code de la méthode `on_draw`{.language-} pour qu'il soit identique au code ci-dessus.
{% endfaire %}

### Texte au milieu de la fenêtre

{% lien %}
[Labels](https://pyglet.readthedocs.io/en/latest/modules/text/index.html#pyglet.text.Label)
{% endlien %}

Un label est un objet non modifiable qui peut-être affiché (dans la méthode `on_draw`{.language-}).

Remplacez sa création dans le fichier `essais-pyglet/fenetre.py`{.fichier} par :

```python
# ...

self.label = pyglet.text.Label(
    "Hello, world!",
    x=self.width // 2,
    y=self.height // 2,
    anchor_x="center",
    anchor_y="center",
)

# ...
```

En exécutant le code, le texte est placé au milieu de l'écran ! En revanche, lorsque vous modifiez la taille de la fenêtre pendant l'exécution du programme, la position ne change pas.

{% exercice %}

* déduire l'origine de la fenêtre en utilisant le redimensionnement de la fenêtre.
* utiliser l’événement `on_resize(width, height)`{.language-} pour replacer le label à la bonne position après chaque redimensionnement en modifiant ses attributs `x`{.language-} et `y`{.language-}.

{% endexercice %}
{% attention %}
La méthode `on_resize`{.language-} est utilisée par `Window`{.language-}, n’oubliez pas de l’appeler avec un `super`{.language-}.
{% endattention %}

{% details  "solution" %}
l'origine est en bas à gauche de la fenêtre.

```python
class HelloWorldWindow(pyglet.window.Window):
    #...

    def on_resize(self, width, height):
        super().on_resize(width, height)
        self.label.x = width // 2
        self.label.y = height // 2

    # ...
```

{% enddetails %}

## Gestion du clavier

{% lien %}
[Gestion du clavier sous pyglet](https://pyglet.readthedocs.io/en/latest/programming_guide/keyboard.html)
{% endlien %}

On utilise deux événements pour gérer le clavier :

* `on_key_press(symbol, modifiers)`{.language-} qui s'active lorsque qu'une touche est appuyée
* `on_key_release(symbol, modifiers)`{.language-} qui s'active lorsque qu'une touche est relâchée

Le paramètre `symbol`{.language-} est un entier qui correspond au code de la touche et `modifiers`{.language-} gère les touches comme `shift`, `control` ou encore `alt`.

Ajoutons une gestion basique du clavier dans le programme :

```python
class HelloWorldWindow(pyglet.window.Window):
    #...

    def on_key_press(self, symbol, modifiers):
        print("press:", symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        print("release:", symbol, modifiers)

    # ...
```

Nous n'avons pas utilisé de `super`{.language-} pour appeler la méthode de la classe mère, car `Window`{.language-} ne gère pas le clavier par défaut.

{% faire "**Exécutez le code précédent et remarquez :**" %}

* que chaque touche a bien un code, ainsi que les touche de modification
* shift gauche et shift droit sont discernables
* qu'après chaque touche appuyée ou relâchée l'évènement `on_draw`{.language-} est lancé
* que même si on laisse appuyé la touche longtemps, il n'y a qu'un seul événement `on_key_press`{.language-} qui est lancé.

{% endfaire %}

### Flèches gauche et droite

{% lien %}
Les code des différentes touches est disponible dans l'objet [pyglet.window.key](https://pyglet.readthedocs.io/en/latest/modules/window_key.html#module-pyglet.window.key).
{% endlien %}

Chaque touche est une constante dont le nom correspond à la la touche et sa valeur au code. Par exemple, la constante `pyglet.window.key.SPACE`{.language-} correspond au nombre 32.

{% faire %}
Vérifiez que lorsque vous appuyez sur la touche espace de votre clavier, c'est bien le symbole 32 qui et affiché
{% endfaire %}

Nous allons maintenant faire bouger d'un cran notre texte lorsque l'on appuie sur les touches "flèche gauche" et "flèche droite".

{% exercice %}
En utilisant le fait que les deux attributs `x`{.language-} et `y`{.language-} contiennent la position du label : faite en sorte que lorsque l'on appuie sur une flèche du clavier (le nom des constantes de  `pyglet.window.key`{.language-} correspondant aux flèches sont disponible [là](https://pyglet.readthedocs.io/en/latest/modules/window_key.html#cursor-control-and-motion)), le texte se déplace de 10 pixels vers la direction de la flèche.
{% endexercice %}
{% details "solution" %}

```python
# ...

from pyglet.window import key

# ...

class HelloWorldWindow(pyglet.window.Window):
    # ...
    
    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.label.y += 10
        elif symbol == key.DOWN:
            self.label.y -= 10
        elif symbol == key.LEFT:
            self.label.x -= 10
        elif symbol == key.RIGHT:
            self.label.x += 10

    # ...
```

{% enddetails %}

Avec cette technique, on ne peut se déplacer que d'un cran par appui sur la touche. Pour gérer les déplacements continus, il faut prendre en compte le temps d'appui sur la touche. C'est le boulot de la partie suivante.

## Gestion du temps

{% lien %}
[Gestion du temps](https://pyglet.readthedocs.io/en/latest/programming_guide/time.html)
{% endlien %}

[La gestion du temps](https://pyglet.readthedocs.io/en/latest/programming_guide/time.html) se fait également par un événement. Sa mise en place est cependant différente des événements que l'on a vu jusqu'à présent :

```python
class HelloWorldWindow(pyglet.window.Window):
    # ...

    def __init__(self):
        super().__init__(400, 200, "texte", resizable=True)

        self.label = pyglet.text.Label(
            "Hello, world!",
            x=self.width // 2,
            y=self.height // 2,
            anchor_x="center",
            anchor_y="center",
        )

        pyglet.clock.schedule_interval(self.update, 1)

    def update(self, dt):
        print(dt)


    # ...
```

Le code précédent fait en sorte que la méthode `update`{.language-} soit exécutée toute les secondes. Le paramètre `dt`{.language-} donne le nombre de secondes exactes depuis le dernier appel de la fonction. Cela permet de gérer le lag s'il existe (remarquez qu'il vaut toujours un peut plus que 1).

{% exercice %}
Faites en sorte que le texte avance de 10 pixels toutes les 0.5s si une touche est appuyée.

Pour cela on ne va pas modifier la position du label dans `on_key_press`{.language-} mais dans update :

* créez deux attributs `dx`{.language-} et `dy`{.language-} à notre objet `HelloWorldWindow`{.language-}. Par défaut ces deux attributs vaudront 0
* à chaque appelle de `update`{.language-}, bougez la position du label de `self.dx`{.language-} et `self.dy`{.language-}
* gérez les valeurs de `self.dx`{.language-} et `self.dy`{.language-} dans `on_key_press`{.language-} et `on_key_release`{.language-} (par exemple `self.dx = -10`{.language-} lorsque l'on appuie sur la flèche gauche et `self.dx = 0`{.language-} lorsque la flèche gauche est relâchée)

{% endexercice %}
{% details "solution" %}

```python
# ...

class HelloWorldWindow(pyglet.window.Window):
    def __init__(self):
        # ...

        self.dx = 0
        self.dy = 0

        # ...

    def update(self, dt):
        self.label.x += self.dx
        self.label.y += self.dy

    # ...

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.dy = 10
        elif symbol == key.DOWN:
            self.dy = -10
        elif symbol == key.LEFT:
            self.dx = -10
        elif symbol == key.RIGHT:
            self.dx = +10

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.dy = 0
        elif symbol == key.DOWN:
            self.dy = 0
        elif symbol == key.LEFT:
            self.dx = 0
        elif symbol == key.RIGHT:
            self.dx = 0
    
    # ...

# ...
```

{% enddetails %}

Avec cette méthode le texte va continuer de se déplacer tant qu'une flèche reste appuyée. On peut même taper plusieurs flèches en même temps pour se déplacer en diagonale (cool, non ?).

Il reste un problème : le texte va sortir de la fenêtre si on reste appuyé trop longtemps. Corrigez ça :

{% exercice %}
Ajoutez à votre code une sentinelle qui empêche les coordonnées `x`{.language-} et `y`{.language-} du label de sortir hors de la fenêtre.

Les dimensions de la fenêtres sont données par ses attributs `width`{.language-} et `height`{.language-}.

{% endexercice %}
{% details "solution" %}

```python

class HelloWorldWindow(pyglet.window.Window):
    # ...

    def update(self, dt):
        self.label.x += self.dx
        if self.label.x < 0:
            self.label.x = 0
        elif self.label.x > self.width:
            self.label.x = self.width

        self.label.y += self.dy
        if self.label.y < 0:
            self.label.y = 0
        elif self.label.y > self.height:
            self.label.y = self.height
    
    # ...
```

{% enddetails %}

## Gestion de la souris

{% lien %}
[Gestion de la souris](https://pyglet.readthedocs.io/en/latest/programming_guide/mouse.html)
{% endlien %}

[Pour gérer la souris](https://pyglet.readthedocs.io/en/latest/programming_guide/mouse.html), comme vous pouvez vous en douter, il s'agit de s'abonner à des événements. Il en existe plusieurs. Commençons par voir ce que ça donne avec les événements `on_mouse_press(x, y, button, modifiers)`{.language-} et `on_mouse_release(x, y, button, modifiers)`{.language-} :

```python

class HelloWorldWindow(pyglet.window.Window):
    # ...

    def on_mouse_press(self, x, y, button, modifiers):
        print("press:", x, y, button)

        if (abs(self.label.x - x) <= self.label.content_width / 2) and (
            abs(self.label.y - y) <= self.label.content_height / 2
        ):
            print("clique dans le label")

    def on_mouse_release(self, x, y, button, modifiers):
        print("release:", x, y, button)

        if (abs(self.label.x - x) <= self.label.content_width / 2) and (
            abs(self.label.y - y) <= self.label.content_height / 2
        ):
            print("relâcher le bouton dans le label")
    
    # ...
```

Lorsque vous cliquez sur un bouton de la souris puis que vous le relâchez, vous devriez voir affiché à l'écran la position du curseur ainsi que le numéro du bouton de la souris qui a servi à cliquer.

Cerise sur le gâteau, lorsque vous cliquez ou relâchez le bouton de la souris sur le label, cela devrait vous l'indiquer.

{% exercice %}

En utilisant l'événement `on_mouse_motion(self, x, y, dx, dy)`{.language-} repérez quand la souris rentre et sort du label. N'hésitez pas à regarder [la documentation de l'événement](https://pyglet.readthedocs.io/en/latest/modules/window.html#pyglet.window.Window.on_mouse_motion) pour comprendre la définition de chaque paramètre.

{% endexercice %}
{% details "solution" %}

```python

class HelloWorldWindow(pyglet.window.Window):
    # ...

    def on_mouse_motion(self, x, y, dx, dy):
        if (abs(self.label.x - x) <= self.label.content_width / 2) and (
            abs(self.label.y - y) <= self.label.content_height / 2
        ):
            if (abs(self.label.x - (x - dx)) > self.label.content_width / 2) or (
                abs(self.label.y - (y - dy)) > self.label.content_height / 2
            ):
                print("entre dans label")
        else:
            if (abs(self.label.x - (x - dx)) <= self.label.content_width / 2) and (
                abs(self.label.y - (y - dy)) <= self.label.content_height / 2
            ):
                print("sort du label")
    
    # ...
```

{% enddetails %}

## Dessiner des formes

{% lien %}
[Les formes](https://pyglet.readthedocs.io/en/latest/programming_guide/shapes.html)

{% endlien %}

La documentation permet de voir que l'on peut facilement dessiner des cercle ou des rectangles en pyglet.

De façon générale, la gestion des graphique en `pyglet` se fait directement en opengl, ce qui dépasse de loin le cadre de ce cours (même si c'est chouette de parler directement à la carte graphique). Nous allons donc uniquement nous restreindre au dessin d'un cercle et d'un rectangle ce qui sera suffisant pour notre projet.

Fichier : `essais-pyglet/forme.py`{.fichier} :

```python
import pyglet
from pyglet import shapes
from pyglet.window import mouse


class Formes(pyglet.window.Window):
    def __init__(self):
        super().__init__(640, 480, "formes")

        self.rectangle = shapes.Rectangle(200, 200, 200, 200, color=(55, 55, 255))
        self.circle = shapes.Circle(0, 0, 50, color=(255, 0, 0))
        self.circle.opacity = 128

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if buttons & mouse.LEFT and (
            (self.circle.x - x) ** 2 + (self.circle.y - y) ** 2
            <= self.circle.radius ** 2
        ):
            self.circle.x += dx
            self.circle.y += dy

    def on_draw(self):
        self.clear()

        self.rectangle.draw()
        self.circle.draw()


forme = Formes()

pyglet.app.run()
print("c'est fini !")
```

{% faire %}
Testez l'exemple ci-dessus et comprenez ce qu'il fait.
{% endfaire %}

Les couleurs sont décrites au [format RGB](https://fr.wikipedia.org/wiki/Rouge_vert_bleu) sous la forme de 3 entiers allant de 0 à 255 en base 10 :

* le premier décrit la composante rouge
* le second la composante verte
* le dernier la composante bleue

On a souvent coutume (dans le monde du web par exemple) de représenter ces 3 nombres par un nombre hexadécimal de 6 chiffres (2 par composante, chaque composante étant codée par un nombre allant de 00 à FF). Par exemple, le nombre `#F58318`{.language-} correspond à la couleur ayant F5 en rouge, 83 en vert et 18 en bleu, les 3 nombres étant en codage hexadécimal. Ce qui en python donne avec un tuple de 3 coordonnées : `(0xF5, 0x83, 0x18)`{.language-}, ou `(245, 131, 24)`{.language-} en base 10 (un nombre écrit en hexadécimal en python commence par `0x`).

{% info %}
Pour gérer et trouver des couleurs sympathiques, utilisez une roue des couleurs, comme [celle d'adobe](https://color.adobe.com/fr/create/color-wheel) par exemple.
{% endinfo %}
