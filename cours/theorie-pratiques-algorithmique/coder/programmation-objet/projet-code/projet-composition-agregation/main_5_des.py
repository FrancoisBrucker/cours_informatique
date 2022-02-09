from dice import Dice

les_des = []
for i in range(5):
    les_des.append(Dice())

for d in les_des:
    d.roll()

for d in les_des:
    print(d)
