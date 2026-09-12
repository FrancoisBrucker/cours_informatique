
import csv

f = open("laposte_hexasmal.csv", "r")
lecteur = csv.reader(f, delimiter=";")

compte = dict()
for ligne in lecteur:
    departement = ligne[2][:-3]
    print(ligne, departement)

    if ligne[2][:-3] not in compte:
        compte[departement] = 1
    else:
        compte[departement] += 1

    if ligne[1] == 'OTTERSWILLER':
        print(ligne)

departements = list(compte.keys())
departements.sort(key=lambda x: compte[x])
for dep in departements:
    print(dep, compte[dep])
