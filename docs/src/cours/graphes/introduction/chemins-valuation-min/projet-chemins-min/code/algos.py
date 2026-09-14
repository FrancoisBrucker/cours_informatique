def dijkstra(G, f, départ, arrivé, avec_nombre_sommets=False):
    prédécesseur = dict()
    coût = {départ: 0}
    V_prim = {départ}

    pivot = départ
    while pivot != arrivé:
        for x in G[pivot]:
            if x in V_prim:
                continue

            if (x not in coût) or (
                coût[x] > coût[pivot] + f(pivot, x)
            ):
                coût[x] = coût[pivot] + f(pivot, x)
                prédécesseur[x] = pivot

        new = None
        for x in G:
            if (x in V_prim) or (x not in coût):
                continue

            if (new is None) or (coût[new] > coût[x]):
                new = x

        pivot = new
        V_prim.add(pivot)

    chemin = [arrivé]
    x = arrivé
    while x != départ:
        x = prédécesseur[x]
        chemin.append(x)
    chemin.reverse()

    if avec_nombre_sommets:
        return chemin, len(V_prim)
    else: 
        return chemin


def A_étoile(G, f, h, départ, arrivé, avec_nombre_sommets=False):
    prédécesseur = dict()
    coût = {départ: 0}
    V_prim = {départ}

    pivot = départ
    while pivot != arrivé:
        for x in G[pivot]:
            if x in V_prim:
                continue

            if (x not in coût) or (
                coût[x] > coût[pivot] + f(pivot, x)
            ):
                coût[x] = coût[pivot] + f(pivot, x)
                prédécesseur[x] = pivot

        new = None
        for x in G:
            if (x in V_prim) or (x not in coût):
                continue

            if (new is None) or (coût[new] + h(new, arrivé) > coût[x] + h(x, arrivé)):
                new = x

        pivot = new
        V_prim.add(pivot)

    chemin = [arrivé]
    x = arrivé
    while x != départ:
        x = prédécesseur[x]
        chemin.append(x)
    chemin.reverse()

    if avec_nombre_sommets:
        return chemin, len(V_prim)
    else:
        return chemin
