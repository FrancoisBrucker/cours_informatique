from dés import d6, d20, Stat, Somme


d_6 = d6()
d_20 = d20()

stat6 = Stat()
d_6.add(stat6)

stat20 = Stat()
d_20.add(stat20)

print(d_6.valeur, d_20.valeur)
print(d_6.lancer().valeur, d_20.lancer().valeur)


for _ in range(1000):
    d_6.lancer()
    d_20.lancer()

print('1000 lancers :', stat6.moyenne(), stat20.moyenne())

somme = 3 * (d6() + 4 + 2 * d20())

print(somme.valeur)
print(somme.lancer().valeur)
