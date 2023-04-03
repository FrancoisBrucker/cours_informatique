import matplotlib.pyplot as plt

def draw(pays, size=8):

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