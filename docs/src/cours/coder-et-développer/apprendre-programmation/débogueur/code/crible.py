def élague(x, crible):
    y = 2 * x
    while y < len(crible):
        crible[y] = False
        y += x


def nouveau_max_premier(ancien_max, crible):
    nouveau_max = ancien_max
    while not crible[nouveau_max]:
        nouveau_max -= 1

    return nouveau_max


def nouveau_min_premier(ancien_min, crible):
    nouveau_min = ancien_min
    while not crible[nouveau_min]:
        nouveau_min += 1

    return nouveau_min


def érathostène(n):
    crible = [True] * (n + 1)
    crible[0] = False
    crible[1] = False

    x = 2
    max_premier = len(crible) - 1

    while x ** x < max_premier:
        élague(x, crible)
        max_premier = nouveau_max_premier(max_premier, crible)

        if x < max_premier:
            x = nouveau_min_premier(x + 1, crible)

    return [i for i in range(len(crible)) if crible[i]]


n = 13

print("Les nombres premiers plus petits que", n, "sont :")
print(érathostène(n))
