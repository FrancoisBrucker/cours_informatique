from time import perf_counter_ns
import gc

import matplotlib.pyplot as plt
import numpy as np


def calcul(f, f_params, rep=10):
    
    gc_actif = gc.isenabled()
    if gc_actif:
        gc.disable()

    t = None
    for _ in range(rep):
        début = perf_counter_ns()
        f(*f_params)
        fin = perf_counter_ns()

        delta = fin - début
        if (t is None) or (delta < t):
          t = delta

    if gc_actif:
        gc.enable()
    
    return t

def calcul_n_max(f_calcul_temps_complexité, n_min, T_MAX):
    n_max = n_min
    while f_calcul_temps_complexité(n_max) < T_MAX:
        n_max *= 2

    return n_max

def affiche_complexité(N, c_min, c_moy, c_max):
    _, ax = plt.subplots(figsize=(20, 5))

    ax.set_title("complexités temporelles")
    ax.set_xlabel("taille du tableau")
    ax.set_ylabel("temps de calcul en ns")

    p1, = ax.plot(N, c_min, 'o-', label="min")
    p2, = ax.plot(N, c_moy, 'o-', label="moyenne")
    p3, = ax.plot(N, c_max, 'o-', label="max")


    ax.legend(handles=(p1, p2, p3))

    plt.show()

def affiche_complexité_vs_théorique(N, c_mesure, degré):
    _, ax = plt.subplots(figsize=(20, 5))

    ax.set_title("complexités temporelles")
    ax.set_xlabel("taille du tableau")
    ax.set_ylabel("temps de calcul en ns")

    p1, = ax.plot(N, c_mesure, 'o-', label="mesurée")

    coefs = np.polyfit(N, c_mesure, degré)
    c_théorique = np.polyval(coefs, N)


    p2, = ax.plot(N, c_théorique, 'o-', label="théorique")
    ax.legend(handles=(p1, p2))

    plt.show()