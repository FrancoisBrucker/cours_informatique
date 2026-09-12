def factorielle(n):
    if n <= 1:
        return n
    else:
        return n * factorielle(n - 1)


n = 10
print(factorielle(n))
