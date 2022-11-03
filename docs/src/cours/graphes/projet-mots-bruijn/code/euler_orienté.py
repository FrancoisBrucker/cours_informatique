import random


def circuit(G, a):
    examinés = set()
    chemin = [a]

    x = a
    while (x != a) or (len(chemin) == 1):
        suivants = G[x] - examinés
        if suivants:
            y = suivants.pop()
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

        # différence par rapport au court : le graphe est orienté on ne supprime pas l'arc opposée
        x = y


def décale(circuit, x):
    circuit = circuit[:-1]
    i = circuit.index(x)

    return circuit[i:] + circuit[:i] + [circuit[i]]


def concatène(c1, c2, x):
    c1 = décale(c1, x)
    c2 = décale(c2, x)

    return c1 + c2[1:]


def euler(G):
    G2 = copie(G)

    circuits = []
    c = circuit(G2, random.choice(list(G2.keys())))

    while c:
        supprime(G2, c)
        circuits.append(c)

        if not G2:
            c = []
            break
        else:
            c = circuit(G2, random.choice(list(G2.keys())))

    while len(circuits) > 1:
        c = circuits.pop()
        for i in range(len(circuits)):
            intersection = set(c).intersection(set(circuits[i]))
            if intersection:
                x = intersection.pop()
                circuits[i] = concatène(circuits[i], c, x)
                break

    return circuits[0]
