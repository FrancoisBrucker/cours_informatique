import random
import time

def affiche(M):
    for l in M:
        print(" ".join(str(x).rjust(3) for x in l))


def création_matrice(n, m):
    return [[0] * m for _ in range(n)]


def extraction_matrice(M, n1, n2, m1, m2):
    return [M[i][m1:m2] for i in range(n1, n2)]

def multiplication_naive(A, B):
    C = création_matrice(len(A), len(B[0]))

    for i in range(len(C)):
        for j in range(len(C[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C


def somme(A, B):
    C = création_matrice(len(A), len(A[0]))
    for i in range(len(C)):
        for j in range(len(C[0])):
            C[i][j] = A[i][j] + B[i][j]
    return C


A = [[1, 2],
     [3, 4],
     [5, 6]]


B = [[1, 2, 3, 4],
     [5, 6, 7, 8]]

C = multiplication_naive(A, B)
affiche(C)

def insertion_matrice(A, M, n, m):
    for i in range(len(A)):
        for j in range(len(A[0])):
            M[n+i][m+j] = A[i][j]


def multiplication_rec(A, B):
    n = len(A)

    if n <= 1:
        return [[A[0][0] * B[0][0]]]
    
    A11 = extraction_matrice(A, 0, n // 2, 0, n // 2)
    A12 = extraction_matrice(A, 0, n //2, n // 2, n)
    A21 = extraction_matrice(A, n // 2, n, 0, n // 2)
    A22 = extraction_matrice(A, n // 2, n, n // 2, n) 

    B11 = extraction_matrice(B, 0, n // 2, 0, n // 2)
    B12 = extraction_matrice(B, 0, n //2, n // 2, n)
    B21 = extraction_matrice(B, n // 2, n, 0, n // 2)
    B22 = extraction_matrice(B, n // 2, n, n // 2, n) 

    C11 = somme(multiplication_rec(A11, B11), multiplication_rec(A12, B21))
    C12 = somme(multiplication_rec(A11, B12), multiplication_rec(A12, B22))
    C21 = somme(multiplication_rec(A21, B11), multiplication_rec(A22, B21))
    C22 = somme(multiplication_rec(A21, B12), multiplication_rec(A22, B22))

    C = création_matrice(n, n)
    insertion_matrice(C11, C, 0, 0)
    insertion_matrice(C12, C, 0, n // 2)
    insertion_matrice(C21, C, n // 2, 0)
    insertion_matrice(C22, C, n // 2, n // 2)

    return C


def matrice_aléatoire(p, v):
    return [[random.randrange(v) for _ in range(2** p)] for _ in range(2 ** p)]

A = matrice_aléatoire(4, 10)
B = matrice_aléatoire(4, 10)
affiche(A)
print("**********")
affiche(B)
print("============")
C = multiplication_naive(A, B)
affiche(C)
C = multiplication_rec(A, B)
print("------------")
affiche(C)
print("============")

def différence(A, B):
    C = création_matrice(len(A), len(A[0]))
    for i in range(len(C)):
        for j in range(len(C[0])):
            C[i][j] = A[i][j] - B[i][j]
    return C

def strassen_rec(A, B):
    n = len(A)

    if n <= 1:
        return [[A[0][0] * B[0][0]]]
    
    A11 = extraction_matrice(A, 0, n // 2, 0, n // 2)
    A12 = extraction_matrice(A, 0, n //2, n // 2, n)
    A21 = extraction_matrice(A, n // 2, n, 0, n // 2)
    A22 = extraction_matrice(A, n // 2, n, n // 2, n) 

    B11 = extraction_matrice(B, 0, n // 2, 0, n // 2)
    B12 = extraction_matrice(B, 0, n //2, n // 2, n)
    B21 = extraction_matrice(B, n // 2, n, 0, n // 2)
    B22 = extraction_matrice(B, n // 2, n, n // 2, n) 

    M1 = strassen_rec(somme(A11, A22), somme(B11, B22))
    M2 = strassen_rec(somme(A21, A22), B11)
    M3 = strassen_rec(A11, différence(B12, B22))
    M4 = strassen_rec(A22, différence(B21, B11))
    M5 = strassen_rec(somme(A11, A12), B22)
    M6 = strassen_rec(différence(A21, A11), somme(B11, B12))
    M7 = strassen_rec(différence(A12, A22), somme(B21, B22))

    C11 = somme(somme(M1, différence(M4, M5)), M7)
    C12 = somme(M3, M5)
    C21 = somme(M2, M4)
    C22 = somme(somme(différence(M1, M2), M3), M6)

    C = création_matrice(n, n)
    insertion_matrice(C11, C, 0, 0)
    insertion_matrice(C12, C, 0, n // 2)
    insertion_matrice(C21, C, n // 2, 0)
    insertion_matrice(C22, C, n // 2, n // 2)

    return C

print("------------")
A = matrice_aléatoire(4, 10)
B = matrice_aléatoire(4, 10)

affiche(différence(multiplication_naive(A, B), strassen_rec(A, B)))
print("============")


for p in range(1, 11):
    A = matrice_aléatoire(p, 10)
    B = matrice_aléatoire(p, 10)
    t1 = time.perf_counter()
    multiplication_naive(A, B)
    t2 = time.perf_counter()
    m1 = t2 - t1

    t1 = time.perf_counter()
    strassen_rec(A, B)
    t2 = time.perf_counter()
    m2 = t2 - t1

    print(2 ** p, "naïf :", m1, "Strassen :", m2, "rapport :", m1/m2)
