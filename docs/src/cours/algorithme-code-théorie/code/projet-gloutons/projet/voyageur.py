import csv

pays = {}
with open("gps-pays-autres.csv", newline="") as fichier_csv:
    for row in csv.reader(fichier_csv, quotechar='"', quoting=csv.QUOTE_NONNUMERIC):
        pays[row[3]] = (row[2], row[1])  # (long, lat)


from math import factorial

print(
    "Nombre de possibilités de voyages pour",
    len(pays),
    "pays :",
    factorial(len(pays) - 1) // 2,
)

import matplotlib.pyplot as plt


def draw(pays, size=20):

    x = []
    y = []
    label = []
    for (nom, (long, lat)) in pays.items():
        x.append(long)
        y.append(lat)

        label.append(nom)

    height = max(y) - min(y)
    width = max(x) - min(x)

    _, ax = plt.subplots(figsize=(size, size * height / width))

    ax.set_title("Les pays")

    ax.scatter(x, y)
    for i in range(len(x)):
        ax.text(x[i], y[i], label[i])

    plt.show()


draw(pays)

europe = {k: v for k, v in pays.items() if (-10 < v[0] < 40) and (35 <= v[1] < 70)}
draw(europe, size=13)


def d(p1, p2):
    return sum((u - v) ** 2 for u, v in zip(pays[p1], pays[p2]))


list_pays = list(pays)
dist_pays = []
for i in range(len(list_pays)):
    for j in range(i + 1, len(list_pays)):
        dist_pays.append(d(list_pays[i], list_pays[j]))

print("min : ", min(dist_pays))
print("max : ", max(dist_pays))
print("moyenne : ", sum(dist_pays) / len(dist_pays))

from random import randint


def glouton(pays):

    reste = list(pays.keys())

    i = randint(0, len(reste) - 1)
    reste[i], reste[-1] = reste[-1], reste[i]

    chemin = [reste.pop()]

    while reste:
        suivant = 0
        d_min = None
        for i in range(len(reste)):
            if d_min is None or d_min > d(chemin[-1], reste[i]):
                d_min = d(chemin[-1], reste[i])
                suivant = i
        reste[suivant], reste[-1] = reste[-1], reste[suivant]
        chemin.append(reste.pop())

    return chemin


def draw_chemin(pays, chemin, size=20):

    x = []
    y = []
    label = []
    for (nom, (long, lat)) in pays.items():
        x.append(long)
        y.append(lat)

        label.append(nom)

    height = max(y) - min(y)
    width = max(x) - min(x)

    _, ax = plt.subplots(figsize=(size, size * height / width))

    ax.set_title("Les pays")

    ax.plot(
        [pays[x][0] for x in chemin] + [pays[chemin[0]][0]],
        [pays[x][1] for x in chemin] + [pays[chemin[0]][1]],
    )
    for i in range(len(x)):
        ax.text(x[i], y[i], label[i])

    plt.show()


chemin = glouton(pays)
draw_chemin(pays, chemin)

chemin = glouton(europe)
draw_chemin(pays, chemin)


def fonction_objectif(chemin):
    return sum([d(chemin[i - 1], chemin[i]) for i in range(1, len(chemin))]) + d(
        chemin[0], chemin[-1]
    )


chemin = glouton(pays)
print(chemin)
print("distance :", fonction_objectif(chemin))

nb_amélioration = 0
for essai in range(20):
    chemin_possible = glouton(pays)

    if fonction_objectif(chemin_possible) < fonction_objectif(chemin):
        print(
            "Iteration :",
            essai + 1,
            "^",
            fonction_objectif(chemin),
            ">",
            fonction_objectif(chemin_possible),
        )
        chemin = chemin_possible
        nb_amélioration += 1
    else:
        print(
            "Iteration :",
            essai + 1,
            "v",
            fonction_objectif(chemin),
            "≤",
            fonction_objectif(chemin_possible),
        )

print("Nombre d'améliorations :", nb_amélioration)


def deux_opt(chemin, i):
    chemin_opt = [chemin[0]] + list(reversed(chemin[1 : i + 1])) + chemin[i + 1 :]

    if fonction_objectif(chemin_opt) < fonction_objectif(chemin):
        return chemin_opt
    return chemin

print("2-opt")
chemin = glouton(europe)

draw_chemin(europe, chemin)

opt = True
while opt:
    opt = False
    for deb in range(len(chemin)):
        chemin = chemin[deb:] + chemin[:deb]
        for i in range(1, len(chemin) - 1):
            chemin_2_opt = deux_opt(chemin, i)
            if fonction_objectif(chemin_2_opt) < fonction_objectif(chemin):
                chemin = chemin_2_opt        
                # opt = True

draw_chemin(europe, chemin)
