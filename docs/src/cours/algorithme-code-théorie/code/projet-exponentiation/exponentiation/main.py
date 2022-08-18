import time
from exponentiation import puissance_naif, puissance_rapide


correct = False
entier = 0

while not correct:
    correct = True
    chaine = input('Donnez un entier positif :')
    try:
        entier = int(chaine)
    except ValueError:
        correct = False
        print("ce n'est pas un nombre. Essayez encore une fois.")
    if entier < 0:
        correct = False
        print("ce n'est pas un entier positif. Essayez encore une fois.")


t1 = time.time()
puissance_naif(3, entier)
t2 = time.time()

delta = t2 - t1

print("temps mis pour exécuter 3 puisssance_naif", entier, "est",
      delta, "secondes")

t1 = time.time()
puissance_rapide(3, entier)
t2 = time.time()

delta = t2 - t1

print("temps mis pour exécuter 3 puisssance_rapide", entier, "est",
      delta, "secondes")
