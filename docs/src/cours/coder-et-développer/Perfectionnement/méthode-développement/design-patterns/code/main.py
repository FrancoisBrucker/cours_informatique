from dés import d6, d20


d6 = d6()
d20 = d20()

print(d6.valeur, d20.valeur)
print(d6.lancer().valeur, d20.lancer().valeur)


for _ in range(1000):
    d6.lancer()
    d20.lancer()

print('1000 lancers :', d6.moyenne(), d20.moyenne())

