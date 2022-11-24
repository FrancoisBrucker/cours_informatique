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
