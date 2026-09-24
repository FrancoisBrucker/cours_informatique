from dés import d6, d20, Stat


d6 = d6()
d20 = d20()

stat6 = Stat()
d6.add(stat6)

stat20 = Stat()
d20.add(stat20)

print(d6.valeur, d20.valeur)
print(d6.lancer().valeur, d20.lancer().valeur)


for _ in range(1000):
    d6.lancer()
    d20.lancer()

print('1000 lancers :', stat6.moyenne(), stat20.moyenne())

