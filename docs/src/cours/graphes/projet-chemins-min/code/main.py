import json
import math


# Chargement des données

with open("../villes_10000_habitants.json") as entree:
    villes = json.load(entree)


print("Marseille", ":")
for clé, valeur in villes["Marseille"].items():
    print(clé, valeur)


def f(v1, v2):
    x1, y1 = villes[v1]["longitude"], villes[v1]["latitude"]
    x2, y2 = villes[v2]["longitude"], villes[v2]["latitude"]

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


G = {clé: set(valeur["voisins"]) for clé, valeur in villes.items()}

print(G["Marseille"])
print(f("Marseille", "Montauban"))
print(f("Marseille", "Paris"))
print(f("Marseille", "Lille"))

# Dessin

def plot(chemin=None):
    import matplotlib.pyplot as plt
    import matplotlib.lines as mlines


    fig, ax = plt.subplots(figsize=(10, 10))

    ax.plot(
        [villes[x]["longitude"] for x in G],
        [villes[x]["latitude"] for x in G],
        "o",
        color="black",
    )

    for x in G:
        ax.text(villes[x]["longitude"], villes[x]["latitude"], x)
        for y in G[x]:
            if y > x:  # évite de tracer 2 fois la même arête
                continue

            ax.add_line(
                mlines.Line2D(
                    (villes[x]["longitude"], villes[y]["longitude"]),
                    (villes[x]["latitude"], villes[y]["latitude"]),
                )
            )

    for i in range(1, len(chemin)):
            x = chemin[i-1]
            y = chemin[i]
            ax.add_line(
                mlines.Line2D(
                    (villes[x]["longitude"], villes[y]["longitude"]),
                    (villes[x]["latitude"], villes[y]["latitude"]),
                    color="red"
                )
            )

    plt.show()

# plot()

# Dijkstra


from algos import dijkstra, A_étoile

# chemin = dijkstra(G, f, "Marseille", "Lille")
chemin, n = dijkstra(G, f, "Marseille", "Brest", True)

print(chemin, n)
chemin, n = A_étoile(G, f, f, "Marseille", "Brest", True)
print(chemin, n)


# d = 0
# for i in range(1, len(chemin)):
#     d += f(chemin[i-1], chemin[i])

# print(d)

# plot(chemin)