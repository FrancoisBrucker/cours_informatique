import random


def copie(G):
    G_copie = dict()

    for x in G:
        G_copie[x] = set(G[x])

    return G_copie


def cycle(G):
    if not G:
        return []

    a = list(G.keys()).pop()
    return cycle_non_orienté(G, a)


def cycle_non_orienté(G, a):
    débuts_possibles = set()
    chemin = [a]

    x = a
    while not G[x].intersection(débuts_possibles):
        x = list(G[x] - set(chemin)).pop()
        chemin.append(x)

        if len(chemin) >= 3:
            débuts_possibles.add(chemin[len(chemin) - 3])

    début = list(G[x].intersection(débuts_possibles)).pop()
    i = chemin.index(début)

    return chemin[i:] + [début]


def supprime_arêtes_du_cycle(c, G):
    x = c[0]
    for y in c[1:]:
        G[x].remove(y)
        G[y].remove(x)

        x = y


def supprime_sommets_degré_zéro(G):
    sommets = list(G.keys())

    for x in sommets:
        if len(G[x]) == 0:
            del G[x]


def décale(cycle, x):
    cycle = cycle[:-1]
    i = cycle.index(x)

    return cycle[i:] + cycle[:i] + [cycle[i]]


def concatène(c1, c2, x):
    c1 = décale(c1, x)
    c2 = décale(c2, x)

    return c1 + c2[1:]


def concatène_cycles(cycles):
    while len(cycles) > 1:
        c = cycles.pop()
        for i in range(len(cycles)):
            intersection = set(c).intersection(set(cycles[i]))
            if intersection:
                x = intersection.pop()
                cycles[i] = concatène(cycles[i], c, x)
                break


G = {
    "1": {"2", "3"},
    "2": {"1", "3", "4", "5"},
    "3": {"1", "2", "4", "5"},
    "4": {"2", "3", "5", "6"},
    "5": {"2", "3", "4", "6"},
    "6": {"4", "5"},
}

G2 = copie(G)

cycles = []
while G:
    c = cycle(G)
    cycles.append(c)
    supprime_arêtes_du_cycle(c, G)
    supprime_sommets_degré_zéro(G)


print(cycles)
concatène_cycles(cycles)
cycle_eulérien = cycles[0]

print(cycle_eulérien)
