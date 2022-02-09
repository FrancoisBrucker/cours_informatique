from dice import Dice

position_initiale = int(input("valeur initiale du dé :"))
position_finale = int(input("position finale du dé :"))

nombre_lancer = 0
de = Dice(position_initiale)

while position_finale != de.get_position():
    de.roll()
    nombre_lancer += 1

print("Il a fallut : ", nombre_lancer, "lacers")
