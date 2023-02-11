import time
import random

from tris import insertion, sélection, bulles


def temps_générique(algorithme, tableau):
    t1 = time.perf_counter()
    algorithme(tableau)
    t2 = time.perf_counter()

    delta = t2 - t1

    return delta


def tableau_aléatoire(n):
    tableau = list(range(n))
    random.shuffle(tableau)

    return tableau

def temps_générique_moyen(algorithme, n):
    NB_ITERATION = 5

    t = 0
    for k in range(NB_ITERATION):
        tableau = tableau_aléatoire(n)
        t += temps_générique(algorithme, tableau)

    return t / NB_ITERATION


def temps_insertion(tableau):
    return temps_générique(insertion, tableau)


def temps_insertion_moyen(n):
    return temps_générique_moyen(insertion, n)

def temps_bulles_moyen(n):
    return temps_générique_moyen(bulles, n)

def temps_sélection(tableau):
    return temps_générique(sélection, tableau)
