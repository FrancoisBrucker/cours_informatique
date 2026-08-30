from dé import Dé

# 1. créer un dé sans paramètre
dé = Dé() 

# 2. afficher à l'écran sa valeur (ça doit être 1)
print(dé.valeur)

# 3. lancer le dé 10 fois et affiche la valeur du dé après chaque lancer
for i in range(10):
   dé.lancer()
   print(dé.texte())