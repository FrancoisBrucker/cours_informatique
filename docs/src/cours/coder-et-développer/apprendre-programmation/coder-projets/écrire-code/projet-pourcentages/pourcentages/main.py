from pourcentage import pourcent

correct = False
entier = 0

while not correct:
    correct = True
    chaîne = input('Donnez un nombre écrit en base 10 :')
    try:
        entier = int(chaîne)
    except ValueError:
        correct = False
        print("ce n'est pas un nombre. Essayez encore une fois.")

nombre_binaire = bin(entier)[2:]

print("Votre nombre",
      chaîne, "contient ", pourcent(nombre_binaire),
      "pourcent de 0 en base 2 (" + nombre_binaire + ").")
