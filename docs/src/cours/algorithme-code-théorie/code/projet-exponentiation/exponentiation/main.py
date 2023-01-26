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


t1 = time.process_time()
puissance_naif(3, entier)
t2 = time.process_time()

delta = t2 - t1

print("temps mis pour exécuter 3 puissance_naif", entier, "est",
      delta, "secondes")

t1 = time.process_time()
puissance_rapide(3, entier)
t2 = time.process_time()

delta = t2 - t1

print("temps mis pour exécuter 3 puissance_rapide", entier, "est",
      delta, "secondes")
