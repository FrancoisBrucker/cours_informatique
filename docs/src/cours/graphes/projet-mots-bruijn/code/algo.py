from euler_orienté import euler


def mots(alphabet, p):
    compteur = [0] * p

    mots = [[alphabet[0]] * p]
    while compteur != [len(alphabet) - 1] * p:
        compteur = next(compteur, len(alphabet))
        mots.append([alphabet[x] for x in compteur])

    return mots


def next(mot, q):
    if mot[-1] != q - 1:
        return mot[:-1] + [mot[-1] + 1]

    else:
        i = len(mot) - 1

        while i > -1 and mot[i] == q - 1:
            i -= 1

        if i == -1:
            return mot
        else:
            return mot[:i] + [mot[i] + 1] + [0] * (len(mot) - i - 1)


for mot in mots(list(range(2)), 4):
    print(mot)


def graphe_Bruijn(n, p):
    G = {tuple(mot): set() for mot in mots(list(range(n)), p - 1)}

    for mot in G:
        for x in range(n):
            G[mot].add(mot[1:] + (x,))
    return G


gb = graphe_Bruijn(2, 3)
for x, nx in gb.items():
    print(x, nx)


cycle = euler(gb)
print(cycle)

mot_bruijn = list(cycle[0])
for i in range(1, len(cycle)):
    mot_bruijn.append(cycle[i][-1])

print(mot_bruijn)
