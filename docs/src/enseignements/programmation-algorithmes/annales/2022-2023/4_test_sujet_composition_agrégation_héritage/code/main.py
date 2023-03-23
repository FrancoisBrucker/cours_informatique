from dés import D6, D20, Somme
# from dés import Somme  # pour la question 2

print("question 1 :")
d6 = D6()
d20 = D20()

print(d6.position(), d20.position())
d6.lancer()
d20.lancer()
print(d6.position(), d20.position())

print("questions 2 et 3 :")

# somme = Somme(d6, d20)  # pour la question 2
somme = d6 + d20

print(somme.position())
somme.lancer()
print(somme.position())

print("question 4 :")

un_d6 = D6()
un_autre_d6 = D6()
un_d20 = D20()

d6_plus_d6_plus_d20 = un_d6 + un_d20 + un_d6
print(d6_plus_d6_plus_d20.position())
d6_plus_d6_plus_d20.lancer()
print(d6_plus_d6_plus_d20.position())

print("question 5 :")

marteau_magique = D6() + 4
print(marteau_magique.position())
marteau_magique.lancer()
print(marteau_magique.position())

print("question 6 :")

les_dés = 3 * (un_d6 + d20)

print(les_dés.position())
les_dés.lancer()
print(les_dés.position())
