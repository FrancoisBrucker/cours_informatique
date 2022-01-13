import time, random

from tris import insertion, selection, fusion, rapide


def temps_generique(algorithme, tableau):
    t1 = time.time()
    algorithme(tableau)
    t2 = time.time()

    delta = t2 - t1

    return delta


def temps_insertion(tableau):
    return temps_generique(insertion, tableau)


def temps_selection(tableau):
    return temps_generique(selection, tableau)


def temps_fusion(tableau):
    NB_ITERATION = 10
    t = 0
    for k in range(NB_ITERATION):
        random.shuffle(tableau)
        t += temps_generique(fusion, tableau)

    return t / NB_ITERATION


def temps_rapide(n):

    tableau = list(range(n))

    t_0 = temps_generique(rapide, tableau)

    NB_ITERATION = 10

    t = 0
    for k in range(NB_ITERATION):
        random.shuffle(tableau)
        t += temps_generique(rapide, tableau)

    return t_0, t / NB_ITERATION
