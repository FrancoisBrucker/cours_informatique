from dé import Dé

liste_d = [Dé() for _ in range(5)]

print(liste_d)

for d in liste_d:
    d.lancer()

print(liste_d)
liste_d.sort()
print(liste_d)