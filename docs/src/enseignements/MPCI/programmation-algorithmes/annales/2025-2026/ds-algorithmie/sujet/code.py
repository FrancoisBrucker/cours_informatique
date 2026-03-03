def décalage(b):
    T_b = [0] * len(b)

    i, j, k = 2, 2, 0
    c = b[j-1]

    while i < len(b):
        k = T_b[j-1]

        if c == b[k]:      
            T_b[i] = k + 1
            i += 1
            j = i
            c = b[j-1]
        elif k <= 1:
            T_b[i] = 0
            i += 1
            j = i
            c = b[j-1]
        else:
            j = k + 1

    return T_b

def sous_chaîne_KMP(a, b):
    Tb = décalage(b)
    
    i = 0
    j = 0

    while i + j < len(a):
        if a[i + j] == b[j]:
            j += 1

            if j >= len(b):
                return i

        else:
            if j == 0:
                i += 1
            else :
                l = j - Tb[j]
                i += l
                j -= l
    return -1

# print(décalage2("ABABACA"))
print(décalage("ABABACA"))
print(sous_chaîne_KMP("ABABAAABABACABCBAB", "ABABACA"))