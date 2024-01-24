import time
from exponentiation import puissance_naif, puissance_rapide


correct = False
entier = 0

while not correct:
    correct = True
    chaîne = input('Donnez un entier positif :')
    try:
        entier = int(chaîne)
    except ValueError:
        correct = False
        print("ce n'est pas un nombre. Essayez encore une fois.")
    if entier < 0:
        correct = False
        print("ce n'es`t pas un entier positif. Essayez encore une fois.")


t1 = time.perf_counter()
puissance_naif(3, entier)
t2 = time.perf_counter()

delta = t2 - t1

print("temps mis pour exécuter puissance_naif(3,", entier, ") est",
      delta, "secondes")

t1 = time.perf_counter()
puissance_rapide(3, entier)
t2 = time.perf_counter()

delta = t2 - t1

print("temps mis pour exécuter puissance_rapide(3,", entier, ") est",
      delta, "secondes")
