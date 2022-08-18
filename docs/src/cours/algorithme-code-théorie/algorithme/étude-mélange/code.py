from random import randint

import matplotlib.pyplot as plt

def aléatoire(T):
    T_prim = []
    for i in range(len(T)):
        T_prim.append(T[randint(0, len(T) - 1)])

    return T_prim

def permutations(T):
    if len(T) == 0:
        return [T]  # la liste contenant toutes les permutation de de T, c'est à dire T

    P = []  # va contenir les permutations de T
    
    for i in range(len(T)):  
        I = [T[i]]
        Pi = permutations(T[:i] + T[i+1:])  # récursion
        for Ti in Pi:
            P.append(I + Ti)
    return P


def mélange(T):
    P = permutations(T)
    i = randint(0, len(P) - 1)
    return P[i]

def compte_mélange(taille_liste, nombre_lancer):
    return compte_mélange_générique(mélange, taille_liste, nombre_lancer)

def compte_mélange_générique(fonction_mélange, taille_liste, nombre_lancer):
    T = list(range(taille_liste))
    P = permutations(T)
    N = [0] * len(P)

    for i in range(nombre_lancer):
        T2 = fonction_mélange(T)
        N[P.index(T2)] += 1
    
    return N

def graphique_mélange_générique(fonction_mélange, taille_tableau, nombre_iteration):

    nombre = compte_mélange_générique(fonction_mélange, taille_tableau, nombre_iteration)

    fig, ax = plt.subplots(figsize=(20, 5))

    ax.set_xlim(0, len(nombre) - 1)
    ax.set_ylim(0, max(nombre) + 1)

    ax.plot(nombre, label="nombre")
    ax.axhline(y=nombre_iteration / len(nombre), color="red", label="théorique")

    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    ax.set_title(str(nombre_iteration) + " permutations d'un tableau à " + str(taille_tableau)+ " éléments")

    plt.show()

def mélange_Knuth(T):
    T2 = list(T)
    for i in range(len(T2) - 1, -1, -1):
        j = randint(0, i)
        T2[i], T2[j] = T2[j], T2[i]
    return T2

def mélange_transposition(T):
    T2 = list(T)
    for k in range(len(T2) - 1):
        i = randint(0, len(T2) - 1)
        j = randint(0, len(T2) - 1)

        T2[i], T2[j] = T2[j], T2[i]
    return T2

# main
# print("\n", "-" * 50, "\n")

# print(list(range(10)), "vs", aléatoire(list(range(10))))

# print("\n", "-" * 50, "\n")

# print("Toutes les permutations à 4 éléments :")
# for P in permutations([1, 2, 3, 4]):
#     print(P)

# print("\n", "-" * 50, "\n")

# nombre = compte_mélange(5, 1000)
# print(min(nombre), sum(nombre) / len(nombre), max(nombre))

# graphique_mélange_générique(mélange, 6, 10000)

# print(mélange_Knuth(list(range(6))))
# graphique_mélange_générique(mélange_Knuth, 6, 10000)

graphique_mélange_générique(mélange_transposition, 6, 10000)
