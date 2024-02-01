from dé import Dé

# 1. créer un dé sans paramètre
dé = Dé()

# 2. afficher à l'écran sa position (ça doit être 1)
print("Position initiale du dé :", dé.position)

# 3. lancer le dé 10 fois et affiche la position du dé après chaque lancé
for i in range(10):
    print("Lancé numéro :", i + 1, "position : ", dé.lancer().position)
