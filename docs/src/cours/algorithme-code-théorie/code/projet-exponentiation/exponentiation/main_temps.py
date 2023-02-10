import time
from exponentiation import puissance_naif, puissance_rapide


correct = False
temps = 0

while not correct:
    correct = True
    chaîne = input("Donnez un temps en seconde :")
    try:
        temps = float(chaîne)
    except ValueError:
        correct = False
        print("ce n'est pas un réel. Essayez encore une fois.")
    if temps < 0:
        correct = False
        print("ce n'est pas un réel positif. Essayez encore une fois.")


y = 1

t1 = time.perf_counter()
puissance_naif(3, y)
t2 = time.perf_counter()

delta = t2 - t1

while delta < temps:
    y *= 2

    t1 = time.perf_counter()
    puissance_naif(3, y)
    t2 = time.perf_counter()

    delta = t2 - t1

g = y / 2
d = y

y = (g + d) // 2

while (d - g) > 1:
    t1 = time.perf_counter()
    puissance_naif(3, y)
    t2 = time.perf_counter()

    delta = t2 - t1

    if delta == temps:
        g = d = y
    elif delta < temps:
        g = y
    else:
        d = y

    y = (g + d) // 2
    print(y, d - g, delta)


print("pour exécuter puissance_naif(3, y) en ", temps, "secondes, il faut y = ", y)

t1 = time.perf_counter()
puissance_naif(3, y)
t2 = time.perf_counter()

delta = t2 - t1

print("Temps mis pour exécuter puissance_naif(3,", y, ") est", delta, "secondes")

t1 = time.perf_counter()
puissance_rapide(3, temps)
t2 = time.perf_counter()

delta = t2 - t1

print("temps mis pour exécuter puissance_rapide(3,", temps, ") est", delta, "secondes")
