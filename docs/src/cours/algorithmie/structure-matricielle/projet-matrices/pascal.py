

# V1

def binom_matrice(n):

    matrice = []
    
    for i in range(n+1):
        ligne = [0] * (i+1)

        matrice.append(ligne)
        for j in range(i+1):
            if (j == i) or (j == 0):
                ligne[j] = 1
            else:
                précédent = matrice[i-1]
                ligne[j] = précédent[j-1] + précédent[j]

    return matrice


def binom(n, k):
    matrice = binom_matrice(n)

    return matrice[n][k]

for l in binom_matrice(10):
    print(" ".join(str(x).rjust(3) for x in l))
print("nombre 4 parmi 10 :", binom(10, 4))

# V2.1

def ligne_suivante(l):
    l2 = [0] * (len(l) + 1)

    l2[0] = 1
    l2[-1] = 1

    for i in range(1, len(l2)-1):
        l2[i] = l[i] + l[i-1]

    return l2


def binom(n, k):
    l = [0]
    for _ in range(n):
       l = ligne_suivante(l)

    return l[k]

print("nombre 4 parmi 10 :", binom(10, 4))


# V2.2

def ligne_suivante(l, k):
    l2 = [0] * min(k + 1, len(l) + 1)

    l2[0] = 1
    l2[-1] = 1

    for i in range(1, len(l)):
        l2[i] = l[i] + l[i-1]

    return l2

def binom(n, k):
    l = [0]
    for _ in range(n):
       l =ligne_suivante(l, k)

    return l[k]

print("nombre 4 parmi 10 :", binom(10, 4))


# V3

def ligne_suivante(l, n, k):
    for j in range(min(n, k), 0, -1):
        l[j] = l[j] + l[j-1]

def binom(n, k):
    l = [1] * (k+1)

    for j in range(n):
       ligne_suivante(l, j, k)
       print(l)

    return l[k]

print("nombre 4 parmi 10 :", binom(10, 4))