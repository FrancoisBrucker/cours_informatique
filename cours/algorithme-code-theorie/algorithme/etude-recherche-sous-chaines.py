def sous_chaine_naif(a, b):
    for i in range(len(a) - len(b) + 1):
        trouvé = True
        for j in range(len(b)):
            if b[j] != a[i + j]:
                trouvé = False
        if trouvé:
            return True
    return False


def sous_chaine_naif_2(a, b):
    for i in range(len(a) - len(b) + 1):
        if b == a[i : i + len(b) + 1]:
            return True
    return False


def creation_decalage(mot):
    unicode_max = max(ord(x) for x in mot)
    decalage = []
    for i in range(unicode_max + 1):
        decalage.append(len(mot))

    for i in range(len(mot) - 1):
        decalage[ord(mot[i])] = len(mot) - 1 - i

    return decalage


def suite_algorithme_BMH(a, b):
    decalage = creation_decalage(b)  # à faire

    i = 0
    while i < len(a) - len(b) + 1:
        trouvé = True
        for j in range(len(b) - 1, -1, -1):
            if b[j] != a[i + j]:
                trouvé = False

                i += decalage[ord(a[i + len(b) - 1])]

        if trouvé:
            return True
    return False


# print(sous_chaine_naif_2("aaaaaaab", "ab"))

print(suite_algorithme_BMH("aaaaaaab", "abc"))
