from dés import D6, D20

d6 = D6()
d20 = D20()

print(d6.position(), d20.position())
d6.lancer()
d20.lancer()
print(d6.position(), d20.position())

somme = d6.somme(d20)

print(somme.position())
somme.lancer()
print(somme.position())


un_d6 = D6()
un_autre_d6 = D6()
un_d20 = D20()

d6_plus_d6_plus_d20 = un_d6.somme(un_d20).somme(un_d6)
print(">", d6_plus_d6_plus_d20.position())
d6_plus_d6_plus_d20.lancer()
print(d6_plus_d6_plus_d20.position())

print(hasattr(un_d6, "position"))

les_dés = un_d6.somme(d20).fois(3)

print(les_dés.position())
les_dés.lancer()
print(les_dés.position())
