import random

from point_fixe import mu


def doppelganger_valide(T):
    for x in T:
        if (x <= 0) or (x >= len(T)):
            return False
    return True


def doppelganger_entrée(n):
    T = []
    for _ in range(n):
        T.append(random.randrange(1, n))

    return T


# def doppelganger_entrée(n):
#     return [random.randrange(1, n) for _ in range(n)]


def doppelganger_naif(T):
    for i in range(len(T)):
        for j in range(i + 1, len(T)):
            if T[i] == T[j]:
                return T[i]


def doppelganger_tri(T):
    T.sort()
    for i in range(1, len(T)):
        if T[i - 1] == T[i]:
            return T[i]


def doppelganger_bool(T):
    B = [False] * len(T)

    for x in T:
        if B[x]:
            return x
        B[x] = True


def doppelganger_optimal(T):
    return mu(T)
