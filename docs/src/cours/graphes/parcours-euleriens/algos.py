import random


def cycle(G):
    if not G:
        return []

    a = random.choice(list(G.keys()))
    examinés = set()
    chemin = [a]

    x = a
    while (x != a) or (len(chemin) == 1):
        suivants = G[x] - examinés
        if suivants:
            y = random.choice(list(suivants))
            if y == a and (len(chemin) < 3):
                suivants.remove(y)
                if suivants:
                    y = random.choice(list(suivants))
                    examinés.add(y)
                    chemin.append(y)
                else:
                    chemin.pop()
            else:
                examinés.add(y)
                chemin.append(y)
        else:
            chemin.pop()

        if chemin:
            x = chemin[-1]
        else:
            break

    return chemin


def copie(G):
    G_copie = dict()

    for x in G:
        G_copie[x] = set(G[x])

    return G_copie


def supprime(G, c):
    x = c[0]
    for y in c[1:]:
        G[x].remove(y)
        if not G[x]:
            del G[x]

        G[y].remove(x)
        if not G[y]:
            del G[y]

        x = y


def décale(cycle, x):
    cycle = cycle[:-1]
    i = cycle.index(x)

    return cycle[i:] + cycle[:i] + [cycle[i]]


def concatène(c1, c2, x):
    c1 = décale(c1, x)
    c2 = décale(c2, x)

    return c1 + c2[1:]


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
c = cycle(G2)

while c:
    supprime(G2, c)
    cycles.append(c)

    c = cycle(G2)

print(cycles)

while len(cycles) > 1:
    c = cycles.pop()
    for i in range(len(cycles)):
        intersection = set(c).intersection(set(cycles[i]))
        if intersection:
            x = intersection.pop()
            cycles[i] = concatène(cycles[i], c, x)
            break

cycle_eulérien = cycles[0]
print(cycle_eulérien)
