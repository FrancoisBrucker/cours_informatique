def dijkstra(G, f, départ, arrivé, n=False):
    prédécesseur = dict()
    coût_entrée = {départ: 0}
    sommets_examinées = {départ}

    pivot = départ
    while pivot != arrivé:
        for x in G[pivot]:
            if x in sommets_examinées:
                continue

            if (x not in coût_entrée) or (
                coût_entrée[x] > coût_entrée[pivot] + f(pivot, x)
            ):
                coût_entrée[x] = coût_entrée[pivot] + f(pivot, x)
                prédécesseur[x] = pivot

        new = None
        for x in G:
            if (x in sommets_examinées) or (x not in coût_entrée):
                continue

            if (new is None) or (coût_entrée[new] > coût_entrée[x]):
                new = x

        pivot = new
        sommets_examinées.add(pivot)

    chemin = [arrivé]
    x = arrivé
    while x != départ:
        x = prédécesseur[x]
        chemin.append(x)
    chemin.reverse()

    if n:
        return chemin, len(sommets_examinées)
    else: 
        return chemin


def A_étoile(G, f, h, départ, arrivé, n=False):
    prédécesseur = dict()
    coût_entrée = {départ: 0}
    sommets_examinées = {départ}

    pivot = départ
    while pivot != arrivé:
        for x in G[pivot]:
            if x in sommets_examinées:
                continue

            if (x not in coût_entrée) or (
                coût_entrée[x] > coût_entrée[pivot] + f(pivot, x)
            ):
                coût_entrée[x] = coût_entrée[pivot] + f(pivot, x)
                prédécesseur[x] = pivot

        new = None
        for x in G:
            if (x in sommets_examinées) or (x not in coût_entrée):
                continue

            if (new is None) or (coût_entrée[new] + h(new, arrivé) > coût_entrée[x] + h(x, arrivé)):
                new = x

        pivot = new
        sommets_examinées.add(pivot)

    chemin = [arrivé]
    x = arrivé
    while x != départ:
        x = prédécesseur[x]
        chemin.append(x)
    chemin.reverse()

    if n:
        return chemin, len(sommets_examinées)
    else:
        return chemin
