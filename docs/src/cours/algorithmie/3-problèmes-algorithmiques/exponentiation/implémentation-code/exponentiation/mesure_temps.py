from time import perf_counter_ns
import gc

import matplotlib.pyplot as plt


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

def affiche_complexité(N, c_1):
    _, ax = plt.subplots(figsize=(20, 5))

    ax.set_title("complexités temporelles")
    ax.set_xlabel("taille du tableau")
    ax.set_ylabel("temps de calcul en ns")

    p1, = ax.plot(N, c_1, 'o-', label="complexité")

    ax.legend(handles=(p1, ))

    plt.show()


def affiche_complexité_2(N, c_1, c_2):
    _, ax = plt.subplots(figsize=(20, 5))

    ax.set_title("complexités temporelles")
    ax.set_xlabel("taille du tableau")
    ax.set_ylabel("temps de calcul en ns")

    p1, = ax.plot(N, c_1, 'o-', label="max naif")
    p2, = ax.plot(N, c_2, 'o-', label="max rapide")
    ax.legend(handles=(p1, p2))

    plt.show()

def affiche_complexité_twinx(N, c_1, c_2):
    _, ax = plt.subplots(figsize=(20, 5))

    ax.set_title("complexités temporelles")
    ax.set_xlabel("taille du tableau")
    ax.set_ylabel("temps de calcul en ns")

    p1, = ax.plot(N, c_1, 'o-', label="max naif")

    ax2 = ax.twinx()
    p2, = ax2.plot(N, c_2, 'o-', label="max rapide", color="orange")
    ax.legend(handles=(p1, p2))

    plt.xscale('log')
    plt.show()