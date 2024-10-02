def marquage(G, c, s, p, f):

    marques = {s: (s, None)}
    examiné = set()

    while (p not in marques) and (set(marques.keys()) - examiné):
        x = (set(marques.keys()) - examiné).pop()

        for y in G[x]:
            if y in marques:
                continue

            if c[(x, y)] > f[(x, y)]:
                if (marques[x][1] is None) or (
                    abs(marques[x][1]) > c[(x, y)] - f[(x, y)]
                ):
                    marques[y] = (x, c[(x, y)] - f[(x, y)])
                else:
                    marques[y] = (x, abs(marques[x][1]))

        for y in G:
            if (y in marques) or (x not in G[y]):
                continue

            if f[(y, x)] > 0:
                if (marques[x][1] is None) or (abs(marques[x][1]) > f[(y, x)]):
                    marques[y] = (x, -f[(y, x)])
                else:
                    marques[y] = (x, -abs(marques[x][1]))

        examiné.add(x)

    return marques


def chaîne_augmentante(s, p, marques):
    C = [p]
    x = p
    while x != s:
        y = marques[x][0]
        x = y
        C.append(x)

    C.reverse()

    return C


def augmentation_flot(s, p, marques, chaîne, f):
    alpha = abs(marques[p][1])

    for i in range(1, len(chaîne)):
        if marques[chaîne[i]][1] > 0:
            f[(chaîne[i - 1], chaîne[i])] += alpha
        else:
            f[(chaîne[i], chaîne[i - 1])] -= alpha


def ford_et_fulkerson(G, c, s, p, f):
    marques = marquage(G, c, s, p, f)

    while p in marques:
        chaîne = chaîne_augmentante(s, p, marques)
        augmentation_flot(s, p, marques, chaîne, f)
        marques = marquage(G, c, s, p, f)


def graphe_écart(G, c, f):
    Gf = {x: set() for x in G}

    for xy in c:
        x, y = xy
        if c[xy] > f[xy]:
            Gf[x].add(y)
        if f[xy] > 0:
            Gf[y].add(x)

    return Gf


def graphe_écart_valuation(G, c, f, v):
    Gf = {x: set() for x in G}
    vf = dict()

    for xy in c:
        x, y = xy
        if c[xy] > f[xy]:
            Gf[x].add(y)

            if (x, y) not in vf:
                vf[(x, y)] = v[(x, y)]
            else:
                vf[(x, y)] = min(v[(x, y)], v[(y, x)])

        if f[xy] > 0:
            Gf[y].add(x)

            if (y, x) not in vf:
                vf[(y, x)] = v[(x, y)]
            else:
                vf[(y, x)] = min(v[(x, y)], v[(y, x)])

    return Gf, vf
