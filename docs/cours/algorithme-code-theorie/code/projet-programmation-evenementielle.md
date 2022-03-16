---
layout: page
title:  "étude / programmation événementielle"
category: cours
tags: informatique cours 
author: "François Brucker"
---

> [Algorithme, code et théorie]({% link cours/algorithme-code-theorie/index.md %}) / [algorithmie]({% link cours/algorithme-code-theorie/algorithme/index.md %}) / [projet : programmation événementielle]({% link cours/algorithme-code-theorie/code/projet-programmation-evenementielle.md %})
>
> prérequis :
>
>* [projet : héritage]({% link cours/algorithme-code-theorie/code/programmation-objet/projet-heritage.md %})
>
{: .chemin}

## mise en place

Nous utiliserons la bibliothèque [pyglet](http://pyglet.org/) pour ce projet. Commencez par l'installer :

```shell
python -m pip install pyglet
```

> installation pyglet
{: .tbd}

### structures

> 1. créez un dossier nommé *"arkanoid"* où vous placerez vos fichiers
> 2. créez un projet vcode dans ce dossier
>
{: .a-faire}

### vérifications

>
> * on vérifie que python est ok avec le terminal et avec vscode
> * on vérifie que le linter est actif dans vscode
>* on vérifie que les tests fonctionnent (en créant un test bidon dans *"tests_tris"* et en vérifiant que `pytest` et vscode le trouvent)
>
{: .a-faire}

## programmation événementielle

La [programmation événementielle](https://fr.wikipedia.org/wiki/Programmation_%C3%A9v%C3%A9nementielle) est un paradigme de programmation très utiliser dans les interfaces graphiques. Cette méthode consiste à réagir à des événements issus du programme comme de cliquer sur un bouton, appuyer sur une touche, etc.

Le principe est le suivant :

1. on inscrit une fonction $f$ à un type d'événement $e$
2. lorsque l'événement $e$ arrive, la fonction $f(e)$  est exécutée

Dans ce projet, les événements que nous aurons à manipuler seront les appuies sur les touches du clavier, le dessin de notre interface, la taille des fenêtres, etc, etc.

Cette méthode de programmation est basée sur le patron de conception [observateur](https://refactoring.guru/fr/design-patterns/observer).

## introduction à pyglet

[pyglet](http://pyglet.org/) est une bibliothèque permettant de créer des interfaces. Nous ne rentrerons pas dans tous les détails de son implémentation (utilisation d'[opengl](https://fr.wikipedia.org/wiki/OpenGL), la gesion du son, etc) mais nous utiliserons assez de ses fonctionnalits pour que vous puissiez aller plus loin de votre côté.

La [documentation de pyglet](https://pyglet.readthedocs.io/en/latest/) est très bien faite et fourmille d'[exemples](https://github.com/pyglet/pyglet/tree/master/examples).

Nous allons placer les différents essais de pyglet dans un sous-dossier de notre projet. Créer un dossier *"essais-pyglet"* dans votre projet *"arkanoid"*.

### hello world

Il y a plusieurs moyen me mettre en place une fenêtre pyglet. Nous allons utiliser la méthode la plus proche de la programmation objet (voir [subclassing window](https://pyglet.readthedocs.io/en/latest/programming_guide/windowing.html#subclassing-window)).

#### une fenêtre

Fichier : *"arkanoid/essais-pyglet/fenetre.py"* :

```python
import pyglet


class HelloWorldWindow(pyglet.window.Window):
    def __init__(self):
        super(HelloWorldWindow, self).__init__(400, 200, "texte")

        self.label = pyglet.text.Label("Hello, world!")

    def on_draw(self):
        self.clear()
        self.label.draw()


window = HelloWorldWindow()
print(window.get_size())

pyglet.app.run()
print("c'est fini !")

```

> Exécutez le programme précédent.
{: .a-faire}

Vous devriez voir apparaitre une fenêtre avec écrit "Hello, world!" en blanc sur fond noir en bas à gauche de la fenêtre. Vous devriez aussi voir dans le terminal le texte : `(400, 200)` qui est la taille de la fenêtre.
En revanche, le texte `c'est fini !` ne devrait apparaître dans le terminal que lorsque la fenêtre se ferme.

> Comprenez :
>
> * comment fonctionne le programme
> * l'héritage de la classe `Window` de pyglet
> * la fonction de la ligne `pyglet.app.run()`
>
{: .a-faire}

#### une fenêtre redimensionnable

La méthode `on_draw` est une méthode spéciale. A chaque fois que l'événement `draw` est activé, cette méthode est exécutée. POur le voir concrètement, modifiez le code précédent avec :

```python
import pyglet


class HelloWorldWindow(pyglet.window.Window):
    def __init__(self):
        super(HelloWorldWindow, self).__init__(400, 200, "texte", resizable=True)

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

> Comprenez :
>
> * l'ajout d'un paramètre lors de l'appel au construction de `Window` qui rend la fenêtre redimensionnable
> * l'ajout d'un `print` dans la méthode `on_draw`
> * lorsque l'on change la taille de la fenêtre, la méthode `on_draw` est exécutée
>
{: .a-faire}

#### texte au milieu de la fenêtre

Un [label](https://pyglet.readthedocs.io/en/latest/modules/text/index.html#pyglet.text.Label) est un objet non modifiable qui peut-être affiché (dans la méthode `on_draw`.)

Remplacez sa création dans le fichier *"arkanoid/essais-pyglet/fenetre.py"* par :

```python
        self.label = pyglet.text.Label(
            "Hello, world!",
            x=self.width // 2,
            y=self.height // 2,
            anchor_x="center",
            anchor_y="center",
        )

```

En exécutant le code, le texte est placé au milieu de l'écran ! En revanche, lorsque vous modifiez la taille de la fenêtre, la position ne change pas.

>
> * déduire l'origine de la fenêtre en utilisant le redimensionnement de la fenêtre.
> * utiliser l'événement `on_resize(width, height)`  pour recréer un nouveau label à la bonne position après chaque redimensionnement (attention, `on_resize` est utilisée par `Window`, n'oubliez pas de l'appeler avec un `super`)
>
{: .a-faire}
{% details  solution %}
l'origine est en bas à gauche de la fenêtre.

```python
class HelloWorldWindow(pyglet.window.Window):
    #...

    def on_resize(self, width, height):
        super().on_resize(width, height)

        self.label = pyglet.text.Label(
            "Hello, world!",
            x=width // 2,
            y=height // 2,
            anchor_x="center",
            anchor_y="center",
        )

    # ...

```

{% enddetails %}

### gestion du clavier

La [gestion du clavier sous pyglet](https://pyglet.readthedocs.io/en/latest/programming_guide/keyboard.html) se fait avec deux événements :

* `on_key_press(symbol, modifiers)` qui s'active lorsque qu'une touche est appuyée
* `on_key_release(symbol, modifiers)` qui s'active lorsque qu'une touche est relâchée

L'attribut `symbol` est un entier qui correspond au code de la touche et `modifiers` gère les touches comme *shift*, *control* ou encore *alt*.

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

Nous n'avons pas utilisé `super` pour appeler la méthode de la classe mère, car `Window` ne gère pas le clavier par défaut.

> Exécutez le code et remarquez :
>
> * que chaque touche a bien un code, ainsi que les touche de modfication
> * shift gauche et shift droit sont indiscernables
> * qu'après chaque touche appuyée ou relâchée l'évènement `on_draw` est lancé
>
{: .a-faire}

#### flèches gauche et droite

Les code des différentes touches est disponible dans l'objet [pyglet.window.key](https://pyglet.readthedocs.io/en/latest/modules/window_key.html#module-pyglet.window.key).

> En utilisant le fait que les deux attributs `x` et `y` contiennent la position du label : déplacez le texte en utilisant les touches de déplacement du clavier.
{: .a-faire}
{% details solution %}

```python
class HelloWorldWindow(pyglet.window.Window):
    # ...
    
    def on_key_press(self, symbol, modifiers):
        delta = 10
        update = False
        if symbol == key.UP:
            x = self.label.x
            y = self.label.y + delta
            update = True
        elif symbol == key.DOWN:
            x = self.label.x
            y = self.label.y - delta
            update = True
        elif symbol == key.LEFT:
            x = self.label.x - delta
            y = self.label.y
            update = True
        elif symbol == key.RIGHT:
            x = self.label.x + delta
            y = self.label.y
            update = True

        if update:
            self.label = pyglet.text.Label(
                "Hello, world!",
                x=x,
                y=y,
                anchor_x="center",
                anchor_y="center",
            )
    # ...

```

> On ne se déplace qu'une fois pas appui sur la touche. Pour gérer les déplacement continu, il faut prendre en compte le temps. C'est le boulot de la partie suivante.

{% enddetails %}

### gestion du temps

[La gestion du temps](https://pyglet.readthedocs.io/en/latest/programming_guide/time.html) se fait également par un événement. Sa mise en place est cependant différentes des événements que l'on a vu jusqu'à présent :

```python
class HelloWorldWindow(pyglet.window.Window):
    # ...

    def __init__(self):
        super(HelloWorldWindow, self).__init__(400, 200, "texte", resizable=True)

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

Le code suivant va faire en sorte que la méthode `update` soit exécutée toute les secondes. Le paramètre `dt` donne le nombre de secondes exactes depuis le dernier appel de la fonction. Cela permet de gérer le lag s'il existe.

>
> Faites en sorte que le texte avance de 10 pixels toutes les .5s si une touche est appuyée.
>
{: .a-faire}
{% details solution %}

```python
# ...

class HelloWorldWindow(pyglet.window.Window):
    def __init__(self):
        super(HelloWorldWindow, self).__init__(400, 200, "texte", resizable=True)

        self.label = pyglet.text.Label(
            "Hello, world!",
            x=self.width // 2,
            y=self.height // 2,
            anchor_x="center",
            anchor_y="center",
        )
        self.dx = 0
        self.dy = 0

        pyglet.clock.schedule_interval(self.update, 0.5)

    def update(self, dt):
        if self.dx != 0 or self.dy != 0:
            self.label = pyglet.text.Label(
                "Hello, world!",
                x=self.label.x + self.dx,
                y=self.label.y + self.dy,
                anchor_x="center",
                anchor_y="center",
            )

    def on_resize(self, width, height):
        super().on_resize(width, height)

        self.label = pyglet.text.Label(
            "Hello, world!",
            x=width // 2,
            y=height // 2,
            anchor_x="center",
            anchor_y="center",
        )

    def on_key_press(self, symbol, modifiers):
        delta = 10
        if symbol == key.UP:
            self.dy = delta
        elif symbol == key.DOWN:
            self.dy = -delta
        elif symbol == key.LEFT:
            self.dx = -delta
        elif symbol == key.RIGHT:
            self.dx = +delta

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.dy = 0
        elif symbol == key.DOWN:
            self.dy = 0
        elif symbol == key.LEFT:
            self.dx = 0
        elif symbol == key.RIGHT:
            self.dx = 0

    def on_draw(self):
        print("draw:", self.get_size())
        self.clear()
        self.label.draw()

# ...
```

On a utilisé deux attributs `dx` et `dy` qui définisse si on doit bouger ou non. la méthode update met à jour la position du texte.

{% enddetails %}

>
> Ajoutez à votre code une sentinelle qui empêche les coordonnées `x` et `y` du label de sortie hors de la fenêtre. 
>
> Les dimensions de la fenêtres sont données par les attributs `width` et `height`.
>
{: .a-faire}
{% details solution %}

```python

class HelloWorldWindow(pyglet.window.Window):
    # ...

    def update(self, dt):
        if self.dx != 0 or self.dy != 0:
            self.label = pyglet.text.Label(
                "Hello, world!",
                x=max(min(self.label.x + self.dx, self.width), 0),
                y=max(min(self.label.y + self.dy, self.height), 0),
                anchor_x="center",
                anchor_y="center",
            )
    
    # ...
```

{% enddetails %}

### gestion de la souris

> début des collisions
{: .tbd}

## arkanoid

<http://tisofts.free.fr/pages/arkanoid/Arkanoid.htm>
<https://www.youtube.com/watch?v=l1E15FOYmKc>

> faire un todo
> y aller petit à petit
> fixer des objectif de code en 1/2h : classe/tests/programme principal
> faire une classe ses tests et implémenter le tout.
{: .tbd}
