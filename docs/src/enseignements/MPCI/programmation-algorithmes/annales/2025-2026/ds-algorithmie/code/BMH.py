def décalage(b):
    d = {}
    for j in range(len(b) - 1):
        c = b[j]
        d[c] = j

    return d


def BMH(a, b):
    décalé = décalage(b)

    i = 0
    j = len(b) - 1
    while i <= len(a) - len(b):
        if a[i + j] != b[j]:
            if a[i + j] not in décalé:
                i += len(b)
            else:
                i += len(b) - décalé[a[i + j]] - 1
            j = len(b) - 1
        elif j == 0:
            return i
        else:
            j -= 1
    return -1


def affiche(a, b):
    i = BMH(a, b)
    print(i)
    if i > -1:
        print(a)
        print(" " * i + b)
    else:
        print(b, "n'est pas une sous-chaîne de", a)


affiche("ABABAAABABACABCBAB",
        "ABABACA")

affiche("ABABAAABABACABCBAB",
        "ABABABA")

