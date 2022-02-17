from pourcentage import pourcent

correct = False
entier = 0

while not correct:
    correct = True
    chaine = input('Donnez un nombre écrit en base 10 :')
    try:
        entier = int(chaine)
    except ValueError:
        correct = False
        print("ce n'est pas un nombre. Essayez encore une fois.")

nombre_binaire = bin(entier)[2:]

print("Votre nombre",
      chaine, "contient ", pourcent(nombre_binaire),
      "pourent de 0 en base 2 (" + nombre_binaire + ").")
