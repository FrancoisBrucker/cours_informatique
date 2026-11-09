import time

print("Avant l'attente")
x = 1000
t1 = time.perf_counter()
x**x**2
t2 = time.perf_counter()
print("Après l'attente")

delta = t2 - t1

print("Temps d'attente :", delta)

# quit()

min_attente = 0
max_attente = 0
moy_attente = 0

for i in range(10):
    t1 = time.perf_counter()
    x**x**2
    t2 = time.perf_counter()

    delta = t2 - t1

    if max_attente == 0:
        min_attente = max_attente = moy_attente = delta
    else:
        min_attente = min(min_attente, delta)
        max_attente = max(max_attente, delta)
        moy_attente += delta

    print(delta, min_attente, moy_attente / (i + 1), max_attente)

moy_attente /= 10

print(min_attente, moy_attente, max_attente)
