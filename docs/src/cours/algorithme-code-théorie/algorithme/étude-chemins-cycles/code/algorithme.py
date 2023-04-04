import random

from math import sqrt

def d(x, y, villes):
    return sqrt((villes[x][0] - villes[y][0]) ** 2 + (villes[x][1] - villes[y][1]) ** 2)

def kruskal(villes):
    segments = []
    for v1 in villes:
        for v2 in villes:
            segments.append([v1, v2, d(v1, v2, villes)])
    

    segments.sort(key=lambda x:x[2])
    représentants = {v: v for v in villes}

    choisis = []

    for segment in segments:
        v1 = segment[0]
        v2 = segment[1]
        if représentants[v1] != représentants[v2]:
            r = représentants[v1]
            for v in villes:
                if représentants[v] == r:
                    représentants[v] = représentants[v2]
            choisis.append((v1, v2))
    
    return choisis


def routes_rec(précédent, courant, y, segments):

    for u, v in segments:        
        if v == courant:
            u, v = v, u

        if u == courant and v == précédent:
            continue
        elif u == courant and v == y:
            return [v]
        elif u == courant:
            fin_chemin = routes_rec(u, v, y, segments)

            if fin_chemin != None:
                fin_chemin.append(v)
                return fin_chemin

    return None
            
def glouton(villes, départ):
    à_voir = set()
    for x in villes:
        à_voir.add(x)
    à_voir.remove(départ)
    
    route = [départ]

    while len(à_voir):
        y = None
        for x in à_voir:
            if y is None or d(route[-1], y, villes) > d(route[-1], x, villes):
                y = x
        route.append(y)
        à_voir.remove(y)

    return route
    

def décroisement(cycle, i, j, villes):
    if i > j:
        i, j = j, i
    if j == i + 1 or (i == 0 and j == len(villes) - 1):
        return list(cycle)
    
    cycle = cycle[i:] + cycle[:i]
    j -= i
    i = 0

    D1 = d(cycle[0], cycle[1], villes) + d(cycle[j], cycle[j + 1], villes)
    D2 = d(cycle[0], cycle[j], villes) + d(cycle[1], cycle[j + 1], villes)

    if D2 < D1 :
        cycle = [cycle[0]] + list(reversed(cycle[1:j+1])) + cycle[j+1:]
    
    return cycle

def parcours_rec(précédent, courant, segments, chemin):
    if courant not in chemin:
        chemin.append(courant)

    for u, v in segments:
        if v == courant:
            u, v = v, u

        if (u, v) == (courant, précédent):
            continue
        elif u == courant:
            parcours_rec(u, v, segments, chemin)

