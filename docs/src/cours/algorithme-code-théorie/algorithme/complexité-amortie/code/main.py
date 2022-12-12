def successeur(N):
    i = len(N) - 1

    while i >= 0 and (N[i] == 1):
        N[i] = 0
        i -= 1

    if i >= 0:
        N[i] = 1

    return len(N) - i


def tous(n):

    N = [0] * n
    total = 0
    for i in range(2**n):
        total += successeur(N)
        print(N)

    return total / 2**n


x = tous(5)
print(x)
