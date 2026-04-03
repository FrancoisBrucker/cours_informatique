def échiquier(n):
    E = []
    for _ in range(n):
        E.append([False] * n)
    return E

for l in échiquier(10):
    print(" ".join(str(x) for x in l))


def position_correcte(E, i, j):
    n = len(E[0])

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
    n = len(E[0])

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
