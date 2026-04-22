def décalage_BMH(b):
    d = {}
    for j in range(len(b) - 1):
        c = b[j]
        d[c] = len(b) - j - 1

    return d


def BMH(a, b):
    décalé = décalage_BMH(b)

    i = 0
    j = len(b) - 1
    while i <= len(a) - len(b):
        if a[i + j] != b[j]:
            i += décalé.get(a[i + j], len(b))
            j = len(b) - 1
        elif j == 0:
            return i
        else:
            j -= 1
    return -1


