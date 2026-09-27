import json
from num import chiffre_associe

message = json.load(
    open("texte.json", encoding="utf-8"),
    object_hook=lambda d: {int(k): v for k, v in d.items()},
)
s = input("Quel est ton prénom : ")
c = chiffre_associe(s)
print("Ton nombre associé est :", c)
print()
print(message[c])

