from personnage import Personnage, Guerriere, Magicien

xena = Guerriere(10, 2, 50)
peon = Personnage(5, 1)
gandalf = Magicien(4, 1, 3)

while xena.get_vie() > 0 and peon.get_vie() > 0:
    print("xena : ", xena.get_vie(), " peon : ", peon.get_vie())
    xena.taper(peon)
    peon.taper(xena)


print("xena : ", xena.get_vie(), " peon : ", peon.get_vie())

if xena.get_vie() > 0:
    surviant = xena
else:
    surviant = peon

while surviant.get_vie() > 0:
    print("survivant : ", surviant.get_vie())
    gandalf.lancer_sort(surviant)
