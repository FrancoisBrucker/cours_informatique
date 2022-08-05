def copie(T):
    nouveau = []
    for x in T:
        nouveau.append(x)

    return nouveau


def maximum(T):
    m = 0
    for i in range(len(T)):
        if T[m] < T[i]:
            m = i
    return m


def minimum(T):
    m = 0
    for i in range(len(T)):
        if T[m] > T[i]:
            m = i
    return m


def recherche(T, k):
    max_value = T[maximum(T)]

    T_copie = copie(T)
    for i in range(k - 1):
        min = minimum(T_copie)
        T_copie[min] = max_value + 1

    return minimum(T_copie)


if __name__ == "__main__":
    T = [1, 3, 2, 6, 4, 5]
    for i in range(1, len(T) + 1):
        m = recherche(T, i)
        print(T, i, m, T[m])
