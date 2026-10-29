import mesure_temps

def recherche(T, x):
    for e in T:
        if e == x:
            return True
    return False

T = list(range(100))


t = mesure_temps.calcul(recherche, (T, 42))

print("l'exécution de la fonction à duré :", t, "ns")
