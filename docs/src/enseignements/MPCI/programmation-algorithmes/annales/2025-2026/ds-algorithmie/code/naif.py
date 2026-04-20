def naïf(a, b):
    for i in range(len(a) - len(b) + 1):
        trouvé = True
        j = 0
        while j < len(b):
            if b[j] != a[i + j]:
                trouvé = False
                j = len(b)
            else:
                j += 1
        if trouvé:
            return i
    return -1


def affiche(a, b):
    i = naïf(a, b)
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

