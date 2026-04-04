import time

def échiquier(n):
    E = []
    for _ in range(n):
        E.append([False] * n)
    return E

def affiche(E):
    print()
    for l in E:
        print(" ".join((x and "♕" or "▢") for x in l))
    print()

affiche(échiquier(10))

def position_correcte(E, i, j):
    n = len(E)

    for k in range(n):
        if (k != i) and E[k][j]:
            return False

    for k in range(n):
        if (k != j) and E[i][k]:
            return False

    for k in range(1, n):
        if (i + k < n) and (j + k < n) and E[i + k][j + k]:
            return False
        if (i + k < n) and (j - k > -1) and E[i + k][j - k]:
            return False
        if (i - k > -1) and (j + k < n) and E[i - k][j + k]:
            return False
        if (i - k > -1) and (j - k > -1) and E[i - k][j - k]:
            return False
        
    return True

E = échiquier(8)
print(position_correcte(E, 4, 6))
E = échiquier(8)
E[4][6] = True
print(position_correcte(E, 4, 6))
print(position_correcte(E, 4, 7))

def échiquier_correct(E):
    n = len(E)

    for i in range(n):
        for j in range(n):
            if E[i][j] and not position_correcte(E, i, j):
                return False
        
    return True


E = échiquier(8)
E[4][6] = True
print(échiquier_correct(E))
E[4][7] = True
print(échiquier_correct(E))

# V1 : on pose toutes les reines et on vérifie

n = 6

def tous_les_échiquiers_rec(E, i=0):
    n = len(E)

    if i == n:
        if échiquier_correct(E):
            affiche(E)
        return
    for j in range(n):
        E[i][j] = True
        tous_les_échiquiers_rec(E, i+1)
        E[i][j] = False

t1 = time.perf_counter()
tous_les_échiquiers_rec(échiquier(n))
t2 = time.perf_counter()
delta = t2 - t1

print("Temps d'exécution :", delta * 1000)



# V2 : on pose les reines une à une

def tous_les_échiquiers_rec(E, i=0):
    n = len(E)

    if i == n:
        affiche(E)
        return
    for j in range(n):
        
        if position_correcte(E, i, j):
            E[i][j] = True
            tous_les_échiquiers_rec(E, i+1)
            E[i][j] = False

t1 = time.perf_counter()
tous_les_échiquiers_rec(échiquier(n))
t2 = time.perf_counter()
delta = t2 - t1

print("Temps d'exécution :", delta  * 1000)



# Permutations

def permutation_correcte(P, i):
    n = len(P)

    for k in range(i):
        if (0 <= P[i] - i + k < n) and (P[i] - i + k == P[k]):
            return False
        if (0 <= P[i] + i - k < n) and (P[i] + i - k == P[k]):
            return False
        
    return True


def affiche_permutation(P):
    E = échiquier(len(P))
    for i in range(len(P)):
        E[i][P[i]] = True
    affiche(E)

def toutes_les_permutations_rec(P, i=0):
    n = len(P)

    if i == n:
        affiche_permutation(P)
        return
    for j in range(i, n):
        P[i], P[j] = P[j], P[i]
        if permutation_correcte(P, i):
            toutes_les_permutations_rec(P, i+1)
        P[i], P[j] = P[j], P[i]


t1 = time.perf_counter()
toutes_les_permutations_rec(list(range(n)))
t2 = time.perf_counter()
delta = t2 - t1

print("Temps d'exécution :", delta  * 1000)


