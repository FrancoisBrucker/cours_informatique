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
