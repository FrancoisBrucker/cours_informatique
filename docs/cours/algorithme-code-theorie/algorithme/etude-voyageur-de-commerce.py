import random

import matplotlib.pyplot as plt


def aleatoire(n):
    villes = []
    for i in range(n):
        villes.append((random.random(), random.random()))

    return villes


def cree_reseau(villes):

    representant = dict()
    for ville in villes:
        representant[ville] = ville

    arêtes = []
    for i in range(len(villes)):
        for j in range(i + 1, len(villes)):
            arêtes.append((villes[i], villes[j]))

    def d(arete):
        v1, v2 = arete
        return (v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2

    arêtes.sort(key=d)

    reseau = []
    for arete in arêtes:
        x, y = arete
        if representant[x] != representant[y]:
            c = representant[x]
            for v in villes:
                if representant[v] == c:
                    representant[v] = representant[y]
            reseau.append(arete)

    return reseau


def dessine_villes(ax, villes):
    ax.plot([x[0] for x in villes], [x[1] for x in villes], "ro")


def dessine_reseau(ax, reseau):
    for arete in reseau:
        ax.plot([x[0] for x in arete], [x[1] for x in arete], color="blue")
    plt.show()


villes = aleatoire(10)
reseau = cree_reseau(villes)

fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

dessine_villes(ax, villes)
dessine_reseau(ax, reseau)
plt.show()
