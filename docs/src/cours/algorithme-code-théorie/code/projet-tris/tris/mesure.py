import time, random

from tris import insertion, sélection, fusion, rapide


def temps_générique(algorithme, tableau):
    t1 = time.time()
    algorithme(tableau)
    t2 = time.time()

    delta = t2 - t1

    return delta

def temps_générique_moyen(algorithme, tableau):
    NB_ITERATION = 10

    copie = list(tableau)
    t = 0
    for k in range(NB_ITERATION):
        random.shuffle(copie)
        t += temps_générique(algorithme, copie)

    return t / NB_ITERATION


def temps_insertion(tableau):
    return temps_générique(insertion, tableau)

def temps_insertion_moyen(tableau):
    return temps_générique_moyen(insertion, tableau)

def temps_selection(tableau):
    return temps_générique(sélection, tableau)


