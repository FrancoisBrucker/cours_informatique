---
layout: page
title:  "Programmation évènementielle"
category: cours
authors: 
  - François Brucker
  - Célia Châtel
---

On utilise la programmation évènementielle pour créer des interfaces graphiques.

## bibliothèque utilisée

### premières modifications

#### couleur du label

```python
from appJar import gui

model = {"valeur": 0}


def press_plus1():
    model["valeur"] += 1
    if model["valeur"] > 0:
        app.setLabelFg("valeur", "blue")
    elif model["valeur"] == 0:
        app.setLabelFg("valeur", "black")

    app.setLabel("valeur", str(model["valeur"]))


def press_moins1():
    model["valeur"] -= 1
    if model["valeur"] < 0:
        app.setLabelFg("valeur", "red")
    elif model["valeur"] == 0:
        app.setLabelFg("valeur", "black")

    app.setLabel("valeur", str(model["valeur"]))

app = gui()
app.setSize(300, 100)

app.addButton("-1", press_moins1, 0, 0)
app.addLabel("valeur", str(model["valeur"]), 0, 1)
app.addButton("+1", press_plus1, 0, 2)

app.go()
print("c'est fini.")

```

#### reset

```python
from appJar import gui

model = {"valeur": 0}


def press_plus1():
    model["valeur"] += 1
    if model["valeur"] > 0:
        app.setLabelFg("valeur", "blue")
    elif model["valeur"] == 0:
        app.setLabelFg("valeur", "black")

    app.setLabel("valeur", str(model["valeur"]))


def press_moins1():
    model["valeur"] -= 1
    if model["valeur"] < 0:
        app.setLabelFg("valeur", "red")
    elif model["valeur"] == 0:
        app.setLabelFg("valeur", "black")

    app.setLabel("valeur", str(model["valeur"]))


def press_zero():
    model["valeur"] = 0
    app.setLabelFg("valeur", "black")
    app.setLabel("valeur", str(model["valeur"]))


app = gui()
app.setSize(300, 100)

app.addButton("-1", press_moins1, 0, 0)
app.addLabel("valeur", str(model["valeur"]), 0, 1)
app.addButton("+1", press_plus1, 0, 2)

app.addButton("à zéro", press_zero, 1, 1)

app.go()
print("c'est fini.")
```

## lancer de dés

### l'interface

```python
from appJar import gui
from dice import Dice

model = {"dice": Dice()}


def press_roll():
    model["dice"].roll()
    app.setLabel("valeur", str(model["dice"].get_position()))


app = gui()
app.setSize(300, 100)
app.setTitle("lancé de dé")

app.addLabel("valeur", str(model["dice"].get_position()), 0, 0)

app.addButton("lancer", press_roll, 1, 0)

app.go()
print("c'est fini.")

```

### changer le dé

```python
from appJar import gui
from dice import Dice

model = {"dice": Dice()}

des_valeurs = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]

def press_roll():
    model["dice"].roll()
    app.setLabel("valeur", des_valeurs[model["dice"].get_position() - 1])


app = gui()
app.setSize(300, 200)
app.setTitle("lancé de dé")

app.addLabel("valeur", des_valeurs[model["dice"].get_position() - 1], 0, 0)
app.getLabelWidget("valeur").config(font="Time 100")
app.addButton("lancer", press_roll, 1, 0)

app.go()
print("c'est fini.")
```

### Lancer 3 dés

```python
from appJar import gui
from dice import Dice

model = {"dice": [Dice(), Dice(), Dice()]}

des_valeurs = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]


def press_roll():
    for i in range(3):
        model["dice"][i].roll()
        app.setLabel("valeur" + str(i), des_valeurs[model["dice"][i].get_position() - 1])


app = gui()
app.setSize(300, 200)
app.setTitle("lancé de dé")

for i in range(3):
    app.addLabel("valeur" + str(i), des_valeurs[model["dice"][i].get_position() - 1], 0, i)
    app.getLabelWidget("valeur" + str(i)).config(font="Time 100")
app.addButton("lancer", press_roll, 1, 1)

app.go()
print("c'est fini.")
```

### somme

```python
from appJar import gui
from dice import Dice

model = {
    "dice": [Dice(), Dice(), Dice()],
    "somme": 3
}

des_valeurs = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]


def press_roll():
    for i in range(3):
        model["dice"][i].roll()
        app.setLabel("valeur" + str(i), des_valeurs[model["dice"][i].get_position() - 1])

    model["somme"] = model["dice"][0].get_position() + model["dice"][1].get_position() + model["dice"][2].get_position()
    app.setLabel("somme", str(model["somme"]))


app = gui()
app.setSize(400, 200)
app.setTitle("lancé de dé")

app.startFrame("left", row=0, column=0)
for i in range(3):
    app.addLabel("valeur" + str(i), des_valeurs[model["dice"][i].get_position() - 1], 0, i)
    app.getLabelWidget("valeur" + str(i)).config(font="Time 100")
app.addButton("lancer", press_roll, 1, 1)
app.stopFrame()

app.startFrame("right", row=0, column=1)
app.addLabel("somme",str(model["somme"]), 0, 0)
app.getLabelWidget("somme").config(font="Time 140")
app.stopFrame()

app.go()
print("c'est fini.")

```

### Lancer des dés choisis

```python
from appJar import gui
from dice import Dice

model = {
    "dice": [Dice(), Dice(), Dice()],
    "somme": 3
}

des_valeurs = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]


def press_roll():
    for i in range(3):
        if app.getCheckBox("check" + str(i)):
            model["dice"][i].roll()
        app.setLabel("valeur" + str(i), des_valeurs[model["dice"][i].get_position() - 1])

    model["somme"] = model["dice"][0].get_position() + model["dice"][1].get_position() + model["dice"][2].get_position()
    app.setLabel("somme", str(model["somme"]))


app = gui()
app.setSize(400, 200)
app.setTitle("lancé de dé")

app.startFrame("left", row=0, column=0)
for i in range(3):
    app.addLabel("valeur" + str(i), des_valeurs[model["dice"][i].get_position() - 1], 0, i)
    app.getLabelWidget("valeur" + str(i)).config(font="Time 100")
    app.addNamedCheckBox("", "check" + str(i), 1, i)
app.addButton("lancer", press_roll, 2, 1)
app.stopFrame()

app.startFrame("right", row=0, column=1)
app.addLabel("somme",str(model["somme"]), 0, 0)
app.getLabelWidget("somme").config(font="Time 140")
app.stopFrame()

app.go()
print("c'est fini.")
```
