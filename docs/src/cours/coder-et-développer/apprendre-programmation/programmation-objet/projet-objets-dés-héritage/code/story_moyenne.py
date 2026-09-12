from dés import D6, D20


d6 = D6()
d20 = D20()

for _ in range(1000):
    d6.lancer()
    d20.lancer()

print('1000 lancers :', d6.moyenne(), d20.moyenne())
