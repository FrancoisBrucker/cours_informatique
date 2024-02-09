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


delta = 0
K = 0
n = 1

while delta < temps:
    t1 = time.perf_counter()
    puissance_naif(3, n)
    t2 = time.perf_counter()

    delta = t2 - t1
    K += 1
    n *= 2


print("pour exécuter puissance_naif(3, y) en ", temps, "secondes, il faut K = ", K)

t1 = time.perf_counter()
puissance_naif(3, 2 ** K)
t2 = time.perf_counter()

delta = t2 - t1

print("Temps mis pour exécuter puissance_naif(3, 2 ** ", K, ") est", delta, "secondes")

t1 = time.perf_counter()
puissance_rapide(3, temps)
t2 = time.perf_counter()

delta = t2 - t1

print("temps mis pour exécuter puissance_rapide(3,", temps, ") est", delta, "secondes")
