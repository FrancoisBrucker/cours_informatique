def composante_connexe(G, origine):
    composante = {origine}
    suivant = [origine]

    while suivant:
        x = suivant.pop()

        for y in G[x]:
            if y not in composante:
                composante.add(y)
                suivant.append(y)

    return composante


def les_composantes(G):
    composantes = []

    dans_une_composante = set()

    for x in G:
        if x in dans_une_composante:
            continue

        composantes.append(composante_connexe(G, x))
        dans_une_composante.update(composantes[-1])

    return composantes


def chemin(G, a, b):
    examinés = {a}
    chemin = [a]

    x = a
    while x != b:
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


def circuit(G, a):
    chemin = [a]

    x = a
    while not G[x].intersection(chemin):
        x = set(G[x]).pop()
        chemin.append(x)

    début = (G[x].intersection(chemin)).pop()
    i = chemin.index(début)

    return chemin[i:] + [début]

def cycle_non_orienté(G, a):
    chemin = [a]

    x = a
    while not G[x].intersection(chemin[:-2]):
        x = (G[x] - set(chemin[-2:])).pop()
        chemin.append(x)

    début = (G[x].intersection(chemin[:-2])).pop()
    i = chemin.index(début)

    return chemin[i:] + [début]


G = {"a": {"b", "c"}, "b": {"a", "c"}, "c": {"a", "b"}, "d": set()}

G2 = {"a": {"b"}, "b": {"c"}, "c": {"a"}, "d": set()}

print(G)
for x in G:
    print(composante_connexe(G, x))

print("------")

print(chemin(G, "a", "b"))
print(chemin(G, "a", "d"))
print(chemin(G, "a", "a"))

print("=======")

print(cycle_non_orienté(G, "a"))
print(cycle_non_orienté(G, "b"))

print("------")

print(circuit(G2, "a"))
print(circuit(G2, "b"))

print("------")
