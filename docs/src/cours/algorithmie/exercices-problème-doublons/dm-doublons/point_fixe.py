
def lièvre_tortue(T):
    x = 0

    tortue = T[x]
    lièvre = T[T[x]]

    while tortue != lièvre:
        tortue = T[tortue]
        lièvre = T[T[lièvre]]

    return tortue


def mu(T):
    x = lièvre_tortue(T)

    tortue = T[x]
    tortue2 = T[0]

    while tortue != tortue2:
        tortue = T[tortue]
        tortue2 = T[tortue2]

    return tortue
