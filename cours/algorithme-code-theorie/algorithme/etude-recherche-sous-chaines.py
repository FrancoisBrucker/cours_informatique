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

# print(suite_algorithme_BMH("aaaaaaab", "abc"))

def algo_naif_construction_t(b):
    T_b = []

    for j in range(1, len(b)):
        T_b.append(0)
        chaîne = b[1:j]
        for k in range(len(chaîne)):
            if b[:k] == chaîne[-k:]:
                T_b[-1] = k

    return T_b

# print(algo_naif_construction_t("ACGAGACGACT"))



def cree_tableau(b):
    T_b = [0]

    j = len(T_b) + 1
    c = b[j-1]

    while len(T_b) < len(b) - 1:
        k = T_b[j-2]

        if c == b[k]:
            T_b.append(k + 1)
                        
            j = len(T_b) + 1
            c = b[j-1]
        elif k <= 1:
                T_b.append(0)

                j = len(T_b) + 1
                c = b[j-1]
        else:
            j = k + 1

    return T_b

print(cree_tableau("ACGAGACGACT"))

def sous_chaine_KMP(a, b):
    # Tb = cree_tableau(b)
    Tb = [0, 0, 1, 2, 0]

    i = 0
    j = 0

    while i + j < len(a):
        if a[i + j] == b[j]:
            j += 1

            if j >= len(b):
                return True

        else:
            if j == 0:
                i += 1
            else:
                l = j - Tb[j - 1]
                i += l
                j -= l
    return False


# print(sous_chaine_KMP("ATATATATATCGGGAA", "ATATCG"))
