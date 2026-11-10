def sélection(T):
    for i in range(len(T) - 1):
        min_index = i
        for j in range(i + 1, len(T)):
            if T[j] < T[min_index]:
                min_index = j
        T[i], T[min_index] = T[min_index], T[i]


def insertion(T):
    for i in range(1, len(T)):
        courant = T[i]
        j = i
        while (j > 0) and (courant < T[j - 1]):
            T[j] = T[j - 1]
            j -= 1
        T[j] = courant


def bulles(T):
    for i in range(len(T) - 1, 0, -1):
        trié = True
        for j in range(i):
            if T[j + 1] < T[j]:
                T[j + 1], T[j] = T[j], T[j + 1]
                trié = False
        if trié:
            return


def combiner(T1, T2):
    i1 = i2 = 0
    T = []
    while i1 < len(T1) or i2 < len(T2):
        if i2 == len(T2):
            T.append(T1[i1])
            i1 += 1
        elif i1 == len(T1):
            T.append(T2[i2])
            i2 += 1
        elif T1[i1] < T2[i2]:
            T.append(T1[i1])
            i1 += 1
        else:
            T.append(T2[i2])
            i2 += 1
    return T


def fusion(T):
    if len(T) < 2:
        return T
    else:
        milieu = len(T) // 2
        T1 = T[:milieu]
        T2 = T[milieu:]

        T1_trié = fusion(T1)
        T2_trié = fusion(T2)
        T_trié = combiner(T1_trié, T2_trié)

        return T_trié


def rapide(T):
    if len(T) <= 1:
        return T

    pivot = T[0]

    T1 = [T[i] for i in range(1, len(T)) if T[i] <= pivot]
    T2 = [T[i] for i in range(1, len(T)) if T[i] > pivot]

    return rapide(T1) + [pivot] + rapide(T2)
