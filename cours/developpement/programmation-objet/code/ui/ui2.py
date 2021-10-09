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
