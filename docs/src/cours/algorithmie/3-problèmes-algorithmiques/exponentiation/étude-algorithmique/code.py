from math import log2


def puissance_naif_rec(nombre, exposant):
    if exposant == 1:
        return nombre
    return nombre * puissance_naif_rec(nombre, exposant - 1)


def puissance_naif_iter(nombre, exposant):
    résultat = nombre
    compteur = exposant - 1
    while compteur > 0:
        résultat *= nombre
        compteur -= 1
    return résultat


def puissance_indienne_rec(nombre, exposant):
    if exposant == 1:
        return nombre
    elif exposant % 2 != 0:
        return nombre * puissance_indienne_rec(nombre, exposant - 1)
    else:
        return nombre * nombre * puissance_indienne_rec(nombre, exposant // 2)


def puissance_indienne_iter(nombre, exposant):
    résultat = nombre
    compteur = exposant - 1

    while compteur > 0:
        if compteur % 2 != 0:
            résultat *= nombre
            compteur -= 1
        else:
            nombre *= nombre
            compteur /= 2

    return résultat


print("naif rec", puissance_naif_rec(2, 7))
print("naif iter", puissance_naif_iter(2, 7))
print("indienne rec", puissance_indienne_rec(2, 7))
print("indienne iter", puissance_indienne_iter(2, 7))


def indienne_suite(x, n):
    a = [x]
    y = a[-1] * a[-1]
    while y < x ** n:
        a.append(y)
        y = a[-1] * a[-1]

    c = n-1
    i = 0
    r = a[i]
    while c > 0:
        # print(a, i, c)
        if c % 2 != 0:
            r = r * a[i]
            a.append(r)
            c = c - 1
        else:
            i = i + 1
            c = c / 2
    return a


print(indienne_suite(2, 10), int(log2(10)), bin(10 - 1))
print(indienne_suite(2, 15), int(log2(15)), bin(15 - 1))
