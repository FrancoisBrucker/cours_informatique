import random

from mesure_temps import calcul

def recherche(T, x):
    for e in T:
        if e == x:
            return True
    return False


def calcule_max(n):
    T = list(range(n))
    return calcul(recherche, (T, -1), rep=5)


def calcule_min(n):
    T = list(range(n))
    return calcul(recherche, (T, 0))


def calcule_moyenne(n, rep=10):
    T = list(range(n))
    t = calcul(recherche, (T, random.randrange(-1, n)), rep=5)
    for _ in range(rep-1):
        t += calcul(recherche, (T, random.randrange(-1, n)), rep=5)
    return t / rep