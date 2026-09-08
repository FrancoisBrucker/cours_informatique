import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

TAILLE = 15

def draw(pays):
    x = []
    y = []
    label = []
    for nom, (long, lat) in pays.items():
        x.append(long)
        y.append(lat)

        label.append(nom)

    height = max(y) - min(y)
    width = max(x) - min(x)

    fig, ax = plt.subplots(figsize=(TAILLE, TAILLE * height / width))
    ax.set_title("Les villes")

    ax.scatter(x, y)
    for i in range(len(x)):
        ax.text(x[i], y[i], label[i])

    plt.show()

def draw_segments(ax, villes, segments, couleur=mcolors.CSS4_COLORS["brown"]):
    for x, y in segments:
        ax.plot(
            [villes[x][0], villes[y][0]],
            [villes[x][1], villes[y][1]],
            color=couleur,
        )
