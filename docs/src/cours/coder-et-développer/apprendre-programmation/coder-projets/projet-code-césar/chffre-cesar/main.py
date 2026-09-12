import texte
from chiffre import césar_chiffre, césar_déchiffre

entrée = input("Tapez une chaîne de caractères en français : ")
texte = texte.conversion(entrée)


clé = input("Tapez une lettre de l'alphabet (clé de chiffrement) : ")
chiffre = césar_chiffre(texte, clé)
déchiffre = césar_déchiffre(chiffre, clé)

print("Texte initial   :", texte)
print("Texte chiffré   :", chiffre)
print("Texte déchiffré :", déchiffre)
