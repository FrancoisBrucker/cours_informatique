import time

print("Avant l'attente")
t1 = time.time()
time.sleep(1)
t2 = time.time()
print("Après l'attente")

delta = t2 - t1

print("Temps d'attente :", delta)

min_attente = 0
max_attente = 0
moy_attente = 0

for i in range(10):
    t1 = time.time()
    time.sleep(2)
    t2 = time.time()

    delta = t2 - t1

    if max_attente == 0:
        min_attente = max_attente = moy_attente = delta
    else:
        min_attente = min(min_attente, delta)
        max_attente = max(max_attente, delta)
        moy_attente += delta

    print(delta, min_attente, moy_attente / (i+1), max_attente)

moy_attente /= 10

print(min_attente, moy_attente, max_attente)
