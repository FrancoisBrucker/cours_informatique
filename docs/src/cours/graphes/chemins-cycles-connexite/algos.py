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


def cycle_non_orienté(G, a):
    examinés = set()
    chemin = [a]

    x = a
    while (x != a) or (len(chemin) == 1):
        suivants = G[x] - examinés
        if suivants:
            y = suivants.pop()
            if y == a and (len(chemin) < 3):
                if suivants:
                    y = suivants.pop()
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

G = {
    "a": {"b", "c"},
    "b": {"a", "c"},
    "c": {"a", "b"},
    "d": set()
}

print(G)
for x in G:
    print(composante_connexe(G, x))

print("------")

print(chemin(G, "a", "b"))
print(chemin(G, "a", "d"))
print(chemin(G, "a", "a"))

print("=======")

print(cycle_non_orienté(G, "a"))
print(cycle_non_orienté(G, "d"))
print(cycle_non_orienté(G, "b"))

print("------")
